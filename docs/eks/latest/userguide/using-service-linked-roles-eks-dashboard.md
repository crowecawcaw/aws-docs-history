**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Using roles for Amazon EKS Dashboard

The Amazon EKS Dashboard uses this service-linked role to aggregate information about cluster resources from multiple regions and accounts. The dashboard integrates with AWS Organizations to securely read information about multiple accounts in your organization.

To learn more about the Amazon EKS Dashboard, see [View aggregated data about cluster resources with the EKS Dashboard](cluster-dashboard.md "cluster-dashboard.md").

## Background

Amazon EKS uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is linked directly to Amazon EKS. Service-linked roles are predefined by Amazon EKS and include all the permissions that the service requires to call other AWS services on your behalf.

A service-linked role makes setting up Amazon EKS easier because you don’t have to manually add the necessary permissions. Amazon EKS defines the permissions of its service-linked roles, and unless defined otherwise, only Amazon EKS can assume its roles. The defined permissions include the trust policy and the permissions policy, and that permissions policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources. This protects your Amazon EKS resources because you can’t inadvertently remove permission to access the resources.

For information about other services that support service-linked roles, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-linked role** column. Choose a **Yes** with a link to view the service-linked role documentation for that service.

## Service-linked role permissions for Amazon EKS

Amazon EKS uses the service-linked role named `AWSServiceRoleForAmazonEKSDashboard`. The role allows Amazon EKS to generate and display the EKS Dashboard, including aggregated information about cluster resources. The attached `AmazonEKSDashboardServiceRolePolicy` policy allows the role to manage the following resources: Auto Scaling groups, security groups, launch templates, and IAM instance profiles. For more information, see [AWS managed policy: AmazonEKSDashboardServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonEKSDashboardServiceRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonEKSDashboardServiceRolePolicy").

The `AWSServiceRoleForAmazonEKSDashboard` service-linked role trusts the following services to assume the role:

- `dashboard.eks.amazonaws.com`

To view the latest version of the JSON policy document, see [AmazonEKSDashboardServiceRolePolicy](../../../aws-managed-policy/latest/reference/AmazonEKSDashboardServiceRolePolicy.md#AmazonEKSDashboardServiceRolePolicy-json "../../../aws-managed-policy/latest/reference/AmazonEKSDashboardServiceRolePolicy.md#AmazonEKSDashboardServiceRolePolicy-json") in the AWS Managed Policy Reference Guide.

You must configure permissions to allow an IAM entity (such as a user, group, or role) to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the _IAM User Guide_.

## Creating a service-linked role for Amazon EKS

You don’t need to manually create a service-linked role. When you enable the dashboard in the AWS console, Amazon EKS creates the service-linked role for you.

For more information about enabling the EKS Dashboard, see [Configure EKS Dashboard integration with AWS Organizations](cluster-dashboard-orgs.md "cluster-dashboard-orgs.md").

###### Important

This service-linked role can appear in your account if you completed an action in another service that uses the features supported by this role.

## Editing a service-linked role for Amazon EKS

Amazon EKS does not allow you to edit the `AWSServiceRoleForAmazonEKSDashboard` service-linked role. After you create a service-linked role, you cannot change the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see [Editing a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Deleting a service-linked role for Amazon EKS

If you no longer need to use a feature or service that requires a service-linked role, we recommend that you delete that role. That way you don’t have an unused entity that is not actively monitored or maintained. However, you must clean up your service-linked role before you can manually delete it.

### Cleaning up a service-linked role

Before you can use IAM to delete a service-linked role, you must first delete any resources used by the role.

###### Note

If the Amazon EKS service is using the role when you try to delete the resources, then the deletion might fail. If that happens, wait for a few minutes and try the operation again.

For more information about disabling the EKS Dashboard, see [Configure EKS Dashboard integration with AWS Organizations](cluster-dashboard-orgs.md "cluster-dashboard-orgs.md").

### Manually delete the service-linked role

Use the IAM console, the AWS CLI, or the AWS API to delete the `AWSServiceRoleForAmazonEKSDashboard` service-linked role. For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.

## Supported regions for Amazon EKS service-linked roles

Amazon EKS supports using service-linked roles in all of the regions where the service is available. For more information, see [Amazon EKS endpoints and quotas](../../../general/latest/gr/eks.md "../../../general/latest/gr/eks.md").
