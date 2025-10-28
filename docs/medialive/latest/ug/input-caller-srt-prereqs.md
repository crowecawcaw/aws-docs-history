# Get ready

1. Obtain the following information from the operator of the upstream
   system:
   - The IP address and port of the content, including the stream if the
     upstream system uses that. For example,
     `192.0.2.120:7001` with stream
     `mycontent`.

   You need two addresses for a standard-class input, or one address
   for a single-class input. For information about input classes and
   their uses, see [Choosing the channel class and input
   class](class-channel-input.md "class-channel-input.md").
   - Whether the content is encrypted. If it is encrypted, find out if
     encryption uses AES 128, AES 192, or AES 256.

   Obtain the passphrase from the operator of the upstream
   system.
   - The stream ID, if the upstream system uses this identifier. The
     upstream system might require a stream ID, in which case you must
     obtain it. Otherwise the SRT handshake between the caller and
     listener will probably fail.
   - The preferred latency (in milliseconds) for implementing packet
     loss and recovery. Packet recovery is a key feature of SRT.

2. If the content is encrypted, you must store the passphrase that the operator
   gave you. Someone in your organization must store the passphrase in a secret in
   AWS Secrets Manager. For more information, see [Storing an encryption or decryption passphrase](encryption-srt-password.md "encryption-srt-password.md") .
   The
   result of creating the secret is an ARN that looks like this:

`arn:aws:secretsmanager:`region`:123456789012:secret:`Sample-abcdef``
