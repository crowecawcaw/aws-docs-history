

# Switching to UEFI on a SuperMicro
<a name="migrate-topic-uefi-supermicro"></a>

To switch the boot mode from BIOS (Legacy mode) to UEFI, you can use the IPMI interface, or you can work when directly connected to the server. 

## Step 1: Install Java applet
<a name="migrate-topic-uefi-supermicro-applet"></a>

Decide if you want to use the IPMI management console, or if you plan to connect directly to the server. If you want to use the console, decide if you want to use the Java remote console applet to access the console, or if you want to use HTML5.

If you want to use the IPMI management console and you want to use the Java remote console applet, you must install the applet. 

1. Make sure you have the IP address of the IPMI. If you don’t have it, connect to the appliance using SSH, then type the following command:

   ```
   sudo ipmiutil lan | grep Param\(3\)
   ```

   The IP address appears in the response. For example:

   ```
   Lan Param(3) IP address: 10 4 130 12
   ```

1. Log in to the IPMI management console via a web browser. Use the ADMIN credentials, with the user name entered in uppercase.

1. From the menu bar, choose **Console Redirection**, then **Launch Console**. The download of a JNLP file starts. 

1. When the download is complete, open the applet. The applet is self signed. Typically, this file is already associated with Java so you should just be able to open it directly.

1. Change the security level in the Java control panel in order for the applet to run:

   1. In Windows, open **Control Panel**, **Programs**, and then **Java**.

   1. Click the **Security** tab. Move the slider to the lowest setting: **Medium**.

   1. Click **OK**. 

You can now open the remote console window. 

## Step 2: Change the mode to UEFI
<a name="migrate-topic-uefi-supermicro-change"></a>

This procedure is nearly identical to the procedure for switching to BIOS. You change the same fields on the **Setup Utility** screen.

1. From the IPMI management console, sign in to the server as the *elemental* user.

1. Reboot the system: 

   ```
   [elemental@hostname]$ sudo reboot
   ```

   The system starts to reboot. The window size might change as the system is rebooting.

1. While the system is rebooting, repeatedly press the **Delete** key on the keyboard (or the **del **button on the virtual keyboard). The **Setup Utility** screen appears.

   You can use these keys to work on the screen:
   + The arrow keys
   + Enter to select
   + ESC to return to the previous screen. 

1. On the main menu, choose **Advanced**.

1. In **sSATA Configuration**, look for fields that have one of these values:
   + **BIOS**
   + **DUAL**
   + **Legacy**
   + **Legacy BIOS**

   Change the value to **EFI**. If there are no fields with these values, go to the next step.

1. In **PCIe/PCI/PnP Configuration**, find every field that has one of these values:
   + **BIOS**
   + **DUAL**
   + **Legacy**
   + **Legacy BIOS**

   In each of these fields, change the value to **EFI**.

1. On the main menu, choose **Boot**. In **Boot Mode Select**, change the value from **DUAL** to **UEFI**.

1. Select **F4**. On the **Save & Exit** dialog, choose **Yes**.