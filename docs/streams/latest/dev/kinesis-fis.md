# Perform resilience testing with AWS Fault Injection Service

AWS Fault Injection Service is a fully managed service that helps you perform fault injection experiments on your AWS workloads. AWS FIS integration with Amazon Kinesis Data Streams enables you to test your application resilience against common Amazon Kinesis Data Streams API errors in a controlled environment. This capability allows you to validate error handling, retry logic, and monitor systems before encountering failures. For more information, see [What is AWS Fault Injection Service?](../../../fis/latest/userguide/what-is.md "../../../fis/latest/userguide/what-is.md").

###### Actions

- API internal error: This injects internal errors into requests made by the the
  target IAM role. The specific response depends on each service and API. The action
  `aws:fis:inject-api-internal-error` creates
  `InternalFailure` errors (HTTP 500).
- API throttle error: This injects internal errors into requests made by the the
  target IAM role. The specific response depends on each service and API. The action
  `aws:fis:inject-api-throttle-error` creates
  `ThrottlingException` errors (HTTP 400).
- API unavailable error: This injects internal errors into requests made by the the
  target IAM role. The specific response depends on each service and API. The action
  `aws:fis:inject-api-unavailable-error` creates
  `ServiceUnavailable` errors (HTTP 503).
- API provisioned throughput exception: This injects internal errors into requests
  made by the the target IAM role. The specific response depends on each service and
  API. The action `aws:kinesis:inject-api-provisioned-throughput-exception`
  creates `ProvisionedThroughputExceededException` errors (HTTP
  400).
- API expired iterator exception: This injects internal errors into requests made by
  the the target IAM role. The specific response depends on each service and API. The
  action `aws:kinesis:inject-api-expired-iterator-exception` creates
  `ExpiredIteratorException` errors (HTTP 400).
  For more information, see [Amazon Kinesis Data Streams actions](../../../fis/latest/userguide/fis-actions-reference.md#aws-kinesis-actions "../../../fis/latest/userguide/fis-actions-reference.md#aws-kinesis-actions").

###### Considerations

- You can use actions above with both provisioned, and on-demand offerings for Amazon Kinesis Data Streams.
- Your streaming resumes once the experiment completes based on the duration
  selected. You can also stop a running experiment before it completes. Alternatively,
  you can define a stop condition to stop the experiment based on alarms that define
  the application health in a Amazon CloudWatch Application Insights.
- You can test up to 280 streams.
  For more information on regional support, see [AWS Fault Injection Service endpoints and quotas](../../../general/latest/gr/fis.md "../../../general/latest/gr/fis.md").
