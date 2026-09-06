

# PublicBuildSummary
<a name="API_PublicBuildSummary"></a>

**Note**  
This API element is not contained in the AWS CLI or AWS SDKs.

## Contents
<a name="API_PublicBuildSummary_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 **buildStatus**   <a name="CodeBuild-Type-PublicBuildSummary-buildStatus"></a>
Type: String  
Required: No

 **primaryArtifact**   <a name="CodeBuild-Type-PublicBuildSummary-primaryArtifact"></a>
Represents a resolved build artifact. A resolved artifact is an artifact that is built and deployed to the destination, such as Amazon S3.  
Type: [ResolvedArtifact](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ResolvedArtifact.html) object  
Required: No

 **publicBuildAlias**   <a name="CodeBuild-Type-PublicBuildSummary-publicBuildAlias"></a>
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^[0-9a-zA-Z%+=]+:\p{XDigit}{8}(-\p{XDigit}{4}){3}-\p{XDigit}{12}$`   
Required: No

 **requestedOn**   <a name="CodeBuild-Type-PublicBuildSummary-requestedOn"></a>
Type: Timestamp  
Required: No

 **secondaryArtifacts**   <a name="CodeBuild-Type-PublicBuildSummary-secondaryArtifacts"></a>
Type: Array of [ResolvedArtifact](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ResolvedArtifact.html) objects  
Required: No