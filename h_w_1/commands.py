import os
import tarfile

class CommandHandler:
    def __init__(self, vfs_path, logger):
        self.vfs_path = vfs_path
        self.logger = logger
        self.current_directory = '/'

        # Распаковка виртуальной файловой системы
        self.extract_vfs()

    def extract_vfs(self):
        with tarfile.open(self.vfs_path, 'r') as tar:
            tar.extractall(path='vfs')

    def ls(self):
        return os.listdir(f'vfs{self.current_directory}')

    def cd(self, directory):
        if os.path.isdir(f'vfs{self.current_directory}/{directory}'):
            self.current_directory = os.path.join(self.current_directory, directory)
            self.logger.log(f'Changed directory to {self.current_directory}')
        else:
            raise FileNotFoundError(f'Directory {directory} not found')

    def rmdir(self, directory):
        os.rmdir(f'vfs{self.current_directory}/{directory}')
        self.logger.log(f'Removed directory {directory}')

    def rm(self, filename):
        os.remove(f'vfs{self.current_directory}/{filename}')
        self.logger.log(f'Removed file {filename}')

    def exit(self):
        self.logger.log('Exiting emulator')
        exit()
