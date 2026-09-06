

# Using service-linked roles for AWS Data Exchange
<a name="using-service-linked-roles-adx"></a>

AWS Data Exchange uses AWS Identity and Access Management (IAM) [service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role). A service-linked role is a unique type of IAM role that is linked directly to AWS Data Exchange. Service-linked roles are predefined by AWS Data Exchange and include all the permissions that the service requires to call other AWS services on your behalf.

A service-linked role makes setting up AWS Data Exchange easier because you don’t have to manually add the necessary permissions. AWS Data Exchange defines the permissions of its service-linked roles, and unless defined otherwise, only AWS Data Exchange can assume its roles. The defined permissions include the trust policy and the permissions policy, and that permissions policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources. This protects your AWS Data Exchange resources because you can't inadvertently remove permission to access the resources.

For information about other services that support service-linked roles, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) and look for the services that have **Yes** in the **Service-linked roles** column. Choose a **Yes** with a link to view the service-linked role documentation for that service.

## Creating a service-linked role for AWS Data Exchange
<a name="create-service-linked-role-license-management"></a>

You don't need to manually create a service-linked role. When you distribute a data grant using license manager, it creates the service-linked role for you. 

**To create a service-linked role**

1. In the [AWS Data Exchange console](https://console.aws.amazon.com/adx/), sign in and choose **Data Grant settings**.

1. On the **Data Grant settings** page, choose **Configure integration**.

1. In the **Create AWS Organizations integration** section, select **Configure integration**.

1. On the **Create AWS Organizations integration** page, choose the appropriate trust level preference, and then choose **Create integration**.

You can also use the IAM console to create a service-linked role with a use case. In the AWS CLI or the AWS API, create a service-linked role with the `{{appropriate-service-name}}.amazonaws.com` service name. For more information, see [Creating a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#create-service-linked-role) in the *IAM User Guide*. If you delete this service-linked role, you can use this same process to create the role again.

## Editing a service-linked role for AWS Data Exchange
<a name="edit-service-linked-role-license-management"></a>

AWS Data Exchange does not allow you to edit the service-linked role. After you create a service-linked role, you cannot change the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see [Editing a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role) in the *IAM User Guide*.

## Deleting a service-linked role for AWS Data Exchange
<a name="delete-service-linked-role-license-management"></a>

If you no longer need to use a feature or service that requires a service-linked role, we recommend that you delete that role. That way you don’t have an unused entity that is not actively monitored or maintained. However, you must clean up the resources for your service-linked role before you can manually delete it.

**Note**  
If the AWS Data Exchange service is using the role when you try to delete the resources, then the deletion might fail. If that happens, wait for a few minutes and try the operation again.

Before you can delete the service-linked role, you must:
+ For the `AWSServiceRoleForAWSDataExchangeLicenseManagement` role, remove all AWS License Manager distributed grants for AWS Data Exchange data grants you received.
+ For the `AWSServiceRoleForAWSDataExchangeOrganizationDiscovery` role, remove all AWS License Manager distributed grants for AWS Data Exchange data grants received by accounts in your AWS organization.

**Manually deleting the service-linked role**

Use the IAM console, the AWS CLI, or the AWS API to delete the service-linked role. For more information, see [Deleting a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role) in the *IAM User Guide*.

## Supported Regions for AWS Data Exchange service-linked roles
<a name="slr-regions-adx"></a>

AWS Data Exchange supports using service-linked roles in all of the AWS Regions where the service is available. For more information, see [AWS Regions and endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html).