# Installing on a SuperMicro

You install RHEL 9 on a SuperMicro chassis from the IPMI interface.

## Install the operating

system

1. Install the Java applet and change the security level. See [Step A: Install Java
   applet](migrate-topic-uefi-supermicro.md#migrate-topic-uefi-supermicro-applet "migrate-topic-uefi-supermicro.md#migrate-topic-uefi-supermicro-applet").
2. Make sure that there are no physical USB drives plugged into the
   system.
3. Make sure that you are at a workstation that has direct access to the
   network that the IPMI interface is on.

###### Note

Don't use a VPN connection. 4. Copy the ISO file for RHEL 9 to your laptop. 5. Open the IPMI remote console viewer. On the main menu, choose
**Virtual Media** or **Media**, then choose **Virtual Storage/Virtual Media Wizard**. 6. Choose **CD/ISO media** and browse to the
ISO that you want to use. Choose **Connect/Plug
in**. 7. Reboot the system. The image should start to boot.

If the image does not start to boot, click the **F11** key while the splash screen is displaying. Then when
the **Please select boot device** prompt
appear, choose **UEFI: Virtual CDROM**.
Move this item to the top of the list by pressing the **+** key repeatedly. 8. The installer starts. At the prompt, enter the hostname of the
appliance and press **Enter**. The
installation starts and takes 20 to 30 minutes. 9. When the installation completes, press the **Enter** key to reboot. 10. Plug out the ISO before it reboots, otherwise you return to the
kickstart menu.

## Finishing steps

1. Installation of the RHEL 9 operating system will remove all network
   configurations. You must manually configure at least one interface
   before you can install the Elemental Live software. For information, go to the
   [AWS Elemental Support Center](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/supportcenter "https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/supportcenter"), and read the Knowledge article [What to do if kickstart removes on-disk network
   configuration](https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/viewknowledge/What-to-do-if-kickstart-removes-on-disk-network-configuration "https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/viewknowledge/What-to-do-if-kickstart-removes-on-disk-network-configuration") or open a case.
2. Sometimes, a kickstart or upgrade generates incorrect mappings for
   Ethernet ports. For information about how to fix this issue, go to the
   [AWS Elemental Support Center](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/supportcenter "https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/supportcenter"), and read the Knowledge article [How to restore default ethernet port order on an Elemental
   appliance](https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/viewknowledge/How-to-restore-default-ethernet-port-order-on-an-Elemental-appliance "https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/viewknowledge/How-to-restore-default-ethernet-port-order-on-an-Elemental-appliance") or open a case.
3. You can now install any third-party packages. To obtain these
   packages, see [Working with RPM repository](migrate-topic-rpm-repository.md "migrate-topic-rpm-repository.md").
