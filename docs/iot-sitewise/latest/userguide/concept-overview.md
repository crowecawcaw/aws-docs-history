# AWS IoT SiteWise concepts

The following are the core concepts of AWS IoT SiteWise:

**Aggregate**

Aggregates are fundamental metrics, or measurements, that AWS IoT SiteWise automatically calculates
for all time series data. For more information, see [Query asset property aggregates in AWS IoT SiteWise](aggregates.md "aggregates.md").

**Asset**

When you input, or ingest, data into AWS IoT SiteWise from your industrial equipment, your devices,
equipment, and processes are each shown as assets. Each asset has associated data. For example,
a piece of equipment might have a serial number, a location, a make and model, and an
installation date. It might also have time series values for availability, performance,
quality, temperature, pressure, and more. Group assets into hierarchies, allowing assets to
access data stored in their child assets. For more information, see [Model industrial assets](industrial-asset-models.md "industrial-asset-models.md").

**Asset hierarchy**

Set up asset hierarchies to create logical representations of your industrial operations.
To do this, define a hierarchy in an asset model and associate assets created from that model
with the specified hierarchy. Metrics in parent assets can combine data from the properties of
child assets, allowing you to calculate metrics that offer insights into your overall operation
or a specific part of it. For more information, see [Define asset model hierarchies](define-asset-hierarchies.md "define-asset-hierarchies.md").

**Asset model**

Every asset is made using an asset model. Asset models are structures that define and
standardize the format of your assets. They ensure consistent information across multiple
assets of the same type, allowing you to handle data in assets that represent groups of
devices. In each asset model, you can define [attributes](#concept-attribute "#concept-attribute"), time series inputs ([measurements](#concept-measurement "#concept-measurement")), time series transformations ([transforms](#concept-transform "#concept-transform")), time series aggregations ([metrics](#concept-metric "#concept-metric")),
and [asset hierarchies](#concept-hierarchy "#concept-hierarchy"). For more information, see [Model industrial assets](industrial-asset-models.md "industrial-asset-models.md").

Decide where your asset model's properties are processed by configuring your asset model
for the edge. Utilize this feature to handle and monitor asset data on your local
devices.

**Asset property**

Asset properties are the structures within each asset that hold industrial data. Each
property has a data type and can also have a unit. A property can be an [attribute](#concept-attribute "#concept-attribute"), a [measurement](#concept-measurement "#concept-measurement"), a [transform](#concept-transform "#concept-transform"), or a [metric](#concept-metric "#concept-metric"). For more information, see [Define data properties](asset-properties.md "asset-properties.md").

Configure asset properties to compute at the edge. For more information
about processing data at the edge, see [Set up an OPC UA source in
SiteWise Edge](configure-opcua-source.md "configure-opcua-source.md").

**Attribute**

Attributes are properties of an asset that typically stay constant, like the device
manufacturer or device location. Attributes can have preset values. Every asset created from an
asset model includes the default values of the attributes defined in that model. For more
information, see [Define static data (attributes)](attributes.md "attributes.md").

**Computation model**

A `ComputationModel` is an abstraction for certain types of compute that can enact on your data.
It defines the blueprint for a suite of computations, where users can describe input, output and
configuration for a specific computation engine.
`ComputationModel` is a new resource with ARN and is stateful and versioned. For more information, see
[Create a computation model (AWS CLI)](anom-detection-sensors-asset.md#create-computation-model "anom-detection-sensors-asset.md#create-computation-model").

**Dashboard**

Each project contains a set of dashboards. Dashboards provide a set of visualizations
for the values of a set of assets. Project owners create the dashboards and the
visualizations that it contains. When a project owner is ready to share the set of
dashboards, the owner can invite viewers to the project, which gives them access to all
dashboards in the project. If you want a different set of viewers for different
dashboards, you must divide the dashboards between projects. When viewers look at
dashboards, they can customize time range to look at specific data.

**Dataset**

Datasets are collections of data that represents time-series data, non-time-series data,
and non-equipment data such as shift schedules, maintenance records, and employee databases.
They support external data and use AWS IoT SiteWise analytic capabilities. It includes dataset sources,
dataset schema and dataset parameters. The AWS IoT SiteWise Assistant uses datasets that consume Amazon Kendra indexes.

**Data stream**

Input, or ingest, industrial data into AWS IoT SiteWise even before creating asset models and
assets. AWS IoT SiteWise automatically generates data streams to collect raw data streams from your
equipment.

**Data stream alias**

Data stream aliases help you easily identify a data stream. For example, the alias
`server1-windfarm/3/turbine/7/temperature` indicates temperature values coming from
turbine #7 in wind farm #3. The term `server1` is the data source name that helps
identify the OPC UA server, and `server1-` is a prefix attached to all data streams
reported from this OPC UA server.

**Data stream association**

After you create asset models and assets, associate data streams with asset properties
defined in your assets to structure your data. AWS IoT SiteWise can then use asset models and assets to
handle incoming data from your data streams. You can also disassociate data streams from asset
properties. For more information, see [Manage data streams for AWS IoT SiteWise](manage-data-streams.md "manage-data-streams.md").

**Destinations**

Destinations in SiteWise Edge represent the endpoints where you want to send your telemetry or
processed data. SiteWise Edge supports the AWS IoT SiteWise hot tier, buffered ingestion, or an Amazon S3 bucket as
destinations. You can configure destinations to subscribe to specific MQTT topics using path
filters. For more information, see [Understand AWS IoT SiteWise Edge destinations](gw-destinations.md#source-destination "gw-destinations.md#source-destination").

**Formula**

Each [transform](#concept-transform "#concept-transform") and [metric](#concept-metric "#concept-metric") property comes with a formula that outlines how the property transforms or
aggregates data. These formulas include property inputs, operators, and functions offered by
AWS IoT SiteWise. For more information, see [Use formula expressions](formula-expressions.md "formula-expressions.md").

**Interface**

An interface is a type of model that defines a standard structure that can be applied
to different asset models. For more information, see [Asset model interfaces](model-interfaces.md "model-interfaces.md").

**Measurement**

Measurements are properties of an asset that depict the raw sensor time series data
streams from a device or equipment. For more information, see [Define data streams from equipment (measurements)](measurements.md "measurements.md").

**Metric**

Metrics are properties of an asset that represent aggregated time series data. Each metric
is accompanied by a mathematical expression ([formula](#concept-formula "#concept-formula"))
that outlines how to aggregate data points and a time interval for computing that aggregation.
Metrics generate a single data point for each specified time interval. For more information,
see [Aggregate data from properties and other assets (metrics)](metrics.md "metrics.md").

**MQTT**

MQTT (Message Queuing Telemetry Transport) is a lightweight messaging protocol for sensors
and devices.

**Packs**

SiteWise Edge gateways use packs to determine how to collect, process, and route data. For more
information about the available packs for your SiteWise Edge gateway, see [Use packs to collect and process data in
SiteWise Edge](data-packs.md "data-packs.md").

Data collection pack

Use the data collection pack so that your SiteWise Edge gateway can collect your industrial
data and route it to the AWS destination of your choice.

Data processing pack

Use the data processing pack to process, store, and retrieve your data at the edge for
up to 30 days. Exchange edge-processed data to and from local applications through SiteWise Edge
APIs.

**OPC UA**

OPC UA (Open Platform Communications Unified Architecture) is a communication protocol for
industrial automation.

**Path filters**

Use path filters within a gateway to subscribe to MQTT topics and publish to AWS IoT SiteWise
supported destinations. MQTT-based sources, data processing pipelines, and destinations all
exchange data using MQTT topics on a self-hosted MQTT-enabled, V3 gateway. You can define topic
filters to specify the data you want to ingest or route to different destinations.

**Portal**

An AWS IoT SiteWise Monitor portal is a web application that you can use to visualize and share your
AWS IoT SiteWise data. A portal has one or more administrators and contains zero or more
projects.

**Portal administrator**

Each SiteWise Monitor portal has one or more portal administrators. Portal administrators use the
portal to create projects that contain collections of assets and dashboards. The portal
administrator then assigns assets and owners to each project. By controlling access to the
project, portal administrators specify which assets that project owners and viewers can
see.

**Project**

Each SiteWise Monitor portal contains a set of projects. Each project has a subset of your
AWS IoT SiteWise assets associated with it. Project owners create one or more dashboards to provide
a consistent way to view the data associated with those assets. Project owners can invite
viewers to the project to allow them to view the assets and dashboards in the project. The
project is the basic unit of sharing within SiteWise Monitor. Project owners can invite users who
were given access to the portal by the AWS administrator. A user must have access to a
portal before a project in that portal can be shared with that user.

**Project owner**

Each SiteWise Monitor project has owners. Project owners create visualizations in the form of
dashboards to represent operational data in a consistent manner. When dashboards are ready
to share, the project owner can invite viewers to the project. Project owners can also
assign other owners to the project. Project owners can configure thresholds and notification
settings for alarms.

**Project viewer**

Each SiteWise Monitor project has viewers. Project viewers can connect to the portal to view the
dashboards that project owners created. In each dashboard, project viewers can adjust the
time range to better understand operational data. Project viewers can only view dashboards
in the projects to which they have access. Project viewers can acknowledge and snooze
alarms.

**Property alias**

You have the option to create aliases on asset properties, such as an OPC UA server data
stream path (for example, /company/windfarm/3/turbine/7/temperature), simplifying the
identification of an asset property during the ingestion or retrieval of asset data. When you
use a [SiteWise Edge gateway](#concept-gateway "#concept-gateway") to ingest data from servers, your
property aliases must match the paths of your raw data streams. For more information, see [Manage data streams for AWS IoT SiteWise](manage-data-streams.md "manage-data-streams.md").

**Property notification**

When you enable property notifications for an asset property, AWS IoT SiteWise publishes an MQTT
message to AWS IoT Core each time that property receives a new value. The message payload includes
details about the update to that property value. Use property value notifications to create
solutions that connect your industrial data in AWS IoT SiteWise with other AWS services. For more
information, see [Interact with other AWS services](interact-with-other-services.md "interact-with-other-services.md").

**SiteWise Edge gateway**

A SiteWise Edge gateway is installed on the customer's premises to gather, handle, and direct
data. A SiteWise Edge gateway connects to your industrial data sources through various protocols to
gather and process data, sending it to the AWS cloud. SiteWise Edge gateways can also connect to
partner data sources. For more information, see [Use AWS IoT SiteWise Edge gateways](gateways.md "gateways.md").

**Transform**

Transforms are properties of an asset that represent transformed time series data. Every
transform is accompanied by a mathematical expression ([formula](#concept-formula "#concept-formula")) that specifies how to convert data points from one form to another. The
transformed data points hold a one-to-one relationship with the input data points. For more
information, see [Transform data (transforms)](transforms.md "transforms.md").

**Visualization**

In each dashboard, project owners decide how to display the properties and alarms of
the assets associated with the project. Availability might be represented as a line
chart, while other values might be displayed as bar charts or key performance indicators
(KPIs). Alarms are best displayed as status grids and status timelines. Project owners
customize each visualization to provide the best understanding of the data for that
asset.
