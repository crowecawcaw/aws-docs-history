

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Requirements
<a name="source-server-actions-requirements"></a>

Before performing any source server actions, ensure that the following requirements are met:
+ AWS Transform MGN has been [initialized](getting-started.md) in the target AWS Region.
+ The AWS Replication Agent has been installed on the source server. [Learn more about adding source servers](adding-servers.md).
+ The IAM user or role performing actions has the **AWSApplicationMigrationFullAccess** managed policy attached, or equivalent permissions.
+ Network connectivity between the source server and the MGN service endpoints is maintained throughout the migration lifecycle. [Learn more about network requirements](preparing-environments.md#Network-Requirements).