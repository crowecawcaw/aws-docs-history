# Getting ready

Before you create an SRT output in your event, perform the following
preparation.

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
  - Agree on a passphrase that you will both use for
    encryption. It can be any length because it's not the
    encryption key itself, it's just used to generate the
    encryption key. The passphrase can use an ASCII characters
    including spaces.

- Discuss the following with the administrator of the downstream
  destination:
  - Find out the role of the downstream destination in the
    transmission—either the SRT caller or the SRT listener. If
    you can't obtain this information, then you could assume
    that the downstream destination is the listener, which is
    typically the case.
  - Obtain
    the IP address and port for each destination for the
    output. For example, `192.168.1.2:5000`.
  - Make sure that the administrator of the downstream
    system sets up to allow Elemental Live to access the
    destination. For example, they might need to open ports on
    the destination, or allow traffic from the public IP
    address of Elemental Live.
  - Tell the downstream destination the latency (in
    milliseconds) that you plan to configure into Elemental Live
    for packet loss and recovery. Packet recovery is a key
    feature of SRT. The downstream destination should choose a
    latency value that is close to the value that you plan to
    use.

  -
  - Note that Elemental Live doesn't use an SRT stream ID
    when delivering output.
