# Step B: Install

(kickstart) the operating system software

Install the operating system on the node. This action is known as
_kickstarting_ the
system.

###### To kickstart the system

1. Insert the USB thumb drive into the hardware unit.
2. Restart the system using the following command.

```
[elemental@hostname ~]$ sudo reboot
```

3. Use the arrow keys to select each option and complete the
   field, using the instructions in the following table as a
   guide.

| Menu Option                                   | Instructions                                                                                                                                                            |
| --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `Set Hostname`                                | Change the hostname to a useful name such as `live-01` or `live-chicago-01`. Do not use `localhost` as the hostname. Do not use periods or underscores in the hostname. |
| `Disk layout: Auto-detect`                    | Keep this set at Auto-detect.                                                                                                                                           |
| `Set Key`                                     | Arrow down to skip this option.                                                                                                                                         |
| `Install and configure base operating system` | Press Enter to begin the OS installation.                                                                                                                               | The operating system is installed. 4. At the `Press return to quit` prompt, press **Enter** to reboot the system. |
