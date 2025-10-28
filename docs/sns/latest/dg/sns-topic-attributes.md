# Amazon SNS message delivery status

Amazon SNS provides support for logging the delivery status of notification messages sent to
topics with the following Amazon SNS endpoints:

- Amazon Data Firehose
- Amazon Simple Queue Service
- AWS Lambda
- HTTPS
- Platform application endpoint
  Delivery status logs are sent to Amazon CloudWatch Logs, providing insights into message delivery
  operations. These logs help you:

- Determine whether a message was successfully delivered to an endpoint.
- Identify the response from the endpoint to Amazon SNS.
- Measure message dwell time (time between publish timestamp and handoff to the
  endpoint).
  You can configure delivery status logging using the AWS Management Console, AWS SDKs, Query API, or
  AWS CloudFormation.
