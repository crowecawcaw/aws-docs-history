# Set up Amazon Managed Grafana for use with Amazon Managed Service for Prometheus

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

## Connecting to Amazon Managed Grafana in a private

VPC

Amazon Managed Service for Prometheus provides a service endpoint for Amazon Managed Grafana to connect to when querying
metrics and alerts.

You can configure Amazon Managed Grafana to use a private VPC (for details on setting up a
private VPC in Grafana, see [Connecting to
Amazon VPC](../../../grafana/latest/userguide/AMG-configure-vpc.md "../../../grafana/latest/userguide/AMG-configure-vpc.md") in the _Amazon Managed Grafana User Guide_). Depending on
the settings, this VPC may not have access to the Amazon Managed Service for Prometheus service endpoint.

To add Amazon Managed Service for Prometheus as a data source to an Amazon Managed Grafana workspace that is configured to
use a specific private VPC, you must first connect your Amazon Managed Service for Prometheus to the same VPC by
creating a VPC endpoint. For more information about creating a VPC endpoint, see
[Create an interface VPC endpoint for Amazon Managed Service for Prometheus](AMP-and-interface-VPC.md#create-VPC-endpoint-for-AMP "AMP-and-interface-VPC.md#create-VPC-endpoint-for-AMP").
