# Switching to Legacy on a Dell

There are three ways to switch the boot mode from UEFI back to BIOS (Legacy
mode).

###### Topics

- [Switch using the IDRAC user
  interface](#migrate-topic-bios-dell-idrac "#migrate-topic-bios-dell-idrac")
- [Switch using RACADM](#migrate-topic-bios-dell-racadm "#migrate-topic-bios-dell-racadm")
- [Switch using the F2 boot
  menu](#migrate-topic-bios-dell-f2 "#migrate-topic-bios-dell-f2")

## Switch using the IDRAC user

interface

iDRAC is a system for controlling Dell servers remotely. It is already
installed and enabled on the Dell server.

This procedure is identical to the procedure for switching to
`UEFI`, except that you specify `BIOS` instead of
`UEFI`.

1. Log into the iDRAC user interface as an administrative user.
2. On the iDRAC menu, choose **Configuration, then BIOS
   Settings**, then **Boot Settings.**
3. On the **Boot Mode** line, change the
   **Current Value** from **UEFI** to
   **BIOS**.
4. Scroll down to the **Apply** button and choose that
   button. The **Pending Value** changes to
   **BIOS**.
5. Scroll down to the bottom of the page and choose **Apply And
   Reboot**.

The system reboots. Legacy mode is now enabled.

## Switch using RACADM

You can revert to Legacy mode by logging into RACADM, which is the iDRAC
command line interface.

This procedure is identical to the procedure for switching to
`UEFI`, except that you specify `BIOS` instead of
`UEFI`.

1. Start a Linux session and log into the iDRAC command line interface as
   a Linux Admin user. For example:

```
ssh ADMIN@<iDRAC hostname or IP>
```

The IDRAC command line interface appears, with the
**racadm>>** prompt. 2. To verify that the current boot environment is UEFI, enter this
command:

```
get BIOS.biosBootSettings.BootMode
```

If the environment is UEFI, a message similar to the following
appears:

```
[Key=BIOS.Setup.1-1#biosBootSettings]
BootMode=Uefi
```

3. Set the **BIOS settings** to
   **BIOS**:

```
set BIOS.BiosBootSettings.BootMode Bios
```

4. Apply and reboot:

```
jobqueue create BIOS.Setup.1-1 -r forced -s TIME_NOW
```

The system reboots. Legacy mode is now enabled.

## Switch using the F2 boot

menu

You can use the boot menu from a direct connection to the server, or through
the IDRAC virtual console.

This procedure is identical to the procedure for switching to
`UEFI`, except that you specify `BIOS` instead of
`UEFI`.

1. This step applies only if you want to use the virtual console: log
   into the iDRAC user interface and launch the Virtual Console.
2. Reboot the appliance.

```
sudo reboot
```

3. The appliance starts to reboot using UEFI, which is currently enabled.
4. As soon as the reboot starts, repeatedly press **F2**
   on the keyboard, until the message **Entering System
   Setup** appears. Then wait for the **System
   Setup** screen to appear.
5. Choose **System BIOS**, then choose **Boot
   Settings**.
6. On the **Boot Mode** line, choose
   **BIOS**.
7. Choose the **Exit** option and follow the prompts to
   save. At the success message, choose **OK**.

The system reboots. Legacy mode is now enabled.
