# CloudWatch metric stream output in OpenTelemetry 1.0.0 format

###### Note

With the OpenTelemetry 1.0.0 format, metric attributes are 
 encoded as a list of `KeyValue` objects instead of the `StringKeyValue` type 
 used in the 0.7.0 format. As a consumer, this is the only major change between the 
 0.7.0 and 1.0.0 formats. A parser generated from the 0.7.0 proto files won't 
 parse metric attributes encoded in the 1.0.0 format. The same is true in reverse, a 
 parser generated from the 1.0.0 proto files will not parse metric attributes encoded in the 0.7.0 format.

OpenTelemetry is a collection of tools, APIs, and SDKs. 
 You can use it to instrument, generate, collect, and export telemetry data 
 (metrics, logs, and traces) for analysis. OpenTelemetry is part of the
 Cloud Native Computing Foundation. For more information, 
 see [OpenTelemetry](https://opentelemetry.io/ "https://opentelemetry.io/").

For information about the full OpenTelemetry 1.0.0 specification, 
 see [Release version 1.0.0](https://github.com/open-telemetry/opentelemetry-proto/releases/tag/v1.0.0 "https://github.com/open-telemetry/opentelemetry-proto/releases/tag/v1.0.0").

A Kinesis record can contain one or more `ExportMetricsServiceRequest`
 OpenTelemetry data structures. Each data structure starts with a header with an
 `UnsignedVarInt32` indicating the record length in bytes.
 Each `ExportMetricsServiceRequest` may contain data from multiple 
 metrics at once.

The following is a string representation of the message of 
 the `ExportMetricsServiceRequest`
 OpenTelemetry data structure. OpenTelemetry serializes the 
 Google Protocol Buffers binary protocol, and this is not human-readable.


```
resource_metrics {
  resource {
    attributes {
      key: "cloud.provider"
      value {
        string_value: "aws"
      }
    }
    attributes {
      key: "cloud.account.id"
      value {
        string_value: "123456789012"
      }
    }
    attributes {
      key: "cloud.region"
      value {
        string_value: "us-east-1"
      }
    }
    attributes {
      key: "aws.exporter.arn"
      value {
        string_value: "arn:aws:cloudwatch:us-east-1:123456789012:metric-stream/MyMetricStream"
      }
    }
  }
  scope_metrics {
    metrics {
      name: "amazonaws.com/AWS/DynamoDB/ConsumedReadCapacityUnits"
      unit: "NoneTranslated"
      summary {
        data_points {
          start_time_unix_nano: 60000000000
          time_unix_nano: 120000000000
          count: 1
          sum: 1.0
          quantile_values {
            value: 1.0
          }
          quantile_values {
            quantile: 0.95
            value: 1.0
          }
          quantile_values {
            quantile: 0.99
            value: 1.0
          }
          quantile_values {
            quantile: 1.0
            value: 1.0
          }
          attributes {
            key: "Namespace"
            value {
              string_value: "AWS/DynamoDB"
            }
          }
          attributes {
            key: "MetricName"
            value {
              string_value: "ConsumedReadCapacityUnits"
            }
          }
          attributes {
            key: "Dimensions"
            value {
              kvlist_value {
                values {
                  key: "TableName"
                  value {
                    string_value: "MyTable"
                  }
                }
              }
            }
          }
        }
        data_points {
          start_time_unix_nano: 70000000000
          time_unix_nano: 130000000000
          count: 2
          sum: 5.0
          quantile_values {
            value: 2.0
          }
          quantile_values {
            quantile: 1.0
            value: 3.0
          }
          attributes {
            key: "Namespace"
            value {
              string_value: "AWS/DynamoDB"
            }
          }
          attributes {
            key: "MetricName"
            value {
              string_value: "ConsumedReadCapacityUnits"
            }
          }
          attributes {
            key: "Dimensions"
            value {
              kvlist_value {
                values {
                  key: "TableName"
                  value {
                    string_value: "MyTable"
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
**Top-level object to serialize OpenTelemetry metric data**

`ExportMetricsServiceRequest` is the top-level wrapper to serialize
 an OpenTelemetry exporter payload. It contains one or more `ResourceMetrics`.


```
message ExportMetricsServiceRequest {
  // An array of ResourceMetrics.
  // For data coming from a single resource this array will typically contain one
  // element. Intermediary nodes (such as OpenTelemetry Collector) that receive
  // data from multiple origins typically batch the data before forwarding further and
  // in that case this array will contain multiple elements.
  repeated opentelemetry.proto.metrics.v1.ResourceMetrics resource_metrics = 1;
}
```
`ResourceMetrics` is the top-level object to represent MetricData objects.
 


```
// A collection of ScopeMetrics from a Resource.
message ResourceMetrics {
  reserved 1000;

  // The resource for the metrics in this message.
  // If this field is not set then no resource info is known.
  opentelemetry.proto.resource.v1.Resource resource = 1;

  // A list of metrics that originate from a resource.
  repeated ScopeMetrics scope_metrics = 2;

  // This schema_url applies to the data in the "resource" field. It does not apply
  // to the data in the "scope_metrics" field which have their own schema_url field.
  string schema_url = 3;
}
```
**The Resource object**

A `Resource` object is a value-pair object that contains some
 information about the resource that generated the metrics. For metrics created by
 AWS, the data structure contains the Amazon Resource Name (ARN) of the resource
 related to the metric, such as an EC2 instance or an S3 bucket.

The `Resource` object contains an attribute 
 called `attributes`, which store a list of key-value pairs.


* `cloud.account.id` contains the account ID
* `cloud.region` contains the Region
* `aws.exporter.arn` contains the metric stream ARN
* `cloud.provider` is always `aws`.

```
// Resource information.
message Resource {
  // Set of attributes that describe the resource.
  // Attribute keys MUST be unique (it is not allowed to have more than one
  // attribute with the same key).
  repeated opentelemetry.proto.common.v1.KeyValue attributes = 1;

  // dropped_attributes_count is the number of dropped attributes. If the value is 0, then
  // no attributes were dropped.
  uint32 dropped_attributes_count = 2;
}
```
**The ScopeMetrics object**

The `scope` field will not be filled. We fill only the metrics field
 that we are exporting.


```
// A collection of Metrics produced by an Scope.
message ScopeMetrics {
  // The instrumentation scope information for the metrics in this message.
  // Semantically when InstrumentationScope isn't set, it is equivalent with
  // an empty instrumentation scope name (unknown).
  opentelemetry.proto.common.v1.InstrumentationScope scope = 1;

  // A list of metrics that originate from an instrumentation library.
  repeated Metric metrics = 2;

  // This schema_url applies to all metrics in the "metrics" field.
  string schema_url = 3;
}
```
**The Metric object**

The metric object contains some metadata and a `Summary` data field 
 that contains a list of `SummaryDataPoint`.

For metric streams, the metadata is as follows:


* `name` will be 
`amazonaws.com/`metric_namespace`/`metric_name``
* `description` will be blank
* `unit` will be filled by mapping the metric datum's 
 unit to the case-sensitive variant of the Unified code for Units of Measure. For more information, see [Translations with OpenTelemetry 1.0.0 format in CloudWatch](CloudWatch-metric-streams-formats-opentelemetry-translation-100.md "CloudWatch-metric-streams-formats-opentelemetry-translation-100.md")
 and [The Unified Code For Units of Measure](https://ucum.org/ucum.html "https://ucum.org/ucum.html").
* `type` will be `SUMMARY`

```
message Metric {
  reserved 4, 6, 8;

  // name of the metric, including its DNS name prefix. It must be unique.
  string name = 1;

  // description of the metric, which can be used in documentation.
  string description = 2;

  // unit in which the metric value is reported. Follows the format
  // described by http://unitsofmeasure.org/ucum.html.
  string unit = 3;

  // Data determines the aggregation type (if any) of the metric, what is the
  // reported value type for the data points, as well as the relatationship to
  // the time interval over which they are reported.
  oneof data {
    Gauge gauge = 5;
    Sum sum = 7;
    Histogram histogram = 9;
    ExponentialHistogram exponential_histogram = 10;
    Summary summary = 11;
  }
}

message Summary {
  repeated SummaryDataPoint data_points = 1;
}
```
**The SummaryDataPoint object**

The SummaryDataPoint object contains the value of a single data point
 in a time series in a DoubleSummary metric.


```
// SummaryDataPoint is a single data point in a timeseries that describes the
// time-varying values of a Summary metric.
message SummaryDataPoint {
  reserved 1;

  // The set of key/value pairs that uniquely identify the timeseries from
  // where this point belongs. The list may be empty (may contain 0 elements).
  // Attribute keys MUST be unique (it is not allowed to have more than one
  // attribute with the same key).
  repeated opentelemetry.proto.common.v1.KeyValue attributes = 7;

  // StartTimeUnixNano is optional but strongly encouraged, see the
  // the detailed comments above Metric.
  //
  // Value is UNIX Epoch time in nanoseconds since 00:00:00 UTC on 1 January
  // 1970.
  fixed64 start_time_unix_nano = 2;

  // TimeUnixNano is required, see the detailed comments above Metric.
  //
  // Value is UNIX Epoch time in nanoseconds since 00:00:00 UTC on 1 January
  // 1970.
  fixed64 time_unix_nano = 3;

  // count is the number of values in the population. Must be non-negative.
  fixed64 count = 4;

  // sum of the values in the population. If count is zero then this field
  // must be zero.
  //
  // Note: Sum should only be filled out when measuring non-negative discrete
  // events, and is assumed to be monotonic over the values of these events.
  // Negative events *can* be recorded, but sum should not be filled out when
  // doing so.  This is specifically to enforce compatibility w/ OpenMetrics,
  // see: https://github.com/OpenObservability/OpenMetrics/blob/main/specification/OpenMetrics.md#summary
  double sum = 5;

  // Represents the value at a given quantile of a distribution.
  //
  // To record Min and Max values following conventions are used:
  // - The 1.0 quantile is equivalent to the maximum value observed.
  // - The 0.0 quantile is equivalent to the minimum value observed.
  //
  // See the following issue for more context:
  // https://github.com/open-telemetry/opentelemetry-proto/issues/125
  message ValueAtQuantile {
    // The quantile of a distribution. Must be in the interval
    // [0.0, 1.0].
    double quantile = 1;

    // The value at the given quantile of a distribution.
    //
    // Quantile values must NOT be negative.
    double value = 2;
  }

  // (Optional) list of values at different quantiles of the distribution calculated
  // from the current snapshot. The quantiles must be strictly increasing.
  repeated ValueAtQuantile quantile_values = 6;

  // Flags that apply to this specific data point.  See DataPointFlags
  // for the available flags and their meaning.
  uint32 flags = 8;
}
```
For more information, see [Translations with OpenTelemetry 1.0.0 format in CloudWatch](CloudWatch-metric-streams-formats-opentelemetry-translation-100.md "CloudWatch-metric-streams-formats-opentelemetry-translation-100.md").
