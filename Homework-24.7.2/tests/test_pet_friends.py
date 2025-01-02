from api import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password
import os

pf = PetFriends()

def test_get_api_key_for_valid_user (email=valid_email, password=valid_password):
    """1) Проверяем возможность получения ключа с корректными данными"""

    # Получаем ключ - auth_key
    status, result = pf.get_api_key(email, password)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert 'key' in result

def test_get_all_pets_with_valid_key(filter=''):
    """2) Проверяем что можно получить информацию о всех питомцах с корректным ключём"""

    # Получаем ключ - auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Получаем список питомцев
    status, result = pf.get_list_of_pets(auth_key,filter)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert len(result['pets']) > 0

def test_add_new_pet_with_valid_data(name='Маня', animal_type='Тайская',  age='5', pet_photo='images/cat1.jpg'):
    """3) Проверяем что можно добавить питомца с корректными данными"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

def test_successful_delete_self_pet():
    """4) Проверяем возможность удаления питомца"""

    # Получаем ключ - auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Маня", "Тайская", "8", "images/cat1.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Ещё раз запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in my_pets.values()

def test_successful_update_self_pet_info(name='Маня', animal_type='Тайская', age=13):
    """5) Проверяем возможность обновления информации о питомце"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Еслди список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status == 200
        assert result['name'] == name
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("Список питомцев пуст")

def test_add_new_pet_without_photo_with_valid_data(name='Маня', animal_type='Тайская',  age='5'):
    """6) Проверяем что можно добавить питомца с корректными данными без фото"""

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

def test_successful_add_self_pet_photo(pet_photo='images/cat2.jpg'):
    """7) Проверяем возможность обновления фото питомца"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']

    # Еслди список не пустой, то пробуем обновить его фото
    if len(my_pets['pets']) > 0:
        status, result = pf.add_pet_photo(auth_key, pet_id, pet_photo)
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

        # Проверяем что статус ответа = 200 и фото соответствует заданному
        assert status == 200
        assert result['pet_photo'] == my_pets['pets'][0]['pet_photo']

    # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
    else:
        raise Exception('Список питомцев пуст')

def test_get_api_key_for_invalid_user(email=invalid_email, password=invalid_password):
    """8) Проверяем возможность получения ключа с некорректными данными"""

    # Пытаеся получить ключ - auth_key
    status, result = pf.get_api_key(email, password)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400 or 401 or 402 or 403 or 404 or 405

def test_add_new_pet_with_invalid_data(name='', animal_type='Тайская',  age='5', pet_photo='images/cat1.jpg'):
    """9) Проверяем что можно добавить питомца с корректными данными, но с пустым именем"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key и добавляем питомца
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400 or 401 or 402 or 403 or 404 or 405

def test_add_new_pet_without_photo_with_valid_data(name='Фалвтаывтаылвдатдылвтадывлталдывталдывтадлытмючясмьвжальажзцущьааяюьмюь', animal_type='Тайская',  age='5'):
    """10) Проверяем что можно добавить питомца с корректными данными без фото, но с слишком длинным name"""

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    # Добавляем питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400 or 401 or 402 or 403 or 404 or 405