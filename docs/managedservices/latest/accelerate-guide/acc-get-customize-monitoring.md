# Customize monitoring in Accelerate

To customize monitoring of your cloud resources based on your application needs:

1. Create a custom monitoring policy. See [Modifying the Accelerate alarm default configuration](acc-mem-modify-default.md "acc-mem-modify-default.md").
2. Apply a custom policy to resources using tags. See [Monitoring in Accelerate](acc-tag-req-mon.md "acc-tag-req-mon.md")
3. Route alerts to the resource owner. See
   [Tag-based alert notification](how-monitoring-works.md#how-mon-works-alert-notes-tags "how-monitoring-works.md#how-mon-works-alert-notes-tags").
   You can use the following CloudWatch dashboards to explore how many of your resources are
   targeted by AMS monitoring and tagging, and how many are not. In your account,
   navigate to the CloudWatch dashboards console, and select one of the following:

- AMS-Alarm-Manager-Reporting-Dashboard
- AMS-Resource-Tagger-Reporting-Dashboard
  For a complete description of the dashboard metrics, see:

- [Viewing the number of resources monitored by Alarm Manager for Accelerate](acc-mem-number-of-resources.md "acc-mem-number-of-resources.md")
- [Viewing the number of resources managed by Resource Tagger](acc-rt-using.md#acc-rt-number-of-resources "acc-rt-using.md#acc-rt-number-of-resources")
