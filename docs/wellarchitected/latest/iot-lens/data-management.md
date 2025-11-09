# Data management

In the domain of IoT architectures, data management stands as a
cornerstone for the workload's success. As devices proliferate and
generate an ever-increasing volume of information, the way data is
handled, processed, and stored becomes crucial for maintaining
operational efficiency and extracting meaningful insights. Modern
IoT solutions must navigate the complexities of managing data
across different layers of the architecture, from edge devices to
cloud storage, while facilitating optimal performance and
cost-effectiveness.

The journey of IoT data, from its creation at the device level to
its final destination in storage systems, requires careful
consideration of multiple factors that impact the overall
solution's effectiveness. These considerations become especially
critical as organizations scale their IoT deployments from
hundreds to thousands or even millions of connected devices. A
well-designed data management strategy must address not only the
immediate needs of data collection and storage but also account
for future growth, regulatory requirements, and the evolving needs
of downstream applications and analytics.

| IOTPERF03: Does transmitted content<br>include auditable metadata? |
| ------------------------------------------------------------------ |
|                                                                    |

In IoT deployments, data integrity and traceability are
fundamental aspects impacting operational reliability, compliance,
and troubleshooting. Messages transmitted within an IoT landscape
must include essential metadata enabling comprehensive auditing
and verification. This becomes increasingly critical as
organizations face growing regulatory scrutiny and data lineage
requirements.

The way IoT devices handle metadata throughout the transmission
process is crucial for building trustworthy systems. The ability
to track and verify message origin, timing, and handling
distinguishes robust, enterprise-grade solutions from basic
implementations. Organizations must implement metadata management
strategies that support both operational requirements and
compliance needs.

Comprehensive metadata practices influence multiple aspects of IoT
solutions, from firmware design to cloud processing. A
well-structured approach enables advanced capabilities like
message deduplication, sequence verification, and temporal
analysis, while providing crucial audit trails. As deployments
scale, proper metadata becomes essential for maintaining system
reliability and enabling sophisticated data analysis.

## IOTPERF03-BP01 Add timestamps to each published message

Timestamps (ideally in UTC time) help in determining delays that
might occur during the transmission of a message from the device
to the application. Timestamps can be associated with the
message and to fields contained in the message. If a timestamp
is included, the sent timestamp is recorded on the cloud-side
along with the sensor or event data.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTPERF03-BP01-01** _Add timestamps on the server side._

- If the devices lack the capability to add timestamps to the
  messages, consider using server-side features to enrich the
  messages with timestamps that correspond to receiving the
  message.
- For example, AWS IoT Rules SQL language provides a
  `timestamp()` function to generate a timestamp when the
  message is received.
- When using AWS IoT Greengrass:
  - Use AWS IoT Greengrass stream manager to batch timestamped
    messages during connectivity interruptions while
    preserving message sequence integrity
  - Consider local AWS Lambda functions to process and
    enrich messages with timestamps closer to the source,
    minimizing latency between event occurrence and
    timestamp application

**Prescriptive guidance
IOTPERF03-BP01-02** _Have a reliable time source on the
device._

- Without a reliable time source, the timestamp can only be
  used relative to the specific device. For example:
  - Devices should use the Network Time Protocol (NTP) to
    obtain a reliable time when connected.
  - Real-time clock (RTC) devices can be used to maintain an
    accurate time while the device lacks network
    connectivity.

- Depending on the application, timestamps can be added at the
  message level or at the single payload field level. Delta
  encoding can be used to reduce the size of the message when
  multiple timestamps are included. Choosing the right
  approach is a trade-off between accuracy, energy efficiency,
  and payload size.

### Resources

- [AWS IoT Rules Developer Guide – timestamp() function](../../../iot/latest/developerguide/iot-sql-functions.md#iot-function-timestamp "../../../iot/latest/developerguide/iot-sql-functions.md#iot-function-timestamp")
- [The Implementation of Timestamp, Bitmap and RAKE Algorithm on Data Compression and Data Transmission from IoT to
  Cloud](https://ieeexplore.ieee.org/document/8528698 "https://ieeexplore.ieee.org/document/8528698")
- [Delta
  encoding](https://en.wikipedia.org/wiki/Delta_encoding "https://en.wikipedia.org/wiki/Delta_encoding")

| IOTPERF04: Is there a mechanism for<br>payload filtering or stream prioritization? |
| ---------------------------------------------------------------------------------- |
|                                                                                    |

Firmware updates are critical, and filtering messages at the
edge might subject the devices to unnecessary load. This
result could be counterproductive from a power and memory
consumption perspective. Sending only messages that the device
makes use of reduces the load on the resources and supports
better performances.

## IOTPERF04-BP01 Have mechanisms to prioritize specific payload types

One strategy to address payload stream prioritization is to
create multiple queues or data streams to separate and channel
different payload types. For example, you could have dedicated
queues or streams for real-time sensor data, firmware updates,
and configuration messages. You can use this separation to apply
different prioritization policies and processing rules based on
the payload type's criticality and performance requirements.

Additionally, use protocol-level features such as Quality of
Service (QoS) in MQTT to provide reliable and prioritized
message delivery. By setting different QoS levels for different
payload types, you can prioritize the delivery of critical
messages over non-critical ones and transmit high-priority data
reliably and with minimal latency.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance
IOTPERF04-BP01-01**
_Create multiple queues
or data streams on the application side to channel different
payload types._

When working with publisher-subscriber type architectures,
make sure to structure topics in the message broker following
a scope and verb approach. With this strategy, you can
subscribe to messages for a given scope (for example, a
device) or refine the subscription on a given scope and verb.

**Prescriptive guidance
IOTPERF04-BP01-02**
_Choose the right
Quality of Service (QoS) for publishing the
messages._

- QoS 0 should be the default choice for all telemetry data
  that can cope with message loss and where data freshness
  is more important than reliability.
- QoS 1 provides reliable message transmission at the
  expense of increased latency, ordered ingestion in case of
  retries, and local memory consumption. It requires a local
  buffer for all unacknowledged messages.
- QoS 2 provides once and only once delivery of messages but
  increases the latency.

### Resources

- [Designing
  MQTT Topics for AWS IoT Core](../../../whitepapers/latest/designing-mqtt-topics-aws-iot-core/designing-mqtt-topics-aws-iot-core.md "../../../whitepapers/latest/designing-mqtt-topics-aws-iot-core/designing-mqtt-topics-aws-iot-core.md")
- [OASIS
  MQTT Version 5.0 QoS Specification](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html#_Toc3901103 "https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html#_Toc3901103")

| IOTPERF05: How do you optimize<br>telemetry data ingestion? |
| ----------------------------------------------------------- |
|                                                             |

IoT solutions drive rich analytics capabilities across vast
areas of crucial enterprise functions, such as operations,
customer care, finance, sales, and marketing. At the same
time, they can be used as efficient exit points for edge
gateways. Careful consideration must be given to architecting
highly efficient IoT implementations where data and analytics
are pushed to the cloud by devices and where machine learning
algorithms are pulled down to the device gateways from the
cloud.

Individual devices can be constrained by the throughput
supported over a given network. The frequency at which data is
exchanged must be balanced with the transport layer and the
ability of the device to optionally store, aggregate, and then
send data to the cloud. Send data from devices to the cloud at
timed intervals that align to the time required by backend
applications to process and take action on the data. For
example, if you need to see data at a one-second increment,
your device must send data at a more frequent time interval
than one second. Conversely, if your application only reads
data at an hourly rate, you can make a trade-off in
performance by aggregating data points at the edge and sending
the data every half hour.

The speed at which enterprise applications, business, and
operations need to gain visibility into IoT telemetry data
determines the most efficient point to process IoT data. In
network constrained environments where the hardware is not
limited, use edge solutions such as AWS IoT Greengrass to
operate and process data offline from the cloud. In cases
where both the network and hardware are constrained, look for
opportunities to compress message payloads by using binary
formatting and grouping similar messages together into a
single request.

For visualizations, several AWS services can be used. Amazon
Managed Service for Apache Flink can process streaming data in
real-time using SQL. Additionally, Quick Suite provides
business intelligence dashboards for IoT data visualization
with minimal setup. AWS IoT SiteWise offers purpose-built
visualization tools for industrial equipment data. For
operational monitoring, Amazon Managed Grafana enables
time-series data visualization with pre-built IoT dashboards,
while Amazon CloudWatch Dashboards can display IoT metrics and
alarms.

Evaluating and optimizing your IoT application for its
specific needs, whether telemetry data ingestion or
controlling devices in the field, improves your outcomes in
balancing performance and reliability within your hardware and
network constraints. Separating the way that your application
handles data collected through sensors or device probes from
command-and-control flows helps achieve more reliable
performance.

## IOTPERF05-BP01 Identify the ingestion mechanisms that best fit your use case

Identify which data ingestion method best fits with your use
case to obtain the best performance and operational complexity
tradeoff. Multiple mechanisms might be needed. This method
provides the optimal ingestion path for the data generated by
your devices to obtain the best trade-offs between performance
and cost.

**Level of risk exposed if this best
practice is not established: Low**

**Prescriptive guidance
IOTPERF05-BP01-01**
_Evaluate ingestion
mechanism for telemetry data._

- Determine if the communication pattern is unidirectional
  (device to backend) or bi-directional. For example:
  - HTTPS should be considered over MQTT when your device is
    acting as an aggregator. Use multiple threads and
    multiple HTTP connections to maximize the throughput for
    high delay networks as HTTP calls are synchronous.

- Consider the APIs provided by the destination for your data
  and adopt them if you can securely access them. For example:
  - AWS IoT SiteWise provides an HTTP API to ingest
    operational data from industrial applications which
    needs to be stored for a limited period and processed as
    a time series with hierarchical aggregation
    capabilities.
  - Real-time video (for example, video surveillance
    cameras) has specific characteristics that makes it more
    suitable to ingest in a dedicated service, such as
    Amazon Kinesis Video Streams.

- Consider the need for data to be buffered locally while the
  device is disconnected and the transmission resumed as soon
  as the connection is re-established. For example:
  - AWS IoT Greengrass stream manager provides a managed
    stream service with local persistence, local processing
    pipelines, and exporters to Amazon Kinesis Data Streams,
    AWS IoT SiteWise, and Amazon S3.

- Consider the latency, throughput, and ordering
  characteristics of the data you want to ingest. For example:
  - For applications with a high ingestion rate
    (high-frequency sensor data) and where message ordering
    is important, Amazon Kinesis Data Streams provides
    stream-oriented processing capabilities and the ability
    to act as temporary storage.
  - For applications that do not have any real time
    requirements (such as logging, large images) and when
    the devices have the possibility to store data locally,
    uploading data directly to Amazon S3 can be both
    performant and cost efficient.

### Resources

- [Device
  communication protocols](../../../iot/latest/developerguide/protocols.md "../../../iot/latest/developerguide/protocols.md")
- [AWS IoT SiteWise adds support for 10 new industrial protocols
  with Domatica EasyEdge integration](https://aws.amazon.com/blogs/iot/aws-iot-sitewise-adds-support-for-10-new-industrial-protocols-with-domatica-easyedge-integration/ "https://aws.amazon.com/blogs/iot/aws-iot-sitewise-adds-support-for-10-new-industrial-protocols-with-domatica-easyedge-integration/")
- [Amazon Kinesis Video Streams system requirements](../../../kinesisvideostreams/latest/dg/system-requirements.md "../../../kinesisvideostreams/latest/dg/system-requirements.md")

## IOTPERF05-BP02 Optimize data sent from devices to backend services

Optimizing the amount of data sent by the devices at the edge
allows the backend to better meet the processing targets set by
the business. Detailed data generated at the edge might have
little value for your application in its raw form.

**Level of risk exposed if this best
practice is not established: Medium**

**Prescriptive guidance
IOTPERF05-BP02-01**
_Aggregate or compress
data at the edge._

Aggregate data points at the edge before sending them to the
cloud, such as performing statistical aggregation, frequency
histograms, signal processing to reduce payload size and
consequently the load of the data transmission.

### Resources

- [Use
  AWS IoT SiteWise Edge gateways](../../../iot-sitewise/latest/userguide/gateways-ggv2.md "../../../iot-sitewise/latest/userguide/gateways-ggv2.md")
- [Cost-effectively ingest IoT data directly into Amazon S3 using AWS IoT Greengrass](../../../prescriptive-guidance/latest/patterns/cost-effectively-ingest-iot-data-directly-into-amazon-s3-using-aws-iot-greengrass.md "../../../prescriptive-guidance/latest/patterns/cost-effectively-ingest-iot-data-directly-into-amazon-s3-using-aws-iot-greengrass.md")

| IOTPERF06: How do you efficiently make<br>sure stored data is usable by business? |
| --------------------------------------------------------------------------------- |
|                                                                                   |

You may have multiple databases in your IoT application, each
selected for attributes such as the write frequency of data to
the database, the read frequency of data from the database,
and how the data is structured and queried. Consider some of
these other criteria when selecting a database offering:

- Volume of data and retention period
- Intrinsic data organization and structure
- Users and applications consuming the data (either raw or
  processed) and their geographical location and dispersion
- Advanced analytics needs, such as machine learning or
  real-time visualizations
- Data synchronization across other teams, organizations,
  and business units
- Security of the data at the row, table, and database
  levels
- Interactions with other related data-driven events such as
  enterprise applications, drill-through dashboards, or
  systems of interaction

## IOTPERF06-BP01 Store data in different tiers following formats, access patterns and methods

AWS has several database offerings that support IoT solutions.
For structured data, you should use Amazon Aurora, a highly
scalable relational interface to organizational data. For
semi-structured data that requires low latency for queries and
will be used by multiple consumers, use Amazon DynamoDB, a fully
managed, multi-Region database that provides consistent
single-digit millisecond latency and offers built-in security,
backup and restore, and in-memory caching.

AWS also provides specific data storage solutions for industrial
use cases with AWS IoT SiteWise. For equipment data, three tiers
are available:

- A hot storage tier optimized for real-time applications
- A warm storage tier optimized for analytical workloads
- A cold storage tier using Amazon Simple Storage Service
  (Amazon S3) for operational data applications with high
  latency tolerance

SiteWise helps you to reduce storage cost by keeping recent data
in the hot storage tier for at least 30 days and moving
historical data to a cost-optimized warm storage tier based upon
user-defined data retention policies.

Use Amazon SageMaker AI AI to build, train, and deploy machine
learning models based on your IoT data, in the cloud, and on the
edge using AWS IoT services, such as machine learning inference
in AWS IoT Greengrass.

Consider storing your raw formatted time series data in a data
warehouse solution such as Amazon Redshift. Unformatted data can
be imported to Amazon Redshift using Amazon S3 and Amazon Data
Firehose. By archiving unformatted data in a scalable, managed
data storage solution, you can begin to gain business insights,
explore your data, and identify trends and patterns over time.

In addition to storing and leveraging the historical trends of
your IoT data, you should have a system that stores the current
state of the device and provides the ability to query against
the current state of all of your devices. This supports internal
analytics and customer facing views into your IoT data.

The AWS IoT Device Shadow service is an effective mechanism to
store a virtual representation of your device in the cloud. AWS IoT Device Shadow service is best suited for managing the
current state of each device.

In addition, for internal teams that need to query against the
shadow for operational needs, use the managed capabilities of
fleet indexing, which provides a searchable index incorporating
your IoT registry and shadow metadata. If there is a need to
provide index-based searching or filtering capability to a large
number of external users, such as for a consumer application,
dynamically archive the shadow state using a combination of the
IoT rules engine, Amazon Data Firehose, and Amazon OpenSearch Service to store your data in a format that allows fine grained
query access for external users.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTPERF06-BP01-01**
_Create automated
mechanisms to transition data from tiers to implement
lifecycles._

In an IoT solution, data often follows a lifecycle, transitioning from real-time ingestion to historical storage and archiving. To efficiently verify that stored data is utilizable throughout its lifecycle, it's crucial to implement automated mechanisms that transition data across different storage tiers based on predefined rules and policies.

For example, you can use AWS IoT rules and AWS Lambda functions to automatically route incoming real-time data to Amazon DynamoDB or Amazon Timestream for low-latency access and processing. As the data ages, you can initiate automated processes to transition it to Amazon S3 or Amazon Glacier for cost-effective, long-term archival storage.

Additionally, you can implement data retention policies and lifecycle management rules within your data storage solutions. For instance, in Amazon DynamoDB, you can configure Time to Live (TTL) settings to automatically expire and remove data after a specified period, improving the efficiency of storage utilization and reducing costs.

By creating automated mechanisms to transition data across different storage tiers, you can optimize storage costs, make data accessible based on its lifecycle stage, and maintain data integrity and availability for various analytical and operational use cases throughout the data lifespan.

### Resources

- [Managing
  the lifecycle of objects](../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md "../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md")
- [Backing
  up and restoring Timestream tables: How it works](../../../timestream/latest/developerguide/backups-how-it-works.md "../../../timestream/latest/developerguide/backups-how-it-works.md")
- [RetentionProperties](../../../timestream/latest/developerguide/API_RetentionProperties.md "../../../timestream/latest/developerguide/API_RetentionProperties.md")
- [Manage
  data storage in AWS IoT SiteWise](../../../iot-sitewise/latest/userguide/manage-data-storage.md "../../../iot-sitewise/latest/userguide/manage-data-storage.md")
- [Configure
  storage settings in AWS IoT SiteWise](../../../iot-sitewise/latest/userguide/configure-storage.md "../../../iot-sitewise/latest/userguide/configure-storage.md")
