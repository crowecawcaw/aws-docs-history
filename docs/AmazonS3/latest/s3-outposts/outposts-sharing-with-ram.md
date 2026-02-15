# Sharing S3 on Outposts by using AWS RAM

Amazon S3 on Outposts supports sharing S3 capacity across multiple accounts within an
organization by using AWS Resource Access Manager ([AWS RAM](../../../ram/latest/userguide/what-is.md "../../../ram/latest/userguide/what-is.md")). With S3 on Outposts sharing, you can allow others to
create and manage buckets, endpoints, and access points on your Outpost.

This topic demonstrates how to use AWS RAM to share S3 on Outposts and related resources with
another AWS account in your AWS organization.

## Prerequisites

- The Outpost owner account has an organization configured in AWS Organizations. For more
  information, see [Creating
  an organization](../../../organizations/latest/userguide/orgs_manage_org_create.md "../../../organizations/latest/userguide/orgs_manage_org_create.md") in the _AWS Organizations User Guide_.
- The organization includes the AWS account that you want to share your
  S3 on Outposts capacity with. For more information, see [Sending invitations to AWS accounts](../../../organizations/latest/userguide/orgs_manage_accounts_invites.md#orgs_manage_accounts_invite-account "../../../organizations/latest/userguide/orgs_manage_accounts_invites.md#orgs_manage_accounts_invite-account") in the
  _AWS Organizations User Guide_.
- Select one of the following options that you want to share. The second
  resource (either **Subnets** or **Outposts**)
  must be selected so that endpoints are also accessible. Endpoints are a
  networking requirement in order to access data stored in S3 on Outposts.

| **Option 1**                                                                                                                                                                                                                                                            | **Option 2**                                                                                                                                                                                                                                                                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **S3 on Outposts**<br>Allows the user to create buckets on your Outposts and<br>access points and to add objects to those buckets.<br>**Subnets**<br>Allows the user to use your virtual private cloud (VPC)<br>and the endpoints that are associated with your subnet. | **S3 on Outposts**<br>Allows the user to create buckets on your Outposts and<br>access points and to add objects to those buckets.<br>**Outposts**<br>Allows the user to see S3 capacity charts and the AWS Outposts<br>console home page. Also allows users to create subnets on<br>shared Outposts and create endpoints. |

## Procedure

1. Sign in to the AWS Management Console by using the AWS account that owns the Outpost, and
   then open the AWS RAM console at [https://console.aws.amazon.com/ram/home](https://console.aws.amazon.com/ram/home "https://console.aws.amazon.com/ram/home").
2. Make sure that you have enabled sharing with AWS Organizations in AWS RAM. For
   information, see [Enable resource sharing within AWS Organizations](../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs "../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs") in the
   _AWS RAM User Guide_.
3. Use either Option 1 or Option 2 in the [prerequisites](#outposts-ram-prereqs "#outposts-ram-prereqs") to create a resource share. If you have multiple
   S3 on Outposts resources, select the Amazon Resource Names (ARNs) of the resources
   that you want to share. To enable endpoints, share either your subnet or
   Outpost.

For more information about how to create a resource share, see [Create a resource share](../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-create "../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-create") in the
_AWS RAM User Guide_. 4. The AWS account that you shared your resources with should now be able to
use S3 on Outposts. Depending on the option that you selected in the [prerequisites](#outposts-ram-prereqs "#outposts-ram-prereqs"), provide the following
information to the account user:

| **Option 1**                                                           | **Option 2**   |
| ---------------------------------------------------------------------- | -------------- |
| The Outpost ID<br>The VPC ID<br>The subnet ID<br>The security group ID | The Outpost ID |

###### Note

The user can confirm that the resources have been shared with them by using the
AWS RAM console, the AWS Command Line Interface (AWS CLI), AWS SDKs, or REST API. The user can view
their existing resource shares by using the [get-resource-shares](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/get-resource-shares.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/get-resource-shares.html") CLI command.

## Usage examples

After you have shared your S3 on Outposts resources with another account, that account
can manage buckets and objects on your Outpost. If you shared the
**Subnets** resource, then that account can use the endpoint that
you created. The following examples demonstrate how a user can use the AWS CLI to interact
with your Outpost after you share these resources.

###### Example: Create a bucket

The following example creates a bucket named `amzn-s3-demo-bucket1` on the Outpost
`op-01ac5d28a6a232904`.
Before using this command, replace each `user input
 placeholder` with the appropriate values for your use
case.

```
aws s3control create-bucket --bucket ``amzn-s3-demo-bucket1`` --outpost-id `op-01ac5d28a6a232904`
```

For more information about this command, see [create-bucket](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/create-bucket.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/create-bucket.html") in the _AWS CLI Reference_.

###### Example: Create an access point

The following example creates an access point on an Outpost by using the example
parameters in the following table. Before using this command, replace these
`user input placeholder` values and
the AWS Region code with the appropriate values for your use case.

| **Parameter**       | **Value**                      |
| ------------------- | ------------------------------ |
| Account ID          | `111122223333`                 |
| Access point name   | `example-outpost-access-point` |
| Outpost ID          | `op-01ac5d28a6a232904`         |
| Outpost bucket name | `amzn-s3-demo-bucket1`         |
| VPC ID              | `vpc-1a2b3c4d5e6f7g8h9`        |

###### Note

The Account ID parameter must be the AWS account ID of the bucket owner,
which is the shared user.

```
aws s3control create-access-point --account-id `111122223333` --name `example-outpost-access-point` \
--bucket arn:aws:s3-outposts:`us-east-1`:`111122223333`:outpost/`op-01ac5d28a6a232904`/bucket/``amzn-s3-demo-bucket1`` \
--vpc-configuration VpcId=`vpc-1a2b3c4d5e6f7g8h9`
```

For more information about this command, see [create-access-point](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/create-access-point.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/create-access-point.html") in the _AWS CLI Reference_.

###### Example: Upload an object

The following example uploads the file
`my_image.jpg` from the user's local file
system to an object named
`images/my_image.jpg` through the access
point `example-outpost-access-point` on the
Outpost `op-01ac5d28a6a232904`, owned by the
AWS account `111122223333`. Before
using this command, replace these `user input
 placeholder` values and the AWS Region code with the
appropriate values for your use case.

```
aws s3api put-object --bucket arn:aws:s3-outposts:`us-east-1`:`111122223333`:outpost/`op-01ac5d28a6a232904`/accesspoint/`example-outpost-access-point` \
--body `my_image.jpg` --key `images/my_image.jpg`
```

For more information about this command, see [put-object](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-object.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-object.html") in the _AWS CLI Reference_.

###### Note

If this operation results in a **`Resource not found`** error
or is unresponsive, your VPC might not have a shared endpoint.

To check whether there is a shared endpoint, use the [list-shared-endpoints](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3outposts/list-shared-endpoints.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3outposts/list-shared-endpoints.html") AWS CLI command. If there is no shared
endpoint, work with the Outpost owner to create one. For more information, see
[ListSharedEndpoints](../API/API_s3outposts_ListSharedEndpoints.md "../API/API_s3outposts_ListSharedEndpoints.md") in the
_Amazon Simple Storage Service API Reference_.

###### Example: Create an endpoint

The following example creates an endpoint on a shared Outpost. Before using this
command, replace the `user input placeholder`
values for the Outpost ID, subnet ID, and security group ID with the appropriate
values for your use case.

###### Note

The user can perform this operation only if the resource share includes the
**Outposts** resource.

```
aws s3outposts create-endpoint --outposts-id `op-01ac5d28a6a232904` --subnet-id `XXXXXX` --security-group-id `XXXXXXX`
```

For more information about this command, see [create-endpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3outposts/create-endpoint.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3outposts/create-endpoint.html") in the _AWS CLI Reference_.
