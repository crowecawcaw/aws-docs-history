# UpdateBudget

Updates a budget that sets spending thresholds for rendering activity.


## Request Syntax



```
PATCH /2023-10-12/farms/`farmId`/budgets/`budgetId` HTTP/1.1
X-Amz-Client-Token: `clientToken`
Content-type: application/json

{
   "[actionsToAdd](#deadlinecloud-UpdateBudget-request-actionsToAdd "#deadlinecloud-UpdateBudget-request-actionsToAdd")": [ 
      { 
         "[description](API_BudgetActionToAdd.md#deadlinecloud-Type-BudgetActionToAdd-description "API_BudgetActionToAdd.md#deadlinecloud-Type-BudgetActionToAdd-description")": "`string`",
         "[thresholdPercentage](API_BudgetActionToAdd.md#deadlinecloud-Type-BudgetActionToAdd-thresholdPercentage "API_BudgetActionToAdd.md#deadlinecloud-Type-BudgetActionToAdd-thresholdPercentage")": `number`,
         "[type](API_BudgetActionToAdd.md#deadlinecloud-Type-BudgetActionToAdd-type "API_BudgetActionToAdd.md#deadlinecloud-Type-BudgetActionToAdd-type")": "`string`"
      }
   ],
   "[actionsToRemove](#deadlinecloud-UpdateBudget-request-actionsToRemove "#deadlinecloud-UpdateBudget-request-actionsToRemove")": [ 
      { 
         "[thresholdPercentage](API_BudgetActionToRemove.md#deadlinecloud-Type-BudgetActionToRemove-thresholdPercentage "API_BudgetActionToRemove.md#deadlinecloud-Type-BudgetActionToRemove-thresholdPercentage")": `number`,
         "[type](API_BudgetActionToRemove.md#deadlinecloud-Type-BudgetActionToRemove-type "API_BudgetActionToRemove.md#deadlinecloud-Type-BudgetActionToRemove-type")": "`string`"
      }
   ],
   "[approximateDollarLimit](#deadlinecloud-UpdateBudget-request-approximateDollarLimit "#deadlinecloud-UpdateBudget-request-approximateDollarLimit")": `number`,
   "[description](#deadlinecloud-UpdateBudget-request-description "#deadlinecloud-UpdateBudget-request-description")": "`string`",
   "[displayName](#deadlinecloud-UpdateBudget-request-displayName "#deadlinecloud-UpdateBudget-request-displayName")": "`string`",
   "[schedule](#deadlinecloud-UpdateBudget-request-schedule "#deadlinecloud-UpdateBudget-request-schedule")": { ... },
   "[status](#deadlinecloud-UpdateBudget-request-status "#deadlinecloud-UpdateBudget-request-status")": "`string`"
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[budgetId](#API_UpdateBudget_RequestSyntax "#API_UpdateBudget_RequestSyntax")**


The budget ID to update.


Pattern: `budget-[0-9a-f]{32}`



Required: Yes




**[clientToken](#API_UpdateBudget_RequestSyntax "#API_UpdateBudget_RequestSyntax")**


The unique token which the server uses to recognize retries of the same request.


Length Constraints: Minimum length of 1. Maximum length of 64.




**[farmId](#API_UpdateBudget_RequestSyntax "#API_UpdateBudget_RequestSyntax")**


The farm ID of the budget to update.


Pattern: `farm-[0-9a-f]{32}`



Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[actionsToAdd](#API_UpdateBudget_RequestSyntax "#API_UpdateBudget_RequestSyntax")**


The budget actions to add. Budget actions specify what happens when the budget runs
 out.


Type: Array of [BudgetActionToAdd](API_BudgetActionToAdd.md "API_BudgetActionToAdd.md") objects


Array Members: Minimum number of 0 items. Maximum number of 10 items.


Required: No




**[actionsToRemove](#API_UpdateBudget_RequestSyntax "#API_UpdateBudget_RequestSyntax")**


The budget actions to remove from the budget.


Type: Array of [BudgetActionToRemove](API_BudgetActionToRemove.md "API_BudgetActionToRemove.md") objects


Array Members: Minimum number of 0 items. Maximum number of 10 items.


Required: No




**[approximateDollarLimit](#API_UpdateBudget_RequestSyntax "#API_UpdateBudget_RequestSyntax")**


The dollar limit to update on the budget. Based on consumed usage.


Type: Float


Valid Range: Minimum value of 0.01.


Required: No




**[description](#API_UpdateBudget_RequestSyntax "#API_UpdateBudget_RequestSyntax")**


The description of the budget to update.


###### Important

This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 100.


Required: No




**[displayName](#API_UpdateBudget_RequestSyntax "#API_UpdateBudget_RequestSyntax")**


The display name of the budget to update.


###### Important

This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 100.


Required: No




**[schedule](#API_UpdateBudget_RequestSyntax "#API_UpdateBudget_RequestSyntax")**


The schedule to update.


Type: [BudgetSchedule](API_BudgetSchedule.md "API_BudgetSchedule.md") object



**Note:** This object is a Union. Only one member of this object can be specified or returned.


Required: No




**[status](#API_UpdateBudget_RequestSyntax "#API_UpdateBudget_RequestSyntax")**


Updates the status of the budget.



* `ACTIVE`–The budget is being evaluated.
* `INACTIVE`–The budget is inactive. This can include Expired,
 Canceled, or deleted Deleted statuses.

Type: String


Valid Values: `ACTIVE | INACTIVE`



Required: No




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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/UpdateBudget "https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/UpdateBudget")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/UpdateBudget "https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/UpdateBudget")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/UpdateBudget "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/UpdateBudget")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/UpdateBudget "https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/UpdateBudget")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/UpdateBudget "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/UpdateBudget")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/UpdateBudget "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/UpdateBudget")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/UpdateBudget "https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/UpdateBudget")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/UpdateBudget "https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/UpdateBudget")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/UpdateBudget "https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/UpdateBudget")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/UpdateBudget "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/UpdateBudget")
