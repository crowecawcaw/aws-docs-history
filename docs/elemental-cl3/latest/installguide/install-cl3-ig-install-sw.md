

# Step C: Install the Conductor Live software
<a name="install-cl3-ig-install-sw"></a>

Perform these on the Conductor Live appliance, either directly at the appliance or from your workstation via SSH. 

**To install the Conductor Live software**

1. At the Linux command line, log in with the *elemental* user credentials.

1. Run the installer with this command. Use the actual file name of your `.run` file rather than the example below.

   ```
   [elemental@hostname ~]$ sudo sh ./elemental_production_conductor_live247_3.25.5.12345.run -l -z -t
   ```

   where -l is a letter, not a number.

1. Follow the prompts:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-cl3/latest/installguide/install-cl3-ig-install-sw.html)

   Then the software is installed. Finally, this message appears:

   ```
   Installation and configuration complete!
   Please open a web browser and point it to https://xxx.xxx.xxx.xxx to get to the web interface.
   Enjoy!
   ```

1. Start a web browser and start the Conductor Live web interface by typing the following:

   ```
   https://<hostname>
   ```

   Make sure the web interface displays.