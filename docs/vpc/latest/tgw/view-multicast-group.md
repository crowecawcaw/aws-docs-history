# View multicast groups in AWS Transit Gateway

You can view information about your multicast groups to verify that members were
discovered using the IGMPv2 protocol. **Member type** (in the console), or
`MemberType` (in the AWS CLI) displays IGMP when AWS discovered members with the
protocol.

###### To view multicast groups using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. On the navigation pane, choose **Transit Gateway Multicast**.
3. Select the multicast domain.
4. Choose the **Groups** tab.

###### To view multicast groups using the AWS CLI

Use the [search-transit-gateway-multicast-groups](../../../cli/latest/reference/ec2/search-transit-gateway-multicast-groups.md "../../../cli/latest/reference/ec2/search-transit-gateway-multicast-groups.md") command.

The following example shows that the IGMP protocol discovered multicast group
members.

```
aws ec2 search-transit-gateway-multicast-groups --transit-gateway-multicast-domain `tgw-mcast-domain-000fb24d04EXAMPLE``{
 "MulticastGroups": [
 {
 "GroupIpAddress": "224.0.1.0",
 "TransitGatewayAttachmentId": "tgw-attach-0372e72386EXAMPLE",
 "SubnetId": "subnet-0187aff814EXAMPLE",
 "ResourceId": "vpc-0065acced4EXAMPLE",
 "ResourceType": "vpc",
 "NetworkInterfaceId": "eni-03847706f6EXAMPLE",
 "MemberType": "igmp"
 }
 ]
}`
```
