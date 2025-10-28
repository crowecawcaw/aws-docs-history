# AWS services commonly used with

Amazon SNS

Integrate Amazon SNS with multiple AWS Cloud services to boost message handling, improve
access control, enable event-driven processing, and automate resources. This integration
optimizes performance, strengthens security, and streamlines operations.

**Amazon CloudWatch**

Amazon CloudWatch provides monitoring and observability for Amazon SNS, helping you
track message delivery, detect anomalies, and troubleshoot issues. With
CloudWatch, you can:

- **Monitor Amazon SNS metrics** such as the
  number of messages published, delivered, or failed across topics and
  subscriptions.
- **Set up CloudWatch Alarms** to trigger
  automated actions when Amazon SNS metrics exceed predefined thresholds,
  such as high delivery failures or throttling.
- **Use CloudWatch Logs to capture Amazon SNS delivery
  status** for messages sent to HTTP/S, Lambda, and Amazon SQS
  endpoints for debugging and auditing.

For more information, see [Monitoring Amazon SNS topics using
CloudWatch](sns-monitoring-using-cloudwatch.md "sns-monitoring-using-cloudwatch.md").

**Amazon SQS**

Amazon SQS is a fully managed message queuing service that enables secure,
durable, and scalable communication between distributed software components.
It helps decouple application architecture by buffering messages, ensuring
reliable delivery, and preventing system failures due to message loss. Amazon SQS
integrates with Amazon SNS in the following ways:

- [Dead-letter queues](sns-dead-letter-queues.md "sns-dead-letter-queues.md") – Amazon SNS can
  route undeliverable messages to an Amazon SQS dead-letter queue for
  troubleshooting and reprocessing.
- [Topic
  subscriptions](sns-sqs-as-subscriber.md "sns-sqs-as-subscriber.md") – You can subscribe
  an Amazon SQS queue to an Amazon SNS topic, allowing Amazon SNS to fan out messages
  to multiple consumers using Amazon SQS.
- [**FIFO queue support**](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-fifo-queues.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-fifo-queues.md")
  – Amazon SQS FIFO queues can be subscribed to Amazon SNS FIFO topics,
  ensuring strict message ordering and exactly-once processing. [Standard Amazon SQS queues](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues.md") can also subscribe to Amazon SNS
  topics but do not guarantee ordered message delivery or
  deduplication.

**AWS CloudFormation**

AWS CloudFormation automates the provisioning and management of AWS resources,
including Amazon SNS topics and subscriptions, using infrastructure as code
(IaC). With AWS CloudFormation, you can:

- **Define Amazon SNS topics, subscriptions, and
  permissions** in a reusable, version-controlled
  template.
- **Ensure consistent deployment** of
  Amazon SNS resources across multiple AWS accounts and Regions.
- **Update or modify Amazon SNS
  configurations** using change sets without manual
  intervention.

For more information, see the [AWS CloudFormation User Guide](../../../AWSCloudFormation/latest/UserGuide.md "../../../AWSCloudFormation/latest/UserGuide.md").

**AWS CloudTrail**

CloudTrail provides visibility into API activity for Amazon SNS, helping you monitor
and audit access to Amazon SNS topics, subscriptions, and messages. With CloudTrail,
you can:

- **Track API calls made to Amazon SNS**,
  including who accessed or modified topics, subscriptions, and
  permissions.
- **Detect unauthorized or unexpected
  activity** by analyzing logs for security and
  compliance purposes.
- **Integrate with Amazon CloudWatch or
  AWS Security Hub** to create alerts based on unusual Amazon SNS
  actions.

For more information, see the [Logging AWS SNS API calls using
AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md").

**AWS Lambda**

AWS Lambda is a serverless compute service that automatically runs your
code in response to events, eliminating the need to provision or manage
servers. It allows you to build event-driven applications that scale
automatically and execute in a highly available compute environment.

Amazon SNS integrates with Lambda by allowing you to subscribe a Lambda function
to an Amazon SNS topic. When an Amazon SNS topic receives a message, it can trigger
the Lambda function, enabling real-time processing, automation, and
application logic execution. This integration is commonly used for:

- [**Event-driven
  processing**](../../../lambda/latest/dg/concepts-event-driven-architectures.md "../../../lambda/latest/dg/concepts-event-driven-architectures.md") – Automatically trigger
  functions in response to Amazon SNS messages.
- [**Data
  transformation**](../../../lambda/latest/dg/concepts-event-driven-architectures.md "../../../lambda/latest/dg/concepts-event-driven-architectures.md") – Modify or filter
  Amazon SNS messages before forwarding them to other services.
- **Automated workflows** –
  Process notifications for application alerts, system monitoring, or
  event orchestration.

**AWS Identity and Access Management (IAM)**

IAM provides secure access control for AWS resources, allowing you to
manage who can access your Amazon SNS topics, what actions they can perform, and
under what conditions. With IAM, you can:

- **Authenticate users and services**
  before they can interact with Amazon SNS topics.
- **Define fine-grained permissions**
  to specify which Amazon SNS topics users or roles can publish to,
  subscribe to, or manage.
- **Use identity-based policies** to
  enforce security best practices, such as restricting access to
  specific AWS accounts, IP addresses, or conditions.

For more information, see [Using identity-based policies with
Amazon SNS](sns-using-identity-based-policies.md "sns-using-identity-based-policies.md").

**AWS Key Management Service (AWS KMS)**

AWS KMS enhances the security of Amazon SNS by enabling server-side encryption
(SSE) for message confidentiality. With AWS KMS, you can:

- **Encrypt Amazon SNS messages at rest**
  using AWS-managed or customer-managed encryption keys
  (CMKs).
- **Control access to Amazon SNS topics** by
  defining fine-grained key policies that restrict who can publish or
  subscribe.
- **Ensure compliance with security and
  regulatory requirements** by auditing key usage through
  AWS CloudTrail.

For more information, see [Managing Amazon SNS encryption keys and costs](sns-key-management.md "sns-key-management.md").

**AWS X-Ray**

X-Ray provides tracing for Amazon SNS, helping you analyze and debug the flow
of messages through your event-driven architecture. With X-Ray, you
can:

- **Trace Amazon SNS message delivery**
  across multiple AWS services, such as Lambda, Amazon SQS, and HTTP/S
  endpoints.
- **Identify latency bottlenecks** by
  visualizing how long messages take to be published, delivered, and
  processed.
- **Detect errors and retries** in
  Amazon SNS message flows to troubleshoot failed deliveries or slow
  processing times.

For more information, see [Active tracing in Amazon SNS](sns-active-tracing.md "sns-active-tracing.md").
