# Install on an SMC

You install RHEL 9 on an SMC chassis from the IPMI interface.

1. Install the Java applet and change the security level, if necessary. For
   information, see [Step 1: Install Java
   applet](migrate-server-218-boot-mode-uefi-smc.md#migrate-server-218-boot-mode-uefi-smc-step1 "migrate-server-218-boot-mode-uefi-smc.md#migrate-server-218-boot-mode-uefi-smc-step1").
2. Make sure that there are no physical USB drives plugged into the
   system.
3. Make sure that you are at a workstation that has direct access to the
   network that the IPMI interface is on.

###### Note

Don't use a VPN connection. 4. Copy the ISO file for RHEL 9 to your laptop. 5. Open the IPMI remote console viewer. On the main menu, choose **Virtual Media** or **Media**, then choose **Virtual
Storage/Virtual Media Wizard**. 6. Choose **CD/ISO media** and browse to the ISO
that you want to use. Choose **Connect/Plug
in**. 7. Reboot the system. The image should start to boot.

If the image does not start to boot, click the **F11** key while the splash screen is displaying. Then when the
**Please select boot device** prompt
appear, choose **UEFI: Virtual CDROM**. Move
this item to the top of the list by pressing the **+** key repeatedly. 8. The installer starts. At the prompt, enter the hostname of the appliance
and press **Enter**. The installation starts
and takes 20 to 30 minutes. 9. When the installation completes, press the **Enter** key to reboot. 10. Plug Out the ISO before it reboots or it takes
you back into the kickstart menu. 11. You can now install any third-party packages. AWS Elemental maintains an RPM
repository for use with RHEL 9. The repository contains the following types
of third-party packages:

    * Packages that are stored in the Red Hat BaseOS repository, and
     that are required to run AWS Elemental software.
    * Packages that are stored in the Red Hat AppStream repository, that
     aren't required but that you want to include.

For more information about the packages that you must obtain from the
AWS Elemental RPM repository, and for instructions about configuring the
repository, see the knowledge base article [Advisory](https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/viewknowledge/Advisory-AWS-Elemental-is-introducing-RHEL-9-2-support-for-Elemental-Live-Conductor-Live-and-Statmux-replacing-CentOS-7 "https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/viewknowledge/Advisory-AWS-Elemental-is-introducing-RHEL-9-2-support-for-Elemental-Live-Conductor-Live-and-Statmux-replacing-CentOS-7").
