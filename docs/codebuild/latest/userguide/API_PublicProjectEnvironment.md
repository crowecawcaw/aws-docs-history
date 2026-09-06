

# PublicProjectEnvironment
<a name="API_PublicProjectEnvironment"></a>

**Note**  
This API element is not contained in the AWS CLI or AWS SDKs.

## Contents
<a name="API_PublicProjectEnvironment_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 **computeType**   <a name="CodeBuild-Type-PublicProjectEnvironment-computeType"></a>
Type: String  
Valid Values:` BUILD_GENERAL1_SMALL | BUILD_GENERAL1_MEDIUM | BUILD_GENERAL1_LARGE | BUILD_GENERAL1_2XLARGE`   
Required: No

 **environmentVariables**   <a name="CodeBuild-Type-PublicProjectEnvironment-environmentVariables"></a>
Type: Array of [EnvironmentVariable](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_EnvironmentVariable.html) objects  
Required: No

 **image**   <a name="CodeBuild-Type-PublicProjectEnvironment-image"></a>
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

 **type**   <a name="CodeBuild-Type-PublicProjectEnvironment-type"></a>
Type: String  
Valid Values:` WINDOWS_CONTAINER | WINDOWS_SERVER_2019_CONTAINER | LINUX_CONTAINER | LINUX_GPU_CONTAINER | ARM_CONTAINER | MAC`   
Required: No