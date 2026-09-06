

# Troubleshooting Resource Explorer setup and configuration issues
<a name="troubleshooting_setup"></a>

Use the information here to help you diagnose and fix issues that can occur when you initially set up or configure AWS Resource Explorer.

**Topics**
+ [Troubleshooting permission-based access issues](#troubleshoot_setup_permission-based-access)
+ [I get an "access denied" message when I make a request to Resource Explorer](#troubleshoot_setup_access-denied)
+ [I get an "access denied" message when I make a request with temporary security credentials](#troubleshooting_setup_access-denied-temp-creds)

## Troubleshooting permission-based access issues
<a name="troubleshoot_setup_permission-based-access"></a>

Resource Explorer provides different user experiences based on your IAM permissions. Use this section to troubleshoot issues related to permission-based access and search results.

### I'm getting partial search results instead of complete results
<a name="troubleshoot_partial_vs_full_results"></a>

If you're receiving partial search results, this indicates you have, at minimum, the permissions in the `[AWSResourceExplorerReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSResourceExplorerReadOnlyAccess.html)` managed policy but lack `iam:CreateServiceLinkedRole` permission (included in the [AWSResourceExplorerFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSResourceExplorerFullAccess.html) managed policy), or the service-linked role hasn't been created in your account yet.
+ **To get complete results:** Obtain `iam:CreateServiceLinkedRole` permission (included in the [AWSResourceExplorerFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSResourceExplorerFullAccess.html) managed policy) from your administrator, or sign in with a role that has this permission. Once you initiate a search with both permissions, Resource Explorer will automatically create the service-linked role and provide complete results.
+ **If the service-linked role already exists:** Verify you have, at minimum, the permissions in the `[AWSResourceExplorerReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSResourceExplorerReadOnlyAccess.html)` managed policy. Users with search permission get complete results after searching in a Region once the service-linked role exists in the account.
**Note**  
Automatic setup may not happen in this case if an index was previously deleted or the aggregator index already exists 
+ **Regional differences:** Results may vary by Region based on index types. Regions with user-owned indexes provide complete results, while Regions with only Resource Explorer-owned indexes provide partial results.

### Service-linked role creation issues
<a name="troubleshoot_slr_creation"></a>

If you receive an error when Resource Explorer attempts to create the service-linked role during your first search, this indicates you lack the `iam:CreateServiceLinkedRole` permission (included in the [AWSResourceExplorerFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSResourceExplorerFullAccess.html) managed policy).
+ **Resolution:** Get permission from your administrator OR sign in with a role that has the `iam:CreateServiceLinkedRole` permission.
**Note**  
**Note:** The service-linked role only needs to be created once per account. After it's created by any user with the appropriate permission, all users with, at minimum, the permissions in the `[AWSResourceExplorerReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSResourceExplorerReadOnlyAccess.html)` managed policy are able to create an index and view for full results in a Region on first search.

### I can't access Resource Explorer search functionality
<a name="troubleshoot_no_search_access"></a>

If you receive access denied errors when trying to use Resource Explorer search, you lack at minimum the permissions in the `[AWSResourceExplorerReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSResourceExplorerReadOnlyAccess.html)` managed policy.
+ **Resolution:** Contact your administrator to obtain the permissions in the `[AWSResourceExplorerReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSResourceExplorerReadOnlyAccess.html)` managed policy. These permissions are also a subset of the `ResourceExplorerFullAccess` managed policy
+ **Organizational control:** If your organization wants to prevent access to Resource Explorer search functionality, administrators can disallow the permissions in the `[AWSResourceExplorerReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSResourceExplorerReadOnlyAccess.html)` managed policy.

### Indexing progress and completion issues
<a name="troubleshoot_indexing_progress"></a>

When Resource Explorer automatically creates indexes and views, you may see indexing progress indicators in the console.
+ **Blue banner "Completing Resource Explorer setup":** This indicates indexing is in progress. You can search immediately and receive partial results while indexing completes in the background.
+ **Green completion banner:** This indicates that the user-index is setup. Refresh to view full results.
+ **Timeline expectations:** Initial indexing typically completes within a few hours, depending on the number of resources in your account. You can use Resource Explorer immediately while indexing continues.
+ **If indexing appears stuck:** Indexing runs automatically in the background. If you don't see progress after several hours, verify your permissions and try refreshing the console.

## I get an "access denied" message when I make a request to Resource Explorer
<a name="troubleshoot_setup_access-denied"></a>

Access denied errors can occur when accessing Resource Explorer search functionality or when trying to configure enhanced features like custom views or cross-Region search.
+ **For basic search access:** Verify you have, at minimum, the permissions in the `[AWSResourceExplorerReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSResourceExplorerReadOnlyAccess.html)` managed policy. This permission provides immediate access to search functionality.
+ **For complete search results:** Verify you have both the permissions in the `[AWSResourceExplorerReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSResourceExplorerReadOnlyAccess.html)` managed policy and the `iam:CreateServiceLinkedRole` permission (included in the [AWSResourceExplorerFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSResourceExplorerFullAccess.html) managed policy), or that the service-linked role already exists in your account.
+ **For enhanced features:** Verify that you have permissions to call the action and resource that you requested. An administrator can grant permissions by assigning an AWS Identity and Access Management (IAM) permission policy to your IAM principal, such as a role, group, or user.

  To provide access, add permissions to your users, groups, or roles:
  + Users and groups in AWS IAM Identity Center:

    Create a permission set. Follow the instructions in [Create a permission set](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) in the *AWS IAM Identity Center User Guide*.
  + Users managed in IAM through an identity provider:

    Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp.html) in the *IAM User Guide*.
  + IAM users:
    + Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html) in the *IAM User Guide*.
    + (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-add-console) in the *IAM User Guide*.

  The policy must allow the requested `Action` on the `Resource` that you want to access.

  If the policy statements that grant those permissions include any conditions, such as time-of-day or IP address restrictions, you also must meet those requirements when you send the request. For information about viewing or modifying policies for an IAM principal, see [Managing IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage.html) in the *IAM User Guide*.
+ If you're signing API requests manually (without using the [AWS SDKs](http://aws.amazon.com/tools/)), verify that you [signed the request](https://docs.aws.amazon.com/general/latest/gr/signing_aws_api_requests.html) correctly.

## I get an "access denied" message when I make a request with temporary security credentials
<a name="troubleshooting_setup_access-denied-temp-creds"></a>
+ Verify that the IAM principal that you're using to make the request has the correct permissions. Permissions for temporary security credentials are derived from a principal defined in IAM, so the permissions are limited to those granted to the principal. For more information about how permissions for temporary security credentials are determined, see [Controlling permissions for temporary security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access.html) in the *IAM User Guide*.
+ Verify that your requests are being signed correctly and that the request is well formed. For details, see the [toolkit](http://aws.amazon.com/tools/) documentation for your chosen SDK or [Using temporary credentials with AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html) in the *IAM User Guide*.
+ Verify that your temporary security credentials haven't expired. For more information, see [Requesting temporary security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html) in the *IAM User Guide*. 