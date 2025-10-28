# Installing on an SuperMicro

You install RHEL 9 on a SuperMicro chassis from the IPMI interface.

1. Install the Java applet and change the security level. See [Step 1: Install Java
   applet](migrate-topic-uefi-supermicro.md#migrate-topic-uefi-supermicro-applet "migrate-topic-uefi-supermicro.md#migrate-topic-uefi-supermicro-applet").
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
and takes 20 to 30 minutes. 9. When the installation completes, press the **Enter** key to reboot. 10. Plug Out the ISO before it reboots or it takes you back into the kickstart
menu. 11. You can now install any third-party packages. To obtain these packages,
see [Working with RPM repository](migrate-topic-rpm-repository.md "migrate-topic-rpm-repository.md").
