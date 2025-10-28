# Step C: Install the Conductor Live software

Perform these on the Conductor Live appliance, either directly at the appliance or
from your workstation via SSH.

###### To install the Conductor Live software

1. At the Linux command line, log in with the _elemental_ user
   credentials.
2. Run the installer with this command. Use the actual file name of your
   `.run` file rather than the example below.

```
[elemental@hostname ~]$ sudo sh ./elemental_production_conductor_live247_3.25.5.12345.run -l -z -t
```

where -l is a letter, not a number. 3. Follow the prompts:

| Prompt                                                                             | Action                                                                                                                                         |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Do you agree to these terms?`                                                     | This prompt appears after you have paged through the EULA (End User License Agreement). Enter `Yes` or `No`. (You must enter Yes to continue.) |
| `Enter this server’s Hostname`                                                     | Type the hostname of this appliance. For example, `conductor-live-3-01`                                                                        |
| `Does eth0 use DHCP to get its IP address?`                                        | Type `Yes` to use DHCP or type `No` to enter a static IP address.                                                                              |
| `Enter eth0's IP address:`                                                         | If you chose static, type the IP address for this hardware unit.                                                                               |
| `Enter eth0's NETMASK:`                                                            | If you chose static, type the netmask for this hardware unit.                                                                                  |
| `Enter eth0's Gateway (or type `none`):`                                           | If you chose static, type `none` or type the gateway for this appliance.                                                                       |
| `Keep this configured nameserver?`                                                 | Skip; you set up a nameserver in the next phase of configuration.                                                                              |
| `Would you like to configure eth1?`                                                | Type `No`; you can configure eth1 in the next phase of the configuration.                                                                      |
| `The firewall for this system is currently disabled. Would you like to enable it?` | Skip; you set up the firewall in the next phase of configuration.                                                                              |
| `Would you like to start the Elemental service now?`                               | Type `Yes`.                                                                                                                                    | Then the software is installed. Finally, this message appears: `Installation and configuration complete! Please open a web browser and point it to https://xxx.xxx.xxx.xxx to get to the web interface. Enjoy!` 4. Start a web browser and start the Conductor Live web interface by typing the following: `https://<hostname>` Make sure the web interface displays. |
