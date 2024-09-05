# coding=UTF-8
from pprint import pprint
import tkinter
import inspect
from HW_11_3_classes import *
def get_parents(obj):
    mro = inspect.getmro(type(obj))
    mros_1 = []
    for i in mro:
        mros_1.append(inspect.getmro(i))
    mros_2 = []
    for i in mros_1:
        l = []
        for j in i:
            if str(j).find('.') > 0:
                s = str(j).split('.')
                l.append(s[1][0:len(s[1])-2])
        if len(l)>0:
            mros_2.append(l)
    for i in mros_2: # Ищем "свою" запись
        if i[0] == type(obj).__name__:
            myself = i
    myself.remove(type(obj).__name__)
    mros_2.remove(mros_2[0])
    for i in myself:
        for j in mros_2:
            if j[0] == i and len(j) > 1:
                for k in range(len(j)-1):
                    myself.remove(j[k+1])
    return tuple(myself)
def introspection_info(obj,show_log = False):
    result = {}
    caller_locals = inspect.currentframe().f_back.f_locals
    try:
        var_name = "'" + [name for name, value in caller_locals.items() if obj is value][0] + "'"
    except IndexError:
        var_name = ', не имеющий имени,'
    if show_log: print(f"Объект {var_name} является экземпляром класса '{type(obj).__name__}'.", end='')
    result['type'] = str(type(obj).__name__)
    if str(type(obj).__name__) in ['int', 'float', 'complex', 'bool', 'str', 'list', 'tuple', 'range', 'bytes', 'bytearray', 'memoryview', 'set', 'frozenset', 'dict', 'NoneType', 'BaseException', 'file', 'contextlib.AbstractContextManager', 'type', 'object', 'classmethod', 'staticmethod', 'property', 'function', 'method', 'module', 'namespace']:
        if show_log: print(' (Базовый класс языка Python.)')
        result['about_type'] = 'Python base class'
    else:
        if show_log: print(" Пользовательский класс, ", end='')
        result['about_type'] = 'User defined type'
        parents = get_parents(obj)
        if len(parents) == 0:
            if show_log: print('не имеющий классов-предшественников.')
            result['Parents'] = None
        else:
            if show_log: print(f'наследник классов {parents}.')
            result['Parents'] = parents
        mdl = inspect.getmodule(obj)
        result['Module'] = mdl
        if show_log: print(mdl)
        mro = inspect.getmro(type(obj))
        result['mro'] = mro
        if show_log: print(f'Method resolution order (mro) класса {type(obj).__name__}:\n {mro}')
    if show_log: print('---------------------------------------------------------------------------------------------')
    try:
        atrs = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
        if show_log: print('Объект имеет следующие атрибуты:')
        result['Attributes'] = atrs
        for i in atrs:
            if show_log: print(i)
    except AttributeError:
        if show_log: print(f'Класс {type(obj).__name__} не имеет доступных атрибутов.')
        result['Attributes'] = None
    if show_log: print('----------------------------------------------')
    members = inspect.getmembers(obj)
    if len(members) > 0:
        if show_log: print('Объект имеет следующие методы:')
        methods = []
        for member in members:
            if inspect.ismethod(member[1]) or inspect.isbuiltin(member[1]):# or inspect.ismethodwrapper(member[1]):
                if show_log: print(member[0])
                methods.append(member[0])
        result['Methods'] = methods
    else:
        if show_log: print('Объект не имеет доступных методов.')
        result['Methods'] = None
    if show_log: print('----------------------------------------------')
    # for member in members:
        # print(member)
    return result
if __name__ == '__main__':
    # my_obj = Figure((255, 0, 0), 15, 17, 6)
    # my_obj = Circle((255,0,0),100)
    # my_obj = ['A', 'B', 'C']
    # my_obj = 4
    # my_obj = tkinter.Tk()
    # my_obj = Nissan(120,'Rotor', 1_500_000)
    # my_obj = 42
    about = introspection_info(my_obj,True)
    print(about)