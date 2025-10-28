This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Step D: Install the AWS Elemental Software

1. Use SCP to move each AWS Elemental software installer (.run file) to the /home/elemental directory on the appropriate virtual machine.
   Use the _elemental_ user credentials.
2. From the VMware vSPhere client, choose **Open Console** and access the virtual machine with the _elemental_ user credentials.

You are logged in at the home directory (/home/elemental). 3. Run the installer as follows. Use the actual filename of your .run file rather
than the example below.

```
[elemental@hostname ~]$ sudo sh ./`<product>` -xeula -l -z
```

where :

    * `<product>` is the file name of the file
     that you downloaded. For example,
     `elemental_production_server_2.18.0.123456.run`.
    * -l is a letter, not a number.

4. You are prompted as described in the table below.

| Prompt                                                                             | Action                                                                                                                                     |
| ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `Enter this server’s Hostname`                                                     | Accept the suggestion, which is the value that you entered when you installed the OVA.                                                     |
| `Is eth0 a management interface?`                                                  | Type `Yes`.                                                                                                                                |
| `Does eth0 use DHCP to get its IP address?`                                        | Accept the suggestion.                                                                                                                     |
| `Enter eth0's IP address:`                                                         | If the prompt appears, accept the suggestion.                                                                                              |
| `Enter eth0's NETMASK:`                                                            | If the prompt appears, accept the suggestion.                                                                                              |
| `Enter eth0's Gateway (or type `none`):`                                           | If the prompt appears, accept the suggestion.                                                                                              |
| `Keep this configured nameserver: 10.6.16.10?`                                     | Skip; you set up a nameserver in the next phase of configuration.                                                                          |
| `Would you like to configure eth1?`                                                | Type `No`; you can configure eth1 in the next phase of the configuration.                                                                  |
| `The firewall for this system is currently disabled. Would you like to enable it?` | Skip; you set up the firewall in the next phase of configuration.                                                                          |
| `Select time zone ('n' for more)`                                                  | Enter the time zone you want to show on the web interface of the nodes. This setting does not affect activity via SSH or via the REST API. |
| `Would you like to start the Elemental service now?`                               | Type `Yes`.                                                                                                                                | The software is installed. This message confirms: `Installation and configuration complete! Please open a web browser and point it to https://xxx.xxx.xxx.xxx to get to the web interface. Enjoy!` 5. Take a snapshot of the VM, as described in the CentOS 7 Virtual Manager online help. 6. Start a web browser and start the AWS Elemental Server web interface by typing the following: `https://<hostname>` Make sure the web interface displays. |
