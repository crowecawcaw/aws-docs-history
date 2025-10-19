# UpdateChannel

Updates a channel specified by a required channel ARN or UUID.


## Request Syntax



```
{
   "Channel": "`string`",
   "Destinations": [ 
      { 
         "Location": "`string`",
         "Type": "`string`"
      }
   ],
   "Name": "`string`"
}
```

## Request Parameters


For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").


The request accepts the following data in JSON format.





**[Channel](#API_UpdateChannel_RequestSyntax "#API_UpdateChannel_RequestSyntax")**


The ARN or ID (the ARN suffix) of the channel that you want to update.


Type: String


Length Constraints: Minimum length of 3. Maximum length of 256.


Pattern: `^[a-zA-Z0-9._/\-:]+$`



Required: Yes




**[Destinations](#API_UpdateChannel_RequestSyntax "#API_UpdateChannel_RequestSyntax")**


The ARNs of event data stores that you want to log events arriving through the channel.


Type: Array of [Destination](API_Destination.md "API_Destination.md") objects


Array Members: Minimum number of 1 item. Maximum number of 200 items.


Required: No




**[Name](#API_UpdateChannel_RequestSyntax "#API_UpdateChannel_RequestSyntax")**



 Changes the name of the channel.
 


Type: String


Length Constraints: Minimum length of 3. Maximum length of 128.


Pattern: `^[a-zA-Z0-9._\-]+$`



Required: No




## Response Syntax



```
{
   "ChannelArn": "***string***",
   "Destinations": [ 
      { 
         "Location": "***string***",
         "Type": "***string***"
      }
   ],
   "Name": "***string***",
   "Source": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[ChannelArn](#API_UpdateChannel_ResponseSyntax "#API_UpdateChannel_ResponseSyntax")**


The ARN of the channel that was updated.


Type: String


Length Constraints: Minimum length of 3. Maximum length of 256.


Pattern: `^[a-zA-Z0-9._/\-:]+$`





**[Destinations](#API_UpdateChannel_ResponseSyntax "#API_UpdateChannel_ResponseSyntax")**


The event data stores that log events arriving through the channel.


Type: Array of [Destination](API_Destination.md "API_Destination.md") objects


Array Members: Minimum number of 1 item. Maximum number of 200 items.




**[Name](#API_UpdateChannel_ResponseSyntax "#API_UpdateChannel_ResponseSyntax")**


The name of the channel that was updated.


Type: String


Length Constraints: Minimum length of 3. Maximum length of 128.


Pattern: `^[a-zA-Z0-9._\-]+$`





**[Source](#API_UpdateChannel_ResponseSyntax "#API_UpdateChannel_ResponseSyntax")**


The event source of the channel that was updated.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 256.


Pattern: `.*`





## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**ChannelAlreadyExistsException** 



 This exception is thrown when the provided channel already exists.
 


HTTP Status Code: 400




**ChannelARNInvalidException** 


This exception is thrown when the specified value of `ChannelARN` is not
 valid.


HTTP Status Code: 400




**ChannelNotFoundException** 


This exception is thrown when CloudTrail cannot find the specified channel.


HTTP Status Code: 400




**EventDataStoreARNInvalidException** 


The specified event data store ARN is not valid or does not map to an event data store
 in your account.


HTTP Status Code: 400




**EventDataStoreNotFoundException** 


The specified event data store was not found.


HTTP Status Code: 400




**InactiveEventDataStoreException** 


The event data store is inactive.


HTTP Status Code: 400




**InvalidEventDataStoreCategoryException** 


This exception is thrown when event categories of specified event data stores are not
 valid.


HTTP Status Code: 400




**InvalidParameterException** 


The request includes a parameter that is not valid.


HTTP Status Code: 400




**OperationNotPermittedException** 


This exception is thrown when the requested operation is not permitted.


HTTP Status Code: 400




**UnsupportedOperationException** 


This exception is thrown when the requested operation is not supported.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/UpdateChannel "https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/UpdateChannel")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudtrail-2013-11-01/UpdateChannel "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudtrail-2013-11-01/UpdateChannel")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/UpdateChannel "https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/UpdateChannel")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/UpdateChannel "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/UpdateChannel")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/UpdateChannel "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/UpdateChannel")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/UpdateChannel "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/UpdateChannel")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/UpdateChannel "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/UpdateChannel")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/UpdateChannel "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/UpdateChannel")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/UpdateChannel "https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/UpdateChannel")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/UpdateChannel "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/UpdateChannel")
