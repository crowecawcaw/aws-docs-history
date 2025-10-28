# Configure EC2 Fast Launch settings for your

Amazon EC2 Windows Server AMI

You can configure EC2 Fast Launch for Windows AMIs that you own, or AMIs
that are shared with you from the AWS Management Console, API, SDKs, CloudFormation, or AWS Command Line Interface (AWS CLI).
Before you configure EC2 Fast Launch, verify that your AMI meets all of the prerequisites
that are required to create the pre-provisioned snapshots. For more information, see
[EC2 Fast Launch prerequisites for Windows](win-start-fast-launch-prereqs.md "win-start-fast-launch-prereqs.md").

When you enable faster launching for Windows instances, Amazon EC2 checks to make sure that
you have the required permissions to launch instances from the specified AMI and Launch Template
(if provided), including permissions for encrypted AMIs. To prevent errors during the
instance launch process, the service validates your permissions before EC2 Fast Launch
is enabled. If you don't have the required permissions, the service returns an error, and
does not enable EC2 Fast Launch.

EC2 Fast Launch integrates with EC2 Image Builder to help you create custom
images with EC2 Fast Launch enabled. For more information, see [Create distribution settings for a Windows AMI with EC2 Fast Launch enabled (AWS CLI)](../../../imagebuilder/latest/userguide/cr-upd-ami-distribution-settings.md#create-ami-dist-win-fast-launch "../../../imagebuilder/latest/userguide/cr-upd-ami-distribution-settings.md#create-ami-dist-win-fast-launch")
in the _EC2 Image Builder User Guide_.

## Enable EC2 Fast Launch

Before changing these settings, make sure that your AMI, and the Region
that you run in meet all [EC2 Fast Launch prerequisites for Windows](win-start-fast-launch-prereqs.md "win-start-fast-launch-prereqs.md").

Console

###### To enable EC2 Fast Launch

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, under **Images**, choose
   **AMIs**.
3. Choose the AMI to update by selecting the check box next to the
   **Name**.
4. From the **Actions** menu above the list of AMIs,
   choose **Configure fast launch**. This opens
   the **Configure fast launch** page, where you
   configure the settings for EC2 Fast Launch.
5. To start using pre-provisioned snapshots to launch instances from
   your Windows AMI faster, select the **Enable fast launch for Windows**
   checkbox.
6. From the **Set anticipated launch frequency**
   drop-down list, choose a value to specify the number of snapshots
   that are created and maintained to cover your expected instance
   launch volume.
7. When you're done making changes, choose **Save
   changes**.

###### Note

If you need to use a launch template to specify a VPC, or to configure
metadata settings for IMDSv2, see [Use a launch template when you set up EC2 Fast Launch](#win-fast-launch-with-template "#win-fast-launch-with-template").

AWS CLI

###### To enable EC2 Fast Launch

Use the following [enable-fast-launch](../../../cli/latest/reference/ec2/enable-fast-launch.md "../../../cli/latest/reference/ec2/enable-fast-launch.md") command to enable EC2 Fast Launch for the
specified AMI, launching six parallel instances for pre-provisioning.

```
aws ec2 enable-fast-launch \
    --image-id `ami-0abcdef1234567890`  \
    --max-parallel-launches `6` \
    --resource-type `snapshot`
```

The following is example output.

```
{
	"ImageId": "ami-0abcdef1234567890",
	"ResourceType": "snapshot",
	"SnapshotConfiguration": {
	    "TargetResourceCount": 10
	},
	"LaunchTemplate": {},
	"MaxParallelLaunches": 6,
	"OwnerId": "0123456789123",
	"State": "enabling",
	"StateTransitionReason": "Client.UserInitiated",
	"StateTransitionTime": "2022-01-27T22:16:03.199000+00:00"
}
```

PowerShell

###### To enable EC2 Fast Launch

Use the [Enable-EC2FastLaunch](../../../powershell/latest/reference/items/Enable-EC2FastLaunch.md "../../../powershell/latest/reference/items/Enable-EC2FastLaunch.md") cmdlet to enable EC2 Fast Launch for
the specified AMI, launching six parallel instances for
pre-provisioning.

```
Enable-EC2FastLaunch `
	-ImageId `ami-0abcdef1234567890` `
	-MaxParallelLaunch `6` `
	-Region `us-west-2` `
	-ResourceType `snapshot`
```

The following is example output.

```
ImageId               : ami-0abcdef1234567890
	LaunchTemplate        :
	MaxParallelLaunches   : 6
	OwnerId               : 0123456789123
	ResourceType          : snapshot
	SnapshotConfiguration : Amazon.EC2.Model.FastLaunchSnapshotConfigurationResponse
	State                 : enabling
	StateTransitionReason : Client.UserInitiated
	StateTransitionTime   : 2/25/2022 12:24:11 PM
```

## Disable EC2 Fast Launch

Before changing these settings, make sure that your AMI, and the Region
that you run in meet all [EC2 Fast Launch prerequisites for Windows](win-start-fast-launch-prereqs.md "win-start-fast-launch-prereqs.md").

Console

###### To disable EC2 Fast Launch

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, under **Images**, choose
   **AMIs**.
3. Choose the AMI to update by selecting the check box next to the
   **Name**.
4. From the **Actions** menu above the list of AMIs,
   choose **Configure fast launch**. This opens
   the **Configure fast launch** page, where you
   configure the settings for EC2 Fast Launch.
5. Clear the **Enable fast launch for Windows**
   checkbox to disable EC2 Fast Launch and to remove
   pre-provisioned snapshots. This results in the AMI using the
   standard launch process for each instance, going forward.

###### Note

When you disable Windows image optimization, any existing
pre-provisioned snapshots are automatically deleted. This step
must be completed before you can start using the feature
again. 6. When you're done making changes, choose **Save
changes**.

AWS CLI

###### To disable EC2 Fast Launch

Use the following [disable-fast-launch](../../../cli/latest/reference/ec2/disable-fast-launch.md "../../../cli/latest/reference/ec2/disable-fast-launch.md") command to disable EC2 Fast Launch on the
specified AMI, and clean up existing pre-provisioned snapshots.

```
aws ec2 disable-fast-launch --image-id `ami-01234567890abcedf`
```

The following is example output.

```
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
    "State": "disabling",
    "StateTransitionReason": "Client.UserInitiated",
    "StateTransitionTime": "2022-01-27T22:47:29.265000+00:00"
}
```

PowerShell

###### To disable EC2 Fast Launch

Use the [Disable-EC2FastLaunch](../../../powershell/latest/reference/items/Disable-EC2FastLaunch.md "../../../powershell/latest/reference/items/Disable-EC2FastLaunch.md") cmdlet to disable EC2 Fast Launch on the
specified AMI, and clean up existing pre-provisioned snapshots.

```
Disable-EC2FastLaunch -ImageId `ami-0abcdef1234567890`
```

The following is example output.

```
ImageId               : ami-0abcdef1234567890
	LaunchTemplate        : Amazon.EC2.Model.FastLaunchLaunchTemplateSpecificationResponse
	MaxParallelLaunches   : 6
	OwnerId               : 0123456789123
	ResourceType          : snapshot
	SnapshotConfiguration :
	State                 : disabling
	StateTransitionReason : Client.UserInitiated
	StateTransitionTime   : 2/25/2022 1:10:08 PM
```

## Use a launch template when you set up EC2 Fast Launch

With a launch template, you can configure a set of launch parameters that Amazon EC2 uses
each time it launches an instance from that template. You can specify such things as
an AMI to use for your base image, instance types, storage, network settings, and more.

Launch templates are optional, except for the following specific cases, where you must
use a launch template for your Windows AMI when you configure faster launching:

- You must use a launch template to specify an existing VPC for your Windows AMI.
  This doesn't apply if you use the default VPC for your AWS account.
- If your account includes a policy that enforces IMDSv2 for Amazon EC2 instances, you
  must create a launch template that specifies the metadata configuration to enforce
  IMDSv2.

Use the launch template that includes your metadata configuration from the EC2 console,
or when you run the [enable-fast-launch](../../../cli/latest/reference/ec2/enable-fast-launch.md "../../../cli/latest/reference/ec2/enable-fast-launch.md")
command in the AWS CLI, or call the [EnableFastLaunch](../APIReference/API_EnableFastLaunch.md "../APIReference/API_EnableFastLaunch.md")
API action.

Amazon EC2 EC2 Fast Launch doesn't support the following configuration when you use a launch
template. If you use a launch template for EC2 Fast Launch, you must not specify any of
the following:

- User data scripts
- Termination protection
- Disabled metadata
- Spot option
- Shutdown behavior that terminates the instance
- Resource tags for network interface, elastic graphic, or spot instance requests

### Specify a VPC

###### Step 1: Create a launch template

Create a launch template that specifies the following details for your
Windows instances:

- The VPC subnet.
- An instance type of `t3.xlarge`.

For more information, see [Create an Amazon EC2 launch template](create-launch-template.md "create-launch-template.md").

**Step 2: Specify the launch template for your EC2 Fast Launch AMI**

Console

###### To specify the launch template for EC2 Fast Launch

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, under **Images**, choose
   **AMIs**.
3. Choose the AMI to update by selecting the check box next to the
   **Name**.
4. From the **Actions** menu above the list of AMIs,
   choose **Configure fast launch**. This opens
   the **Configure fast launch** page, where you
   configure the settings for EC2 Fast Launch.
5. The **Launch template** box performs a filtered search
   that finds launch templates in your account in the current Region that
   match the text you've entered. Specify all or part of the launch template
   name or ID in the box to show a list of matching launch templates. For
   example, if you enter `fast` in the box, Amazon EC2 finds all of the
   launch templates in your account in the current Region that have "fast" in
   the name.

To create a new launch template, you can choose **Create launch
template**. 6. When you select a launch template, Amazon EC2 shows the default version for
that template in the **Source template version** box. To
specify a different version, highlight the default version to replace it,
and enter the version number you want in the box. 7. When you're done making changes, choose **Save
changes**.

AWS CLI

###### To specify the launch template for EC2 Fast Launch

Use the [enable-fast-launch](../../../cli/latest/reference/ec2/enable-fast-launch.md "../../../cli/latest/reference/ec2/enable-fast-launch.md")
command with the `--launch-template` option, specifying
either the name or the ID of the launch template.

```
--launch-template LaunchTemplateName=`my-launch-template`
```

PowerShell

###### To specify the launch template for EC2 Fast Launch

Use the [Enable-EC2FastLaunch](../../../powershell/latest/reference/items/Enable-EC2FastLaunch.md "../../../powershell/latest/reference/items/Enable-EC2FastLaunch.md")
cmdlet with the `-LaunchTemplate_LaunchTemplateId` or
`-LaunchTemplate_LaunchTemplateName` parameter.

```
-LaunchTemplate_LaunchTemplateName `my-launch-template`
```

For more information about EC2 launch templates, see
[Store instance launch parameters in Amazon EC2 launch templates](ec2-launch-templates.md "ec2-launch-templates.md").
