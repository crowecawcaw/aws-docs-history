# Error: "Your account ID does not exist in an AWS

organization"

## Scenario

You get the error "**`Your account ID does not exist in an AWS
 organization`**" when trying to share a resource with accounts or
organizational units (OUs) in your organization.

## Cause

This error can happen if the service-linked role [AWSServiceRoleForResourceAccessManager](https://console.aws.amazon.com/iam/home#/roles/AWSServiceRoleForResourceAccessManager "https://console.aws.amazon.com/iam/home#/roles/AWSServiceRoleForResourceAccessManager") isn't successfully created when
you turn on integration between AWS Resource Access Manager and AWS Organizations.

## Solution

To re-create the required service-linked role, perform the following steps to turn
off integration and then turn it on again.

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
