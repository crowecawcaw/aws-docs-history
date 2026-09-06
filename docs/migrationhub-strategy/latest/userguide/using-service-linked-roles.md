

AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform).

# Using service-linked roles for Strategy Recommendations
<a name="using-service-linked-roles"></a>

Migration Hub Strategy Recommendations uses AWS Identity and Access Management (IAM)[ service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role). A service-linked role is a unique type of IAM role that is linked directly to Strategy Recommendations. Service-linked roles are predefined by Strategy Recommendations and include all the permissions that the service requires to call other AWS services on your behalf. 

A service-linked role makes setting up Strategy Recommendations easier because you don’t have to manually add the necessary permissions. Strategy Recommendations defines the permissions of its service-linked roles, and unless defined otherwise, only Strategy Recommendations can assume its roles. The defined permissions include the trust policy and the permissions policy, and that permissions policy cannot be attached to any other IAM entity.

For information about other services that support service-linked roles, see [AWS Services That Work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) and look for the services that have **Yes ** in the **Service-Linked Role** column. Choose a **Yes** with a link to view the service-linked role documentation for that service.

## Service-linked role permissions for Strategy Recommendations
<a name="slr-permissions"></a>

Strategy Recommendations uses the service-linked role named **AWSServiceRoleForMigrationHubStrategy** and associates it with **AWSMigrationHubStrategyServiceRolePolicy** IAM policy – Provides access to AWS Migration Hub and AWS Application Discovery Service. This policy also grants permissions for storing reports in Amazon Simple Storage Service (Amazon S3).

The **AWSServiceRoleForMigrationHubStrategy** service-linked role trusts the following services to assume the role:
+ `migrationhub-strategy.amazonaws.com`

The role permissions policy allows Strategy Recommendations to complete the following actions. 

AWS Application Discovery Service actions  
 `discovery:ListConfigurations`   
 `discovery:DescribeConfigurations` 

AWS Migration Hub actions  
 `mgh:GetHomeRegion` 

Amazon S3 actions  
 `s3:GetBucketAcl`   
 `s3:GetBucketLocation`   
 `s3:GetObject`   
 `s3:ListAllMyBuckets`   
 `s3:ListBucket`   
 `s3:PutObject`   
 `s3:PutObjectAcl`

To view the permissions for this policy, see [AWSMigrationHubStrategyServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSMigrationHubStrategyServiceRolePolicy.html) in the *AWS Managed Policy Reference Guide*.

To view the update history of this policy, see [Strategy Recommendations updates to AWS managed policies](security-iam-awsmanpol.md#security-iam-awsmanpol-updates).

You must configure permissions to allow an IAM entity (such as a user, group, or role) to create, edit, or delete a service-linked role. For more information, see [Service-Linked Role Permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the *IAM User Guide*.

## Creating a service-linked role for Strategy Recommendations
<a name="create-slr"></a>

You don't need to manually create a service-linked role. When you agree to allow Migration Hub to create a service-linked role (SLR) in your account in the AWS Management Console, Strategy Recommendations creates the service-linked role for you.

If you delete this service-linked role, and then need to create it again, you can use the same process to recreate the role in your account. When you agree to allow Migration Hub to create a service-linked role (SLR) in your account, Strategy Recommendations creates the service-linked role for you again. 

## Editing a service-linked role for Strategy Recommendations
<a name="edit-slr"></a>

Strategy Recommendations does not allow you to edit the **AWSServiceRoleForMigrationHubStrategy** service-linked role. After you create a service-linked role, you cannot change the name of the role because various entities might reference the role. However, you can edit the description of the role using the Strategy Recommendations console, CLI, or API.

## Deleting a service-linked role for Strategy Recommendations
<a name="delete-slr"></a>

**To manually delete the service-linked role using IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the ** AWSServiceRoleForMigrationHubStrategy** service-linked role. For more information, see [Deleting a Service-Linked Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role) in the *IAM User Guide*.

When deleting Strategy Recommendations resources used by the **AWSServiceRoleForMigrationHubStrategy** SLR, you cannot have any running assessments (tasks for generating recommendations). No background assessments can be running, either. If assessments are running, the SLR deletion fails in the IAM console. If the SLR deletion fails, you can retry the deletion after all background tasks have completed. You don’t need to clean up any created resources before you delete the SLR.

## Supported Regions for Strategy Recommendations service-linked roles
<a name="slr-regions"></a>

Strategy Recommendations supports using service-linked roles in all of the regions where the service is available. For more information, see [AWS Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html).