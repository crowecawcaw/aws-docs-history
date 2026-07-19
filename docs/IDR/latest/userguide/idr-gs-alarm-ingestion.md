# Alarm Ingestion

The AWS Incident Detection and Response Customer Command Line Interface (IDR CLI) can create new Amazon CloudWatch alarms or ingest your existing ones and can deploy and test infrastructure through AWS CloudFormation to allow third-party tools to send alerts to AWS Incident Detection and Response.

AWS Incident Detection and Response can ingest alarms from Amazon CloudWatch and third party Application Performance Monitoring (APM) tools via Amazon EventBridge:

- [Ingesting CloudWatch alarms](idr-gs-ingest-cw-alarms.md "idr-gs-ingest-cw-alarms.md")
- [Ingesting Third Party Application Performance Monitoring Alarms](idr-gs-ingest-apm-alarms.md "idr-gs-ingest-apm-alarms.md")

## Steps for alarm ingestion

The following steps need to be completed for alarm ingestion:

- [Alarm definition](idr-gs-alarm-definition.md "idr-gs-alarm-definition.md")
- [Alarm ingestion using the IDR CLI](https://github.com/awslabs/CLI-for-AWS-Incident-Detection-and-Response "https://github.com/awslabs/CLI-for-AWS-Incident-Detection-and-Response")
- [Alarm review and feedback](idr-gs-alarm-review.md "idr-gs-alarm-review.md")
- [Provision access for alarm ingestion to Incident Detection and Response](idr-gs-access-prov.md "idr-gs-access-prov.md")
- [Alarms go live](idr-gs-alarms-go-live.md "idr-gs-alarms-go-live.md")

## Alternative options for ingesting alarms

If you can't use the IDR CLI for onboarding, consult your Technical Account Manager (TAM) for alternative options. For more information, see [Workload onboarding questionnaire in Incident Detection and Response (exception path)](idr-gs-questionnaire.md "idr-gs-questionnaire.md").
