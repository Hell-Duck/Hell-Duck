import xml.etree.ElementTree as ET
from datetime import datetime

class Logger:
    def __init__(self, log_file):
        self.log_file = log_file
        self.root = ET.Element("Log")

    def log(self, action):
        entry = ET.SubElement(self.root, "Entry")
        entry.set("timestamp", datetime.now().isoformat())
        entry.text = action
        self.save_log()

    def save_log(self):
        tree = ET.ElementTree(self.root)
        tree.write(self.log_file)
