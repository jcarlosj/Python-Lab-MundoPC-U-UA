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
        return f'''
        Product: { type( self ) .__name__ }, ID: { self .__id }, Name: { self .__name }
            { self .__monitor }
            { self .__keyboard }
            { self .__mouse }
        '''

    @classmethod
    def increment_counter( cls ) :
        cls .counter += 1

        return cls .counter

# ! Testing:
if __name__ == '__main__' :
    monitor_1 = Monitor( 'Samsung', 21 )
    keyboard_1 = Keyboard( 'USB', 'Logitec' )
    mouse_1 = Mouse( 'USB', 'Logitec' )

    computer_1 = Computer( 'Gamming PC', monitor_1, keyboard_1, mouse_1 )

    print( computer_1 )

    monitor_2 = Monitor( 'Dell', 29 )
    computer_2 = Computer( 'Design PC', monitor_2 )
    print( computer_2 )