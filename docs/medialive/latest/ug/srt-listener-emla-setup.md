# Additional setup for MediaLive Anywhere channels

If you are creating an SRT listener output on a MediaLive Anywhere channel, there are additional configuration requirements:

- **Logical interface name**: In the **Destinations** section, you must specify the logical interface for each output in listener mode. This field appears when you create a channel on a MediaLive Anywhere cluster. The logical interface determines which physical network interface on the MediaLive Anywhere node will be used for the SRT listener.
- **Node interface IPs**: After you create the channel, the destination information will include the node interface IPs. This field displays the IP address that the downstream system should use to connect to the MediaLive Anywhere node. The IP address is associated with the physical interface that is mapped to the logical interface you selected.

      + **In the console**: The node interface IPs are displayed in the **Destinations** table under the **SRT destination settings** section.
      + **Using the API**: The node interface IPs are included in the node describe call as `PhysicalInterfaceIpAddresses`.

  You must provide this IP address to the downstream systems so they can configure their SRT callers to connect to the correct MediaLive Anywhere node interface.
