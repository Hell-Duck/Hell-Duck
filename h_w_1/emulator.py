import configparser
from gui import GUI
from logger import Logger
from commands import CommandHandler

def main():
    # Загрузка конфигурации
    config = configparser.ConfigParser()
    config.read('config.ini')
    
    hostname = config['Settings']['hostname']
    vfs_path = config['Settings']['vfs_path']
    log_file = config['Settings']['log_file']
    
    # Инициализация логгера
    logger = Logger(log_file)
    
    # Инициализация обработчика команд
    command_handler = CommandHandler(vfs_path, logger)
    
    # Запуск GUI
    gui = GUI(hostname, command_handler)
    gui.run()

if __name__ == "__main__":
    main()
