# How to Use the IAM Role With WorkSpaces Applications Streaming Instances

After you create an IAM role, you can apply it to an image builder or fleet streaming instance when you launch the image builder or create a fleet. You can also apply an IAM role to existing fleets. For information about how to apply IAM role when you launch an image builder, see [Launch an Image Builder to Install and Configure Streaming Applications](tutorial-image-builder-create.md "tutorial-image-builder-create.md"). For information about how to apply IAM role when you create a fleet, see [Create a Fleet in Amazon WorkSpaces Applications](set-up-stacks-fleets-create.md "set-up-stacks-fleets-create.md").

When you apply an IAM role to your image builder or fleet streaming instance,
WorkSpaces Applications retrieves temporary credentials and creates the
**appstream_machine_role** credential profile on the instance.
The temporary credentials are valid for 1 hour, and new credentials retrieved every
hour. The previous credentials do not expire, so you can use them for as long as
they are valid. You can use the credential profile to call AWS services
programmatically by using the AWS Command Line Interface (AWS CLI), AWS Tools
for PowerShell, or the AWS SDK with the language of your choice.

When you make the API calls, specify **appstream_machine_role** as the credential profile. Otherwise, the operation fails due to insufficient permissions.

WorkSpaces Applications assumes the specified role while the streaming instance is provisioned. Because WorkSpaces Applications uses the elastic network interface that is attached to your VPC for AWS API calls, your application or script must wait for the elastic network interface to become available before making AWS API calls. If API calls are made before the elastic network interface is available, the calls fail.

The following examples show how you can use the **appstream_machine_role** credential profile to describe streaming instances (EC2 instances) and to create the Boto client. Boto is the Amazon Web Services (AWS) SDK for Python.

**Describe Streaming Instances (EC2 instances) by Using the AWS CLI**

```
aws ec2 describe-instances --region us-east-1 --profile appstream_machine_role
```

**Describe Streaming Instances (EC2 instances) by Using AWS Tools for PowerShell**

You must use AWS Tools for PowerShell version 3.3.563.1 or later, with the Amazon Web Services SDK for .NET version 3.3.103.22 or later. You can download the AWS Tools for Windows installer, which includes AWS Tools for PowerShell and the Amazon Web Services SDK for .NET, from the [AWS Tools for PowerShell](https://aws.amazon.com/powershell/ "https://aws.amazon.com/powershell/") website.

```
Get-EC2Instance -Region us-east-1 -ProfileName appstream_machine_role
```

**Creating the Boto Client by Using the AWS SDK for Python**

```
session = boto3.Session(profile_name='appstream_machine_role')
```
