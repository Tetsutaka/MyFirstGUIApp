import os
import logging
import glob
import shutil

SAMPLE_DIR = "sample/*"
DEBUG_DIR = "debug"
TEST = False

class RenameApp:
    def __init__(self, path_to_sample_data) -> None:
        self.path_to_sample_data = path_to_sample_data
        self.set_logging()

    def set_logging(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        stream_handler = logging.StreamHandler()
        self.logger.addHandler(stream_handler)
        file_handler = logging.FileHandler("sample.log")
        self.logger.addHandler(file_handler)
    
    def error_handler():
        pass

    def copy_data_for_debug(self, new_path):
        files = glob.glob(self.path_to_sample_data)
        if len(files) == 0:
            self.logger.error(f"no files found in '{self.path_to_sample_data}'")
            return
        if not os.path.exists(new_path):
            self.logger.info(f"Created directory '{new_path}'")
            os.makedirs(new_path, exist_ok=True)
        for file in files:
            if TEST:
                self.logger.info(f"DEBUG: Copied directory '{file}' to '{new_path}'")
                continue
            shutil.copy(file, new_path)
            self.logger.info(f"Copied directory '{file}' to '{new_path}'")


if __name__ == "__main__":
    app = RenameApp(SAMPLE_DIR)
    app.copy_data_for_debug(new_path=DEBUG_DIR)