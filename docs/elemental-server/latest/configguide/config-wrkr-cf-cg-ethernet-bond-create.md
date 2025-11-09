This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Step A: Create the Bond

First, create the bond for the network devices. In the next step, you will add the devices to the bond.

###### To create the bond

1. On the AWS Elemental Server web interface, go to the **Settings** page
   and choose **Network**.
2. On the **Network** page, choose **Network Devices**.
3. On the **Network Devices** page, choose **Add Network Device**.
4. In the **Add a New Network Device** dialog, select **bond
   (bondN)**.
5. Complete the fields as follows:
   - **Bond ID**: Provide a number that is unique among your bonded
     interfaces.
   - **Management**: Select if the devices that you're bonding are management
     interfaces.
   - **Description**: Auto-populates when you choose a device name. You can modify
     the description as needed.
   - **Address Mode**: Select the type of IP addresses this device uses, either
     **dhcp**, **static**, or
     **none**. If you're bonding eth0 and eth1, use static IPs.
   - **IP Address**, **Netmask**, **Gateway**:
     Available when static IP addresses are used only. Complete with your networking
     information.
   - **Static Routes**: Select if you're using static routing.
   - **Network**, **Netmask**,
     **Gateway**: Available when static routes are used only. Complete
     with your networking information.

6. In **Mode**, select the bonding mode that you're using. The
   following table describes the modes that AWS Elemental Server supports:

| Bonding mode                          | Description                                                                                                                                                                                                                                                                               |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Round robin                           | Transmissions are received and sent sequentially on each bonded interface<br>beginning with the first one available.                                                                                                                                                                      |
| Active backup                         | Transmissions are received and sent out via the first available bonded<br>interface. The other interface is only used if the active interface<br>fails.                                                                                                                                   |
| Balanced XOR                          | Using the exclusive-or (XOR) method, the interface matches up the incoming<br>request's MAC address with the MAC address for one of the bonded interface NICs.<br>Once this link is established, transmissions are sent out sequentially beginning<br>with the first available interface. |
| Broadcast                             | All transmissions are sent on all interfaces in the bond.                                                                                                                                                                                                                                 |
| IEEE 802.3ad dynamic link aggregation | Creates aggregation groups that share the same speed and duplex settings.<br>Transmits and receives on all interfaces in the active aggregator. Requires a<br>switch that is 802.3ad compliant.                                                                                           |
| Adaptive transmit load balancing      | Outgoing traffic is distributed according to current load on each interface<br>in the bond. Incoming traffic is received by the currently active interface. If<br>the receiving interface fails, another interface takes over the MAC address of<br>the failed interface.                 |
| Adaptive load balancing               | Includes transmit and receive load balancing for IPV4 traffic. Receive load<br>balancing is achieved through ARP negotiation.                                                                                                                                                             |

7. In **Link Mode**, select the linking mode that you're using for
   this bond and complete the relevant fields, as described here:
   - For media-independent interface (MII) mode, complete these fields:
     - **MII Monitoring Frequency**: Determines how often the link
       state of each bonded interface is inspected for link failure, in milliseconds.
       We recommend 100ms as a starting point.
     - **Use Carrier** (optional): When checked, MII uses MII or
       ETHTOOL ioctls instead of netif_carrier_ok. Relies on the device driver to
       maintain link state. Note that ETHTOOL ioctls is less efficient and uses
       deprecated kernel calling sequences.
     - **Down Delay** (optional): Specifies the time, in
       milliseconds, to wait before disabling an interface after a link failure is
       detected. This value should be a multiple of the MII monitoring frequency.
       Otherwise, it AWS Elemental Server rounds it to the nearest multiple of the
       monitoring frequency. The default is 0.
     - **LACP Rate** (optional): Used with IEEE 802.3ad dynamic
       link aggregation only. Determines the rate that control packets are sent to the
       interface. **Fast** is every one second, and
       **Slow** is every 30 seconds.
     - **Up Delay** (optional): Specifies the time, in
       milliseconds, to wait before enabling an interface after a link failure is
       detected. This value should be a multiple of the MII monitoring frequency.
       Otherwise, it AWS Elemental Server rounds it to the nearest multiple of the
       monitoring frequency. The default is 0.

   - For address resolution protocol (ARP) mode, complete these fields:
     - **ARP Interval**: Determines how often the link state of
       each bonded interface is inspected, in milliseconds. Periodically checks devices
       for traffic and generates regular interval traffic via ARP probes for ARP IP
       target.
     - **ARP IP Target**: Specifies the IP address to use for ARP
       probes.
     - **Use Carrier** (optional): When checked, MII uses MII or
       ETHTOOL ioctls instead of netif_carrier_ok. Relies on the device driver to
       maintain link state. Note that ETHTOOL ioctls is less efficient and uses
       deprecated kernel calling sequences.
     - **LACP Rate** (optional): Used with IEEE 802.3ad dynamic
       link aggregation only. Determines the rate that control packets are sent to the
       interface. **Fast** is every one second, and
       **Slow** is every 30 seconds.

8. Choose **Save**. The new bond appears in the Network Devices list.
   Don't apply changes yet.
