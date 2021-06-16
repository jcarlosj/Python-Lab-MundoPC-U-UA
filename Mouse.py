from Device import Device

class Mouse( Device ) :

    counter = 0

    def __init__( self, type, brand ) :
        Device .__init__( self, type, brand )
        self .__id = self .increment_counter()

    def __str__( self ) :
        return f'{ self .__id } [ { Device .__str__( self ) } ]'

    @classmethod
    def increment_counter( cls ) :
        cls .counter += 1

        return cls .counter

# ! Testing:
if __name__ == '__main__' :
    mouse_1 = Mouse( 'Mouse', 'Microsoft' )
    print( mouse_1 )