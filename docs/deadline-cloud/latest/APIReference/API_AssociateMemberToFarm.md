# AssociateMemberToFarm

Assigns a farm membership level to a member.


## Request Syntax



```
PUT /2023-10-12/farms/`farmId`/members/`principalId` HTTP/1.1
Content-type: application/json

{
   "identityStoreId": "`string`",
   "membershipLevel": "`string`",
   "principalType": "`string`"
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[farmId](#API_AssociateMemberToFarm_RequestSyntax "#API_AssociateMemberToFarm_RequestSyntax")**


The ID of the farm to associate with the member.


Pattern: `farm-[0-9a-f]{32}`



Required: Yes




**[principalId](#API_AssociateMemberToFarm_RequestSyntax "#API_AssociateMemberToFarm_RequestSyntax")**


The member's principal ID to associate with the farm.


Length Constraints: Minimum length of 1. Maximum length of 47.


Pattern: `([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}`



Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[identityStoreId](#API_AssociateMemberToFarm_RequestSyntax "#API_AssociateMemberToFarm_RequestSyntax")**


The identity store ID of the member to associate with the farm.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 36.


Pattern: `d-[0-9a-f]{10}$|^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`



Required: Yes




**[membershipLevel](#API_AssociateMemberToFarm_RequestSyntax "#API_AssociateMemberToFarm_RequestSyntax")**


The principal's membership level for the associated farm.


Type: String


Valid Values: `VIEWER | CONTRIBUTOR | OWNER | MANAGER`



Required: Yes




**[principalType](#API_AssociateMemberToFarm_RequestSyntax "#API_AssociateMemberToFarm_RequestSyntax")**


The principal type of the member to associate with the farm.


Type: String


Valid Values: `USER | GROUP`



Required: Yes




## Response Syntax



```
HTTP/1.1 200

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDeniedException** 


You don't have permission to perform the action.





**context** 


Information about the resources in use when the exception was thrown.




HTTP Status Code: 403




**InternalServerErrorException** 


Deadline Cloud can't process your request right now. Try again later.





**retryAfterSeconds** 


The number of seconds a client should wait before retrying the request.




HTTP Status Code: 500




**ResourceNotFoundException** 


The requested resource can't be found.





**context** 


Information about the resources in use when the exception was thrown.




**resourceId** 


The identifier of the resource that couldn't be found.




**resourceType** 


The type of the resource that couldn't be found.




HTTP Status Code: 404




**ServiceQuotaExceededException** 


You exceeded your service quota. Service quotas, also referred to as limits, are the
 maximum number of service resources or operations for your AWS account.





**context** 


Information about the resources in use when the exception was thrown.




**quotaCode** 


Identifies the quota that has been exceeded.




**reason** 


A string that describes the reason the quota was exceeded.




**resourceId** 


The identifier of the affected resource.




**resourceType** 


The type of the affected resource




**serviceCode** 


Identifies the service that exceeded the quota.




HTTP Status Code: 402




**ThrottlingException** 


Your request exceeded a request rate quota.





**context** 


Information about the resources in use when the exception was thrown.




**quotaCode** 


Identifies the quota that is being throttled.




**retryAfterSeconds** 


The number of seconds a client should wait before retrying the request.




**serviceCode** 


Identifies the service that is being throttled.




HTTP Status Code: 429




**ValidationException** 


The request isn't valid. This can occur if your request contains malformed JSON or
 unsupported characters.





**context** 


Information about the resources in use when the exception was thrown.




**fieldList** 


A list of fields that failed validation.




**reason** 


The reason that the request failed validation.




HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/AssociateMemberToFarm "https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/AssociateMemberToFarm")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/AssociateMemberToFarm "https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/AssociateMemberToFarm")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/AssociateMemberToFarm "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/AssociateMemberToFarm")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/AssociateMemberToFarm "https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/AssociateMemberToFarm")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/AssociateMemberToFarm "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/AssociateMemberToFarm")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/AssociateMemberToFarm "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/AssociateMemberToFarm")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/AssociateMemberToFarm "https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/AssociateMemberToFarm")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/AssociateMemberToFarm "https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/AssociateMemberToFarm")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/AssociateMemberToFarm "https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/AssociateMemberToFarm")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/AssociateMemberToFarm "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/AssociateMemberToFarm")
