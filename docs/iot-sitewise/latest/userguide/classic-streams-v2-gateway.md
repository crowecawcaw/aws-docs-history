# Classic streams, V2 gateways for AWS IoT SiteWise Edge

Understand the features and limitations of Classic streams, V2 gateways for AWS IoT SiteWise Edge.

The Classic streams, V2 gateway maintains traditional functionality familiar from earlier AWS IoT SiteWise
deployments before the introduction of MQTT-enabled, V3 gateways. These SiteWise Edge gateways are
considered Classic streams, V2 gateways. They maintain backward compatibility and are functional with
the data processing pack. While the Classic streams, V2 gateway offers reliable
performance for existing setups, it has limitations compared to newer gateway options.
Specifically, this gateway type is not fully compatible with the advanced features
available in the MQTT-enabled, V3 gateway destination. To use the MQTT messaging protocol, you can
create a new MQTT-enabled, V3 gateway. For more information, see [MQTT-enabled, V3 gateways for AWS IoT SiteWise Edge](mqtt-enabled-v3-gateway.md "mqtt-enabled-v3-gateway.md").

###### Topics

- [Use packs to collect and process data in
  SiteWise Edge](data-packs.md "data-packs.md")
- [Configure the AWS IoT SiteWise publisher
  component](configure-publisher-component.md "configure-publisher-component.md")
- [Destinations and AWS IoT Greengrass stream manager](destinations-gg-stream-manager.md "destinations-gg-stream-manager.md")
- [Configure edge capabilities on
  AWS IoT SiteWise Edge](edge-data-collection-and-processing.md "edge-data-collection-and-processing.md")
- [Configure edge data processing for AWS IoT SiteWise models
  and assets](edge-processing.md "edge-processing.md")
