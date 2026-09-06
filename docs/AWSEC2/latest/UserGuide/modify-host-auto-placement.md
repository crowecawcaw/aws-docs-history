

# Modify the auto-placement setting for an existing Amazon EC2 Dedicated Host
<a name="modify-host-auto-placement"></a>

You can modify the auto-placement settings of a Dedicated Host after you have allocated it to your AWS account.

------
#### [ Console ]

**To modify the auto-placement of a Dedicated Host**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Dedicated Hosts**.

1. Select a host and choose **Actions**, **Modify host**.

1. For **Instance auto-placement**, choose **Enable** to enable auto-placement, or clear **Enable** to disable auto-placement. For more information, see [Amazon EC2 Dedicated Host auto-placement and host affinity](dedicated-hosts-understanding.md).

1. Choose **Save**.

------
#### [ AWS CLI ]

**To modify the auto-placement of a Dedicated Host**  
Use the [modify-hosts](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-hosts.html) command.

```
aws ec2 modify-hosts \
    --auto-placement {{on}} \
    --host-ids {{h-012a3456b7890cdef}}
```

------
#### [ PowerShell ]

**To modify the auto-placement of a Dedicated Host**  
Use the [Edit-EC2Host](https://docs.aws.amazon.com/powershell/latest/reference/items/Edit-EC2Host.html) cmdlet.

```
Edit-EC2Host `
    -AutoPlacement {{1}} `
    -HostId {{h-012a3456b7890cdef}}
```

------