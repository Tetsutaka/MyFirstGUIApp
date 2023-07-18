import os
import logging
import glob
import shutil

SAMPLE_DIR = "sample/*"
DEBUG_DIR = "debug"
TEST = False

class RenameApp:
    def __init__(self, path_to_sample_data: str) -> None:
        self.path_to_sample_data = path_to_sample_data
        self.set_logging()

    def set_logging(self):
        # Set logger
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        stream_handler = logging.StreamHandler()
        self.logger.addHandler(stream_handler)
        file_handler = logging.FileHandler("sample.log")
        self.logger.addHandler(file_handler)

    def copy_data_for_debug(self, new_path: str):
        files = glob.glob(self.path_to_sample_data)
        if len(files) == 0:  # Exit process if no file or directory found.
            self.logger.error(f"no file or directory found in '{self.path_to_sample_data}'")
            return
        if not os.path.exists(new_path):  # Create directory if there is no destination directory.
            self.logger.info(f"Created directory '{new_path}'")
            os.makedirs(new_path, exist_ok=True)
        for file in files:
            if TEST:  # If it is test mode, it exits without processing any file or directory.
                self.logger.info(f"DEBUG: Copied directory '{file}' to '{new_path}'")
                continue
            shutil.copytree(file, os.path.join(new_path, file), dirs_exist_ok=True)
            self.logger.info(f"Copied directory '{file}' to '{new_path}'")


if __name__ == "__main__":
    app = RenameApp(SAMPLE_DIR)
    app.copy_data_for_debug(new_path=DEBUG_DIR)