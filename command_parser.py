import re

class CommandParser:
    def parse(self, command_line):
        """Парсирует командную строку"""
        command_line = command_line.strip()
        
        if not command_line:
            return None
        
        # Разбиваем на команду и аргументы
        parts = command_line.split(maxsplit=1)
        command = parts[0]
        args = parts[1] if len(parts) > 1 else ""
        
        # Парсируем аргументы с поддержкой кавычек
        args_list = self._parse_args(args)
        
        return {
            'command': command,
            'args': args_list,
            'raw_args': args
        }
    
    def _parse_args(self, args_string):
        """Парсирует аргументы с поддержкой кавычек"""
        if not args_string:
            return []
        
        args = []
        current_arg = ""
        in_quotes = False
        
        for char in args_string:
            if char == '"':
                in_quotes = not in_quotes
            elif char == ' ' and not in_quotes:
                if current_arg:
                    args.append(current_arg)
                    current_arg = ""
            else:
                current_arg += char
        
        if current_arg:
            args.append(current_arg)
        
        return args
