# Use `CopyImage` with a CLI

The following code examples show how to use `CopyImage`.

CLI

**AWS CLI**

**Example 1: To copy an AMI to another Region**

The following `copy-image` example command copies the specified AMI from the `us-west-2` Region to the `us-east-1` Region and adds a short description.

```
`aws ec2 copy-image \
 --region `us-east-1` \
 --name `ami-name` \
 --source-region `us-west-2` \
 --source-image-id `ami-066877671789bd71b` \
 --description `"This is my copied image."``

```

Output:

```
{
    "ImageId": "ami-0123456789abcdefg"
}
```

For more information, see [Copy an AMI](../../../AWSEC2/latest/UserGuide/CopyingAMIs.md "../../../AWSEC2/latest/UserGuide/CopyingAMIs.md") in the _Amazon EC2 User Guide_.

**Example 2: To copy an AMI to another Region and encrypt the backing snapshot**

The following `copy-image` command copies the specified AMI from the `us-west-2` Region to the current Region and encrypts the backing snapshot using the specified KMS key.

```
`aws ec2 copy-image \
 --source-region `us-west-2` \
 --name `ami-name` \
 --source-image-id `ami-066877671789bd71b` \
 --encrypted \
 --kms-key-id `alias/my-kms-key``

```

Output:

```
{
    "ImageId": "ami-0123456789abcdefg"
}
```

For more information, see [Copy an AMI](../../../AWSEC2/latest/UserGuide/CopyingAMIs.md "../../../AWSEC2/latest/UserGuide/CopyingAMIs.md") in the _Amazon EC2 User Guide_.

**Example 3: To include your user-defined AMI tags when copying an AMI**

The following `copy-image` command uses the `--copy-image-tags` parameter to copy your user-defined AMI tags when copying the AMI.

```
`aws ec2 copy-image \
 --region `us-east-1` \
 --name `ami-name` \
 --source-region `us-west-2` \
 --source-image-id `ami-066877671789bd71b` \
 --description `"This is my copied image."`
 --copy-image-tags`

```

Output:

```
{
    "ImageId": "ami-0123456789abcdefg"
}
```

For more information, see [Copy an AMI](../../../AWSEC2/latest/UserGuide/CopyingAMIs.md "../../../AWSEC2/latest/UserGuide/CopyingAMIs.md") in the _Amazon EC2 User Guide_.

- For API details, see
  [CopyImage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/copy-image.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/copy-image.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example copies the specified AMI in the 'EU (Ireland)' region to the 'US West (Oregon)' region. If -Region is not specified, the current default region is used as the destination region.**

```
Copy-EC2Image -SourceRegion eu-west-1 -SourceImageId ami-12345678 -Region us-west-2 -Name "Copy of ami-12345678"

```

**Output:**

```
ami-87654321
```

- For API details, see
  [CopyImage](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example copies the specified AMI in the 'EU (Ireland)' region to the 'US West (Oregon)' region. If -Region is not specified, the current default region is used as the destination region.**

```
Copy-EC2Image -SourceRegion eu-west-1 -SourceImageId ami-12345678 -Region us-west-2 -Name "Copy of ami-12345678"

```

**Output:**

```
ami-87654321
```

- For API details, see
  [CopyImage](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
