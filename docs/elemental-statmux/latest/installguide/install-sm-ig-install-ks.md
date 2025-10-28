This is version 2.20 of the AWS Elemental Statmux documentation.
This is the latest version. For prior versions, see the
_Previous Versions_ section of [AWS Elemental Statmux
and AWS Elemental Live Documentation](../../../elemental-live.md "../../../elemental-live.md").

# Step B: Install (Kickstart) the Operating System Software

###### To kickstart the system

1. Insert the USB thumb drive into the hardware unit.
2. Restart the system using the following command.

```
[elemental@hostname ~]$ `sudo reboot`
```

3. Use the arrow keys to select each option and complete the field, using the instructions in the following table as a guide.

| Menu Option                                   | Instructions                                                                                                                                                                |
| --------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Set Hostname`                                | Change the hostname to a useful name such as `statmux-01` or `statmux-chicago-01`. Do not use localhost as the hostname! Do not use periods or underscores in the hostname. |
| `Disk layout: Auto-detect`                    | Leave this set at Auto-detect.                                                                                                                                              |
| `Set Key`                                     | Arrow down to skip this option.                                                                                                                                             |
| `Install and configure base operating system` | Press Enter to begin the OS installation.                                                                                                                                   | The operating system is installed. 4. For the changes to take effect, reboot the system by pressing **Enter** at the prompt `Press return to quit`. |
