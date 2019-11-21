from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from infomation import db,create_app

from infomation import models

app = create_app('development')

#Flask-Script
manage = Manager(app)
#数据库迁移扩展
Migrate(app,db)
manage.add_command('db',MigrateCommand)


if __name__ == '__main__':
    app.run()