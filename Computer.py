from Monitor import Monitor
from Keyboard import Keyboard
from Mouse import Mouse

class Computer :

    counter = 0

    def __init__( self, name, monitor = None, keyboard = None, mouse = None ) :
        self .__monitor = monitor
        self .__keyboard = keyboard
        self .__mouse = mouse
        self .__name = name
        self .__id = self .increment_counter()

    def __str__( self ) :
        return f'{ type( self ) .__name__ } { self .__id } - { self .__name } [ { self .__monitor .__str__() }, { self .__keyboard .__str__() }, { self .__mouse .__str__() } ]'

    @classmethod
    def increment_counter( cls ) :
        cls .counter += 1

        return cls .counter

if __name__ == '__main__' :
    monitor_1 = Monitor( 'Samsung', '21"' )
    keyboard_1 = Keyboard( 'Keyboard', 'Logitec' )
    mouse_1 = Mouse( 'Mouse', 'Logitec' )

    computer_1 = Computer( 'Gamming PC', monitor_1, keyboard_1, mouse_1 )

    print( computer_1 )

    monitor_2 = Monitor( 'Dell', '29"' )
    computer_2 = Computer( 'DesignWeb', monitor_2 )
    print( computer_2 )