# Change the time zone of your

instance

Amazon EC2 instances are set to the UTC (Coordinated Universal Time) time zone by default.
You can change the time on an instance to the local time zone or to another time zone in
your network.

Use the instructions for your instance's operating system.

###### Important

This information applies to Amazon Linux. For information about other
distributions, see their specific documentation.

###### To change the time zone on Amazon Linux

1. View the system's current time zone setting.

```
`[ec2-user ~]$` `timedatectl`
```

2. List the available time zones.

```
`[ec2-user ~]$` `timedatectl list-timezones`
```

3. Set the chosen time zone.

```
`[ec2-user ~]$` `sudo timedatectl set-timezone `America/Vancouver``
```

4. (Optional) Confirm that the current time zone is updated to the new
   time zone by running the **timedatectl** command
   again.

```
`[ec2-user ~]$` `timedatectl`
```

###### To change the time zone on a Windows instance

1. From your instance, open a Command Prompt window.
2. Identify the time zone to use on the instance. To get a list of time
   zones, use the following command:

```
tzutil /l
```

This command returns a list of all available time zones in the
following format:

```
`display name`
`time zone ID`
```

3. Locate the time zone ID to assign to the instance.
4. Example: Assign the UTC time zone:

```
tzutil /s "UTC"
```

Example: Assign Pacific Standard Time:

```
tzutil /s "Pacific Standard Time"
```

When you change the time zone on a Windows instance, you must ensure that
the time zone persists through system restarts. Otherwise, when the instance
restarts, it reverts back to using UTC time. You can persist your time zone
setting by adding a **RealTimeIsUniversal** registry key.
This key is set by default on all current generation instances. To verify
whether the **RealTimeIsUniversal** registry key is set, see
step 3 in the following procedure. If the key is not set, follow these steps
from the beginning.

###### To set the RealTimeIsUniversal registry key

1. From the instance, open a Command Prompt window.
2. Use the following command to add the registry key:

```
reg add "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\TimeZoneInformation" /v RealTimeIsUniversal /d 1 /t REG_DWORD /f
```

3. (Optional) Verify that the instance saved the key successfully
   using the following command:

```
reg query "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\TimeZoneInformation" /s
```

This command returns the subkeys for the
**TimeZoneInformation** registry key. You should
see the **RealTimeIsUniversal** key at the bottom of
the list, similar to the following:

```
HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\TimeZoneInformation
    Bias                            REG_DWORD     0x1e0
    DaylightBias                    REG_DWORD     0xffffffc4
    DaylightName                    REG_SZ        @tzres.dll,-211
    DaylightStart                   REG_BINARY    00000300020002000000000000000000
    StandardBias                    REG_DWORD     0x0
    StandardName                    REG_SZ        @tzres.dll,-212
    StandardStart                   REG_BINARY    00000B00010002000000000000000000
    TimeZoneKeyName                 REG_SZ        Pacific Standard Time
    DynamicDaylightTimeDisabled     REG_DWORD     0x0
    ActiveTimeBias                  REG_DWORD     0x1a4
    RealTimeIsUniversal             REG_DWORD     0x1
```
