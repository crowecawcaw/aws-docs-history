# Source configuration for Cisco Umbrella

## Integrating with Cisco Umbrella

Cisco Umbrella is a cloud-delivered security platform that provides secure
internet access and threat protection across all devices, locations, and users. It
uses DNS-layer security, web filtering, and cloud-delivered firewall features to
block malicious domains and prevent cyberattacks before they reach your network.
CloudWatch pipelines enables you to collect this data in CloudWatch Logs.

## Instructions to setup Amazon S3 and Amazon SQS

Configuring Cisco Umbrella to send logs to an Amazon S3 bucket involves several steps,
primarily focused on setting up the Amazon S3 bucket, Amazon SQS queue, and IAM roles, then
configuring the CloudWatch pipeline.

- Make sure Cisco Umbrella logs environment exporter is configured with S3.
  This is typically found under Admin → Logs Management in the Cisco
  Umbrella console.
- Amazon S3 bucket that stores the Cisco Umbrella logs should reside in the same
  AWS region as your CloudWatch pipeline.
- Create an Amazon SQS queue in the same AWS region as your Amazon S3 bucket. This
  queue will receive notifications when new log files are added to the Amazon S3
  bucket.
- Configure the Amazon S3 bucket to create event notifications, specifically for
  "Object Create" events. These notifications should be sent to the Amazon SQS
  queue you created in the previous step.

## Configuring the CloudWatch Pipeline

When configuring the pipeline to read data from Cisco Umbrella, choose Cisco
Umbrella as the data source. After filling in the required information and creating
the pipeline, data will be available in the selected CloudWatch Logs log group.

## Supported Open Cybersecurity Schema Framework Event Classes

This integration supports OCSF schema version v1.5.0 and [Cisco
Umbrella events](https://securitydocs.cisco.com/docs/umbrella-sig/olh/152763.dita "https://securitydocs.cisco.com/docs/umbrella-sig/olh/152763.dita") that map to DNS Activity (4003), Network Activity
(4001), Data Security Finding (2006), and Entity Management (3004). Each event comes
from a source as mentioned below.

**DNS Activity** contains the following actions:

- [DNS Logs](https://securitydocs.cisco.com/docs/umbrella-sig/olh/152744.dita "https://securitydocs.cisco.com/docs/umbrella-sig/olh/152744.dita")

**Network Activity** contains the following actions:

- [Cloud Firewall Logs](https://securitydocs.cisco.com/docs/umbrella-sig/olh/152740.dita "https://securitydocs.cisco.com/docs/umbrella-sig/olh/152740.dita")
- [Secure Gateway logs](https://securitydocs.cisco.com/docs/umbrella-sig/olh/152788.dita "https://securitydocs.cisco.com/docs/umbrella-sig/olh/152788.dita")
- [IPS logs](https://securitydocs.cisco.com/docs/umbrella-sig/olh/152760.dita "https://securitydocs.cisco.com/docs/umbrella-sig/olh/152760.dita")

**Data Security Finding** contains the following actions:

- [DLP (Data Loss Prevention) logs](https://securitydocs.cisco.com/docs/umbrella-sig/olh/152741.dita "https://securitydocs.cisco.com/docs/umbrella-sig/olh/152741.dita")

**Entity Management** contains the following actions:

- [Admin Audit logs](https://securitydocs.cisco.com/docs/umbrella-sig/olh/152738.dita "https://securitydocs.cisco.com/docs/umbrella-sig/olh/152738.dita")
