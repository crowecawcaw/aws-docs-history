End of support notice: On May 20, 2026, AWS will end support for
AWS IoT Events. After May 20, 2026, you will no longer be able to access the AWS IoT Events console or AWS IoT Events
resources. For more information, see [AWS IoT Events end of
support](iotevents-end-of-support.md "iotevents-end-of-support.md").

# AWS IoT Events end of support

After careful consideration, we decided to end support for the AWS IoT Events service,
effective May 20, 2026. AWS IoT Events will no longer accept new customers beginning May 20, 2025. As
an existing customer with an account signed up for the service before May 20, 2025, you can
continue to use AWS IoT Events features. After May 20, 2026, you will no longer be able to use
AWS IoT Events.

This page provides instructions and considerations for AWS IoT Events customers to transition to an
alternate solution to meet your business needs.

###### Note

The solutions presented in these guides are meant to serve as an illustrative
examples, not as a production-ready replacements for AWS IoT Events functionality. Customize the
code, workflow, and related AWS resources to your business needs.

###### Topics

- [Considerations when migrating away from
  AWS IoT Events](#eos-considerations "#eos-considerations")
- [Migration procedure for detector models
  in AWS IoT Events](eos-procedure-detector-models.md "eos-procedure-detector-models.md")
- [Migration procedure for AWS IoT SiteWise alarms in
  AWS IoT Events](eos-procedure-alarms.md "eos-procedure-alarms.md")

## Considerations when migrating away from

AWS IoT Events

- Implement security best practices, including using IAM roles with least
  privilege for each component and encrypting data at rest and in transit. For
  more information, see [Security best practices in
  IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.
- Consider the number of shards for the Kinesis stream based on your data ingestion
  requirements. For more information on Kinesis shards, see [Amazon Kinesis Data Streams
  terminology and concepts](../../../streams/latest/dev/key-concepts.md "../../../streams/latest/dev/key-concepts.md") in the
  _Amazon Kinesis Data Streams Developer Guide_.
- Set up comprehensive monitoring and debugging using CloudWatch for metrics and logs.
  For more information, see [What is
  CloudWatch?](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md") in the _Amazon CloudWatch User Guide_.
- Consider the structure of your error handling, including how to manage
  messages that fail processing repeatedly, implementing retry policies, and
  setting up a process to isolate and analyze problematic messages.
- Use the [AWS Pricing Calculator](https://calculator.aws "https://calculator.aws")
  to estimate costs for your specific use case.
