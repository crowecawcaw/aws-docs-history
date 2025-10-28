# Monitoring CodeArtifact

Monitoring is an important part of maintaining the reliability, availability, and performance of
CodeArtifact and your other AWS solutions. AWS provides the following monitoring tools to watch
CodeArtifact, report when something is wrong, and take automatic actions when appropriate:

- You can use Amazon EventBridge to automate your AWS services and respond automatically to system
  events, such as application availability issues or resource changes. Events from AWS
  services are delivered to EventBridge in near real time. You can write simple rules to indicate
  which events are of interest to you and which automated actions to take when an event
  matches a rule. For more information, see [Amazon EventBridge User Guide](../../../eventbridge/latest/userguide.md "../../../eventbridge/latest/userguide.md") and [CodeArtifact event format and example](monitoring-events.md#service-event-format-example "monitoring-events.md#service-event-format-example").
- You can use Amazon CloudWatch metrics to view CodeArtifact usage by operation. CloudWatch metrics includes all requests made to CodeArtifact, and requests are shown
  by account. You can view these metrics in CloudWatch metrics by navigating to the **Usage/By AWS Resource** AWS namespace.
  For more information, see
  [Use Amazon CloudWatch metrics](../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md "../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md") in
  the _Amazon CloudWatch User Guide_.

###### Topics

- [Monitoring CodeArtifact events](monitoring-events.md "monitoring-events.md")
- [Use an event to start a CodePipeline
  execution](configure-service-events-codepipeline.md "configure-service-events-codepipeline.md")
- [Use an event to run a Lambda
  function](configure-service-events-lambda-function.md "configure-service-events-lambda-function.md")
