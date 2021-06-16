class Device :

    def __init__( self, type, brand ) :
        self ._input_type = type
        self ._brand = brand

    @property
    def type( self ) :
        return self ._input_type

    @property
    def brand( self ) :
        return self ._brand

    @type .setter
    def type( self, type ) :
        self ._type = type

    @type .setter
    def brand( self, brand ) :
        self ._brand = brand

    def __str__( self ) :
        return f'Product: { type( self ) .__name__ }, Brand: { self ._brand }, Type: { self ._input_type }'


# ! Testing:
if __name__ == '__main__' :
    device_1 = Device( 'Teclado', 'Genius' )
    print( device_1 )