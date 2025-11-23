# Create an EC2 Instance Connect Endpoint

You can create an EC2 Instance Connect Endpoint to allow secure connection to your instances.

###### Considerations

- **Shared subnets** – You can create an
  EC2 Instance Connect Endpoint in a subnet shared with you. However, you can't use
  EC2 Instance Connect Endpoints that the VPC owner created in a subnet shared with you.
- **IP address types** – EC2 Instance Connect Endpoints
  support the following address types, which must be compatible with your
  subnet:
  - `ipv4` – Connect only to EC2 instances with private
    IPv4 addresses.
  - `dualstack` – Connect to EC2 instances with either
    private IPv4 addresses or IPv6 addresses.
  - `ipv6` – Connect only to EC2 instances with IPv6
    addresses.

###### Prerequisites

You must have the required IAM permissions to create an EC2 Instance Connect Endpoint. For more
information, see [Permissions to create, describe,
modify, and delete EC2 Instance Connect Endpoints](permissions-for-ec2-instance-connect-endpoint.md#iam-CreateInstanceConnectEndpoint "permissions-for-ec2-instance-connect-endpoint.md#iam-CreateInstanceConnectEndpoint").

Console

###### To create an EC2 Instance Connect Endpoint

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the left navigation pane, choose **Endpoints**.
3. Choose **Create endpoint**, and then specify the endpoint
   settings as follows:
   1. (Optional) For **Name tag**, enter a name for the
      endpoint.
   2. For **Type**, choose **EC2
      Instance Connect Endpoint**.
   3. Under **Network settings**, for
      **VPC**, select the VPC that has the
      target instances.
   4. (Optional) To preserve client IP addresses, expand
      **Additional settings** and select the
      **Preserve Client IP** check box.
      Otherwise, the default is to use the endpoint network
      interface as the client IP address.

   ###### Note

   This option is only available when the endpoint's IP
   address type is configured as IPv4. 5. (Optional) For **Security groups**, select the
   security group to associate with the endpoint. Otherwise, the
   default is to use the default security group for the VPC. For more
   information, see [Security groups for EC2 Instance Connect Endpoint](eice-security-groups.md "eice-security-groups.md"). 6. For **Subnet**, select the subnet in which to
   create the endpoint. 7. For **IP address type**, choose the IP
   address type for the endpoint. Choose
   **Dualstack** if you need to support
   both IPv4 and IPv6 connections to your instances. Choose
   **IPv4** if you need to support client
   IP preservation. 8. (Optional) To add a tag, choose **Add new tag**
   and enter the tag key and the tag value.

4. Review your settings and then choose **Create
   endpoint**.

The initial status of the endpoint is **Pending**. Before
you can connect to an instance using this endpoint, you must wait until the
endpoint status is **Available**. This can take a few
minutes. 5. To connect to an instance using your endpoint, see [Connect to an instance](connect-using-eice.md "connect-using-eice.md").

AWS CLI

###### To create an EC2 Instance Connect Endpoint

Use the [create-instance-connect-endpoint](../../../cli/latest/reference/ec2/create-instance-connect-endpoint.md "../../../cli/latest/reference/ec2/create-instance-connect-endpoint.md")
command.

```
aws ec2 create-instance-connect-endpoint \
    --subnet-id `subnet-0123456789example`
```

To specify the type of traffic that the endpoint supports, include the
`--ip-address-type` parameter. Valid values are
`ipv4`, `dualstack`, or `ipv6`. The
subnet must support the IP address type that you specify. When the
`--ip-address-type` parameter is omitted, the default value
is determined by the IP address type supported by the subnet.

```
aws ec2 create-instance-connect-endpoint \
    --subnet-id `subnet-0123456789example` \
    --ip-address-type `ipv4`
```

The following is example output.

```
{
        "OwnerId": "`111111111111`",
        "InstanceConnectEndpointId": "`eice-0123456789example`",
        "InstanceConnectEndpointArn": "arn:aws:ec2:`us-east-1`:`111111111111`:instance-connect-endpoint/`eice-0123456789example`",
        "State": "create-complete",
        "StateMessage": "",
        "DnsName": "`eice-0123456789example`.`0123abcd`.ec2-instance-connect-endpoint.`us-east-1`.amazonaws.com",
        "FipsDnsName": "`eice-0123456789example`.`0123abcd`.fips.ec2-instance-connect-endpoint.`us-east-1`.amazonaws.com",
        "NetworkInterfaceIds": [
            "`eni-0123abcd`"
        ],
        "VpcId": "`vpc-0123abcd`",
        "AvailabilityZone": "`us-east-1a`",
        "AvailabilityZoneId": "`use1-az4`",
        "CreatedAt": "`2023-04-07T15:43:53.000Z`",
        "SubnetId": "`subnet-0123abcd`",
        "PreserveClientIp": false,
        "SecurityGroupIds": [
            "`sg-0123abcd`"
        ],
        "Tags": [],
        "IpAddressType": "`ipv4`"
}
```

###### To monitor the creation status

The initial value for the `State` field is
`create-in-progress`. Before you can connect to an
instance using this endpoint, wait until the state is
`create-complete`. Use the [describe-instance-connect-endpoints](../../../cli/latest/reference/ec2/describe-instance-connect-endpoints.md "../../../cli/latest/reference/ec2/describe-instance-connect-endpoints.md")
command to monitor the status of the EC2 Instance Connect Endpoint. The
`--query` parameter filters the results to the
`State` field.

```
aws ec2 describe-instance-connect-endpoints --instance-connect-endpoint-ids `eice-0123456789example` --query InstanceConnectEndpoints[*].State --output text
```

The following is example output.

```
create-complete
```

PowerShell

###### To create the EC2 Instance Connect Endpoint

Use the [New-EC2InstanceConnectEndpoint](../../../powershell/latest/reference/items/New-EC2InstanceConnectEndpoint.md "../../../powershell/latest/reference/items/New-EC2InstanceConnectEndpoint.md")
cmdlet.

```
New-EC2InstanceConnectEndpoint -SubnetId `subnet-0123456789example`
```

To specify the type of traffic that the endpoint supports, include the
`-IpAddressType` parameter. Valid values are
`ipv4`, `dualstack`, or `ipv6`. The
subnet must support the IP address type that you specify. When the
`-IpAddressType` parameter is omitted, the default value is
determined by the IP address type supported by the subnet.

```
New-EC2InstanceConnectEndpoint -SubnetId `subnet-0123456789example` -IpAddressType `ipv4`
```

The following is example output.

```
OwnerId                     : `111111111111`
InstanceConnectEndpointId   : `eice-0123456789example`
InstanceConnectEndpointArn  : arn:aws:ec2:`us-east-1`:`111111111111`:instance-connect-endpoint/`eice-0123456789example`
State                       : create-complete
StateMessage                :
DnsName                     : `eice-0123456789example`.`0123abcd`.ec2-instance-connect-endpoint.`us-east-1`.amazonaws.com
FipsDnsName                 : `eice-0123456789example`.`0123abcd`.fips.ec2-instance-connect-endpoint.`us-east-1`.amazonaws.com
NetworkInterfaceIds         : {`eni-0123abcd`}
VpcId                       : `vpc-0123abcd`
AvailabilityZone            : `us-east-1a`
AvailabilityZoneId          : `use1-az4`
CreatedAt                   : 4/7/2023 3:43:53 PM
SubnetId                    : `subnet-0123abcd`
PreserveClientIp            : False
SecurityGroupIds            : {`sg-0123abcd`}
Tags                        : {}
IpAddressType               : `ipv4`
```

###### To monitor the creation status

The initial value for the `State` field is
`create-in-progress`. Before you can connect to an
instance using this endpoint, wait until the state is
`create-complete`. Use the [Get-EC2InstanceConnectEndpoint](../../../powershell/latest/reference/items/Get-EC2InstanceConnectEndpoint.md "../../../powershell/latest/reference/items/Get-EC2InstanceConnectEndpoint.md") cmdlet to
monitor the status of the EC2 Instance Connect Endpoint. `.State.Value`
filters the results to the `State` field.

```
(Get-EC2InstanceConnectEndpoint -InstanceConnectEndpointId "`eice-0123456789example`").State.Value
```

The following is example output.

```
create-complete
```
