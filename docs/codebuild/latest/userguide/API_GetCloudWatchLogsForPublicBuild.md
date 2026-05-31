# GetCloudWatchLogsForPublicBuild

###### Note

This API element is not contained in the AWS CLI or AWS SDKs.

## Request Syntax

```
{
   "maxResult": `number`,
   "nextToken": "`string`",
   "publicBuildAlias": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](../APIReference/CommonParameters.md "../APIReference/CommonParameters.md").

The request accepts the following data in JSON format.

###### Note

In the following list, the required parameters are described first.

**[publicBuildAlias](#API_GetCloudWatchLogsForPublicBuild_RequestSyntax "#API_GetCloudWatchLogsForPublicBuild_RequestSyntax")**

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `^[0-9a-zA-Z%+=]+:\p{XDigit}{8}(-\p{XDigit}{4}){3}-\p{XDigit}{12}$`

Required: Yes

**[maxResult](#API_GetCloudWatchLogsForPublicBuild_RequestSyntax "#API_GetCloudWatchLogsForPublicBuild_RequestSyntax")**

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 10000.

Required: No

**[nextToken](#API_GetCloudWatchLogsForPublicBuild_RequestSyntax "#API_GetCloudWatchLogsForPublicBuild_RequestSyntax")**

Type: String

Required: No

## Response Syntax

```
{
   "logs": [ "***string***" ],
   "nextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[logs](#API_GetCloudWatchLogsForPublicBuild_ResponseSyntax "#API_GetCloudWatchLogsForPublicBuild_ResponseSyntax")**

Type: Array of strings

**[nextToken](#API_GetCloudWatchLogsForPublicBuild_ResponseSyntax "#API_GetCloudWatchLogsForPublicBuild_ResponseSyntax")**

Type: String

Length Constraints: Minimum length of 1.

## Errors

For information about the errors that are common to all actions, see [Common Errors](../APIReference/CommonErrors.md "../APIReference/CommonErrors.md").

**InvalidInputException**

HTTP Status Code: 400

**ResourceNotFoundException**

HTTP Status Code: 400
