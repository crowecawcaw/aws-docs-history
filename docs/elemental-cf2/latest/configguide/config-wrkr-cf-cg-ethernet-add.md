This is version 2.18 of the AWS Elemental Conductor File documentation. This is the
latest version. For prior versions, see the _Archive_ section of
[AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Add Ethernet Devices

1. On the AWS Elemental Conductor File web interface, choose **Nodes** in the main menu.
2. On the **Nodes** screen, choose **Edit** (wrench icon) beside the primary Conductor node.
3. On the **Network Configuration** screen, choose **Network** > **Network Devices**.
4. On the **Network Devices** tab, choose **Add Network Device**.
5. In the **Add Network Device** dialog, select **eth** as the device type and choose **Save**.
6. In the **Edit a Network Device** dialog, complete the fields as follows:
   - **Device Name**: Specify "ethN" (for example, `eth1`).
   - **Management**: Leave unchecked. eth0 has already been set up as the management interface and you do not need more than one management interface in the cluster. The management interface is ideally connected to a network dedicated to communication between Conductor and its worker nodes.
   - **Description**: Optional.
   - **Address Mode**: Select **DHCP**, **Static**, or **None**. We recommend that you select **Static** if you plan to bond the two Conductor management interfaces.

   If you choose Static Routing, extra fields appear for you to configure the device: **IP Address**, **Netmask**, (optional) **Gateway**, and (optional) **Static Routes**.

7. Choose **Save**. The new device appears in the Network Devices list.
8. Repeat these steps for each worker in the cluster.
