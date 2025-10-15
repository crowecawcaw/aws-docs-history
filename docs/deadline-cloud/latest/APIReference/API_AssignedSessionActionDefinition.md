# AssignedSessionActionDefinition

The definition of the assigned session action.


## Contents


###### Important

This data type is a UNION, so only one of the following members can be specified when used or returned.





**envEnter** 


The environment a session starts on.


Type: [AssignedEnvironmentEnterSessionActionDefinition](API_AssignedEnvironmentEnterSessionActionDefinition.md "API_AssignedEnvironmentEnterSessionActionDefinition.md") object


Required: No




**envExit** 


The environment a session exits from.


Type: [AssignedEnvironmentExitSessionActionDefinition](API_AssignedEnvironmentExitSessionActionDefinition.md "API_AssignedEnvironmentExitSessionActionDefinition.md") object


Required: No




**syncInputJobAttachments** 


The job attachment to sync with an assigned session action.


Type: [AssignedSyncInputJobAttachmentsSessionActionDefinition](API_AssignedSyncInputJobAttachmentsSessionActionDefinition.md "API_AssignedSyncInputJobAttachmentsSessionActionDefinition.md") object


Required: No




**taskRun** 


The task run.


Type: [AssignedTaskRunSessionActionDefinition](API_AssignedTaskRunSessionActionDefinition.md "API_AssignedTaskRunSessionActionDefinition.md") object


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/AssignedSessionActionDefinition "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/AssignedSessionActionDefinition")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/AssignedSessionActionDefinition "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/AssignedSessionActionDefinition")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/AssignedSessionActionDefinition "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/AssignedSessionActionDefinition")
