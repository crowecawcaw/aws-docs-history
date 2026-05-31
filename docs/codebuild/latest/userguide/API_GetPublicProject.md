# GetPublicProject

###### Note

This API element is not contained in the AWS CLI or AWS SDKs.

## Request Syntax

```
{
   "publicProjectAlias": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](../APIReference/CommonParameters.md "../APIReference/CommonParameters.md").

The request accepts the following data in JSON format.

###### Note

In the following list, the required parameters are described first.

**[publicProjectAlias](#API_GetPublicProject_RequestSyntax "#API_GetPublicProject_RequestSyntax")**

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `^[0-9a-zA-Z%+=]+$`

Required: Yes

## Response Syntax

```
{
   "project": {
      "artifacts": {
         "artifactIdentifier": "***string***",
         "location": "***string***",
         "type": "***string***"
      },
      "buildBatchConfig": {
         "combineArtifacts": ***boolean***,
         "restrictions": {
            "computeTypesAllowed": [ "***string***" ],
            "maximumBuildsAllowed": ***number***
         },
         "timeoutInMins": ***number***
      },
      "concurrentBuildLimit": ***number***,
      "description": "***string***",
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
      "name": "***string***",
      "queuedTimeoutInMinutes": ***number***,
      "secondaryArtifacts": [
         {
            "artifactIdentifier": "***string***",
            "location": "***string***",
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
      "timeoutInMinutes": ***number***,
      "webhook": {
         "branchFilter": "***string***",
         "buildType": "***string***",
         "filterGroups": [
            [
               {
                  "excludeMatchedPattern": ***boolean***,
                  "pattern": "***string***",
                  "type": "***string***"
               }
            ]
         ],
         "payloadUrl": "***string***",
         "url": "***string***"
      }
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[project](#API_GetPublicProject_ResponseSyntax "#API_GetPublicProject_ResponseSyntax")**

Type: [PublicProject](API_PublicProject.md "API_PublicProject.md") object

## Errors

For information about the errors that are common to all actions, see [Common Errors](../APIReference/CommonErrors.md "../APIReference/CommonErrors.md").

**InvalidInputException**

HTTP Status Code: 400

**ResourceNotFoundException**

HTTP Status Code: 400
