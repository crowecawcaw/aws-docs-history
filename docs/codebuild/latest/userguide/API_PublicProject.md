

# PublicProject
<a name="API_PublicProject"></a>

**Note**  
This API element is not contained in the AWS CLI or AWS SDKs.

## Contents
<a name="API_PublicProject_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 **artifacts**   <a name="CodeBuild-Type-PublicProject-artifacts"></a>
Type: [PublicProjectArtifacts](API_PublicProjectArtifacts.md) object  
Required: No

 **buildBatchConfig**   <a name="CodeBuild-Type-PublicProject-buildBatchConfig"></a>
Type: [PublicProjectBuildBatchConfig](API_PublicProjectBuildBatchConfig.md) object  
Required: No

 **concurrentBuildLimit**   <a name="CodeBuild-Type-PublicProject-concurrentBuildLimit"></a>
Type: Integer  
Required: No

 **description**   <a name="CodeBuild-Type-PublicProject-description"></a>
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 255.  
Required: No

 **environment**   <a name="CodeBuild-Type-PublicProject-environment"></a>
Type: [PublicProjectEnvironment](API_PublicProjectEnvironment.md) object  
Required: No

 **name**   <a name="CodeBuild-Type-PublicProject-name"></a>
Type: String  
Length Constraints: Minimum length of 2. Maximum length of 150.  
Pattern: `[A-Za-z0-9][A-Za-z0-9\-_]{1,254}`   
Required: No

 **queuedTimeoutInMinutes**   <a name="CodeBuild-Type-PublicProject-queuedTimeoutInMinutes"></a>
Type: Integer  
Valid Range: Minimum value of 5. Maximum value of 480.  
Required: No

 **secondaryArtifacts**   <a name="CodeBuild-Type-PublicProject-secondaryArtifacts"></a>
Type: Array of [PublicProjectArtifacts](API_PublicProjectArtifacts.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 12 items.  
Required: No

 **secondarySources**   <a name="CodeBuild-Type-PublicProject-secondarySources"></a>
Type: Array of [PublicProjectSource](API_PublicProjectSource.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 12 items.  
Required: No

 **secondarySourceVersions**   <a name="CodeBuild-Type-PublicProject-secondarySourceVersions"></a>
Type: Array of [ProjectSourceVersion](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ProjectSourceVersion.html) objects  
Array Members: Minimum number of 0 items. Maximum number of 12 items.  
Required: No

 **source**   <a name="CodeBuild-Type-PublicProject-source"></a>
Type: [PublicProjectSource](API_PublicProjectSource.md) object  
Required: No

 **sourceVersion**   <a name="CodeBuild-Type-PublicProject-sourceVersion"></a>
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

 **timeoutInMinutes**   <a name="CodeBuild-Type-PublicProject-timeoutInMinutes"></a>
Type: Integer  
Valid Range: Minimum value of 5. Maximum value of 480.  
Required: No

 **webhook**   <a name="CodeBuild-Type-PublicProject-webhook"></a>
Type: [PublicWebhook](API_PublicWebhook.md) object  
Required: No