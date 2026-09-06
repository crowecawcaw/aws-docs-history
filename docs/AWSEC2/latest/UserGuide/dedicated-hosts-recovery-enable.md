

# Manage Amazon EC2 Dedicated Host recovery
<a name="dedicated-hosts-recovery-enable"></a>

Dedicated Host auto recovery restarts your instances on to a new replacement host when certain problematic conditions are detected on your Dedicated Host. You can enable host recovery when you allocate the Dedicated Host or after allocation.

Use the following procedures to enable host recovery when allocating the host.

------
#### [ Console ]

**To enable host recovery at allocation**  
When allocating a Dedicated Host using the Amazon EC2 console, for **Host recovery**, choose **Enable**. For more information, see [Allocate an Amazon EC2 Dedicated Host for use in your account](dedicated-hosts-allocating.md).

------
#### [ AWS CLI ]

**To enable host recovery at allocation**  
Use the [allocate-hosts](https://docs.aws.amazon.com/cli/latest/reference/ec2/allocate-hosts.html) command.

```
aws ec2 allocate-hosts \
    --instance-type {{m5.large}} \
    --availability-zone {{eu-west-1a}} \
    --auto-placement on \
    --host-recovery on \
    --quantity 1
```

------
#### [ PowerShell ]

**To enable host recovery at allocation**  
Use the [New-EC2Host](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2Host.html) cmdlet.

```
New-EC2Host `
    -InstanceType {{m5.large}} `
    -AvailabilityZone {{eu-west-1a}} `
    -AutoPlacement on `
    -HostRecovery on `
    -Quantity 1
```

------

Use the following procedures to manage host recovery for a Dedicated Host.

------
#### [ Console ]

**To manage host recovery after allocation**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Dedicated Hosts**.

1. Select the Dedicated Host.

1. Choose **Actions**, **Modify host**.

1. For **Host recovery**, select or clear **Enable**.

1. Choose **Save**.

------
#### [ AWS CLI ]

**To enable host recovery after allocation**  
Use the [modify-hosts](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-hosts.html) command.

```
aws ec2 modify-hosts \
    --host-recovery on \
    --host-ids {{h-012a3456b7890cdef}}
```

**To disable host recovery after allocation**  
Use the [modify-hosts](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-hosts.html) command and specify the `host-recovery` parameter with a value of `off`.

```
aws ec2 modify-hosts \
    --host-recovery off \
    --host-ids {{h-012a3456b7890cdef}}
```

------
#### [ PowerShell ]

**To enable host recovery after allocation**  
Use the [Edit-host](https://docs.aws.amazon.com/powershell/latest/reference/items/Edit-EC2Host.html) cmdlet.

```
Edit-EC2Host `
    -HostRecovery on `
    -HostId {{h-012a3456b7890cdef}}
```

**To disable host recovery after allocation**  
Use the [Edit-EC2Host](https://docs.aws.amazon.com/powershell/latest/reference/items/Edit-EC2Host.html) cmdlet.

```
Edit-EC2Host `
    -HostRecovery off `
    -HostId {{h-012a3456b7890cdef}}
```

------