# Auditing CloudWatch telemetry configurations

You can use Amazon CloudWatch to discover and understand the state of telemetry configuration for your
 AWS resources from a central view in the CloudWatch console. This simplifies the process of auditing
 your telemetry collection configurations across multiple resource types within an account or
 across multiple accounts in AWS Organizations. With a consolidated view, you can easily review and manage
 telemetry settings, helping you to ensure proper monitoring and data collection across your AWS
 environment.

CloudWatch Telemetry config can be used to audit telemetry for the following types of AWS
 resource types:


* Amazon EC2 instances that provide detailed metrics. For more information, see  [Manage
 detailed monitoring for your EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/manage-detailed-monitoring.html "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/manage-detailed-monitoring.html") in the*Amazon EC2 User Guide.*
* Amazon VPC virtual networks that provide flow logs. For more information, see  [Logging IP traffic using VPC
 Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html "https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html") in the *Amazon VPC User Guide*.
* Lambda functions that provide traces. For more information, see  [Visualize Lambda function invocations using
 AWS X-Ray](https://docs.aws.amazon.com/lambda/latest/dg/services-xray.html "https://docs.aws.amazon.com/lambda/latest/dg/services-xray.html") in the *AWS X-Ray Developer Guide*.
To begin auditing and configuring your telemetry, you must first enable the telemetry
 configuration feature for your AWS account or organization. Enabling this feature creates
 AWS Config service-linked configuration recorders that discover resources and their
 associated telemetry configuration metadata. For more information, see [Configuration
 Recorder](https://docs.aws.amazon.com/config/latest/developerguide/config-concepts.html#config-recorder "https://docs.aws.amazon.com/config/latest/developerguide/config-concepts.html#config-recorder") in the AWS Config Developer Guide.

###### Note

AWS Config periodically takes inventory of, or discovers, all the resources in
 your account as an anti-entropy behavior, regardless of the resource types in scope for your
 configuration recorders. The inventory includes deleted resources and resources that
 AWS Config is not currently recording. This behavior helps maintain data
 consistency.

This means that although the service-linked configuration recorder for the CloudWatch telemetry
 configuration feature is configured to record three resource types (Amazon EC2 instances, Amazon EC2 VPC
 virtual networks, and Lambda functions), you might see describe calls from
 `ConfigResourceCompositionSession` and `AWSConfig-Describe` in AWS CloudTrail.
 For more information, see [Non-recorded Resources](https://docs.aws.amazon.com/config/latest/developerguide/select-resources.html#select-resources-non-recorded "https://docs.aws.amazon.com/config/latest/developerguide/select-resources.html#select-resources-non-recorded") in the AWS Config Developer Guide.

Telemetry config uses this information and offers visibility into the configuration status,
 at the resource type level and at more granular telemetry detail levels. You can customize your
 view of the resources or telemetry details using filters, and modify the telemetry configuration
 directly from the resource's console page.

You can enable **Telemetry config** at no additional cost. 
When you use enablement rules to automatically manage telemetry, AWS Config charges apply based on the number of configuration
 items recorded for the resource types you specify in the enablement rule. For more information, see [AWS Config pricing](https://aws.amazon.com/config/pricing/ "https://aws.amazon.com/config/pricing/").

###### Topics

* [Turning on telemetry auditing](telemetry-config-turn-on.md "telemetry-config-turn-on.md")
* [Viewing AWS resource telemetry in
 CloudWatch](telemetry-config-view-resources.md "telemetry-config-view-resources.md")
* [Working with telemetry enablement rules](telemetry-config-rules.md "telemetry-config-rules.md")
* [Turning off CloudWatch telemetry configuration](telemetry-config-turn-off.md "telemetry-config-turn-off.md")
