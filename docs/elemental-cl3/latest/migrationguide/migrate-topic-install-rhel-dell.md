# Installing on a

Dell

You can install RHEL 9 on a Dell chassis either from the iDRAC interface or using
a USB stick.

## Install using the iDRAC

interface

### Get Ready

1. Make sure that there are no physical USB drives plugged into the
   system.
2. Make sure that you are at a workstation that has direct access to
   the network that the iDRAC interface is on. (So don't use a VPN
   connection.)
3. Log into iDRAC through the web interface. Use an administrative
   username and password.
4. Launch the Virtual Console. On the main menu, select
   **Virtual Media**. On the next screen, select
   **Connect Virtual Media**. The
   **Virtual Media** screen appears.
5. In the **Map CD/DVD** section, in **Image
   File**, click **Choose File**. In the
   window that appears, navigate to the kickstart .iso file, select it,
   and click **Open**. The **Image
   File** field in the **Virtual Media**
   screen now specifies the image file.
6. Click **Map Device**. Then at the bottom of the
   screen, click **Close**.

The kickstart .ISO image file is now mapped to the virtual CD/DVD drive.

1. On the main menu of the Virtual Console, click
   **Boot**. On the **Boot
   Controls** list, click **Virtual
   CD/DVD/ISO**. Then at the **Confirm Boot
   Action** prompt, click **Yes**.
2. On the main menu of the Virtual Console, click
   **Power**, then click **Reset System
   (warm boot)**, and at the **Confirm**
   prompt, click **Yes**.

The system reboots into the kickstart .iso. Lines of text appear, and
finally the prompt **Enter the server complete hostname**
appears.

### Install the operating

system

1. At the **Enter the server complete hostname**
   prompt, enter the hostname that already applies to this node, then
   press **Enter**. The installation starts.
2. When the installation is complete, press
   **Enter** to quit and reboot.

### Finishing

steps

1. Installation of the RHEL 9 operating system will remove all
   network configurations. You must manually configure at least one
   interface before you can install the Elemental Live software. For
   information, go to the [AWS Elemental Support Center](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/supportcenter "https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/supportcenter"), and read the Knowledge article
   [What to do if kickstart removes on-disk network
   configuration](https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/viewknowledge/What-to-do-if-kickstart-removes-on-disk-network-configuration "https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/viewknowledge/What-to-do-if-kickstart-removes-on-disk-network-configuration") or open a case.
2. Sometimes, a kickstart or upgrade generates incorrect mappings for
   Ethernet ports. For information about how to fix this issue, go to
   the [AWS Elemental Support Center](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/supportcenter "https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/supportcenter"), and read the Knowledge article [How to restore default ethernet port order on an Elemental
   appliance](https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/viewknowledge/How-to-restore-default-ethernet-port-order-on-an-Elemental-appliance "https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/viewknowledge/How-to-restore-default-ethernet-port-order-on-an-Elemental-appliance") or open a case.
3. You can now install any third-party packages. To obtain these
   packages, see [Working with RPM repository](migrate-topic-rpm-repository.md "migrate-topic-rpm-repository.md").

## USB stick

### Install the operating

system

1. Make sure that you have created a boot USB drive. See [Create a boot USB drive](migrate-topic-create-boot.md "migrate-topic-create-boot.md").
2. Insert the USB drive into an available USB port. You might need to
   press **F2** while booting in order to select the
   boot device. The recovery (kickstart) screen appears.
3. Enter the hostname that already applies to this node, then press
   **Enter**. The installation starts.
4. When the installation is complete, remove the USB drive from the
   system and store it in a secure location.
5. Then on the screen, press the reboot button shown or press the
   **Enter** key.

### Finishing

steps

1. Installation of the RHEL 9 operating system will remove all
   network configurations. You must manually configure at least one
   interface before you can install the Elemental Live software. For
   information, go to the [AWS Elemental Support Center](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/supportcenter "https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/supportcenter"), and read the Knowledge article
   [What to do if kickstart removes on-disk network
   configuration](https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/viewknowledge/What-to-do-if-kickstart-removes-on-disk-network-configuration "https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/viewknowledge/What-to-do-if-kickstart-removes-on-disk-network-configuration") or open a case.
2. Sometimes, a kickstart or upgrade generates incorrect mappings for
   Ethernet ports. For information about how to fix this issue, go to
   the [AWS Elemental Support Center](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/supportcenter "https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/supportcenter"), and read the Knowledge article [How to restore default ethernet port order on an Elemental
   appliance](https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/viewknowledge/How-to-restore-default-ethernet-port-order-on-an-Elemental-appliance "https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/viewknowledge/How-to-restore-default-ethernet-port-order-on-an-Elemental-appliance") or open a case.
3. You can now install any third-party packages. To obtain these
   packages, see [Working with RPM repository](migrate-topic-rpm-repository.md "migrate-topic-rpm-repository.md").
