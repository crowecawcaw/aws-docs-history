

# Use service-linked roles for Reachability Analyzer
<a name="using-service-linked-roles"></a>

Reachability Analyzer uses AWS Identity and Access Management (IAM)[ service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html#id_roles_terms-and-concepts) for multi-account analysis. A service-linked role is a unique type of IAM role that is linked directly to Reachability Analyzer. Service-linked roles are predefined by Reachability Analyzer and include all the permissions that the service requires to call other AWS services on your behalf. 

A service-linked role makes setting up Reachability Analyzer easier because you don't have to add the necessary permissions yourself. Reachability Analyzer defines the permissions of its service-linked roles, and unless defined otherwise, only Reachability Analyzer can assume its roles. The defined permissions include the trust policy and the permissions policy, and that permissions policy cannot be attached to any other IAM entity.

## Service-linked role permissions for Reachability Analyzer
<a name="slr-permissions"></a>

Reachability Analyzer uses the service-linked role named **AWSServiceRoleForReachabilityAnalyzer** to access AWS resources and integrate with AWS Organizations on your behalf.

The **AWSServiceRoleForReachabilityAnalyzer** role trusts the following services to assume the role:
+ `reachabilityanalyzer.networkinsights.amazonaws.com`

The **AWSServiceRoleForReachabilityAnalyzer** service-linked role uses the managed policy [AWSReachabilityAnalyzerServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSReachabilityAnalyzerServiceRolePolicy.html).

You must configure permissions to allow an IAM entity (such as a user, group, or role) to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create-service-linked-role.html#service-linked-role-permissions) in the *IAM User Guide*.

## Create a service-linked role for Reachability Analyzer
<a name="create-slr"></a>

You don't need to create this service-linked role yourself. When you enable integration with AWS Organizations, Reachability Analyzer creates the **AWSServiceRoleForReachabilityAnalyzer** role for you. For more information, see [Enable trusted access in Reachability Analyzer](enable-trusted-access.md).

If you delete this service-linked role and then enable integration with AWS Organizations, Reachability Analyzer creates the **AWSServiceRoleForReachabilityAnalyzer** role for you again.

## Edit a service-linked role for Reachability Analyzer
<a name="edit-slr"></a>

Reachability Analyzer does not allow you to edit the **AWSServiceRoleForReachabilityAnalyzer** role. After you create a service-linked role, you cannot change the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see [Editing a service-linked role description](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_update-service-linked-role.html#edit-service-linked-role-iam-console) in the *IAM User Guide*.

## Delete a service-linked role for Reachability Analyzer
<a name="delete-slr"></a>

If you are finished performing multi-account analysis, we recommend that you delete the **AWSServiceRoleForReachabilityAnalyzer** role. You can delete this service-linked role only after you disable the integration of Reachability Analyzer with AWS Organizations.

If the Reachability Analyzer service is using the role when you try to delete the resources, then the deletion might fail. If that happens, wait for a few minutes and try the operation again.

**To disable integration with AWS Organizations**  
Make sure that you are not running a path analysis. To disable integration using the Reachability Analyzer console, see [Disable trusted access in Reachability Analyzer](disable-trusted-access.md). To disable integration using the AWS CLI or an API, see [How to enable or disabled trusted access](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html#orgs_how-to-enable-disable-trusted-access) in the *AWS Organizations User Guide*.

**To delete the service-linked role using IAM**  
Use IAM to delete the **AWSServiceRoleForReachabilityAnalyzer** role. For more information, see [Deleting a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_delete.html#id_roles_manage_delete_slr) in the *IAM User Guide*.