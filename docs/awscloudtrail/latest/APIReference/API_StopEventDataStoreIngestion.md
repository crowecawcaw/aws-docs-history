# StopEventDataStoreIngestion

Stops the ingestion of live events on an event data store specified as either an ARN or the ID portion of the ARN. To stop ingestion, the event data store `Status` must be `ENABLED` 
 and the `eventCategory` must be `Management`, `Data`, `NetworkActivity`, or `ConfigurationItem`.


## Request Syntax



```
{
   "EventDataStore": "`string`"
}
```

## Request Parameters


For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").


The request accepts the following data in JSON format.





**[EventDataStore](#API_StopEventDataStoreIngestion_RequestSyntax "#API_StopEventDataStoreIngestion_RequestSyntax")**


The ARN (or ID suffix of the ARN) of the event data store for which you want to stop ingestion.


Type: String


Length Constraints: Minimum length of 3. Maximum length of 256.


Pattern: `^[a-zA-Z0-9._/\-:]+$`



Required: Yes




## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**ConflictException** 


This exception is thrown when the specified resource is not ready for an operation. This
 can occur when you try to run an operation on a resource before CloudTrail has time
 to fully load the resource, or because another operation is modifying the resource. If this exception occurs, wait a few minutes, and then try the
 operation again.


HTTP Status Code: 400




**EventDataStoreARNInvalidException** 


The specified event data store ARN is not valid or does not map to an event data store
 in your account.


HTTP Status Code: 400




**EventDataStoreNotFoundException** 


The specified event data store was not found.


HTTP Status Code: 400




**InsufficientDependencyServiceAccessPermissionException** 


This exception is thrown when the IAM identity that is used to create
 the organization resource lacks one or more required permissions for creating an
 organization resource in a required service.


HTTP Status Code: 400




**InvalidEventDataStoreCategoryException** 


This exception is thrown when event categories of specified event data stores are not
 valid.


HTTP Status Code: 400




**InvalidEventDataStoreStatusException** 


The event data store is not in a status that supports the operation.


HTTP Status Code: 400




**InvalidParameterException** 


The request includes a parameter that is not valid.


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




**UnsupportedOperationException** 


This exception is thrown when the requested operation is not supported.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/StopEventDataStoreIngestion "https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/StopEventDataStoreIngestion")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudtrail-2013-11-01/StopEventDataStoreIngestion "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudtrail-2013-11-01/StopEventDataStoreIngestion")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/StopEventDataStoreIngestion "https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/StopEventDataStoreIngestion")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/StopEventDataStoreIngestion "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/StopEventDataStoreIngestion")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/StopEventDataStoreIngestion "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/StopEventDataStoreIngestion")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/StopEventDataStoreIngestion "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/StopEventDataStoreIngestion")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/StopEventDataStoreIngestion "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/StopEventDataStoreIngestion")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/StopEventDataStoreIngestion "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/StopEventDataStoreIngestion")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/StopEventDataStoreIngestion "https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/StopEventDataStoreIngestion")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/StopEventDataStoreIngestion "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/StopEventDataStoreIngestion")
