# Connect to Amazon SageMaker Studio and Studio Classic

Through an Interface VPC Endpoint

You can connect to your Amazon SageMaker Studio and Amazon SageMaker Studio Classic from your [Amazon Virtual Private Cloud](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md") (Amazon VPC) through an [interface endpoint](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md") in your VPC
instead of connecting over the internet. When you use an interface VPC endpoint (interface
endpoint), communication between your VPC and Studio or Studio Classic is conducted
entirely and securely within the AWS network.

Studio and Studio Classic supports interface endpoints that are powered by [AWS PrivateLink](../../../vpc/latest/userguide/endpoint-services-overview.md "../../../vpc/latest/userguide/endpoint-services-overview.md"). Each interface endpoint is represented by one or more [Elastic network
interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") with private IP addresses in your VPC subnets.

Studio and Studio Classic supports interface endpoints in all AWS Regions where both
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/pricing/ "https://aws.amazon.com/sagemaker/pricing/") and [Amazon VPC](https://aws.amazon.com/vpc/pricing/ "https://aws.amazon.com/vpc/pricing/") are available.

###### Topics

- [Create a VPC Endpoint](#studio-interface-endpoint-create "#studio-interface-endpoint-create")
- [Create a VPC Endpoint Policy for
  Studio or Studio Classic](#studio-private-link-policy "#studio-private-link-policy")
- [Allow Access Only from Within Your
  VPC](#studio-private-link-restrict "#studio-private-link-restrict")

## Create a VPC Endpoint

You can create an interface endpoint to connect to Studio or Studio Classic with
either the AWS console or the AWS Command Line Interface (AWS CLI). For instructions, see [Creating an
interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint"). Make sure that you create interface endpoints for all of
the subnets in your VPC from which you want to connect to Studio and Studio Classic.

When you create an interface endpoint, ensure that the security groups on your
endpoint allow inbound access for HTTPS traffic from the security groups associated with
Studio and Studio Classic. For more information, see [Control access to services with VPC endpoints](../../../vpc/latest/privatelink/vpc-endpoints-access.md#vpc-endpoints-security-groups "../../../vpc/latest/privatelink/vpc-endpoints-access.md#vpc-endpoints-security-groups").

###### Note

In addition to creating an interface endpoint to connect to Studio and
Studio Classic, create an interface endpoint to connect to the Amazon SageMaker API. When users
call [`CreatePresignedDomainUrl`](../APIReference/API_CreatePresignedDomainUrl.md "../APIReference/API_CreatePresignedDomainUrl.md") to get the URL to connect to
Studio and Studio Classic, that call goes through the interface endpoint used to
connect to the SageMaker API.

When you create the interface endpoint, specify
`aws.sagemaker.`Region`.studio` as
the service name for either Studio or Studio Classic. After you create the interface
endpoint, enable private DNS for your endpoint. When you connect to Studio or
Studio Classic from within the VPC using the SageMaker API, the AWS CLI, or the console, you
connect through the interface endpoint instead of the public internet. You also need to
set up a custom DNS with private hosted zones for the Amazon VPC endpoint so Studio or
Studio Classic can access the SageMaker API using the
`api.sagemaker.$region.amazonaws.com` endpoint rather than using the VPC
endpoint URL. For instructions on setting up a private hosted zone, see [Working with private hosted zones](../../../Route53/latest/DeveloperGuide/hosted-zones-private.md "../../../Route53/latest/DeveloperGuide/hosted-zones-private.md").

## Create a VPC Endpoint Policy for

Studio or Studio Classic

You can attach an Amazon VPC endpoint policy to the interface VPC endpoints that you use to
connect to Studio or Studio Classic. The endpoint policy controls access to Studio
or Studio Classic. You can specify the following:

- The principal that can perform actions.
- The actions that can be performed.
- The resources on which actions can be performed.

To use a VPC endpoint with Studio or Studio Classic, your endpoint policy must allow
the `CreateApp` operation on the KernelGateway app type. This allows traffic
that is routed to through the VPC endpoint to call the `CreateApp` API. The
following example VPC endpoint policy shows how to allow the `CreateApp`
operation.

```
{
 "Statement": [
   {
     "Action": "sagemaker:CreateApp",
     "Effect": "Allow",
     "Resource": "arn:aws:sagemaker:us-west-2:acct-id:app/domain-id/*",
     "Principal": "*"
   }
 ]
}
```

For more information, see [Controlling access to services
with VPC endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md").

The following example of a VPC endpoint policy specifies that all users that have
access to the endpoint are allowed to access the user profiles in the SageMaker AI domain with
the specified domain ID. Access to other domains is denied.

```
{
  "Statement": [
      {
          "Action": "sagemaker:CreatePresignedDomainUrl",
          "Effect": "Allow",
          "Resource": "arn:aws:sagemaker:us-west-2:acct-id:user-profile/domain-id/*",
          "Principal": "*"
      }
  ]
}
```

## Allow Access Only from Within Your

VPC

Users outside your VPC can connect to Studio or Studio Classic over the internet even
if you set up an interface endpoint in your VPC.

To allow access to only connections made from within your VPC, create an AWS Identity and Access Management
(IAM) policy to that effect. Add that policy to every user, group, or role used to
access Studio or Studio Classic. This feature is only supported when using IAM mode
for authentication, and is not supported in IAM Identity Center mode. The following examples
demonstrate how to create such policies.

###### Important

If you apply an IAM policy similar to one of the following examples, users
cannot access Studio or Studio Classic or the specified SageMaker APIs through the SageMaker AI
console. To access Studio or Studio Classic, users must use a presigned URL or call
the SageMaker APIs directly.

**Example 1: Allow connections only within the subnet of an
interface endpoint**

The following policy allows connections only to callers within the subnet where you
created the interface endpoint.

JSON

```
`{
 "Id": "sagemaker-studio-example-1",
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "EnableSageMakerStudioAccess",
 "Effect": "Allow",
 "Action": [
 "sagemaker:CreatePresignedDomainUrl",
 "sagemaker:DescribeUserProfile"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:SourceVpc": "`vpc-111bbaaa`"
 }
 }
 }
 ]
}`

```

**Example 2: Allow connections only through interface endpoints
using `aws:sourceVpce`**

The following policy allows connections only to those made through the interface
endpoints specified by the `aws:sourceVpce` condition key. For example, the
first interface endpoint could allow access through the SageMaker AI console. The second
interface endpoint could allow access through the SageMaker API.

JSON

```
`{
 "Id": "sagemaker-studio-example-2",
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "EnableSageMakerStudioAccess",
 "Effect": "Allow",
 "Action": [
 "sagemaker:CreatePresignedDomainUrl",
 "sagemaker:DescribeUserProfile"
 ],
 "Resource": "*",
 "Condition": {
 "ForAnyValue:StringEquals": {
 "aws:sourceVpce": [
 `"vpce-111bbccc"`,
 `"vpce-111bbddd"`
 ]
 }
 }
 }
 ]
}`

```

This policy includes the [`DescribeUserProfile`](../APIReference/API_DescribeUserProfile.md "../APIReference/API_DescribeUserProfile.md") action. Typically you call
`DescribeUserProfile` to make sure that the status of the user profile is
`InService` before you try to connect to the domain. For example:

```
aws sagemaker describe-user-profile \
    --domain-id `domain-id` \
    --user-profile-name `profile-name`
```

Response:

```
{
    "DomainId": "domain-id",
    "UserProfileArn": "arn:aws:sagemaker:us-west-2:acct-id:user-profile/domain-id/profile-name",
    "UserProfileName": "profile-name",
    "HomeEfsFileSystemUid": "200001",
    "Status": "InService",
    "LastModifiedTime": 1605418785.555,
    "CreationTime": 1605418477.297
}
```

```
aws sagemaker create-presigned-domain-url
    --domain-id `domain-id` \
    --user-profile-name `profile-name`
```

Response:

```
{
    "AuthorizedUrl": "https://domain-id.studio.us-west-2.sagemaker.aws/auth?token=AuthToken"
}
```

For both of these calls, if you are using a version of the AWS SDK that was released
before August 13, 2018, you must specify the endpoint URL in the call. For example, the
following example shows a call to `create-presigned-domain-url`:

```
aws sagemaker create-presigned-domain-url
    --domain-id `domain-id` \
    --user-profile-name `profile-name` \
    --endpoint-url `vpc-endpoint-id`.api.sagemaker.`Region`.vpce.amazonaws.com
```

**Example 3: Allow connections from IP addresses using
`aws:SourceIp`**

The following policy allows connections only from the specified range of IP addresses
using the `aws:SourceIp` condition key.

JSON

```
`{
 "Id": "sagemaker-studio-example-3",
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "EnableSageMakerStudioAccess",
 "Effect": "Allow",
 "Action": [
 "sagemaker:CreatePresignedDomainUrl",
 "sagemaker:DescribeUserProfile"
 ],
 "Resource": "*",
 "Condition": {
 "IpAddress": {
 "aws:SourceIp": [
 `"192.0.2.0/24"`,
 `"203.0.113.0/24"`
 ]
 }
 }
 }
 ]
}`

```

**Example 4: Allow connections from IP addresses through an
interface endpoint using `aws:VpcSourceIp`**

If you are accessing Studio or Studio Classic through an interface endpoint, you can
use the `aws:VpcSourceIp` condition key to allow connections only from the
specified range of IP addresses within the subnet where you created the interface
endpoint as shown in the following policy:

JSON

```
`{
 "Id": "sagemaker-studio-example-4",
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "EnableSageMakerStudioAccess",
 "Effect": "Allow",
 "Action": [
 "sagemaker:CreatePresignedDomainUrl",
 "sagemaker:DescribeUserProfile"
 ],
 "Resource": "*",
 "Condition": {
 "IpAddress": {
 "aws:VpcSourceIp": [
 `"192.0.2.0/24"`,
 `"203.0.113.0/24"`
 ]
 },
 "StringEquals": {
 "aws:SourceVpc": `"vpc-111bbaaa"`
 }
 }
 }
 ]
}`

```
