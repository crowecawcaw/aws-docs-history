

# Using service-linked roles for Billing Conductor
<a name="using-service-linked-roles"></a>

AWS Billing Conductor uses AWS Identity and Access Management (IAM) [service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role). A service-linked role is a unique type of IAM role that is linked directly to Billing Conductor. Service-linked roles are predefined by Billing Conductor and include all the permissions that the service requires to call other AWS services on your behalf.

A service-linked role makes setting up Billing Conductor easier because you don’t have to manually add the necessary permissions. Billing Conductor defines the permissions of its service-linked roles, and unless defined otherwise, only Billing Conductor can assume its roles. The defined permissions include the trust policy and the permissions policy, and that permissions policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources. This protects your Billing Conductor resources because you can't inadvertently remove permission to access the resources.

For information about other services that support service-linked roles, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) and look for the services that have **Yes** in the **Service-linked roles** column. Choose a **Yes** with a link to view the service-linked role documentation for that service.

## Service-linked role permissions for Billing Conductor
<a name="service-linked-role-permissions"></a>

Billing Conductor uses the service-linked role named **AWSServiceRoleForBillingConductor** – this role allows Billing Conductor to create and manage billing groups in your account on your behalf.

The AWSServiceRoleForBillingConductor service-linked role trusts the following services to assume the role:
+ `billingconductor.amazonaws.com`

The role permissions policy named `AWSBillingConductorRolePolicy` allows Billing Conductor to complete the following actions on the specified resources:
+ Action: `billingconductor:CreateBillingGroup` on billing group and pricing plan resources
+ Action: `billingconductor:GetBillingTransferPreference` on all AWS resources
+ Action: `organizations:DescribeResponsibilityTransfer` on all AWS resources

For the full policy document, including the JSON, see [AWSBillingConductorRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBillingConductorRolePolicy.html) in the *AWS Managed Policy Reference Guide*.

You must configure permissions to allow your users, groups, or roles to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the *IAM User Guide*.

## Creating a service-linked role for Billing Conductor
<a name="create-service-linked-role"></a>

You don't need to manually create a service-linked role. When you enable the automatic billing group creation preference for a billing transfer, Billing Conductor creates the service-linked role for you.

## Editing a service-linked role for Billing Conductor
<a name="edit-service-linked-role"></a>

Billing Conductor does not allow you to edit the AWSServiceRoleForBillingConductor service-linked role. After you create a service-linked role, you cannot change the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see [Editing a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role) in the *IAM User Guide*.

## Deleting a service-linked role for Billing Conductor
<a name="delete-service-linked-role"></a>

If you no longer need to use a feature or service that requires a service-linked role, we recommend that you delete that role. That way you don’t have an unused entity that is not actively monitored or maintained. However, you must clean up your service-linked role before you can manually delete it.

### Clean up the service-linked role
<a name="slr-cleanup"></a>

Before you can delete the AWSServiceRoleForBillingConductor service-linked role, you must disable every automatic billing group creation preference that references it. While any enabled preference references the role, Billing Conductor reports the role as in use and the deletion is blocked.

### Manually delete the service-linked role
<a name="slr-manual-delete"></a>

After you disable the referencing preferences, use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForBillingConductor service-linked role. For more information, see [Deleting a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role) in the *IAM User Guide*.

## Supported Regions for Billing Conductor service-linked roles
<a name="slr-regions"></a>

Billing Conductor supports using service-linked roles in all of the Regions where the service is available. For more information, see [AWS Regions and endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html).