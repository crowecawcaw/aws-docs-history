# BudgetSummary

The budget summary.


## Contents





**approximateDollarLimit** 


The approximate dollar limit of the budget.


Type: Float


Valid Range: Minimum value of 0.01.


Required: Yes




**budgetId** 


The budget ID.


Type: String


Pattern: `budget-[0-9a-f]{32}`



Required: Yes




**createdAt** 


The date and time the resource was created.


Type: Timestamp


Required: Yes




**createdBy** 


The user or system that created this resource.


Type: String


Required: Yes




**displayName** 


The display name of the budget summary to update.


###### Important

This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 100.


Required: Yes




**status** 


The status of the budget.



* `ACTIVE`–The budget is being evaluated.
* `INACTIVE`–The budget is inactive. This can include Expired,
 Canceled, or deleted Deleted statuses.

Type: String


Valid Values: `ACTIVE | INACTIVE`



Required: Yes




**usages** 


The consumed usage for the budget.


Type: [ConsumedUsages](API_ConsumedUsages.md "API_ConsumedUsages.md") object


Required: Yes




**usageTrackingResource** 


The resource used to track expenditure in the budget.


Type: [UsageTrackingResource](API_UsageTrackingResource.md "API_UsageTrackingResource.md") object



**Note:** This object is a Union. Only one member of this object can be specified or returned.


Required: Yes




**description** 



*This member has been deprecated.*



The description of the budget summary.


###### Important

This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 100.


Required: No




**updatedAt** 


The date and time the resource was updated.


Type: Timestamp


Required: No




**updatedBy** 


The user or system that updated this resource.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/BudgetSummary "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/BudgetSummary")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/BudgetSummary "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/BudgetSummary")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/BudgetSummary "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/BudgetSummary")
