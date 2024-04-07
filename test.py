from main import clean_text
import re
def test_clean_text():
    # Тестирование замены имен и фамилий
    assert clean_text("John Doe") == "[censored]"

    # Тестирование замены номеров телефонов
    assert clean_text("Phone: +78881231213") == "[censored]"

    # Тестирование замены геолокации
    assert clean_text("IP Address: 192.168.1.1") == "[censored]"

    print("All tests passed successfully!")

if __name__ == "__main__":
    test_clean_text()