# Switch to UEFI on a Dell

There are three ways to switch the boot mode from Legacy mode to UEFI.

###### Topics

- [Switch using the IDRAC
  user interface](#migrate-server-218-boot-mode-uefi-idrac "#migrate-server-218-boot-mode-uefi-idrac")
- [Switch using
  RACADM](#migrate-server-218-boot-mode-uefi-racadm "#migrate-server-218-boot-mode-uefi-racadm")
- [Switch using the F2 boot
  menu](#migrate-server-218-boot-mode-uefi-f2 "#migrate-server-218-boot-mode-uefi-f2")

## Switch using the IDRAC

user interface

iDRAC is a system for controlling Dell servers remotely. It is already
installed and enabled on the Dell server. However, you might need to configure
it. For more information about configuring iDRAC, see the official [Dell iDRAC User Guide](https://www.dell.com/support/manuals/us/en/04/idrac9-lifecycle-controller-v4.x-series/idrac9_4.00.00.00_ug_new "https://www.dell.com/support/manuals/us/en/04/idrac9-lifecycle-controller-v4.x-series/idrac9_4.00.00.00_ug_new").

This procedure is identical to the procedure for switching to BIOS, except
that you choose **UEFI** instead of
**BIOS**.

1. Log into the iDRAC user interface as an administrative user.
2. On the iDRAC menu, choose **Configuration, then BIOS
   Settings**, then **Boot Settings.**
3. On the **Boot Mode** line, change the
   **Current Value** from **BIOS** to
   **UEFI**.
4. Scroll down to the **Apply** button and choose that
   button. The **Pending Value** changes to
   **UEFI**.
5. Scroll down to the bottom of the page and choose **Apply And
   Reboot**.

The system reboots. UEFI is now enabled.

## Switch using

RACADM

You can switch to UEFI mode by logging into RACADM, which is the iDRAC command
line interface.

This procedure is identical to the procedure for switching to BIOS, except
that you specify **UEFI** instead of
**BIOS**.

1. Start a Linux session and log into the iDRAC command line interface as
   a Linux Admin user. For example:

```
ssh ADMIN@<iDRAC hostname or IP>
```

The IDRAC command line interface appears, with the
**racadm>>** prompt. 2. To verify that the current boot environment is BIOS, enter this
command:

```
get BIOS.biosBootSettings.BootMode
```

If the environment is BIOS, a message similar to the following
appears:

```
[Key=BIOS.Setup.1-1#biosBootSettings]
BootMode=Bios
```

3. Set the **BIOS settings** to
   **UEFI**:

```
set BIOS.BiosBootSettings.BootMode Uefi
```

4. Apply and reboot:

```
jobqueue create BIOS.Setup.1-1 -r Forced
```

The system reboots. UEFI is now enabled.

## Switch using the F2 boot

menu

You can use the boot menu from a direct connection to the server, or through
the IDRAC virtual console.

This procedure is identical to the procedure for switching to BIOS, except
that you specify **UEFI** instead of
**BIOS**.

1. This step applies only if you want to use the virtual console: log
   into the iDRAC user interface and launch the Virtual Console.
2. Reboot the appliance.

```
sudo reboot
```

3. The appliance starts to reboot using BIOS, which is currently enabled.
4. As soon as the reboot starts, repeatedly press **F2**
   on the keyboard, until the message **Entering System
   Setup** appears. Then wait for the **System
   Setup** screen to appear.
5. Choose **System BIOS**, then choose **Boot
   Settings**.
6. On the **Boot Mode** line, choose
   **UEFI**.
7. Choose the **Exit** option and follow the prompts to
   save. At the success message, choose **OK**.

The system reboots. UEFI is now enabled.
