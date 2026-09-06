

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Generating the required AWS credentials
<a name="credentials"></a>

In order to install the AWS Replication Agent, you must first generate the required AWS credentials. 

**Note**  
Temporary credentials have many advantages. You don't need to rotate them or revoke them when they're no longer needed, and they cannot be reused after they expire. You can specify for how long the credentials are valid, up to a maximum limit. Because they provide enhanced security, using temporary credentials is considered best practice and the recommended option.

## Temporary credentials
<a name="credentials-agent-temporary"></a>

The temporary credentials provided by AWS Transform MGN utilize a similar mechanism to the one used by [IAM Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html).

To create temporary credentials, you need to:

1.  [Create a new IAM Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html) with the **AWSApplicationMigrationAgentInstallationPolicy** policy.

1. Request temporary security credentials [through AWS STS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html) through the [AssumeRole API](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html). 

   An example of generating temporary credentials via AWS CLI can be found [here](https://docs.aws.amazon.com/cli/latest/reference/sts/assume-role.html#examples).

[Learn more about how temporary credentials work.](Agent-Related-FAQ.md#temporary-credentials-operation)

## Permanent credentials
<a name="credentials-agent-iam"></a>

Where possible, we recommend using temporary credentials instead of creating users who have long-term credentials such as passwords and access keys. However, there are specific use cases that require long-term credentials (for example, agentless snapshot based replications). In general, you should be able to use the same policy as recommended above in *Temporary Credentials*.

## Installing the AWS Replication Agent on an Amazon EC2 instance
<a name="agent-installations-in-aws"></a>

When installing an AWS Replication Agent on an Amazon EC2 instance (when the source server is in AWS Regions), you don't need to generate credentials. Instead, you can use an instance profile with the required IAM policy. This option can only be used when replicating a server within the same account.
+ Go to the Amazon EC2 console and select your Amazon EC2 instance.
+ From the top right-hand menu, select **Actions > Security > Modify IAM role**.
+ Use a role that contains the [AWSApplicationMigrationServiceEc2InstancePolicy](security-iam-awsmanpol-AWSApplicationMigrationServiceEc2InstancePolicy.md) policy.

  If none exists, choose **Create new IAM role**, attach the policy and return to the Amazon EC2 console window.
+ Select your new role from the drop-down list and choose **Update**.