

# Use `ModifyNetworkInterfaceAttribute` with a CLI
<a name="example_ec2_ModifyNetworkInterfaceAttribute_section"></a>

The following code examples show how to use `ModifyNetworkInterfaceAttribute`.

------
#### [ CLI ]

**AWS CLI**  
**Example 1: To modify the attachment attribute of a network interface**  
The following `modify-network-interface-attribute` example modifies the `attachment` attribute of the specified network interface.  

```
aws ec2 modify-network-interface-attribute \
    --network-interface-id {{eni-686ea200}} \
    --attachment {{AttachmentId=eni-attach-43348162,DeleteOnTermination=false}}
```
This command produces no output.  
**Example 2: To modify the description attribute of a network interface**  
The following `modify-network-interface-attribute` example modifies the `description` attribute of the specified network interface.  

```
aws ec2 modify-network-interface-attribute \
    --network-interface-id {{eni-686ea200}} \
    --description {{"My description"}}
```
This command produces no output.  
**Example 3: To modify the groupSet attribute of a network interface**  
The following `modify-network-interface-attribute` example modifies the `groupSet` attribute of the specified network interface.  

```
aws ec2 modify-network-interface-attribute \
    --network-interface-id {{eni-686ea200}} \
    --groups {{sg-903004f8}} {{sg-1a2b3c4d}}
```
This command produces no output.  
**Example 4: To modify the sourceDestCheck attribute of a network interface**  
The following `modify-network-interface-attribute` example modifies the `sourceDestCheck` attribute of the specified network interface.  

```
aws ec2 modify-network-interface-attribute \
    --network-interface-id {{eni-686ea200}} \
    --no-source-dest-check
```
This command produces no output.  
For more information, see [Modify network interface attributes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/modify-network-interface-attributes.html) in the *Amazon EC2 User Guide*.  
+  For API details, see [ModifyNetworkInterfaceAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-network-interface-attribute.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

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
+  For API details, see [ModifyNetworkInterfaceAttribute](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

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
+  For API details, see [ModifyNetworkInterfaceAttribute](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.