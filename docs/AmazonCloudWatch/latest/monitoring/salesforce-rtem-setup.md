# Salesforce RTEM integration configuration

Salesforce is a cloud-based Customer Relationship Management (CRM) platform that provides business applications for sales, service, marketing, and IT operations. It generates real-time security events through the [Pub/Sub API](https://developer.salesforce.com/docs/platform/pub-sub-api/overview "https://developer.salesforce.com/docs/platform/pub-sub-api/overview") (gRPC) covering login activity, API usage, file events, and data access across 19+ event channels with sub-second delivery. CloudWatch pipelines use the Salesforce Pub/Sub API to stream these events into CloudWatch Logs.

###### Topics

- [Source configuration for Salesforce RTEM](salesforce-rtem-source-config.md "salesforce-rtem-source-config.md")
- [CloudWatch pipelines configuration for Salesforce RTEM](salesforce-rtem-pipeline-setup.md "salesforce-rtem-pipeline-setup.md")
