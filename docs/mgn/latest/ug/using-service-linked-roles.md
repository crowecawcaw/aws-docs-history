NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Using service-linked roles for

AWS Application Migration Service

AWS Application Migration Service uses AWS Identity and Access Management (IAM)[service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to AWS Application Migration Service. Service-linked roles are predefined by
AWS Application Migration Service and include all the permissions that the service requires to
call other AWS services on your behalf.

A service-linked role makes setting up AWS Application Migration Service easier because you don’t have to
manually add the necessary permissions. AWS Application Migration Service defines the permissions of its
service-linked roles, and unless defined otherwise, only AWS Application Migration Service can assume its
roles. The defined permissions include the trust policy and the permissions policy, and
that permissions policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources.
This protects your AWS Application Migration Service resources because you can't inadvertently remove
permission to access the resources.

For information about other services that support service-linked roles, see [AWS Services
That Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-Linked Role** column. Choose a
**Yes**
with a link to view the service-linked role
documentation for that service.

## AWSServiceRoleForApplicationMigrationService

service-linked role

AWS Application Migration Service uses the service-linked role named
**AWSServiceRoleForApplicationMigrationService**. This is a managed
IAM policy with scoped permissions that AWS Application Migration Service needs to run in your account.

The AWSServiceRoleForApplicationMigrationService service-linked role trusts the `mgn.amazonaws.com` service principal to assume the role. The role permissions are defined in the [AWSApplicationMigrationServiceRolePolicy](security-iam-awsmanpol-AWSApplicationMigrationServiceRolePolicy.md "security-iam-awsmanpol-AWSApplicationMigrationServiceRolePolicy.md") AWS managed policy.

To view the policy permission details see
[AWSApplicationMigrationServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSApplicationMigrationServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSApplicationMigrationServiceRolePolicy.md") in the AWS Managed Policy Reference Guide.

You must configure permissions to allow an IAM entity (such as a user, group, or
role) to create, edit, or delete a service-linked role. For more information, see [Service-Linked Role Permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating a service-linked role for AWS Application Migration Service

You don't need to manually create a service-linked role. When you configure the
Replication Configuration Template for AWS Application Migration Service, a service-linked
role is automatically created. MGN automatically creates the IAM service-linked role,
which you can see in the IAM console. You don't need to manually create or configure this
role.

If you delete this service-linked role, and then need to create it again, you can use
the same process to recreate the role in your account. When you create the first new
replication configuration template in MGN, it creates the service-linked role for you
again.

In the AWS CLI or the AWS API, create a service-linked role with the
AWS Application Migration Service name. For more information, see [Creating a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role") in
the*IAM User Guide*. If you delete this service-linked
role, you can use this same process to create the role again.

## Editing a service-linked role for AWS Application Migration Service

AWS Application Migration Service does not allow you to edit the
AWSServiceRoleForApplicationMigrationService service-linked role. After you create a
service-linked role, you cannot change the name of the role because various entities might
reference the role. However, you can edit the description of the role using IAM. For
more information, see [Editing a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the
_IAM User Guide_.

## Deleting a service-linked role for AWS Application Migration Service

If you no longer need to use a feature or service that requires a service-linked
role, we recommend that you delete that role. That way you don’t have an unused entity
that is not actively monitored or maintained. However, you must clean up the resources
for your service-linked role before you can manually delete it.

###### Note

If AWS Application Migration Service is using the role when you try to delete the
resources, the deletion might fail. If that happens, wait for a few minutes and try the
operation again.

**To clean up AWS Application Migration Service resources used
by AWSServiceRoleforApplicationMigrationService**

1. Identify and delete any waves and applications in all
   AWS Regions
   1. identify any waves:

   ```
   aws mgn list-waves
   ```

   2. Delete any waves:

   ```
   aws mgn delete-wave --wave-id {WaveID}
   ```

   3. Identify any application:

   ```
   aws mgn list-applications
   ```

   4. Delete any application:

   ```
   aws mgn delete-application --application-id {ApplicationID}
   ```

2. Identify and delete any source servers in all AWS Regions
   1. Identify any active source servers:

   ```
   aws mgn describe-source-servers --filters isArchived=False --query "items[*].sourceServerID"
   ```

   2. Disconnect any active source servers:

   ```
   aws mgn disconnect-from-service --source-server-id {SourceServerID}
   ```

   3. Archive any disconnected source servers:

   ```
   aws mgn mark-as-archived --source-server-id {SourceServerID}
   ```

   4. Delete any archived source server:

   ```
   aws mgn delete-source-server --source-server-id {SourceServerID}
   ```

3. Identify and delete any AWS MGN jobs in all AWS Regions
   1. Identify any AWS MGN jobs

   ```
   aws mgn describe-jobs
   ```

   2. Delete any AWS MGN jobs:

   ```
   aws mgn delete-job --job-id {MGNJobId}
   ```

4. Identify and delete any AWS MGN replication templates
   1. Identify any AWS MGN replication template:

   ```
   aws mgn describe-replication-configuration-templates
   ```

   2. Remove any AWS MGN replication templates:

   ```
   aws mgn delete-replication-configuration-template --replication-configuration-template-id {rct-TemplateID}
   ```

Resources can be cleaned up without stopping any service provided by
AWS Application Migration Service. Cleaning up AWS Application Migration Service
resources will cause AWS Application Migration Service to stop working. For more
information, see [Cleaning up a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
_IAM User Guide_.

**To manually delete the service-linked role using
IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the
AWSServiceRoleForApplicationMigrationService service-linked role. For more information,
see [Deleting a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
_IAM User Guide_.

## Supported Regions for AWS MGN service-linked roles

AWS Application Migration Service supports using service-linked roles in all of the [AWS Regions where
the service is available](what-is-application-migration-service.md#supported-regions "what-is-application-migration-service.md#supported-regions").
