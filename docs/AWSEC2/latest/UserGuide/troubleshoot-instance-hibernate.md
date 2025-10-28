# Troubleshoot Amazon EC2 instance

hibernation

Use this information to help diagnose and fix issues that you might encounter when
hibernating an instance.

###### Hibernation issues

- [Can't hibernate immediately after
  launch](#hibernate-troubleshooting-1 "#hibernate-troubleshooting-1")
- [Takes too long to transition from
  stopping to stopped, and memory state not restored
  after start](#hibernate-troubleshooting-2 "#hibernate-troubleshooting-2")
- [Instance "stuck" in the stopping state](#hibernate-troubleshooting-3 "#hibernate-troubleshooting-3")
- [Can’t start Spot Instance immediately after
  hibernate](#hibernate-troubleshooting-4 "#hibernate-troubleshooting-4")
- [Resume Spot Instances failed](#hibernate-troubleshooting-5 "#hibernate-troubleshooting-5")

## Can't hibernate immediately after

launch

If you try to hibernate an instance too quickly after you've launched it, you get
an error.

You must wait for about two minutes for Linux instances and about five minutes for
Windows instances after launch before hibernating.

## Takes too long to transition from

stopping to stopped, and memory state not restored
after start

If it takes a long time for your hibernating instance to transition from the
`stopping` state to `stopped`, and if the memory state is
not restored after you start, this could indicate that hibernation was not properly
configured.

**Linux instances**

Check the instance system log and look for messages that are related to
hibernation. To access the system log, [connect](connect-to-linux-instance.md "connect-to-linux-instance.md") to the instance or use the [get-console-output](../../../cli/latest/reference/ec2/get-console-output.md "../../../cli/latest/reference/ec2/get-console-output.md")
command. Find the log lines from the `hibinit-agent`. If the log lines
indicate a failure or the log lines are missing, there was most likely a failure
configuring hibernation at launch.

For example, the following message indicates that the instance root volume is not
large enough: `hibinit-agent: Insufficient disk space. Cannot create setup for
 hibernation. Please allocate a larger root device.`

If the last log line from the `hibinit-agent` is `hibinit-agent:
 Running: swapoff /swap`, hibernation was successfully configured.

If you do not see any logs from these processes, your AMI might not support
hibernation. For information about supported AMIs, see [Prerequisites for EC2 instance hibernation](hibernating-prerequisites.md "hibernating-prerequisites.md").
If you used your own Linux AMI, make sure that you followed the instructions for
[Configure a Linux AMI to support
hibernation](hibernation-enabled-AMI.md "hibernation-enabled-AMI.md").

###### Windows Server 2016 and later

Check the EC2 launch log and look for messages that are related to
hibernation. To access the EC2 launch log, [connect](connecting_to_windows_instance.md "connecting_to_windows_instance.md") to the instance and
open the
`C:\ProgramData\Amazon\EC2-Windows\Launch\Log\Ec2Launch.log`
file in a text editor. If you're using EC2Launch v2, open
`C:\ProgramData\Amazon\EC2Launch\log\agent.log`.

###### Note

By default, Windows hides files and folders under
`C:\ProgramData`. To view EC2 Launch directories and
files, enter the path in Windows Explorer or change the folder properties to
show hidden files and folders.

Find the log lines for hibernation. If the log lines indicate a failure or the log
lines are missing, there was most likely a failure configuring hibernation at
launch.

For example, the following message indicates that hibernation failed to configure:
`Message: Failed to enable hibernation.` If the error message
includes decimal ASCII values, you can convert the ASCII values to plain text in
order to read the full error message.

If the log line contains `HibernationEnabled: true`, hibernation was
successfully configured.

###### Windows Server 2012 R2 and earlier

Check the EC2 config log and look for messages that are related to
hibernation. To access the EC2 config log, [connect](connecting_to_windows_instance.md "connecting_to_windows_instance.md") to the instance and
open the `C:\Program
 Files\Amazon\Ec2ConfigService\Logs\Ec2ConfigLog.txt` file in a
text editor. Find the log lines for `SetHibernateOnSleep`. If the log
lines indicate a failure or the log lines are missing, there was most likely a
failure configuring hibernation at launch.

For example, the following message indicates that the instance root volume is not
large enough: `SetHibernateOnSleep: Failed to enable hibernation: Hibernation
 failed with the following error: There is not enough space on the
 disk.`

If the log line is `SetHibernateOnSleep: HibernationEnabled: true`,
hibernation was successfully configured.

###### Windows instance size

If you’re using a T3 or T3a Windows instance with less than 1 GiB of RAM, try increasing
the size of the instance to one that has at least 1 GiB of RAM.

## Instance "stuck" in the stopping state

If you hibernated your instance and it appears "stuck" in the
`stopping` state, you can forcibly stop it. For more information, see
[Troubleshoot Amazon EC2 instance stop issues](TroubleshootingInstancesStopping.md "TroubleshootingInstancesStopping.md").

## Can’t start Spot Instance immediately after

hibernate

If you try to start a Spot Instance within two minutes of hibernating it, you might get the
following error:

`You failed to start the Spot Instance because the associated Spot Instance request is not in
 an appropriate state to support start.`

Wait for about two minutes for Linux instances and about five minutes for Windows
instances and then retry starting the instance.

## Resume Spot Instances failed

If your Spot Instance was hibernated successfully but failed to resume, and instead
rebooted (a fresh restart where the hibernated state is not retained), it might be
because the user data contained the following script:

```
/usr/bin/enable-ec2-spot-hibernation
```

Remove this script from the **User data** field in the launch
template, and then request a new Spot Instance.

Note that even if the instance failed to resume, without the hibernated state
preserved, the instance can still be started in the same way as starting from the
`stopped` state.
