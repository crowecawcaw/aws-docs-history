This is version 2.20 of the AWS Elemental Statmux documentation.
This is the latest version. For prior versions, see the
_Previous Versions_ section of [AWS Elemental Statmux
and AWS Elemental Live Documentation](../../../elemental-live.md "../../../elemental-live.md").

# Step D: Install the AWS Elemental Software

These steps must be performed on each system where you are installing
AWS Elemental software, either directly at the machine or from your workstation via SSH.
Make sure that you use the `.run` file that corresponds to the `.iso` file that you used to reinstall the
operating system.

1. At the Linux command line, log in with the _elemental_ user credentials.

Run the installer as follows. Use the actual filename of your .run file, rather than the example below.

```
[elemental@hostname ~]$ sudo sh ./elemental_production_statmux_dg_version_short;.nnnnn.run -l -z -t
```

where -l is a letter, not a number. 2. You are prompted as described in the table below.

| Prompt                                                                              | Action                                                                                                                                         |
| ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Do you agree to these terms?`                                                      | This prompt appears after you have paged through the EULA (End User License Agreement). Enter `Yes` or `No`. (You must enter Yes to continue.) |
| `Enter this server’s Hostname`                                                      | Type the hostname of this hardware unit. For example, `statmux-01`                                                                             |
| `Is eth0 a management interface?`                                                   | Type `Yes`.                                                                                                                                    |
| `Does eth0 use DHCP to get its IP address?`                                         | Type `Yes` to use DHCP or type `No` to enter a static IP address.                                                                              |
| `Enter eth0's IP address:`                                                          | If you chose static, type the IP address for this hardware unit.                                                                               |
| `Enter eth0's NETMASK:`                                                             | If you chose static, type the netmask for this hardware unit.                                                                                  |
| `Enter eth0's Gateway (or type `none`):`                                            | If you chose static, type `none` or type the gateway for this hardware unit.                                                                   |
| `Keep this configured nameserver?`                                                  | Skip; you set up a nameserver in the next phase of configuration.                                                                              |
| `Would you like to configure eth1?`                                                 | Type `No`; you can configure eth1 in the next phase of the configuration.                                                                      |
| `The firewall for this system is currently disabled. Would you like to enable it?`  | Skip; you set up the firewall in the next phase of configuration.                                                                              |
| `For security purposes, we require that you change the default password.`           | This prompt is shown if you are still using the default password.                                                                              |
| `Is this machine a part of or intended to be a part of a Conductor Live 3 cluster?` | Type `No`.                                                                                                                                     |
| `Is this a Statmux machine, or intended to be linked to a Statmux machine?`         | Type `Yes`.                                                                                                                                    |
| `Will this machine require use of SNMP alerts?`                                     | If applicable, type `Yes` to open the related port.                                                                                            |
| `Will this machine be ingesting RTMP?`                                              | If applicable, type `Yes` to open the related port.                                                                                            |
| `Will this machine ingest MPEG-TS over UDP? (ports 5000-5100)`                      | If applicable, type `Yes` to open the related port.                                                                                            |
| `Is this machine licensed as part of a licensing pool?`                             | If applicable, type `Yes` to open the related port.                                                                                            |
| `Will this machine serve files using Windows file-sharing (Samba/CIFS)?`            | If applicable, type `Yes` to open the related port.                                                                                            |
| `Will this machine be an NTP server?`                                               | If applicable, type `Yes` to open the related port.                                                                                            |
| `Select time zone ('n' for more)`                                                   | Enter the time zone you want to show on the web interface of the nodes. This setting does not affect activity via SSH or via the REST API.     |
| `Would you like to start the Elemental service now?`                                | Type `Yes`.                                                                                                                                    | Then the software will be installed. Finally, this message will appear: `Installation and configuration complete! Please open a web browser and point it to http://xxx.xxx.xxx.xxx to get to the web interface. Enjoy!` 3. Start a web browser and start the AWS Elemental Statmux web interface by typing the following: `http://<hostname>` Make sure the web interface displays. |
