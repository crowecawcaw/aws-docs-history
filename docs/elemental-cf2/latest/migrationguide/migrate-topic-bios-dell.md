

# Switching to Legacy on a Dell
<a name="migrate-topic-bios-dell"></a>

There are three ways to switch the boot mode from UEFI back to BIOS (Legacy mode).

**Topics**
+ [Switch using the IDRAC user interface](#migrate-topic-bios-dell-idrac)
+ [Switch using RACADM](#migrate-topic-bios-dell-racadm)
+ [Switch using the F2 boot menu](#migrate-topic-bios-dell-f2)

## Switch using the IDRAC user interface
<a name="migrate-topic-bios-dell-idrac"></a>

iDRAC is a system for controlling Dell servers remotely. It is already installed and enabled on the Dell server. 

This procedure is identical to the procedure for switching to `UEFI`, except that you specify `BIOS` instead of `UEFI`.

1. Log into the iDRAC user interface as an administrative user.

1. On the iDRAC menu, choose **Configuration, then BIOS Settings**, then **Boot Settings.**

1. On the **Boot Mode** line, change the **Current Value** from **UEFI** to **BIOS**.

1. Scroll down to the **Apply ** button and choose that button. The **Pending Value** changes to **BIOS**.

1. Scroll down to the bottom of the page and choose **Apply And Reboot**.

The system reboots. Legacy mode is now enabled.

## Switch using RACADM
<a name="migrate-topic-bios-dell-racadm"></a>

You can revert to Legacy mode by logging into RACADM, which is the iDRAC command line interface.

This procedure is identical to the procedure for switching to `UEFI`, except that you specify `BIOS` instead of `UEFI`.

1. Start a Linux session and log into the iDRAC command line interface as a Linux Admin user. For example:

   ```
   ssh ADMIN@<iDRAC hostname or IP>
   ```

   The IDRAC command line interface appears, with the **racadm>>** prompt. 

1. To verify that the current boot environment is UEFI, enter this command:

   ```
   get BIOS.biosBootSettings.BootMode
   ```

   If the environment is UEFI, a message similar to the following appears:

   ```
   [Key=BIOS.Setup.1-1#biosBootSettings] 
   BootMode=Uefi
   ```

1. Set the **BIOS settings** to **BIOS**:

   ```
   set BIOS.BiosBootSettings.BootMode Bios
   ```

1. Apply and reboot:

   ```
   jobqueue create BIOS.Setup.1-1 -r forced -s TIME_NOW
   ```

The system reboots. Legacy mode is now enabled.

## Switch using the F2 boot menu
<a name="migrate-topic-bios-dell-f2"></a>

You can use the boot menu from a direct connection to the server, or through the IDRAC virtual console. 

This procedure is identical to the procedure for switching to `UEFI`, except that you specify `BIOS` instead of `UEFI`.

1. This step applies only if you want to use the virtual console: log into the iDRAC user interface and launch the Virtual Console.

1. Reboot the appliance. 

   ```
   sudo reboot
   ```

1. The appliance starts to reboot using UEFI, which is currently enabled. 

1. As soon as the reboot starts, repeatedly press **F2** on the keyboard, until the message **Entering System Setup** appears. Then wait for the **System Setup** screen to appear.

1. Choose **System BIOS**, then choose **Boot Settings**. 

1. On the **Boot Mode** line, choose **BIOS**. 

1. Choose the **Exit** option and follow the prompts to save. At the success message, choose **OK**. 

The system reboots. Legacy mode is now enabled.