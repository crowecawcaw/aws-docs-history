# Generating IAM credentials and configuring CloudWatch logging

The DRSFA client requires AWS credentials to operate.

###### Important

Temporary credentials are the recommended option. They do not require rotation,
cannot be reused after expiration, and provide enhanced security. You can specify how
long they remain valid, up to a maximum limit.

## Temporary credentials

To create temporary credentials:

1. [Create a new
   IAM Role](../../../IAM/latest/UserGuide/id_roles_create.md "../../../IAM/latest/UserGuide/id_roles_create.md") with the [AWSElasticDisasterRecoveryFailbackInstallationPolicy](../../../aws-managed-policy/latest/reference/AWSElasticDisasterRecoveryFailbackInstallationPolicy.md "../../../aws-managed-policy/latest/reference/AWSElasticDisasterRecoveryFailbackInstallationPolicy.md")
   policy.
2. Request temporary security credentials [through
   AWS STS](../../../IAM/latest/UserGuide/id_credentials_temp_request.md "../../../IAM/latest/UserGuide/id_credentials_temp_request.md") using the [AssumeRole
   API](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md").

## Configuring CloudWatch logging

After generating credentials, create a CloudWatch log group named
**DRS_Mass_Failback_Automation**. If this log group does
not exist or has the wrong name, the DRSFA client still works but does not send logs to
CloudWatch. Learn more about working with log groups in the [Amazon
CloudWatch Logs documentation](../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md "../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md").
