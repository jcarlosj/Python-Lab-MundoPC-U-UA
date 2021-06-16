from Monitor import Monitor
from Keyboard import Keyboard
from Mouse import Mouse
from Computer import Computer

class Order :

    counter = 0

    def __init__( self, computers ) :
        self .__products = computers
        self .__id = self .increment_counter()

    def __str__( self ) :
        template_str = ''

        for computer in self .__products :
            template_str += computer .__str__()

        # [ str( product ) for product in self .__products ]: Es una lista de compresion
        return f'''   { type( self ) .__name__ }: { self .__id } 
            { template_str } 
        '''

    @classmethod
    def increment_counter( cls ) :
        cls .counter += 1

        return cls .counter

    def add( self, computer ) :
        self .__products .append( computer )

# ! Testing:
if __name__ == '__main__' :
    monitor_1 = Monitor( 'Samsung', '21"' )
    monitor_2 = Monitor( 'Dell', '29"' )
    keyboard_1 = Keyboard( 'USB', 'Logitec' )
    keyboard_2 = Keyboard( 'USB', 'Microsoft' )
    mouse_1 = Mouse( 'USB', 'Logitec' )
    mouse_2 = Mouse( 'USB', 'Microsoft' )

    computer_1 = Computer( 'Gamming PC', monitor_1, keyboard_1, mouse_1 )
    computer_2 = Computer( 'Design PC', monitor_2 )
    computer_3 = Computer( 'Server PC', monitor_2, keyboard_2, mouse_2 )

    order_1 = Order( [ computer_1 ] )
    order_2 = Order( [ computer_2, computer_3 ] )

    order_1 .add( computer_3 )
    order_2 .add( computer_1 )

    print( order_1 )
    print( order_2 )
