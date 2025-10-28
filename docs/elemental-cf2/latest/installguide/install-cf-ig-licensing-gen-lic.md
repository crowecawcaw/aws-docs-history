This is version 2.18 of the AWS Elemental Conductor File documentation. This is the
latest version. For prior versions, see the _Archive_ section of
[AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Step b: Generate a License

Activation Key File

The operating system that you installed on your hardware has a utility you can use to generate an activation key file.

###### To generate an activation key file

1. Using an SSH client such as PuTTY, log in to the hardware unit with the _elemental_ user credentials.

You are logged in at the home directory (/elemental). 2. Enter this command.

```
[elemental@hostname ~] **./keygen**
```

3.  At the prompt, enter the activation code. The following file is created
    in the home directory: `activation_<hostname of the system>`.key`` .
4.  Copy the file to your workstation. For example:

        * Use SCP or a similar utility on a Linux workstation.

    Use the _elemental_ user credentials and copy and paste the file from the network share.

5.  Repeat these steps for each AWS Elemental Conductor File hardware unit.
    - Make sure to log in to each hardware unit for each activation key file that you want to generate: each activation key file that you create must contain the hostname of the individual hardware unit.
    - Make sure to use a different activation code on each unit.
