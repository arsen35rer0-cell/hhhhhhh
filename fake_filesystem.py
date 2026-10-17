import os
from datetime import datetime

class FakeFileSystem:
    def __init__(self):
        self.drives = {
            'C': {
                'Users': {
                    'Admin': {
                        'Desktop': {},
                        'Documents': {
                            'Project.txt': 'Some project data',
                            'Notes.txt': 'My notes'
                        },
                        'Downloads': {}
                    }
                },
                'Windows': {
                    'System32': {}
                },
                'Program Files': {
                    'Python': {},
                    'Git': {}
                }
            },
            'D': {
                'Data': {
                    'Backup': {}
                }
            }
        }
    
    def path_exists(self, path):
        """Проверяет, существует ли путь"""
        return self._navigate(path) is not None
    
    def list_directory(self, path):
        """Список файлов в директории"""
        obj = self._navigate(path)
        if obj is None or not isinstance(obj, dict):
            return None
        return list(obj.keys())
    
    def get_file_content(self, path):
        """Получает содержимое файла"""
        obj = self._navigate(path)
        if isinstance(obj, str):
            return obj
        return None
    
    def is_directory(self, path):
        """Проверяет, является ли путь директорией"""
        obj = self._navigate(path)
        return isinstance(obj, dict)
    
    def get_drive_info(self, drive):
        """Информация о диске"""
        return {
            'total': '476 GB',
            'used': '312 GB',
            'free': '164 GB',
            'percent': 65
        }
    
    def _navigate(self, path):
        """Навигирует по фейковой FS"""
        path = path.strip('\\').replace('/', '\\')
        
        if not path or path == '\\':
            return self.drives
        
        parts = path.split('\\')
        
        if not parts[0]:  # Путь начинается с \
            return None
        
        drive = parts[0][0].upper()
        
        if drive not in self.drives:
            return None
        
        current = self.drives[drive]
        
        for part in parts[1:]:
            if part and isinstance(current, dict):
                current = current.get(part)
                if current is None:
                    return None
            elif part:
                return None
        
        return current
