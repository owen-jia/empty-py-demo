import email


class Employee:
    def __init__(self, name='', age=''):
        self.name = name
        self.age = age

    def info(self):
        print(f'Employee,name:{self.name},age:{self.age}')
        raise NameError('raise NameError')


class MyEmail(email.MIMEPart):
    def __init__(self):
        super.__init__(self)

    def set_content(self, *args, **kw):
        super().set_content(*args, **kw)
        if 'MIME-Version' not in self:
            self['MIME-Version'] = '1.0'

