# SessionActionSummary

The details of a session action.


## Contents





**definition** 


The session action definition.


Type: [SessionActionDefinitionSummary](API_SessionActionDefinitionSummary.md "API_SessionActionDefinitionSummary.md") object



**Note:** This object is a Union. Only one member of this object can be specified or returned.


Required: Yes




**sessionActionId** 


The session action ID.


Type: String


Pattern: `sessionaction-[0-9a-f]{32}-(0|([1-9][0-9]{0,9}))`



Required: Yes




**status** 


The status of the session action.


Type: String


Valid Values: `ASSIGNED | RUNNING | CANCELING | SUCCEEDED | FAILED | INTERRUPTED | CANCELED | NEVER_ATTEMPTED | SCHEDULED | RECLAIMING | RECLAIMED`



Required: Yes




**endedAt** 


The date and time the resource ended running.


Type: Timestamp


Required: No




**manifests** 


The list of manifest properties that describe file attachments for the task run.


Type: Array of [TaskRunManifestPropertiesResponse](API_TaskRunManifestPropertiesResponse.md "API_TaskRunManifestPropertiesResponse.md") objects


Required: No




**progressPercent** 


The completion percentage for the session action.


Type: Float


Valid Range: Minimum value of 0. Maximum value of 100.


Required: No




**startedAt** 


The date and time the resource started running.


Type: Timestamp


Required: No




**workerUpdatedAt** 


The Linux timestamp of the last date and time that the session action was
 updated.


Type: Timestamp


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/SessionActionSummary "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/SessionActionSummary")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/SessionActionSummary "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/SessionActionSummary")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/SessionActionSummary "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/SessionActionSummary")
