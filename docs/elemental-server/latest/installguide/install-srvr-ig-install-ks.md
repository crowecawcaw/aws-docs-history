

This is version 2.18 of the AWS Elemental Server documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server/).

# Step B: Install (Kickstart) the Operating System Software
<a name="install-srvr-ig-install-ks"></a>

You must install a configured operating system from an `.iso` file onto each physical machine that will be running AWS Elemental software. Doing so is referred to as “kickstarting the system”.

Make sure that you install the right version of the operating system with each piece of software. The correct `.iso` file is always provided with the `.run` file under **Activations** at [AWS Elemental Support Center Activations](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/activations).

**Create a Boot USB Drive or DVD**  
Do this from your workstation.

Use a third-party utility (such as PowerISO or ISO2USB) to create a bootable DVD or USB drive from your `.iso` file. Instructions for using these utilities can be found in the [AWS Elemental Support Center](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/supportcenter) knowledge base.

**Install the Operating System at Each Node**  
Do this from each Elemental node.

1. Insert the DVD or USB thumb drive into the hardware unit.

1. Boot up or reboot the system. The installer automatically starta.  
![](http://docs.aws.amazon.com/elemental-server/latest/installguide/images/install-installer-shared-png.png)

1. Use the arrow keys to select each option and do the following:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-server/latest/installguide/install-srvr-ig-install-ks.html)

   The operating system is installed. From now on, the system runs this customized version of your Linux operating system.

1. Repeat the above steps on each system, using the `.iso` file that goes with the AWS Elementalsoftware you are installing on each system.