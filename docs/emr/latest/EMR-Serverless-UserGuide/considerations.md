# Other considerations

The following list contains other considerations with EMR Serverless.

- EMR Serverless is available in the following AWS Regions:

      + US East (Ohio)
      + US East (N. Virginia)
      + US West (N. California)
      + US West (Oregon)
      + Africa (Cape Town)
      + Asia Pacific (Hong Kong)
      + Asia Pacific (Jakarta)
      + Asia Pacific (Mumbai)
      + Asia Pacific (Osaka)
      + Asia Pacific (Seoul)
      + Asia Pacific (Singapore)
      + Asia Pacific (Sydney)
      + Asia Pacific (Tokyo)
      + Canada (Central)
      + Europe (Frankfurt)
      + Europe (Ireland)
      + Europe (London)
      + Europe (Milan)
      + Europe (Paris)
      + Europe (Spain)
      + Europe (Stockholm)
      + Middle East (Bahrain)
      + Middle East (UAE)
      + South America (São Paulo)
      + AWS GovCloud (US-East)
      + AWS GovCloud (US-West)

  For a list
  of endpoints associated with these Regions, refer to [Service endpoints](endpoints-quotas.md#endpoints "endpoints-quotas.md#endpoints").

- The default timeout for a job run is 12 hours. You can change this setting with the
  `executionTimeoutMinutes` property in the `startJobRun` API or the AWS SDK.
  You can set `executionTimeoutMinutes` to 0 if you want your job run to never time
  out. For example, if you have a streaming application, set
  `executionTimeoutMinutes` to 0 to allow the streaming job to run
  continuously.
- The `billedResourceUtilization` property in the `getJobRun` API shows
  the aggregate vCPU, memory, and storage that AWS has billed for the job run. Billed
  resources include a 1-minute minimum usage for workers, plus additional storage over 20 GB
  per worker. These resources don't include usage for idle pre-initialized workers.
- Without VPC connectivity, a job can access some AWS service endpoints in the same
  AWS Region. These services include Amazon S3, AWS Glue, AWS Lake Formation, Amazon CloudWatch Logs, AWS KMS, AWS Security Token Service,
  Amazon DynamoDB, and AWS Secrets Manager. You can enable VPC connectivity to access other
  AWS services through [AWS PrivateLink](../../../vpc/latest/privatelink/what-is-privatelink.md "../../../vpc/latest/privatelink/what-is-privatelink.md"), but you aren't
  required to do this. To access external services, create your application with a
  VPC.
- EMR Serverless doesn't support HDFS. The local disks on workers are temporary storage that
  EMR Serverless uses to shuffle and process data during job runs.
