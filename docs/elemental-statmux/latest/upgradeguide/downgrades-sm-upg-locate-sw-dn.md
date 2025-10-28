This is version 2.20 of the AWS Elemental Statmux documentation.
This is the latest version. For prior versions, see the
_Previous Versions_ section of [AWS Elemental Statmux
and AWS Elemental Live Documentation](../../../elemental-live.md "../../../elemental-live.md").

# Step B: Copy the AWS Elemental Installer

Locate and copy the installer for AWS Elemental Statmux.

1. Find the version of the software that you're downgrading to.

Follow these
steps:

    1. From a Linux prompt, log in to the hardware until with the *elemental* user
     credentials.
    2. Look for the desired installer as shown here.



    ```
    `[elemental@hostname ~]` ls
    ```

    Look for the file named similar to this `...elemental_production_statmux_2.17.0.123456.run...`

2. If you find the software, skip to [Step C: Downgrade the Node](downgrades-sm-upg-dg-node.md "downgrades-sm-upg-dg-node.md").

If the software isn't on the hardware unit, go to the next step. 3. From your regular workstation, open a web browser, go to [AWS Elemental Support Center Activations](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/activations "https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/activations") and download the software for the version that
you're going to. 4. Make a note of where downloads are stored on your workstation. For example:

```
h:/corporate/downloads/.
```

5. Make a note of the name of the download file. For example:
   `elemental_production_statmux_2.17.0.123456.run`
6. Copy the download file from your workstation to `/home/elemental/` on one of the nodes. For example:
   - Use SFTP protocol and an FTP client application on your workstation computer.
     Connect to the IP address for AWS Elemental Delta on port 22 with the _elemental_ user
     credentials and transfer the file.
   - Use SCP protocol and an SCP client application on your workstation computer. Copy
     the file with the _elemental_ user credentials and transfer the file.

7. Repeat the download to any other nodes that are changing versions. If you're changing versions on several nodes, copy the download file to every hardware unit at once. Doing so reduces downtime on each node as you start installing the new software.
