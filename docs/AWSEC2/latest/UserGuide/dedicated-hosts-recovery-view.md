

# View the host recovery setting for your Amazon EC2 Dedicated Host
<a name="dedicated-hosts-recovery-view"></a>

You can view the host recovery configuration for a Dedicated Host at any time.

------
#### [ Console ]

**To view the host recovery configuration for a Dedicated Host**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Dedicated Hosts**.

1. Select the Dedicated Host, and in the **Description** tab, review the **Host Recovery** field.

------
#### [ AWS CLI ]

**To view the host recovery configuration for a Dedicated Host**  
Use the [describe-hosts](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-hosts.html) command.

```
aws ec2 describe-hosts \
    --host-ids {{h-012a3456b7890cdef}} \
    --query Hosts[].HostRecovery
```

The following is example output.

```
on
```

------
#### [ PowerShell ]

**To view the host recovery configuration for a Dedicated Host**  
Use the [Get-EC2Host](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2Host.html) cmdlet.

```
(Get-EC2Host -HostId {{h-012a3456b7890cdef}}).Hosts | Select HostRecovery
```

The following is example output.

```
HostRecovery
------------
on
```

------