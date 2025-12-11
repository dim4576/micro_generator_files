"""
Скрипт для генерации тестовых файлов, папок и подпапок
для тестирования backup_manager
"""
import os
import random
import string
from pathlib import Path
from datetime import datetime, timedelta
import time

def generate_random_string(length=8):
    """Генерирует случайную строку"""
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def generate_hash_string():
    """Генерирует строку, похожую на хэш (MD5, SHA1, SHA256)"""
    hash_types = ['md5', 'sha1', 'sha256', 'sha512']
    hash_type = random.choice(hash_types)
    hash_length = {'md5': 32, 'sha1': 40, 'sha256': 64, 'sha512': 128}[hash_type]
    return ''.join(random.choices(string.hexdigits.lower(), k=hash_length))

def generate_timestamp():
    """Генерирует случайную дату в прошлом"""
    days_ago = random.randint(0, 90)
    hours_ago = random.randint(0, 23)
    minutes_ago = random.randint(0, 59)
    
    dt = datetime.now() - timedelta(days=days_ago, hours=hours_ago, minutes=minutes_ago)
    return dt

def generate_backup_filename():
    """Генерирует имя файла бэкапа"""
    patterns = [
        f"backup_{generate_timestamp().strftime('%Y%m%d_%H%M%S')}.bak",
        f"backup_{generate_timestamp().strftime('%Y-%m-%d')}.zip",
        f"db_backup_{generate_timestamp().strftime('%Y%m%d')}.sql",
        f"backup_{generate_random_string(6)}_{generate_timestamp().strftime('%Y%m%d')}.tar.gz",
        f"backup_{generate_timestamp().strftime('%Y%m%d_%H%M%S')}.7z",
        f"backup_{generate_timestamp().strftime('%Y-%m-%d_%H-%M-%S')}.rar",
        f"backup_{generate_timestamp().strftime('%Y%m%d')}.dump",
        f"backup_{generate_random_string(4)}.bak",
        f"backup_{generate_timestamp().strftime('%Y%m%d')}_{generate_random_string(4)}.zip",
    ]
    return random.choice(patterns)

def generate_log_filename():
    """Генерирует имя файла лога"""
    patterns = [
        f"app_{generate_timestamp().strftime('%Y-%m-%d')}.log",
        f"application_{generate_timestamp().strftime('%Y%m%d')}.log",
        f"error_{generate_timestamp().strftime('%Y-%m-%d')}.log",
        f"access_{generate_timestamp().strftime('%Y%m%d')}.log",
        f"debug_{generate_timestamp().strftime('%Y-%m-%d_%H%M%S')}.log",
        f"server_{generate_timestamp().strftime('%Y%m%d')}.log",
        f"app.log.{generate_timestamp().strftime('%Y%m%d')}",
        f"app.log.{generate_timestamp().strftime('%Y-%m-%d')}",
        f"log_{generate_timestamp().strftime('%Y%m%d_%H%M%S')}.txt",
        f"system_{generate_timestamp().strftime('%Y-%m-%d')}.log",
        f"application_{generate_timestamp().strftime('%Y-%m-%d')}_{generate_random_string(3)}.log",
    ]
    return random.choice(patterns)

def generate_checksum_filename():
    """Генерирует имя файла хэшсуммы"""
    patterns = [
        f"file_{generate_random_string(6)}.md5",
        f"checksum_{generate_random_string(8)}.sha1",
        f"{generate_random_string(10)}.sha256",
        f"hash_{generate_timestamp().strftime('%Y%m%d')}.md5",
        f"checksums_{generate_timestamp().strftime('%Y%m%d')}.txt",
        f"file_{generate_random_string(8)}.sha512",
        f"MD5SUMS",
        f"SHA1SUMS",
        f"SHA256SUMS",
        f"checksum_{generate_random_string(6)}.hash",
    ]
    return random.choice(patterns)

def generate_temp_filename():
    """Генерирует имя временного файла"""
    patterns = [
        f"tmp_{generate_random_string(8)}.tmp",
        f"temp_{generate_timestamp().strftime('%Y%m%d_%H%M%S')}.tmp",
        f"~{generate_random_string(6)}.tmp",
        f"temp_{generate_random_string(10)}.temp",
        f"tmp_{generate_timestamp().strftime('%Y%m%d')}_{generate_random_string(4)}.tmp",
    ]
    return random.choice(patterns)

def generate_archive_filename():
    """Генерирует имя архива"""
    patterns = [
        f"archive_{generate_timestamp().strftime('%Y%m%d')}.zip",
        f"archive_{generate_timestamp().strftime('%Y-%m-%d')}.tar.gz",
        f"archive_{generate_random_string(6)}.7z",
        f"archive_{generate_timestamp().strftime('%Y%m%d_%H%M%S')}.rar",
        f"old_files_{generate_timestamp().strftime('%Y%m%d')}.zip",
        f"archive_{generate_timestamp().strftime('%Y-%m-%d')}.tar",
    ]
    return random.choice(patterns)

def generate_database_filename():
    """Генерирует имя файла базы данных"""
    patterns = [
        f"database_{generate_timestamp().strftime('%Y%m%d')}.sql",
        f"db_backup_{generate_timestamp().strftime('%Y-%m-%d_%H%M%S')}.sql",
        f"dump_{generate_timestamp().strftime('%Y%m%d')}.sql.gz",
        f"db_{generate_random_string(6)}_{generate_timestamp().strftime('%Y%m%d')}.sql",
        f"backup_db_{generate_timestamp().strftime('%Y%m%d')}.dump",
    ]
    return random.choice(patterns)

def generate_snapshot_filename():
    """Генерирует имя файла снимка"""
    patterns = [
        f"snapshot_{generate_timestamp().strftime('%Y%m%d_%H%M%S')}.snap",
        f"snapshot_{generate_timestamp().strftime('%Y-%m-%d')}.img",
        f"snap_{generate_random_string(6)}_{generate_timestamp().strftime('%Y%m%d')}.snapshot",
        f"snapshot_{generate_timestamp().strftime('%Y%m%d')}.vhd",
    ]
    return random.choice(patterns)

def generate_misc_filename():
    """Генерирует другие типы файлов"""
    patterns = [
        f"old_{generate_random_string(8)}.old",
        f"copy_{generate_timestamp().strftime('%Y%m%d')}_{generate_random_string(4)}.copy",
        f"backup_{generate_random_string(6)}.bak",
        f"file_{generate_timestamp().strftime('%Y%m%d_%H%M%S')}.dat",
        f"data_{generate_random_string(8)}.data",
        f"export_{generate_timestamp().strftime('%Y%m%d')}.csv",
        f"export_{generate_timestamp().strftime('%Y-%m-%d')}.json",
    ]
    return random.choice(patterns)

def generate_folder_name():
    """Генерирует имя папки"""
    patterns = [
        f"backup_{generate_timestamp().strftime('%Y%m%d')}",
        f"backup_{generate_timestamp().strftime('%Y-%m-%d')}",
        f"backup_{generate_random_string(6)}",
        f"old_backups_{generate_timestamp().strftime('%Y%m%d')}",
        f"archive_{generate_timestamp().strftime('%Y%m%d')}",
        f"logs_{generate_timestamp().strftime('%Y-%m-%d')}",
        f"temp_{generate_random_string(8)}",
        f"backup_{generate_timestamp().strftime('%Y%m%d_%H%M%S')}",
        f"snapshot_{generate_timestamp().strftime('%Y%m%d')}",
        f"old_{generate_random_string(6)}",
    ]
    return random.choice(patterns)

def create_file_with_timestamp(file_path, dt):
    """Создает файл с заданной датой модификации"""
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Создаем файл с небольшим содержимым
    content = f"Test file generated at {datetime.now()}\n"
    content += f"Original timestamp: {dt}\n"
    content += f"Random data: {generate_random_string(50)}\n"
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    # Устанавливаем дату модификации
    timestamp = dt.timestamp()
    os.utime(file_path, (timestamp, timestamp))

def generate_files(base_path, num_files=50, num_folders=10, max_depth=3, current_depth=0):
    """Генерирует файлы и папки в указанной директории"""
    base_path = Path(base_path)
    base_path.mkdir(parents=True, exist_ok=True)
    
    print(f"Генерация файлов в: {base_path}")
    
    # Генерируем файлы
    file_generators = [
        generate_backup_filename,
        generate_log_filename,
        generate_checksum_filename,
        generate_temp_filename,
        generate_archive_filename,
        generate_database_filename,
        generate_snapshot_filename,
        generate_misc_filename,
    ]
    
    print(f"Создание {num_files} файлов...")
    for i in range(num_files):
        generator = random.choice(file_generators)
        filename = generator()
        file_path = base_path / filename
        
        # Если файл уже существует, добавляем суффикс
        counter = 1
        while file_path.exists():
            name_parts = file_path.stem, file_path.suffix
            file_path = base_path / f"{name_parts[0]}_{counter}{name_parts[1]}"
            counter += 1
        
        dt = generate_timestamp()
        create_file_with_timestamp(file_path, dt)
        
        if (i + 1) % 10 == 0:
            print(f"  Создано {i + 1}/{num_files} файлов...")
    
    # Генерируем папки и подпапки
    if current_depth < max_depth and num_folders > 0:
        print(f"Создание {num_folders} папок (глубина {current_depth + 1}/{max_depth})...")
        for i in range(num_folders):
            folder_name = generate_folder_name()
            folder_path = base_path / folder_name
            
            # Если папка уже существует, добавляем суффикс
            counter = 1
            while folder_path.exists():
                folder_path = base_path / f"{folder_name}_{counter}"
                counter += 1
            
            folder_path.mkdir(parents=True, exist_ok=True)
            
            # Устанавливаем дату модификации папки
            dt = generate_timestamp()
            timestamp = dt.timestamp()
            os.utime(folder_path, (timestamp, timestamp))
            
            # Рекурсивно создаем файлы и подпапки
            if current_depth < max_depth - 1:
                sub_num_files = random.randint(5, 20)
                sub_num_folders = random.randint(0, 5) if current_depth < max_depth - 2 else 0
                generate_files(
                    folder_path,
                    num_files=sub_num_files,
                    num_folders=sub_num_folders,
                    max_depth=max_depth,
                    current_depth=current_depth + 1
                )
            else:
                # В последнем уровне создаем только файлы
                sub_num_files = random.randint(3, 15)
                generate_files(
                    folder_path,
                    num_files=sub_num_files,
                    num_folders=0,
                    max_depth=max_depth,
                    current_depth=current_depth + 1
                )
    
    print(f"Завершено: {base_path}")

def main():
    """Главная функция"""
    # Получаем путь к папке, где находится скрипт
    script_dir = Path(__file__).parent.absolute()
    
    print("=" * 60)
    print("Генератор тестовых файлов для backup_manager")
    print("=" * 60)
    print(f"Рабочая директория: {script_dir}")
    print()
    
    # Параметры генерации
    num_files = 50  # Количество файлов в корневой папке
    num_folders = 10  # Количество папок в корневой папке
    max_depth = 3  # Максимальная глубина вложенности
    
    try:
        generate_files(
            script_dir,
            num_files=num_files,
            num_folders=num_folders,
            max_depth=max_depth
        )
        
        print()
        print("=" * 60)
        print("Генерация завершена успешно!")
        print("=" * 60)
        
    except Exception as e:
        print(f"Ошибка при генерации: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()

