class CodeBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.fields = {}

    def add_field(self, type, name):
        self.fields[type] = name
        return self

    def __str__(self):
        if (self.root_name):
            stringified = 'class ' + self.root_name + ':'
            
            if (len(self.fields) > 0):
                stringified += '\n  def __init__(self):'
                for key in self.fields:
                    stringified += '\n    self.' + str(key) + ' = ' + str(self.fields[key])
            else:
                stringified += '\n  pass'
        
            return stringified

        return ''
        
cb = CodeBuilder('Person').add_field('name', '""')\
                          .add_field('age', '0')
print(cb)
