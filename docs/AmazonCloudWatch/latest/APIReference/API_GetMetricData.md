# GetMetricData

You can use the `GetMetricData` API to retrieve CloudWatch metric
 values. The operation can also include a CloudWatch Metrics Insights query, and
 one or more metric math functions.

A `GetMetricData` operation that does not include a query can retrieve
 as many as 500 different metrics in a single request, with a total of as many as 100,800
 data points. You can also optionally perform metric math expressions on the values of
 the returned statistics, to create new time series that represent new insights into your
 data. For example, using Lambda metrics, you could divide the Errors metric by the
 Invocations metric to get an error rate time series. For more information about metric
 math expressions, see [Metric Math Syntax and Functions](../monitoring/using-metric-math.md#metric-math-syntax "../monitoring/using-metric-math.md#metric-math-syntax") in the *Amazon CloudWatch User
 Guide*.

If you include a Metrics Insights query, each `GetMetricData` operation can
 include only one query. But the same `GetMetricData` operation can also
 retrieve other metrics. Metrics Insights queries can query only the most recent three
 hours of metric data. For more information about Metrics Insights, see [Query your metrics with CloudWatch Metrics Insights](../monitoring/query_with_cloudwatch-metrics-insights.md "../monitoring/query_with_cloudwatch-metrics-insights.md").

Calls to the `GetMetricData` API have a different pricing structure than
 calls to `GetMetricStatistics`. For more information about pricing, see
 [Amazon CloudWatch
 Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

Amazon CloudWatch retains metric data as follows:


* Data points with a period of less than 60 seconds are available for 3
 hours. These data points are high-resolution metrics and are available only for
 custom metrics that have been defined with a `StorageResolution` of
 1.
* Data points with a period of 60 seconds (1-minute) are available for 15
 days.
* Data points with a period of 300 seconds (5-minute) are available for 63
 days.
* Data points with a period of 3600 seconds (1 hour) are available for 455
 days (15 months).
Data points that are initially published with a shorter period are aggregated
 together for long-term storage. For example, if you collect data using a period of 1
 minute, the data remains available for 15 days with 1-minute resolution. After 15 days,
 this data is still available, but is aggregated and retrievable only with a resolution
 of 5 minutes. After 63 days, the data is further aggregated and is available with a
 resolution of 1 hour.

If you omit `Unit` in your request, all data that was collected with any
 unit is returned, along with the corresponding units that were specified when the data
 was reported to CloudWatch. If you specify a unit, the operation returns only data that
 was collected with that unit specified. If you specify a unit that does not match the
 data collected, the results of the operation are null. CloudWatch does not perform unit
 conversions.


**Using Metrics Insights queries with metric
 math**


You can't mix a Metric Insights query and metric math syntax in the same expression,
 but you can reference results from a Metrics Insights query within other Metric math
 expressions. A Metrics Insights query without a **GROUP
 BY** clause returns a single time-series (TS), and can be used as input for
 a metric math expression that expects a single time series. A Metrics Insights query
 with a **GROUP BY** clause returns an array of time-series
 (TS[]), and can be used as input for a metric math expression that expects an array of
 time series. 


## Request Parameters





**EndTime** 


The time stamp indicating the latest data to be returned.


The value specified is exclusive; results include data points up to the specified
 time stamp.


For better performance, specify `StartTime` and `EndTime` values
 that align with the value of the metric's `Period` and sync up with the
 beginning and end of an hour. For example, if the `Period` of a metric is 5
 minutes, specifying 12:05 or 12:30 as `EndTime` can get a faster response
 from CloudWatch than setting 12:07 or 12:29 as the `EndTime`.


Type: Timestamp


Required: Yes




**LabelOptions** 


This structure includes the `Timezone` parameter, which you can use to
 specify your time zone so that the labels of returned data display the correct time for
 your time zone. 


Type: [LabelOptions](API_LabelOptions.md "API_LabelOptions.md") object


Required: No




**MaxDatapoints** 


The maximum number of data points the request should return before paginating. If you
 omit this, the default of 100,800 is used.


Type: Integer


Required: No




**MetricDataQueries** 


The metric queries to be returned. A single `GetMetricData` call can
 include as many as 500 `MetricDataQuery` structures. Each of these structures
 can specify either a metric to retrieve, a Metrics Insights query, or a math expression
 to perform on retrieved data. 


Type: Array of [MetricDataQuery](API_MetricDataQuery.md "API_MetricDataQuery.md") objects


Required: Yes




**NextToken** 


Include this value, if it was returned by the previous `GetMetricData`
 operation, to get the next set of data points.


Type: String


Required: No




**ScanBy** 


The order in which data points should be returned. `TimestampDescending`
 returns the newest data first and paginates when the `MaxDatapoints` limit is
 reached. `TimestampAscending` returns the oldest data first and paginates
 when the `MaxDatapoints` limit is reached.


If you omit this parameter, the default of `TimestampDescending` is
 used.


Type: String


Valid Values: `TimestampDescending | TimestampAscending`



Required: No




**StartTime** 


The time stamp indicating the earliest data to be returned.


The value specified is inclusive; results include data points with the specified
 time stamp. 


CloudWatch rounds the specified time stamp as follows:



* Start time less than 15 days ago - Round down to the nearest whole minute.
 For example, 12:32:34 is rounded down to 12:32:00.
* Start time between 15 and 63 days ago - Round down to the nearest 5-minute
 clock interval. For example, 12:32:34 is rounded down to 12:30:00.
* Start time greater than 63 days ago - Round down to the nearest 1-hour
 clock interval. For example, 12:32:34 is rounded down to 12:00:00.

If you set `Period` to 5, 10, 20, or 30, the start time of your request is
 rounded down to the nearest time that corresponds to even 5-, 10-, 20-, or 30-second
 divisions of a minute. For example, if you make a query at (HH:mm:ss) 01:05:23 for the
 previous 10-second period, the start time of your request is rounded down and you
 receive data from 01:05:10 to 01:05:20. If you make a query at 15:07:17 for the previous
 5 minutes of data, using a period of 5 seconds, you receive data timestamped between
 15:02:15 and 15:07:15. 


For better performance, specify `StartTime` and `EndTime` values
 that align with the value of the metric's `Period` and sync up with the
 beginning and end of an hour. For example, if the `Period` of a metric is 5
 minutes, specifying 12:05 or 12:30 as `StartTime` can get a faster response
 from CloudWatch than setting 12:07 or 12:29 as the `StartTime`.


Type: Timestamp


Required: Yes




## Response Elements


The following elements are returned by the service.





**Messages** 


Contains a message about this `GetMetricData` operation, if the operation
 results in such a message. An example of a message that might be returned is
 `Maximum number of allowed metrics exceeded`. If there is a message, as
 much of the operation as possible is still executed.


A message appears here only if it is related to the global `GetMetricData`
 operation. Any message about a specific metric returned by the operation appears in the
 `MetricDataResult` object returned for that metric.


Type: Array of [MessageData](API_MessageData.md "API_MessageData.md") objects




**MetricDataResults** 


The metrics that are returned, including the metric name, namespace, and
 dimensions.


Type: Array of [MetricDataResult](API_MetricDataResult.md "API_MetricDataResult.md") objects




**NextToken** 


A token that marks the next batch of returned results.


Type: String




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**InvalidNextToken** 


The next token specified is invalid.





**message** 





HTTP Status Code: 400




## Examples


### Example


The following example requests a Metrics Insights query for aggregated
 `CPUUtilization`, and a metric.


#### Sample Request



```
{
    "StartTime": 1637061900,
    "EndTime": 1637074500,
    "MetricDataQueries": [
        {
            "Expression": "SELECT AVG(CPUUtilization) FROM SCHEMA(\"AWS/EC2\", InstanceId)",
            "Id": "q1",
            "Period": 300,
            "Label": "Cluster CpuUtilization"
        },
        {
            "Id": "m1",
            "Label": "Unhealthy Behind Load Balancer",
            "MetricStat": {
                "Metric": {
                    "Namespace": "AWS/ApplicationELB",
                    "MetricName": "UnHealthyHostCount",
                    "Dimensions": [
                        {
                            "Name": "TargetGroup",
                            "Value": "targetgroup/EC2Co-Defau-EXAMPLEWNAD/89cc68152b367e5f"
                        },
                        {
                            "Name": "LoadBalancer",
                            "Value": "app/EC2Co-EcsEl-EXAMPLE69Q/fdd2210e799e4376"
                        }
                    ]
                },
                "Period": 300,
                "Stat": "Average"
            }
        }
    ]
}
```

#### Sample Response



```
{
    "Messages": [],
    "MetricDataResults": [
        {
            "Id": "m1",
            "Label": "Unhealthy Behind Load Balancer",
            "StatusCode": "Complete",
            "Timestamps": [
                1637074200,      
                1637073900,
                1637073600
            ],
            "Values": [
                0,
                0,
                0
            ]
        },
        {
            "Id": "q1",
            "Label": "Cluster CpuUtilization",
            "StatusCode": "Complete",
            "Timestamps": [
                1637074245,
                1637073945,
                1637073645
            ],
            "Values": [
                1.2158469945359334,
                0.8678863271635757,
                0.7201860957623283
            ]
        }
    ]
}
```

### Example


The following example includes a Metrics Insights query for that is given the
 ID `error_rate`. The returned results of the query are then used in
 the metric math expression to return `availability`. 


#### Sample Request



```
{
    "StartTime": 1518867432,
    "EndTime": 1518868032,
    "MetricQueries": [
        {
            "Id": "availability",
            "Expression": "(1 - error_rate) * 100",
            "Label": "Availability"
        },
        {
            "Id": " error_rate",
            "Expression": "SELECT AVG(ErrorRate) FROM MyService",
            "Period": 300,
            "ReturnData": false
        }
    ]
}
```

### Example


The following example requests three separate metrics across two namespaces.
 The labels of the first two metrics use dynamic labels to display the peak value
 of `CPUUtilization` during the time shown on the graph, and also the
 time that the peak value was recorded. The `Timezone` setting
 specifies that the times shown in those dynamic labels reflect the United States
 Eastern time zone, which is 4 hours behind UTC.


#### Sample Request



```
{
  "StartTime": 1518867432,
  "EndTime": 1518868232,
  "LabelOptions": {
    "Timezone" : "-0400"
    },
  "MetricDataQueries": [
    {
      "Id": "m1",
      "Label": "CPUUtilization, peak of ${MAX} was at ${MAX_TIME}",
      "MetricStat": {
        "Metric": {
          "Namespace": "AWS/EC2",
          "MetricName": "CPUUtilization",
          "Dimensions": [
            {
              "Name": "InstanceId",
              "Value": "i-1234567890abcdef0"
            }
          ]
        },
        "Period": 300,
        "Stat": "Average"
      }
    },
    {
      "Id": "m2",
      "Label": "CPUUtilization, peak of ${MAX} was at ${MAX_TIME}",
      "MetricStat": {
        "Metric": {
          "Namespace": "AWS/EC2",
          "MetricName": "CPUUtilization",
          "Dimensions": [
            {
              "Name": "InstanceId",
              "Value": "i-111111111111111111"
            }
          ]
        },
        "Period": 300,
        "Stat": "Average"
      }
    },
    {
      "Id": "m3",
      "MetricStat": {
        "Metric": {
          "Namespace": "AWS/ELB",
          "MetricName": "HealthyHostCount",
          "Dimensions": [
            {
              "Name": "LoadBalancerName",
              "Value": "my-lb-B"
            }
          ]
        },
        "Period": 300,
        "Stat": "Sum",
        "Unit": "None"
      }
    }
  ]
}
```

#### Sample Response



```
{
  "MetricDataResults": [
    {
      "Id": "m1",
      "StatusCode": "Complete",
      "Label": "CPUUtilization, peak of 31.5 was at 1-22 13:05",
      "Timestamps": [
        1518868032,      
        1518867732,
        1518867432
      ],
      "Values": [
        15000,
        14000,
        16000
      ]
    },
    {
      "Id": "m2",
      "StatusCode": "Complete",
      "Label": "CPUUtilization, peak of 63.2 was at 1-22 13:20",
      "Timestamps": [
        1518868032,
        1518867732,
        1518867432
      ],
      "Values": [
        15,
        14,
        16
      ]
    },
    {
      "Id": "m3",
      "StatusCode": "Complete",
      "Label": "AWS/EC2 HealthyHostCount",
      "Timestamps": [
        1518868032,
        1518867732,
        1518867432
      ],
      "Values": [
        15,
        14,
        16
      ]
    }
  ]
}
```

### Example


The following example retrieves the `NetworkOut` metric for two
 Auto Scaling groups, and uses them in an expression. These two metrics are
 called m1 and m2, and the expression calculates e1 as the results of m2/m1. The
 raw values and time stamps of the `NetworkOut` metrics are not
 returned.


#### Sample Request



```
{
  "StartTime": 1518867432,
  "EndTime": 1518868232,
  "MetricQueries": [
    {
      "Id": "e1",
      "Expression": "m2 / m1",
      "Label": "my-asg-B / my-asg-A"
    },
    {
      "Id": "m1",
      "MetricStat": {
        "Metric": {
          "Namespace": "AWS/EC2",
          "MetricName": "NetworkOut",
          "Dimensions": [
            {
              "Name": "AutoScalingGroupName",
              "Value": "my-asg-A"
            }
          ]
        },
        "Period": 300,
        "Stat": "SampleCount",
        "Unit": "Bytes"
      },
      "ReturnData": false
    },
    {
      "Id": "m2",
      "MetricStat": {
        "Metric": {
          "Namespace": "AWS/EC2",
          "MetricName": "NetworkOut",
          "Dimensions": [
            {
              "Name": "AutoScalingGroupName",
              "Value": "my-asg-B"
            }
          ]
        },
        "Period": 300,
        "Stat": "SampleCount",
        "Unit": "Bytes"
      },
      "ReturnData": false
    }
  ]
}
```

#### Sample Response



```
{
  "MetricDataResults": [
    {
      "Id": "m1",
      "StatusCode": "Complete"
    },
    {
      "Id": "m2",
      "StatusCode": "Complete"
    },
    {
      "Id": "e1",
      "StatusCode": "Complete",
      "Label": "my-asg-B / my-asg-A",
      "Timestamps": [
        1518868032,
        1518867732,
        1518867432
      ],
      "Values": [
        100,
        100,
        100
      ]
    }
  ]
}
```

### Example


In the following example, two levels of metric math expressions are used, with
 the result of one expression used as an input to the next expression:


#### Sample Request



```
{
  "StartTime": 1518867432,
  "EndTime": 1518868232,
  "MetricDataQueries": [
    {
      "Id": "e1",
      "Expression": "e2 + m3",
      "Label": "my-asg-A * my-asg-B + my-asg-C"
    },
    {
      "Id": "e2",
      "Expression": "m1 * m2",
       "Label": "my-asg-A * my-asg-B"
    },
    {
      "Id": "m1",
      "MetricStat": {
        "Metric": {
          "Namespace": "AWS/EC2",
          "MetricName": "NetworkOut",
          "Dimensions": [
            {
              "Name": "AutoScalingGroupName",
              "Value": "my-asg-A"
            }
          ]
        },
        "Period": 300,
        "Stat": "SampleCount",
        "Unit": "Bytes"
      },
      "ReturnData": false
    },
    {
      "Id": "m2",
      "MetricStat": {
        "Metric": {
          "Namespace": "AWS/EC2",
          "MetricName": "NetworkOut",
          "Dimensions": [
            {
              "Name": "AutoScalingGroupName",
              "Value": "my-asg-B"
            }
          ]
        },
        "Period": 300,
        "Stat": "SampleCount",
        "Unit": "Bytes"
      },
      "ReturnData": false
    },
    {
      "Id": "m3",
      "MetricStat": {
        "Metric": {
          "Namespace": "AWS/EC2",
          "MetricName": "NetworkOut",
          "Dimensions": [
            {
              "Name": "AutoScalingGroupName",
              "Value": "my-asg-C"
            }
          ]
        },
        "Period": 300,
        "Stat": "SampleCount",
        "Unit": "Bytes"
      },
      "ReturnData": false
    }
  ]
}
```

#### Sample Response



```
{
  "MetricDataResults": [
    {
      "Id": "m1",
      "StatusCode": "Complete"
    },
    {
      "Id": "m2",
      "StatusCode": "Complete"
    },
    {
      "Id": "m3",
      "StatusCode": "Complete"
    },
    {
      "Id": "e1",
      "StatusCode": "Complete",
      "Label": "my-asg-A * my-asg-B + my-asg-C",
      "Timestamps": [
        1518868032,
        1518867732,
        1518867432
      ],
      "Values": [
        200,
        200,
        200
      ]
    },
    {
      "Id": "e2",
      "StatusCode": "Complete",
      "Label": "my-asg-A * my-asg-B",
      "Timestamps": [
        1518868032,
        1518867732,
        1518867432
      ],
      "Values": [
        100,
        100,
        100
      ]
    }
  ]
}
```

### Example


In the following example, custom metrics are searched and assigned IDs that
 contain either "error" or "request", even if the original metric names did not
 contain those words. Then an error rate is calculated using the
 `METRICS("string")` function on the assigned IDs.


#### Sample Request



```
{
  "StartTime": 1518867432,
  "EndTime": 1518868432,
  "MetricDataQueries": [
    {
      "Id": "errorRate",
      "Label": "Error Rate",
      "Expression": "errors/requests"
    },
    {
      "Id": "errorRatePercent",
      "Label": "% Error Rate",
      "Expression": "errorRate*100"
    },
    {
      "Id": "requests",
      "Expression": "SUM(METRICS('request'))",
      "ReturnData": false
    },
    {
      "Id": "errors",
      "Expression": "SUM(METRICS('error'))",
      "ReturnData": false
    },
    {
      "Id": "error1",
      "MetricStat": {
        "Metric": {
          "Namespace": "MyService",
          "MetricName": "BadRequests",
          "Dimensions": [
            {
              "Name": "Component",
              "Value": "component-1"
            }
          ]
        },
        "Period": 60,
        "Stat": "Sum"
      },
      "ReturnData": false
    },
    {
      "Id": "error2",
      "MetricStat": {
        "Metric": {
          "Namespace": "MyService",
          "MetricName": "ConnectionErrors",
          "Dimensions": [
            {
              "Name": "Component",
              "Value": "component-1"
            }
          ]
        },
        "Period": 60,
        "Stat": "Sum"
      },
      "ReturnData": false
    },
    {
      "Id": "request1",
      "MetricStat": {
        "Metric": {
          "Namespace": "MyService",
          "MetricName": "InternalRequests",
          "Dimensions": [
            {
              "Name": "Component",
              "Value": "component-1"
            }
          ]
        },
        "Period": 60,
        "Stat": "Sum"
      },
      "ReturnData": false
    },
    {
      "Id": "request2",
      "MetricStat": {
        "Metric": {
          "Namespace": "MyService",
          "MetricName": "ExternalRequests",
          "Dimensions": [
            {
              "Name": "Component",
              "Value": "component-1"
            }
          ]
        },
        "Period": 60,
        "Stat": "Sum"
      },
      "ReturnData": false
    }
  ]
}
```

#### Sample Response



```
{
  "MetricDataResults": [
    {
      "Id": "errorRate",
      "Label": "Error Rate",
      "StatusCode": "Complete",
      "Timestamps": [
        1518868032,
        1518867732,
        1518867432
      ],
      "Values": [
        0.1,
        0.5,
        0.3
      ]
    },
    {
      "Id": "errorRatePercent",
      "Label": "% Error Rate",
      "StatusCode": "Complete",
      "Timestamps": [
        1518868032,
        1518867732,
        1518867432
      ],
      "Values": [
        10,
        50,
        30
      ]
    }
  ]
}
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/GetMetricData "https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/GetMetricData")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/monitoring-2010-08-01/GetMetricData "https://docs.aws.amazon.com/goto/DotNetSDKV3/monitoring-2010-08-01/GetMetricData")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/GetMetricData "https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/GetMetricData")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/GetMetricData "https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/GetMetricData")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/GetMetricData "https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/GetMetricData")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/GetMetricData "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/GetMetricData")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/GetMetricData "https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/GetMetricData")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/GetMetricData "https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/GetMetricData")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/GetMetricData "https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/GetMetricData")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/GetMetricData "https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/GetMetricData")
