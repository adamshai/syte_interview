
class DefaultConfig(object):
    def __init__(self, options = None):
        self.SQLALCHEMY_DATABASE_URI = 'sqlite:////etc/todo-list.db'
        self.SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(DefaultConfig):
    def __init__(self, options = None):
        super().__init__(options)
        self.DEBUG = True


class TestConfig(DefaultConfig):
    def __init__(self, options = None):
        super().__init__(options)
        if options.get('db_path') is None:
            raise Exception('A test must have a DB path')
        self.SQLALCHEMY_DATABASE_URI = options.get('db_path')
        self.TESTING = True


def get_config(options):
    if options is None or options.get('environment') is None:
        return DefaultConfig(options)
    return {
        'dev' : DevConfig(options),
        'test' : TestConfig(options),
    }.get(options.get('environment'), DefaultConfig(options))

