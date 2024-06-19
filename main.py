import os
import subprocess

WINDOW_EXECUTOR_PATH = "./src/scripts/executor.bat"
LINUX_EXECUTOR_PATH  = "./src/scripts/executor.sh"
MODEL_PATH = "./src/model/model.ipynb"


def get_os() -> str:
    return os.name

def execute_project(os_type: str = None):
    if os_type is None:
        os_type = get_os()
    
    if os_type == "nt":  # Windows
        subprocess.call(WINDOW_EXECUTOR_PATH, shell=True)
    elif os_type == "posix":  # Linux/Unix
        subprocess.call(["bash", LINUX_EXECUTOR_PATH])
    else:
        raise ValueError("Unsupported OS type")

if __name__ == "__main__":
    execute_project()
