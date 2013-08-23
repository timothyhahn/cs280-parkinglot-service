from flask.ext.script import Manager, Server

from parkinglot import app
import os

import parkinglot.settings as settings

PORT = os.environ.get('PORT', 8765)

app.debug = settings.debug
app.config['SECRET_KEY'] = settings.secret_key

manager = Manager(app)
manager.add_command('runserver', Server(host='0.0.0.0', port=PORT))


@manager.command
def init_db():
    "Sets up the DB"
    print "Setting up DB"
    from parkinglot.database import init_db
    init_db()


@manager.command
def clear_db():
    "Clears the DB"
    print "Clearing DB"
    from parkinglot.database import clear_db
    clear_db()

if __name__ == "__main__":
    manager.run()
