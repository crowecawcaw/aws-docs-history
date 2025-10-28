# Errors when trying to share with accounts

outside of my organization

## Scenario

You get one of the following errors when you try to share resources with accounts
that are outside of your organization:

- "**`You cannot share the resource outside your
organization.`**"
- "**`The resource you are attempting to share can only be shared
within your AWS Organization.`**"
- "**`InvalidParameterException: Principal Account-ID is not in your
AWS organization. You do not have permission to add external
AWS accounts to a resource share.`**"
- "**`OperationNotPermittedException: The resource you are
attempting to share can only be shared within your AWS
Organization.`**"

## Possible causes

and solutions

### Some resource types can be shared

only with accounts in the same organization

Some resource types can’t be shared with any account that isn't a member of
that organization. An example resource type with this restriction is virtual
private connections (VPCs) that are part of Amazon Elastic Compute Cloud (Amazon EC2).

To verify if you can share a particular resource type with accounts and
principals outside of your organization, see [Shareable AWS
resources](shareable.md "shareable.md").

### The service-linked role wasn't

successfully created

This issue can occur if the service-linked role
`AWSServiceRoleForResourceAccessManager` wasn't successfully
created when you turned on integration between AWS RAM and AWS Organizations.

If you receive one of these errors when attempting to share a resource with an
account that **_is_** part of your organization, perform the following
steps to delete and re-create the service-linked role.

###### Important

When you disable trusted access to AWS Organizations, principals within your organization are removed from all resource shares and
lose access to those shared resources.

1. Sign in to your the management account of your organization using an IAM role
   or user with administrative permissions.
2. Navigate to the [Services page in the AWS Organizations console](https://console.aws.amazon.com/organizations/v2/home/services "https://console.aws.amazon.com/organizations/v2/home/services").
3. Choose **RAM**.
4. Choose **Disable trusted access**.
5. Navigate to the [Settings page
   in the AWS RAM console](https://console.aws.amazon.com/ram/home#Settings: "https://console.aws.amazon.com/ram/home#Settings:").
6. Select the box **Enable sharing with AWS Organizations**, and then
   choose **Save settings**.
