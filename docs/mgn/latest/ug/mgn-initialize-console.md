NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Initializing Application Migration Service with the console

In order to use AWS Application Migration Service (Application Migration Service), the service must first be initialized for any
AWS Region in which you plan to use Application Migration Service.

You can initialize the service via the console or via the API.

During the initialization process:

- The required IAM roles and policies will be created.
- The required templates are configured.
  AWS Application Migration Service must be initialized upon first use from within the Application Migration Service console by creating a
  replication template.

Once you create the replication template, the initialization process takes place
automatically.

###### Important

The AWS Application Migration Service can only be initialized by the IAM user with the "AdministratorAccess"
managed policy attached in your AWS account.

For information on the IAM roles that Application Migration Service creates on your behalf during the
initialization process, see [IAM role creation](#mgn-iam-roles-initializing "#mgn-iam-roles-initializing"). For information on the predefined managed IAM
policies that Application Migration Service includes, see [Additional policies](#mgn-policies "#mgn-policies").

You can also initialize Application Migration Service using the API. For more information, see [Initializing AWS Application Migration Service with the API](mgn-initialize-api.md "mgn-initialize-api.md").

## IAM role creation

During initialization the following IAM roles will be created.

1. **AWSServiceRoleForApplicationMigrationService**
2. **AWSApplicationMigrationReplicationServerRole**
3. **AWSApplicationMigrationConversionServerRole**
4. **AWSApplicationMigrationMGHRole**
5. **AWSApplicationMigrationLaunchInstanceWithDrsRole**
6. **AWSApplicationMigrationLaunchInstanceWithSsmRole**
7. **AWSApplicationMigrationAgentRole**

Learn more about [AWS Application Migration Service roles and managed
policies](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

## Additional policies

You can create roles with granular permission for AWS Application Migration Service. The service comes with the
following predefined managed IAM policies:

- **AWSApplicationMigrationFullAccess** – This policy provides
  permissions to all public APIs of AWS Application Migration Service (AWS MGN), as well as permissions to read AWS KMS
  key information.
- **AWSApplicationMigrationEC2Access** – This policy allows
  Amazon EC2 operations required to use AWS Application Migration Service (AWS MGN) to launch the migrated servers as Amazon EC2
  instances.
- **AWSApplicationMigrationSSMAccess** – This policy allows
  Amazon EC2 Systems Manager operations required to use AWS Application Migration Service (AWS MGN) to run SSM documents post
  migration of source servers.
- **AWSApplicationMigrationReadOnlyAccess** – The read-only
  policy allows the user to view all data available in the AWS MGN console but does not allow
  them to modify any data or perform any actions. This policy also includes several Amazon EC2
  read-only permissions.
- **AWSApplicationMigrationAgentPolicy** – This policy allows a
  user to install the AWS Replication Agent. [Learn more about
  installing the AWS Replication Agent](credentials.md "credentials.md").
- **AWSApplicationMigrationAgentInstallationPolicy** – This
  policy allows a user to install the AWS Replication Agent. [Learn
  more about installing the AWS Replication Agent](credentials.md "credentials.md").
- **AWSApplicationMigrationServiceEc2InstancePolicy** – This
  policy allows installing and using the AWS Replication Agent, which is used by Application Migration Service (AWS
  MGN) to migrate source servers that run on Amazon EC2 (cross-Region or cross-AZ). An IAM role with
  this policy should be attached (as an Amazon EC2 Instance Profile) to the Amazon EC2 Instances.

You can find all of these policies in the [IAM Console](https://console.aws.amazon.com/iam/home?region=us-east-1 "https://console.aws.amazon.com/iam/home?region=us-east-1").

###### Important

You must attach the AWSApplicationMigrationFullAccess and the
AWSApplicationMigrationEC2Access policies to your users and roles in order to be able to launch
test and cutover instances and to complete a full migration cycle with AWS MGN.
