import os
import sys
import shutil
from manage import main


def runserver():
    collectstatic()
    migrate()
    sys.argv = ['manage.py', 'runserver']
    main()


def migrate():
    sys.argv = ['manage.py', 'makemigrations']
    main()
    sys.argv = ['manage.py', 'migrate']
    main()


def collectstatic():
    if not os.path.exists('assets'):
        os.makedirs('assets')
    if not os.path.exists('media'):
        os.makedirs('media')
    sys.argv = ['manage.py', 'collectstatic', '--noinput']
    main()


def clear():
    shutil.rmtree('assets', True)
    shutil.rmtree('static', True)
    shutil.rmtree('media', True)
    if os.path.exists('db.sqlite3'):
        os.remove('db.sqlite3')
