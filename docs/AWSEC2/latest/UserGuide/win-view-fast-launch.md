# View AMIs with EC2 Fast Launch enabled

You can use the [describe-fast-launch-images](../../../cli/latest/reference/ec2/describe-fast-launch-images.md "../../../cli/latest/reference/ec2/describe-fast-launch-images.md") command in the AWS CLI, or the [Get-EC2FastLaunchImage](../../../powershell/latest/reference/items/Get-EC2FastLaunchImage.md "../../../powershell/latest/reference/items/Get-EC2FastLaunchImage.md")
Tools for PowerShell Cmdlet to get details for AMIs that have EC2 Fast Launch enabled.

Amazon EC2 provides the following details for each Windows AMI that is returned in the
results:

- The image ID for an AMI with EC2 Fast Launch enabled.
- The resource type that is used for pre-provisioning the associated Windows AMI. Supported
  value: `snapshot`.
- The snapshot configuration, which is a group of parameters that configure
  pre-provisioning for the associated Windows AMI using snapshots.
- Launch template information, including the ID, name, and version of the launch
  template that the associated AMI uses when it launches Window instances from
  pre-provisioned snapshots.
- The maximum number of instances that can be launched at the same time for creating
  resources.
- The owner ID for the associated AMI. This is not populated for AMIs that are shared
  with you.
- The current state of EC2 Fast Launch for the associated AMI. Supported
  values include: `enabling | enabling-failed | enabled | enabled-failed |
disabling | disabling-failed`.

###### Note

You can also see the current state displayed in the **Manage
image optimization** page in the EC2 console, as **Image optimization
state**.

- The reason that EC2 Fast Launch for the associated AMI changed to the current
  state.
- The time that EC2 Fast Launch for the associated AMI changed to the current
  state.

AWS CLI

###### To find AMIs configured for EC2 Fast Launch

Use the following [describe-fast-launch-images](../../../cli/latest/reference/ec2/describe-fast-launch-images.md "../../../cli/latest/reference/ec2/describe-fast-launch-images.md") command to describe the details
for each of the AMIs in the account that are configured for EC2 Fast Launch.
In this example, only one AMI in the account is configured
for EC2 Fast Launch.

```
aws ec2 describe-fast-launch-images
```

The following is example output.

```
{
    "FastLaunchImages": [
        {
            "ImageId": "ami-01234567890abcedf",
            "ResourceType": "snapshot",
            "SnapshotConfiguration": {},
            "LaunchTemplate": {
                "LaunchTemplateId": "lt-01234567890abcedf",
                "LaunchTemplateName": "EC2FastLaunchDefaultResourceCreation-a8c6215d-94e6-441b-9272-dbd1f87b07e2",
                "Version": "1"
            },
            "MaxParallelLaunches": 6,
            "OwnerId": "0123456789123",
            "State": "enabled",
            "StateTransitionReason": "Client.UserInitiated",
            "StateTransitionTime": "2022-01-27T22:20:06.552000+00:00"
        }
    ]
}
```

PowerShell

###### To find AMIs configured for EC2 Fast Launch

Use the following [Get-EC2FastLaunchImage](../../../powershell/latest/reference/items/Get-EC2FastLaunchImage.md "../../../powershell/latest/reference/items/Get-EC2FastLaunchImage.md") cmdlet to describe the details for
each of the AMIs in the account that are configured for EC2 Fast Launch.
In this example, only one AMI in the account is configured
for EC2 Fast Launch.

```
Get-EC2FastLaunchImage -ImageId `ami-0abcdef1234567890`
```

The following is example output.

```
ImageId               : ami-0abcdef1234567890
LaunchTemplate        : Amazon.EC2.Model.FastLaunchLaunchTemplateSpecificationResponse
MaxParallelLaunches   : 6
OwnerId               : 012345678912
ResourceType          : snapshot
SnapshotConfiguration :
State                 : enabled
StateTransitionReason : Client.UserInitiated
StateTransitionTime   : 2/25/2022 12:54:43 PM
```
