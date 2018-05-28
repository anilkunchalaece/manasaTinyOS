/**
 * This class is automatically generated by mig. DO NOT EDIT THIS FILE.
 * This class implements a Java interface to the 'RadioCountMsg'
 * message type.
 */

public class RadioCountMsg extends net.tinyos.message.Message {

    /** The default size of this message type in bytes. */
    public static final int DEFAULT_MESSAGE_SIZE = 7;

    /** The Active Message type associated with this message. */
    public static final int AM_TYPE = 6;

    /** Create a new RadioCountMsg of size 7. */
    public RadioCountMsg() {
        super(DEFAULT_MESSAGE_SIZE);
        amTypeSet(AM_TYPE);
    }

    /** Create a new RadioCountMsg of the given data_length. */
    public RadioCountMsg(int data_length) {
        super(data_length);
        amTypeSet(AM_TYPE);
    }

    /**
     * Create a new RadioCountMsg with the given data_length
     * and base offset.
     */
    public RadioCountMsg(int data_length, int base_offset) {
        super(data_length, base_offset);
        amTypeSet(AM_TYPE);
    }

    /**
     * Create a new RadioCountMsg using the given byte array
     * as backing store.
     */
    public RadioCountMsg(byte[] data) {
        super(data);
        amTypeSet(AM_TYPE);
    }

    /**
     * Create a new RadioCountMsg using the given byte array
     * as backing store, with the given base offset.
     */
    public RadioCountMsg(byte[] data, int base_offset) {
        super(data, base_offset);
        amTypeSet(AM_TYPE);
    }

    /**
     * Create a new RadioCountMsg using the given byte array
     * as backing store, with the given base offset and data length.
     */
    public RadioCountMsg(byte[] data, int base_offset, int data_length) {
        super(data, base_offset, data_length);
        amTypeSet(AM_TYPE);
    }

    /**
     * Create a new RadioCountMsg embedded in the given message
     * at the given base offset.
     */
    public RadioCountMsg(net.tinyos.message.Message msg, int base_offset) {
        super(msg, base_offset, DEFAULT_MESSAGE_SIZE);
        amTypeSet(AM_TYPE);
    }

    /**
     * Create a new RadioCountMsg embedded in the given message
     * at the given base offset and length.
     */
    public RadioCountMsg(net.tinyos.message.Message msg, int base_offset, int data_length) {
        super(msg, base_offset, data_length);
        amTypeSet(AM_TYPE);
    }

    /**
    /* Return a String representation of this message. Includes the
     * message type name and the non-indexed field values.
     */
    public String toString() {
      String s = "Message <RadioCountMsg> \n";
      try {
        s += "  [nodeId=0x"+Long.toHexString(get_nodeId())+"]\n";
      } catch (ArrayIndexOutOfBoundsException aioobe) { /* Skip field */ }
      try {
        s += "  [temp=0x"+Long.toHexString(get_temp())+"]\n";
      } catch (ArrayIndexOutOfBoundsException aioobe) { /* Skip field */ }
      try {
        s += "  [humi=0x"+Long.toHexString(get_humi())+"]\n";
      } catch (ArrayIndexOutOfBoundsException aioobe) { /* Skip field */ }
      try {
        s += "  [light=0x"+Long.toHexString(get_light())+"]\n";
      } catch (ArrayIndexOutOfBoundsException aioobe) { /* Skip field */ }
      return s;
    }

    // Message-type-specific access methods appear below.

    /////////////////////////////////////////////////////////
    // Accessor methods for field: nodeId
    //   Field type: short, unsigned
    //   Offset (bits): 0
    //   Size (bits): 8
    /////////////////////////////////////////////////////////

    /**
     * Return whether the field 'nodeId' is signed (false).
     */
    public static boolean isSigned_nodeId() {
        return false;
    }

    /**
     * Return whether the field 'nodeId' is an array (false).
     */
    public static boolean isArray_nodeId() {
        return false;
    }

    /**
     * Return the offset (in bytes) of the field 'nodeId'
     */
    public static int offset_nodeId() {
        return (0 / 8);
    }

    /**
     * Return the offset (in bits) of the field 'nodeId'
     */
    public static int offsetBits_nodeId() {
        return 0;
    }

    /**
     * Return the value (as a short) of the field 'nodeId'
     */
    public short get_nodeId() {
        return (short)getUIntBEElement(offsetBits_nodeId(), 8);
    }

    /**
     * Set the value of the field 'nodeId'
     */
    public void set_nodeId(short value) {
        setUIntBEElement(offsetBits_nodeId(), 8, value);
    }

    /**
     * Return the size, in bytes, of the field 'nodeId'
     */
    public static int size_nodeId() {
        return (8 / 8);
    }

    /**
     * Return the size, in bits, of the field 'nodeId'
     */
    public static int sizeBits_nodeId() {
        return 8;
    }

    /////////////////////////////////////////////////////////
    // Accessor methods for field: temp
    //   Field type: int, unsigned
    //   Offset (bits): 8
    //   Size (bits): 16
    /////////////////////////////////////////////////////////

    /**
     * Return whether the field 'temp' is signed (false).
     */
    public static boolean isSigned_temp() {
        return false;
    }

    /**
     * Return whether the field 'temp' is an array (false).
     */
    public static boolean isArray_temp() {
        return false;
    }

    /**
     * Return the offset (in bytes) of the field 'temp'
     */
    public static int offset_temp() {
        return (8 / 8);
    }

    /**
     * Return the offset (in bits) of the field 'temp'
     */
    public static int offsetBits_temp() {
        return 8;
    }

    /**
     * Return the value (as a int) of the field 'temp'
     */
    public int get_temp() {
        return (int)getUIntBEElement(offsetBits_temp(), 16);
    }

    /**
     * Set the value of the field 'temp'
     */
    public void set_temp(int value) {
        setUIntBEElement(offsetBits_temp(), 16, value);
    }

    /**
     * Return the size, in bytes, of the field 'temp'
     */
    public static int size_temp() {
        return (16 / 8);
    }

    /**
     * Return the size, in bits, of the field 'temp'
     */
    public static int sizeBits_temp() {
        return 16;
    }

    /////////////////////////////////////////////////////////
    // Accessor methods for field: humi
    //   Field type: int, unsigned
    //   Offset (bits): 24
    //   Size (bits): 16
    /////////////////////////////////////////////////////////

    /**
     * Return whether the field 'humi' is signed (false).
     */
    public static boolean isSigned_humi() {
        return false;
    }

    /**
     * Return whether the field 'humi' is an array (false).
     */
    public static boolean isArray_humi() {
        return false;
    }

    /**
     * Return the offset (in bytes) of the field 'humi'
     */
    public static int offset_humi() {
        return (24 / 8);
    }

    /**
     * Return the offset (in bits) of the field 'humi'
     */
    public static int offsetBits_humi() {
        return 24;
    }

    /**
     * Return the value (as a int) of the field 'humi'
     */
    public int get_humi() {
        return (int)getUIntBEElement(offsetBits_humi(), 16);
    }

    /**
     * Set the value of the field 'humi'
     */
    public void set_humi(int value) {
        setUIntBEElement(offsetBits_humi(), 16, value);
    }

    /**
     * Return the size, in bytes, of the field 'humi'
     */
    public static int size_humi() {
        return (16 / 8);
    }

    /**
     * Return the size, in bits, of the field 'humi'
     */
    public static int sizeBits_humi() {
        return 16;
    }

    /////////////////////////////////////////////////////////
    // Accessor methods for field: light
    //   Field type: int, unsigned
    //   Offset (bits): 40
    //   Size (bits): 16
    /////////////////////////////////////////////////////////

    /**
     * Return whether the field 'light' is signed (false).
     */
    public static boolean isSigned_light() {
        return false;
    }

    /**
     * Return whether the field 'light' is an array (false).
     */
    public static boolean isArray_light() {
        return false;
    }

    /**
     * Return the offset (in bytes) of the field 'light'
     */
    public static int offset_light() {
        return (40 / 8);
    }

    /**
     * Return the offset (in bits) of the field 'light'
     */
    public static int offsetBits_light() {
        return 40;
    }

    /**
     * Return the value (as a int) of the field 'light'
     */
    public int get_light() {
        return (int)getUIntBEElement(offsetBits_light(), 16);
    }

    /**
     * Set the value of the field 'light'
     */
    public void set_light(int value) {
        setUIntBEElement(offsetBits_light(), 16, value);
    }

    /**
     * Return the size, in bytes, of the field 'light'
     */
    public static int size_light() {
        return (16 / 8);
    }

    /**
     * Return the size, in bits, of the field 'light'
     */
    public static int sizeBits_light() {
        return 16;
    }

}
