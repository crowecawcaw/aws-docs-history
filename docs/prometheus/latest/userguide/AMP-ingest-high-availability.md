# Set up Amazon Managed Service for Prometheus for high

availability data

When you send data to Amazon Managed Service for Prometheus, it is automatically replicated across AWS
Availability Zones in the Region, and is served to you from a cluster of hosts that
provide scalability, availability, and security. You might want to add additional high
availability fail-safes, depending on your particular setup. There are two common ways
that you might additional high availability safeties to your setup:

- If you have multiple containers or instances that have the same data, you can
  send that data to Amazon Managed Service for Prometheus and have the data automatically de-duplicated. This
  helps to ensure that your data will be sent to your Amazon Managed Service for Prometheus workspace.

For more information about de-duplicating high-availability data, see [Deduplicating high availability metrics sent to
Amazon Managed Service for Prometheus](AMP-ingest-dedupe.md "AMP-ingest-dedupe.md").

- If you want to ensure that you have access to your data, even when the AWS
  Region is not available, you can send your metrics to a second workspace, in
  another Region.

For more information about sending metrics data to multiple workspaces, see
[Use cross Region workspaces to add
high availability in Amazon Managed Service for Prometheus](AMP-send-to-multiple-workspaces.md "AMP-send-to-multiple-workspaces.md").

###### Topics

- [Deduplicating high availability metrics sent to
  Amazon Managed Service for Prometheus](AMP-ingest-dedupe.md "AMP-ingest-dedupe.md")
- [Send high availability data to
  Amazon Managed Service for Prometheus with Prometheus](Send-high-availability-data.md "Send-high-availability-data.md")
- [Set up high availability data
  to Amazon Managed Service for Prometheus using the Prometheus Operator Helm chart](Send-high-availability-data-operator.md "Send-high-availability-data-operator.md")
- [Send high-availability data to
  Amazon Managed Service for Prometheus with AWS Distro for OpenTelemetry](Send-high-availability-data-ADOT.md "Send-high-availability-data-ADOT.md")
- [Send high availability data
  to Amazon Managed Service for Prometheus with the Prometheus community Helm chart](Send-high-availability-prom-community.md "Send-high-availability-prom-community.md")
- [Answers to common questions about high availability
  configuration in Amazon Managed Service for Prometheus](HA_FAQ.md "HA_FAQ.md")
- [Use cross Region workspaces to add
  high availability in Amazon Managed Service for Prometheus](AMP-send-to-multiple-workspaces.md "AMP-send-to-multiple-workspaces.md")
