# Creating access points restricted to a virtual private cloud

When you create an access point, you can choose to make the access point accessible from the internet, or
you can specify that all requests made through that access point must originate from a specific
Amazon Virtual Private Cloud. An access point that's accessible from the internet is said to have a
network origin of `Internet`. It can be used from anywhere on the internet,
subject to any other access restrictions in place for the access point, underlying bucket or Amazon FSx volume, and
related resources, such as the requested objects. An access point that's only accessible from a
specified Amazon VPC has a network origin of `VPC`, and Amazon S3 rejects any request made to
the access point that doesn't originate from that Amazon VPC.

###### Important

You can only specify an access point's network origin when you create the access point. After you
create the access point, you can't change its network origin.

To restrict an access point to Amazon VPC-only access, you include the `VpcConfiguration`
parameter with the request to create the access point. In the `VpcConfiguration`
parameter, you specify the Amazon VPC ID that you want to be able to use the access point. If a request is
made through the access point, the request must originate from the Amazon VPC or Amazon S3 will reject it.

You can retrieve an access point's network origin using the AWS CLI, AWS SDKs, or REST APIs. If an
access point has a Amazon VPC configuration specified, its network origin is `VPC`. Otherwise,
the access point's network origin is `Internet`.

###### Example

**_Example: Create an access point that's restricted to
Amazon VPC access_**

The following example creates an access point named `example-vpc-ap` for bucket
`amzn-s3-demo-bucket` in account `123456789012` that allows access
only from the `vpc-1a2b3c` Amazon VPC. The example then verifies that the new access point has a
network origin of `VPC`.

AWS CLI

```
`$` `aws fsx create-and-attach-s3-access-point --name `example-vpc-ap` --type OPENZFS --openzfs-configuration \
 VolumeId=`fsvol-0123456789abcdef9`,FileSystemIdentity='{Type=POSIX,PosixUser={Uid=`1234567`,Gid=`1234567`}}' \
 --s3-access-point VpcConfiguration='{VpcId=`vpc-id}`,Policy=`access-point-policy-json``
```

```
`$` `{
 {
 "S3AccessPointAttachment": {
 "Lifecycle": "CREATING",
 "CreationTime": 1728935791.8,
 "Name": "example-vpc-ap",
 "OpenZFSConfiguration": {
 "VolumeId": "fsvol-0123456789abcdef9",
 "FileSystemIdentity": {
 "Type": "UNIX",
 "UnixUser": {
 "Name": "my-unix-user"
 }
 }
 },
 "S3AccessPoint": {
 "ResourceARN": "arn:aws:s3:us-east-1:111122223333:accesspoint/example-vpc-ap",
 "Alias": "access-point-abcdef0123456789ab12jj77xy51zacd4-ext-s3alias",
 "VpcConfiguration": {
 "VpcId": "vpc-1a2b3c"
 }
 }
 }
 }`
```

To use an access point with a Amazon VPC, you must modify the access policy for your Amazon VPC endpoint.
Amazon VPC endpoints allow traffic to flow from your Amazon VPC to Amazon S3. They have access control
policies that control how resources within the Amazon VPC are allowed to interact with Amazon S3.
Requests from your Amazon VPC to Amazon S3 only succeed through an access point if the Amazon VPC endpoint policy
grants access to both the access point and the underlying bucket.

###### Note

To make resources accessible only within a Amazon VPC, make sure to create a [private hosted zone](../../../Route53/latest/DeveloperGuide/hosted-zone-private-creating.md "../../../Route53/latest/DeveloperGuide/hosted-zone-private-creating.md") for your Amazon VPC endpoint. To use a
private hosted zone, [modify your Amazon VPC settings](../../../vpc/latest/userguide/vpc-dns.md#vpc-dns-updating "../../../vpc/latest/userguide/vpc-dns.md#vpc-dns-updating") so that the [Amazon VPC
network attributes](../../../vpc/latest/userguide/vpc-dns.md#vpc-dns-support "../../../vpc/latest/userguide/vpc-dns.md#vpc-dns-support") `enableDnsHostnames` and `enableDnsSupport` are set to
`true`.

The following example policy statement configures an Amazon VPC endpoint to allow calls to
`GetObject` and an access point named `example-vpc-ap`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Principal": "*",
 "Action": [
 "s3:GetObject"
 ],
 "Effect": "Allow",
 "Resource": [
 "arn:aws:s3:us-east-1:123456789012:accesspoint/example-vpc-ap/object/*"
 ]
 }]
}`

```

###### Note

The `Resource` declaration in this example uses an Amazon Resource Name
(ARN) to specify the access point.

For more information about Amazon VPC endpoint policies, see [Gateway
endpoints for Amazon S3](../../../vpc/latest/userguide/vpc-endpoints-s3.md#vpc-endpoints-policies-s3 "../../../vpc/latest/userguide/vpc-endpoints-s3.md#vpc-endpoints-policies-s3") in the _Amazon VPC User Guide_.
