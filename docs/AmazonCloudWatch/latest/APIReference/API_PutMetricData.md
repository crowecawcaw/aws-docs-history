# PutMetricData

Publishes metric data to Amazon CloudWatch. CloudWatch associates the data with the
 specified metric. If the specified metric does not exist, CloudWatch creates the metric.
 When CloudWatch creates a metric, it can take up to fifteen minutes for the metric to
 appear in calls to [ListMetrics](API_ListMetrics.md "API_ListMetrics.md").

You can publish metrics with associated entity data (so that related telemetry can be
 found and viewed together), or publish metric data by itself. To send entity data with
 your metrics, use the `EntityMetricData` parameter. To send metrics without
 entity data, use the `MetricData` parameter. The
 `EntityMetricData` structure includes `MetricData` structures
 for the metric data.

You can publish either individual values in the `Value` field, or arrays of
 values and the number of times each value occurred during the period by using the
 `Values` and `Counts` fields in the `MetricData`
 structure. Using the `Values` and `Counts` method enables you to
 publish up to 150 values per metric with one `PutMetricData` request, and
 supports retrieving percentile statistics on this data.

Each `PutMetricData` request is limited to 1 MB in size for HTTP POST
 requests. You can send a payload compressed by gzip. Each request is also limited to no
 more than 1000 different metrics (across both the `MetricData` and 
 `EntityMetricData` properties).

Although the `Value` parameter accepts numbers of type `Double`,
 CloudWatch rejects values that are either too small or too large. Values must be in the
 range of -2^360 to 2^360. In addition, special values (for example, NaN, +Infinity,
 -Infinity) are not supported.

You can use up to 30 dimensions per metric to further clarify what data the metric
 collects. Each dimension consists of a Name and Value pair. For more information about
 specifying dimensions, see [Publishing
 Metrics](../monitoring/publishingMetrics.md "../monitoring/publishingMetrics.md") in the *Amazon CloudWatch User Guide*.

You specify the time stamp to be associated with each data point. You can specify time
 stamps that are as much as two weeks before the current date, and as much as 2 hours
 after the current day and time.

Data points with time stamps from 24 hours ago or longer can take at least 48 hours to
 become available for [GetMetricData](API_GetMetricData.md "API_GetMetricData.md") or [GetMetricStatistics](API_GetMetricStatistics.md "API_GetMetricStatistics.md") from the time they are submitted. Data points with time
 stamps between 3 and 24 hours ago can take as much as 2 hours to become available for
 [GetMetricData](API_GetMetricData.md "API_GetMetricData.md") or [GetMetricStatistics](API_GetMetricStatistics.md "API_GetMetricStatistics.md").

CloudWatch needs raw data points to calculate percentile statistics. If you publish
 data using a statistic set instead, you can only retrieve percentile statistics for this
 data if one of the following conditions is true:


* The `SampleCount` value of the statistic set is 1 and
 `Min`, `Max`, and `Sum` are all
 equal.
* The `Min` and `Max` are equal, and `Sum`
 is equal to `Min` multiplied by `SampleCount`.

## Request Parameters





**EntityMetricData** 


Data for metrics that contain associated entity information. You can include up to 
 two `EntityMetricData` objects, each of which can contain a single 
 `Entity` and associated metrics.


The limit of metrics allowed, 1000, is the sum of both `EntityMetricData` 
 and `MetricData` metrics.


Type: Array of [EntityMetricData](API_EntityMetricData.md "API_EntityMetricData.md") objects


Required: No




**MetricData** 


The data for the metrics. Use this parameter if your metrics do not contain
 associated entities. The array can include no more than 1000 metrics per call.


The limit of metrics allowed, 1000, is the sum of both `EntityMetricData` 
 and `MetricData` metrics.


Type: Array of [MetricDatum](API_MetricDatum.md "API_MetricDatum.md") objects


Required: No




**Namespace** 


The namespace for the metric data. You can use ASCII characters for the namespace,
 except for control characters which are not supported.


To avoid conflicts with AWS service namespaces, you should not
 specify a namespace that begins with `AWS/`



Type: String


Length Constraints: Minimum length of 1. Maximum length of 255.


Pattern: `[^:].*`



Required: Yes




**StrictEntityValidation** 


Whether to accept valid metric data when an invalid entity is sent.



* When set to `true`: Any validation error (for entity or metric 
 data) will fail the entire request, and no data will be ingested. The failed 
 operation will return a 400 result with the error.
* When set to `false`: Validation errors in the entity will not 
 associate the metric with the entity, but the metric data will still be 
 accepted and ingested. Validation errors in the metric data will fail the 
 entire request, and no data will be ingested.


In the case of an invalid entity, the operation will return a 
 `200` status, but an additional response header will contain 
 information about the validation errors. The new header, 
 `X-Amzn-Failure-Message` is an enumeration of the following 
 values:




	+ `InvalidEntity` - The provided entity is invalid.
	+ `InvalidKeyAttributes` - The provided
	 `KeyAttributes` of an entity is invalid.
	+ `InvalidAttributes` - The provided `Attributes`
	 of an entity is invalid.
	+ `InvalidTypeValue` - The provided `Type` in the
	 `KeyAttributes` of an entity is invalid.
	+ `EntitySizeTooLarge` - The number of 
	 `EntityMetricData` objects allowed is 2.
	+ `MissingRequiredFields` - There are missing required 
	 fields in the `KeyAttributes` for the provided
	 `Type`.
For details of the requirements for specifying an entity, see 
 [How 
 to add related information to telemetry](../monitoring/adding-your-own-related-telemetry.md "../monitoring/adding-your-own-related-telemetry.md") in the 
 *CloudWatch User Guide*.

This parameter is *required* when `EntityMetricData` is
 included.


Type: Boolean


Required: No




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**InternalServiceError** 


Request processing has failed due to some unknown error, exception, or
 failure.





**Message** 





HTTP Status Code: 500




**InvalidParameterCombination** 


Parameters were used together that cannot be used together.





**message** 





HTTP Status Code: 400




**InvalidParameterValue** 


The value of an input parameter is bad or out-of-range.





**message** 





HTTP Status Code: 400




**MissingParameter** 


An input parameter that is required is missing.





**message** 





HTTP Status Code: 400




## Examples


### Example


The following example puts data for a single metric containing one
 dimension:


#### Sample Request



```
https://monitoring.us-west-1.amazonaws.com
?Action=PutMetricData
&Version=2010-08-01
&Namespace=TestNamespace
&MetricData.member.1.MetricName=buffers
&MetricData.member.1.Unit=Bytes
&MetricData.member.1.Value=231434333
&MetricData.member.1.Dimensions.member.1.Name=InstanceType
&MetricData.member.1.Dimensions.member.1.Value=m1.small
&AUTHPARAMS
```

### Example


The following example puts data for a single metric containing two
 dimensions:


#### Sample Request



```
https://monitoring.us-west-1.amazonaws.com
?Action=PutMetricData
&Version=2010-08-01
&Namespace=TestNamespace
&MetricData.member.1.MetricName=buffers
&MetricData.member.1.Unit=Bytes
&MetricData.member.1.Value=231434333
&MetricData.member.1.Dimensions.member.1.Name=InstanceID
&MetricData.member.1.Dimensions.member.1.Value=i-aaba32d4
&MetricData.member.1.Dimensions.member.2.Name=InstanceType
&MetricData.member.1.Dimensions.member.2.Value=m1.small
&AUTHPARAMS
```

### Example


The following example puts data for two metrics, each with two
 dimensions:


#### Sample Request



```
https://monitoring.us-west-1.amazonaws.com
?Action=PutMetricData
&Version=2010-08-01
&Namespace=TestNamespace
&MetricData.member.1.MetricName=buffers
&MetricData.member.1.Unit=Bytes
&MetricData.member.1.Value=231434333
&MetricData.member.1.Dimensions.member.1.Name=InstanceID
&MetricData.member.1.Dimensions.member.1.Value=i-aaba32d4
&MetricData.member.1.Dimensions.member.2.Name=InstanceType
&MetricData.member.1.Dimensions.member.2.Value=m1.small
&MetricData.member.2.MetricName=latency
&MetricData.member.2.Unit=Milliseconds
&MetricData.member.2.Value=23
&MetricData.member.2.Dimensions.member.1.Name=InstanceID
&MetricData.member.2.Dimensions.member.1.Value=i-aaba32d4
&MetricData.member.2.Dimensions.member.2.Name=InstanceType
&MetricData.member.2.Dimensions.member.2.Value=m1.small
&AUTHPARAMS
```

### Example


The following example puts data for a high-resolution metric:


#### Sample Request



```
https://monitoring.us-west-1.amazonaws.com
?Action=PutMetricData
&Version=2010-08-01
&Namespace=HighResolutionMetric
&MetricData.member.1.MetricName=HighResdata
&MetricData.member.1.Unit=Bytes
&MetricData.member.1.Value=542868
&MetricData.member.1.StorageResolution=1
&AUTHPARAMS
```

### Example


The following example puts multiple values for each of two metrics, using
 `Values` and `Counts` arrays:


#### Sample Request



```
https://monitoring.us-west-1.amazonaws.com
?Action=PutMetricData
&Version=2010-08-01
&Namespace=TestNamespace
&MetricData.member.1.MetricName=Reads
&MetricData.member.1.Unit=Count
&MetricData.member.1.Values.member.1=5
&MetricData.member.1.Values.member.2=8
&MetricData.member.1.Values.member.3=10
&MetricData.member.1.Values.member.4=9
&MetricData.member.1.Counts.member.1=1
&MetricData.member.1.Counts.member.2=5
&MetricData.member.1.Counts.member.3=6
&MetricData.member.1.Counts.member.4=5
&MetricData.member.1.Dimensions.member.1.Name=InstanceID
&MetricData.member.1.Dimensions.member.1.Value=i-aaba32d4
&MetricData.member.2.MetricName=Writes
&MetricData.member.2.Unit=Count
&MetricData.member.2.Values.member.1=2
&MetricData.member.2.Values.member.2=3
&MetricData.member.2.Values.member.3=0
&MetricData.member.2.Counts.member.1=2
&MetricData.member.2.Counts.member.2=2
&MetricData.member.2.Counts.member.3=1
&MetricData.member.2.Dimensions.member.1.Name=InstanceID
&MetricData.member.2.Dimensions.member.1.Value=i-aaba32d4
&AUTHPARAMS
```

### Example


The following example uses `EntityMetricData` to put a metric
 with entity data for a service running in Amazon EC2:


#### Sample Request



```
https://monitoring.us-west-1.amazonaws.com
?Action=PutMetricData
&Version=2010-08-01
&StrictEntityValidation=true
&Namespace=TestNamespace
&EntityMetricData.member.1.Entity.KeyAttributes.entry.1.key=Type
&EntityMetricData.member.1.Entity.KeyAttributes.entry.1.value=Service
&EntityMetricData.member.1.Entity.KeyAttributes.entry.2.key=Name
&EntityMetricData.member.1.Entity.KeyAttributes.entry.2.value=MyTestService
&EntityMetricData.member.1.Entity.KeyAttributes.entry.3.key=Environment
&EntityMetricData.member.1.Entity.KeyAttributes.entry.3.value=MyTestEnvironment
&EntityMetricData.member.1.Entity.Attributes.entry.1.key=PlatformType
&EntityMetricData.member.1.Entity.Attributes.entry.1.value=AWS::EC2
&EntityMetricData.member.1.Entity.Attributes.entry.2.key=EC2.InstanceId
&EntityMetricData.member.1.Entity.Attributes.entry.2.value=i-1234567890abcdef0
&EntityMetricData.member.1.MetricData.member.1.MetricName=buffers
&EntityMetricData.member.1.MetricData.member.1.Timestamp=2024-11-06T02:16:28Z
&EntityMetricData.member.1.MetricData.member.1.Unit=Count
&EntityMetricData.member.1.MetricData.member.1.Values.member.1=2
&EntityMetricData.member.1.MetricData.member.1.Values.member.2=3
&EntityMetricData.member.1.MetricData.member.1.Values.member.3=0
&EntityMetricData.member.1.MetricData.member.1.Counts.member.1=2
&EntityMetricData.member.1.MetricData.member.1.Counts.member.2=2
&EntityMetricData.member.1.MetricData.member.1.Counts.member.3=1
&EntityMetricData.member.1.MetricData.member.1.Dimensions.member.1.Name=InstanceID
&EntityMetricData.member.1.MetricData.member.1.Dimensions.member.1.Value=i-aaba32d4
&EntityMetricData.member.1.MetricData.member.1.Dimensions.member.2.Name=InstanceType
&EntityMetricData.member.1.MetricData.member.1.Dimensions.member.2.Value=m1.small
&AUTHPARAMS
```

### Example


The following example uses `EntityMetricData` to put a metric
 with entity data for a service running in Lambda:


#### Sample Request



```
https://monitoring.us-west-1.amazonaws.com
?Action=PutMetricData
&Version=2010-08-01
&StrictEntityValidation=true
&Namespace=TestNamespace
&EntityMetricData.member.1.Entity.KeyAttributes.entry.1.key=Type
&EntityMetricData.member.1.Entity.KeyAttributes.entry.1.value=Service
&EntityMetricData.member.1.Entity.KeyAttributes.entry.2.key=Name
&EntityMetricData.member.1.Entity.KeyAttributes.entry.2.value=MyTestService
&EntityMetricData.member.1.Entity.KeyAttributes.entry.3.key=Environment
&EntityMetricData.member.1.Entity.KeyAttributes.entry.3.value=MyTestEnvironment
&EntityMetricData.member.1.Entity.Attributes.entry.1.key=PlatformType
&EntityMetricData.member.1.Entity.Attributes.entry.1.value=AWS::Lambda
&EntityMetricData.member.1.Entity.Attributes.entry.2.key=Lambda.Function
&EntityMetricData.member.1.Entity.Attributes.entry.2.value=MyTestFunction
&EntityMetricData.member.1.MetricData.member.1.MetricName=faults
&EntityMetricData.member.1.MetricData.member.1.Timestamp=2024-11-06T02:16:28Z
&EntityMetricData.member.1.MetricData.member.1.Unit=Count
&EntityMetricData.member.1.MetricData.member.1.Values.member.1=2
&EntityMetricData.member.1.MetricData.member.1.Values.member.2=3
&EntityMetricData.member.1.MetricData.member.1.Values.member.3=0
&EntityMetricData.member.1.MetricData.member.1.Counts.member.1=2
&EntityMetricData.member.1.MetricData.member.1.Counts.member.2=2
&EntityMetricData.member.1.MetricData.member.1.Counts.member.3=1
&EntityMetricData.member.1.MetricData.member.1.Dimensions.member.1.Name=InstanceID
&EntityMetricData.member.1.MetricData.member.1.Dimensions.member.1.Value=i-aaba32d4
&EntityMetricData.member.1.MetricData.member.1.Dimensions.member.2.Name=InstanceType
&EntityMetricData.member.1.MetricData.member.1.Dimensions.member.2.Value=m1.small
&AUTHPARAMS
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/PutMetricData "https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/PutMetricData")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/monitoring-2010-08-01/PutMetricData "https://docs.aws.amazon.com/goto/DotNetSDKV3/monitoring-2010-08-01/PutMetricData")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/PutMetricData "https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/PutMetricData")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/PutMetricData "https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/PutMetricData")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/PutMetricData "https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/PutMetricData")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/PutMetricData "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/PutMetricData")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/PutMetricData "https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/PutMetricData")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/PutMetricData "https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/PutMetricData")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/PutMetricData "https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/PutMetricData")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/PutMetricData "https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/PutMetricData")
