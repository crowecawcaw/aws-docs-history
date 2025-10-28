This is version 2.18 of the AWS Elemental Conductor File documentation. This is the
latest version. For prior versions, see the _Archive_ section of
[AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Configure DNS and NTP Servers for the Cluster

You can configure servers in the following ways:

- Create a list of DNS servers for each node to use.
- Create a list of NTP servers for each node to use.

###### To configure servers

1. On the AWS Elemental Conductor File node, choose **Nodes** in the main menu.
2. On the **Nodes** screen, choose **Edit** (wrench icon) beside the primary Conductor node.
3. On the The **Hostname, DNS & NTP** tab, choose **Network > Hostname, DNS & NTP**.

###### Important

This screen has a warning in red. It does not apply the first time you set up DNS and NTP servers. 4. Add servers as desired and choose **Save**. 5. If you have a secondary Conductor node, switch to the web interface for that node and repeat these steps.
