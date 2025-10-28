# AWS Cloud WAN events and metrics

AWS provides the following monitoring tools to watch the resources in your global network,
report when something is wrong, and take automatic actions when appropriate.

- _Amazon CloudWatch_ monitors your AWS resources and the applications
  that you run on AWS in real time. You can collect and track metrics, create
  customized dashboards, and set alarms that notify you or take actions when a
  specified metric reaches a threshold that you specify. For more information, see the
  [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").
- _Amazon EventBridge_ delivers a near-real-time stream of system events
  that describe changes in AWS resources. EventBridge enables automated event-driven
  computing, as you can write rules that watch for certain events and then trigger
  automated actions in other AWS services when these events happen. For more
  information, see the [Amazon EventBridge User Guide](../../../eventbridge/latest/userguide.md "../../../eventbridge/latest/userguide.md").
  You must first onboard CloudWatch Logs Insights before you can view Events on the AWS Cloud WAN dashboards.
  See [Onboard CloudWatch Logs Insights for AWS Cloud WAN](cloudwan-onboard-events.md "cloudwan-onboard-events.md") for the onboarding steps.

###### Topics

- [CloudWatch metrics](cloudwan-metrics.md "cloudwan-metrics.md")
- [Onboard CloudWatch Logs Insights](cloudwan-onboard-events.md "cloudwan-onboard-events.md")
- [Monitor with Amazon CloudWatch Events](cloudwan-cloudwatch-events.md "cloudwan-cloudwatch-events.md")
- [Monitor Cloud WAN with CloudWatch
  metrics](cloudwan-cloudwatch-metrics.md "cloudwan-cloudwatch-metrics.md")
