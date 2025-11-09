This is version 2.18 of the AWS Elemental Conductor File documentation. This is the
latest version. For prior versions, see the _Archive_ section of
[AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Run the Configuration Script for AWS Elemental Conductor File

Perform this procedure if one of these applies:

- You have two Conductor File nodes.
- You want to require users to enter login credentials when working with the cluster (user authentication).

###### Getting Ready

If you have a redundant Conductor File configuration, designate one of the nodes as the primary Conductor File node and the other as the secondary Conductor File node.

###### Configuring AWS Elemental Conductor File

If you have a redundant Conductor File configuration, perform this procedure on both nodes: first the primary, and then the secondary. If you have a non-redundant configuration, perform this procedure on the one Conductor File node.

1. From a Linux prompt, log in with the _elemental_ user credentials. Once
   you're logged in, the initial directory is `/home/elemental`.
2. Change to the directory where the configuration script is located:

```
[elemental@hostname ~]$ **cd /opt/elemental\_se**
```

3. Run the configuration script as follows:

```
[elemental@hostname elemental_se]$ **sudo ./configure**
```

4. The following prompts appear. Complete each prompt as follows.

| Prompt                                                                             | Action                                                                                                                                                                                                                                                                                                                                                                                        |
| ---------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Enter this server’s Hostname`                                                     | This is already set to the value that you entered or accepted during node installation. For more information, see [AWS Elemental Server Configuration Guide](../../../elemental-server/latest/configguide.md "../../../elemental-server/latest/configguide.md").<br>Change the value only if you realize that you have given the same hostname to more than one hardware unit in the cluster. |
| `Is eth0 a management interface?`                                                  | This is already set to the value that you entered or accepted during node installation. For more information, see [AWS Elemental Server Configuration Guide](../../../elemental-server/latest/configguide.md "../../../elemental-server/latest/configguide.md").                                                                                                                              |
| `Does eth0 use DHCP to get its IP address?`                                        | This is already set to the value that you entered or accepted during node installation. For more information, see [AWS Elemental Server Configuration Guide](../../../elemental-server/latest/configguide.md "../../../elemental-server/latest/configguide.md").                                                                                                                              |
| `Enter eth0's IP address:`                                                         | This is already set to the value that you entered or accepted during node installation. For more information, see [AWS Elemental Server Configuration Guide](../../../elemental-server/latest/configguide.md "../../../elemental-server/latest/configguide.md").                                                                                                                              |
| `Enter eth0's NETMASK:`                                                            | This is already set to the value that you entered or accepted during node installation. For more information, see [AWS Elemental Server Configuration Guide](../../../elemental-server/latest/configguide.md "../../../elemental-server/latest/configguide.md").                                                                                                                              |
| `Enter eth0's Gateway (or type `none`):`                                           | This is already set to the value that you entered or accepted during node installation. For more information, see [AWS Elemental Server Configuration Guide](../../../elemental-server/latest/configguide.md "../../../elemental-server/latest/configguide.md").                                                                                                                              |
| `Keep this configured nameserver: 10.6.16.10?`                                     | Skip; you will set up a nameserver on the web interface.                                                                                                                                                                                                                                                                                                                                      |
| `Would you like to configure eth1?`                                                | Skip; you will set up more Ethernet devices on the web interface.                                                                                                                                                                                                                                                                                                                             |
| `The firewall for this system is currently disabled. Would you like to enable it?` | Skip; you can set up the firewall on the web interface.                                                                                                                                                                                                                                                                                                                                       |
| `Configure this node as the secondary node?`                                       | See the following section _Configuring the Conductor Nodes_.                                                                                                                                                                                                                                                                                                                                  |
| `Select time zone ('n' for more)`                                                  | Change the time zone as appropriate. This impacts only the web interface.                                                                                                                                                                                                                                                                                                                     |
| `Would you like to start the Elemental service now?`                               | Type `Yes`.                                                                                                                                                                                                                                                                                                                                                                                   |

###### Configuring the Conductor File Nodes

Take the appropriate action:

- If you have a redundant configuration and the node that you are configuring is the primary Conductor File node, type `No`.
- If you have a redundant configuration and the node that you are configuring is the secondary Conductor File node, type `Yes`. At the next prompt, enter the IP address or hostname of the primary node.
- If you have a non-redundant configuration (only one Conductor File node), type `No`.
