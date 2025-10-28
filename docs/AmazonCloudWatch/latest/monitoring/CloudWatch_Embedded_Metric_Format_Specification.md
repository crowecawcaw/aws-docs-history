# Specification: Embedded metric format

The CloudWatch embedded metric format is a JSON specification used to instruct CloudWatch Logs to automatically extract metric values embedded in structured log events.
You can use CloudWatch to graph and create alarms on the extracted metric values.
This section describes embedded metric format specification conventions and the embedded metric format document structure.

## Embedded metric format

specification conventions

The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this
format specification are to be interpreted as described in [Key Words RFC2119](http://tools.ietf.org/html/rfc2119 "http://tools.ietf.org/html/rfc2119").

The terms "JSON", "JSON text", "JSON value", "member", "element", "object", "array", "number", "string", "boolean", "true", "false", and
"null" in this format specification are to be interpreted as defined in [JavaScript Object Notation RFC8259](https://tools.ietf.org/html/rfc8259 "https://tools.ietf.org/html/rfc8259").

###### Note

If you plan to create alarms on metrics created using embedded metric format, see
[Setting alarms on metrics created with the embedded metric format](CloudWatch_Embedded_Metric_Format_Alarms.md "CloudWatch_Embedded_Metric_Format_Alarms.md") for recommendations.

## Embedded metric format

document structure

This section describes the structure of an embedded metric format document. Embedded metric format documents are defined in
[JavaScript Object Notation RFC8259](https://tools.ietf.org/html/rfc8259 "https://tools.ietf.org/html/rfc8259").

Unless otherwise noted, objects defined by this specification MUST NOT contain any additional members.
Members not recognized by this specification MUST be ignored. Members defined in this specification are case-sensitive.

The embedded metric format is subject to the same limits as standard CloudWatch Logs events and are limited to a maximum size of 1 MB.

With the embedded metric format,
you can track the processing
of your EMF logs
by metrics
that are published
in the `AWS/Logs` namespace
of your account.
These can be used
to track failed metric generation
from EMF,
as well as whether failures happen due
to parsing or validation.
For more details see [Monitoring with CloudWatch metrics](../logs/CloudWatch-Logs-Monitoring-CloudWatch-Metrics.md "../logs/CloudWatch-Logs-Monitoring-CloudWatch-Metrics.md").

### Root node

The LogEvent message MUST be a valid JSON object with no additional data at the beginning or end of the LogEvent message string.
For more information about the LogEvent structure, see [InputLogEvent](../../../AmazonCloudWatchLogs/latest/APIReference/API_InputLogEvent.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_InputLogEvent.md").

Embedded metric format documents MUST contain the following top-level member on the root node. This is a [Metadata
object](#CloudWatch_Embedded_Metric_Format_Specification_structure_metadata "#CloudWatch_Embedded_Metric_Format_Specification_structure_metadata") object.

```
{
 "_aws": {
    "CloudWatchMetrics": [ ... ]
  }
}
```

The root node MUST contain all [Target
members](#CloudWatch_Embedded_Metric_Format_Specification_structure_target "#CloudWatch_Embedded_Metric_Format_Specification_structure_target") members defined by the references in the
[MetricDirective object](#CloudWatch_Embedded_Metric_Format_Specification_structure_metricdirective "#CloudWatch_Embedded_Metric_Format_Specification_structure_metricdirective").

The root node MAY contain any other members that are not included in the above requirements. The values of these members MUST be valid JSON types.

### Metadata

object

The `_aws` member can be used to represent metadata about the payload that informs downstream
services how they should process the LogEvent. The value MUST be an object and MUST contain the following members:

- **CloudWatchMetrics**— An array of [MetricDirective object](#CloudWatch_Embedded_Metric_Format_Specification_structure_metricdirective "#CloudWatch_Embedded_Metric_Format_Specification_structure_metricdirective") used to
  instruct CloudWatch to extract metrics from the root node of the LogEvent.

```
{
  "_aws": {
    "CloudWatchMetrics": [ ... ]
  }
}
```

- **Timestamp**— A number representing the time stamp used for metrics
  extracted from the event. Values MUST be expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.

```
{
  "_aws": {
    "Timestamp": 1559748430481
  }
}
```

### MetricDirective object

The MetricDirective object instructs downstream services that the LogEvent contains metrics that will be extracted and published to CloudWatch.
MetricDirectives MUST contain the following members:

- **Namespace**— A string representing the CloudWatch namespace for the metric.
- **Dimensions**— A [DimensionSet array](#CloudWatch_Embedded_Metric_Format_Specification_structure_dimensionset "#CloudWatch_Embedded_Metric_Format_Specification_structure_dimensionset").
- **Metrics**— An array of [MetricDefinition](#CloudWatch_Embedded_Metric_Format_Specification_structure_metricdefinition "#CloudWatch_Embedded_Metric_Format_Specification_structure_metricdefinition") objects.
  This array MUST NOT contain more than 100 MetricDefinition objects.

### DimensionSet array

A DimensionSet is an array of strings containing the dimension keys that will be applied to all metrics in the document.
The values within this array MUST also be members on the root-node—referred to as the
[Target
members](#CloudWatch_Embedded_Metric_Format_Specification_structure_target "#CloudWatch_Embedded_Metric_Format_Specification_structure_target")

A DimensionSet MUST NOT contain more than 30 dimension keys. A DimensionSet MAY be empty.

The target member MUST have a string value. This value MUST NOT contain more than 1024 characters. The target member defines a dimension that will be published as part of the metric identity.
Every DimensionSet used creates a new metric in CloudWatch. For more information about dimensions, see [Dimension](../APIReference/API_Dimension.md "../APIReference/API_Dimension.md")
and [Dimensions](cloudwatch_concepts.md#Dimension "cloudwatch_concepts.md#Dimension").

```
{
 "_aws": {
   "CloudWatchMetrics": [
     {
       "Dimensions": [ [ "functionVersion" ] ],
       ...
     }
   ]
 },
 "functionVersion": "$LATEST"
}
```

###### Note

Be careful when configuring your metric extraction as it impacts your custom metric usage and corresponding bill.
If you unintentionally create metrics based on high-cardinality dimensions (such as `requestId`), the embedded metric format will by design create
a custom metric corresponding to each unique dimension combination. For more information, see [Dimensions](cloudwatch_concepts.md#Dimension "cloudwatch_concepts.md#Dimension").

### MetricDefinition object

A MetricDefinition is an object that MUST contain the following member:

- **Name**— A string [Reference values](#CloudWatch_Embedded_Metric_Format_Specification_structure_referencevalues "#CloudWatch_Embedded_Metric_Format_Specification_structure_referencevalues") to a metric [Target
  members](#CloudWatch_Embedded_Metric_Format_Specification_structure_target "#CloudWatch_Embedded_Metric_Format_Specification_structure_target"). Metric targets MUST be
  either a numeric value or an array of numeric values.

A MetricDefinition object MAY contain the following members:

- **Unit**— An OPTIONAL string value representing the unit of measure for the
  corresponding metric. Values SHOULD be valid CloudWatch metric units. For information about valid units,
  see [MetricDatum](../APIReference/API_MetricDatum.md "../APIReference/API_MetricDatum.md").
  If a value is not provided, then a default value of NONE is assumed.
- **StorageResolution**— An OPTIONAL integer value
  representing the storage resolution for the corresponding metric. Setting this to 1 specifies
  this metric as a high-resolution metric, so that
  CloudWatch stores the metric with sub-minute resolution down to one second. Setting this to 60 specifies
  this metric as standard-resolution, which CloudWatch stores at 1-minute resolution. Values SHOULD be valid
  CloudWatch supported resolutions, 1 or 60. If a value is not provided, then a default value of 60 is assumed.

For more information about high-resolution metrics, see
[High-resolution metrics](publishingMetrics.md#high-resolution-metrics "publishingMetrics.md#high-resolution-metrics").

###### Note

If you plan to create alarms on metrics created using embedded metric format, see
[Setting alarms on metrics created with the embedded metric format](CloudWatch_Embedded_Metric_Format_Alarms.md "CloudWatch_Embedded_Metric_Format_Alarms.md") for recommendations.

```
{
  "_aws": {
    "CloudWatchMetrics": [
      {
        "Metrics": [
          {
            "Name": "Time",
            "Unit": "Milliseconds",
            "StorageResolution": 60
          }
        ],
        ...
      }
    ]
  },
  "Time": 1
}
```

### Reference values

Reference values are string values that reference [Target
members](#CloudWatch_Embedded_Metric_Format_Specification_structure_target "#CloudWatch_Embedded_Metric_Format_Specification_structure_target") members on the root node.
These references should NOT be confused with the JSON Pointers described in [RFC6901](https://tools.ietf.org/html/rfc6901 "https://tools.ietf.org/html/rfc6901"). Target values cannot be nested.

### Target

members

Valid targets MUST be members on the root node and cannot be nested objects. For example, a \_reference\_ value of `"A.a"`
MUST match the following member:

```
{ "A.a" }
```

It MUST NOT match the nested member:

```
{ "A": { "a" } }
```

Valid values of target members depend on what is referencing them. A metric target MUST
be a numeric value or an array of numeric values. Numeric array metric targets MUST NOT
have more than 100 members. A dimension target MUST have a string value.

### Embedded metric

format example and JSON schema

The following is a valid example of embedded metric format.

```
{
  "_aws": {
    "Timestamp": 1574109732004,
    "CloudWatchMetrics": [
      {
        "Namespace": "lambda-function-metrics",
        "Dimensions": [["functionVersion"]],
        "Metrics": [
          {
            "Name": "time",
            "Unit": "Milliseconds",
            "StorageResolution": 60
          }
        ]
      }
    ]
  },
  "functionVersion": "$LATEST",
  "time": 100,
  "requestId": "989ffbf8-9ace-4817-a57c-e4dd734019ee"
}
```

You can use the following schema to validate embedded metric format documents.

```
{
    "type": "object",
    "title": "Root Node",
    "required": [
        "_aws"
    ],
    "properties": {
        "_aws": {
            "$id": "#/properties/_aws",
            "type": "object",
            "title": "Metadata",
            "required": [
                "Timestamp",
                "CloudWatchMetrics"
            ],
            "properties": {
                "Timestamp": {
                    "$id": "#/properties/_aws/properties/Timestamp",
                    "type": "integer",
                    "title": "The Timestamp Schema",
                    "examples": [
                        1565375354953
                    ]
                },
                "CloudWatchMetrics": {
                    "$id": "#/properties/_aws/properties/CloudWatchMetrics",
                    "type": "array",
                    "title": "MetricDirectives",
                    "items": {
                        "$id": "#/properties/_aws/properties/CloudWatchMetrics/items",
                        "type": "object",
                        "title": "MetricDirective",
                        "required": [
                            "Namespace",
                            "Dimensions",
                            "Metrics"
                        ],
                        "properties": {
                            "Namespace": {
                                "$id": "#/properties/_aws/properties/CloudWatchMetrics/items/properties/Namespace",
                                "type": "string",
                                "title": "CloudWatch Metrics Namespace",
                                "examples": [
                                    "MyApp"
                                ],
                                "pattern": "^(.*)$",
                                "minLength": 1,
                                "maxLength": 1024
                            },
                            "Dimensions": {
                                "$id": "#/properties/_aws/properties/CloudWatchMetrics/items/properties/Dimensions",
                                "type": "array",
                                "title": "The Dimensions Schema",
                                "minItems": 1,
                                "items": {
                                    "$id": "#/properties/_aws/properties/CloudWatchMetrics/items/properties/Dimensions/items",
                                    "type": "array",
                                    "title": "DimensionSet",
                                    "minItems": 0,
                                    "maxItems": 30,
                                    "items": {
                                        "$id": "#/properties/_aws/properties/CloudWatchMetrics/items/properties/Dimensions/items/items",
                                        "type": "string",
                                        "title": "DimensionReference",
                                        "examples": [
                                            "Operation"
                                        ],
                                        "pattern": "^(.*)$",
                                        "minLength": 1,
                                        "maxLength": 250
}
                                }
                            },
                            "Metrics": {
                                "$id": "#/properties/_aws/properties/CloudWatchMetrics/items/properties/Metrics",
                                "type": "array",
                                "title": "MetricDefinitions",
                                "items": {
                                    "$id": "#/properties/_aws/properties/CloudWatchMetrics/items/properties/Metrics/items",
                                    "type": "object",
                                    "title": "MetricDefinition",
                                    "required": [
                                        "Name"
                                    ],
                                    "properties": {
                                        "Name": {
                                            "$id": "#/properties/_aws/properties/CloudWatchMetrics/items/properties/Metrics/items/properties/Name",
                                            "type": "string",
                                            "title": "MetricName",
                                            "examples": [
                                                "ProcessingLatency"
                                            ],
                                            "pattern": "^(.*)$",
                                            "minLength": 1,
                                            "maxLength": 1024
                                        },
                                        "Unit": {
                                            "$id": "#/properties/_aws/properties/CloudWatchMetrics/items/properties/Metrics/items/properties/Unit",
                                            "type": "string",
                                            "title": "MetricUnit",
                                            "examples": [
                                                "Milliseconds"
                                            ],
                                            "pattern": "^(Seconds|Microseconds|Milliseconds|Bytes|Kilobytes|Megabytes|Gigabytes|Terabytes|Bits|Kilobits|Megabits|Gigabits|Terabits|Percent|Count|Bytes\\/Second|Kilobytes\\/Second|Megabytes\\/Second|Gigabytes\\/Second|Terabytes\\/Second|Bits\\/Second|Kilobits\\/Second|Megabits\\/Second|Gigabits\\/Second|Terabits\\/Second|Count\\/Second|None)$"
                                         },
                                         "StorageResolution": {
                                            "$id": "#/properties/_aws/properties/CloudWatchMetrics/items/properties/Metrics/items/properties/StorageResolution",
                                            "type": "integer",
                                            "title": "StorageResolution",
                                            "examples": [
                                                60
                                            ]
                                         }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
```

## Entity information in EMF format

When you publish logs to Amazon CloudWatch using Embedded Metric Format (EMF), you can include entity information in the log event. This section describes how to specify entity information and how CloudWatch processes this information.

### Entity types

When no Entity is specified with the `PutLogEvents` request, CloudWatch will look for entity information in the EMF log content:

- **Service-type entities**

Required fields: `Service` and `Environment`

- **Resource-type entities**

Required fields: `ResourceType` and `Identifier`

### Platform attributes

CloudWatch automatically determines the platform type based on these attributes:

- **Kubernetes (K8s):**

Required: `K8s.Cluster`

Optional: `K8s.Namespace`, `K8s.Workload`, `K8s.Node`, `K8s.Pod`, `EC2.InstanceId`, `EC2.AutoScalingGroup`

- **Amazon EKS**

Required: `EKS.Cluster`

Optional: `K8s.Namespace`, `K8s.Workload`, `K8s.Node`, `K8s.Pod`, `EC2.InstanceId`

- **Amazon ECS:**

Required: `ECS.Cluster`

Optional: `ECS.Service`, `ECS.Task`

- **Amazon EC2**

Required: `EC2.InstanceId`

Optional: `EC2.AutoScalingGroup`

- **Lambda:**

Required: `Lambda.Function`

- **Generic hosts:**

Required: `Host`

### Example EMF log format

```
{
    "_aws": {
        "CloudWatchMetrics": [
            {
                "Metrics": [
                    {"Name": "RequestLatency", "Unit": "Milliseconds"}
                ],
                "Namespace": "MyApplication"
            }
        ]
    },
    "Service": "PaymentService",
    "Environment": "Production",
    "K8s.Cluster": "main-cluster",
    "K8s.Namespace": "payment-ns",
    "K8s.Pod": "payment-pod-123",
    "K8s.Node": "worker-node-1",
    "K8s.Workload": "payment-deployment",
    "RequestLatency": 135.5,
    "timestamp": 1622163600000
}
```

### Generated Entity

The above EMF log will generate the following Entity:

```
{
    "KeyAttributes": {
        "Type": "Service",
        "Name": "PaymentService",
        "Environment": "Production"
    },
    "Attributes": {
        "PlatformType": "K8s",
        "K8s.Cluster": "main-cluster",
        "K8s.Namespace": "payment-ns",
        "K8s.Pod": "payment-pod-123",
        "K8s.Node": "worker-node-1",
        "K8s.Workload": "payment-deployment"
    }
}
```

### Entity processing

CloudWatch processes the entity information as follows:

- **KeyAttributes:**
  - Determines entity type based on required fields
  - For Service-type, extracts Service name and Environment
  - These become the primary identifiers for the entity

- **Attributes:**
  - Sets PlatformType based on included platform attributes
  - Includes all relevant platform-specific information
  - Maintains relationship context for the telemetry data

CloudWatch uses this entity information to establish relationships between different pieces of telemetry data, enabling enhanced observability and contextual analysis of your applications and infrastructure. For more information,
see [How to add related information to custom telemetry sent to CloudWatch](adding-your-own-related-telemetry.md "adding-your-own-related-telemetry.md") .

###### Note

Entity information helps CloudWatch create a complete picture of your application's telemetry data and its relationships within your infrastructure.
