# SessionActionDefinition

The definition of the session action.


## Contents


###### Important

This data type is a UNION, so only one of the following members can be specified when used or returned.





**envEnter** 


The environment to enter into.


Type: [EnvironmentEnterSessionActionDefinition](API_EnvironmentEnterSessionActionDefinition.md "API_EnvironmentEnterSessionActionDefinition.md") object


Required: No




**envExit** 


The environment to exit from.


Type: [EnvironmentExitSessionActionDefinition](API_EnvironmentExitSessionActionDefinition.md "API_EnvironmentExitSessionActionDefinition.md") object


Required: No




**syncInputJobAttachments** 


The job attachments to sync with a session action.


Type: [SyncInputJobAttachmentsSessionActionDefinition](API_SyncInputJobAttachmentsSessionActionDefinition.md "API_SyncInputJobAttachmentsSessionActionDefinition.md") object


Required: No




**taskRun** 


The task run in the session.


Type: [TaskRunSessionActionDefinition](API_TaskRunSessionActionDefinition.md "API_TaskRunSessionActionDefinition.md") object


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/SessionActionDefinition "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/SessionActionDefinition")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/SessionActionDefinition "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/SessionActionDefinition")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/SessionActionDefinition "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/SessionActionDefinition")
