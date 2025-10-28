# Step C: Install the AWS Elemental

Software

1. Use SCP to move each AWS Elemental software installer (`.run`
   file) to the `/home/elemental` directory on the appropriate virtual
   machine (VM). Use the _elemental_ user credentials.
2. From the VMware vSPhere client, choose **Open Console** and
   access the VM with the elemental username and default password.

You are logged in at the home directory (/home/elemental). 3. Run the installer as follows. When you do this use the actual file name of
your `.run` file, rather than the file name in the example
below.

```
[elemental@hostname ~]$ sudo sh ./`<product>` -xeula -l -z
```

Where:

    * `<product>` is the file name of the file
     that you downloaded. For example,
     `elemental_production_conductor_live247_3.25.5.12345.run`.
    * -l is a letter, not a number.

4. You are prompted as described in the table below.

| Prompt                                                                             | Action                                                                                 |
| ---------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Enter this server’s Hostname`                                                     | Accept the suggestion, which is the value that you entered when you installed the OVA. |
| `Does eth0 use DHCP to get its IP address?`                                        | Accept the suggestion.                                                                 |
| `Enter eth0's IP address:`                                                         | If the prompt appears, accept the suggestion.                                          |
| `Enter eth0's NETMASK:`                                                            | If the prompt appears, accept the suggestion.                                          |
| `Enter eth0's Gateway (or type `none`):`                                           | If the prompt appears, accept the suggestion.                                          |
| `Keep this configured nameserver?`                                                 | Skip; you set up a nameserver in the next phase of configuration.                      |
| `Would you like to configure eth1?`                                                | Type `No`; you can configure eth1 in the next phase of the configuration.              |
| `The firewall for this system is currently disabled. Would you like to enable it?` | Skip; you set up the firewall in the next phase of configuration.                      |
| `For security purposes, we require that you change the default password.`          | This prompt is shown if you are still using the default password.                      |
| `Would you like to start the Elemental service now?`                               | Type `Yes`.                                                                            | The software is installed. This message confirms both installation and configuration are complete: `Installation and configuration complete! Please open a web browser and point it to https://xxx.xxx.xxx.xxx to get to the web interface. Enjoy!` 5. Take a snapshot of the VM as described in the CentOS 7 Virtual Manager online help. 6. Start a web browser and start the Conductor Live web interface by typing: `https://<hostname>` Make sure the web interface displays. |
