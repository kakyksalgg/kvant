"""Эксперимент: сборка мусора в CPython. Глава 6, шаг 6.5."""
import gc
import weakref


class Node:
    """Узел, хранит значение и ссылку на следующий."""
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f'Node({self.value})'

a = Node('A')
b = Node('B')
a.next = b
b.next = a

wa = weakref.ref(a)
wb = weakref.ref(b)

print(f'До удаления: a = {wa()}, b = {wb()}')

gc.disable()
print('Сборщик циклов выключен')

del a
del b

print(f'После del, без gc.collect: a = {wa()}, b = {wb()}')

gc.collect()
print(f'После gc.collect(): a = {wa()}, b = {wb()}')

gc.enable()