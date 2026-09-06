

# Setting up an SRT input
<a name="input-srt-setup"></a>

You create an SRT input in Elemental Live in order to ingest a transport stream. The upstream system that provides the transport stream is the sender and is set up as an SRT listener. 

**To set up an SRT input**

1. From the **Input** menu in your event, select **Secure Reliable Transport**.

1. Complete the following fields:
   + **Network Location**: The IP address and host that you obtained from the upstream, with the protocol. For example:

     `srt://192.168.1.2:5000`
   + **Interface**: See the tooltip on the web interface.
   + **Latency**: The latency that you want to apply to aid in packet recovery in Elemental Live. You should closely match the latency that the upstream system prefers. For more details, see the tooltip.
   + **Stream ID**: Enter this value if the upstream system provided it. 

1. Complete the encryption fields, if applicable:
   + **Encryption**: Choose **None**, or choose the encryption level that you obtained from the upstream system.
   + **Passphrase**: Enter the passphrase that the upstream system provided. 