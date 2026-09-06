

# View shared Amazon EC2 Dedicated Hosts in your AWS account
<a name="identifying-shared-dh"></a>

You can view Dedicated Host that you are sharing with other accounts, and Dedicated Hosts that are shared with you. If you own the Dedicated Host, you can see all of the instances running on the host, including instances launched by consumers. If the Dedicated Host is shared with you, you can see only the instances that you launched onto the shared host, and not those launched by other consumers.

Owners and consumers can identify shared Dedicated Hosts using one of the following methods.

------
#### [ Console ]

**To identify a shared Dedicated Host**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Dedicated Hosts**. The screen lists Dedicated Hosts that you own and Dedicated Hosts that are shared with you.

1. The **Owner** column shows the AWS account ID of the Dedicated Host owner.

1. To view the instances running on the hosts, select the **Instances** tab.

------
#### [ AWS CLI ]

**To identify a shared Dedicated Host**  
Use the [ describe-hosts](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-hosts.html) command. The command returns the Dedicated Hosts that you own and Dedicated Hosts that are shared with you. The value of `Owner` is the account ID of the owner of the Dedicated Host. The `Instances` list describes the instances running on the host.

```
aws ec2 describe-hosts --filter "Name=state,Values=available"
```

------
#### [ PowerShell ]

**To identify a shared Dedicated Host**  
Use the [Get-EC2host](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2Host.html) cmdlet. The cmdlet returns the Dedicated Hosts that you own and Dedicated Hosts that are shared with you. The value of `Owner` in the response is the account ID of the owner of the Dedicated Host. The `Instances` list describes the instances running on the host.

```
Get-EC2Host -Filter @{Name="state"; Values="available"}
```

------