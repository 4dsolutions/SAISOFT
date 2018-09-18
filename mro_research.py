class Gen0 (object):
    """the Old One"""

    def __init__(self):
        print("__init__ of {}".format("Gen0"))

class Adam(Gen0):
    """one of two in Gen1"""

    def __init__(self):
        super().__init__()
        print("__init__ of {}".format("Adam"))
         
class Eve(Gen0):
    """one of two in Gen1"""

    def __init__(self):
        super().__init__()
        print("__init__ of {}".format("Eve"))

    def waldo(self):
        print("Waldo in {}".format("Eve"))    

class Cain(Adam, Eve):
    """Gen2"""
    def __init__(self):
        super().__init__()
        print("__init__ of {}".format("Cain"))


class Abel(Adam, Eve):
    """Gen2"""

    def __init__(self):
        super().__init__()
        print("__init__ of {}".format("Abel"))


class Seth(Adam, Eve):
    """Gen2"""

    def __init__(self):
        super().__init__()
        print("__init__ of {}".format("Seth"))

class Azura(Adam, Eve):
    """Gen2"""

    def __init__(self):
        super().__init__()
        print("__init__ of {}".format("Azura"))

class Enosh(Seth, Azura):
    """Gen3"""

    def __init__(self):
        super().__init__()
        print("__init__ of {}".format("Enosh"))

class Kenan(Enosh):
    """Gen4"""

    def __init__(self):
        super().__init__()
        print("__init__ of {}".format("Kenan"))

class Mahalaleel(Kenan):
    """Gen5"""

    def __init__(self):
        super().__init__()
        print("__init__ of {}".format("Mahalaleel"))

class Jared(Mahalaleel):
    """Gen6"""

    def __init__(self):
        super().__init__()
        print("__init__ of {}".format("Jared"))

class Enoch(Jared):
    """Gen7"""

    def __init__(self):
        super().__init__()
        print("__init__ of {}".format("Enoch"))

class Methusela(Enoch):
    """Gen8"""

    def __init__(self):
        super().__init__()
        print("__init__ of {}".format("Methusela"))

    def waldo(self):
        print("Waldo in {}".format("Methusela")) 

class Elisha(Enoch):
    """Gen8"""

    def __init__(self):
        super().__init__()
        print("__init__ of {}".format("Elisha"))


class Lamech(Methusela):
    """Gen9"""

    def __init__(self):
        super().__init__()
        print("__init__ of {}".format("Lamech"))

class Ashmua(Elisha):
    """Gen9"""

    def __init__(self):
        super().__init__()
        print("__init__ of {}".format("Ashmua"))

    def waldo(self):
        print("Waldo in {}".format("Ashuma"))   
        

class Noah(Lamech, Ashmua):
    """Gen10"""

    def __init__(self):
        super().__init__()
        print("__init__ of {}".format("Noah"))


if __name__ == "__main__":
    import inspect
    subject = Noah()
    subject.waldo()
    print(inspect.getmro(subject.__class__))
    