# Getting ready

Before you create a Zixi output in your event, perform the following
preparation.

- Speak to the administrator of the downstream system and make
  sure that they can work as the Zixi
  receiver.
  If they can't, then you can't deliver using the Zixi
  option.
- Decide if you want to deliver redundant streams in the output.
  Each stream has a different destination on the downstream system.
  The downstream destination initially handles one stream. If that
  stream fails, the downstream destination can switch to the other
  stream.

You should find out if the downstream destination can handle
this type of resiliency. If they can't then there is no point to
delivering two streams.

If you do want to deliver two streams, you must make sure that
your content provider can send you two copies of the source. The
two copies must be completely identical.

- Decide if you want to encrypt the content. If you do, discuss
  the following with the downstream destination:
  - Discuss the encryption level with the administrator of
    the downstream system. Both sides must use the same level.
    You can use AES 128, AES 192, or AES 256. You should
    provide this information to the downstream destination so
    that they can set up with the same level.
  - Agree on an encryption key value. The value is an ASCII
    representation of hexadecimal bytes. The length must be
    correct for the encryption level. For example, for AES 128,
    it must be a 32-character string of 16 hexadecimal
    bytes.

- Discuss the following with the administrator of the downstream
  destination:
  - Obtain the IP address and port for each destination for
    the output. For example, `198.51.100.0:2088`.
  - Make sure that the administrator of the downstream
    system sets up to allow Elemental Live to access the
    destination. For example, they might need to open ports on
    the destination, or allow traffic from the public IP
    address of Elemental Live.
  - Tell the downstream destination the latency (in
    milliseconds) that you plan to configure into Elemental Live
    for packet loss and recovery. Packet recovery is a key
    feature of Zixi. The downstream destination should choose a
    latency value that is close to the value that you plan to
    use.

  -
