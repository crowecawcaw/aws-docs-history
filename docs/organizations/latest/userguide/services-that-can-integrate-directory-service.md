# AWS Directory Service and

AWS Organizations

AWS Directory Service for Microsoft Active Directory, or AWS Managed Microsoft AD, lets you run Microsoft Active
Directory (AD) as a managed service. AWS Directory Service makes it easy to set up and run directories
in the AWS Cloud or connect your AWS resources with an existing on-premises Microsoft
Active Directory. AWS Managed Microsoft AD also integrates tightly with AWS Organizations to allow seamless
directory sharing across multiple AWS accounts and any VPC in a Region. For more
information, see the [AWS Directory Service Administration Guide](../../../directoryservice/latest/admin-guide.md "../../../directoryservice/latest/admin-guide.md").

To share an Directory Service across an organization, the organization must have **All features** enabled, and the directory must be in the organization management account.

Use the following information to help you integrate
AWS Directory Service with AWS Organizations.

## Enabling trusted access with

Directory Service

For information about the permissions needed to enable trusted access, see [Permissions required to enable trusted
access](orgs_integrate_services.md#orgs_trusted_access_perms "orgs_integrate_services.md#orgs_trusted_access_perms").

You can enable trusted access using either the AWS Directory Service console or the AWS Organizations
console.

###### Important

We strongly recommend that whenever possible, you use the AWS Directory Service console or
tools to enable integration with Organizations. This lets AWS Directory Service perform any
configuration that it requires, such as creating resources needed by the service.
Proceed with these steps only if you can’t enable integration using the tools
provided by AWS Directory Service. For more information, see [this note](orgs_integrate_services.md#important-note-about-integration "orgs_integrate_services.md#important-note-about-integration").

If you enable trusted access by using the AWS Directory Service console or tools then you
don’t need to complete these steps.

###### To enable trusted access using the Directory Service console

To share a directory, which automatically enables trusted access, see [Share
Your Directory](../../../directoryservice/latest/admin-guide/ms_ad_directory_sharing.md "../../../directoryservice/latest/admin-guide/ms_ad_directory_sharing.md") in the _AWS Directory Service Administration Guide_. For step-by-step instructions, see [Tutorial: Sharing Your AWS Managed Microsoft AD Directory](../../../directoryservice/latest/admin-guide/ms_ad_tutorial_directory_sharing.md "../../../directoryservice/latest/admin-guide/ms_ad_tutorial_directory_sharing.md").

You can enable trusted access by using the AWS Organizations console.

AWS Management Console

###### To enable trusted service access using the Organizations console

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. In the navigation pane, choose **Services**.
3. Choose **AWS Directory Service** in the list of services.
4. Choose **Enable trusted access**.
5. In the **Enable trusted access for AWS Directory Service** dialog
   box, type **enable** to confirm it, and then choose **Enable trusted
   access**.
6. If you are the administrator of only AWS Organizations, tell the
   administrator of AWS Directory Service that they can now enable that service
   to work with AWS Organizations from the service console .

## Disabling trusted access with

Directory Service

For information about the permissions needed to disable trusted
access, see [Permissions required to disable
trusted access](orgs_integrate_services.md#orgs_trusted_access_disable_perms "orgs_integrate_services.md#orgs_trusted_access_disable_perms").

If you disable trusted access using AWS Organizations while you are using Directory Service, all
previously shared directories continue to operate as normal. However, you can no longer
share new directories within the organization until you enable trusted access
again.

You can only disable trusted access using the Organizations
tools.

You can disable trusted access by using the AWS Organizations console.

AWS Management Console

###### To disable trusted service access using the Organizations console

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. In the navigation pane, choose **Services**.
3. Choose **AWS Directory Service** in the list of services.
4. Choose **Disable trusted access**.
5. In the **Disable trusted access for AWS Directory Service** dialog
   box, type **disable** to confirm, and then choose **Disable trusted
   access**.
6. If you are the administrator of only AWS Organizations, tell the
   administrator of AWS Directory Service that they can now disable that service from working with AWS Organizations
   using tthe service console or tools;.
