# Updating firmware

## Step 1: Update the firmware

To update the BIOS firmware and the BMC firmware (IPMI for SuperMicro, iDRAC for
Dell), check with the firmware manufacturers for the following information:

- The latest firmware versions.
- Information about which BIOS firmware and BMC firmware versions are
  compatible with each other.

To update the firmware, follow the manufacturer's instructions.

## Step 2: Reboot the chassis

After you update the firmware, you must perform a cold reboot.

- You can physically power the appliance on and off.
- Or if you don't have physical access to the appliance, you can use
  `ipmiutil` to perform a cold reboot. This method resets the
  System Management processor. It doesn't reset the chassis.

This method is not considered to be a clean restart. This cold power cycle
cuts the power quickly and discharges all remnant power in its components.
Don't use this method as a standard way of rebooting.

**To reset using ipmiutil**

This procedure takes about 5 minutes. Don't be tempted to skip this reset because
if you do, the node might not run properly.

1. Stop the node from the web interface or command line of the AWS Elemental
   software.
2. From the Linux prompt, use the **elemental** user to
   start a remote terminal session to the AWS Elemental Server node.
3. Run the following command:

```
[elemental@hostname ~]$ sudo ipmiutil power -k
```

4. Wait 30 seconds. Then run the following command continually until the
   output shows a state that includes the codes `S0` or
   `2a`:

```
[elemental@hostname ~]$ watch -n 5 "sudo ipmiutil health | grep 'Power State'"
```

5. Press `Ctrl-C` to exit watch.
6. Run the following command:

```
[elemental@hostname ~]$ sudo sync
```

7. Run the following power cycle command:

```
[elemental@hostname ~]$ sudo ipmiutil power -c
```

This command turns off and turns on the appliance and terminates the SSH
connection. The RAID status might show as `Verify` during the
boot sequence. This is normal. 8. You now restart the node, if you want the node to resume activity.
