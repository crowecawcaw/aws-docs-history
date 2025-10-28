# Provisioned throughput exception errors

Provisioned throughput exceeded exception errors (HTTP 400) occur when the request
rate for a Kinesis stream surpasses the throughput limits of one or more shards. Each shard
has specific read, and write capacity limits, and exceeding those limits triggers this
exception. Scenarios leading to this exception include: sudden spikes in data ingestion
or consumption, insufficient shard capacity for the data volume being processed, or
uneven distribution of partition keys.

###### Recommendations for handling exceptions

- Implement exponential back-off and re-try mechanisms.
- Increase the number of shards to accommodate higher throughput.
- Ensure that there is proper distribution of partition keys.
- Monitor stream metrics.
  Additionally, using the Kinesis on-demand capacity mode helps to automatically adjust
  workloads, and minimize the occurrence of this exception. For more information, see
  [What is
  AWS Fault Injection Service?](../../../fis/latest/userguide/what-is.md "../../../fis/latest/userguide/what-is.md")

###### Note

Improper distribution issues are outside of on-demand mode capability of automatic scaling.

###### To perform a basic experiment

1. Use baseline metrics: record normal throughput patterns before testing.
2. Create an experiment: use the `aws:kinesis:inject-api-provisioned-throughput-exception` action.
3. Configure the intensity: start with 25% request throttling.
4. Monitor the responses: verify re-try logic with exponential back-off.
5. Validate the scaling: confirm that auto-scaling triggers the activation.
6. Check the alarms: ensure that the `CloudWatch` alarms are running as expected.
   Applications should implement proper back-off strategies, monitor `WriteProvisionedThroughputExceeded`, and `ReadProvisionedThroughputExceeded` metrics, and trigger shard scaling when appropriate.

###### Action details

- **Resource Type**: IAM Role ARN
- **Target Operations**: `PutRecord`,
  `PutRecords`, `GetRecords`
- \***\*Error Code\*\***:
  `ProvisionedThroughputExceededException`(HTTP 400)
- \***\*Description\*\***:
  simulates scenarios where request rate exceeds shard capacity limits, testing
  application throttling, and scaling responses.

###### Parameters

- **IAM Role ARN**: the role that your application uses for Kinesis Data Streams operations.
- **Operations**: target operations: `PutRecord`, `PutRecords`, `GetRecords`.
- **Resource List**: the specific stream names or
  shard identifiers.
- **Duration**: the experiment duration, which is the duration from one minute to 12 hours. In the AWS FIS API, the value is a string in ISO 8601 format. For example, PT1M represents one minute. In the AWS FIS console, you enter the number of seconds, minutes, or hours.
- **Intensity**: the percentage of requests to throttle.

###### Required permissions

- `kinesis:InjectApiError`
  Example experiment template

The following example shows a provisioned throughput exception for all requests up to
5 Kinesis Data streams with the specified tag. AWS FIS selects the streams to affect at
random. After 5 minutes the fault is removed.

```
{
    "description": "Kinesis stream experiment",
    "targets": {
        "KinesisStreams-Target-1": {
            "resourceType": "aws:kinesis:stream",
            "resourceTags": {
                   "tag-key": "tag-value"
            },
            "selectionMode": "COUNT(5)"
        }
    },
    "actions": {
         "kinesis": {
              "actionId": "aws:kinesis:stream-provisioned-throughput-exception",
              "description": "my-stream",
              "parameters": {
                   "duration": "PT5M",
                   "percentage": "100",
                   "service": "kinesis"
              },
              "targets": {
                    "KinesisStreams": "KinesisStreams-Target-1"
              }
         }
   },
   "stopConditions": [
         {
              "source": "none"
         }
   ],
   "roleArn": "arn:aws:iam::111122223333:role/role-name",
   "tags": {},
   "experimentOptions": {
       "accountTargeting": "single-account",
       "emptyTargetResolutionMode": "fail"
   }
}
```

Experiment role permissions example

The following permission allows you to run the `aws:kinesis:stream-provisioned-throughput-exception` and `aws:kinesis:stream-expired-iterator-exception` actions on a specific stream that impact 50% of requests.
