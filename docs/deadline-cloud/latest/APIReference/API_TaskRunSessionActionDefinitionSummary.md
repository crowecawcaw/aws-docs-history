# TaskRunSessionActionDefinitionSummary

The details of a task run in a session action.


## Contents





**stepId** 


The step ID.


Type: String


Pattern: `step-[0-9a-f]{32}`



Required: Yes




**parameters** 


The parameters of a task run in a session action.


Type: String to [TaskParameterValue](API_TaskParameterValue.md "API_TaskParameterValue.md") object map


Required: No




**taskId** 


The task ID.


Type: String


Pattern: `task-[0-9a-f]{32}-(0|([1-9][0-9]{0,9}))`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/TaskRunSessionActionDefinitionSummary "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/TaskRunSessionActionDefinitionSummary")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/TaskRunSessionActionDefinitionSummary "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/TaskRunSessionActionDefinitionSummary")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/TaskRunSessionActionDefinitionSummary "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/TaskRunSessionActionDefinitionSummary")
