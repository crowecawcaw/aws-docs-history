# Review ENA Express settings for your EC2

instance

You can verify the ENA Express settings by instance or by network interface. To update
the ENA Express settings, see [Configure ENA Express settings for your EC2
instance](ena-express-configure.md "ena-express-configure.md").

Console

###### To view ENA Express settings for a network interface

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the left navigation pane, choose **Network
   interfaces**.
3. Select a network interface to see the details for that instance.
   You can choose the **Network interface ID** link to
   open the detail page, or you can select the checkbox on the left side of the list to view details in the
   detail pane at the bottom of the page.
4. In the **Network interface attachment** section
   on the **Details** tab or detail page, review
   settings for **ENA Express** and **ENA
   Express UDP**.

###### To view ENA Express settings for an instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the left navigation pane, choose
   **Instances**.
3. Select an instance to see the details for that instance. You can
   choose the **Instance ID** link to open the detail
   page, or you can select the checkbox on the left side of the list to view details in the
   detail pane at the bottom of the page.
4. In the **Network interfaces** section on the
   **Networking** tab, scroll right to review
   settings for **ENA Express** and **ENA
   Express UDP**.

AWS CLI

###### To get the ENA Express settings for an instance

Use the [describe-instances](../../../cli/latest/reference/describe-instances.md "../../../cli/latest/reference/describe-instances.md") command. This command
example returns a list of ENA Express configurations for the network
interfaces attached to each of the running instances that are specified
by the `--instance-ids` parameter.

```
aws ec2 describe-instances \
    --instance-ids `i-1234567890abcdef0` `i-0598c7d356eba48d7` \
    --query 'Reservations[*].Instances[*].[InstanceId, NetworkInterfaces[*].Attachment.EnaSrdSpecification]'
```

The following is example output.

```
[
    [
        [
            "i-1234567890abcdef0",
            [
                {
                    "EnaSrdEnabled": true,
                    "EnaSrdUdpSpecification": {
                        "EnaSrdUdpEnabled": false
                    }
                }
            ]
        ]
    ],
    [
        [
            "i-0598c7d356eba48d7",
            [
            {
                    "EnaSrdEnabled": true,
                    "EnaSrdUdpSpecification": {
                        "EnaSrdUdpEnabled": false
                    }
                }
            ]
        ]
    ]
]
```

###### To get the ENA Express settings for a network interface

Use the [describe-network-interfaces](../../../cli/latest/reference/describe-network-interfaces.md "../../../cli/latest/reference/describe-network-interfaces.md")
command.

```
aws ec2 describe-network-interfaces \
    --network-interface-ids `eni-1234567890abcdef0` \
    --query NetworkInterfaces[].[NetworkInterfaceId,Attachment.EnaSrdSpecification]
```

The following is example output.

```
[
    [
        "eni-1234567890abcdef0",
        {
            "EnaSrdEnabled": true,
            "EnaSrdUdpSpecification": {
                "EnaSrdUdpEnabled": false
            }
        }
    ]
]
```

PowerShell

###### To get the ENA Express settings for a network interface

Use the [Get-EC2NetworkInterface](../../../powershell/latest/reference/items/Get-EC2NetworkInterface.md "../../../powershell/latest/reference/items/Get-EC2NetworkInterface.md") cmdlet.

```
Get-EC2NetworkInterface `
    -NetworkInterfaceId `eni-1234567890abcdef0` | `
Select-Object `
    Association,
    NetworkInterfaceId,
    OwnerId,
    @{Name = 'AttachTime'; Expression = { $_.Attachment.AttachTime } },
    @{Name = 'AttachmentId'; Expression = { $_.Attachment.AttachmentId } },
    @{Name = 'DeleteOnTermination'; Expression = { $_.Attachment.DeleteOnTermination } },
    @{Name = 'NetworkCardIndex'; Expression = { $_.Attachment.NetworkCardIndex } },
    @{Name = 'InstanceId'; Expression = { $_.Attachment.InstanceId } },
    @{Name = 'InstanceOwnerId'; Expression = { $_.Attachment.InstanceOwnerId } },
    @{Name = 'Status'; Expression = { $_.Attachment.Status } },
    @{Name = 'EnaSrdEnabled'; Expression = { $_.Attachment.EnaSrdSpecification.EnaSrdEnabled } },
    @{Name = 'EnaSrdUdpEnabled'; Expression = { $_.Attachment.EnaSrdSpecification.EnaSrdUdpSpecification.EnaSrdUdpEnabled } }
```

The following is example output.

```
Association         :
NetworkInterfaceId  : eni-0d1234e5f6a78901b
OwnerId             : 111122223333
AttachTime          : 6/11/2022 1:13:11 AM
AttachmentId        : eni-attach-0d1234e5f6a78901b
DeleteOnTermination : True
NetworkCardIndex    : 0
InstanceId          : i-1234567890abcdef0
InstanceOwnerId     : 111122223333
Status              : attached
EnaSrdEnabled       : True
EnaSrdUdpEnabled    : False
```
