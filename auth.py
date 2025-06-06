# Задача 1: Обфускация исходного кода с помощью PyArmor

## Шаги:

### 1. Установка PyArmorpip install pyarmor

### 2. Обфускация файла auth.py
pyarmor gen -O dist auth.py
- -O dist — указывает папку для сохранения обфусцированного кода.
- После выполнения команда создаст папку dist/outpus, где будет находиться преобразованный файл.

### 3. Проверка результата
- Перейдите в папку dist/outpus и откройте файл auth.py. Он будет выглядеть как нечитаемый, зашифрованный или запутанный код.


# Задача 2: Упаковка и шифрование исходного файла

## 1. Создание защищённого исполняемого файла с PyInstaller

### Установка PyInstallerpip install pyinstaller

### Создание файлаpyinstaller --onefile --key=MySecretKey auth.py
- --onefile — создаёт один исполняемый файл.
- --key=MySecretKey — добавляет симметричное шифрование для защиты кода.

### Проверка
- В папке dist появится файл auth.exe (или auth на Linux/Mac).
- Попробуйте запустить его и убедиться, что он работает.


## 2. Анализ защиты

- Uncompyle6: попробуйте декомпилировать .pyc файл, чтобы проверить, насколько легко восстановить исходный код.pip install uncompyle6
uncompyle6 dist/auth.pyc

- Ghidra: используйте для анализа бинарного файла, чтобы понять, насколько хорошо защищён код.

  
## 3. Усиление защиты: шифрование строк

### Внедрение шифрования строк в коде
from cryptography.fernet import Fernet

# Генерация ключа
key = Fernet.generate_key()
cipher = Fernet(key)

# Шифрование пароля
enc_password = cipher.encrypt(b"Admin@2024")

# Расшифровка и проверка
def check_password(input_pwd):
    real_pwd = cipher.decrypt(enc_password).decode()
    return input_pwd == real_pwd

# Итоговая структура кода с шифрованием строк
from cryptography.fernet import Fernet

# Генерация ключа (лучше сохранить его отдельно)
key = b'ваш_ключ_здесь'  # вставьте свой ключ
cipher = Fernet(key)

# Зашифрованный пароль
enc_password = b'ваши_зашифрованные_данные'

def check_password(input_pwd):
    real_pwd = cipher.decrypt(enc_password).decode()
    return input_pwd == real_pwd
