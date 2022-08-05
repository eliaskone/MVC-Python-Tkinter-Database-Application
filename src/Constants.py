import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(BASE_DIR, 'src')
PICTURES_DIR = os.path.join(BASE_DIR, 'pictures')
DATABASE_NAME = os.path.join(SRC_DIR, 'books.db')
ADD_PICTURE = os.path.join(PICTURES_DIR, 'add.png')
UPDATE_PICTURE = os.path.join(PICTURES_DIR, 'update.png')
DELETE_PICTURE = os.path.join(PICTURES_DIR, 'delete.png')

