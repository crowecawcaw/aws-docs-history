

# PublicProjectSource
<a name="API_PublicProjectSource"></a>

**Note**  
This API element is not contained in the AWS CLI or AWS SDKs.

## Contents
<a name="API_PublicProjectSource_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 **type**   <a name="CodeBuild-Type-PublicProjectSource-type"></a>
Type: String  
Valid Values:` NO_SOURCE | CODECOMMIT | CODEPIPELINE | GITHUB | S3 | BITBUCKET | GITHUB_ENTERPRISE | GITLAB | GITLAB_SELF_MANAGED`   
Required: Yes

 **buildspec**   <a name="CodeBuild-Type-PublicProjectSource-buildspec"></a>
Type: String  
Required: No

 **gitCloneDepth**   <a name="CodeBuild-Type-PublicProjectSource-gitCloneDepth"></a>
Type: Integer  
Valid Range: Minimum value of 0.  
Required: No

 **gitSubmodulesConfig**   <a name="CodeBuild-Type-PublicProjectSource-gitSubmodulesConfig"></a>
 Information about the Git submodules configuration for an AWS CodeBuild build project.   
Type: [GitSubmodulesConfig](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_GitSubmodulesConfig.html) object  
Required: No

 **location**   <a name="CodeBuild-Type-PublicProjectSource-location"></a>
Type: String  
Required: No

 **sourceIdentifier**   <a name="CodeBuild-Type-PublicProjectSource-sourceIdentifier"></a>
Type: String  
Required: No