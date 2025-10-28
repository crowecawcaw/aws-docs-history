# Use `ModifyNetworkInterfaceAttribute` with a CLI

The following code examples show how to use `ModifyNetworkInterfaceAttribute`.

CLI

**AWS CLI**

**To modify the attachment attribute of a network interface**

This example command modifies the `attachment` attribute of the specified network interface.

Command:

```
`aws ec2 modify-network-interface-attribute --network-interface-id `eni-686ea200` --attachment `AttachmentId=eni-attach-43348162,DeleteOnTermination=false``

```

**To modify the description attribute of a network interface**

This example command modifies the `description` attribute of the specified network interface.

Command:

```
`aws ec2 modify-network-interface-attribute --network-interface-id `eni-686ea200` --description `"My description"``

```

**To modify the groupSet attribute of a network interface**

This example command modifies the `groupSet` attribute of the specified network interface.

Command:

```
`aws ec2 modify-network-interface-attribute --network-interface-id `eni-686ea200` --groups `sg-903004f8` `sg-1a2b3c4d``

```

**To modify the sourceDestCheck attribute of a network interface**

This example command modifies the `sourceDestCheck` attribute of the specified network interface.

Command:

```
`aws ec2 modify-network-interface-attribute --network-interface-id `eni-686ea200` --no-source-dest-check`

```

- For API details, see
  [ModifyNetworkInterfaceAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-network-interface-attribute.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-network-interface-attribute.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example modifies the specified network interface so that the specified attachment is deleted on termination.**

```
Edit-EC2NetworkInterfaceAttribute -NetworkInterfaceId eni-1a2b3c4d -Attachment_AttachmentId eni-attach-1a2b3c4d -Attachment_DeleteOnTermination $true

```

**Example 2: This example modifies the description of the specified network interface.**

```
Edit-EC2NetworkInterfaceAttribute -NetworkInterfaceId eni-1a2b3c4d -Description "my description"

```

**Example 3: This example modifies the security group for the specified network interface.**

```
Edit-EC2NetworkInterfaceAttribute -NetworkInterfaceId eni-1a2b3c4d -Groups sg-1a2b3c4d

```

**Example 4: This example disables source/destination checking for the specified network interface.**

```
Edit-EC2NetworkInterfaceAttribute -NetworkInterfaceId eni-1a2b3c4d -SourceDestCheck $false

```

- For API details, see
  [ModifyNetworkInterfaceAttribute](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example modifies the specified network interface so that the specified attachment is deleted on termination.**

```
Edit-EC2NetworkInterfaceAttribute -NetworkInterfaceId eni-1a2b3c4d -Attachment_AttachmentId eni-attach-1a2b3c4d -Attachment_DeleteOnTermination $true

```

**Example 2: This example modifies the description of the specified network interface.**

```
Edit-EC2NetworkInterfaceAttribute -NetworkInterfaceId eni-1a2b3c4d -Description "my description"

```

**Example 3: This example modifies the security group for the specified network interface.**

```
Edit-EC2NetworkInterfaceAttribute -NetworkInterfaceId eni-1a2b3c4d -Groups sg-1a2b3c4d

```

**Example 4: This example disables source/destination checking for the specified network interface.**

```
Edit-EC2NetworkInterfaceAttribute -NetworkInterfaceId eni-1a2b3c4d -SourceDestCheck $false

```

- For API details, see
  [ModifyNetworkInterfaceAttribute](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
