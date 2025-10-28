# Use `DescribeNetworkInterfaces` with a CLI

The following code examples show how to use `DescribeNetworkInterfaces`.

CLI

**AWS CLI**

**To describe your network interfaces**

This example describes all your network interfaces.

Command:

```
`aws ec2 describe-network-interfaces`

```

Output:

```
{
  "NetworkInterfaces": [
      {
          "Status": "in-use",
          "MacAddress": "02:2f:8f:b0:cf:75",
          "SourceDestCheck": true,
          "VpcId": "vpc-a01106c2",
          "Description": "my network interface",
          "Association": {
              "PublicIp": "203.0.113.12",
              "AssociationId": "eipassoc-0fbb766a",
              "PublicDnsName": "ec2-203-0-113-12.compute-1.amazonaws.com",
              "IpOwnerId": "123456789012"
          },
          "NetworkInterfaceId": "eni-e5aa89a3",
          "PrivateIpAddresses": [
              {
                  "PrivateDnsName": "ip-10-0-1-17.ec2.internal",
                  "Association": {
                      "PublicIp": "203.0.113.12",
                      "AssociationId": "eipassoc-0fbb766a",
                      "PublicDnsName": "ec2-203-0-113-12.compute-1.amazonaws.com",
                      "IpOwnerId": "123456789012"
                  },
                  "Primary": true,
                  "PrivateIpAddress": "10.0.1.17"
              }
          ],
          "RequesterManaged": false,
          "Ipv6Addresses": [],
          "PrivateDnsName": "ip-10-0-1-17.ec2.internal",
          "AvailabilityZone": "us-east-1d",
          "Attachment": {
              "Status": "attached",
              "DeviceIndex": 1,
              "AttachTime": "2013-11-30T23:36:42.000Z",
              "InstanceId": "i-1234567890abcdef0",
              "DeleteOnTermination": false,
              "AttachmentId": "eni-attach-66c4350a",
              "InstanceOwnerId": "123456789012"
          },
          "Groups": [
              {
                  "GroupName": "default",
                  "GroupId": "sg-8637d3e3"
              }
          ],
          "SubnetId": "subnet-b61f49f0",
          "OwnerId": "123456789012",
          "TagSet": [],
          "PrivateIpAddress": "10.0.1.17"
      },
      {
          "Status": "in-use",
          "MacAddress": "02:58:f5:ef:4b:06",
          "SourceDestCheck": true,
          "VpcId": "vpc-a01106c2",
          "Description": "Primary network interface",
          "Association": {
              "PublicIp": "198.51.100.0",
              "IpOwnerId": "amazon"
          },
          "NetworkInterfaceId": "eni-f9ba99bf",
          "PrivateIpAddresses": [
              {
                  "Association": {
                      "PublicIp": "198.51.100.0",
                      "IpOwnerId": "amazon"
                  },
                  "Primary": true,
                  "PrivateIpAddress": "10.0.1.149"
              }
          ],
          "RequesterManaged": false,
          "Ipv6Addresses": [],
          "AvailabilityZone": "us-east-1d",
          "Attachment": {
              "Status": "attached",
              "DeviceIndex": 0,
              "AttachTime": "2013-11-30T23:35:33.000Z",
              "InstanceId": "i-0598c7d356eba48d7",
              "DeleteOnTermination": true,
              "AttachmentId": "eni-attach-1b9db777",
              "InstanceOwnerId": "123456789012"
          },
          "Groups": [
              {
                  "GroupName": "default",
                  "GroupId": "sg-8637d3e3"
              }
          ],
          "SubnetId": "subnet-b61f49f0",
          "OwnerId": "123456789012",
          "TagSet": [],
          "PrivateIpAddress": "10.0.1.149"
      }
  ]
}
```

This example describes network interfaces that have a tag with the key `Purpose` and the value `Prod`.

Command:

```
`aws ec2 describe-network-interfaces --filters `Name=tag:Purpose,Values=Prod``

```

Output:

```
{
  "NetworkInterfaces": [
      {
          "Status": "available",
          "MacAddress": "12:2c:bd:f9:bf:17",
          "SourceDestCheck": true,
          "VpcId": "vpc-8941ebec",
          "Description": "ProdENI",
          "NetworkInterfaceId": "eni-b9a5ac93",
          "PrivateIpAddresses": [
              {
                  "PrivateDnsName": "ip-10-0-1-55.ec2.internal",
                  "Primary": true,
                  "PrivateIpAddress": "10.0.1.55"
              },
              {
                  "PrivateDnsName": "ip-10-0-1-117.ec2.internal",
                  "Primary": false,
                  "PrivateIpAddress": "10.0.1.117"
              }
          ],
          "RequesterManaged": false,
          "PrivateDnsName": "ip-10-0-1-55.ec2.internal",
          "AvailabilityZone": "us-east-1d",
          "Ipv6Addresses": [],
          "Groups": [
              {
                  "GroupName": "MySG",
                  "GroupId": "sg-905002f5"
              }
          ],
          "SubnetId": "subnet-31d6c219",
          "OwnerId": "123456789012",
          "TagSet": [
              {
                  "Value": "Prod",
                  "Key": "Purpose"
              }
          ],
          "PrivateIpAddress": "10.0.1.55"
      }
  ]
}
```

- For API details, see
  [DescribeNetworkInterfaces](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-network-interfaces.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-network-interfaces.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example describes the specified network interface.**

```
Get-EC2NetworkInterface -NetworkInterfaceId eni-12345678

```

**Output:**

```
Association        :
Attachment         : Amazon.EC2.Model.NetworkInterfaceAttachment
AvailabilityZone   : us-west-2c
Description        :
Groups             : {my-security-group}
MacAddress         : 0a:e9:a6:19:4c:7f
NetworkInterfaceId : eni-12345678
OwnerId            : 123456789012
PrivateDnsName     : ip-10-0-0-107.us-west-2.compute.internal
PrivateIpAddress   : 10.0.0.107
PrivateIpAddresses : {ip-10-0-0-107.us-west-2.compute.internal}
RequesterId        :
RequesterManaged   : False
SourceDestCheck    : True
Status             : in-use
SubnetId           : subnet-1a2b3c4d
TagSet             : {}
VpcId              : vpc-12345678
```

**Example 2: This example describes all your network interfaces.**

```
Get-EC2NetworkInterface

```

- For API details, see
  [DescribeNetworkInterfaces](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example describes the specified network interface.**

```
Get-EC2NetworkInterface -NetworkInterfaceId eni-12345678

```

**Output:**

```
Association        :
Attachment         : Amazon.EC2.Model.NetworkInterfaceAttachment
AvailabilityZone   : us-west-2c
Description        :
Groups             : {my-security-group}
MacAddress         : 0a:e9:a6:19:4c:7f
NetworkInterfaceId : eni-12345678
OwnerId            : 123456789012
PrivateDnsName     : ip-10-0-0-107.us-west-2.compute.internal
PrivateIpAddress   : 10.0.0.107
PrivateIpAddresses : {ip-10-0-0-107.us-west-2.compute.internal}
RequesterId        :
RequesterManaged   : False
SourceDestCheck    : True
Status             : in-use
SubnetId           : subnet-1a2b3c4d
TagSet             : {}
VpcId              : vpc-12345678
```

**Example 2: This example describes all your network interfaces.**

```
Get-EC2NetworkInterface

```

- For API details, see
  [DescribeNetworkInterfaces](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
