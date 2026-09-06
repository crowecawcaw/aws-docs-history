

# PublicBuildBatch
<a name="API_PublicBuildBatch"></a>

**Note**  
This API element is not contained in the AWS CLI or AWS SDKs.

## Contents
<a name="API_PublicBuildBatch_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 **artifacts**   <a name="CodeBuild-Type-PublicBuildBatch-artifacts"></a>
Type: [PublicBuildArtifacts](API_PublicBuildArtifacts.md) object  
Required: No

 **buildBatchConfig**   <a name="CodeBuild-Type-PublicBuildBatch-buildBatchConfig"></a>
Type: [PublicProjectBuildBatchConfig](API_PublicProjectBuildBatchConfig.md) object  
Required: No

 **buildBatchNumber**   <a name="CodeBuild-Type-PublicBuildBatch-buildBatchNumber"></a>
Type: Long  
Required: No

 **buildBatchStatus**   <a name="CodeBuild-Type-PublicBuildBatch-buildBatchStatus"></a>
Type: String  
Valid Values:` PENDING | SUCCEEDED | FAILED | FAULT | TIMED_OUT | IN_PROGRESS | STOPPED`   
Required: No

 **buildGroups**   <a name="CodeBuild-Type-PublicBuildBatch-buildGroups"></a>
Type: Array of [PublicBuildGroup](API_PublicBuildGroup.md) objects  
Required: No

 **buildTimeoutInMinutes**   <a name="CodeBuild-Type-PublicBuildBatch-buildTimeoutInMinutes"></a>
Type: Integer  
Required: No

 **complete**   <a name="CodeBuild-Type-PublicBuildBatch-complete"></a>
Type: Boolean  
Required: No

 **currentPhase**   <a name="CodeBuild-Type-PublicBuildBatch-currentPhase"></a>
Type: String  
Required: No

 **endTime**   <a name="CodeBuild-Type-PublicBuildBatch-endTime"></a>
Type: Timestamp  
Required: No

 **environment**   <a name="CodeBuild-Type-PublicBuildBatch-environment"></a>
Type: [PublicProjectEnvironment](API_PublicProjectEnvironment.md) object  
Required: No

 **id**   <a name="CodeBuild-Type-PublicBuildBatch-id"></a>
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

 **initiator**   <a name="CodeBuild-Type-PublicBuildBatch-initiator"></a>
Type: String  
Required: No

 **logsStatus**   <a name="CodeBuild-Type-PublicBuildBatch-logsStatus"></a>
Type: [PublicLogsStatus](API_PublicLogsStatus.md) object  
Required: No

 **phases**   <a name="CodeBuild-Type-PublicBuildBatch-phases"></a>
Type: Array of [BuildBatchPhase](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BuildBatchPhase.html) objects  
Required: No

 **projectName**   <a name="CodeBuild-Type-PublicBuildBatch-projectName"></a>
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

 **publicBuildBatchAlias**   <a name="CodeBuild-Type-PublicBuildBatch-publicBuildBatchAlias"></a>
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^[0-9a-zA-Z%+=]+:[a-z0-9]{8}(-[a-z0-9]{4}){3}-[a-z0-9]{12}$`   
Required: No

 **queuedTimeoutInMinutes**   <a name="CodeBuild-Type-PublicBuildBatch-queuedTimeoutInMinutes"></a>
Type: Integer  
Required: No

 **resolvedSourceVersion**   <a name="CodeBuild-Type-PublicBuildBatch-resolvedSourceVersion"></a>
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

 **secondaryArtifacts**   <a name="CodeBuild-Type-PublicBuildBatch-secondaryArtifacts"></a>
Type: Array of [PublicBuildArtifacts](API_PublicBuildArtifacts.md) objects  
Required: No

 **secondarySources**   <a name="CodeBuild-Type-PublicBuildBatch-secondarySources"></a>
Type: Array of [PublicProjectSource](API_PublicProjectSource.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 12 items.  
Required: No

 **secondarySourceVersions**   <a name="CodeBuild-Type-PublicBuildBatch-secondarySourceVersions"></a>
Type: Array of [ProjectSourceVersion](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ProjectSourceVersion.html) objects  
Array Members: Minimum number of 0 items. Maximum number of 12 items.  
Required: No

 **source**   <a name="CodeBuild-Type-PublicBuildBatch-source"></a>
Type: [PublicProjectSource](API_PublicProjectSource.md) object  
Required: No

 **sourceVersion**   <a name="CodeBuild-Type-PublicBuildBatch-sourceVersion"></a>
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

 **startTime**   <a name="CodeBuild-Type-PublicBuildBatch-startTime"></a>
Type: Timestamp  
Required: No