NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Generating the required AWS credentials

In order to install the AWS Replication Agent, you must first generate the required
AWS credentials.

###### Important

Temporary credentials have many advantages. You don't need to rotate them or revoke them
when they're no longer needed, and they cannot be reused after they expire. You can specify
for how long the credentials are valid, up to a maximum limit. Because they provide enhanced
security, using temporary credentials is considered best practice and the recommended
option.

## Temporary credentials

The temporary credentials provided by AWS Application Migration Service utilize a similar mechanism to the one
used by [IAM
Roles Anywhere](../../../rolesanywhere/latest/userguide/introduction.md "../../../rolesanywhere/latest/userguide/introduction.md").

To create temporary credentials, you need to:

1. [Create a
   new IAM Role](../../../IAM/latest/UserGuide/id_roles_create.md "../../../IAM/latest/UserGuide/id_roles_create.md") with the **AWSApplicationMigrationAgentInstallationPolicy** policy.
2. Request temporary security credentials [through AWS STS](../../../IAM/latest/UserGuide/id_credentials_temp_request.md "../../../IAM/latest/UserGuide/id_credentials_temp_request.md") through the [AssumeRole
   API](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md").

An example of generating temporary credentials via AWS CLI can be found [here](../../../cli/latest/reference/sts/assume-role.md#examples "../../../cli/latest/reference/sts/assume-role.md#examples").

[Learn more about how temporary
credentials work.](Agent-Related-FAQ.md#temporary-credentials-operation "Agent-Related-FAQ.md#temporary-credentials-operation")

## Permanent credentials

Where possible, we recommend using temporary credentials instead of creating users who
have long-term credentials such as passwords and access keys. However, there are
specific use cases that require long-term credentials (for example, agentless snapshot
based replications). In general, you should be able to use the same policy as
recommended above in _Temporary Credentials_.

## Installing the AWS Replication Agent on an

Amazon EC2 instance

When installing an AWS Replication Agent on an Amazon EC2 instance (when the source server
is in AWS Regions), you don't need to generate credentials. Instead, you can use an instance
profile with the required IAM policy:

- Go to the Amazon EC2 console and select your Amazon EC2 instance.
- From the top right-hand menu, select **Actions > Security > Modify
  IAM role**.
- Use a role that contains the [AWSApplicationMigrationServiceEc2InstancePolicy](security-iam-awsmanpol-AWSApplicationMigrationServiceEc2InstancePolicy.md "security-iam-awsmanpol-AWSApplicationMigrationServiceEc2InstancePolicy.md") policy.

If none exists, click **Create new IAM role**, attach the
policy and return to the Amazon EC2 console window.

- Select your new role from the drop-down list and click **Update**.
