# Step B: Copy the AWS Elemental

installer

Locate and copy the installer for Elemental Live.

1. Find the version of the AWS Elemental Live software that you're downgrading
   to:
   - From a Linux prompt, log in to the hardware until with the
     _elemental_ user credentials.
   - Look for the desired installer as shown here.

   ```
   `[elemental@hostname ~]` ls
   ```

   For example, look for
   `...elemental_production_live_2.23.5.12345.run...`

2. If you find the software, skip to [Step C: Downgrade the node](downgrades-lv-upg-dg-node.md "downgrades-lv-upg-dg-node.md").

If the software isn't on the hardware unit, go to the next
step. 3. From your regular workstation, open a web browser, go to [AWS Elemental Support Center Activations](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/activations "https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/activations") and
download the software for the version that you're downgrading to. 4. Make a note of where downloads are stored on your workstation. For
example:

```
h:/corporate/downloads/.
```

5. Make a note of the name of the download file. For example:
   `elemental_production_live_2.23.5.12345.run`
6. Copy the download file from your workstation to
   `/home/elemental/` on one of the nodes. For
   example:
   - Use SFTP protocol and an FTP client application on your
     workstation computer. Connect to the IP address for Elemental Live
     on port 22 with the _elemental_ user
     credentials and transfer the file.
   - Use SCP protocol and an SCP client application on your
     workstation computer. Copy the file with the
     _elemental_ user credentials and transfer the
     file.

7. Repeat the download to any other nodes that are changing versions.
   If you're changing versions on several nodes, copy the download
   file to every hardware unit at once. Doing so reduces downtime on each
   node as you start installing the new software.
