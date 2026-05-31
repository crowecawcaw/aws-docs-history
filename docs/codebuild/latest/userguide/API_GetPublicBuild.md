# GetPublicBuild

###### Note

This API element is not contained in the AWS CLI or AWS SDKs.

## Request Syntax

```
{
   "publicBuildAlias": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](../APIReference/CommonParameters.md "../APIReference/CommonParameters.md").

The request accepts the following data in JSON format.

###### Note

In the following list, the required parameters are described first.

**[publicBuildAlias](#API_GetPublicBuild_RequestSyntax "#API_GetPublicBuild_RequestSyntax")**

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `^[0-9a-zA-Z%+=]+:\p{XDigit}{8}(-\p{XDigit}{4}){3}-\p{XDigit}{12}$`

Required: Yes

## Response Syntax

```
{
   "build": {
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
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[build](#API_GetPublicBuild_ResponseSyntax "#API_GetPublicBuild_ResponseSyntax")**

Type: [PublicBuild](API_PublicBuild.md "API_PublicBuild.md") object

## Errors

For information about the errors that are common to all actions, see [Common Errors](../APIReference/CommonErrors.md "../APIReference/CommonErrors.md").

**InvalidInputException**

HTTP Status Code: 400

**ResourceNotFoundException**

HTTP Status Code: 400
