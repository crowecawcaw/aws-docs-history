# Use AMS SSP to provision Amazon EventBridge in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access Amazon EventBridge capabilities directly in your AMS managed account. Amazon EventBridge is a serverless event bus service that makes it easy to connect your applications with
data from a variety of sources. EventBridge delivers a stream of real-time data from your own
applications, Software-as-a-Service (SaaS) applications, and AWS services and routes that data to
targets such as AWS Lambda. You can set up routing rules to determine where to send your data to
build application architectures that react in real time to all of your data sources. EventBridge
allows you to build event driven architectures, which are loosely coupled and distributed.

To learn more, see [Amazon EventBridge](https://aws.amazon.com/eventbridge/ "https://aws.amazon.com/eventbridge/").

## EventBridge in AWS Managed Services FAQ

**Q: How do I request access to EventBridge in my AMS account?**

Request access to EventBridge by submitting an RFC with the Management | AWS
service | Self-provisioned service | Add (ct-1w8z66n899dct) change type.
This RFC provisions the following IAM roles to your account: `customer_eventbridge_role` and `customer_eventbridge_scheduler_execution_role`. After it's provisioned in your account, you must onboard the role in your federation solution.

The execution role, `customer_eventbridge_scheduler_execution_role` is an IAM role that EventBridge Scheduler assumes to interact with other AWS services on your behalf. The permission policies attached to this role grant EventBridge Scheduler access to invoke targets.

###### Note

By default, EventBridge Scheduler uses AWS owned keys for EventBridge to encrypt the data. To use a customer managed key for EventBridge to encrypt the data, submit the RFC using the Management | AWS service | Self-provisioned service | [Add (managed automation)](../ctref/management-aws-self-provisioned-service-add-review-required.md "../ctref/management-aws-self-provisioned-service-add-review-required.md") change type (ct-3qe6io8t6jtny) for service provisioning.

**Q: What are the restrictions to using EventBridge in my AMS account?**

You must submit AMS RFCs and create the following resources: Service
roles to trigger the batch job, SQS queue, CodeBuild, CodePipeline, and SSM commands.

**Q: What are the prerequisites or dependencies to using EventBridge in my AMS account?**

You must request an EventBridge service role with an RFC using the Deployment | Advanced stack components | Identity and Access Management (IAM) | Create entity or policy (managed automation) change type (ct-3dpd8mdd9jn1r) prior to using EventBridge
to trigger other AWS resources, such as AWS Batch, Lambda, Amazon SNS, Amazon SQS, or Amazon CloudWatch Logs resources. Specify the services
to invoke when requesting your service role. To learn about permissions
required to invoke targets, see
[Using Resource-Based Policies for EventBridge](../../../eventbridge/latest/userguide/resource-based-policies-eventbridge.md "../../../eventbridge/latest/userguide/resource-based-policies-eventbridge.md").

EventBridge is integrated with AWS CloudTrail, a service that provides a
record of actions taken by a user, role, or an AWS service in EventBridge.
CloudTrail must be enabled and allowed to store the log files to S3
buckets. Note: All AMS accounts have CloudTrail enabled, so no action is
needed.

**Q: The role customer_eventbridge_scheduler_execution_role has a prerequisite for an AWS Key Management Service Key (optional, if used for encryption). How do I adopt AWS KMS CMKs in data encryption at rest/transit?**

By default, EventBridge Scheduler encrypts event metadata and message data that it stores under an AWS owned key (encryption at rest). EventBridge Scheduler also encrypts data that passes between EventBridge Scheduler and other services using Transport Layer Security (TLS) (encryption in transit).

If your specific use case requires that you control and audit the encryption keys that protect your data on EventBridge Scheduler, you can use a customer managed key.

You must request an RFC using the Management | AWS service | Self-provisioned service | Add (managed automation) change type prior to using Amazon EventBridge to onboard the AWS KMS permission.
