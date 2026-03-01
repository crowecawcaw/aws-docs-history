# Audit and turn on AWS telemetry related configurations

You can use Amazon CloudWatch to discover and audit the state of telemetry configuration and be able
to create a rule to enable telemetry for popular AWS resource types from a central view in the
CloudWatch console. The experience provides a view to audit your telemetry configurations within an
account or across multiple accounts in AWS Organizations using the AWS Organizations
Management or CloudWatch Delegated Admin Account, helping you to ensure proper monitoring and data
collection across your AWS environment.

CloudWatch Ingestion can be used to audit and configure telemetry for popular AWS Log Sources such as
Amazon VPC Flow Logs (Auditing and Configuration Available), AWS WAF Logs (Auditing and Configuration Available),
Amazon Route 53 Resolver Query Logs (Auditing and Configuration Available), Amazon NLB (Configuration Available),
Amazon EKS Control Plane Logs (Auditing and Configuration Available),
AWS CloudTrail Data Events and Management Events (Configuration Available),
and Amazon Bedrock AgentCore Logs (Configuration Available).

To begin auditing and configuring your telemetry, you must enable trusted access for CloudWatch for
your AWS organization and then enable the telemetry configuration experience feature for your
AWS account or organization. Enabling this feature creates AWS Config
service-linked configuration recorders that discover resources and their associated telemetry
configuration metadata. For more information, see [Configuration
Recorder](../../../config/latest/developerguide/config-concepts.md#config-recorder "../../../config/latest/developerguide/config-concepts.md#config-recorder") in the AWS Config Developer Guide.

###### Note

AWS Config periodically takes inventory of, or discovers, all the resources in
your account as an anti-entropy behavior, regardless of the resource types in scope for your
configuration recorders. The inventory includes deleted resources and resources that
AWS Config is not currently recording. This behavior helps maintain data
consistency.

This means that although the service-linked configuration recorder for the CloudWatch telemetry
configuration feature is configured to record specific resource types, you might see describe
calls from `ConfigResourceCompositionSession` and `AWSConfig-Describe` in
AWS CloudTrail. For more information, see [Non-recorded Resources](../../../config/latest/developerguide/select-resources.md#select-resources-non-recorded "../../../config/latest/developerguide/select-resources.md#select-resources-non-recorded") in the AWS Config Developer Guide.

Telemetry config uses this information and offers visibility into the configuration status,
at the resource type level and at more granular telemetry detail levels. You can customize your
view of the resources or telemetry details using filters, and modify the telemetry configuration
directly from the resource's console page.

Amazon CloudWatch uses AWS Config Internal service linked recorder.
You are not charged for CIs that CloudWatch uses as part of the Internal Service Linked Recorders.

###### Topics

- [Turning on telemetry auditing and configuration](telemetry-config-turn-on.md "telemetry-config-turn-on.md")
- [Viewing AWS resource telemetry in CloudWatch](telemetry-config-view-resources.md "telemetry-config-view-resources.md")
- [Working with telemetry enablement rules](telemetry-config-rules.md "telemetry-config-rules.md")
- [Turning off CloudWatch telemetry configuration](telemetry-config-turn-off.md "telemetry-config-turn-off.md")
