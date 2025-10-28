# OPC UA data sources for AWS IoT SiteWise Edge

gateways

After you set up an AWS IoT SiteWise Edge gateway, you can configure data sources so that
your SiteWise Edge gateway can ingest data from local industrial equipment to AWS IoT SiteWise. Each
source represents a local server, such as an OPC UA server, that your SiteWise Edge
gateway connects and retrieves industrial data streams. For more information about
setting up a SiteWise Edge gateway, see [Create a self-hosted SiteWise Edge gateway](create-gateway-ggv2.md "create-gateway-ggv2.md").

The gateway type, MQTT-enabled, V3 gateways versus Classic stream, V2 gateways, influences how
OPC UA data is handled. In Classic stream, V2 gateways, OPC UA data sources are
added directly to the gateway IoT SiteWise publisher configuration. Each data source is
coupled with the gateway, and data routing is configured individually for each
source. In contrast, using MQTT-enabled, V3 gateways, OPC UA data sources are converted to MQTT
topics and are managed through centralized destinations. For more information on
each type, see [MQTT-enabled, V3 gateways for AWS IoT SiteWise Edge](mqtt-enabled-v3-gateway.md "mqtt-enabled-v3-gateway.md") and [Classic streams, V2 gateways for AWS IoT SiteWise Edge](classic-streams-v2-gateway.md "classic-streams-v2-gateway.md").

###### Note

AWS IoT SiteWise restarts your SiteWise Edge gateway each time you add or edit a source.
Your SiteWise Edge gateway won't ingest data while it's updating source configuration. The time to restart your
SiteWise Edge gateway depends on the number of tags on your SiteWise Edge gateway's sources. Restart time can range
from a few seconds (for a SiteWise Edge gateway with few tags) to several minutes (for a SiteWise Edge gateway with many tags).

After you create sources, you can associate your data streams with asset
properties. For more information about how to create and use assets, see [Model industrial assets](industrial-asset-models.md "industrial-asset-models.md").

You can view CloudWatch metrics to verify that a data source is connected to AWS IoT SiteWise. For
more information, see [AWS IoT Greengrass Version 2 gateway metrics](monitor-cloudwatch-metrics.md#gateway-metrics-ggv2 "monitor-cloudwatch-metrics.md#gateway-metrics-ggv2").

Currently, AWS IoT SiteWise supports the following data source protocols:

- [OPC
  UA](https://en.wikipedia.org/wiki/OPC_Unified_Architecture "https://en.wikipedia.org/wiki/OPC_Unified_Architecture") – A machine-to-machine (M2M) communication protocol
  for industrial automation.

## Support for additional industrial

protocols

SiteWise Edge supports a wide range of industrial protocols through integration with
data source partners. These partnerships enable connectivity with over 200
different protocols, accommodating various industrial systems and
devices.

For a list of available data source partners, see [SiteWise Edge gateway partner data
source options](connect-partner-data-source.md "connect-partner-data-source.md").
