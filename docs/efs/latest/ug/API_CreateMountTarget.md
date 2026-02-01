# CreateMountTarget

Creates a mount target for a file system. You can then mount the file system on EC2
instances by using the mount target. For more information about mount targets, see [Managing mount targets](accessing-fs.md "accessing-fs.md").

To create a mount target for an EFS file system, the file system's
lifecycle state must be `available`. For more information, see [DescribeFileSystems](API_DescribeFileSystems.md "API_DescribeFileSystems.md").

After creating the mount target, Amazon EFS returns a response that includes a
`MountTargetId` and an IP address (`IpAddress` or
`Ipv6Address`). You use this IP address when mounting the file system in an
EC2 instance. You can also use the mount target's DNS name when mounting the file
system. The EC2 instance on which you mount the file system by using the mount target
can resolve the mount target's DNS name to its IP address. For more information, see
[How Amazon EFS
works](how-it-works.md "how-it-works.md").

Note that you can create mount targets for a file system in only one VPC, and there can be
only one mount target per Availability Zone. For more information, see [Creating mount
targets](manage-fs-access-create-delete-mount-targets.md "manage-fs-access-create-delete-mount-targets.md").

If the request satisfies the requirements, Amazon EFS does the following:

- Creates a new mount target in the specified subnet.
- Creates a new network interface in the subnet with the folowing:

      + The description `Mount target *fsmt-id* for file system
       *fs-id*` where `*fsmt-id*` is the mount target ID, and `*fs-id*` is the `FileSystemId`.
      + The `requesterManaged` property of the network interface set to
       `true`, and the `requesterId` value set to
       `EFS`.

  Each mount target has one corresponding requester-managed EC2 network
  interface. After the network interface is created, Amazon EFS sets the
  `NetworkInterfaceId` field in the mount target's description to the
  network interface ID, and the IP address to its address. If network interface creation
  fails, the entire `CreateMountTarget` operation fails.

###### Note

The `CreateMountTarget` call returns only after creating the network
interface, but while the mount target state is still `creating`, you can check
the mount target creation status by calling the [DescribeMountTargets](API_DescribeMountTargets.md "API_DescribeMountTargets.md") operation, which among other things returns the mount
target state.

This operation requires permissions for the following action on the file
system:

- `elasticfilesystem:CreateMountTarget`
  This operation also requires permissions for the following Amazon EC2
  actions:

- `ec2:DescribeSubnets`
- `ec2:DescribeNetworkInterfaces`
- `ec2:CreateNetworkInterface`

## Request Syntax

```
POST /2015-02-01/mount-targets HTTP/1.1
Content-type: application/json

{
   "FileSystemId": "`string`",
   "IpAddress": "`string`",
   "IpAddressType": "`string`",
   "Ipv6Address": "`string`",
   "SecurityGroups": [ "`string`" ],
   "SubnetId": "`string`"
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[FileSystemId](#API_CreateMountTarget_RequestSyntax "#API_CreateMountTarget_RequestSyntax")**

The ID of the file system for which to create the mount target.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^(arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:file-system/fs-[0-9a-f]{8,40}|fs-[0-9a-f]{8,40})$`

Required: Yes

**[IpAddress](#API_CreateMountTarget_RequestSyntax "#API_CreateMountTarget_RequestSyntax")**

If the `IpAddressType` for the mount target is IPv4 ( `IPV4_ONLY` or
`DUAL_STACK`), then specify the IPv4 address to use. If you do not specify an
`IpAddress`, then Amazon EFS selects an unused IP address from the subnet
specified for `SubnetId`.

Type: String

Length Constraints: Minimum length of 7. Maximum length of 15.

Pattern: `^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$`

Required: No

**[IpAddressType](#API_CreateMountTarget_RequestSyntax "#API_CreateMountTarget_RequestSyntax")**

The IP address type for the mount target. The possible values are `IPV4_ONLY`
(only IPv4 addresses), `IPV6_ONLY` (only IPv6 addresses), and
`DUAL_STACK` (dual-stack, both IPv4 and IPv6 addresses). If you don’t specify an
`IpAddressType`, then `IPV4_ONLY` is used.

###### Note

The `IPAddressType` must match the IP type of the subnet. Additionally, the
`IPAddressType` parameter overrides the value set as the default IP address for
the subnet in the VPC. For example, if the `IPAddressType` is
`IPV4_ONLY` and `AssignIpv6AddressOnCreation` is `true`,
then IPv4 is used for the mount target. For more information, see [Modify the IP
addressing attributes of your subnet](../../../vpc/latest/userguide/subnet-public-ip.md "../../../vpc/latest/userguide/subnet-public-ip.md").

Type: String

Valid Values: `IPV4_ONLY | IPV6_ONLY | DUAL_STACK`

Required: No

**[Ipv6Address](#API_CreateMountTarget_RequestSyntax "#API_CreateMountTarget_RequestSyntax")**

If the `IPAddressType` for the mount target is IPv6 (`IPV6_ONLY` or
`DUAL_STACK`), then specify the IPv6 address to use. If you do not specify an
`Ipv6Address`, then Amazon EFS selects an unused IP address from the
subnet specified for `SubnetId`.

Type: String

Length Constraints: Minimum length of 3. Maximum length of 39.

Required: No

**[SecurityGroups](#API_CreateMountTarget_RequestSyntax "#API_CreateMountTarget_RequestSyntax")**

VPC security group IDs, of the form `sg-xxxxxxxx`. These must be for the same
VPC as the subnet specified. The maximum number of security groups depends on account quota.
For more information, see [Amazon VPC Quotas](../../../vpc/latest/userguide/amazon-vpc-limits.md "../../../vpc/latest/userguide/amazon-vpc-limits.md") in the
_Amazon VPC User Guide_ (see the **Security
Groups** table). If you don't specify a security group, then Amazon EFS
uses the default security group for the subnet's VPC.

Type: Array of strings

Array Members: Maximum number of 100 items.

Length Constraints: Minimum length of 11. Maximum length of 43.

Pattern: `^sg-[0-9a-f]{8,40}`

Required: No

**[SubnetId](#API_CreateMountTarget_RequestSyntax "#API_CreateMountTarget_RequestSyntax")**

The ID of the subnet to add the mount target in. For One Zone file systems, use the subnet
that is associated with the file system's Availability Zone. The subnet type must be the same type
as the `IpAddressType`.

Type: String

Length Constraints: Minimum length of 15. Maximum length of 47.

Pattern: `^subnet-[0-9a-f]{8,40}$`

Required: Yes

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "AvailabilityZoneId": "***string***",
   "AvailabilityZoneName": "***string***",
   "FileSystemId": "***string***",
   "IpAddress": "***string***",
   "Ipv6Address": "***string***",
   "LifeCycleState": "***string***",
   "MountTargetId": "***string***",
   "NetworkInterfaceId": "***string***",
   "OwnerId": "***string***",
   "SubnetId": "***string***",
   "VpcId": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[AvailabilityZoneId](#API_CreateMountTarget_ResponseSyntax "#API_CreateMountTarget_ResponseSyntax")**

The unique and consistent identifier of the Availability Zone that the mount target resides in.
For example, `use1-az1` is an AZ ID for the us-east-1 Region and it
has the same location in every AWS account.

Type: String

**[AvailabilityZoneName](#API_CreateMountTarget_ResponseSyntax "#API_CreateMountTarget_ResponseSyntax")**

The name of the Availability Zone in which the mount target is located. Availability Zones are
independently mapped to names for each AWS account. For example, the
Availability Zone `us-east-1a` for your AWS account might not be the
same location as `us-east-1a` for another AWS account.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `.+`

**[FileSystemId](#API_CreateMountTarget_ResponseSyntax "#API_CreateMountTarget_ResponseSyntax")**

The ID of the file system for which the mount target is intended.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^(arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:file-system/fs-[0-9a-f]{8,40}|fs-[0-9a-f]{8,40})$`

**[IpAddress](#API_CreateMountTarget_ResponseSyntax "#API_CreateMountTarget_ResponseSyntax")**

The IPv4 address for the mount target.

Type: String

Length Constraints: Minimum length of 7. Maximum length of 15.

Pattern: `^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$`

**[Ipv6Address](#API_CreateMountTarget_ResponseSyntax "#API_CreateMountTarget_ResponseSyntax")**

The IPv6 address for the mount target.

Type: String

Length Constraints: Minimum length of 3. Maximum length of 39.

**[LifeCycleState](#API_CreateMountTarget_ResponseSyntax "#API_CreateMountTarget_ResponseSyntax")**

Lifecycle state of the mount target.

Type: String

Valid Values: `creating | available | updating | deleting | deleted | error`

**[MountTargetId](#API_CreateMountTarget_ResponseSyntax "#API_CreateMountTarget_ResponseSyntax")**

System-assigned mount target ID.

Type: String

Length Constraints: Minimum length of 13. Maximum length of 45.

Pattern: `^fsmt-[0-9a-f]{8,40}$`

**[NetworkInterfaceId](#API_CreateMountTarget_ResponseSyntax "#API_CreateMountTarget_ResponseSyntax")**

The ID of the network interface that Amazon EFS created when it created the mount
target.

Type: String

**[OwnerId](#API_CreateMountTarget_ResponseSyntax "#API_CreateMountTarget_ResponseSyntax")**

AWS account ID that owns the resource.

Type: String

Length Constraints: Maximum length of 14.

Pattern: `^(\d{12})|(\d{4}-\d{4}-\d{4})$`

**[SubnetId](#API_CreateMountTarget_ResponseSyntax "#API_CreateMountTarget_ResponseSyntax")**

The ID of the mount target's subnet.

Type: String

Length Constraints: Minimum length of 15. Maximum length of 47.

Pattern: `^subnet-[0-9a-f]{8,40}$`

**[VpcId](#API_CreateMountTarget_ResponseSyntax "#API_CreateMountTarget_ResponseSyntax")**

The virtual private cloud (VPC) ID that the mount target is configured in.

Type: String

## Errors

**AvailabilityZonesMismatch**

Returned if the Availability Zone that was specified for the mount target is
different from the file system's Availability Zone.
For more information, see [Regional and One Zone storage redundancy](accessing-fs.md "accessing-fs.md").

**ErrorCode**

The error code is a string that uniquely identifies an error condition.
It is meant to be read and understood by programs that detect and handle errors by type.

**Message**

The error message contains a generic description of the error
condition in English. It is intended for a human audience. Simple programs display the message directly
to the end user if they encounter an error condition they don't know how or don't care to handle.
Sophisticated programs with more exhaustive error handling and proper internationalization are
more likely to ignore the error message.

HTTP Status Code: 400

**BadRequest**

Returned if the request is malformed or contains an error such as an invalid
parameter value or a missing required parameter.

**ErrorCode**

The error code is a string that uniquely identifies an error condition.
It is meant to be read and understood by programs that detect and handle errors by type.

**Message**

The error message contains a generic description of the error
condition in English. It is intended for a human audience. Simple programs display the message directly
to the end user if they encounter an error condition they don't know how or don't care to handle.
Sophisticated programs with more exhaustive error handling and proper internationalization are
more likely to ignore the error message.

HTTP Status Code: 400

**FileSystemNotFound**

Returned if the specified `FileSystemId` value doesn't exist in the
requester's AWS account.

**ErrorCode**

The error code is a string that uniquely identifies an error condition.
It is meant to be read and understood by programs that detect and handle errors by type.

**Message**

The error message contains a generic description of the error
condition in English. It is intended for a human audience. Simple programs display the message directly
to the end user if they encounter an error condition they don't know how or don't care to handle.
Sophisticated programs with more exhaustive error handling and proper internationalization are
more likely to ignore the error message.

HTTP Status Code: 404

**IncorrectFileSystemLifeCycleState**

Returned if the file system's lifecycle state is not "available".

**ErrorCode**

The error code is a string that uniquely identifies an error condition.
It is meant to be read and understood by programs that detect and handle errors by type.

**Message**

The error message contains a generic description of the error
condition in English. It is intended for a human audience. Simple programs display the message directly
to the end user if they encounter an error condition they don't know how or don't care to handle.
Sophisticated programs with more exhaustive error handling and proper internationalization are
more likely to ignore the error message.

HTTP Status Code: 409

**InternalServerError**

Returned if an error occurred on the server side.

**ErrorCode**

The error code is a string that uniquely identifies an error condition.
It is meant to be read and understood by programs that detect and handle errors by type.

**Message**

The error message contains a generic description of the error
condition in English. It is intended for a human audience. Simple programs display the message directly
to the end user if they encounter an error condition they don't know how or don't care to handle.
Sophisticated programs with more exhaustive error handling and proper internationalization are
more likely to ignore the error message.

HTTP Status Code: 500

**IpAddressInUse**

Returned if the request specified an IP address (`IpAddress` or `Ipv6Address`) that is already in use
in the subnet.

**ErrorCode**

The error code is a string that uniquely identifies an error condition.
It is meant to be read and understood by programs that detect and handle errors by type.

**Message**

The error message contains a generic description of the error
condition in English. It is intended for a human audience. Simple programs display the message directly
to the end user if they encounter an error condition they don't know how or don't care to handle.
Sophisticated programs with more exhaustive error handling and proper internationalization are
more likely to ignore the error message.

HTTP Status Code: 409

**MountTargetConflict**

Returned if the mount target would violate one of the specified restrictions based
on the file system's existing mount targets.

**ErrorCode**

The error code is a string that uniquely identifies an error condition.
It is meant to be read and understood by programs that detect and handle errors by type.

**Message**

The error message contains a generic description of the error
condition in English. It is intended for a human audience. Simple programs display the message directly
to the end user if they encounter an error condition they don't know how or don't care to handle.
Sophisticated programs with more exhaustive error handling and proper internationalization are
more likely to ignore the error message.

HTTP Status Code: 409

**NetworkInterfaceLimitExceeded**

The calling account has reached the limit for elastic network interfaces for the
specific AWS Region. Either delete some network interfaces or request
that the account quota be raised. For more information, see [Amazon VPC Quotas](../../../vpc/latest/userguide/amazon-vpc-limits.md "../../../vpc/latest/userguide/amazon-vpc-limits.md")
in the _Amazon VPC User Guide_ (see the **Network
interfaces per Region** entry in the **Network
interfaces** table).

**ErrorCode**

The error code is a string that uniquely identifies an error condition.
It is meant to be read and understood by programs that detect and handle errors by type.

**Message**

The error message contains a generic description of the error
condition in English. It is intended for a human audience. Simple programs display the message directly
to the end user if they encounter an error condition they don't know how or don't care to handle.
Sophisticated programs with more exhaustive error handling and proper internationalization are
more likely to ignore the error message.

HTTP Status Code: 409

**NoFreeAddressesInSubnet**

Returned no `IpAddress` or `Ipv6Address` was provided in the request and there are
no free IP addresses in the specified subnet.

**ErrorCode**

The error code is a string that uniquely identifies an error condition.
It is meant to be read and understood by programs that detect and handle errors by type.

**Message**

The error message contains a generic description of the error
condition in English. It is intended for a human audience. Simple programs display the message directly
to the end user if they encounter an error condition they don't know how or don't care to handle.
Sophisticated programs with more exhaustive error handling and proper internationalization are
more likely to ignore the error message.

HTTP Status Code: 409

**SecurityGroupLimitExceeded**

Returned if the number of `SecurityGroups` specified in the request is
greater than the limit, which is based on account quota. Either delete some security groups
or request that the account quota be raised. For more information, see [Amazon VPC Quotas](../../../vpc/latest/userguide/amazon-vpc-limits.md "../../../vpc/latest/userguide/amazon-vpc-limits.md")
in the _Amazon VPC User Guide_ (see the **Security Groups**
table).

**ErrorCode**

The error code is a string that uniquely identifies an error condition.
It is meant to be read and understood by programs that detect and handle errors by type.

**Message**

The error message contains a generic description of the error
condition in English. It is intended for a human audience. Simple programs display the message directly
to the end user if they encounter an error condition they don't know how or don't care to handle.
Sophisticated programs with more exhaustive error handling and proper internationalization are
more likely to ignore the error message.

HTTP Status Code: 400

**SecurityGroupNotFound**

Returned if one of the specified security groups doesn't exist in the subnet's
virtual private cloud (VPC).

**ErrorCode**

The error code is a string that uniquely identifies an error condition.
It is meant to be read and understood by programs that detect and handle errors by type.

**Message**

The error message contains a generic description of the error
condition in English. It is intended for a human audience. Simple programs display the message directly
to the end user if they encounter an error condition they don't know how or don't care to handle.
Sophisticated programs with more exhaustive error handling and proper internationalization are
more likely to ignore the error message.

HTTP Status Code: 400

**SubnetNotFound**

Returned if there is no subnet with ID `SubnetId` provided in the
request.

**ErrorCode**

The error code is a string that uniquely identifies an error condition.
It is meant to be read and understood by programs that detect and handle errors by type.

**Message**

The error message contains a generic description of the error
condition in English. It is intended for a human audience. Simple programs display the message directly
to the end user if they encounter an error condition they don't know how or don't care to handle.
Sophisticated programs with more exhaustive error handling and proper internationalization are
more likely to ignore the error message.

HTTP Status Code: 400

**UnsupportedAvailabilityZone**

Returned if the requested Amazon EFS functionality is not available in the specified Availability Zone.

**ErrorCode**

The error code is a string that uniquely identifies an error condition.
It is meant to be read and understood by programs that detect and handle errors by type.

**Message**

The error message contains a generic description of the error
condition in English. It is intended for a human audience. Simple programs display the message directly
to the end user if they encounter an error condition they don't know how or don't care to handle.
Sophisticated programs with more exhaustive error handling and proper internationalization are
more likely to ignore the error message.

HTTP Status Code: 400

## Examples

### Create a mount target at an available IPv4 address on a subnet

The following request specifies only the file system and subnet for the mount target.
The target is created at an available IPv4 address on the specified subnet, with the
default security group associated with the VPC.

#### Sample Request

```
POST /2015-02-01/mount-targets HTTP/1.1
Host: elasticfilesystem.us-west-2.amazonaws.com
x-amz-date: 20140620T221118Z
Authorization: <...>
Content-Type: application/json
Content-Length: 160

{"SubnetId": "subnet-748c5d03", "FileSystemId": "fs-01234567"}
```

#### Sample Response

```
HTTP/1.1 200 OK
x-amzn-RequestId: 01234567-89ab-cdef-0123-456789abcdef
Content-Type: application/json
Content-Length: 252

{
    "OwnerId": "231243201240",
    "MountTargetId": "fsmt-55a4413c",
    "FileSystemId": "fs-01234567",
    "SubnetId": "subnet-01234567",
    "LifeCycleState": "available",
    "IpAddress": "172.31.22.183"
    "NetworkInterfaceId":"eni-1bcb7772"
    "AvailabilityZoneId": "eus1-az2",
    "AvailabilityZoneName": "eu-south-1b",
    "VpcId": "vpc-08d45b31fa009a15e"
}
```

### Create a mount target at a specific IPv4 address

The following request specifies the file system, subnet, security group, and IPv4
address to use for the mount target.

#### Sample Request

```
POST /2015-02-01/mount-targets HTTP/1.1
Host: elasticfilesystem.us-west-2.amazonaws.com
x-amz-date: 20140620T221118Z
Authorization: <...>
Content-Type: application/json
Content-Length: 160

{
   "FileSystemId":"fs-01234567",
   "SubnetId":"subnet-01234567",
   "IpAddress":"10.0.2.42",
   "SecurityGroups":[
      "sg-01234567"
   ]
}
```

#### Sample Response

```
HTTP/1.1 200 OK
x-amzn-RequestId: 01234567-89ab-cdef-0123-456789abcdef
Content-Type: application/json
Content-Length: 252

{
   "OwnerId":"251839141158",
   "MountTargetId":"fsmt-9a13661e",
   "FileSystemId":"fs-01234567",
   "SubnetId":"subnet-fd04ff94",
   "LifeCycleState":"available",
   "IpAddress":"10.0.2.42",
   "NetworkInterfaceId":"eni-1bcb7772"
   "AvailabilityZoneId": "eus1-az2",
   "AvailabilityZoneName": "eu-south-1b",
   "VpcId": "vpc-08d45b31fa009a15e"
}
```

### Create a mount target at a specific IPv6 address

The following request specifies the file system, subnet, security group, and IPv6
address to use for the mount target.

#### Sample Request

```
POST /2015-02-01/mount-targets HTTP/1.1
Host: elasticfilesystem.us-west-2.amazonaws.com
x-amz-date: 20140620T221118Z
Authorization: <...>
Content-Type: application/json
Content-Length: 160

{
   "FileSystemId":"fs-01234567",
   "SubnetId":"subnet-01234567",
   "Ipv6Address":"2001:0db8:85a3:0000:0000:8a2e:0370:7334",
   "IpAddressType": "IPV6_ONLY",
   "SecurityGroups":[
      "sg-01234567"
   ]
}
```

#### Sample Response

```
HTTP/1.1 200 OK
x-amzn-RequestId: 01234567-89ab-cdef-0123-456789abcdef
Content-Type: application/json
Content-Length: 252

{
   "OwnerId":"251839141158",
   "MountTargetId":"fsmt-9a13661e",
   "FileSystemId":"fs-01234567",
   "SubnetId":"subnet-fd04ff94",
   "LifeCycleState":"available",
   "Ipv6Address":"2001:0db8:85a3:0000:0000:8a2e:0370:7334",
   "NetworkInterfaceId":"eni-1bcb7772"
   "AvailabilityZoneId": "eus1-az2",
   "AvailabilityZoneName": "eu-south-1b",
   "VpcId": "vpc-08d45b31fa009a15e"
}
```

### Create a mount target at an available IPv4 address on dual-stack subnet

The following request specifies the file system, subnet, and address type for the
mount target. The target is created at an available IPv4 address on the specified
dual-stack subnet, with the default security group associated with the VPC.

#### Sample Request

```
POST /2015-02-01/mount-targets HTTP/1.1
Host: elasticfilesystem.us-west-2.amazonaws.com
x-amz-date: 20140620T221118Z
Authorization: <...>
Content-Type: application/json
Content-Length: 160

{"SubnetId": "subnet-748c5d03", "FileSystemId": "fs-01234567"}
```

#### Sample Response

```
HTTP/1.1 200 OK
x-amzn-RequestId: 01234567-89ab-cdef-0123-456789abcdef
Content-Type: application/json
Content-Length: 252

{
    "OwnerId": "251839141158",
    "MountTargetId": "fsmt-55a4413c",
    "FileSystemId": "fs-01234567",
    "SubnetId":"subnet-fd04ff94",
    "LifeCycleState": "available",
    "IpAddress": "172.31.22.183"
    "Ipv6Address": "2a05:d01a:419:8611:3e57:75ab:5719:b238",
    "NetworkInterfaceId": "eni-01234567",
    "AvailabilityZoneId": "eus1-az2",
    "AvailabilityZoneName": "eu-south-1b",
    "VpcId": "vpc-08d45b31fa009a15e"
}
```

### Create mount target at specific Ipv4 and IPv6 addresses on dual-stack subnet

The following request specifies the file system, subnet, security group, IPv4 address,
IPv6 address for the mount target. The target is created at the specified IPv4 and IPv6
addresses on a dual-stack subnet.

#### Sample Request

```
POST /2015-02-01/mount-targets HTTP/1.1
Host: elasticfilesystem.us-west-2.amazonaws.com
x-amz-date: 20140620T221118Z
Authorization: <...>
Content-Type: application/json
Content-Length: 160

{
   "FileSystemId":"fs-01234567",
   "SubnetId":"subnet-01234567",
   "IpAddressType": "DUAL_STACK",
   "IpAddress": "10.0.1.25",
   "Ipv6Address":"2001:0db8:85a3:0000:0000:8a2e:0370:7334",
   "SecurityGroups":[
      "sg-01234567"
   ]
}
```

#### Sample Response

```
HTTP/1.1 200 OK
x-amzn-RequestId: 01234567-89ab-cdef-0123-456789abcdef
Content-Type: application/json
Content-Length: 252

{
    "OwnerId": "231243201240",
    "MountTargetId": "fsmt-55a4413c",
    "FileSystemId": "fs-01234567",
    "SubnetId": "subnet-01234567",
    "LifeCycleState": "available",
    "IpAddress": "10.0.1.25",
    "Ipv6Address":"2001:0db8:85a3:0000:0000:8a2e:0370:7334",
    "NetworkInterfaceId": "eni-01234567",
    "AvailabilityZoneId": "eus1-az2",
    "AvailabilityZoneName": "eu-south-1b",
    "VpcId": "vpc-08d45b31fa009a15e"
}
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/elasticfilesystem-2015-02-01/CreateMountTarget.md "../../../goto/cli2/elasticfilesystem-2015-02-01/CreateMountTarget.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/elasticfilesystem-2015-02-01/CreateMountTarget.md "../../../goto/DotNetSDKV4/elasticfilesystem-2015-02-01/CreateMountTarget.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/CreateMountTarget.md "../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/CreateMountTarget.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/elasticfilesystem-2015-02-01/CreateMountTarget.md "../../../goto/SdkForGoV2/elasticfilesystem-2015-02-01/CreateMountTarget.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/CreateMountTarget.md "../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/CreateMountTarget.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/CreateMountTarget.md "../../../goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/CreateMountTarget.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/elasticfilesystem-2015-02-01/CreateMountTarget.md "../../../goto/SdkForKotlin/elasticfilesystem-2015-02-01/CreateMountTarget.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/elasticfilesystem-2015-02-01/CreateMountTarget.md "../../../goto/SdkForPHPV3/elasticfilesystem-2015-02-01/CreateMountTarget.md")
- [AWS SDK for Python](../../../goto/boto3/elasticfilesystem-2015-02-01/CreateMountTarget.md "../../../goto/boto3/elasticfilesystem-2015-02-01/CreateMountTarget.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/CreateMountTarget.md "../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/CreateMountTarget.md")
