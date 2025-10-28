This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Step b: Generate a License

Activation Key File

The operating system that you installed on your virtual machine (VM) has a utility you can use to
generate an activation key file.

###### To generate an activation key file

1. From the VMware vSphere client, choose **Open Console** and access the desired VM,
   using the _elemental_ user credentials.

You are logged in at the home directory (/elemental). 2. Enter this command.

```
[elemental@hostname ~] **./keygen**
```

3. At the prompt, enter the activation code for the first VM, including the dashes.
   The following file is created in the home directory: `activation_<hostname 
of the system>`.key``
4. Copy the activation key file from the VM to your workstation using SCP.

Use the _elemental_ user credentials. 5. Repeat these steps for each VM.

    * Make sure to repeat step 1 for each activation key file that you
     want to generate: each key file must contain the hostname of the individual VM.
    * Make sure to use a different activation code on each
     VM.
