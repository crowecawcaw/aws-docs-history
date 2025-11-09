# Monitoring an integration

## Integration states

The following integration states describe the integration:

- `Creating` - The integration is being created.
- `Active` - The integration is sending transactional data to the target.
- `Modifying` - The integration is being modified.
- `Syncing` - The integration has encountered a recoverable error and is re-seeding data.
- `Needs attention` - The integration encountered an event or error that requires manual intervention to resolve it. To fix the issue, follow the instructions in the error message on the integration details.
- `Failed` - The integration encountered an unrecoverable event or error. You must delete and recreate the integration.
- `Deleting` - The integration is being deleted.

## Viewing Amazon CloudWatch logs for an integration

AWS Glue zero-ETL integrations generate Amazon CloudWatch logs for visibility into your data movement. Log events relating to each successful ingestion or any failures experienced due to problematic data records at source, or data write errors due to schema changes or insufficient permissions are emitted to a default log group created in a customer account.

For each integration created, the log events for that integration will be collected under `/aws-glue/zeroETL-integrations/logs/` in Amazon Cloudwatch. Inside the log group, log messages will be split into log streams. Each integration created has a dedicated log stream to where all logs for that integration are written. For example, logs for an integration with IntegrationArn `arn:aws:glue:us-east-1:123456789012:integration:03cabe77-79e7-4b7a-b3da-8c160bea6bbf` can be found under /aws-glue/zeroETL-integrations/logs/03cabe77-79e7-4b7a-b3da-8c160bea6bbf. {IntegrationId} can be referenced from the {integrationArn} generated when an integration is created.

###### Note

For a cross-account scenario, source processing Logs are emitted in the source account where the integration exists and target processing logs are emitted in the target account where the target database exists.

### IAM permissions required to enable logging

When creating your integration, the following IAM permissions are needed by the source and target roles to enable CloudWatch logging for an integration. AWS Glue zero-ETL integrations use these permissions provided in the source and target roles to emit CloudWatch logs to customer accounts.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogGroup",
 "logs:CreateLogStream",
 "logs:PutLogEvents"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

### Log messages

Log format: zero-ETL integrations emit four types of log messages:

```
// Ingestion started
{
"integrationArn": "arn:aws:glue:us-east-2:123456789012:integration/1a012bba-123a-1bba-ab1c-173de3b12345",
...
    "messageType": "IngestionStarted",
    "details": {
        "tableName": "testDDBTable",
        "message": "Ingestion Job started"
    }
}
// Data processing stats on successful table ingestion
{
...
    "messageType": "IngestionProcessingStats",
    "details": {
        "tableName": "testDDBTable",
        "insert_count": 100,
        "update_count": 10,
        "delete_count": 10
    }
}
// Ingestion failure logs for failed table-processing
{
...
    "messageType": "IngestionFailed",
    "details": {
        "tableName": "testDDBTable",
        "errorMessage": "Failed to ingest data with error: Target Glue database not found.",
        "error_code" : "client_error"
    }
}
// Ingestion completed notification with lastSyncedTimestamp
{
...
    "messageType": "IngestionCompleted",
    "details": {
        "tableName": "testDDBTable",
        "message": "Ingestion Job completed"
        "lastSyncedTimestamp": "1132344255745"
    }
}
```

## Viewing Amazon CloudWatch metrics for an integration

Once an integration completes, you can see these Amazon Cloudwatch metrics generated in your account for each AWS Glue job run:

CloudWatch metrics namespace: "AWS/Glue/ZeroETL"

Metrics dimensions:

- `integrationArn`
- `loadType`
- `tableName`

Metric names:

- `InsertCount` - number of records inserted in the target Iceberg table.
- `UpdateCount` - number of records updated in the target Iceberg table.
- `DeleteCount` - number of records deleted from the target Iceberg table.
- `IngestionSucceeded` - count 1, if the ingestion succeeded for the integration.
- `IngestionFailed` - count 1, if the ingestion failed for the integration.
- `LastSyncTimestamp` - timestamp until which source has been synced to target.

## Managing event notifications with Amazon EventBridge

Zero-ETL integrations use Amazon EventBridge to manage event notifications to keep you up-to-date regarding changes in your integrations. Amazon EventBridge is a serverless event bus service that you can use to connect your applications with data from a variety of sources. In this case, the event source is AWS Glue. Events, which are monitored changes in an environment, are sent to EventBridge from AWS Glue automatically. Events are delivered in near real time.

EventBridge provides an environment for you to write event rules, which can specify actions to take for specific events. You can also set up targets, which are resources that EventBridge can send an event to. A target can include an API destination, an Amazon CloudWatch log group, and others. For more information about rules, see [Amazon EventBridge rules](../../../eventbridge/latest/userguide/eb-rules.md "../../../eventbridge/latest/userguide/eb-rules.md"). For more information about targets, see [Amazon EventBridge targets](../../../eventbridge/latest/userguide/eb-targets.md "../../../eventbridge/latest/userguide/eb-targets.md").

To capture all Zero-ETL notifications, create an Eventbridge rule which matches the following:

```
{
  "source": [{
    "prefix": "aws.glue-zero-etl“
  }],
  "detail-type": [{
    "prefix": "Glue Zero ETL“
  }]
}

```

The following table includes zero-ETL integration events, with additional
metadata:

| Customer-facing detail type                   | Explanation                                                                                                |
| --------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| AWS Glue Zero ETL Ingestion Completed         | Individual execution for an entity has completed<br>successfully.                                          |
| AWS Glue Zero ETL Ingestion Failed            | Individual execution for an entity has completed<br>unsuccessfully (either with a client or system error). |
| AWS Glue Zero ETL Integration Resynced        | Integration has been RESYNCED.                                                                             |
| AWS Glue Zero ETL Integration Failed          | Integration status has changed to FAILED due to an<br>error.                                               |
| AWS Glue Zero ETL Integration Needs Attention | Integration status has changed to NEEDS_ATTENTION due to an<br>error.                                      |
| AWS Glue Zero ETL Ingestion In Progress       | Individual execution for an entity has made partial progress towards completion.                           |
