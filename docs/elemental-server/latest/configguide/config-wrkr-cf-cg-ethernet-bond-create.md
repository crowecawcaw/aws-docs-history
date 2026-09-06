

This is version 2.18 of the AWS Elemental Server documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server/).

# Step A: Create the Bond
<a name="config-wrkr-cf-cg-ethernet-bond-create"></a>

First, create the bond for the network devices. In the next step, you will add the devices to the bond.

**To create the bond**

1. On the AWS Elemental Server web interface, go to the **Settings** page and choose **Network**.

1. On the **Network** page, choose **Network Devices**.

1. On the **Network Devices** page, choose **Add Network Device**.

1. In the **Add a New Network Device** dialog, select **bond (bondN)**.

1. Complete the fields as follows:
   + **Bond ID**: Provide a number that is unique among your bonded interfaces.
   + **Management**: Select if the devices that you're bonding are management interfaces.
   + **Description**: Auto-populates when you choose a device name. You can modify the description as needed.
   + **Address Mode**: Select the type of IP addresses this device uses, either **dhcp**, **static**, or **none**. If you're bonding eth0 and eth1, use static IPs. 
   + **IP Address**, **Netmask**, **Gateway**: Available when static IP addresses are used only. Complete with your networking information.
   + **Static Routes**: Select if you're using static routing.
   + **Network**, **Netmask**, **Gateway**: Available when static routes are used only. Complete with your networking information.

1. In **Mode**, select the bonding mode that you're using. The following table describes the modes that AWS Elemental Server supports:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-server/latest/configguide/config-wrkr-cf-cg-ethernet-bond-create.html)

1. In **Link Mode**, select the linking mode that you're using for this bond and complete the relevant fields, as described here:
   + For media-independent interface (MII) mode, complete these fields:
     + **MII Monitoring Frequency**: Determines how often the link state of each bonded interface is inspected for link failure, in milliseconds. We recommend 100ms as a starting point.
     + **Use Carrier** (optional): When checked, MII uses MII or ETHTOOL ioctls instead of netif\_carrier\_ok. Relies on the device driver to maintain link state. Note that ETHTOOL ioctls is less efficient and uses deprecated kernel calling sequences.
     + **Down Delay** (optional): Specifies the time, in milliseconds, to wait before disabling an interface after a link failure is detected. This value should be a multiple of the MII monitoring frequency. Otherwise, it AWS Elemental Server rounds it to the nearest multiple of the monitoring frequency. The default is 0.
     + **LACP Rate** (optional): Used with IEEE 802.3ad dynamic link aggregation only. Determines the rate that control packets are sent to the interface. **Fast** is every one second, and **Slow** is every 30 seconds.
     + **Up Delay** (optional): Specifies the time, in milliseconds, to wait before enabling an interface after a link failure is detected. This value should be a multiple of the MII monitoring frequency. Otherwise, it AWS Elemental Server rounds it to the nearest multiple of the monitoring frequency. The default is 0.
   + For address resolution protocol (ARP) mode, complete these fields:
     + **ARP Interval**: Determines how often the link state of each bonded interface is inspected, in milliseconds. Periodically checks devices for traffic and generates regular interval traffic via ARP probes for ARP IP target.
     + **ARP IP Target**: Specifies the IP address to use for ARP probes.
     + **Use Carrier** (optional): When checked, MII uses MII or ETHTOOL ioctls instead of netif\_carrier\_ok. Relies on the device driver to maintain link state. Note that ETHTOOL ioctls is less efficient and uses deprecated kernel calling sequences.
     + **LACP Rate** (optional): Used with IEEE 802.3ad dynamic link aggregation only. Determines the rate that control packets are sent to the interface. **Fast** is every one second, and **Slow** is every 30 seconds.

1. Choose **Save**. The new bond appears in the Network Devices list. Don't apply changes yet.