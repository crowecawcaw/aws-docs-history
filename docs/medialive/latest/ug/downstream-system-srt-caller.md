# Coordinate with the downstream system

With an SRT output group, you can create more than one output, in order to deliver the
same content to more than one downstream system.

You and the operator of each downstream system must discuss details about the output
delivery. With caller mode, MediaLive is the caller and the sender. The
downstream system is the listener and the receiver.

1. Decide if you need two destinations for the output:
   - If the MediaLive channel is a [standard
     channel](plan-redundancy.md "plan-redundancy.md"), you need two destinations.
   - If the MediaLive channel is a single-pipeline channel, you need one
     destination.

2. Obtain the IP address and port for each destination. For example,
   `srt://203.0.113.22:5000` and
   `srt://203.0.113.88:5001`.

Note that if you are delivering to MediaConnect, you can obtain the
addresses only after the MediaConnect operator creates the flows. See the last step in
this procedure. 3. MediaLive always encrypts the content, therefore you must agree about the
following encryption details:

    * The encryption algorithm: AES 128, AES 192, or AES 256.
    * The passphrase that MediaLive and the downstream system will use to create
     the encryption and decryption keys. The passphrase can be 10 to 79
     Unicode characters, which means that spaces are allowed.

4. Discuss the following with the operator of the downstream system:
   - Tell the downstream system about the latency (in milliseconds) that
     you plan to configure into MediaLive for packet loss and recovery. Packet
     recovery is a key feature of SRT. The downstream destination
     should choose a latency value that is close to the value that you plan
     to use.

   You will configure the latency in each output, so each downstream
   system can have a different latency.
   - MediaLive works without a stream ID. But if you want to include one, or if
     the downstream system would like to use one, agree on the ID. Maximum
     512 UTF-8 characters.

5. If you are delivering to a MediaConnect flow, ask the MediaConnect operator to create their
   flow now.

Ask the operator to give you the one or two addresses that are in the Inbound
IP address field for that flow. These addresses are the destinations for the SRT
output. For example, `srt://203.0.113.22:5000` and
`srt://203.0.113.88:5001`.
