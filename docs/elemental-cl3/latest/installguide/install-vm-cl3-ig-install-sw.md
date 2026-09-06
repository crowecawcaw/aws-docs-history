

# Step C: Install the AWS Elemental Software
<a name="install-vm-cl3-ig-install-sw"></a>

1. Use SCP to move each AWS Elemental software installer (`.run` file) to the `/home/elemental` directory on the appropriate virtual machine (VM). Use the *elemental* user credentials.

1. From the VMware vSPhere client, choose **Open Console** and access the VM with the elemental username and default password.

   You are logged in at the home directory (/home/elemental).

1. Run the installer as follows. When you do this use the actual file name of your `.run` file, rather than the file name in the example below.

   ```
   [elemental@hostname ~]$ sudo sh ./{{<product>}} -xeula -l -z
   ```

   Where:
   + {{<product>}} is the file name of the file that you downloaded. For example, `elemental_production_conductor_live247_3.25.5.12345.run`.
   + -l is a letter, not a number. 

1. You are prompted as described in the table below.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-cl3/latest/installguide/install-vm-cl3-ig-install-sw.html)

   The software is installed. This message confirms both installation and configuration are complete:

   ```
   Installation and configuration complete!
   Please open a web browser and point it to https://xxx.xxx.xxx.xxx to get to the web interface.
   Enjoy!
   ```

1. Take a snapshot of the VM as described in the CentOS 7 Virtual Manager online help.

1. Start a web browser and start the Conductor Live web interface by typing:

   ```
   https://<hostname>
   ```

   Make sure the web interface displays.