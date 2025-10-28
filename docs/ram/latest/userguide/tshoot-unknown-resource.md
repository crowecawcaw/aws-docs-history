# Error: "UnknownResourceException"

## Scenario

You get one of the following errors:

- "**`CannotCreateResourceShare: UnknownResourceException:
OrganizationalUnit ou-`xxxx` could not be
found`**"
- "**`CannotUpdateResourceShare: UnknownResourceException:
OrganizationalUnit ou-`xxxx` could not be
found`**".

## Cause

These errors can occur if you enable integration between AWS RAM and AWS Organizations by
using either the [Organizations console or
the Organizations EnableAWSServiceAccess API](../../../organizations/latest/userguide/orgs_integrate_services.md "../../../organizations/latest/userguide/orgs_integrate_services.md") instead of by [using the AWS RAM console](getting-started-sharing.md#getting-started-sharing-orgs "getting-started-sharing.md#getting-started-sharing-orgs"). When you
enable integration by using the Organizations console or API, the service doesn’t create the
`AWSServiceRoleForResourceAccessManager` role in your account. That
role is needed to access information about your organization. Because the role
wasn't created, AWS RAM can’t access details about the accounts or organizational
units (OUs) in your organization.

## Solution

To resolve the issue, turn off integration between AWS RAM and AWS Organizations. Then turn
it on again by calling the AWS RAM [EnableSharingWithAwsOrganization](../APIReference/API_EnableSharingWithAwsOrganization.md "../APIReference/API_EnableSharingWithAwsOrganization.md") API operation, or by using the
AWS Management Console to perform the following steps.

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

You should now be able to use AWS RAM to share your resources with accounts and OUs
in the organization.
