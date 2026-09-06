

# Unshare a Dedicated Host that is shared with other AWS accounts
<a name="unsharing-dh"></a>

The Dedicated Host owner can unshare a shared Dedicated Host at any time. When you unshare a shared Dedicated Host, the following rules apply:
+ Consumers with whom the Dedicated Host was shared can no longer launch new instances onto it.
+ Instances owned by consumers that were running on the Dedicated Host at the time of unsharing continue to run but are scheduled for [retirement](schedevents_actions_retire.md). Consumers receive retirement notifications for the instances and they have two weeks to take action on the notifications. However, if the Dedicated Host is reshared with the consumer within the retirement notice period, the instance retirements are cancelled.

To unshare a shared Dedicated Host that you own, you must remove it from the resource share.

------
#### [ Console ]

**To unshare a shared Dedicated Host that you own**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Dedicated Hosts**.

1. Choose the Dedicated Host to unshare and choose the **Sharing** tab.

1. The **Sharing** tab lists the resource shares to which the Dedicated Host has been added. Select the resource share from which to remove the Dedicated Host and choose **Remove host from resource share**.

**To unshare a shared Dedicated Host that you own using the AWS RAM console**  
See [Update a resource share](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing-update.html) in the *AWS RAM User Guide*.

------
#### [ AWS CLI ]

**To unshare a shared Dedicated Host that you own**  
Use the [disassociate-resource-share](https://docs.aws.amazon.com/cli/latest/reference/ram/disassociate-resource-share.html) command.

```
aws ram disassociate-resource-share \
    --resource-share-arn arn:aws:ram:{{us-east-2}}:{{123456789012}}:resource-share/{{7ab63972-b505-7e2a-420d-6f5d3EXAMPLE}} \
	--resource-arns arn:aws:ec2:{{us-east-2}}:{{123456789012}}:dedicated-host/{{h-07879acf49EXAMPLE}}
```

------
#### [ PowerShell ]

**To unshare a shared Dedicated Host that you own**  
Use the [Disconnect-RAMResourceShare](https://docs.aws.amazon.com/powershell/latest/reference/items/Disconnect-RAMResourceShare.html) cmdlet.

```
Disconnect-RAMResourceShare `
    -ResourceShareArn "arn:aws:ram:{{us-east-2}}:{{123456789012}}:resource-share/{{7ab63972-b505-7e2a-420d-6f5d3EXAMPLE}}" `
    -ResourceArn "arn:aws:ec2:{{us-east-2}}:{{123456789012}}:dedicated-host/{{h-07879acf49EXAMPLE}}"
```

------