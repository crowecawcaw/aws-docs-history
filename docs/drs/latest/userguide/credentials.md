# Generating the required AWS credentials

In order to install the AWS Replication Agent, you must first generate the required AWS
credentials. You can create temporary credentials with AWS STS.

## Temporary credentials

Before you install the AWS Replication Agent, you need to generate temporary AWS security credentials.
The temporary credentials provided by AWS Elastic Disaster Recovery utilize a similar mechanism to the one used by
[IAM Roles Anywhere](../../../rolesanywhere/latest/userguide/introduction.md "../../../rolesanywhere/latest/userguide/introduction.md").

To create temporary credentials, take the following steps:

1. [Create a
   new IAM Role](../../../IAM/latest/UserGuide/id_roles_create.md "../../../IAM/latest/UserGuide/id_roles_create.md") with the **AWSElasticDisasterRecoveryAgentInstallationPolicy** policy.
2. Request temporary security credentials [via AWS STS](../../../IAM/latest/UserGuide/id_credentials_temp_request.md "../../../IAM/latest/UserGuide/id_credentials_temp_request.md")
   using the [AssumeRole API](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md").

[Learn more about how temporary
credentials work.](Agent-Related-FAQ.md#temporary-credentials-operation "Agent-Related-FAQ.md#temporary-credentials-operation")

###### Note

You can also create the default IAM role with the required permissions as an instance profile, as described in [Instance profile role installation](adding-servers-from-aws-instances.md#Instance-Profile-Role-Installation "adding-servers-from-aws-instances.md#Instance-Profile-Role-Installation").
