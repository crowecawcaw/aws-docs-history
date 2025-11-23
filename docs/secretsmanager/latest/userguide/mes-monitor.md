# Monitor and troubleshoot managed external secrets

Managed external secrets provide comprehensive monitoring capabilities through
AWS CloudTrail logs and Amazon CloudWatch metrics. All rotation activities are logged with
detailed information about success, failure, and any errors encountered during the
process.

Common issues in the rotation workflow include an incorrect configuration of role permissions or the secret value.
Failure to set these fields is the format specified by the integration partners can cause rotation failures,
as the service will be unable to access the secret or connect with the integration partner client to update the secret.
Other issues could be network connectivity problems, credential expiration, or partner service availability.
The managed rotation service includes retry logic and error handling to maximize reliability

You can monitor rotation schedules, success rates, and performance metrics through Amazon CloudWatch.
You can configure custom alarms through [event bridge](../../../eventbridge/latest/userguide/eb-create-pattern.md "../../../eventbridge/latest/userguide/eb-create-pattern.md") to alert you of rotation failures or other issues that require attention.
