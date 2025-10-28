# Modify network interface attributes

You can change the following network interface attributes:

- Description
- Security groups
- Delete on termination
- Source/destination check
- Idle connection tracking timeout

###### Considerations

You can't change the attributes of a requester-managed network interface.

Console

###### To modify network interface attributes

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Network Interfaces**.
3. Select the checkbox for the network interface.
4. To change the description, do the following
   1. Choose **Actions**, **Change description**.
   2. For **Description**, enter a description.
   3. Choose **Save**.

5. To change the security groups, do the following:
   1. Choose **Actions**, **Change security groups**.
   2. For **Associated security groups**, add and remove security
      groups as needed. The security group and network interface must be created for
      the same VPC.
   3. Choose **Save**.

6. To change the termination behavior, do the following:
   1. Choose **Actions**, **Change
      termination behavior**.
   2. Select or clear **Delete on termination**,
      **Enable**.
   3. Choose **Save**.

7. To change source/destination checking, do the following:
   1. Choose **Actions**, **Change
      source/dest check**.
   2. Select or clear **Source/destination check**,
      **Enable**.
   3. Choose **Save**.

8. To change idle connection tracking timeouts, do the following:
   1. Choose **Actions**,
      **Modify idle connection tracking timeout**.
   2. Modify timeout values as needed. For more information, see
      [Idle connection tracking timeout](security-group-connection-tracking.md#connection-tracking-timeouts "security-group-connection-tracking.md#connection-tracking-timeouts").
      - **TCP established timeout**: Timeout (in seconds) for idle TCP
        connections in an established state.
        - Min: `60` seconds
        - Max: `432000` seconds
        - Default: `350` seconds for [Nitrov6](../../../ec2/latest/instancetypes/ec2-nitro-instances.md "../../../ec2/latest/instancetypes/ec2-nitro-instances.md")
          instance types, excluding P6e-GB200. And `432000` seconds for other instance types, including P6e-GB200.
        - Recommended: Less than `432000` seconds

      - **UDP timeout**: Timeout (in seconds) for idle UDP flows that
        have seen traffic only in a single direction or a single request-response transaction.
        - Min: `30` seconds
        - Max: `60` seconds
        - Default: `30` seconds

      - **UDP stream timeout**: Timeout (in seconds) for idle UDP flows
        classified as streams which have seen more than one request-response transaction.
        - Min: `60` seconds
        - Max: `180` seconds
        - Default: `180` seconds

   3. Choose **Save**.

AWS CLI

###### Example: To modify the description

Use the following [modify-network-interface-attribute](../../../cli/latest/reference/ec2/modify-network-interface-attribute.md "../../../cli/latest/reference/ec2/modify-network-interface-attribute.md")
command.

```
aws ec2 modify-network-interface-attribute \
    --network-interface-id `eni-1234567890abcdef0` \
    --description "`my updated description`"
```

###### Example: To modify the security groups

Use the following [modify-network-interface-attribute](../../../cli/latest/reference/ec2/modify-network-interface-attribute.md "../../../cli/latest/reference/ec2/modify-network-interface-attribute.md")
command.

```
aws ec2 modify-network-interface-attribute \
    --network-interface-id `eni-1234567890abcdef0` \
    --groups `sg-1234567890abcdef0`
```

###### Example: To modify the termination behavior

Use the following [modify-network-interface-attribute](../../../cli/latest/reference/ec2/modify-network-interface-attribute.md "../../../cli/latest/reference/ec2/modify-network-interface-attribute.md")
command.

```
aws ec2 modify-network-interface-attribute \
    --network-interface-id `eni-1234567890abcdef0` \
    --attachment AttachmentId=`eni-attach-43348162abEXAMPLE`,DeleteOnTermination=`false`
```

###### Example: To enable source/destination checking

Use the following [modify-network-interface-attribute](../../../cli/latest/reference/ec2/modify-network-interface-attribute.md "../../../cli/latest/reference/ec2/modify-network-interface-attribute.md")
command.

```
aws ec2 modify-network-interface-attribute \
    --network-interface-id `eni-1234567890abcdef0` \
    --source-dest-check
```

###### Example: To modify idle connection tracking timout

Use the following [modify-network-interface-attribute](../../../cli/latest/reference/ec2/modify-network-interface-attribute.md "../../../cli/latest/reference/ec2/modify-network-interface-attribute.md")
command. For more information, see [Idle connection tracking timeout](security-group-connection-tracking.md#connection-tracking-timeouts "security-group-connection-tracking.md#connection-tracking-timeouts").

```
aws ec2 modify-network-interface-attribute \
    --network-interface-id `eni-1234567890abcdef0` \
    --connection-tracking-specification TcpEstablishedTimeout=`172800`,UdpStreamTimeout=`90`,UdpTimeout=`60`
```

PowerShell

###### Example: To modify the description

Use the [Edit-EC2NetworkInterfaceAttribute](../../../powershell/latest/reference/items/Edit-EC2NetworkInterfaceAttribute.md "../../../powershell/latest/reference/items/Edit-EC2NetworkInterfaceAttribute.md")
cmdlet.

```
Edit-EC2NetworkInterfaceAttribute `
    -NetworkInterfaceId `eni-1234567890abcdef0` `
    -Description "`my updated description`"
```

###### Example: To modify the security groups

Use the [Edit-EC2NetworkInterfaceAttribute](../../../powershell/latest/reference/items/Edit-EC2NetworkInterfaceAttribute.md "../../../powershell/latest/reference/items/Edit-EC2NetworkInterfaceAttribute.md")
cmdlet.

```
Edit-EC2NetworkInterfaceAttribute `
    -NetworkInterfaceId `eni-1234567890abcdef0` `
    -Group `sg-1234567890abcdef0`
```

###### Example: To modify the termination behavior

Use the [Edit-EC2NetworkInterfaceAttribute](../../../powershell/latest/reference/items/Edit-EC2NetworkInterfaceAttribute.md "../../../powershell/latest/reference/items/Edit-EC2NetworkInterfaceAttribute.md")
cmdlet.

```
Edit-EC2NetworkInterfaceAttribute `
    -NetworkInterfaceId `eni-1234567890abcdef0` `
    -Attachment_AttachmentId `eni-attach-43348162abEXAMPLE` `
    -Attachment_DeleteOnTermination `$false`
```

###### Example: To enable source/destination checking

Use the [Edit-EC2NetworkInterfaceAttribute](../../../powershell/latest/reference/items/Edit-EC2NetworkInterfaceAttribute.md "../../../powershell/latest/reference/items/Edit-EC2NetworkInterfaceAttribute.md")
cmdlet.

```
Edit-EC2NetworkInterfaceAttribute `
    -NetworkInterfaceId `eni-1234567890abcdef0` `
    -SourceDestCheck `$true`
```

###### Example: To modify idle connection tracking timeouts

Use the [Edit-EC2NetworkInterfaceAttribute](../../../powershell/latest/reference/items/Edit-EC2NetworkInterfaceAttribute.md "../../../powershell/latest/reference/items/Edit-EC2NetworkInterfaceAttribute.md")
cmdlet. For more information, see [Idle connection tracking timeout](security-group-connection-tracking.md#connection-tracking-timeouts "security-group-connection-tracking.md#connection-tracking-timeouts").

```
Edit-EC2NetworkInterfaceAttribute `
    -NetworkInterfaceId `eni-1234567890abcdef0` `
    -ConnectionTrackingSpecification_TcpEstablishedTimeout `172800` `
    -ConnectionTrackingSpecification_UdpStreamTimeout `90` `
    -ConnectionTrackingSpecification_UdpTimeout `60`
```
