import unittest
import xml.etree.ElementTree as ET
import os
from unittest.mock import patch
from io import StringIO
import httpx

# Импортируем функции из основного task
from task import download, count_cars, middle_price, find_Ford, min_price_Toyota_Hilux

class TestCarFunctions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Создаем тестовый XML-файл перед запуском всех тестов.
        """
        cls.test_xml_data = '''
        <cars>
            <car>
                <maker>Ford</maker>
                <model>Mustang</model>
                <year>2015</year>
                <price>30000</price>
            </car>
            <car>
                <maker>Toyota</maker>
                <model>Hilux</model>
                <year>2018</year>
                <price>25000</price>
            </car>
            <car>
                <maker>Ford</maker>
                <model>Focus</model>
                <year>2015</year>
                <price>20000</price>
            </car>
        </cars>
        '''
        with open('test_cars.xml', 'w') as f:
            f.write(cls.test_xml_data)

    @classmethod
    def tearDownClass(cls):
        """
        Удаляем тестовый XML-файл после завершения всех тестов.
        """
        if os.path.exists('test_cars.xml'):
            os.remove('test_cars.xml')

def test_count_cars(self):
    """
    Тест для функции count_cars.
    """
    with patch('sys.stdout', new=StringIO()) as fake_out:
        count_cars('test_cars.xml')
        self.assertIn("Всего автомобилей в каталоге: 3", fake_out.getvalue())

def test_middle_price(self):
    """
    Тест для функции middle_price.
    """
    with patch('sys.stdout', new=StringIO()) as fake_out:
        middle_price('test_cars.xml')
        self.assertIn("Средняя цена автомобилей: 25000.0 USD", fake_out.getvalue())

def test_find_Ford(self):
    """
    Тест для функции find_Ford.
    """
    with patch('sys.stdout', new=StringIO()) as fake_out:
        find_Ford('test_cars.xml')
        self.assertIn("Ford 2015 года выпуска в каталоге: 2", fake_out.getvalue())

def test_min_price_Toyota_Hilux(self):
    """
    Тест для функции min_price_Toyota_Hilux.
    """
    with patch('sys.stdout', new=StringIO()) as fake_out:
        min_price_Toyota_Hilux('test_cars.xml')
        self.assertIn("Минимальная цена Toyota Hilux: 25000 USD", fake_out.getvalue())
        self.assertIn("Год выпуска: 2018", fake_out.getvalue())
@patch('httpx.Client')
def test_download(self, mock_client):
    """
    Тест для функции download.
    """
    mock_response = unittest.mock.Mock()
    mock_response.status_code = 200
    mock_response.content = self.test_xml_data.encode()
    mock_client.return_value.get.return_value = mock_response

    with patch('sys.stdout', new=StringIO()) as fake_out:
        download()
        self.assertIn("Файл успешно скачан.", fake_out.getvalue())

    # Проверяем, что файл был создан
    self.assertTrue(os.path.exists('cars.xml'))

if __name__ == '__main__':
    unittest.main()