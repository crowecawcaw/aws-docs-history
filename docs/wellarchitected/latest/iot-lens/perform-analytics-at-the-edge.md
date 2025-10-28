# Perform analytics at the edge

Data preparation is usually required before analytics can be
performed at the edge.  There are various types of preparation
and transformation that can be done at the edge to improve the
sustainability of the solution:

- Data filtering: IoT edge devices can filter out irrelevant
  data or noise from sensor data streams. For example,
  temperature sensors may monitor and report temperature at a
  high rate, but reflecting those changes as they come may not
  be useful to a specific application or use case. By
  filtering out the unnecessary data points, edge devices can
  reduce the amount of data that needs to be transmitted and
  processed, reducing communication related power and cloud
  processing costs.
- Data aggregation: Devices can aggregate sensor data from
  multiple sources and over time to reduce the amount of data
  sent to the cloud. This can involve combining data from
  multiple sensors to create a single data stream, or
  aggregating data from multiple devices to provide a
  system-level view of performance or behavior.  This can
  reduce the number of connection requests as well as messages
  sent to the cloud.
- Data enrichment: Sensor data can be enriched with additional
  contextual information, such as location or time data. This
  can enable more accurate analysis and insights, as well as
  provide additional context for cloud applications or
  systems. This reduces the need to enrich data in the
  cloud.  Local processing and data enrichment should be
  considered when the cost of doing the same operation in the
  cloud out-weighs the impact of larger payloads and
  additional local computation and resources.
- Data normalization: Devices can normalize sensor data from
  different devices or sources to support consistency and
  compatibility with cloud applications or systems. This can
  involve converting data formats, units of measurement, or
  other data attributes to a common standard, reducing the
  need to do this in the cloud.

Devices can perform real-time analytics, predictive maintenance,
anomaly detection, optimization, and security monitoring by
analyzing sensor data and triggering alerts or actions based on
predefined rules or machine learning models, without sending the
source data to the cloud.

To perform analytics in an efficient and sustainable manner on
the edge, use lightweight algorithms to improve performance and
resource efficiency on IoT devices. Examples include algorithms
such as decision trees or regression models that are less
computationally intensive than deep learning models.  In
addition, optimizing data structures can improve the performance
and efficiency of analytics algorithms on IoT devices. Examples
include data structures such as binary trees or hash tables that
require less memory and processing power.
