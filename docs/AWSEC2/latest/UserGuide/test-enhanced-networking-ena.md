# Test whether enhanced networking is enabled

You can test whether enhanced networking is enabled in your instances or your AMIs.

###### Instance attribute

Check the value of the `enaSupport` instance attribute.

AWS CLI
Use the [describe-instances](../../../cli/latest/reference/ec2/describe-instances.md "../../../cli/latest/reference/ec2/describe-instances.md") command.

```
aws ec2 describe-instances \
    --instance-ids `i-1234567890abcdef0` \
    --query "Reservations[].Instances[].EnaSupport"
```

If enhanced networking is enabled, the output is as follows.

```
[
    true
]
```

PowerShell
Use the [Get-EC2Instance](../../../powershell/latest/reference/items/Get-EC2Instance.md "../../../powershell/latest/reference/items/Get-EC2Instance.md") cmdlet.

```
(Get-EC2Instance -InstanceId `i-1234567890abcdef0`).Instances.EnaSupport
```

If enhanced networking is enabled, the output is as follows.

```
True
```

###### Image attribute

Check the value of the `enaSupport` image attribute.

AWS CLI
Use the [describe-images](../../../cli/latest/reference/ec2/describe-images.md "../../../cli/latest/reference/ec2/describe-images.md") command.

```
aws ec2 describe-images \
    --image-id `ami-0abcdef1234567890` \
    --query "Images[].EnaSupport"
```

If enhanced networking is enabled, the output is as follows.

```
[
    true
]
```

PowerShell
Use the [Get-EC2Image](../../../powershell/latest/reference/items/Get-EC2Image.md "../../../powershell/latest/reference/items/Get-EC2Image.md") cmdlet.

```
(Get-EC2Image -ImageId `ami-0abcdef1234567890`).EnaSupport
```

If enhanced networking is enabled, the output is as follows.

```
True
```

###### Linux network interface driver

Use the following command to verify that the `ena` kernel driver
is being used on a particular interface, substituting the interface name that
you want to check. If you are using a single interface (default), this is
`eth0`. If your Linux distribution supports predictable network names,
this could be a name like `ens5`. For more information, expand the section
for RHEL, SUSE, and CentOS in
[Enable enhanced networking on your instance](enabling_enhanced_networking.md "enabling_enhanced_networking.md").

In the following example, the `ena` kernel driver is not
loaded, because the listed driver is `vif`.

```
`[ec2-user ~]$` ethtool -i `eth0``driver: vif
version:
firmware-version:
bus-info: vif-0
supports-statistics: yes
supports-test: no
supports-eeprom-access: no
supports-register-dump: no
supports-priv-flags: no`
```

In this example, the `ena` kernel driver is loaded and at
the minimum recommended version. This instance has enhanced networking properly
configured.

```
`[ec2-user ~]$` ethtool -i `eth0``driver: ena
version: 1.5.0g
firmware-version:
expansion-rom-version:
bus-info: 0000:00:05.0
supports-statistics: yes
supports-test: no
supports-eeprom-access: no
supports-register-dump: no
supports-priv-flags: no`
```
