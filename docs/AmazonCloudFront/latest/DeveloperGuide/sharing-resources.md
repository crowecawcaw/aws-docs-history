# Working with shared resources in CloudFront

Amazon CloudFront integrates with AWS Resource Access Manager (AWS RAM) to enable resource sharing. AWS RAM enables
you to share some CloudFront resources with other AWS accounts or through AWS Organizations. With
AWS RAM, you share resources that you own by creating a _resource share_. A
resource share specifies the resources to share, and the consumers with whom to share them.
Consumers can include:

- Specific AWS accounts inside or outside of its organization in AWS Organizations
- An organizational unit inside its organization in AWS Organizations
- Its entire organization in AWS Organizations
  For more information about AWS RAM, see the [AWS RAM User Guide](../../../ram/latest/userguide.md "../../../ram/latest/userguide.md").

This topic explains how to share resources that you own, and how to use resources that are
shared with you.

###### Contents

- [Prerequisites for sharing resources](#sharing-prereqs "#sharing-prereqs")
- [Sharing a VPC origin](#sharing-share "#sharing-share")
- [Using a shared VPC origin](#using-shared-vpc-origin "#using-shared-vpc-origin")
- [Identifying a shared VPC origin](#sharing-identify "#sharing-identify")
- [Unsharing a shared VPC origin](#sharing-unshare "#sharing-unshare")
- [Responsibilities and permissions for shared
  VPC origins](#sharing-perms "#sharing-perms")
- [Billing and metering](#sharing-billing "#sharing-billing")
- [Shared resource quotas](#sharing-quotas "#sharing-quotas")

## Prerequisites for sharing resources

- You must have the AWSRAMDefaultPermissionCloudFront managed
  policy to grant read-only access the resource share. For more information, see
  [AWSRAMDefaultPermissionCloudFront](#aws-ram-default-permission-cloudfront "#aws-ram-default-permission-cloudfront").
- To share a VPC origin, you must own it in your AWS account. This means that
  the resource must be allocated or provisioned in your account. You can't share a
  resource that has been shared with you.
- To share a resource with your organization or an organizational unit in
  AWS Organizations, you must enable sharing with AWS Organizations. For more information, see
  [Enable Sharing with AWS Organizations](../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs "../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs") in the
  _AWS RAM User Guide_.

## Sharing a VPC origin

###### Note

Currently, CloudFront supports sharing VPC origins. If you haven't created one already,
see [Restrict access with VPC origins](private-content-vpc-origins.md "private-content-vpc-origins.md").

When you share a VPC origin that you own with other AWS accounts, you enable them to
use that resource as the origin for their CloudFront distributions.

To share a VPC origin, you must add it to a resource share. A resource share is an
AWS RAM resource that lets you share your resources across AWS accounts.

A resource share specifies the following:

- The resources that you want to share
- The consumers with whom they are shared with
- The service’s managed policy that determines the permissions to the
  resources

When you share a VPC origin using the CloudFront console, you add it to an existing
resource share. If you don't have a resource share already you can create one when
you're sharing a VPC origin from the CloudFront console. You can also use the [AWS RAM console](https://console.aws.amazon.com/ram "https://console.aws.amazon.com/ram") or AWS CLI to create one
separately.

You can share VPC origins with other AWS accounts and AWS Organizations.

- If you’re sharing the resource with an AWS organization, all consumers in
  that specific organization are allowed access to the VPC origin.
- If you’re sharing with an AWS account or an organization that you’re not
  part of, the consumers will receive an invitation to accept the resource share.
  Once accepted, they can use the VPC origin.

You can share a VPC origin that you own using the CloudFront console, the AWS RAM console, or
the AWS CLI.

###### To create a resource share by using the CloudFront console

1. Open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. In the navigation pane, choose **VPC origins**.
3. Select one or more resources and choose **Share VPC
   origin**.
4. Choose **Create resource share**.
5. For **Name**, enter a name for the resource share.
6. For **Principal type**, select one of the following
   options:
   - **AWS account** – Grant access to a specific
     AWS account.
   - **Organizational unit** – Grant access to a
     specific organizational unit (OU).
   - **Organization** – Grant access to your entire
     organization, including its child OUs and AWS accounts.
   1. If you chose **AWS account**, enter the account ID
      number. You can choose **Add new account** to add up to
      5 AWS accounts.
   2. If you chose **Organizational unit**, enter the OU
      unit ARN. You can enter only 1 OU.
   3. If you chose **Organization**, enter the organization
      ARN. You can enter only 1 organization.

7. Choose **Share resources**.

By default, CloudFront applies the [AWSRAMDefaultPermissionCloudFront](#aws-ram-default-permission-cloudfront "#aws-ram-default-permission-cloudfront") AWS managed policy on
the resource share. This policy allows read-only actions on the resource share,
so that consuming accounts can't update or delete the shared resource. You can't
edit or remove this policy from the resource share.

###### Tip

After you create the resource share, you can add additional AWS accounts
from the AWS RAM console. For more information, see [Update a resource share in AWS RAM](../../../ram/latest/userguide/working-with-sharing-update.md "../../../ram/latest/userguide/working-with-sharing-update.md") in the _AWS RAM
User Guide_.

###### To share a VPC origin that you own using the CloudFront console

1. Open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. In the navigation pane, choose **VPC origins**.
3. Select a resource and choose **Share VPC origin**.
4. On the **Share VPC origin** page, you can select an existing
   resource share that you want to add this VPC origin to.
5. Choose **Share resource**.

On the resource detail page, under **Shared with**, you can
see that your VPC origin is shared with the following details:

    * Resource share names
    * Share status
    * Last modified date

After you create and share the resource share with the consuming accounts, they have
12 hours to accept the invitation. For more information, see [Accepting and
rejecting resource share invitations](../../../ram/latest/userguide/working-with-shared-invitations.md "../../../ram/latest/userguide/working-with-shared-invitations.md") in the _AWS RAM User
Guide_.

###### Important

To enable consuming accounts to use your VPC origin for their CloudFront distribution,
you must also give them the VPC origin's Elastic Load Balancing or Amazon EC2 endpoint.

###### To share a VPC origin that you own using the AWS RAM console

Create a resource share and then choose the CloudFront resources that you want to add to
it. For more information, see [Creating
a Resource Share](../../../ram/latest/userguide/working-with-sharing.md#working-with-sharing-create "../../../ram/latest/userguide/working-with-sharing.md#working-with-sharing-create") in the _AWS RAM User Guide_.

###### To share a VPC origin that you own using the AWS CLI

Use the [create-resource-share](../../../cli/latest/reference/ram/create-resource-share.md "../../../cli/latest/reference/ram/create-resource-share.md") command.

## Using a shared VPC origin

To use a shared VPC origin, the account that receives the invitation must accept the
resource share. You can do that by navigating to the AWS Resource Access Manager console in the
US East (N. Virginia) Region and accepting any pending requests in the
**Pending** tab. For more information, see [Accepting shared resources](../../../ram/latest/userguide/working-with-shared-invitations.md "../../../ram/latest/userguide/working-with-shared-invitations.md") in the _AWS RAM User Guide_.

After you accept the resource share, you can then use the VPC origin as the origin for
your CloudFront distributions.

###### To use a shared VPC origin

1. Open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. On the navigation pane, for **Distributions**, do one of the
   following:
   - For a new distribution, choose **Create
     distribution**.
   - For an existing distribution, choose the distribution ID.

3. For the **Origin type**, choose **VPC
   origin**, and then specify the VPC origin that was shared with
   you.
4. For **VPC origin endpoint**, enter the private DNS name of
   your Amazon EC2 instance or Elastic Load Balancing load balancer, or the origin domain. If you don’t
   already have this value, you must get it from the AWS account that owns the
   VPC origin. If you don’t already have this endpoint, you can get it from the
   AWS account that owns the VPC origin.
5. Follow the rest of the console steps to create or update your distribution.

## Identifying a shared VPC origin

Owners and consumers can identify shared VPC origins using the CloudFront console and
AWS CLI.

###### To identify a shared VPC origin using the CloudFront console

1. Open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. In the navigation pane, choose **VPC origins**. You can use
   the **Owner ID** column to identify the AWS account that the
   resource belongs to.
3. Select a resource.
4. On the resource detail page, under **Shared with**, you can
   see that your VPC origin is shared with the following details:
   - Resource share names
   - Share status
   - Last modified date

## Unsharing a shared VPC origin

When you unshare a resource, the AWS accounts (consuming accounts) can no longer use
that resource for new distributions or update existing distributions.

###### Note

If you unshare a resource, existing distributions that are still using that
resource remain active and will continue to serve traffic. However, these
distributions can't be edited until the unshared resource is removed as the origin.
We recommend that you ensure that any consuming accounts stop using the unshared
resource before you unshare it.

To unshare a shared VPC origin that you own, you must remove it from the resource
share. You can do this using the CloudFront console, AWS RAM console, or the AWS CLI.

###### To unshare a shared VPC origin that you own using the CloudFront console

1. Open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. In the navigation pane, choose **VPC origins**.
3. Select a resource and choose **Unshare**.
4. Review the details in the **Unshare resource** dialog box and
   then choose **Unshare**. The principals listed will no longer
   have access to your shared resource.

###### To unshare a shared VPC origin that you own using the AWS RAM console

See [Updating a Resource Share](../../../ram/latest/userguide/working-with-sharing.md#working-with-sharing-update "../../../ram/latest/userguide/working-with-sharing.md#working-with-sharing-update") in the _AWS RAM User Guide_.

###### To unshare a shared VPC origin that you own using the AWS CLI

Use the [disassociate-resource-share](../../../cli/latest/reference/ram/disassociate-resource-share.md "../../../cli/latest/reference/ram/disassociate-resource-share.md") command.

## Responsibilities and permissions for shared

VPC origins

### Permissions for owners

As the resource-owning account, ensure that any consuming accounts stop using the
resource before you unshare or delete it.

### Permissions for consumers

Consuming accounts can use shared resources as origins for their CloudFront
distributions, but they can't edit or delete the resources. By default, the [AWSRAMDefaultPermissionCloudFront](#aws-ram-default-permission-cloudfront "#aws-ram-default-permission-cloudfront") AWS managed policy is
applied to the resource share in the sharing account (the account that owns the
resource).

### AWSRAMDefaultPermissionCloudFront

When you create a resource share in CloudFront, CloudFront uses the **AWSRAMDefaultPermissionCloudFront** AWS managed policy and applies
it to your resource share. This policy grants read-only permissions to CloudFront
resources that can be shared from the resource owner to the consuming account.

For more information about managing permissions in AWS RAM, see [Managing permissions in AWS RAM](../../../ram/latest/userguide/security-ram-permissions.md "../../../ram/latest/userguide/security-ram-permissions.md") in the _AWS Resource Access Manager User
Guide_.

## Billing and metering

There are no extra charges for sharing VPC origins with other AWS accounts. The
usage costs of traffic for a distribution that is using a shared VPC origin will go to
the consuming account that owns the distribution.

## Shared resource quotas

CloudFront uses the same resource share quotas as specified by AWS RAM. From the CloudFront console,
you can add up to 5 AWS accounts, 1 OU, or 1 organization. To add more, use the AWS RAM
console or AWS RAM API.

For more information, see [Service quotas for AWS RAM](../../../ram/latest/userguide/service-quotas.md "../../../ram/latest/userguide/service-quotas.md") in
the _AWS RAM User Guide_.
