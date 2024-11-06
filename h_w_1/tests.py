import unittest
from commands import CommandHandler
from logger import Logger

class TestCommandHandler(unittest.TestCase):
    def setUp(self):
        self.logger = Logger('test_log.xml')
        self.command_handler = CommandHandler('test_vfs.tar', self.logger)

    def test_ls(self):
        self.assertTrue(isinstance(self.command_handler.ls(), list))

    def test_cd(self):
        self.command_handler.cd('test_directory')
        self.assertEqual(self.command_handler.current_directory, '/test_directory')

    def test_rmdir(self):
        self.command_handler.rmdir('test_directory')
        self.assertNotIn('test_directory', self.command_handler.ls())

    def test_rm(self):
        self.command_handler.rm('test_file.txt')
        self.assertNotIn('test_file.txt', self.command_handler.ls())

if __name__ == '__main__':
    unittest.main()
