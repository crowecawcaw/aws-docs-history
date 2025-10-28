# Configure the EC2Launch v1 agent on your Windows

instance

After your instance has been initialized the first time, you can configure EC2Launch
to run again and perform different start-up tasks.

###### Tasks

- [Configure initialization tasks](#ec2launch-inittasks "#ec2launch-inittasks")
- [Schedule EC2Launch to run on every boot](#run-on-every-boot "#run-on-every-boot")
- [Initialize drives and map drive letters](#ec2launch-mapping "#ec2launch-mapping")
- [Send Windows event logs to the EC2
  console](#ec2launch-sendlogs "#ec2launch-sendlogs")
- [Send Windows is ready message after a
  successful boot](#ec2launch-sendwinisready "#ec2launch-sendwinisready")

## Configure initialization tasks

Specify settings in the `LaunchConfig.json` file to enable or
disable the following initialization tasks:

- Set the computer name to the instance private IPv4 address.
- Set the monitor to always stay on.
- Set up new wallpaper.
- Add DNS suffix list.

###### Note

This adds a DNS suffix lookup for the following domain and configures
other standard suffixes. For more information about how launch agents
set DNS suffixes, see [Configure DNS Suffix for EC2 Windows launch agents](launch-agents-set-dns.md "launch-agents-set-dns.md").

```
`region`.ec2-utilities.amazonaws.com
```

- Extend the boot volume size.
- Set the administrator password.

###### To configure initialization settings

1. On the instance to configure, open the following file in a text editor:
   `C:\ProgramData\Amazon\EC2-Windows\Launch\Config\LaunchConfig.json`.
2. Update the following settings as needed and save your changes. Provide a
   password in `adminPassword` only if
   `adminPasswordtype` is `Specify`.

```
{
	"setComputerName": false,
	"setMonitorAlwaysOn": true,
	"setWallpaper": true,
	"addDnsSuffixList": true,
	"extendBootVolumeSize": true,
	"handleUserData": true,
	"adminPasswordType": "Random | Specify | DoNothing",
	"adminPassword": "password that adheres to your security policy (optional)"
}
```

The password types are defined as follows:

`Random`

EC2Launch generates a password and encrypts it using the
user's key. The system disables this setting after the instance
is launched so that this password persists if the instance is
rebooted or stopped and started.

`Specify`

EC2Launch uses the password you specify in
`adminPassword`. If the password does not meet
the system requirements, EC2Launch generates a random password
instead. The password is stored in
`LaunchConfig.json` as clear text and is
deleted after Sysprep sets the administrator password. EC2Launch
encrypts the password using the user's key.

`DoNothing`

EC2Launch uses the password you specify in the
`unattend.xml` file. If you don't specify
a password in `unattend.xml`, the
administrator account is disabled. 3. In Windows PowerShell, run the following command to schedule the script to
run as a Windows Scheduled Task. The script runs one time during the next
boot and then disables these tasks from running again.

```
C:\ProgramData\Amazon\EC2-Windows\Launch\Scripts\InitializeInstance.ps1 -Schedule
```

## Schedule EC2Launch to run on every boot

You can schedule EC2Launch to run on every boot instead of only the initial
boot.

To enable EC2Launch to run on every boot:

1. Open Windows PowerShell and run the following command:

```
C:\ProgramData\Amazon\EC2-Windows\Launch\Scripts\InitializeInstance.ps1 -SchedulePerBoot
```

2. Or, run the executable with the following command:

```
C:\ProgramData\Amazon\EC2-Windows\Launch\Settings\Ec2LaunchSettings.exe
```

Then select `Run EC2Launch on every boot`. You can specify that
your EC2 instance `Shutdown without Sysprep` or `Shutdown
 with Sysprep`.

###### Note

When you enable EC2Launch to run on every boot, the following happens the next
time EC2Launch runs:

- If `AdminPasswordType` is still set to `Random`,
  EC2Launch will generate a new password at the next boot. After that
  boot, `AdminPasswordType` is automatically set to
  `DoNothing` to prevent EC2Launch from generating new
  passwords on subsequent boots. To prevent EC2Launch from generating a
  new password on the first boot, manually set
  `AdminPasswordType` to `DoNothing` before you
  reboot.
- `HandleUserData` will be set back to `false`
  unless the user data has `persist` set to `true`.
  For more information, see [User data scripts](user-data.md#user-data-scripts "user-data.md#user-data-scripts").

## Initialize drives and map drive letters

Specify settings in the `DriveLetterMappingConfig.json` file to
map drive letters to volumes on your EC2 instance. The script initializes drives
that are not already initialized and partitioned. For more information about getting
volume details in Windows, see [Get-Volume](https://learn.microsoft.com/en-us/powershell/module/storage/get-volume "https://learn.microsoft.com/en-us/powershell/module/storage/get-volume") in the Microsoft documentation.

###### To map drive letters to volumes

1. Open the
   `C:\ProgramData\Amazon\EC2-Windows\Launch\Config\DriveLetterMappingConfig.json`
   file in a text editor.
2. Specify the following volume settings and save your changes:

```
{
	"driveLetterMapping": [
		{
			"volumeName": "`sample volume`",
			"driveLetter": "`H`"
		}
	]
}
```

3. Open Windows PowerShell and use the following command to run the EC2Launch
   script that initializes the disks:

```
C:\ProgramData\Amazon\EC2-Windows\Launch\Scripts\InitializeDisks.ps1
```

To initialize the disks each time the instance boots, add the
`-Schedule` flag as follows:

```
C:\ProgramData\Amazon\EC2-Windows\Launch\Scripts\InitializeDisks.ps1 -Schedule
```

## Send Windows event logs to the EC2

console

Specify settings in the `EventLogConfig.json` file to send
Windows Event logs to EC2 console logs.

###### To configure settings to send Windows Event logs

1. On the instance, open the
   `C:\ProgramData\Amazon\EC2-Windows\Launch\Config\EventLogConfig.json`
   file in a text editor.
2. Configure the following log settings and save your changes:

```
{
	"events": [
		{
			"logName": "`System`",
			"source": "`An event source (optional)`",
			"level": "`Error | Warning | Information`",
			"numEntries": `3`
		}
	]
}
```

3. In Windows PowerShell, run the following command so that the system
   schedules the script to run as a Windows Scheduled Task each time the
   instance boots.

```
C:\ProgramData\Amazon\EC2-Windows\Launch\Scripts\SendEventLogs.ps1 -Schedule
```

The logs can take three minutes or more to appear in the EC2 console
logs.

## Send Windows is ready message after a

successful boot

The EC2Config service sent the "Windows is ready" message to the EC2 console after
every boot. EC2Launch sends this message only after the initial boot. For backwards
compatibility with the EC2Config service, you can schedule EC2Launch to send this
message after every boot. On the instance, open Windows PowerShell and run the
following command. The system schedules the script to run as a Windows Scheduled
Task.

```
C:\ProgramData\Amazon\EC2-Windows\Launch\Scripts\SendWindowsIsReady.ps1 -Schedule
```
