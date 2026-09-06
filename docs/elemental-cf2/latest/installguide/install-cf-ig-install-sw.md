

This is version 2.18 of the AWS Elemental Conductor File documentation. This is the latest version. For prior versions, see the *Archive* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server).

# Step C: Install the AWS Elemental Software
<a name="install-cf-ig-install-sw"></a>

These steps must be performed on each node where you are installing AWS Elemental software, either directly at the machine or from your workstation via SSH. 

Make sure that you use the `.run` file that corresponds to the .iso file that you used to set up the operating system on the node. That is, install Conductor File software on the nodes that you kickstarted with the Conductor File `.iso` and worker software on nodes that you kickstarted with the worker `.iso`.

**To install the software**

1. At the Linux command line, log in with the *elemental* user credentials.

1. Run the installer as follows. Use the actual filename of your `.run` file, rather than the example below.

   ```
   [elemental@hostname ~]$ sudo sh ./elemental_production_conductor_file_2.11.nnnnn.run -l -z -t
   ```

   where -l is a letter, not a number.

1. You are prompted as described in the table below.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-cf2/latest/installguide/install-cf-ig-install-sw.html)

   Then the software will be installed. Finally, this message appears when installation and configuration are complete:

   ```
   Installation and configuration complete!
   Please open a web browser and point it to https://xxx.xxx.xxx.xxx to get to the web interface.
   Enjoy!
   ```

1. Start a web browser and start the AWS Elemental Conductor File web interface by typing the following:

   ```
   https://<hostname>
   ```

   Make sure the web interface displays.