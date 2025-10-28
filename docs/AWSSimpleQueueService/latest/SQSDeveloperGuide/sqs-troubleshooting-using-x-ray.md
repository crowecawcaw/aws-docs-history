# Troubleshooting Amazon Simple Queue Service queues using

AWS X-Ray

AWS X-Ray collects data about requests that your application serves and lets you view and
filter data to identify potential issues and opportunities for optimization. For any traced
request to your application, you can see detailed information about the request, the response,
and the calls that your application makes to downstream AWS resources, microservices,
databases and HTTP web APIs.

To send AWS X-Ray trace headers through Amazon SQS, you can do one of the following:

- Use the `X-Amzn-Trace-Id`
  [tracing
  header](../../../xray/latest/devguide/xray-concepts.md#xray-concepts-tracingheader "../../../xray/latest/devguide/xray-concepts.md#xray-concepts-tracingheader").
- Use the `AWSTraceHeader`
  [message system attribute](sqs-message-metadata.md#sqs-message-system-attributes "sqs-message-metadata.md#sqs-message-system-attributes").
  To collect data on errors and latency, you must instrument the [`AmazonSQS`](../../../sdk-for-java/latest/reference/index.md "../../../sdk-for-java/latest/reference/index.md") client using the [AWS X-Ray SDK](../../../xray-sdk-for-java/latest/javadoc/index.md "../../../xray-sdk-for-java/latest/javadoc/index.md").

You can use the AWS X-Ray console to view the map of connections between Amazon SQS and other
services that your application uses. You can also use the console to view metrics such as
average latency and failure rates. For more information, see [Amazon SQS and AWS X-Ray](../../../xray/latest/devguide/xray-services-sqs.md "../../../xray/latest/devguide/xray-services-sqs.md") in the
_AWS X-Ray Developer Guide_.
