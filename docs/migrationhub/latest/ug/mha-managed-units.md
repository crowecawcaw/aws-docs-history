AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Managed AWS Migration Hub automation units

###### Note

The AWS Migration Hub Automation feature is in preview release. It is available in
US East (N. Virginia). To use this feature, you must set your AWS Region to US East (N. Virginia).
You must also set the AWS Migration Hub home Region to US East (N. Virginia). For instructions on how to
set the AWS Migration Hub home Region, see [Managing your AWS Migration Hub home Region](home-region.md "home-region.md").

This is pre-release documentation. Both the AWS Migration Hub Automation feature and the
documentation are subject to change.

This topic describes the automation units that AWS Migration Hub provides. These units are referred
to as managed automation units. This topic also describes the prerequisites for running a
managed automation unit.

## Prerequisites for running managed automation

units

- Ensure that you have created an IAM role that has the trust policy that Migration Hub needs
  to be able to run the unit and the permissions policy that the unit needs. For information
  about the required trust policy and permissions policy, see [IAM roles and permissions for AWS Migration Hub automation
  units](mha-iam-roles.md "mha-iam-roles.md"). After you create the required role, associate it with the automation unit. For
  instructions, see [Associating an IAM role with an AWS Migration Hub
  automation unit](associate-role-with-unit.md "associate-role-with-unit.md").
- The following automation units all use AWS Application Migration Service. Ensure that AWS Application Migration Service is initialized
  in the AWS Region where you plan to run one or more of these units. For instructions,
  see [Initializing Application Migration Service with the console](../../../mgn/latest/ug/mgn-initialize-console.md "../../../mgn/latest/ug/mgn-initialize-console.md") or [Initializing AWS
  Application Migration Service with the API](../../../mgn/latest/ug/mgn-initialize-api.md "../../../mgn/latest/ug/mgn-initialize-api.md").
- Import your inventory into AWS Application Migration Service. For instructions, see [Importing your data
  inventory](../../../mgn/latest/ug/import-main.md "../../../mgn/latest/ug/import-main.md").

###### Managed automation units

- [AWS-MGN-InstallReplicationAgent](#mha-AWS-MGN-InstallReplicationAgent "#mha-AWS-MGN-InstallReplicationAgent")
- [AWS-MGN-VerifyReplicationHealth](#mha-AWS-MGN-VerifyReplicationHealth "#mha-AWS-MGN-VerifyReplicationHealth")
- [AWS-MGN-LaunchTestInstances](#mha-AWS-MGN-LaunchTestInstances.xml "#mha-AWS-MGN-LaunchTestInstances.xml")
- [AWS-MGN-MarkReadyForCutover](#mha-AWS-MGN-MarkReadyForCutover "#mha-AWS-MGN-MarkReadyForCutover")
- [AWS-MGN-TerminateTargetInstances](#mha-AWS-TerminateTargetInstances "#mha-AWS-TerminateTargetInstances")
- [AWS-MGN-LaunchCutoverInstances](#mha-AWS-MGN-LaunchCutoverInstances "#mha-AWS-MGN-LaunchCutoverInstances")
- [AWS-MGN-FinalizeCutover](#mha-AWS-MGN-FinalizeCutover "#mha-AWS-MGN-FinalizeCutover")
- [AWS-MGN-ArchiveSourceServers](#mha-AWS-MGN-ArchiveSourceServers "#mha-AWS-MGN-ArchiveSourceServers")

## AWS-MGN-InstallReplicationAgent

This automation unit uses the MGN connector to install AWS Replication Agent on source servers. The unit
performs the following actions:

1. It registers source servers with the MGN connector.
2. It registers credentials with source servers.
3. It verifies required IAM roles exist in the account.
4. It verifies the prerequisites that are required to install the AWS Replication Agent on the source
   servers.
5. It installs the AWS Replication Agent agent on the source servers.

**Prerequisites:**

1. Ensure that your source servers meet the requirements for installing the AWS Replication Agent. For
   details, see [Installation requirements](../../../mgn/latest/ug/installation-requirements.md "../../../mgn/latest/ug/installation-requirements.md") .
2. **Prepare Application Migration Service import file and import it to
   Application Migration Service**:
   - Create an import file in the CSV format that contains the information about the
     servers that you want to migrate.
   - The import file must include the following fields: `mgn:account-id`,
     `mgn:region` , `mgn:wave:name` , `mgn:wave:tag:[KEY]`
     , `mgn:wave:description` , `mgn:app:name` ,
     `mgn:app:description` , `mgn:server:user-provided-id` ,
     `mgn:server:platform` , `mgn:server:fqdn-for-action-framework` ,
     `mgn:launch:instance-type` , `mgn:launch:placement:tenancy` ,
     `mgn:launch:iam-instance-profile:name` ,
     `mgn:launch:placement:host-id` .
   - Import the CSV file to the Application Migration Service service by using the AWS Management Console, AWS CLI, or AWS
     SDK.

3. **Set up the MGN connector**:
   - Navigate to the MGN service in the AWS Management Console.
   - Follow the instructions to download and install the MGN connector on a dedicated
     Linux server.
   - Configure the connector to connect to the MGN service.

4. **Store source servers credentials in an AWS Secrets Manager
   secret**:
   - Follow the instructions described in [Register server
     credentials](../../../mgn/latest/ug/connector-register-server-credentials.md "../../../mgn/latest/ug/connector-register-server-credentials.md") to create a new secret in AWS Secrets Manager that stores the credentials
     for the source servers.
   - Make sure to add the `AWSApplicationMigrationServiceManaged` tag to the
     secret.
   - The Application Migration Service service will use the stored credentials in order to connect to the source
     servers and perform actions on them during the migration process.

### Inputs

| Parameter name       | Description                                                                                      | Type   | Required? |
| -------------------- | ------------------------------------------------------------------------------------------------ | ------ | --------- |
| WaveARN              | Application Migration Service wave ARN                                                           | string | True      |
| ApplicationARNs      | List of Application Migration Service application ARNs.                                          | array  | False     |
| ConnectorArn         | Application Migration Service connector ARN to use for the Application Migration Service rehost. | string | True      |
| CredentialsSecretArn | Secret ARN containing the credentials for the source servers in scope.                           | string | True      |

## AWS-MGN-VerifyReplicationHealth

Run this unit after you install the replication agent on the source servers.

After you install the replication agent on the source machines, you monitor the status of
data replication and resolve issues like permissions or network performance. This managed unit
retries every 10 minutes until the status of every server in the wave changes to Continuous Data
Replication.

Depending on the amount of data to replicate on the provided source servers, replication can
take several days.

### Inputs

| Parameter name  | Description                                             | Type   | Required? |
| --------------- | ------------------------------------------------------- | ------ | --------- |
| WaveARN         | Application Migration Service wave ARN                  | string | True      |
| ApplicationARNs | List of Application Migration Service application ARNs. | array  | False     |

## AWS-MGN-LaunchTestInstances

After you add all of your source servers and configure their launch settings, you are ready
to launch one test instance per source server. To verify that your applications can function
properly within the AWS environment, it is crucial that you test the migration of your source
servers to AWS before you initiate a cutover.

Before you run this automation unit, ensure that ReplicationStatus is healthy.

### Inputs

| Parameter name  | Description                                             | Type   | Required? |
| --------------- | ------------------------------------------------------- | ------ | --------- |
| WaveARN         | Application Migration Service wave ARN                  | string | True      |
| ApplicationARNs | List of Application Migration Service application ARNs. | array  | False     |

## AWS-MGN-MarkReadyForCutover

After you launch your test instances, go to the Amazon EC2 console and use SSH or RDP to connect
to your test instances and ensure that the instances are functioning correctly. If you are done
with your testing and are ready for cutover, you can finalize the test. This will change your
migration lifecycle status of your source servers to Ready for cutover, indicating that all
testing is complete and that these servers are now ready for cutover.

Before you run this automation unit, make sure that you have finished your testing and that
you are ready for cutover.

### Inputs

| Parameter name  | Description                                             | Type   | Required? |
| --------------- | ------------------------------------------------------- | ------ | --------- |
| WaveARN         | Application Migration Service wave ARN                  | string | True      |
| ApplicationARNs | List of Application Migration Service application ARNs. | array  | False     |

## AWS-MGN-TerminateTargetInstances

This automation unit starts and verifies the
completion of an Application Migration Service job that terminates launched Amazon EC2 test and cutover instances.

This unit does not work for any source
server whose lifecycle state is TESTING, CUTTING_OVER, or CUTOVER.

### Inputs

| Parameter name  | Description                                             | Type   | Required? |
| --------------- | ------------------------------------------------------- | ------ | --------- |
| WaveARN         | Application Migration Service wave ARN                  | string | True      |
| ApplicationARNs | List of Application Migration Service application ARNs. | array  | False     |

## AWS-MGN-LaunchCutoverInstances

After you finalize the testing of all of your source servers, you are ready for cutover. The
cutover will migrate your source servers to the cutover instances on AWS.

### Inputs

| Parameter name  | Description                                             | Type   | Required? |
| --------------- | ------------------------------------------------------- | ------ | --------- |
| WaveARN         | Application Migration Service wave ARN                  | string | True      |
| ApplicationARNs | List of Application Migration Service application ARNs. | array  | False     |

## AWS-MGN-FinalizeCutover

After you perform a successful cutover and complete the migration, this automation unit
changes the migration lifecycle status of your source servers to Cutover complete. This status
indicates that the migration was successful. This unit also stops data replication and causes
all replicated data to be discarded. All AWS resources used for data replication will be
terminated.

To ensure that your cutover instances are functioning correctly after you launch them, go to
the Amazon EC2 console and use SSH or RDP to connect to the instances. Validate connectivity, and
perform acceptance tests for your application.

### Inputs

| Parameter name  | Description                                             | Type   | Required? |
| --------------- | ------------------------------------------------------- | ------ | --------- |
| WaveARN         | Application Migration Service wave ARN                  | string | True      |
| ApplicationARNs | List of Application Migration Service application ARNs. | array  | False     |

## AWS-MGN-ArchiveSourceServers

This automation unit archives source servers by removing them from the main AWS Application Migration Service
(Application Migration Service) source servers page. Archiving allows you to focus on source servers that haven't yet
been cut over.

Ensure that the servers that you plan to archive have launched cutover instances.

### Inputs

| Parameter name  | Description                                             | Type   | Required? |
| --------------- | ------------------------------------------------------- | ------ | --------- |
| WaveARN         | Application Migration Service wave ARN                  | string | True      |
| ApplicationARNs | List of Application Migration Service application ARNs. | array  | False     |
