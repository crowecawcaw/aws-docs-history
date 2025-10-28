This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Add Ethernet Devices

The eth0 device was automatically set up during installation. If you also set up eth1 at
that time, no further configuration is required. If you didn't set up eth1 or want to set up more devices, use these
instructions to do so.

###### To add Ethernet devices

1. On the AWS Elemental Server web interface, go to the **Settings** page
   and choose **Network**.
2. On the **Network** page, choose **Network Devices**.
3. On the **Network Devices** page, choose **Add Network Device**.
4. In the **Add a New Network Device** dialog, select **eth (ethN)**.
5. Complete the fields as follows:
   - **Device Name**: Select the eth device that you're setting up.
   - **Management**: Typically, leave this unchecked. This device won't be set up
     as a management interface. The node is usually installed with eth0 as the management
     interface and the node doesn't need more than one.
   - **Description**: Auto-populates when you choose a device name. You can modify
     the description as needed.
   - **Master Device**: Should display **`No devices with port bond
settings available.`** This wording indicates that you haven't created a
     bond-type device, so bonding isn't available.
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

6. Choose **Save**. The new device appears in the Network Devices
   list.
