# Ingest alarms into AWS Incident Detection and Response

AWS Incident Detection and Response supports alarm ingestion through [Amazon EventBridge](https://aws.amazon.com/eventbridge/ "https://aws.amazon.com/eventbridge/"). This section describes
how to integrate AWS Incident Detection and Response with different Application Performance Monitoring (APM)
tools, including Amazon CloudWatch, APMs with direct integration with Amazon EventBridge (for example,
Datadog and New Relic), and APMs without direct integration with Amazon EventBridge. For a
complete list of APMs with direct integration to Amazon EventBridge, see [Amazon EventBridge
integrations](https://aws.amazon.com/eventbridge/integrations "https://aws.amazon.com/eventbridge/integrations").

###### Topics

- [Provision access](idr-gs-access-prov.md "idr-gs-access-prov.md")
- [Integrate with CloudWatch](idr-gs-integrate_cloudwatch.md "idr-gs-integrate_cloudwatch.md")
- [Ingest alarms from APMs with EventBridge integration](idr-gs-ingest_alarms_from_apm_to_eventbridge.md "idr-gs-ingest_alarms_from_apm_to_eventbridge.md")
- [Example: Integrating notifications from Datadog and Splunk](example_integrating_notifications.md "example_integrating_notifications.md")
- [Ingest alarms from APMs without EventBridge integration](idr-ingesting-alarms-using-webhooks.md "idr-ingesting-alarms-using-webhooks.md")
