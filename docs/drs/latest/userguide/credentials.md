

# Generating the required AWS credentials
<a name="credentials"></a>

 In order to install the AWS Replication Agent, you must first generate the required AWS credentials. You can create temporary credentials with AWS STS.

**Important**  
Temporary credentials have many advantages. You do not need to rotate them or revoke them when they are no longer needed, and they cannot be reused after they expire. You can specify for how long the credentials are valid, up to a maximum limit. Because they provide enhanced security, using temporary credentials is considered best practice and the recommended option. For more information, see [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-workloads-use-roles).

## Temporary credentials
<a name="credentials-agent-temporary"></a>

Before you install the AWS Replication Agent, you need to generate temporary AWS security credentials. The temporary credentials provided by AWS Elastic Disaster Recovery utilize a similar mechanism to the one used by [IAM Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html).

To create temporary credentials, take the following steps:

1.  [Create a new IAM Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html) with the **AWSElasticDisasterRecoveryAgentInstallationPolicy** policy.

1.  Request temporary security credentials [via AWS STS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html) using the [AssumeRole API](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html). 

[Learn more about how temporary credentials work.](Agent-Related-FAQ.md#temporary-credentials-operation)

**Note**  
You can also create the default IAM role with the required permissions as an instance profile, as described in [Instance profile role installation](https://docs.aws.amazon.com/drs/latest/userguide/adding-servers-from-aws-instances.html#Instance-Profile-Role-Installation ).