This is version 2.20 of the AWS Elemental Statmux documentation.
This is the latest version. For prior versions, see the
_Previous Versions_ section of [AWS Elemental Statmux
and AWS Elemental Live Documentation](../../../elemental-live.md "../../../elemental-live.md").

# Step C: Install the AWS Elemental Software

Perform these on each node where you are installing AWS Elemental software, either directly
at the machine or from your workstation via SSH.

Make sure that you use the `.run` file that corresponds to the
`.iso` file that you used to set up the operating system on
the node. That is, install AWS Elemental Statmux software on the nodes that you kickstarted
with the Statmux `.iso` and worker software on nodes that
you kickstarted with the worker `.iso`.

###### To install the software

1. At the Linux command line, log in with the _elemental_ user credentials.
2. Run the installer as follows. Use the actual file name of your
   `.run` file, rather than the example below.

```
[elemental@hostname ~]$ sudo sh ./elemental_production_statmux_2.20.nnnnn.run -l -z -t
```

where -l is a letter, not a number. 3. You are prompted as described in the table below.

| Prompt                                                                             | Action                                                                                                                                         |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Do you agree to these terms?`                                                     | This prompt appears after you have paged through the EULA (End User License Agreement). Enter `Yes` or `No`. (You must enter Yes to continue.) |
| `Enter this server’s Hostname`                                                     | Type the hostname of this hardware unit. For example, `statmux-01`                                                                             |
| `Does eth0 use DHCP to get its IP address?`                                        | Type `Yes` to use DHCP or type `No` to enter a static IP address.                                                                              |
| `Enter eth0's IP address:`                                                         | If you chose static, type the IP address for this hardware unit.                                                                               |
| `Enter eth0's NETMASK:`                                                            | If you chose static, type the netmask for this hardware unit.                                                                                  |
| `Enter eth0's Gateway (or type `none`):`                                           | If you chose static, type `none` or type the gateway for this hardware unit.                                                                   |
| `Keep this configured nameserver?`                                                 | Skip; you set up a nameserver in the next phase of configuration.                                                                              |
| `Would you like to configure eth1?`                                                | Type `No`; you can configure eth1 in the next phase of the configuration.                                                                      |
| `The firewall for this system is currently disabled. Would you like to enable it?` | Skip; you set up the firewall in the next phase of configuration.                                                                              |
| `For security purposes, we require that you change the default password.`          | This prompt is shown if you are still using the default password.                                                                              |
| `Select time zone ('n' for more)`                                                  | Enter the time zone you want to show on the web interface of the nodes. This setting does not affect activity via SSH or via the REST API.     |
| `Would you like to start the Elemental service now?`                               | Type `Yes`.                                                                                                                                    | Then the software will be installed. Finally, this message will appear: `Installation and configuration complete! Please open a web browser and point it to http://xxx.xxx.xxx.xxx to get to the web interface. Enjoy!` 4. Start a web browser and start the AWS Elemental Statmux web interface by typing the following: `http://<hostname>` Make sure the web interface displays. |
