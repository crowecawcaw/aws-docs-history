# ListOrganizationServiceAccessStatus

Gets the status of the Service Linked Role (SLR) deployment for the accounts in a given Amazon Web Services Organization.


## Request Syntax



```
GET /organizations/service-access?maxResults=`MaxResults`&nextToken=`NextToken` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[MaxResults](#API_ListOrganizationServiceAccessStatus_RequestSyntax "#API_ListOrganizationServiceAccessStatus_RequestSyntax")**


The maximum number of results to return.


Valid Range: Minimum value of 1. Maximum value of 500.




**[NextToken](#API_ListOrganizationServiceAccessStatus_RequestSyntax "#API_ListOrganizationServiceAccessStatus_RequestSyntax")**


The token for the next page of results.


Length Constraints: Minimum length of 0. Maximum length of 2048.


Pattern: `[\s\S]*`





## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "***string***",
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





**[NextToken](#API_ListOrganizationServiceAccessStatus_ResponseSyntax "#API_ListOrganizationServiceAccessStatus_ResponseSyntax")**


The token for the next page of results.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 2048.


Pattern: `[\s\S]*`





**[OrganizationStatus](#API_ListOrganizationServiceAccessStatus_ResponseSyntax "#API_ListOrganizationServiceAccessStatus_ResponseSyntax")**


Displays the status of an Amazon Web Services Organization.


Type: [OrganizationStatus](API_OrganizationStatus.md "API_OrganizationStatus.md") object




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").


## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/ListOrganizationServiceAccessStatus "https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/ListOrganizationServiceAccessStatus")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/networkmanager-2019-07-05/ListOrganizationServiceAccessStatus "https://docs.aws.amazon.com/goto/DotNetSDKV3/networkmanager-2019-07-05/ListOrganizationServiceAccessStatus")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/ListOrganizationServiceAccessStatus "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/ListOrganizationServiceAccessStatus")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/ListOrganizationServiceAccessStatus "https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/ListOrganizationServiceAccessStatus")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/ListOrganizationServiceAccessStatus "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/ListOrganizationServiceAccessStatus")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/ListOrganizationServiceAccessStatus "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/ListOrganizationServiceAccessStatus")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/ListOrganizationServiceAccessStatus "https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/ListOrganizationServiceAccessStatus")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/ListOrganizationServiceAccessStatus "https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/ListOrganizationServiceAccessStatus")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/ListOrganizationServiceAccessStatus "https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/ListOrganizationServiceAccessStatus")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/ListOrganizationServiceAccessStatus "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/ListOrganizationServiceAccessStatus")
