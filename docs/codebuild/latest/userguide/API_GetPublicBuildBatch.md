# GetPublicBuildBatch

###### Note

This API element is not contained in the AWS CLI or AWS SDKs.

## Request Syntax

```
{
   "publicBuildBatchAlias": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](../APIReference/CommonParameters.md "../APIReference/CommonParameters.md").

The request accepts the following data in JSON format.

###### Note

In the following list, the required parameters are described first.

**[publicBuildBatchAlias](#API_GetPublicBuildBatch_RequestSyntax "#API_GetPublicBuildBatch_RequestSyntax")**

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `^[0-9a-zA-Z%+=]+:[a-z0-9]{8}(-[a-z0-9]{4}){3}-[a-z0-9]{12}$`

Required: Yes

## Response Syntax

```
{
   "publicBuildBatch": {
      "artifacts": {
         "artifactIdentifier": "***string***",
         "packaging": "***string***",
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
      "buildBatchNumber": ***number***,
      "buildBatchStatus": "***string***",
      "buildGroups": [
         {
            "currentBuildSummary": {
               "buildStatus": "***string***",
               "primaryArtifact": {
                  "identifier": "***string***",
                  "location": "***string***",
                  "type": "***string***"
               },
               "publicBuildAlias": "***string***",
               "requestedOn": ***number***,
               "secondaryArtifacts": [
                  {
                     "identifier": "***string***",
                     "location": "***string***",
                     "type": "***string***"
                  }
               ]
            },
            "dependsOn": [ "***string***" ],
            "identifier": "***string***",
            "ignoreFailure": ***boolean***,
            "priorBuildSummaryList": [
               {
                  "buildStatus": "***string***",
                  "primaryArtifact": {
                     "identifier": "***string***",
                     "location": "***string***",
                     "type": "***string***"
                  },
                  "publicBuildAlias": "***string***",
                  "requestedOn": ***number***,
                  "secondaryArtifacts": [
                     {
                        "identifier": "***string***",
                        "location": "***string***",
                        "type": "***string***"
                     }
                  ]
               }
            ]
         }
      ],
      "buildTimeoutInMinutes": ***number***,
      "complete": ***boolean***,
      "currentPhase": "***string***",
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
      "publicBuildBatchAlias": "***string***",
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
      "startTime": ***number***
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[publicBuildBatch](#API_GetPublicBuildBatch_ResponseSyntax "#API_GetPublicBuildBatch_ResponseSyntax")**

Type: [PublicBuildBatch](API_PublicBuildBatch.md "API_PublicBuildBatch.md") object

## Errors

For information about the errors that are common to all actions, see [Common Errors](../APIReference/CommonErrors.md "../APIReference/CommonErrors.md").

**InvalidInputException**

HTTP Status Code: 400

**ResourceNotFoundException**

HTTP Status Code: 400
