# GetBudget

Get a budget.


## Request Syntax



```
GET /2023-10-12/farms/`farmId`/budgets/`budgetId` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[budgetId](#API_GetBudget_RequestSyntax "#API_GetBudget_RequestSyntax")**


The budget ID.


Pattern: `budget-[0-9a-f]{32}`



Required: Yes




**[farmId](#API_GetBudget_RequestSyntax "#API_GetBudget_RequestSyntax")**


The farm ID of the farm connected to the budget.


Pattern: `farm-[0-9a-f]{32}`



Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "actions": [ 
      { 
         "description": "***string***",
         "thresholdPercentage": ***number***,
         "type": "***string***"
      }
   ],
   "approximateDollarLimit": ***number***,
   "budgetId": "***string***",
   "createdAt": "***string***",
   "createdBy": "***string***",
   "description": "***string***",
   "displayName": "***string***",
   "queueStoppedAt": "***string***",
   "schedule": { ... },
   "status": "***string***",
   "updatedAt": "***string***",
   "updatedBy": "***string***",
   "usages": { 
      "approximateDollarUsage": ***number***
   },
   "usageTrackingResource": { ... }
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[actions](#API_GetBudget_ResponseSyntax "#API_GetBudget_ResponseSyntax")**


The budget actions for the budget.


Type: Array of [ResponseBudgetAction](API_ResponseBudgetAction.md "API_ResponseBudgetAction.md") objects


Array Members: Minimum number of 0 items. Maximum number of 10 items.




**[approximateDollarLimit](#API_GetBudget_ResponseSyntax "#API_GetBudget_ResponseSyntax")**


The consumed usage limit for the budget.


Type: Float


Valid Range: Minimum value of 0.01.




**[budgetId](#API_GetBudget_ResponseSyntax "#API_GetBudget_ResponseSyntax")**


The budget ID.


Type: String


Pattern: `budget-[0-9a-f]{32}`





**[createdAt](#API_GetBudget_ResponseSyntax "#API_GetBudget_ResponseSyntax")**


The date and time the resource was created.


Type: Timestamp




**[createdBy](#API_GetBudget_ResponseSyntax "#API_GetBudget_ResponseSyntax")**


The user or system that created this resource.


Type: String




**[description](#API_GetBudget_ResponseSyntax "#API_GetBudget_ResponseSyntax")**


The description of the budget.


###### Important

This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 100.




**[displayName](#API_GetBudget_ResponseSyntax "#API_GetBudget_ResponseSyntax")**


The display name of the budget.


###### Important

This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 100.




**[queueStoppedAt](#API_GetBudget_ResponseSyntax "#API_GetBudget_ResponseSyntax")**


The date and time the queue stopped.


Type: Timestamp




**[schedule](#API_GetBudget_ResponseSyntax "#API_GetBudget_ResponseSyntax")**


The budget schedule.


Type: [BudgetSchedule](API_BudgetSchedule.md "API_BudgetSchedule.md") object



**Note:** This object is a Union. Only one member of this object can be specified or returned.




**[status](#API_GetBudget_ResponseSyntax "#API_GetBudget_ResponseSyntax")**


The status of the budget.



* `ACTIVE`–Get a budget being evaluated.
* `INACTIVE`–Get an inactive budget. This can include expired,
 canceled, or deleted statuses.

Type: String


Valid Values: `ACTIVE | INACTIVE`





**[updatedAt](#API_GetBudget_ResponseSyntax "#API_GetBudget_ResponseSyntax")**


The date and time the resource was updated.


Type: Timestamp




**[updatedBy](#API_GetBudget_ResponseSyntax "#API_GetBudget_ResponseSyntax")**


The user or system that updated this resource.


Type: String




**[usages](#API_GetBudget_ResponseSyntax "#API_GetBudget_ResponseSyntax")**


The usages of the budget.


Type: [ConsumedUsages](API_ConsumedUsages.md "API_ConsumedUsages.md") object




**[usageTrackingResource](#API_GetBudget_ResponseSyntax "#API_GetBudget_ResponseSyntax")**


The resource that the budget is tracking usage for.


Type: [UsageTrackingResource](API_UsageTrackingResource.md "API_UsageTrackingResource.md") object



**Note:** This object is a Union. Only one member of this object can be specified or returned.




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



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/GetBudget "https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/GetBudget")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/GetBudget "https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/GetBudget")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/GetBudget "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/GetBudget")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/GetBudget "https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/GetBudget")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/GetBudget "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/GetBudget")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/GetBudget "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/GetBudget")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/GetBudget "https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/GetBudget")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/GetBudget "https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/GetBudget")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/GetBudget "https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/GetBudget")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/GetBudget "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/GetBudget")
