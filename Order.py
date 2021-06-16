from Monitor import Monitor
from Keyboard import Keyboard
from Mouse import Mouse
from Computer import Computer

class Order :

    counter = 0

    def __init__( self ) :
        self .__products = []
        self .__id = 0

    def __str__( self ) :
        # [ str( product ) for product in self .__products ]: Es una lista de compresion
        return f'{ type( self ) .__name__ } { self .__id } \n { [ str( product ) for product in self .__products ] }'

    @classmethod
    def increment_counter( cls ) :
        cls .counter += 1

        return cls .counter

    def add( self, computer ) :
        self .__id = self .increment_counter()
        self .__products .append( computer )

if __name__ == '__main__' :
    monitor_1 = Monitor( 'Samsung', '21"' )
    monitor_2 = Monitor( 'Dell', '29"' )
    keyboard_1 = Keyboard( 'Keyboard', 'Logitec' )
    keyboard_2 = Keyboard( 'Keyboard', 'Microsoft' )
    mouse_1 = Mouse( 'Mouse', 'Logitec' )
    mouse_2 = Mouse( 'Mouse', 'Microsoft' )

    computer_1 = Computer( 'Gamming PC', monitor_1, keyboard_1, mouse_1 )
    computer_2 = Computer( 'Design PC', monitor_2 )
    computer_3 = Computer( 'Server PC', monitor_2, keyboard_2, mouse_2 )

    order_1 = Order()
    order_2 = Order()

    order_1 .add( computer_1 )
    order_1 .add( computer_3 )
    order_2 .add( computer_2 )

    print( order_1 )
    print( order_2 )
