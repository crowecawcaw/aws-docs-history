

# GetCloudWatchLogsForPublicBuild
<a name="API_GetCloudWatchLogsForPublicBuild"></a>

**Note**  
This API element is not contained in the AWS CLI or AWS SDKs.

## Request Syntax
<a name="API_GetCloudWatchLogsForPublicBuild_RequestSyntax"></a>

```
{
   "maxResult": {{number}},
   "nextToken": "{{string}}",
   "publicBuildAlias": "{{string}}"
}
```

## Request Parameters
<a name="API_GetCloudWatchLogsForPublicBuild_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](https://docs.aws.amazon.com/codebuild/latest/APIReference/CommonParameters.html).

The request accepts the following data in JSON format.

**Note**  
In the following list, the required parameters are described first.

 ** [publicBuildAlias](#API_GetCloudWatchLogsForPublicBuild_RequestSyntax) **   <a name="CodeBuild-GetCloudWatchLogsForPublicBuild-request-publicBuildAlias"></a>
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^[0-9a-zA-Z%+=]+:\p{XDigit}{8}(-\p{XDigit}{4}){3}-\p{XDigit}{12}$`   
Required: Yes

 ** [maxResult](#API_GetCloudWatchLogsForPublicBuild_RequestSyntax) **   <a name="CodeBuild-GetCloudWatchLogsForPublicBuild-request-maxResult"></a>
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 10000.  
Required: No

 ** [nextToken](#API_GetCloudWatchLogsForPublicBuild_RequestSyntax) **   <a name="CodeBuild-GetCloudWatchLogsForPublicBuild-request-nextToken"></a>
Type: String  
Required: No

## Response Syntax
<a name="API_GetCloudWatchLogsForPublicBuild_ResponseSyntax"></a>

```
{
   "logs": [ "string" ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_GetCloudWatchLogsForPublicBuild_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [logs](#API_GetCloudWatchLogsForPublicBuild_ResponseSyntax) **   <a name="CodeBuild-GetCloudWatchLogsForPublicBuild-response-logs"></a>
Type: Array of strings

 ** [nextToken](#API_GetCloudWatchLogsForPublicBuild_ResponseSyntax) **   <a name="CodeBuild-GetCloudWatchLogsForPublicBuild-response-nextToken"></a>
Type: String  
Length Constraints: Minimum length of 1.

## Errors
<a name="API_GetCloudWatchLogsForPublicBuild_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](https://docs.aws.amazon.com/codebuild/latest/APIReference/CommonErrors.html).

 **InvalidInputException**   
HTTP Status Code: 400

 **ResourceNotFoundException**   
HTTP Status Code: 400