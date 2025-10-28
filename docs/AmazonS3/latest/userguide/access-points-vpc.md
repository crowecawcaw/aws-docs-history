# Creating access points restricted to a virtual private

cloud

When you create an access point you can choose to make the access point accessible from the internet, or
you can specify that all requests made through that access point must originate from a specific
virtual private cloud (VPC). An access point that's accessible from the internet is said to have a network origin of
`Internet`. It can be used from anywhere on the internet, subject to any
other access restrictions in place for the access point, underlying data source, and related resources,
such as the requested objects. An access point that's only accessible from a specified VPC has a
network origin of `VPC`, and Amazon S3 rejects any request made to the access point that
doesn't originate from that VPC.

###### Important

You can only specify an access point's network origin when you create the access point. After you
create the access point, you can't change its network origin.

To restrict an access point to VPC-only access, you include the `VpcConfiguration`
parameter with the request to create the access point. In the `VpcConfiguration`
parameter, you specify the VPC ID that you want to be able to use the access point. If a request
is made through the access point, the request must originate from the VPC or Amazon S3 will reject it.

You can retrieve an access point's network origin using the AWS CLI, AWS SDKs, or REST APIs. If an
access point has a VPC configuration specified, its network origin is `VPC`. Otherwise,
the access point's network origin is `Internet`.

## Example: Create and restrict an access point to an VPC ID

The following example creates an access point named `example-vpc-ap` for bucket
`amzn-s3-demo-bucket` in account `123456789012` that allows
access only from the `vpc-1a2b3c` VPC. The example then verifies that the
new access point has a network origin of `VPC`.

AWS CLI

```
aws s3control create-access-point --name example-vpc-ap --account-id 123456789012 --bucket `amzn-s3-demo-bucket` --vpc-configuration VpcId=vpc-1a2b3c
```

```
aws s3control get-access-point --name example-vpc-ap --account-id 123456789012

{
    "Name": "example-vpc-ap",
    "Bucket": "`amzn-s3-demo-bucket`",
    "NetworkOrigin": "VPC",
    "VpcConfiguration": {
        "VpcId": "vpc-1a2b3c"
    },
    "PublicAccessBlockConfiguration": {
        "BlockPublicAcls": true,
        "IgnorePublicAcls": true,
        "BlockPublicPolicy": true,
        "RestrictPublicBuckets": true
    },
    "CreationDate": "2019-11-27T00:00:00Z"
}
```

To use an access point with a VPC, you must modify the access policy for your VPC endpoint.
VPC endpoints allow traffic to flow from your VPC to Amazon S3. They have access control
policies that control how resources within the VPC are allowed to interact with Amazon S3.
Requests from your VPC to Amazon S3 only succeed through an access point if the VPC endpoint policy
grants access to both the access point and the underlying bucket.

###### Note

To make resources accessible only within a VPC, make sure to create a [private hosted zone](../../../Route53/latest/DeveloperGuide/hosted-zone-private-creating.md "../../../Route53/latest/DeveloperGuide/hosted-zone-private-creating.md") for your VPC endpoint. To use a
private hosted zone, [modify your VPC settings](../../../vpc/latest/userguide/vpc-dns.md#vpc-dns-updating "../../../vpc/latest/userguide/vpc-dns.md#vpc-dns-updating") so that the [VPC
network attributes](../../../vpc/latest/userguide/vpc-dns.md#vpc-dns-support "../../../vpc/latest/userguide/vpc-dns.md#vpc-dns-support")
`enableDnsHostnames` and `enableDnsSupport` are set to
`true`.

The following example policy statement configures a VPC endpoint to allow calls to
`GetObject` for a bucket named `awsexamplebucket1` and an access point
named `example-vpc-ap`.

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
 "arn:aws:s3:::awsexamplebucket1/*",
 "arn:aws:s3:us-west-2:123456789012:accesspoint/example-vpc-ap/object/*"
 ]
 }]
}`

```

###### Note

The `"Resource"` declaration in this example uses an Amazon Resource Name
(ARN) to specify the access point. For more information about access point ARNs, see [Referencing access points with ARNs, access point aliases, or virtual-hosted–style URIs](access-points-naming.md "access-points-naming.md").

For more information about VPC endpoint policies, see [Using
endpoint policies for Amazon S3](../../../vpc/latest/userguide/vpc-endpoints-s3.md#vpc-endpoints-policies-s3 "../../../vpc/latest/userguide/vpc-endpoints-s3.md#vpc-endpoints-policies-s3") in the _VPC User Guide_.

For a tutorial on creating access points with VPC endpoints, see [Managing Amazon S3 access with VPC endpoints and access points](https://aws.amazon.com/blogs/storage/managing-amazon-s3-access-with-vpc-endpoints-and-s3-access-points/ "https://aws.amazon.com/blogs/storage/managing-amazon-s3-access-with-vpc-endpoints-and-s3-access-points/").

## Example: Create and restrict an access point

attached to an FSx for OpenZFS volume to an VPC ID

You can create an access point that is attached it to an FSx for OpenZFS volume using the Amazon FSx
console, AWS CLI, or API. Once attached, you can use the S3 object APIs to access your file
data from a specified VPC.

For instructions on creating and restricting an access point attached to an FSx for OpenZFS volume see,
[Creating access points restricted to a virtual private cloud (VPC)](../../../fsx/latest/OpenZFSGuide/create-access-points.md "../../../fsx/latest/OpenZFSGuide/create-access-points.md") in the
_FSx for OpenZFS User Guide_.
