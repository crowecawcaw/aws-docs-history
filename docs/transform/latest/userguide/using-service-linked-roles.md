# Using service-linked roles for AWS Transform

AWS Transform uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to AWS Transform. Service-linked roles are predefined by AWS Transform and
include all the permissions that the service requires to call other AWS services on your
behalf.

## Using service-linked roles for

AWS Transform

AWS Transform uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to AWS Transform. Service-linked roles are predefined by AWS Transform and
include all the permissions that the service requires to call other AWS services on your
behalf.

A service-linked role makes setting up AWS Transform easier because you don't have to
manually add the necessary permissions. AWS Transform defines the permissions of its
service-linked roles, and unless defined otherwise, only AWS Transform can assume its roles.
The defined permissions include the trust policy and the permissions policy, and that
permissions policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources.
This protects your AWS Transform resources because you can't inadvertently remove permission
to access the resources.

For information about other services that support service-linked roles, see [AWS services
that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-linked roles** column. Choose
a **Yes** with a link to view the service-linked role
documentation for that service.

### Service-linked role permissions for AWS Transform

AWS Transform uses the service-linked role named [AWSServiceRoleForAWSTransform](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSServiceRoleForAWSTransform "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSServiceRoleForAWSTransform")
– This Service-Linked Role provides AWS Transform with the ability to provide usage information.

The AWSServiceRoleForAWSTransform service-linked role trusts the following services to assume the
role:

- `transform.amazonaws.com`

The role permissions policy named AWSServiceRoleForAWSTransform allows AWS Transform to complete the
following actions on the specified resources:

- cloudwatch:PutMetricData
  - Send custom metrics to CloudWatch for AWS Transform operations
  - Track transformation progress, success rates, and performance metrics
  - Enable monitoring and alerting on transformation workflows

- sso:DescribeApplication
  - View details about a specific application in Identity Center
  - Get application metadata like name, description, status, and configuration

- sso:GetApplicationAssignmentConfiguration
  - Retrieve assignment configuration settings for an application
  - See how users/groups are configured to be assigned to the application

- sso:ListApplicationAssignmentsForPrincipal
  - List all applications assigned to a specific user or group (principal)
  - View which applications a particular identity has access to

- Enables decryption of KMS-encrypted data when accessed through IAM Identity Center. Only works when the encryption context contains a valid IAM Identity Center instance ARN and must be accessed via IAM Identity Center service endpoints.
- Allows decryption of KMS-encrypted data when accessed through Identity Store. Only works when the encryption context contains a valid Identity Store ARN and must be accessed via Identity Store service endpoints.

You must configure permissions to allow your users, groups, or roles to create, edit, or
delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

### Creating a service-linked role for AWS Transform

You don't need to manually create a service-linked role. When you
create a profile for AWS Transform in the AWS Management Console, AWS Transform creates the service-linked role
for you.

If you delete this service-linked role, and then need to create it again, you can use
the same process to recreate the role in your account. When you update the settings, AWS Transform
creates the service-linked role for you again.

You can also use the IAM console or AWS CLI to create a service-linked role with the
`transform.amazonaws.com` service name. For more information, see [Creating a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role") in the _IAM User Guide_. If
you delete this service-linked role, you can use this same process to create the role
again.

### Editing a service-linked role for AWS Transform

AWS Transform does not allow you to edit the AWSServiceRoleForAWSTransform service-linked role. After you
create a service-linked role, you cannot change the name of the role because various
entities might reference the role. However, you can edit the description of the role using
IAM. For more information, see [Editing a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the
_IAM User Guide_.

### Deleting a service-linked role for AWS Transform

If you no longer need to use a feature or service that requires a service-linked role,
we recommend that you delete that role. That way you don't have an unused entity that is not
actively monitored or maintained. However, you must clean up the resources for your
service-linked role before you can manually delete it.

###### Note

If the AWS Transform service is using the role when you try to delete the resources,
then the deletion might fail. If that happens, wait for a few minutes and try the
operation again.

**To manually delete the service-linked role using
IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForAWSTransform
service-linked role. For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
_IAM User Guide_.

### Supported Regions for AWS Transform service-linked

roles

AWS Transform does not support using service-linked roles in every Region where the
service is available. You can use the AWSServiceRoleForAWSTransform role in the following Regions. For more
information, see [AWS Regions and endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md").

| Region name           | Region identity | Support in AWS Transform |
| --------------------- | --------------- | ------------------------ |
| US East (N. Virginia) | us-east-1       | Yes                      |
| Europe (Frankfurt)    | eu-central-1    | Yes                      |
