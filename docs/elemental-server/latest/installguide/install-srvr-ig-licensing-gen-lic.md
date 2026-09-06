

This is version 2.18 of the AWS Elemental Server documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server/).

# Step b: Generate a License Activation Key File
<a name="install-srvr-ig-licensing-gen-lic"></a>

The operating system that you installed on your hardware has a utility you can use to generate an activation key file. 

**To generate an activation key file**

1. Using an SSH client such as PuTTY, log in to the hardware unit with the *elemental* user credentials. 

   You are logged in at the home directory (/elemental).

1. Enter this command.

   ```
   [elemental@hostname ~] ./keygen
   ```

1. At the prompt, enter the activation code. The following file is created in the home directory: `activation_<hostname of the system>.key `.

1. Copy the file to your workstation. For example:
   + Use SCP or a similar utility on a Linux workstation.

   Use the *elemental* user credentials and copy and paste the file from the network share.

1. Repeat these steps for each AWS Elemental Server hardware unit. 
   + Make sure to log in to each hardware unit for each activation key file that you want to generate: each activation key file that you create must contain the hostname of the individual hardware unit.
   + Make sure to use a different activation code on each unit.