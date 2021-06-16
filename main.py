from Monitor import Monitor
from Keyboard import Keyboard
from Mouse import Mouse
from Computer import Computer
from Order import Order

print( ' Mundo PC '. center( 60, '-' ) )

monitor_1 = Monitor( 'Samsung', '21"' )
monitor_2 = Monitor( 'Dell', '29"' )
monitor_3 = Monitor( 'Samsung', '19"' )
monitor_4 = Monitor( 'Dell', '21"' )
monitor_5 = Monitor( 'Dell', '15"' )

keyboard_1 = Keyboard( 'wireless USB', 'Logitec' )
keyboard_2 = Keyboard( 'USB', 'Microsoft' )
keyboard_3 = Keyboard( 'USB', 'Logitec' )
keyboard_4 = Keyboard( 'wireless USB', 'Microsoft' )

mouse_1 = Mouse( 'wireless USB', 'Logitec' )
mouse_2 = Mouse( 'wireless USB', 'Microsoft' )
mouse_3 = Mouse( 'USB', 'Logitec' )
mouse_4 = Mouse( 'USB', 'Microsoft' )

computer_1 = Computer( 'Gamming PC', monitor_1, keyboard_2, mouse_2 )
computer_2 = Computer( 'Design PC', monitor_2, None, mouse_4 )
computer_3 = Computer( 'Server PC', monitor_2 )
computer_4 = Computer( 'Dev PC', monitor_4, keyboard_1, mouse_1 )

order_1 = Order( [ computer_1 ] )
order_2 = Order( [ computer_2, computer_3, computer_4 ] )

order_1 .add( computer_3 )
order_2 .add( computer_1 )

print( order_1 )
print( order_2 )