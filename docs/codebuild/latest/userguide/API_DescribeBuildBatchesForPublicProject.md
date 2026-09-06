

# DescribeBuildBatchesForPublicProject
<a name="API_DescribeBuildBatchesForPublicProject"></a>

**Note**  
This API element is not contained in the AWS CLI or AWS SDKs.

## Request Syntax
<a name="API_DescribeBuildBatchesForPublicProject_RequestSyntax"></a>

```
{
   "filter": { 
      "[status](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BuildBatchFilter.html)": "{{string}}"
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "publicProjectAlias": "{{string}}",
   "sortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeBuildBatchesForPublicProject_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](https://docs.aws.amazon.com/codebuild/latest/APIReference/CommonParameters.html).

The request accepts the following data in JSON format.

**Note**  
In the following list, the required parameters are described first.

 ** [publicProjectAlias](#API_DescribeBuildBatchesForPublicProject_RequestSyntax) **   <a name="CodeBuild-DescribeBuildBatchesForPublicProject-request-publicProjectAlias"></a>
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^[0-9a-zA-Z%+=]+$`   
Required: Yes

 ** [filter](#API_DescribeBuildBatchesForPublicProject_RequestSyntax) **   <a name="CodeBuild-DescribeBuildBatchesForPublicProject-request-filter"></a>
Specifies filters when retrieving batch builds.  
Type: [BuildBatchFilter](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BuildBatchFilter.html) object  
Required: No

 ** [maxResults](#API_DescribeBuildBatchesForPublicProject_RequestSyntax) **   <a name="CodeBuild-DescribeBuildBatchesForPublicProject-request-maxResults"></a>
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [nextToken](#API_DescribeBuildBatchesForPublicProject_RequestSyntax) **   <a name="CodeBuild-DescribeBuildBatchesForPublicProject-request-nextToken"></a>
Type: String  
Required: No

 ** [sortOrder](#API_DescribeBuildBatchesForPublicProject_RequestSyntax) **   <a name="CodeBuild-DescribeBuildBatchesForPublicProject-request-sortOrder"></a>
Type: String  
Valid Values:` ASCENDING | DESCENDING`   
Required: No

## Response Syntax
<a name="API_DescribeBuildBatchesForPublicProject_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "publicBuildBatches": [ 
      { 
         "buildBatchNumber": number,
         "buildBatchStatus": "string",
         "endTime": number,
         "publicBuildBatchAlias": "string",
         "sourceVersion": "string",
         "startTime": number
      }
   ]
}
```

## Response Elements
<a name="API_DescribeBuildBatchesForPublicProject_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_DescribeBuildBatchesForPublicProject_ResponseSyntax) **   <a name="CodeBuild-DescribeBuildBatchesForPublicProject-response-nextToken"></a>
Type: String

 ** [publicBuildBatches](#API_DescribeBuildBatchesForPublicProject_ResponseSyntax) **   <a name="CodeBuild-DescribeBuildBatchesForPublicProject-response-publicBuildBatches"></a>
Type: Array of [BuildBatchForDescribeBuildBatchesPublic](API_BuildBatchForDescribeBuildBatchesPublic.md) objects

## Errors
<a name="API_DescribeBuildBatchesForPublicProject_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](https://docs.aws.amazon.com/codebuild/latest/APIReference/CommonErrors.html).

 **InvalidInputException**   
HTTP Status Code: 400

 **ResourceNotFoundException**   
HTTP Status Code: 400