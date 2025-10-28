This is version 2.18 of the AWS Elemental Conductor File documentation. This is the
latest version. For prior versions, see the _Archive_ section of
[AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Step B: Deploy the VM and Install

AWS Elemental Conductor File

Set-up the AWS Elemental Conductor File nodes before setting up the worker AWS Elemental Server nodes.

Perform these steps from your workstation.

###### Install the Conductor Software on the Primary Node

1. Place the OVA image in a convenient location accessible to the VM host.
2. Start the VMware vSphere client and choose the option that lets you run the
   OVF Deploy wizard to create the VM guest.
3. Complete the fields in the wizard. Pay special attention to the following
   settings:
   - For the _source_, enter the location
     where you saved the OVA file.
   - Ensure that the _hostname_ that you
     assign to the VM guest is unique across all of your AWS Elemental
     products.
   - For _network settings_, such as DNS
     servers and eth configuration, leave the fields blank. You will
     configure these settings later in the AWS Elemental Conductor File installation and
     configuration process.

4. Choose **Finish**. The OVA is installed, the
   guest is created, and AWS Elemental Conductor File is installed on that guest with the eth0
   configured as specified.
5. Before proceeding, take a snapshot of the VM, as described in the VMware
   vSphere help text.

###### Verify Installation

The VMware vSphere client provides feedback about creation of the VM guest. However,
it does not provide status feedback during installation of the AWS Elemental
software. Therefore, to monitor progress of the installation once the VM guest has
been created, follow these steps:

1. From the VMware vSphere client, choose **Open Console** and
   access the AWS Elemental Conductor File VM. The screen shows a progress bar.
2. Press Esc on your keyboard to switch the display to showing text.
3. Watch for the following:
   - Early in the installation process, the display pauses on the line
     `Starting: ATD`. This indicates that the installation is
     in progress.
   - The log-in prompt appears when the installation is complete.

4. At the log in prompt, enter the _elemental_ user credentials.

You are logged in at the home directory (/elemental). If the install succeeds,
the AWS Elemental banner is displayed.

###### Install on Secondary Node

Perform the same installation and verification on the secondary AWS Elemental Conductor File
node.
