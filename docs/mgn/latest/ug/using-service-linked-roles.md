

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Using service-linked roles for AWS Transform MGN
<a name="using-service-linked-roles"></a>

AWS Transform MGN uses AWS Identity and Access Management (IAM)[ service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role). A service-linked role is a unique type of IAM role that is linked directly to AWS Transform MGN. Service-linked roles are predefined by AWS Transform MGN and include all the permissions that the service requires to call other AWS services on your behalf. 

A service-linked role makes setting up AWS Transform MGN easier because you don’t have to manually add the necessary permissions. AWS Transform MGN defines the permissions of its service-linked roles, and unless defined otherwise, only AWS Transform MGN can assume its roles. The defined permissions include the trust policy and the permissions policy, and that permissions policy cannot be attached to any other IAM entity. 

You can delete a service-linked role only after first deleting their related resources. This protects your AWS Transform MGN resources because you can't inadvertently remove permission to access the resources. 

For information about other services that support service-linked roles, see [AWS Services That Work with IAM ](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) and look for the services that have **Yes **in the **Service-Linked Role** column. Choose a **Yes** with a link to view the service-linked role documentation for that service. 

## AWSServiceRoleForApplicationMigrationService service-linked role
<a name="slr-permissions"></a>

AWS Transform MGN uses the service-linked role named **AWSServiceRoleForApplicationMigrationService**. This service-linked role has scoped permissions that AWS Transform MGN needs to run in your account. Its permissions are defined by the AWSApplicationMigrationServiceRolePolicy AWS managed policy. 

The AWSServiceRoleForApplicationMigrationService service-linked role trusts the `mgn.amazonaws.com` service principal to assume the role. The role permissions are defined in the [AWSApplicationMigrationServiceRolePolicy](https://docs.aws.amazon.com/mgn/latest/ug/security-iam-awsmanpol-AWSApplicationMigrationServiceRolePolicy.html) AWS managed policy. 

To view the policy permission details see [AWSApplicationMigrationServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSApplicationMigrationServiceRolePolicy.html) in the AWS Managed Policy Reference Guide. 

You must configure permissions to allow an IAM entity (such as a user, group, or role) to create, edit, or delete a service-linked role. For more information, see [Service-Linked Role Permissions ](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the *IAM User Guide*. 

## Creating a service-linked role for AWS Transform MGN
<a name="create-slr"></a>

You don't need to manually create a service-linked role. When you configure the Replication Configuration Template for AWS Transform MGN, a service-linked role is automatically created. MGN automatically creates the IAM service-linked role, which you can see in the IAM console. You don't need to manually create or configure this role. 

If you delete this service-linked role, and then need to create it again, you can use the same process to recreate the role in your account. When you create the first new replication configuration template in MGN, it creates the service-linked role for you again. 

In the AWS CLI or the AWS API, create a service-linked role with the AWS Transform MGN name. For more information, see [Creating a Service-Linked Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#create-service-linked-role) in the*IAM User Guide*. If you delete this service-linked role, you can use this same process to create the role again. 

## Editing a service-linked role for AWS Transform MGN
<a name="edit-slr"></a>

AWS Transform MGN does not allow you to edit the AWSServiceRoleForApplicationMigrationService service-linked role. After you create a service-linked role, you cannot change the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see [Editing a Service-Linked Role ](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role) in the *IAM User Guide*. 

## Deleting a service-linked role for AWS Transform MGN
<a name="delete-slr"></a>

If you no longer need to use a feature or service that requires a service-linked role, we recommend that you delete that role. That way you don’t have an unused entity that is not actively monitored or maintained. However, you must clean up the resources for your service-linked role before you can manually delete it. 

**Note**  
If AWS Transform MGN is using the role when you try to delete the resources, the deletion might fail. If that happens, wait for a few minutes and try the operation again. 

 **To clean up AWS Transform MGN resources used by AWSServiceRoleForApplicationMigrationService**

1. Identify and delete any waves and applications in all AWS Regions

   1. identify any waves:

      ```
      aws mgn list-waves
      ```

   1. Delete any waves:

      ```
      aws mgn delete-wave --wave-id {WaveID}
      ```

   1. Identify any application:

      ```
      aws mgn list-applications
      ```

   1. Delete any application:

      ```
      aws mgn delete-application --application-id {ApplicationID}
      ```

1. Identify and delete any source servers in all AWS Regions

   1. Identify any active source servers:

      ```
      aws mgn describe-source-servers --filters isArchived=False --query "items[*].sourceServerID"
      ```

   1. Disconnect any active source servers:

      ```
      aws mgn disconnect-from-service --source-server-id {SourceServerID}
      ```

   1.  Archive any disconnected source servers: 

      ```
      aws mgn mark-as-archived --source-server-id {SourceServerID}
      ```

   1. Delete any archived source server:

      ```
      aws mgn delete-source-server --source-server-id {SourceServerID}
      ```

1. Identify and delete any MGN jobs in all AWS Regions

   1. Identify any MGN jobs

      ```
      aws mgn describe-jobs
      ```

   1. Delete any MGN jobs:

      ```
      aws mgn delete-job --job-id {MGNJobId}
      ```

1. Identify and delete any MGN replication templates

   1. Identify any MGN replication template:

      ```
      aws mgn describe-replication-configuration-templates
      ```

   1. Remove any MGN replication templates:

      ```
      aws mgn delete-replication-configuration-template --replication-configuration-template-id {rct-TemplateID}
      ```

 

Resources cannot be cleaned up without stopping the services provided by AWS Transform MGN. Cleaning up AWS Transform MGN resources will cause AWS Transform MGN to stop working. Before you run the following commands, confirm that migrations and replication are no longer needed. For more information, see [Cleaning up a Service-Linked Role ](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role) in the *IAM User Guide*. 

 **To manually delete the service-linked role using IAM ** 

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForApplicationMigrationService service-linked role. For more information, see [Deleting a Service-Linked Role ](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role) in the *IAM User Guide*. 

## Supported Regions for MGN service-linked roles
<a name="slr-regions"></a>

AWS Transform MGN supports using service-linked roles in all of the [AWS Regions where the service is available](what-is-mgn.md#supported-regions). 