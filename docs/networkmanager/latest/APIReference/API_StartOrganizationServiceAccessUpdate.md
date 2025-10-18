# StartOrganizationServiceAccessUpdate

Enables the Network Manager service for an Amazon Web Services Organization. This can only be called by a management account within the organization. 


## Request Syntax



```
POST /organizations/service-access HTTP/1.1
Content-type: application/json

{
   "Action": "`string`"
}
```

## URI Request Parameters


The request does not use any URI parameters.


## Request Body


The request accepts the following data in JSON format.





**[Action](#API_StartOrganizationServiceAccessUpdate_RequestSyntax "#API_StartOrganizationServiceAccessUpdate_RequestSyntax")**


The action to take for the update request. This can be either `ENABLE` or `DISABLE`.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 50.


Required: Yes




## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "OrganizationStatus": { 
      "AccountStatusList": [ 
         { 
            "AccountId": "***string***",
            "SLRDeploymentStatus": "***string***"
         }
      ],
      "OrganizationAwsServiceAccessStatus": "***string***",
      "OrganizationId": "***string***",
      "SLRDeploymentStatus": "***string***"
   }
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[OrganizationStatus](#API_StartOrganizationServiceAccessUpdate_ResponseSyntax "#API_StartOrganizationServiceAccessUpdate_ResponseSyntax")**


The status of the service access update request for an Amazon Web Services Organization.


Type: [OrganizationStatus](API_OrganizationStatus.md "API_OrganizationStatus.md") object




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDeniedException** 


You do not have sufficient access to perform this action.


HTTP Status Code: 403




**ConflictException** 


There was a conflict processing the request. Updating or deleting the resource can
 cause an inconsistent state.





**ResourceId** 


The ID of the resource.




**ResourceType** 


The resource type.




HTTP Status Code: 409




**InternalServerException** 


The request has failed due to an internal error.





**RetryAfterSeconds** 


Indicates when to retry the request.




HTTP Status Code: 500




**ServiceQuotaExceededException** 


A service limit was exceeded.





**LimitCode** 


The limit code.




**Message** 


The error message.




**ResourceId** 


The ID of the resource.




**ResourceType** 


The resource type.




**ServiceCode** 


The service code.




HTTP Status Code: 402




**ThrottlingException** 


The request was denied due to request throttling.





**RetryAfterSeconds** 


Indicates when to retry the request.




HTTP Status Code: 429




**ValidationException** 


The input fails to satisfy the constraints.





**Fields** 


The fields that caused the error, if applicable.




**Reason** 


The reason for the error.




HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/StartOrganizationServiceAccessUpdate "https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/StartOrganizationServiceAccessUpdate")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/networkmanager-2019-07-05/StartOrganizationServiceAccessUpdate "https://docs.aws.amazon.com/goto/DotNetSDKV3/networkmanager-2019-07-05/StartOrganizationServiceAccessUpdate")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/StartOrganizationServiceAccessUpdate "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/StartOrganizationServiceAccessUpdate")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/StartOrganizationServiceAccessUpdate "https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/StartOrganizationServiceAccessUpdate")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/StartOrganizationServiceAccessUpdate "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/StartOrganizationServiceAccessUpdate")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/StartOrganizationServiceAccessUpdate "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/StartOrganizationServiceAccessUpdate")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/StartOrganizationServiceAccessUpdate "https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/StartOrganizationServiceAccessUpdate")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/StartOrganizationServiceAccessUpdate "https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/StartOrganizationServiceAccessUpdate")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/StartOrganizationServiceAccessUpdate "https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/StartOrganizationServiceAccessUpdate")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/StartOrganizationServiceAccessUpdate "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/StartOrganizationServiceAccessUpdate")
