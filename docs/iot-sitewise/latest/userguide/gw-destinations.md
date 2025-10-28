# Destinations and path filters

Destinations in AWS IoT SiteWise Edge provide a flexible and efficient way to manage how your
industrial data flows from edge devices to the cloud. This section explains how to configure
destinations, use path filters to route specific data streams, and choose the right destination
type for your use case.

You can use destinations and path filters on self-hosted MQTT-enabled, V3 gateways and
gateways used in conjunction with AWS IoT SiteWise Edge application hosted on Siemens Industrial Edge. Destinations
and path filters do not work with Classic Streams, V2 gateways.

###### Topics

- [Understand AWS IoT SiteWise Edge destinations](#source-destination "#source-destination")
- [Understand path filters for AWS IoT SiteWise Edge
  destinations](#destinations-path-filters "#destinations-path-filters")
- [Add an AWS IoT SiteWise Edge real-time destination](destinations-real-time.md "destinations-real-time.md")
- [Add an AWS IoT SiteWise buffered destination using Amazon S3](destinations-buffered.md "destinations-buffered.md")
- [Add path filters to AWS IoT SiteWise Edge
  destinations](destinations-add-path-filters.md "destinations-add-path-filters.md")
- [Manage AWS IoT SiteWise Edge destinations](destinations-manage.md "destinations-manage.md")

## Understand AWS IoT SiteWise Edge destinations

Use AWS IoT SiteWise Edge destinations to determine where to send your source data. You can choose
your data destination based on specific characteristics you need, like cost-effectiveness,
low latency, or storage requirements. Integrate device data captured by AWS IoT SiteWise, our partners,
or custom applications to publish and subscribe to path filters (topics) at the edge. You can
then model, transfer, and store your device data in the cloud.

###### Note

For full use of all destination features on self-hosted gateways, upgrade to the latest
versions of the IoT SiteWise publisher and IoT SiteWise OPC UA collector. Stream support is continued on
Classic streams, V2 gateways to maintain compatibility with existing setups. For more
information, see [Classic streams, V2 gateways for AWS IoT SiteWise Edge](classic-streams-v2-gateway.md "classic-streams-v2-gateway.md")

###### Topics

- [How SiteWise Edge destinations enhance data management](#how-destinations-work "#how-destinations-work")
- [Destination types](#destination-types "#destination-types")
- [Compare destination functionality between gateway versions](#destinations-vs-publisher-component "#destinations-vs-publisher-component")
- [Destination limitations](#destinations-limitiations "#destinations-limitiations")
- [Use cases for SiteWise Edge destinations](#destinations-use-cases "#destinations-use-cases")

### How SiteWise Edge destinations enhance data management

Export data from the edge to AWS IoT SiteWise in real time, or in batches using Amazon S3.

Destinations enhance flexibility and scalability in your AWS IoT SiteWise environment.
Destinations implement a centralized data management model, where sources publish data to a
central system. Destinations determine where your data is sent using path filters.
Destinations can subscribe to multiple path filters.

MQTT-enabled gateways, whether self-hosted or running on Siemens Industrial Edge, use MQTT for local
communication and come with a default real-time destination which has filters set to
`#`. This means that, by default, all messages on all topics are published to
the AWS IoT SiteWise real-time destination. For more information, see [Understand path filters for AWS IoT SiteWise Edge
destinations](#destinations-path-filters "#destinations-path-filters"). You can
add one real-time destination in each gateway.

### Destination types

When configuring a destination for your gateway, you have two main options: real-time
configuration using AWS IoT SiteWise, and a buffered configuration using Amazon S3. Each destination type
has its own set of settings and considerations.

**AWS IoT SiteWise real-time settings**

Choose this to send data directly to AWS IoT SiteWise hot-tier storage to facilitate
ingesting and monitoring data in real-time. The real-time settings manage data flow,
particularly when a gateway experiences connectivity issues with the cloud. During
connection loss, data is temporarily stored locally on the gateway. Once the
connection is re-established, the stored data is automatically sent to the
cloud.

You can adjust various aspects of the data publishing process, such as the maximum
amount of data to be stored locally, the rate at which data is sent to the cloud upon
reconnection, and when to delete data after the storage reaches its capacity.

For more information on AWS IoT SiteWise storage tiers, see, [Manage data storage in AWS IoT SiteWise](manage-data-storage.md "manage-data-storage.md").

**AWS IoT SiteWise buffered using Amazon S3 settings**

This destination type allows you to buffer data locally on the gateway and
periodically send it to an Amazon S3 bucket in batches. The data is stored in the efficient
Parquet format, which is optimized for analytical workloads. Once the data is in Amazon S3,
you can import it into AWS IoT SiteWise for storage, processing, and analysis.

Choose this option to ingest data in batches, and store historical data in a
cost-effective way. You can configure your preferred Amazon S3 bucket location, and the
frequency at which you want data to be uploaded to Amazon S3. You can also choose what to
do with the data after ingestion into AWS IoT SiteWise. You can choose to have the data
available in both SiteWise and Amazon S3 or you can choose to delete it automatically from
Amazon S3.

### Compare destination functionality between gateway versions

The destinations feature in MQTT-enabled gateways streamlines data flow management.
Destinations simplify data management through centralized configuration of data routing to
various endpoints. This approach eliminates the need for complex individual stream setups,
making the overall system more flexible and easier to manage.

By comparison, the Classic streams, V2 gateway, SiteWise Edge transmits data from data sources
to publishers via AWS IoT Greengrass streams, configuring data destinations individually for each data
source.

With the AWS IoT SiteWise destination feature, the publisher routing configuration is
consolidated. Destination configuration allows you to manage destinations and path filters
in a centralized manner. You can easily add a destination, manage path filters, delete
unnecessary filters or destinations, depending on your needs.

Additionally, the destinations feature utilizes MQTT (Message Queuing Telemetry
Transport), an industry-standard protocol widely used in industrial IoT applications. This
adoption of MQTT helps AWS IoT SiteWise to facilitate easier integration with various devices and
systems.

### Destination limitations

Current limitations for destinations on SiteWise Edge gateways include:

- The data processing pack isn't supported on MQTT-enabled gateways.
- Data type support is limited to AWS IoT SiteWise data types. For information on enabling data
  type conversion, see [Converting unsupported data types](string-conversion.md "string-conversion.md").

### Use cases for SiteWise Edge destinations

SiteWise Edge destinations are utilized in diverse applications. Here are some key
examples:

**Industrial automation**
_Real-time monitoring and predictive maintenance_

In industrial settings, sensors and devices on the factory floor can publish data
to SiteWise Edge. Destinations can be configured to filter and route relevant data, enabling
real-time monitoring and analysis of machine performance. You can subscribe to
relevant MQTT topics using path filters, process the data, and then publish the
processed data. In this way, you can selectively route processed data to AWS cloud
analytic services or on-premises systems. Manufacturers can then implement predictive
maintenance strategies, optimize production processes, and reduce downtime.

**Smart buildings**
_Energy efficiency and occupancy optimization_

Building automation systems generate data streams to monitor and control various
aspects of a building, such as HVAC systems, lighting, and access control. With
SiteWise Edge, these data streams can be ingested, processed, and routed to different
destinations. Facility managers can configure destinations to filter and forward
relevant data, enabling advanced capabilities like energy efficiency measures and
occupancy optimization while ensuring data privacy and compliance.

These use cases demonstrate how the Destinations feature in SiteWise Edge can be leveraged
across various industries to ingest, process, and route data efficiently. This enables
advanced capabilities such as real-time monitoring, predictive maintenance, energy
efficiency, and remote diagnostics while ensuring data privacy and compliance.

## Understand path filters for AWS IoT SiteWise Edge

destinations

###### Topics

- [Path filter requirements](#path-filter-requirements "#path-filter-requirements")
- [Best practices for path filters](#create-effective-path-filters "#create-effective-path-filters")
- [Path filters for OPC UA servers](#path-filters-opcua "#path-filters-opcua")
- [Special characters in path filter
  names](#path-filters-special-characters "#path-filters-special-characters")

Each destination is configured to route data to AWS IoT SiteWise or Amazon S3. Path filters allow you to
select specific data to filter when receiving MQTT messages for a destination. Path filters
represent the logical names of your data streams, acting as subscriptions to desired MQTT
topics.

In MQTT, data is organized into topics, which are hierarchical strings separated by
forward slashes (`/`). For example, a device might publish temperature data to the
topic `home/livingroom/sensor1/temperature`. Here,
`home/livingroom/sensor1` represents the path or logical name of the sensor, and
`temperature` is the data type being published.

You can use path filters to subscribe to specific topics or a range of topics using
wildcards (`+` and `#`). The `+` wildcard matches a single
level in the topic hierarchy. For example, `home/+/sensor1/temperature` would match
`home/livingroom/sensor1/temperature` and
`home/bedroom/sensor1/temperature`. The `#` wildcard, when used at the
end of a filter, matches multiple levels.

You can also use a variety of characters typically not allowed in the MQTT specification
within a path filter name. These characters don't function as wildcards when used within a
name. AWS IoT SiteWise converts these characters using encoding to ensure MQTT compliance while
preserving your original naming structure. This feature is particularly useful for
accommodating existing naming conventions from other systems. For more information, see [Special characters in path filter
names](#path-filters-special-characters "#path-filters-special-characters").

By carefully selecting the appropriate path filters, you can control which data is sent to
a specific destination. Tailor the data flow to your IoT system's requirements using path
filters.

### Path filter requirements

When entering path filters using the AWS IoT SiteWise console, keep the following in mind:

- Path filters are delimited by a new line, with each line representing a separate
  path filter.
- Individual path filters can have between 1 and 65,535 bytes.
- A path filter can't be blank.
- Null values (U+0000) are not allowed.
- You can enter up to 100 path filters or 65,535 characters at a time, whichever limit
  is reached first.
- The overall limit is 20,000 path filters for all the destinations on a gateway
  combined.
- You can use `%`, `#`, `+`, and `$`
  characters within path filter names, however AWS IoT SiteWise automatically converts them to URI
  encoding.

### Best practices for path filters

When creating path filters for your AWS IoT SiteWise destinations, consider the following
strategies to effectively manage your data.

- Structure your filters to mirror your device hierarchy. For example, in a
  manufacturing setting, `factory/+/machine/#`, captures data from all machines
  across different production lines.
- Use specific levels for device types, locations, or functions. For example,
  `factory/assembly-line/robot/temperature`. Or, in smart agriculture,
  `farm/+/crop/+/moisture`, to monitor moisture levels for various crops
  across different fields.
- Leverage wildcards strategically: Use `+` for variations at a single
  level and `#` to capture all subsequent levels. For example,
  `building/+/+/energy-consumption`, tracks energy usage across different
  zones and floors in a building. This assumes the first `+` captures all
  floors and the second `+` captures all zones.
- Balance specificity and flexibility by creating filters that are specific enough to
  capture relevant data but flexible enough to accommodate future changes. For example,
  `site/+/equipment-type/+/measurement` allows for addition of new sites or
  equipment types without changing the filter structure.

Test your filters thoroughly to ensure they capture the intended data and align with
your IoT system's architecture and goals.

### Path filters for OPC UA servers

For OPC UA servers, your path filters must correspond to the OPC UA tag names. The final
level of your path filter must match the OPC UA tag name exactly. For example, if your OPC
UA tag is `Device1.Temperature`, your path filter might be
`factory/line1/Device1.Temperature`. You can use wildcards in the preceding
levels, such as `factory/+/Device1.Temperature` to capture the tag across
multiple production lines. If you have special characters within your path filter names, see
[Special characters in path filter
names](#path-filters-special-characters "#path-filters-special-characters") for more information.

### Special characters in path filter

names

AWS IoT SiteWise accommodates characters commonly used in industrial protocols like OPC UA, which
are typically not allowed in standard MQTT topic names. This feature facilitates smoother
integration of industrial systems with MQTT-based architectures.

###### Note

While our special character handling is helpful for integration and migration, it's
recommended to align with standard MQTT naming conventions for new implementations when
possible to ensure broader compatibility.

When receiving data from industrial sources, AWS IoT SiteWise normalizes topic names using URI
encoding for special characters:

- `%` becomes `%25` (encoded first as the escape
  character)
- `#` becomes `%23`
- `+` becomes `%2B`
- `$` becomes `%24` (only when at the start of a topic)

This encoding ensures that source data containing these special MQTT characters can be
safely used as MQTT topic names while preserving the original industrial naming
conventions.

###### Example : Special characters in path filter names

Here are examples of how industrial topic names might appear in AWS IoT SiteWise path
filters:

- `Factory1/Line#2/Sensor+3` becomes
  `Factory1/Line%232/Sensor%2B3`
- `Plant%A/Unit$1/Temp` becomes
  `Plant%25A/Unit%241/Temp`
- `Site1/#Section/+Node` becomes
  `Site1/%23Section/%2BNode`

When creating subscriptions or viewing topic names in AWS IoT SiteWise, you'll see the original,
unencoded versions. The encoding is handled automatically to ensure MQTT compliance.
