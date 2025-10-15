# CreateBudget

Creates a budget to set spending thresholds for your rendering activity.


## Request Syntax



```
POST /2023-10-12/farms/`farmId`/budgets HTTP/1.1
X-Amz-Client-Token: `clientToken`
Content-type: application/json

{
   "[actions](#deadlinecloud-CreateBudget-request-actions "#deadlinecloud-CreateBudget-request-actions")": [ 
      { 
         "[description](API_BudgetActionToAdd.md#deadlinecloud-Type-BudgetActionToAdd-description "API_BudgetActionToAdd.md#deadlinecloud-Type-BudgetActionToAdd-description")": "`string`",
         "[thresholdPercentage](API_BudgetActionToAdd.md#deadlinecloud-Type-BudgetActionToAdd-thresholdPercentage "API_BudgetActionToAdd.md#deadlinecloud-Type-BudgetActionToAdd-thresholdPercentage")": `number`,
         "[type](API_BudgetActionToAdd.md#deadlinecloud-Type-BudgetActionToAdd-type "API_BudgetActionToAdd.md#deadlinecloud-Type-BudgetActionToAdd-type")": "`string`"
      }
   ],
   "[approximateDollarLimit](#deadlinecloud-CreateBudget-request-approximateDollarLimit "#deadlinecloud-CreateBudget-request-approximateDollarLimit")": `number`,
   "[description](#deadlinecloud-CreateBudget-request-description "#deadlinecloud-CreateBudget-request-description")": "`string`",
   "[displayName](#deadlinecloud-CreateBudget-request-displayName "#deadlinecloud-CreateBudget-request-displayName")": "`string`",
   "[schedule](#deadlinecloud-CreateBudget-request-schedule "#deadlinecloud-CreateBudget-request-schedule")": { ... },
   "[usageTrackingResource](#deadlinecloud-CreateBudget-request-usageTrackingResource "#deadlinecloud-CreateBudget-request-usageTrackingResource")": { ... }
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[clientToken](#API_CreateBudget_RequestSyntax "#API_CreateBudget_RequestSyntax")**


The unique token which the server uses to recognize retries of the same request.


Length Constraints: Minimum length of 1. Maximum length of 64.




**[farmId](#API_CreateBudget_RequestSyntax "#API_CreateBudget_RequestSyntax")**


The farm ID to include in this budget.


Pattern: `farm-[0-9a-f]{32}`



Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[actions](#API_CreateBudget_RequestSyntax "#API_CreateBudget_RequestSyntax")**


The budget actions to specify what happens when the budget runs out.


Type: Array of [BudgetActionToAdd](API_BudgetActionToAdd.md "API_BudgetActionToAdd.md") objects


Array Members: Minimum number of 0 items. Maximum number of 10 items.


Required: Yes




**[approximateDollarLimit](#API_CreateBudget_RequestSyntax "#API_CreateBudget_RequestSyntax")**


The dollar limit based on consumed usage.


Type: Float


Valid Range: Minimum value of 0.01.


Required: Yes




**[description](#API_CreateBudget_RequestSyntax "#API_CreateBudget_RequestSyntax")**


The description of the budget.


###### Important

This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 100.


Required: No




**[displayName](#API_CreateBudget_RequestSyntax "#API_CreateBudget_RequestSyntax")**


The display name of the budget.


###### Important

This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 100.


Required: Yes




**[schedule](#API_CreateBudget_RequestSyntax "#API_CreateBudget_RequestSyntax")**


The schedule to associate with this budget.


Type: [BudgetSchedule](API_BudgetSchedule.md "API_BudgetSchedule.md") object



**Note:** This object is a Union. Only one member of this object can be specified or returned.


Required: Yes




**[usageTrackingResource](#API_CreateBudget_RequestSyntax "#API_CreateBudget_RequestSyntax")**


The queue ID provided to this budget to track usage.


Type: [UsageTrackingResource](API_UsageTrackingResource.md "API_UsageTrackingResource.md") object



**Note:** This object is a Union. Only one member of this object can be specified or returned.


Required: Yes




## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "[budgetId](#deadlinecloud-CreateBudget-response-budgetId "#deadlinecloud-CreateBudget-response-budgetId")": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[budgetId](#API_CreateBudget_ResponseSyntax "#API_CreateBudget_ResponseSyntax")**


The budget ID.


Type: String


Pattern: `budget-[0-9a-f]{32}`





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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/CreateBudget "https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/CreateBudget")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/CreateBudget "https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/CreateBudget")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/CreateBudget "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/CreateBudget")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/CreateBudget "https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/CreateBudget")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/CreateBudget "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/CreateBudget")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/CreateBudget "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/CreateBudget")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/CreateBudget "https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/CreateBudget")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/CreateBudget "https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/CreateBudget")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/CreateBudget "https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/CreateBudget")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/CreateBudget "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/CreateBudget")
