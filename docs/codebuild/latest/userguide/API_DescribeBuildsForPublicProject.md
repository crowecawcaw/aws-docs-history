# DescribeBuildsForPublicProject

###### Note

This API element is not contained in the AWS CLI or AWS SDKs.

## Request Syntax

```
{
   "maxResults": `number`,
   "nextToken": "`string`",
   "publicProjectAlias": "`string`",
   "sortOrder": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](../APIReference/CommonParameters.md "../APIReference/CommonParameters.md").

The request accepts the following data in JSON format.

###### Note

In the following list, the required parameters are described first.

**[publicProjectAlias](#API_DescribeBuildsForPublicProject_RequestSyntax "#API_DescribeBuildsForPublicProject_RequestSyntax")**

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `^[0-9a-zA-Z%+=]+$`

Required: Yes

**[maxResults](#API_DescribeBuildsForPublicProject_RequestSyntax "#API_DescribeBuildsForPublicProject_RequestSyntax")**

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 100.

Required: No

**[nextToken](#API_DescribeBuildsForPublicProject_RequestSyntax "#API_DescribeBuildsForPublicProject_RequestSyntax")**

Type: String

Required: No

**[sortOrder](#API_DescribeBuildsForPublicProject_RequestSyntax "#API_DescribeBuildsForPublicProject_RequestSyntax")**

Type: String

Valid Values: `ASCENDING | DESCENDING`

Required: No

## Response Syntax

```
{
   "builds": [
      {
         "artifacts": {
            "artifactIdentifier": "***string***",
            "packaging": "***string***",
            "type": "***string***"
         },
         "buildComplete": ***boolean***,
         "buildNumber": ***number***,
         "buildStatus": "***string***",
         "endTime": ***number***,
         "environment": {
            "computeType": "***string***",
            "environmentVariables": [
               {
                  "name": "***string***",
                  "type": "***string***",
                  "value": "***string***"
               }
            ],
            "image": "***string***",
            "type": "***string***"
         },
         "id": "***string***",
         "initiator": "***string***",
         "logsStatus": {
            "cloudWatchLogsStatus": "***string***",
            "s3LogsStatus": "***string***"
         },
         "phases": [
            {
               "contexts": [
                  {
                     "message": "***string***",
                     "statusCode": "***string***"
                  }
               ],
               "durationInSeconds": ***number***,
               "endTime": ***number***,
               "phaseStatus": "***string***",
               "phaseType": "***string***",
               "startTime": ***number***
            }
         ],
         "projectName": "***string***",
         "queuedTimeoutInMinutes": ***number***,
         "resolvedSourceVersion": "***string***",
         "secondaryArtifacts": [
            {
               "artifactIdentifier": "***string***",
               "packaging": "***string***",
               "type": "***string***"
            }
         ],
         "secondarySources": [
            {
               "buildspec": "***string***",
               "gitCloneDepth": ***number***,
               "gitSubmodulesConfig": {
                  "fetchSubmodules": ***boolean***
               },
               "location": "***string***",
               "sourceIdentifier": "***string***",
               "type": "***string***"
            }
         ],
         "secondarySourceVersions": [
            {
               "sourceIdentifier": "***string***",
               "sourceVersion": "***string***"
            }
         ],
         "source": {
            "buildspec": "***string***",
            "gitCloneDepth": ***number***,
            "gitSubmodulesConfig": {
               "fetchSubmodules": ***boolean***
            },
            "location": "***string***",
            "sourceIdentifier": "***string***",
            "type": "***string***"
         },
         "sourceVersion": "***string***",
         "startTime": ***number***,
         "timeoutInMinutes": ***number***
      }
   ],
   "nextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[builds](#API_DescribeBuildsForPublicProject_ResponseSyntax "#API_DescribeBuildsForPublicProject_ResponseSyntax")**

Type: Array of [PublicBuild](API_PublicBuild.md "API_PublicBuild.md") objects

**[nextToken](#API_DescribeBuildsForPublicProject_ResponseSyntax "#API_DescribeBuildsForPublicProject_ResponseSyntax")**

Type: String

## Errors

For information about the errors that are common to all actions, see [Common Errors](../APIReference/CommonErrors.md "../APIReference/CommonErrors.md").

**InvalidInputException**

HTTP Status Code: 400

**ResourceNotFoundException**

HTTP Status Code: 400
