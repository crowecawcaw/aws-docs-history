# Provide connection information to downstream systems

After you create the channel with SRT outputs in listener mode, you must provide connection information to the operators of the downstream systems so they can configure their SRT callers to connect to MediaLive.

###### To obtain the connection information

1. After you have created the channel, select the channel by its name. The channel details appear.
2. Choose the **Destinations** tab.
3. In the **Output destinations** section, find the SRT output group.
4. For each output in the group, note the connection information that downstream systems will need. For a standard channel, there are two sets of information (one for each pipeline). For a single-pipeline channel, there is one set.

**For MediaLive channels**:

    * In the **Egress endpoints** section under the **Destinations** tab, note the **Source IP** address. This is the IP address that downstream systems should connect to.
    * In the **SRT destination settings** section, note the **Listener port**.
    * Provide the destination to downstream operators in the format `srt://`source-ip`:`listener-port``.

**For MediaLive Anywhere channels**:

    * In the **SRT destination settings** section under the **Destinations** tab, note the **Node interface IPs**. This is the IP address that downstream systems should connect to.
    * In the same section, note the **Listener port**.
    * Provide the destination to downstream operators in the format `srt://`node-interface-ip`:`listener-port``.

5. Provide these destination URLs to the operators of the downstream systems. The operators must configure their SRT callers to connect to these addresses.
   Make sure that the operators at the downstream systems set up as follows:

- They configure the correct number of connections:
  - If the MediaLive channel is a standard channel, they must connect to both destination addresses for redundancy.
  - If the MediaLive channel is a single-pipeline channel, they must connect to the single destination address.

- They configure their SRT callers to use the same encryption algorithm and passphrase that you agreed on.
- They configure their SRT callers to use a latency value. SRT will negotiate and use the maximum of the latency values configured on both sides.
- If you specified a stream ID in the output configuration, the downstream systems can optionally send a stream ID value during connection. MediaLive accepts connections with any stream ID value (or no stream ID). The stream ID is logged for monitoring and troubleshooting purposes only.
- Their source IP addresses must be included in the CIDR allow list of the input security group that the channel security group references. Otherwise, MediaLive will reject their connection attempts.
