This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Step C: Install the AWS Elemental Software

These steps must be performed on each node where you are installing AWS Elemental software,
either directly at the machine or from your workstation via SSH.

Make sure that you use the .run file that corresponds to the .iso file that you
used to set up the operating system on the node. That is, install AWS Elemental
Conductor File software on the nodes that you kickstarted with the AWS Elemental
Conductor File .iso and worker software on nodes that you kickstarted with the
worker .iso.

###### To install the software

1. At the Linux command line, log in with the _elemental_ user
   credentials.
2. Run the installer as follows. Use the actual filename of your .run file,
   rather than the example below.

For GPU and CPU versions of the software.

```
[elemental@hostname ~]$ sudo sh ./elemental_production_server_2.18.n.nnnnn.run -l -z -t
```

For CPU-only versions of the software.

```
[elemental@hostname ~]$ sudo sh ./elemental_production_server_cpu_2.18.n.nnnnn.run -l -z -t
```

Where -l is a letter, not a number. 3. You are prompted as described in the table below.

| Prompt                                                                             | Action                                                                                                                                                                                                                                                 |
| ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Do you agree to these terms?`                                                     | This prompt appears after you have paged through the EULA (End User License Agreement). Enter `Yes` or `No`. (You must enter Yes to continue.)                                                                                                         |
| `Enter this server’s Hostname`                                                     | Type the hostname of this hardware unit. For example, `server-01`                                                                                                                                                                                      |
| `Is eth0 a management interface?`                                                  | Type `Yes`.                                                                                                                                                                                                                                            |
| `Does eth0 use DHCP to get its IP address?`                                        | Type `Yes` to use DHCP or type `No` to enter a static IP address. If you plan to bond eth0 and eth1 (which you will set up in a later phase), we recommend that you enter a static IP address and set up eth0, eth1, and bond0 all on the same subnet. |
| `Enter eth0's IP address:`                                                         | If you chose static, type the IP address for this hardware unit.                                                                                                                                                                                       |
| `Enter eth0's NETMASK:`                                                            | If you chose static, type the netmask for this hardware unit.                                                                                                                                                                                          |
| `Enter eth0's Gateway (or type `none`):`                                           | If you chose static, type `none` or type the gateway for this hardware unit.                                                                                                                                                                           |
| `Keep this configured nameserver: 10.6.16.10?`                                     | Skip; you set up a nameserver in the next phase of configuration.                                                                                                                                                                                      |
| `Would you like to configure eth1?`                                                | Type `No`; you can configure eth1 in the next phase of the configuration.                                                                                                                                                                              |
| `The firewall for this system is currently disabled. Would you like to enable it?` | Skip; you set up the firewall in the next phase of configuration.                                                                                                                                                                                      |
| `Select time zone ('n' for more)`                                                  | Enter the time zone you want to show on the web interface of the nodes. This setting does not affect activity via SSH or via the REST API.                                                                                                             |
| `Would you like to start the Elemental service now?`                               | Type `Yes`.                                                                                                                                                                                                                                            | Then the software is installed. Finally, this message appears: `Installation and configuration complete! Please open a web browser and point it to https://xxx.xxx.xxx.xxx to get to the web interface. Enjoy!` 4. Start a web browser and start the AWS Elemental Server web interface by typing the following: `https://<hostname>` Make sure the web interface displays. |
