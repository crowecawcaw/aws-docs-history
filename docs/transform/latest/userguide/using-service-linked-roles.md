

# Using service-linked roles for AWS Transform
<a name="using-service-linked-roles"></a>

AWS Transform uses AWS Identity and Access Management (IAM) [ service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role). A service-linked role is a unique type of IAM role that is linked directly to AWS Transform. Service-linked roles are predefined by AWS Transform and include all the permissions that the service requires to call other AWS services on your behalf.

## Using service-linked roles for AWS Transform
<a name="using-service-linked-roles-qdev"></a>

AWS Transform uses AWS Identity and Access Management (IAM) [service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role). A service-linked role is a unique type of IAM role that is linked directly to AWS Transform. Service-linked roles are predefined by AWS Transform and include all the permissions that the service requires to call other AWS services on your behalf. 

A service-linked role makes setting up AWS Transform easier because you don't have to manually add the necessary permissions. AWS Transform defines the permissions of its service-linked roles, and unless defined otherwise, only AWS Transform can assume its roles. The defined permissions include the trust policy and the permissions policy, and that permissions policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources. This protects your AWS Transform resources because you can't inadvertently remove permission to access the resources.

For information about other services that support service-linked roles, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) and look for the services that have **Yes** in the **Service-linked roles** column. Choose a **Yes** with a link to view the service-linked role documentation for that service.

### Service-linked role permissions for AWS Transform
<a name="slr-permissions"></a>

AWS Transform uses the service-linked role named [AWSServiceRoleForAWSTransform](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSServiceRoleForAWSTransform) – This Service-Linked Role provides AWS Transform with the ability to provide usage information.

The AWSServiceRoleForAWSTransform service-linked role trusts the following services to assume the role:
+ `transform.amazonaws.com`

The role permissions policy named AWSServiceRoleForAWSTransform allows AWS Transform to complete the following actions on the specified resources:
+ cloudwatch:PutMetricData
  + Send custom metrics to CloudWatch for AWS Transform operations
  + Track transformation progress, success rates, and performance metrics
  + Enable monitoring and alerting on transformation workflows
+ sso:DescribeApplication
  + View details about a specific application in Identity Center
  + Get application metadata like name, description, status, and configuration
+ sso:GetApplicationAssignmentConfiguration
  + Retrieve assignment configuration settings for an application
  + See how users/groups are configured to be assigned to the application
+ sso:ListApplicationAssignmentsForPrincipal
  + List all applications assigned to a specific user or group (principal)
  + View which applications a particular identity has access to
+ Enables decryption of KMS-encrypted data when accessed through IAM Identity Center. Only works when the encryption context contains a valid IAM Identity Center instance ARN and must be accessed via IAM Identity Center service endpoints.
+ Allows decryption of KMS-encrypted data when accessed through Identity Store. Only works when the encryption context contains a valid Identity Store ARN and must be accessed via Identity Store service endpoints.
+ secretsmanager:GetSecretValue
  + Access AWS Transform service-linked secrets used to store client secrets for external identity providers
  + Resource: arn:aws:secretsmanager:\*:\*:secret:transform-preprod\!\*
  + Condition: Must be owned by transform-preprod service and accessed from same account
+ support:CreateCase, support:DescribeCases, support:DescribeCommunications, support:AddCommunicationToCase, support:ResolveCase
  + Create and manage premium support cases from the AWS Transform web application
  + View case details and communications
  + Add communications and resolve support cases

You must configure permissions to allow your users, groups, or roles to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the *IAM User Guide*.

### Creating a service-linked role for AWS Transform
<a name="create-slr"></a>

You don't need to manually create a service-linked role. When you create a profile for AWS Transform in the AWS Management Console, AWS Transform creates the service-linked role for you. 

If you delete this service-linked role, and then need to create it again, you can use the same process to recreate the role in your account. When you update the settings, AWS Transform creates the service-linked role for you again. 

You can also use the IAM console or AWS CLI to create a service-linked role with the `transform.amazonaws.com` service name. For more information, see [Creating a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#create-service-linked-role) in the *IAM User Guide*. If you delete this service-linked role, you can use this same process to create the role again.

### Editing a service-linked role for AWS Transform
<a name="edit-slr"></a>

AWS Transform does not allow you to edit the AWSServiceRoleForAWSTransform service-linked role. After you create a service-linked role, you cannot change the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see [Editing a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role) in the *IAM User Guide*.

### Deleting a service-linked role for AWS Transform
<a name="delete-slr"></a>

If you no longer need to use a feature or service that requires a service-linked role, we recommend that you delete that role. That way you don't have an unused entity that is not actively monitored or maintained. However, you must clean up the resources for your service-linked role before you can manually delete it.

**Note**  
If the AWS Transform service is using the role when you try to delete the resources, then the deletion might fail. If that happens, wait for a few minutes and try the operation again.

**To manually delete the service-linked role using IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForAWSTransform service-linked role. For more information, see [Deleting a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role) in the *IAM User Guide*.

### Supported Regions for AWS Transform service-linked roles
<a name="slr-regions"></a>

AWS Transform does not support using service-linked roles in every Region where the service is available. You can use the AWSServiceRoleForAWSTransform role in the following Regions. For more information, see [AWS Regions and endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html).



| Region name | Region identity | Support in AWS Transform | 
| --- | --- | --- | 
| US East (N. Virginia) | us-east-1 | Yes | 
| Europe (Frankfurt) | eu-central-1 | Yes | 

## Using service-linked roles for AWS Transform Custom
<a name="using-service-linked-roles-custom"></a>

AWS Transform Custom uses the service-linked role named **AWSServiceRoleForAWSTransformCustom** to publish metrics and logs to your account on your behalf. These metrics let you monitor transformation counts, latencies, and status codes directly in your dashboards. Logs provide visibility into issues encountered during transformations.

This [service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role) is predefined by AWS Transform Custom and includes only the permissions the service needs. You don't have to manually add any permissions, and the role can only be assumed by AWS Transform Custom. For general information about service-linked roles, see [Using service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html) in the *IAM User Guide*.

### Service-linked role permissions for AWS Transform Custom
<a name="slr-permissions-custom"></a>

The AWSServiceRoleForAWSTransformCustom service-linked role trusts the following services to assume the role:
+ `transform-custom.amazonaws.com`

The role permissions policy named AWSServiceRoleForAWSTransformCustom allows AWS Transform Custom to complete the following actions on the specified resources:
+ `cloudwatch:PutMetricData` on all AWS resources
  + Publish operational metrics to under the `AWS/TransformCustom` namespace
  + Track transformation counts, latencies, and status codes
  + Scoped to the `AWS/TransformCustom` namespace via the `cloudwatch:namespace` condition key
+ `logs:CreateLogGroup` and `logs:PutRetentionPolicy` on the `/aws/TransformCustom` log group
  + Create the CloudWatch Logs log group for publishing transformation logs
  + Set log retention policies on the log group
  + Scoped to `arn:aws:logs:*:*:log-group:/aws/TransformCustom` with an `aws:ResourceAccount` condition ensuring access only within your account
+ `logs:CreateLogStream` and `logs:PutLogEvents` on log streams within the `/aws/TransformCustom` log group
  + Create log streams and publish log events for transformation operations
  + Scoped to `arn:aws:logs:*:*:log-group:/aws/TransformCustom:log-stream:*` with an `aws:ResourceAccount` condition ensuring access only within your account

You must configure permissions to allow your users, groups, or roles to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the *IAM User Guide*.

### Creating a service-linked role for AWS Transform Custom
<a name="create-slr-custom"></a>

You don't need to manually create a service-linked role. When you run a transformation using the AWS Transform Custom CLI, AWS Transform Custom creates the service-linked role for you.

If you delete this service-linked role, and then need to create it again, you can use the same process to recreate the role in your account. When you run a transformation using the AWS Transform Custom CLI, AWS Transform Custom creates the service-linked role for you again.

You can also use the IAM console to create a service-linked role with the **AWSServiceRoleForAWSTransformCustom** use case. In the AWS CLI or the AWS API, create a service-linked role with the `transform-custom.amazonaws.com` service name. For more information, see [Creating a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#create-service-linked-role) in the *IAM User Guide*. If you delete this service-linked role, you can use this same process to create the role again.

### Editing a service-linked role for AWS Transform Custom
<a name="edit-slr-custom"></a>

AWS Transform Custom does not allow you to edit the AWSServiceRoleForAWSTransformCustom service-linked role. After you create a service-linked role, you cannot change the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see [Editing a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role) in the *IAM User Guide*.

### Deleting a service-linked role for AWS Transform Custom
<a name="delete-slr-custom"></a>

If you no longer need to use a feature or service that requires a service-linked role, we recommend that you delete that role. That way you don't have an unused entity that is not actively monitored or maintained.

The AWSServiceRoleForAWSTransformCustom service-linked role does not create persistent resources in your account. You can delete it directly without any resource cleanup.

If you delete this role and later run a transformation using the AWS Transform Custom CLI, the service-linked role is automatically recreated.

**To manually delete the service-linked role using IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForAWSTransformCustom service-linked role. For more information, see [Deleting a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role) in the *IAM User Guide*.

### Supported Regions for AWS Transform Custom service-linked roles
<a name="slr-regions-custom"></a>

AWS Transform Custom supports using service-linked roles in all Regions where AWS Transform Custom is available. For a list of supported Regions, see [Supported Regions](https://docs.aws.amazon.com/transform/latest/userguide/custom-get-started.html#custom-region-configuration).