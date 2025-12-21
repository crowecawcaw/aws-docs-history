# External metrics ingestion

You can use the external metrics ingestion feature to configure AWS Compute Optimizer to ingest EC2
memory utilization metrics from one of the four observability products: Datadog, Dynatrace,
Instana, and New Relic. When you enable external metrics ingestion, Compute Optimizer analyzes your
external EC2 memory utilization metrics in addition to your CPU, disk, network, IO, and
throughput data to generate EC2 rightsizing recommendations. These recommendations can provide
you with additional savings and enhanced performance. For more information, see [Configuring external metrics
ingestion](configure-external-metrics-ingestion.md "configure-external-metrics-ingestion.md").

###### Note

External metrics ingestion doesn't support EC2 instances that are part of EC2 Auto Scaling groups.

## Metric requirements

To generate EC2 rightsizing recommendations with external memory utilization metrics,
Compute Optimizer requires at least 30 consecutive hours of memory utilization metrics from your
observability product. If you don’t have enough hours of external memory utilization
metrics, Compute Optimizer analyzes and generates recommendations from your CloudWatch metrics until you reach
the external memory metric requirements.

###### Note

When external metrics ingestion is enabled, Compute Optimizer prioritizes your external memory utilization metrics over
your CloudWatch memory data. If you opt out of external metrics ingestion, Compute Optimizer defaults back to analyze
and generate recommendations based on your CloudWatch metrics.

## Organization and account level

You can configure external metric ingestion at both the organization and account level.
If you're a member account of an AWS organization that configured external metrics
ingestion, you can opt out of this feature. For more information, see [Opting out of external metrics
ingestion](deactivate-external-metrics-ingestion.md "deactivate-external-metrics-ingestion.md").

Suppose that you're a new member of an AWS organization that already configured
external metrics ingestion. Then, you must configure external metrics ingestion for your
AWS account manually. For more information, see [Configuring external metrics
ingestion](configure-external-metrics-ingestion.md "configure-external-metrics-ingestion.md").

## Next steps

For instructions on how to configure external metric ingestion, see [Configuring external metrics
ingestion](configure-external-metrics-ingestion.md "configure-external-metrics-ingestion.md").
