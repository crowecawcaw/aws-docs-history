# Onboarding Accelerate monitoring

Monitoring is enabled by default for all new resources except Amazon EC2 instances. You can start monitoring your Amazon EC2 instances by tagging your instances.

To onboard monitoring, first make sure that your configuration monitors the resources that you want AMS
to monitor, and ignores the resources that you want it to ignore.

You can use the following CloudWatch dashboards to explore how many of your resources are targeted by AMS
monitoring and tagging, and how many are not. In your account, navigate to the CloudWatch dashboards console, and select one of the following:

- AMS-Alarm-Manager-Reporting-Dashboard
- AMS-Resource-Tagger-Reporting-Dashboard
  For a complete description of the dashboard metrics, see:

- [Viewing the number of resources monitored by Alarm Manager for Accelerate](acc-mem-number-of-resources.md "acc-mem-number-of-resources.md")
- [Viewing the number of resources managed by Resource Tagger](acc-rt-using.md#acc-rt-number-of-resources "acc-rt-using.md#acc-rt-number-of-resources")

## Onboarding resources to be monitored in Accelerate

To override the default behavior, for example, to
disable default monitoring for non-EC2 resources, you need to untag those resources using a custom configuration profile.
For more information about tagging for monitoring, see [Monitoring in Accelerate](acc-tag-req-mon.md "acc-tag-req-mon.md").

Monitoring is disabled for EC2 instances until you onboard your instances, which includes tagging your instances using a custom configuration profile.
The next section describes EC2 instance onboarding.

## Creating a monitoring configuration profile in Accelerate

- For information about using the default configuration, see
  [Accelerate Alarm Manager](acc-mem-tag-alarms.md "acc-mem-tag-alarms.md").
- For information about using a custom configuration, see
  [Modifying the Accelerate alarm default configuration](acc-mem-modify-default.md "acc-mem-modify-default.md").
