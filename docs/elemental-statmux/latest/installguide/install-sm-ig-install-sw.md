

This is version 2.20 of the AWS Elemental Statmux documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Statmux and AWS Elemental Live Documentation](https://docs.aws.amazon.com/elemental-live).

# Step C: Install the AWS Elemental Software
<a name="install-sm-ig-install-sw"></a>

Perform these on each node where you are installing AWS Elemental software, either directly at the machine or from your workstation via SSH. 

Make sure that you use the `.run` file that corresponds to the `.iso` file that you used to set up the operating system on the node. That is, install AWS Elemental Statmux software on the nodes that you kickstarted with the Statmux `.iso` and worker software on nodes that you kickstarted with the worker `.iso`.

**To install the software**

1. At the Linux command line, log in with the *elemental* user credentials.

1. Run the installer as follows. Use the actual file name of your `.run` file, rather than the example below.

   ```
   [elemental@hostname ~]$ sudo sh ./elemental_production_statmux_2.20.nnnnn.run -l -z -t
   ```

   where -l is a letter, not a number.

1. You are prompted as described in the table below.     
[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-statmux/latest/installguide/install-sm-ig-install-sw.html)

   Then the software will be installed. Finally, this message will appear:

   ```
   Installation and configuration complete!
   Please open a web browser and point it to http://xxx.xxx.xxx.xxx to get to the web interface.
   Enjoy!
   ```

1. Start a web browser and start the AWS Elemental Statmux web interface by typing the following:

   ```
   http://<hostname>
   ```

   Make sure the web interface displays.