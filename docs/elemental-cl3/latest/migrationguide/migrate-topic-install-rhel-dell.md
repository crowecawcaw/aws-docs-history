

# Installing on a Dell
<a name="migrate-topic-install-rhel-dell"></a>

You can install RHEL 9 on a Dell chassis either from the iDRAC interface or using a USB stick.

## Install using the iDRAC interface
<a name="migrate-topic-rhel-dell-idrac"></a>

### Get Ready
<a name="migrate-topic-rhel-dell-idrac-stepa"></a>

1. Make sure that there are no physical USB drives plugged into the system.

1. Make sure that you are at a workstation that has direct access to the network that the iDRAC interface is on. (So don't use a VPN connection.) 

1. Log into iDRAC through the web interface. Use an administrative username and password.

1. Launch the Virtual Console. On the main menu, select **Virtual Media**. On the next screen, select **Connect Virtual Media**. The **Virtual Media** screen appears.

1. In the **Map CD/DVD** section, in **Image File**, click **Choose File**. In the window that appears, navigate to the kickstart .iso file, select it, and click **Open**. The **Image File** field in the **Virtual Media** screen now specifies the image file. 

1. Click **Map Device**. Then at the bottom of the screen, click **Close**.

The kickstart .ISO image file is now mapped to the virtual CD/DVD drive. 

1. On the main menu of the Virtual Console, click **Boot**. On the **Boot Controls** list, click **Virtual CD/DVD/ISO**. Then at the **Confirm Boot Action** prompt, click **Yes**.

1. On the main menu of the Virtual Console, click **Power**, then click **Reset System (warm boot)**, and at the **Confirm** prompt, click **Yes**.

The system reboots into the kickstart .iso. Lines of text appear, and finally the prompt **Enter the server complete hostname** appears.

### Install the operating system
<a name="migrate-topic-rhel-dell-idrac-stepb"></a>

1. At the **Enter the server complete hostname** prompt, enter the hostname that already applies to this node, then press **Enter**. The installation starts.

1. When the installation is complete, press **Enter** to quit and reboot.

### Finishing steps
<a name="migrate-topic-rhel-dell-idrac-finish"></a>

1. Installation of the RHEL 9 operating system will remove all network configurations. You must manually configure at least one interface before you can install the Elemental Live software. For information, go to the [AWS Elemental Support Center](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/supportcenter), and read the Knowledge article [ What to do if kickstart removes on-disk network configuration](https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/viewknowledge/What-to-do-if-kickstart-removes-on-disk-network-configuration) or open a case.

1. Sometimes, a kickstart or upgrade generates incorrect mappings for Ethernet ports. For information about how to fix this issue, go to the [AWS Elemental Support Center](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/supportcenter), and read the Knowledge article [How to restore default ethernet port order on an Elemental appliance](https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/viewknowledge/How-to-restore-default-ethernet-port-order-on-an-Elemental-appliance) or open a case.

1. You can now install any third-party packages. To obtain these packages, see [Working with RPM repository](migrate-topic-rpm-repository.md).

## USB stick
<a name="migrate-topic-rhel-dell-stick"></a>

### Install the operating system
<a name="migrate-topic-rhel-dell-stick-stepa"></a>

1. Make sure that you have created a boot USB drive. See [Create a boot USB drive](migrate-topic-create-boot.md).

1. Insert the USB drive into an available USB port. You might need to press **F2** while booting in order to select the boot device. The recovery (kickstart) screen appears.

1. Enter the hostname that already applies to this node, then press **Enter**. The installation starts.

1. When the installation is complete, remove the USB drive from the system and store it in a secure location. 

1. Then on the screen, press the reboot button shown or press the **Enter** key.

### Finishing steps
<a name="migrate-topic-rhel-dell-stick-finish"></a>

1. Installation of the RHEL 9 operating system will remove all network configurations. You must manually configure at least one interface before you can install the Elemental Live software. For information, go to the [AWS Elemental Support Center](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/supportcenter), and read the Knowledge article [ What to do if kickstart removes on-disk network configuration](https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/viewknowledge/What-to-do-if-kickstart-removes-on-disk-network-configuration) or open a case.

1. Sometimes, a kickstart or upgrade generates incorrect mappings for Ethernet ports. For information about how to fix this issue, go to the [AWS Elemental Support Center](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/supportcenter), and read the Knowledge article [How to restore default ethernet port order on an Elemental appliance](https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/viewknowledge/How-to-restore-default-ethernet-port-order-on-an-Elemental-appliance) or open a case.

1. You can now install any third-party packages. To obtain these packages, see [Working with RPM repository](migrate-topic-rpm-repository.md).