# Log retention and rotation defaults

This section describes AMS log management defaults; for more information, see
[Log Management](../userguide/log-mgmt.md "../userguide/log-mgmt.md").

- Rotation = Log turnover inside the instances
- Retention = Period of time we keep the logs in Amazon CloudWatch Logs and Amazon Simple Storage Service (S3)
  The logs are retained in CloudWatch Logs as needed (you can configure this), and in S3. They don't
  expire or get deleted and are subject to service durability. For detailed S3 durability information, see
  [Data protection in Amazon S3](../../../AmazonS3/latest/userguide/DataDurability.md "../../../AmazonS3/latest/userguide/DataDurability.md").

You can request a change to log retention for all logs, except AWS CloudTrail logs, which are
kept for 10 years for audit and security reasons.

Log rotation is configured inside the instances. By default, operating system and security logs rotate hourly if they reach over 100MB, this is
done to ensure that you don't run short on disk in the instances.

The log agent inside the instances uploads the log online to CloudWatch Logs, from there the logs are archived to S3.

The logs are stored in CloudWatch Logs and S3 in the raw format they are generated, there is no pre-processing.
