# Query your Prometheus metrics

Now that metrics are being ingested to the workspace, you can query them. A common way
to query your metrics is to use a service such as Grafana to query the metrics. In this
section, you will learn how to use Amazon Managed Grafana to query metrics from Amazon Managed Service for Prometheus.

###### Note

To learn about other ways to query your Amazon Managed Service for Prometheus metrics, or use the Amazon Managed Service for Prometheus
APIs, see [Query your Prometheus metrics](AMP-query.md "AMP-query.md").

This section assumes you already have a [workspace created](AMP-onboard-create-workspace.md "AMP-onboard-create-workspace.md"), and are [ingesting metrics](AMP-onboard-ingest-metrics.md "AMP-onboard-ingest-metrics.md") into it.

You perform your queries using the standard Prometheus query language, PromQL. For
more information about PromQL and its syntax, see [Querying
Prometheus](https://prometheus.io/docs/prometheus/latest/querying/basics/ "https://prometheus.io/docs/prometheus/latest/querying/basics/") in the Prometheus documentation.

Amazon Managed Grafana is a fully managed service for open-source Grafana that simplifies
connecting to open-source, third-party ISV, and AWS services for visualizing and
analyzing your data sources at scale.

Amazon Managed Service for Prometheus supports using Amazon Managed Grafana to query metrics in a workspace. In the Amazon Managed Grafana
console, you can add an Amazon Managed Service for Prometheus workspace as a data source by discovering your
existing Amazon Managed Service for Prometheus accounts. Amazon Managed Grafana manages the configuration of the authentication
credentials that are required to access Amazon Managed Service for Prometheus. For detailed instructions on creating
a connection to Amazon Managed Service for Prometheus from Amazon Managed Grafana, see the instructions in [the
Amazon Managed Grafana User Guide](../../../grafana/latest/userguide/prometheus-data-source.md "../../../grafana/latest/userguide/prometheus-data-source.md").

You may also view your Amazon Managed Service for Prometheus alerts in Amazon Managed Grafana. For instructions to set up
integration with alerts, see [Integrate alerts with Amazon Managed Grafana or open source
Grafana](integrating-grafana.md "integrating-grafana.md").

###### Note

If you have configured your Amazon Managed Grafana workspace to use a Private VPC, you must
connect your Amazon Managed Service for Prometheus workspace to the same VPC. For more information, see [Connecting to Amazon Managed Grafana in a private
VPC](AMP-amg.md#AMP-onboard-amg-in-vpc "AMP-amg.md#AMP-onboard-amg-in-vpc").
