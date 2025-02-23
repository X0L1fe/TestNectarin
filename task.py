import httpx
import xml.etree.ElementTree as ET

FILE = "https://strategic.nectarin.ru/test_tasks/cars.xml"
"""
При пинге с Postman получил такой токен авторизации    
"""
AUTH = 'Basic dGVzdF9weXRob246dGFzaw=='
MENU = True
# XML структура:
# maker - Марка
# model - Модель автомобиля
# year - Год выпуска
# color - Цвет кузова
# engine - Объем двигателя
# price - Цена, USD

def download():
    """
    Скачивает XML-файл
    """
    try:
        with httpx.Client() as client:
            headers = {
                'Authorization': AUTH
                }
            response = client.get(
                FILE,
                headers=headers
            )

        if response.status_code == 200:
            with open('cars.xml', 'wb') as f:
                f.write(response.content)
            print("Файл успешно скачан.")
        else:
            print(f"Ошибка при скачивании. \n {response.text} \n {response.status_code}")
    except httpx.RequestError as e:
        print (f'Ошибка: {str(e)}')   

def count_cars(file_path='cars.xml'):
    """
    Сколько всего автомобилей содержится в каталоге
    """
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        # каждый автомобиль представлен элементом <car>
        cars = root.findall('car')
        print(f"Всего автомобилей в каталоге: {len(cars)}")
    except FileNotFoundError:
        print("Файл cars.xml не найден.")
    except Exception as e:
        print(f"Ошибка при обработке XML: {str(e)}")

def middle_price():
    """
    Найти среднюю цену автомобилей
    """
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        prices = []
        # каждый автомобиль представлен элементом <car>
        for car in root.findall('car'):
            price = float(car.find('price').text)
            prices.append(price)
        print(f"Средняя цена автомобилей: {sum(prices) / len(prices)} USD")
    except FileNotFoundError:
        print("Файл cars.xml не найден.")
    except Exception as e:
        print(f"Ошибка при обработке XML: {str(e)}")
    

def find_Ford():
    """
    Сколько автомобилей Ford 2015 года выпуска в каталоге
    """
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        count = 0
        for car in root.findall('car'):
            maker = car.find('maker').text
            year = int(car.find('year').text)
            if maker == 'Ford' and year == 2015:
                count += 1
        print(f"Ford 2015 года выпуска в каталоге: {count}")
    except FileNotFoundError:
        print("Файл cars.xml не найден.")
    except Exception as e:
        print(f"Ошибка при обработке XML: {str(e)}")
        

def min_price_Toyota_Hilux():
    """
    Найти автомобиль с минимальной ценой Toyota Hilux в каталоге
    И какой год выпуска будет
    """
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        min_price = float('inf')
        min_car = None
        for car in root.findall('car'):
            maker = car.find('maker').text
            model = car.find('model').text
            price = float(car.find('price').text)
            if maker == 'Toyota' and model == 'Hilux' and price < min_price:
                min_price = price
                min_car = car
        if min_car:
            print(f"Минимальная цена Toyota Hilux: {min_car.find('price').text} USD\nГод выпуска: {min_car.find('year').text}")
        else:
            print("Автомобиль Toyota Hilux не найден.")
    except FileNotFoundError:
        print("Файл cars.xml не найден.")
    except Exception as e:
        print(f"Ошибка при обработке XML: {str(e)}")

while MENU == True:
    print("""
          Меню:
          [1] Скачать XML-файл
          [2] Посчитать количество автомобилей
          [3] Найти среднюю цену автомобилей
          [4] Найти автомобиль Ford 2015 года выпуска
          [5] Найти автомобиль с минимальной ценой Toyota Hilux
          [6] Выйти
          """)
    choice = input("Выберите пункт меню: ")
    
    if choice == '1':
        download()
    elif choice == '2':
        count_cars()
    elif choice == '3':
        middle_price()
    elif choice == '4':
        find_Ford()
    elif choice == '5':
        min_price_Toyota_Hilux()
    elif choice == '6':
        MENU = False
    else:
        print("Неверный ввод. Попробуйте снова.")