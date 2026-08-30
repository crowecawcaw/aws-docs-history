NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Initializing AWS Transform MGN with the API

In order to use AWS Transform MGN (MGN), the service must first be initialized for any
AWS Region in which you plan to use MGN.

You can initialize the service via the console or via the API.

During the initialization process:

- The required IAM roles and policies will be created.
- The required templates are configured.
  You can initialize AWS Transform MGN through the API. This option allows you to automate service
  initialization through a script when initializing multiple accounts.

You can also initialize MGN using the console. For more information, see [Initializing MGN with the console](mgn-initialize-console.md "mgn-initialize-console.md").

To initialize the service via the API, take the following steps:

1. Create the required IAM roles.
2. Create the replication template and launch template.

###### Note

You must complete both steps to finalize the service initialization process.

## Creating the required IAM roles

To initialize MGN with the API, create the following IAM roles through the [IAM
CreateRole API](../../../IAM/latest/APIReference/API_CreateRole.md "../../../IAM/latest/APIReference/API_CreateRole.md"). Learn more about [creating IAM
roles in the AWS IAM documentation](../../../IAM/latest/UserGuide/id_roles_create.md "../../../IAM/latest/UserGuide/id_roles_create.md"). Creation of each role must include the following
parameters:

| Role name                                            | Trusted entities    |
| ---------------------------------------------------- | ------------------- |
|                                                      | **Principal**       | **Action**                                  | **Condition**                                                                                |
| **AWSApplicationMigrationReplicationServerRole**     | "ec2.amazonaws.com" | "sts:AssumeRole"                            | -                                                                                            |
| **AWSApplicationMigrationConversionServerRole**      | "ec2.amazonaws.com" | "sts:AssumeRole"                            | -                                                                                            |
| **AWSApplicationMigrationMGHRole**                   | "mgn.amazonaws.com" | "sts:AssumeRole"                            | -                                                                                            |
| **AWSApplicationMigrationLaunchInstanceWithDrsRole** | "ec2.amazonaws.com" | "sts:AssumeRole"                            | -                                                                                            |
| **AWSApplicationMigrationLaunchInstanceWithSsmRole** | "ec2.amazonaws.com" | "sts:AssumeRole"                            | -                                                                                            |
| **AWSApplicationMigrationFsxProxyRole**              | "mgn.amazonaws.com" | "sts:AssumeRole"                            | -                                                                                            |
| **AWSApplicationMigrationFsxProxyLinkRole**          | "mgn.amazonaws.com" | "sts:AssumeRole"                            | -                                                                                            |
| **AWSApplicationMigrationAgentRole**                 | "mgn.amazonaws.com" | ["sts:AssumeRole", "sts:SetSourceIdentity"] | {"StringLike": {"sts:SourceIdentity": "s-\*", "aws:SourceAccount":<br>"<SOURCE-ACCOUNT-ID>"} |

1. Attach Managed Policy**AWSApplicationMigrationReplicationServerPolicy** to Role **AWSApplicationMigrationReplicationServerRole**
2. Attach Managed Policy **AWSApplicationMigrationConversionServerPolicy** to Role **AWSApplicationMigrationConversionServerRole**
3. Attach Managed Policy **AWSApplicationMigrationMGHAccess**
   to Role **AWSApplicationMigrationMGHRole**
4. Attach Managed Policies **AmazonSSMManagedInstanceCore** and
   **AWSElasticDisasterRecoveryEc2InstancePolicy** to Role
   **AWSApplicationMigrationLaunchInstanceWithDrsRole**
5. Attach Managed Policy **AmazonSSMManagedInstanceCore** to
   Role **AWSApplicationMigrationLaunchInstanceWithSsmRole**
6. Attach Managed Policy**AWSApplicationMigrationFSxProxyPolicy** to Role **AWSApplicationMigrationFsxProxyRole**
7. Attach Managed Policy**AWSApplicationMigrationFSxProxyVPCPolicy** to Role **AWSApplicationMigrationFsxProxyLinkRole**
8. Attach Managed Policy**AWSApplicationMigrationAgentPolicy\_v2** to Role **AWSApplicationMigrationAgentRole**

Once the policies are attached to the roles, run the `aws mgn
 initialize-service` command. This will automatically create the service-linked role,
create instance profiles, and add Roles to Instance Profiles. After running this command, you
must still create the replication configuration template and launch configuration template to
finalize initialization.

[Learn more about AWS Transform MGN roles and managed
policies](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

## Creating the templates

To finalize the initialization process, you will need to [create the replication template](../APIReference/API_CreateReplicationConfigurationTemplate.md "../APIReference/API_CreateReplicationConfigurationTemplate.md") and launch template by running the following
commands:

- `aws mgn create-replication-configuration-template`

- `aws mgn create-launch-configuration-template`
