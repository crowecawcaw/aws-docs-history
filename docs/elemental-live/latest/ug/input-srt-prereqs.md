# Get ready

Before you create an SRT input in your event, speak to the
administrator of the upstream system, and obtain the following
information:

- The IP address and port of the content. For example,
  192.168.1.2:5000.
- Whether the content is encrypted. If it is encrypted, find out
  if encryption uses AES 128, AES 192, or AES 256.

Obtain the passphrase from the administrator of the upstream
system.

- The stream ID, if the upstream system uses this identifier.
  The sender might require a stream ID, in which case you must
  obtain it. Otherwise the SRT handshake between the caller and
  listener might fail.
- The preferred latency (in milliseconds) for implementing
  packet loss and recovery. Packet recovery is a key feature of
  SRT.
