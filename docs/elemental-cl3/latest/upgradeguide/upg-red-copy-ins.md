# Step B: Copy the AWS Elemental installers

Locate and copy the AWS Elemental installers for worker and Conductor Live nodes.

1. From your regular workstation, open a web browser, go to [AWS Elemental Support Center Activations](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/activations "https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/activations") and download the software for the version that
   you're upgrading to.
2. Make a note of where downloads are stored on your workstation. For example:

```
h:/corporate/downloads/.
```

3. Make a note of the name of the download file. For example:
   `elemental_production_conductor_live247_3.25.5.12345.run`
4. Copy the download file from your workstation to `/home/elemental/` on one of the nodes. For example:
   - Use SFTP protocol and an FTP client application on your workstation computer.
     Connect to the IP address for Conductor Live on port 22 with the _elemental_ user
     credentials and transfer the file.
   - Use SCP protocol and an SCP client application on your workstation computer. Copy
     the file with the _elemental_ user credentials and transfer the file.

5. Repeat the download to any other nodes that are changing versions. If you're
   changing versions on several nodes, copy the download file to every appliance at
   once. Doing so reduces downtime on each node as you start installing the new
   software.
   For detailed downloading steps, see [Downloading Conductor Live Software](detailed-dl-cl3-upg.md "detailed-dl-cl3-upg.md").
