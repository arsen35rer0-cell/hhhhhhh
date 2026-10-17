import os
from datetime import datetime

def format_file_size(size_bytes):
    """Форматирует размер файла"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} TB"

def get_file_modified_time(path):
    """Получает время модификации файла"""
    try:
        return datetime.fromtimestamp(os.path.getmtime(path))
    except:
        return datetime.now()

def is_valid_path(path):
    """Проверяет валидность пути"""
    invalid_chars = '<>:"|?*'
    return not any(char in path for char in invalid_chars)
