# MQTT-enabled, V3 gateways for AWS IoT SiteWise Edge

AWS IoT SiteWise can use MQTT-enabled, V3 gateways, representing a significant advancement in the SiteWise Edge
gateway architecture. This gateway type leverages the MQTT (Message Queuing Telemetry
Transport) protocol for data communication, providing enhanced flexibility and
efficiency in industrial IoT deployments.

The MQTT-enabled, V3 gateway uses MQTT for data transfer, enabling a lightweight, publish-subscribe
network protocol that efficiently transports messages between devices and the cloud. You
can set up various data destinations, including real-time data ingestion directly into
AWS IoT SiteWise and buffered data ingestion using Amazon S3. To enable precise data collection, you
can implement path filters to subscribe to specific MQTT topics.

MQTT-enabled, V3 gateways come with a pre-configured real-time destination with filters set to "#"
(all topics), which you can customize or remove as needed. To streamline data
management, only one real-time destination can exist in each gateway.

The MQTT-enabled architecture differs significantly from the Classic streams, V2
gateway. While V2 uses a stream-based approach, V3 employs MQTT, offering more
configurable data destinations and filtering options. However, note that V3 does not
support the data processing pack, which is available in V2.

The MQTT-enabled, V3 gateway offers several advantages:

- Improved scalability, due to MQTT's lightweight nature, enabling better
  handling of numerous devices and high-frequency data transmission.
- Enhanced data control through path filters, enabling granular management of
  data collection and reducing unnecessary data transfer and processing.
- Flexible data handling, allowing configuration between real-time processing
  and buffered storage based on specific needs.
- Alignment with modern IoT communication standards, setting the stage for
  future enhancements and integrations.
  Consider adopting the MQTT-enabled, V3 gateway for new deployments, especially when you require
  flexible data ingestion options and precise control over data collection.

###### Note

For existing deployments or scenarios requiring the data processing pack, the
Classic streams, V2 gateway remains a viable option.

By offering both gateway types, AWS IoT SiteWise ensures that you can choose the solution that
best fits your specific industrial IoT needs, whether you prioritize advanced MQTT
capabilities or compatibility with existing systems.

## Destinations and path filters

View the following topics to learn more about destinations and path filters in
MQTT-enabled gateways:

- [Understand AWS IoT SiteWise Edge destinations](gw-destinations.md#source-destination "gw-destinations.md#source-destination")
- [Add an AWS IoT SiteWise Edge real-time destination](destinations-real-time.md "destinations-real-time.md")
- [Add an AWS IoT SiteWise buffered destination using Amazon S3](destinations-buffered.md "destinations-buffered.md")
- [Understand path filters for AWS IoT SiteWise Edge
  destinations](gw-destinations.md#destinations-path-filters "gw-destinations.md#destinations-path-filters")
- [Add path filters to AWS IoT SiteWise Edge
  destinations](destinations-add-path-filters.md "destinations-add-path-filters.md")
- [Manage AWS IoT SiteWise Edge destinations](destinations-manage.md "destinations-manage.md")
