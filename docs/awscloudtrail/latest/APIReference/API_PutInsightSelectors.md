# PutInsightSelectors

Lets you enable Insights event logging by specifying the Insights selectors that you
 want to enable on an existing trail or event data store. You also use `PutInsightSelectors` to turn
 off Insights event logging, by passing an empty list of Insights types. The valid Insights
 event types are `ApiErrorRateInsight` and
 `ApiCallRateInsight`.

To enable Insights on an event data store, you must specify the ARNs (or ID suffix of the ARNs) for the source event data store (`EventDataStore`) and the destination event data store (`InsightsDestination`). The source event data store logs management events and enables Insights. 
 The destination event data store logs Insights events based upon the management event activity of the source event data store. The source and destination event data stores must belong to the same AWS account.

To log Insights events for a trail, you must specify the name (`TrailName`) of the CloudTrail trail for which you want to change or add Insights
 selectors.

To log CloudTrail Insights events on API call volume, the trail or event data store
 must log `write` management events. To log CloudTrail
 Insights events on API error rate, the trail or event data store must log `read` or
 `write` management events. You can call `GetEventSelectors` on a trail 
 to check whether the trail logs management events. You can call `GetEventDataStore` on an 
 event data store to check whether the event data store logs management events.

For more information, see [Working with CloudTrail Insights](../userguide/logging-insights-events-with-cloudtrail.md "../userguide/logging-insights-events-with-cloudtrail.md") in the *AWS CloudTrail User Guide*.


## Request Syntax



```
{
   "EventDataStore": "`string`",
   "InsightsDestination": "`string`",
   "InsightSelectors": [ 
      { 
         "InsightType": "`string`"
      }
   ],
   "TrailName": "`string`"
}
```

## Request Parameters


For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").


The request accepts the following data in JSON format.





**[EventDataStore](#API_PutInsightSelectors_RequestSyntax "#API_PutInsightSelectors_RequestSyntax")**


The ARN (or ID suffix of the ARN) of the source event data store for which you want to change or add Insights
 selectors. To enable Insights on an event data store, you must provide both the 
 `EventDataStore` and `InsightsDestination` parameters.


You cannot use this parameter with the `TrailName` parameter.


Type: String


Length Constraints: Minimum length of 3. Maximum length of 256.


Pattern: `^[a-zA-Z0-9._/\-:]+$`



Required: No




**[InsightsDestination](#API_PutInsightSelectors_RequestSyntax "#API_PutInsightSelectors_RequestSyntax")**



 The ARN (or ID suffix of the ARN) of the destination event data store that logs Insights events. To enable Insights on an event data store, you must provide both the 
 `EventDataStore` and `InsightsDestination` parameters.
 


You cannot use this parameter with the `TrailName` parameter.


Type: String


Length Constraints: Minimum length of 3. Maximum length of 256.


Pattern: `^[a-zA-Z0-9._/\-:]+$`



Required: No




**[InsightSelectors](#API_PutInsightSelectors_RequestSyntax "#API_PutInsightSelectors_RequestSyntax")**


A JSON string that contains the Insights types you want to log on a trail or event data store.
 `ApiCallRateInsight` and `ApiErrorRateInsight` are valid Insight
 types.


The `ApiCallRateInsight` Insights type analyzes write-only
 management API calls that are aggregated per minute against a baseline API call volume.


The `ApiErrorRateInsight` Insights type analyzes management
 API calls that result in error codes. The error is shown if the API call is
 unsuccessful.


Type: Array of [InsightSelector](API_InsightSelector.md "API_InsightSelector.md") objects


Required: Yes




**[TrailName](#API_PutInsightSelectors_RequestSyntax "#API_PutInsightSelectors_RequestSyntax")**


The name of the CloudTrail trail for which you want to change or add Insights
 selectors.


You cannot use this parameter with the `EventDataStore` and `InsightsDestination` parameters.


Type: String


Required: No




## Response Syntax



```
{
   "EventDataStoreArn": "***string***",
   "InsightsDestination": "***string***",
   "InsightSelectors": [ 
      { 
         "InsightType": "***string***"
      }
   ],
   "TrailARN": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[EventDataStoreArn](#API_PutInsightSelectors_ResponseSyntax "#API_PutInsightSelectors_ResponseSyntax")**


The Amazon Resource Name (ARN) of the source event data store for which you want to change or add Insights
 selectors.


Type: String


Length Constraints: Minimum length of 3. Maximum length of 256.


Pattern: `^[a-zA-Z0-9._/\-:]+$`





**[InsightsDestination](#API_PutInsightSelectors_ResponseSyntax "#API_PutInsightSelectors_ResponseSyntax")**



 The ARN of the destination event data store that logs Insights events.
 


Type: String


Length Constraints: Minimum length of 3. Maximum length of 256.


Pattern: `^[a-zA-Z0-9._/\-:]+$`





**[InsightSelectors](#API_PutInsightSelectors_ResponseSyntax "#API_PutInsightSelectors_ResponseSyntax")**


A JSON string that contains the Insights event types that you want to log on a trail or event data store.
 The valid Insights types are `ApiErrorRateInsight` and
 `ApiCallRateInsight`.


Type: Array of [InsightSelector](API_InsightSelector.md "API_InsightSelector.md") objects




**[TrailARN](#API_PutInsightSelectors_ResponseSyntax "#API_PutInsightSelectors_ResponseSyntax")**


The Amazon Resource Name (ARN) of a trail for which you want to change or add Insights
 selectors.


Type: String




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**CloudTrailARNInvalidException** 


This exception is thrown when an operation is called with an ARN that is not valid.


The following is the format of a trail ARN: `arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail`



The following is the format of an event data store ARN:
 `arn:aws:cloudtrail:us-east-2:123456789012:eventdatastore/EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE`



The following is the format of a dashboard ARN: `arn:aws:cloudtrail:us-east-1:123456789012:dashboard/exampleDash`



The following is the format of a channel ARN:
 `arn:aws:cloudtrail:us-east-2:123456789012:channel/01234567890`



HTTP Status Code: 400




**InsufficientEncryptionPolicyException** 


For the `CreateTrail`
`PutInsightSelectors`, `UpdateTrail`, `StartQuery`, and `StartImport` operations, this exception is thrown 
 when the policy on the S3 bucket or AWS KMS key does
 not have sufficient permissions for the operation.


For all other operations, this exception is thrown when the policy for the AWS KMS key does
 not have sufficient permissions for the operation.


HTTP Status Code: 400




**InsufficientS3BucketPolicyException** 


This exception is thrown when the policy on the S3 bucket is not sufficient.


HTTP Status Code: 400




**InvalidHomeRegionException** 


This exception is thrown when an operation is called on a trail from a Region other than
 the Region in which the trail was created.


HTTP Status Code: 400




**InvalidInsightSelectorsException** 


For `PutInsightSelectors`, this exception is thrown when the formatting or syntax of the `InsightSelectors` JSON statement is not
 valid, or the specified `InsightType` in the `InsightSelectors` statement is not
 valid. Valid values for `InsightType` are `ApiCallRateInsight` and `ApiErrorRateInsight`. To enable Insights on an event data store, the destination event data store specified by the 
 `InsightsDestination` parameter must log Insights events and the source event data 
 store specified by the `EventDataStore` parameter must log management events.


For `UpdateEventDataStore`, this exception is thrown if Insights are enabled on the event data store and the updated 
 advanced event selectors are not compatible with the configured `InsightSelectors`. 
 If the `InsightSelectors` includes an `InsightType` of `ApiCallRateInsight`, the source event data store must log `write` management events. 
 If the `InsightSelectors` includes an `InsightType` of `ApiErrorRateInsight`, the source event data store must log management events.


HTTP Status Code: 400




**InvalidParameterCombinationException** 


This exception is thrown when the combination of parameters provided is not
 valid.


HTTP Status Code: 400




**InvalidParameterException** 


The request includes a parameter that is not valid.


HTTP Status Code: 400




**InvalidTrailNameException** 


This exception is thrown when the provided trail name is not valid. Trail names must
 meet the following requirements:



* Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores
 (\_), or dashes (-)
* Start with a letter or number, and end with a letter or number
* Be between 3 and 128 characters
* Have no adjacent periods, underscores or dashes. Names like
 `my-_namespace` and `my--namespace` are not valid.
* Not be in IP address format (for example, 192.168.5.4)

HTTP Status Code: 400




**KmsException** 


This exception is thrown when there is an issue with the specified AWS KMS
 key and the trail or event data store can't be updated.


HTTP Status Code: 400




**NoManagementAccountSLRExistsException** 


 This exception is thrown when the management account does not have a service-linked
 role. 


HTTP Status Code: 400




**NotOrganizationMasterAccountException** 


This exception is thrown when the AWS account making the request to
 create or update an organization trail or event data store is not the management account
 for an organization in AWS Organizations. For more information, see [Prepare For Creating a Trail For Your Organization](../userguide/creating-an-organizational-trail-prepare.md "../userguide/creating-an-organizational-trail-prepare.md") or [Organization event data stores](../userguide/cloudtrail-lake-organizations.md "../userguide/cloudtrail-lake-organizations.md").


HTTP Status Code: 400




**OperationNotPermittedException** 


This exception is thrown when the requested operation is not permitted.


HTTP Status Code: 400




**S3BucketDoesNotExistException** 


This exception is thrown when the specified S3 bucket does not exist.


HTTP Status Code: 400




**ThrottlingException** 



 This exception is thrown when the request rate exceeds the limit. 
 


HTTP Status Code: 400




**TrailNotFoundException** 


This exception is thrown when the trail with the given name is not found.


HTTP Status Code: 400




**UnsupportedOperationException** 


This exception is thrown when the requested operation is not supported.


HTTP Status Code: 400




## Examples


### Example


The following example shows how to use Insight selectors to enable CloudTrail Insights on a trail named *SampleTrail*.



```
{
   "InsightSelectors": '[{"InsightType": "ApiCallRateInsight"},{"InsightType": "ApiErrorRateInsight"}]',
   "TrailARN": "arn:aws:cloudtrail:us-east-2:123456789012:trail/SampleTrail"
}
```

### Example


The following example shows how to disable CloudTrail Insights on a trail
 named SampleTrail. Disable Insights event collection by passing an empty string of
 insight types (`[ ]`).



```
{
   "InsightSelectors": [ ],
   "TrailARN": "arn:aws:cloudtrail:us-east-2:123456789012:trail/SampleTrail"
}
```

### Example


The following example shows how to use Insight selectors to enable CloudTrail Insights on an event data store.



```
{
   "EventDataStore": "arn:aws:cloudtrail:us-east-1:123456789012:eventdatastore/EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE",
   "InsightsDestination": "arn:aws:cloudtrail:us-east-1:123456789012:eventdatastore/EXAMPLE-d483-5c7d-4ac2-adb5dEXAMPLE",
   "InsightSelectors": [
      {
         "InsightType": "ApiCallRateInsight"
      },
      {
         "InsightType": "ApiErrorRateInsight"
      }
   ]
}
```

### Example


The following example shows how to disable CloudTrail Insights on an event data store.



```
{
   "EventDataStore": "arn:aws:cloudtrail:us-east-1:123456789012:eventdatastore/EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE",
   "InsightSelectors": [ ]
}
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/PutInsightSelectors "https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/PutInsightSelectors")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudtrail-2013-11-01/PutInsightSelectors "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudtrail-2013-11-01/PutInsightSelectors")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/PutInsightSelectors "https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/PutInsightSelectors")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/PutInsightSelectors "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/PutInsightSelectors")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/PutInsightSelectors "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/PutInsightSelectors")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/PutInsightSelectors "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/PutInsightSelectors")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/PutInsightSelectors "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/PutInsightSelectors")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/PutInsightSelectors "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/PutInsightSelectors")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/PutInsightSelectors "https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/PutInsightSelectors")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/PutInsightSelectors "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/PutInsightSelectors")
