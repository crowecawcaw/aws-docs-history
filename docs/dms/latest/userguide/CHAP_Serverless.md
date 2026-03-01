# AWS DMS Serverless limitations

AWS DMS Serverless has the following limitations:

- You can only modify an AWS DMS replication configuration that is in the `CREATED`,
  `STOPPED`, or `FAILED` states. For details about which settings you can
  change under which conditions, see [Modifying AWS DMS serverless replications](CHAP_Serverless.md#CHAP_Serverless.modify "CHAP_Serverless.md#CHAP_Serverless.modify").
- You can only delete an AWS DMS replication configuration that is in the
  `STOPPED`, or `FAILED` states.
- Unlike replication instances, AWS DMS Serverless replications do not have a public IP address for management tasks.
  You manage serverless replications using the console.
- This release of AWS DMS serverless does not support all the source and target endpoint types that AWS DMS standard
  supports. For a list of supported engine types, see [AWS DMS Serverless components](CHAP_Serverless.md "CHAP_Serverless.md").
- Serverless replications need to access dependencies by using VPC endpoints. You must use VPC endpoints to access the
  following endpoint types:

      + Amazon Amazon S3
      + Amazon Kinesis
      + AWS Secrets Manager
      + Amazon DynamoDB
      + Amazon Redshift
      + Amazon OpenSearch Service

  For information about setting up VPC endpoints, see [Configuring VPC endpoints for AWS DMS](CHAP_VPC_Endpoints.md "CHAP_VPC_Endpoints.md").

- AWS DMS serverless does not support views.
- AWS DMS Serverless does not support SSL connections for DB2 endpoints.
- AWS DMS Serverless does not support setting custom CDC start points.
- When a replication task is in deprovisioned state, the metadata related to the
  table and the replication statistics are lost.
