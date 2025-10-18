# DescribeAnomalyDetectors

Lists the anomaly detection models that you have created in your account. For single
 metric anomaly detectors, you can list all of the models in your account or filter the
 results to only the models that are related to a certain namespace, metric name, or
 metric dimension. For metric math anomaly detectors, you can list them by adding
 `METRIC_MATH` to the `AnomalyDetectorTypes` array. This will
 return all metric math anomaly detectors in your account.


## Request Parameters





**AnomalyDetectorTypes** 


The anomaly detector types to request when using
 `DescribeAnomalyDetectorsInput`. If empty, defaults to
 `SINGLE_METRIC`.


Type: Array of strings


Array Members: Maximum number of 2 items.


Valid Values: `SINGLE_METRIC | METRIC_MATH`



Required: No




**Dimensions** 


Limits the results to only the anomaly detection models that are associated with the
 specified metric dimensions. If there are multiple metrics that have these dimensions
 and have anomaly detection models associated, they're all returned.


Type: Array of [Dimension](API_Dimension.md "API_Dimension.md") objects


Array Members: Maximum number of 30 items.


Required: No




**MaxResults** 


The maximum number of results to return in one operation. The maximum value that you
 can specify is 100.


To retrieve the remaining results, make another call with the returned
 `NextToken` value. 


Type: Integer


Valid Range: Minimum value of 1.


Required: No




**MetricName** 


Limits the results to only the anomaly detection models that are associated with the
 specified metric name. If there are multiple metrics with this name in different
 namespaces that have anomaly detection models, they're all returned.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 255.


Required: No




**Namespace** 


Limits the results to only the anomaly detection models that are associated with the
 specified namespace.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 255.


Pattern: `[^:].*`



Required: No




**NextToken** 


Use the token returned by the previous operation to request the next page of
 results.


Type: String


Required: No




## Response Elements


The following elements are returned by the service.





**AnomalyDetectors** 


The list of anomaly detection models returned by the operation.


Type: Array of [AnomalyDetector](API_AnomalyDetector.md "API_AnomalyDetector.md") objects




**NextToken** 


A token that you can use in a subsequent operation to retrieve the next set of
 results.


Type: String




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**InternalServiceError** 


Request processing has failed due to some unknown error, exception, or
 failure.





**Message** 





HTTP Status Code: 500




**InvalidNextToken** 


The next token specified is invalid.





**message** 





HTTP Status Code: 400




**InvalidParameterCombination** 


Parameters were used together that cannot be used together.





**message** 





HTTP Status Code: 400




**InvalidParameterValue** 


The value of an input parameter is bad or out-of-range.





**message** 





HTTP Status Code: 400




## Examples


### Example


The following example lists all the anomaly detectors for metrics with the
 name `CPUUtilization`.


#### Sample Request



```
{
    "MetricName:": "CPUUtilization"
}
```

#### Sample Response



```
{
    "AnomalyDetectors": [
        {
            "Namespace": "AWS/EC2",
            "MetricName": "CPUUtilization",
            "Dimensions": [
                {
                    "Name": "dimension1",
                    "Value": "value1"
                },
                {
                    "Name": "dimension2",
                    "Value": "value2"
                }
            ],
            "Stat": "Average",
            "Configuration": {
                "ExcludedTimeRanges": [
                    
                ]
            }
        },
        {
            "Namespace": "AWS/EC2",
            "MetricName": "CPUUtilization",
            "Dimensions": [
                {
                    "Name": "dimension1",
                    "Value": "value1"
                }
            ],
            "Stat": "SampleCount",
            "Configuration": {
                "ExcludedTimeRanges": [
                    
                ]
            }
        },
        {
            "Namespace": "APITest1",
            "MetricName": "Metric1",
            "Dimensions": [
                {
                    "Name": "dimension1",
                    "Value": "value1"
                }
            ],
            "Stat": "SampleCount",
            "Configuration": {
                "ExcludedTimeRanges": [
                    
                ]
            }
        },
        {
            "Namespace": "CustomNamespace",
            "MetricName": "CPUUtilization",
            "Dimensions": [
                {
                    "Name": "dimension1",
                    "Value": "value1"
                },
                {
                    "Name": "dimension2",
                    "Value": "value2"
                }
            ],
            "Stat": "Maximum",
            "Configuration": {
                "ExcludedTimeRanges": [
                    
                ]
            }
        }
    ]
}
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/DescribeAnomalyDetectors "https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/DescribeAnomalyDetectors")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/monitoring-2010-08-01/DescribeAnomalyDetectors "https://docs.aws.amazon.com/goto/DotNetSDKV3/monitoring-2010-08-01/DescribeAnomalyDetectors")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/DescribeAnomalyDetectors "https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/DescribeAnomalyDetectors")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/DescribeAnomalyDetectors "https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/DescribeAnomalyDetectors")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/DescribeAnomalyDetectors "https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/DescribeAnomalyDetectors")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/DescribeAnomalyDetectors "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/DescribeAnomalyDetectors")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/DescribeAnomalyDetectors "https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/DescribeAnomalyDetectors")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/DescribeAnomalyDetectors "https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/DescribeAnomalyDetectors")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/DescribeAnomalyDetectors "https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/DescribeAnomalyDetectors")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/DescribeAnomalyDetectors "https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/DescribeAnomalyDetectors")
