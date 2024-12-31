from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
full_path = BASE_DIR.joinpath('files', 'DataBase.db')
full_path_str = str(full_path)

# Replace backslashes with forward slashes
full_path_str = full_path_str.replace("\\", "/")

# Append a forward slash after '/cdn/media'
# full_path_str += '/'
db_path = full_path_str

# TOKEN
token = ''

