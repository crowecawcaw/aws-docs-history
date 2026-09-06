

# Generating IAM credentials and configuring CloudWatch logging
<a name="failback-failover-drsfa-credentials"></a>

The DRSFA client requires AWS credentials to operate.

**Important**  
Temporary credentials are the recommended option. They do not require rotation, cannot be reused after expiration, and provide enhanced security. You can specify how long they remain valid, up to a maximum limit.

## Temporary credentials
<a name="credentials-failback-failover-temporary"></a>

To create temporary credentials:

1. [Create a new IAM Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html) with the [AWSElasticDisasterRecoveryFailbackInstallationPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSElasticDisasterRecoveryFailbackInstallationPolicy.html) policy.

1. Request temporary security credentials [through AWS STS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html) using the [AssumeRole API](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html).

## Configuring CloudWatch logging
<a name="failback-failover-drsfa-cloudwatch"></a>

After generating credentials, create a CloudWatch log group named **DRS\_Mass\_Failback\_Automation**. If this log group does not exist or has the wrong name, the DRSFA client still works but does not send logs to CloudWatch. Learn more about working with log groups in the [Amazon CloudWatch Logs documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html).