# Use `ModifyImageAttribute` with a CLI

The following code examples show how to use `ModifyImageAttribute`.

CLI

**AWS CLI**

**Example 1: To make an AMI public**

The following `modify-instance-attribute` example makes the specified AMI public.

```
`aws ec2 modify-image-attribute \
 --image-id `ami-5731123e` \
 --launch-permission `"Add=[{Group=all}]"``

```

This command produces no output.

**Example 2: To make an AMI private**

The following `modify-instance-attribute` example makes the specified AMI private.

```
`aws ec2 modify-image-attribute \
 --image-id `ami-5731123e` \
 --launch-permission `"Remove=[{Group=all}]"``

```

This command produces no output.

**Example 3: To grant launch permission to an AWS account**

The following `modify-instance-attribute` example grants launch permissions to the specified AWS account.

```
`aws ec2 modify-image-attribute \
 --image-id `ami-5731123e` \
 --launch-permission `"Add=[{UserId=123456789012}]"``

```

This command produces no output.

**Example 4: To remove launch permission from an AWS account**

The following `modify-instance-attribute` example removes launch permissions from the specified AWS account.

```
`aws ec2 modify-image-attribute \
 --image-id `ami-5731123e` \
 --launch-permission `"Remove=[{UserId=123456789012}]"``

```

- For API details, see
  [ModifyImageAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-image-attribute.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-image-attribute.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example updates the description for the specified AMI.**

```
Edit-EC2ImageAttribute -ImageId ami-12345678 -Description "New description"

```

**Example 2: This example makes the AMI public (for example, so any AWS account can use it).**

```
Edit-EC2ImageAttribute -ImageId ami-12345678 -Attribute launchPermission -OperationType add -UserGroup all

```

**Example 3: This example makes the AMI private (for example, so that only you as the owner can use it).**

```
Edit-EC2ImageAttribute -ImageId ami-12345678 -Attribute launchPermission -OperationType remove -UserGroup all

```

**Example 4: This example grants launch permission to the specified AWS account.**

```
Edit-EC2ImageAttribute -ImageId ami-12345678 -Attribute launchPermission -OperationType add -UserId 111122223333

```

**Example 5: This example removes launch permission from the specified AWS account.**

```
Edit-EC2ImageAttribute -ImageId ami-12345678 -Attribute launchPermission -OperationType remove -UserId 111122223333

```

- For API details, see
  [ModifyImageAttribute](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example updates the description for the specified AMI.**

```
Edit-EC2ImageAttribute -ImageId ami-12345678 -Description "New description"

```

**Example 2: This example makes the AMI public (for example, so any AWS account can use it).**

```
Edit-EC2ImageAttribute -ImageId ami-12345678 -Attribute launchPermission -OperationType add -UserGroup all

```

**Example 3: This example makes the AMI private (for example, so that only you as the owner can use it).**

```
Edit-EC2ImageAttribute -ImageId ami-12345678 -Attribute launchPermission -OperationType remove -UserGroup all

```

**Example 4: This example grants launch permission to the specified AWS account.**

```
Edit-EC2ImageAttribute -ImageId ami-12345678 -Attribute launchPermission -OperationType add -UserId 111122223333

```

**Example 5: This example removes launch permission from the specified AWS account.**

```
Edit-EC2ImageAttribute -ImageId ami-12345678 -Attribute launchPermission -OperationType remove -UserId 111122223333

```

- For API details, see
  [ModifyImageAttribute](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
