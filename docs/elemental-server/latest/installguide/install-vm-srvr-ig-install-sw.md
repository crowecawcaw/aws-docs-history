

This is version 2.18 of the AWS Elemental Server documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server/).

# Step C: Install the AWS Elemental Software
<a name="install-vm-srvr-ig-install-sw"></a>

1. Use SCP to move each AWS Elemental software installer (.run file) to the /home/elemental directory on the appropriate virtual machine. Use the *elemental* user credentials.

1. From the VMware vSPhere client, choose **Open Console** and access the virtual machine with the *elemental* user credentials.

   You are logged in at the home directory (/home/elemental).

1. Run the installer as follows. Use the actual filename of your .run file, rather than the example below.

   ```
   [elemental@hostname ~]$ sudo sh ./{{<product>}} -xeula -l -z
   ```

   where :
   + {{<product>}} is the file name of the file that you downloaded. For example, `elemental_production_server_2.18.0.123456.run`.
   + -l is a letter, not a number. 

1. You are prompted as described in the table below.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-server/latest/installguide/install-vm-srvr-ig-install-sw.html)

   The software is installed. This message confirms:

   ```
   Installation and configuration complete!
   Please open a web browser and point it to https://xxx.xxx.xxx.xxx to get to the web interface.
   Enjoy!
   ```

1. Take a snapshot of the VM, as described in the CentOS 7 Virtual Manager online help.

1. Start a web browser and start the AWS Elemental Server web interface by typing the following:

   ```
   https://<hostname>
   ```

   Make sure the web interface displays.