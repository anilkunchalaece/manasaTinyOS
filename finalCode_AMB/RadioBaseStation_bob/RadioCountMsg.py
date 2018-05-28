#
# This class is automatically generated by mig. DO NOT EDIT THIS FILE.
# This class implements a Python interface to the 'RadioCountMsg'
# message type.
#

import tinyos.message.Message

# The default size of this message type in bytes.
DEFAULT_MESSAGE_SIZE = 7

# The Active Message type associated with this message.
AM_TYPE = 6

class RadioCountMsg(tinyos.message.Message.Message):
    # Create a new RadioCountMsg of size 7.
    def __init__(self, data="", addr=None, gid=None, base_offset=0, data_length=7):
        tinyos.message.Message.Message.__init__(self, data, addr, gid, base_offset, data_length)
        self.amTypeSet(AM_TYPE)
    
    # Get AM_TYPE
    def get_amType(cls):
        return AM_TYPE
    
    get_amType = classmethod(get_amType)
    
    #
    # Return a String representation of this message. Includes the
    # message type name and the non-indexed field values.
    #
    def __str__(self):
        s = "Message <RadioCountMsg> \n"
        try:
            s += "  [nodeId=0x%x]\n" % (self.get_nodeId())
        except:
            pass
        try:
            s += "  [temp=0x%x]\n" % (self.get_temp())
        except:
            pass
        try:
            s += "  [humi=0x%x]\n" % (self.get_humi())
        except:
            pass
        try:
            s += "  [light=0x%x]\n" % (self.get_light())
        except:
            pass
        return s

    # Message-type-specific access methods appear below.

    #
    # Accessor methods for field: nodeId
    #   Field type: short
    #   Offset (bits): 0
    #   Size (bits): 8
    #

    #
    # Return whether the field 'nodeId' is signed (False).
    #
    def isSigned_nodeId(self):
        return False
    
    #
    # Return whether the field 'nodeId' is an array (False).
    #
    def isArray_nodeId(self):
        return False
    
    #
    # Return the offset (in bytes) of the field 'nodeId'
    #
    def offset_nodeId(self):
        return (0 / 8)
    
    #
    # Return the offset (in bits) of the field 'nodeId'
    #
    def offsetBits_nodeId(self):
        return 0
    
    #
    # Return the value (as a short) of the field 'nodeId'
    #
    def get_nodeId(self):
        return self.getUIntElement(self.offsetBits_nodeId(), 8, 1)
    
    #
    # Set the value of the field 'nodeId'
    #
    def set_nodeId(self, value):
        self.setUIntElement(self.offsetBits_nodeId(), 8, value, 1)
    
    #
    # Return the size, in bytes, of the field 'nodeId'
    #
    def size_nodeId(self):
        return (8 / 8)
    
    #
    # Return the size, in bits, of the field 'nodeId'
    #
    def sizeBits_nodeId(self):
        return 8
    
    #
    # Accessor methods for field: temp
    #   Field type: int
    #   Offset (bits): 8
    #   Size (bits): 16
    #

    #
    # Return whether the field 'temp' is signed (False).
    #
    def isSigned_temp(self):
        return False
    
    #
    # Return whether the field 'temp' is an array (False).
    #
    def isArray_temp(self):
        return False
    
    #
    # Return the offset (in bytes) of the field 'temp'
    #
    def offset_temp(self):
        return (8 / 8)
    
    #
    # Return the offset (in bits) of the field 'temp'
    #
    def offsetBits_temp(self):
        return 8
    
    #
    # Return the value (as a int) of the field 'temp'
    #
    def get_temp(self):
        return self.getUIntElement(self.offsetBits_temp(), 16, 1)
    
    #
    # Set the value of the field 'temp'
    #
    def set_temp(self, value):
        self.setUIntElement(self.offsetBits_temp(), 16, value, 1)
    
    #
    # Return the size, in bytes, of the field 'temp'
    #
    def size_temp(self):
        return (16 / 8)
    
    #
    # Return the size, in bits, of the field 'temp'
    #
    def sizeBits_temp(self):
        return 16
    
    #
    # Accessor methods for field: humi
    #   Field type: int
    #   Offset (bits): 24
    #   Size (bits): 16
    #

    #
    # Return whether the field 'humi' is signed (False).
    #
    def isSigned_humi(self):
        return False
    
    #
    # Return whether the field 'humi' is an array (False).
    #
    def isArray_humi(self):
        return False
    
    #
    # Return the offset (in bytes) of the field 'humi'
    #
    def offset_humi(self):
        return (24 / 8)
    
    #
    # Return the offset (in bits) of the field 'humi'
    #
    def offsetBits_humi(self):
        return 24
    
    #
    # Return the value (as a int) of the field 'humi'
    #
    def get_humi(self):
        return self.getUIntElement(self.offsetBits_humi(), 16, 1)
    
    #
    # Set the value of the field 'humi'
    #
    def set_humi(self, value):
        self.setUIntElement(self.offsetBits_humi(), 16, value, 1)
    
    #
    # Return the size, in bytes, of the field 'humi'
    #
    def size_humi(self):
        return (16 / 8)
    
    #
    # Return the size, in bits, of the field 'humi'
    #
    def sizeBits_humi(self):
        return 16
    
    #
    # Accessor methods for field: light
    #   Field type: int
    #   Offset (bits): 40
    #   Size (bits): 16
    #

    #
    # Return whether the field 'light' is signed (False).
    #
    def isSigned_light(self):
        return False
    
    #
    # Return whether the field 'light' is an array (False).
    #
    def isArray_light(self):
        return False
    
    #
    # Return the offset (in bytes) of the field 'light'
    #
    def offset_light(self):
        return (40 / 8)
    
    #
    # Return the offset (in bits) of the field 'light'
    #
    def offsetBits_light(self):
        return 40
    
    #
    # Return the value (as a int) of the field 'light'
    #
    def get_light(self):
        return self.getUIntElement(self.offsetBits_light(), 16, 1)
    
    #
    # Set the value of the field 'light'
    #
    def set_light(self, value):
        self.setUIntElement(self.offsetBits_light(), 16, value, 1)
    
    #
    # Return the size, in bytes, of the field 'light'
    #
    def size_light(self):
        return (16 / 8)
    
    #
    # Return the size, in bits, of the field 'light'
    #
    def sizeBits_light(self):
        return 16
    