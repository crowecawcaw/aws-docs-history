

# PublicBuild
<a name="API_PublicBuild"></a>

**Note**  
This API element is not contained in the AWS CLI or AWS SDKs.

## Contents
<a name="API_PublicBuild_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 **artifacts**   <a name="CodeBuild-Type-PublicBuild-artifacts"></a>
Type: [PublicBuildArtifacts](API_PublicBuildArtifacts.md) object  
Required: No

 **buildComplete**   <a name="CodeBuild-Type-PublicBuild-buildComplete"></a>
Type: Boolean  
Required: No

 **buildNumber**   <a name="CodeBuild-Type-PublicBuild-buildNumber"></a>
Type: Long  
Required: No

 **buildStatus**   <a name="CodeBuild-Type-PublicBuild-buildStatus"></a>
Type: String  
Valid Values:` PENDING | SUCCEEDED | FAILED | FAULT | TIMED_OUT | IN_PROGRESS | STOPPED`   
Required: No

 **endTime**   <a name="CodeBuild-Type-PublicBuild-endTime"></a>
Type: Timestamp  
Required: No

 **environment**   <a name="CodeBuild-Type-PublicBuild-environment"></a>
Type: [PublicProjectEnvironment](API_PublicProjectEnvironment.md) object  
Required: No

 **id**   <a name="CodeBuild-Type-PublicBuild-id"></a>
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

 **initiator**   <a name="CodeBuild-Type-PublicBuild-initiator"></a>
Type: String  
Required: No

 **logsStatus**   <a name="CodeBuild-Type-PublicBuild-logsStatus"></a>
Type: [PublicLogsStatus](API_PublicLogsStatus.md) object  
Required: No

 **phases**   <a name="CodeBuild-Type-PublicBuild-phases"></a>
Type: Array of [BuildPhase](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BuildPhase.html) objects  
Required: No

 **projectName**   <a name="CodeBuild-Type-PublicBuild-projectName"></a>
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

 **queuedTimeoutInMinutes**   <a name="CodeBuild-Type-PublicBuild-queuedTimeoutInMinutes"></a>
Type: Integer  
Required: No

 **resolvedSourceVersion**   <a name="CodeBuild-Type-PublicBuild-resolvedSourceVersion"></a>
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

 **secondaryArtifacts**   <a name="CodeBuild-Type-PublicBuild-secondaryArtifacts"></a>
Type: Array of [PublicBuildArtifacts](API_PublicBuildArtifacts.md) objects  
Required: No

 **secondarySources**   <a name="CodeBuild-Type-PublicBuild-secondarySources"></a>
Type: Array of [PublicProjectSource](API_PublicProjectSource.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 12 items.  
Required: No

 **secondarySourceVersions**   <a name="CodeBuild-Type-PublicBuild-secondarySourceVersions"></a>
Type: Array of [ProjectSourceVersion](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ProjectSourceVersion.html) objects  
Array Members: Minimum number of 0 items. Maximum number of 12 items.  
Required: No

 **source**   <a name="CodeBuild-Type-PublicBuild-source"></a>
Type: [PublicProjectSource](API_PublicProjectSource.md) object  
Required: No

 **sourceVersion**   <a name="CodeBuild-Type-PublicBuild-sourceVersion"></a>
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

 **startTime**   <a name="CodeBuild-Type-PublicBuild-startTime"></a>
Type: Timestamp  
Required: No

 **timeoutInMinutes**   <a name="CodeBuild-Type-PublicBuild-timeoutInMinutes"></a>
Type: Integer  
Required: No