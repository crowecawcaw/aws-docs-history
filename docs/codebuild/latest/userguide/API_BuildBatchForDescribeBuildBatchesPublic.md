

# BuildBatchForDescribeBuildBatchesPublic
<a name="API_BuildBatchForDescribeBuildBatchesPublic"></a>

**Note**  
This API element is not contained in the AWS CLI or AWS SDKs.

## Contents
<a name="API_BuildBatchForDescribeBuildBatchesPublic_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 **buildBatchNumber**   <a name="CodeBuild-Type-BuildBatchForDescribeBuildBatchesPublic-buildBatchNumber"></a>
Type: Long  
Required: No

 **buildBatchStatus**   <a name="CodeBuild-Type-BuildBatchForDescribeBuildBatchesPublic-buildBatchStatus"></a>
Type: String  
Valid Values:` PENDING | SUCCEEDED | FAILED | FAULT | TIMED_OUT | IN_PROGRESS | STOPPED`   
Required: No

 **endTime**   <a name="CodeBuild-Type-BuildBatchForDescribeBuildBatchesPublic-endTime"></a>
Type: Timestamp  
Required: No

 **publicBuildBatchAlias**   <a name="CodeBuild-Type-BuildBatchForDescribeBuildBatchesPublic-publicBuildBatchAlias"></a>
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^[0-9a-zA-Z%+=]+:[a-z0-9]{8}(-[a-z0-9]{4}){3}-[a-z0-9]{12}$`   
Required: No

 **sourceVersion**   <a name="CodeBuild-Type-BuildBatchForDescribeBuildBatchesPublic-sourceVersion"></a>
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

 **startTime**   <a name="CodeBuild-Type-BuildBatchForDescribeBuildBatchesPublic-startTime"></a>
Type: Timestamp  
Required: No