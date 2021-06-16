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
        return f'ID: { self .__id }, Product: { type( self ) .__name__ }, Brand: { self .__brand }, Size: { self .__size }'

    @classmethod
    def generate_id( cls ) :
        cls .counter += 1

        return cls .counter

# ! Testing:
if __name__ == '__main__' :
    monitor_1 = Monitor( 'Samsung', 21 )
    monitor_2 = Monitor( 'HP', 19 )
    print( monitor_1 )
    print( monitor_2 )