# Data processing pack

availability change

###### Note

The data processing pack (DPP) feature is no longer availabke to new customers. Existing customers can continue to use the service as normal. For more information, see
[Data processing pack availability change](../appguide/iotsitewise-dpp-availability-change.md "../appguide/iotsitewise-dpp-availability-change.md").

For capabilities similar to AWS IoT data processing pack feature explore
either [open-source alternatives](open-source-edge-integrations.md "open-source-edge-integrations.md") or our [partner
integrations](cpa-add-source.md "cpa-add-source.md"). The AWS IoT SiteWise Data Processing Pack is a feature of AWS IoT SiteWise
that provides data transformations, metrics, filtering, local storage and
visualization at the edge.

###### Note

AWS IoT SiteWise and the AWS IoT SiteWise Edge data collection pack feature continues to be
available, but the data processing pack feature is entering maintenance mode.

## Migration options

Explore these migration options for replacing the data processing pack
functionality.

**Open-source alternatives**

Create local data processing pipelines using Node-RED for data
transformation, InfluxDB for time-series storage, and Grafana
for visualization. These tools work with MQTT-enabled, V3 gateways through
MQTT to provide edge processing and local insights while
synchronizing data with the AWS Cloud.

For more information, see [Process and visualize data with SiteWise Edge and
open-source tools](open-source-edge-integrations.md "open-source-edge-integrations.md").

**Partner integrations**

Connect industrial equipment and sensors through third-party
partner data sources like CloudRail, EasyEdge, and Litmus Edge.
These Greengrass components are developed in partnership with
AWS and support over 200 industrial protocols for
comprehensive data collection and processing.

For more information, see [Add
a data source](cpa-add-source.md "cpa-add-source.md").

**MQTT-enabled, V3 gateways**

MQTT-enabled, V3 gateways use lightweight MQTT protocol for efficient data
communication and offer flexible data destinations including
real-time ingestion and buffered Amazon S3 ingestion. You can
implement path filters for precise data collection and benefit
from improved scalability and IoT standards alignment.
MQTT-enabled, V3 gateways provide cloud-based data processing through AWS IoT SiteWise
core services including asset models, computed properties,
alarms, and historical data queries.

For more information, see [MQTT-enabled, V3 gateways for AWS IoT SiteWise Edge](mqtt-enabled-v3-gateway.md "mqtt-enabled-v3-gateway.md").

## Frequently asked questions

Yes, you can migrate gradually using any combination of the
migration options. You can deploy MQTT-enabled, V3 gateways, open-source
alternatives, or partner integrations alongside existing
Classic streams, V2 gateways with the data processing pack. All options can send
data to the same AWS IoT SiteWise environment.

The data processing pack remains available to existing customers
in maintenance mode. You'll receive advance notice if any changes to
availability are planned. Monitor AWS service announcements and
your account notifications for updates.
