# ResponseBudgetAction

The details of a budget action.


## Contents





**thresholdPercentage** 


The percentage threshold for the budget.


Type: Float


Valid Range: Minimum value of 0. Maximum value of 100.


Required: Yes




**type** 


The action taken on the budget once scheduling stops.


Type: String


Valid Values: `STOP_SCHEDULING_AND_COMPLETE_TASKS | STOP_SCHEDULING_AND_CANCEL_TASKS`



Required: Yes




**description** 


The budget action description.


###### Important

This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 100.


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/ResponseBudgetAction "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/ResponseBudgetAction")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/ResponseBudgetAction "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/ResponseBudgetAction")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/ResponseBudgetAction "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/ResponseBudgetAction")
