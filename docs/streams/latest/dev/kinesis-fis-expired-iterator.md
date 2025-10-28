# Expired iterator exception errors

Expired iterator exception errors (HTTP 400) occur when the shard iterator is
expired, and is no longer used to retrieve stream records when calling
`GetRecords`. This occurs when there are delays between read operations,
which are caused by long-running data processing tasks, network issues, or application
downtime.

###### Note

A shard iterator is valid for 5 minutes after the time it's issued.

###### Recommendations for handling exceptions

- Refreshing shard iterators before they expire.
- Incorporating error handling to obtain new iterators.
- Utilizing the Kinesis Kinesis Client Library (KCL) which automatically manages shard
  iterator expiration.
  For more information, see [What is AWS Fault Injection Service?](../../../fis/latest/userguide/what-is.md "../../../fis/latest/userguide/what-is.md")

###### To perform a basic experiment

1. Create an experiment template: use the AWS FIS console.
2. Select the action: use the
   `aws:kinesis:inject-api-expired-iterator-exception`
   action.
3. Configure the targets: specify the IAM role and Kinesis Data Streamsoperations.
4. Set the duration: start with 5-10 minutes for initial testing.
5. Add stop conditions: [stop conditions for AWS FIS](../../../fis/latest/userguide/stop-conditions.md "../../../fis/latest/userguide/stop-conditions.md").
6. Run the experiment: monitor the application behavior.

###### Action details

- **Resource Type**: IAM Role ARN
- **Target Operations**:
  `GetRecords`
- \***\*Error Code\*\***:
  `ExpiredIteratorException`(HTTP 400)
- \***\*Description\*\***:
  the provided iterator exceeds the maximum age allowed, simulating scenarios
  where record processing is too slow or checkpointing logic fails.

###### Parameters

- **IAM Role ARN**: the role that your application uses for Kinesis Data Streams operations.
- **Operations**: target operations:
  `GetRecords`
- **Resource List**: the specific stream names or
  ARNs.
- **Duration**: the experiment duration. This is
  configurable.
- **Intensity**: the percentage of requests to throttle.

###### Required permissions

- `kinesis:InjectApiError`
