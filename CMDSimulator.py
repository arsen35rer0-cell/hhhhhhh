import os
import sys
import time
from datetime import datetime
from command_parser import CommandParser
from commands import CommandExecutor
from fake_filesystem import FakeFileSystem

class CMDSimulator:
    def __init__(self):
        self.current_path = "C:\\Users\\Admin"
        self.filesystem = FakeFileSystem()
        self.parser = CommandParser()
        self.executor = CommandExecutor(self.filesystem)
        self.history = []
        self.running = True
        
    def get_prompt(self):
        """Генерирует приглашение ввода как в реальном cmd"""
        return f"{self.current_path}> "
    
    def run(self):
        """Главный цикл симулятора"""
        while self.running:
            try:
                prompt = self.get_prompt()
                user_input = input(prompt).strip()
                
                if not user_input:
                    continue
                
                self.history.append(user_input)
                self.process_command(user_input)
                
            except KeyboardInterrupt:
                print("\n^C")
                self.running = False
            except EOFError:
                break
    
    def process_command(self, command_line):
        """Обрабатывает введённую команду"""
        # Парсируем команду
        parsed = self.parser.parse(command_line)
        
        if not parsed:
            return
        
        cmd_name = parsed['command'].lower()
        args = parsed['args']
        
        # Выполняем команду
        result = self.executor.execute(
            cmd_name, 
            args, 
            self.current_path
        )
        
        # Если команда изменяет директорию
        if cmd_name == 'cd' and result['success']:
            self.current_path = result.get('new_path', self.current_path)
        
        # Выводим результат
        if result['output']:
            print(result['output'], end='')
        
        if result['error']:
            print(f"Error: {result['error']}")
