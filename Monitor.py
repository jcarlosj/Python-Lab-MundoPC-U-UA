class Monitor :

    counter = 0

    def __init__( self, brand, size ) :
        self .__id = self .generate_id()
        self .__brand = brand
        self .__size = size

    @property
    def brand( self ) :
        return self .__brand

    @property
    def size( self ) :
        return self .__size

    def __str__( self ) -> str:
        return f'{ type( self ) .__name__ } { self .__id } [ brand: { self .__brand }, size: { self .__size } ]'

    @classmethod
    def generate_id( cls ) :
        cls .counter += 1

        return cls .counter

# ! Testing:
if __name__ == '__main__' :
    monitor_1 = Monitor( 'Samsung', '15"' )
    print( monitor_1 )