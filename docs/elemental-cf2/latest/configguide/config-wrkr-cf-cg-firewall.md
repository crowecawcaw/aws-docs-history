This is version 2.18 of the AWS Elemental Conductor File documentation. This is the
latest version. For prior versions, see the _Archive_ section of
[AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Open Ports on the Firewall for AWS Elemental Server Nodes

The procedure for opening ports on the firewall for AWS Elemental Server nodes is the same as for
AWS Elemental Conductor File nodes.

You can enable or disable the firewall. By default, the firewall is enabled.

The installer configures the ports on your firewall that must be open for incoming and outgoing traffic to and from each node. You can open more ports if required for any reason.

###### To open ports on the firewall

1. On the AWS Elemental Conductor File node, click **Nodes** in the main menu.
2. On the **Nodes** screen, choose **Edit** (wrench icon) beside a worker node node.
3. On the **Node Configuration** screen, choose **Firewall**.
4. Choose **Firewall On**. A list of ports appears.
5. In the list of ports, add or delete ports as desired.
6. Repeat on all worker nodes in the cluster.
