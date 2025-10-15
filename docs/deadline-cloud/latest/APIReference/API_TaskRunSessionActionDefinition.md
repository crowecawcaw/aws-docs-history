# TaskRunSessionActionDefinition

The task, step, and parameters for the task run in the session action.


## Contents





**parameters** 


The task parameters.


Type: String to [TaskParameterValue](API_TaskParameterValue.md "API_TaskParameterValue.md") object map


Required: Yes




**stepId** 


The step ID.


Type: String


Pattern: `step-[0-9a-f]{32}`



Required: Yes




**taskId** 


The task ID.


Type: String


Pattern: `task-[0-9a-f]{32}-(0|([1-9][0-9]{0,9}))`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/TaskRunSessionActionDefinition "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/TaskRunSessionActionDefinition")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/TaskRunSessionActionDefinition "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/TaskRunSessionActionDefinition")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/TaskRunSessionActionDefinition "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/TaskRunSessionActionDefinition")
