

# GetPublicBuildBatch
<a name="API_GetPublicBuildBatch"></a>

**Note**  
This API element is not contained in the AWS CLI or AWS SDKs.

## Request Syntax
<a name="API_GetPublicBuildBatch_RequestSyntax"></a>

```
{
   "publicBuildBatchAlias": "{{string}}"
}
```

## Request Parameters
<a name="API_GetPublicBuildBatch_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](https://docs.aws.amazon.com/codebuild/latest/APIReference/CommonParameters.html).

The request accepts the following data in JSON format.

**Note**  
In the following list, the required parameters are described first.

 ** [publicBuildBatchAlias](#API_GetPublicBuildBatch_RequestSyntax) **   <a name="CodeBuild-GetPublicBuildBatch-request-publicBuildBatchAlias"></a>
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^[0-9a-zA-Z%+=]+:[a-z0-9]{8}(-[a-z0-9]{4}){3}-[a-z0-9]{12}$`   
Required: Yes

## Response Syntax
<a name="API_GetPublicBuildBatch_ResponseSyntax"></a>

```
{
   "publicBuildBatch": { 
      "artifacts": { 
         "artifactIdentifier": "string",
         "packaging": "string",
         "type": "string"
      },
      "buildBatchConfig": { 
         "combineArtifacts": boolean,
         "restrictions": { 
            "[computeTypesAllowed](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BatchRestrictions.html)": [ "string" ],
            "[maximumBuildsAllowed](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BatchRestrictions.html)": number
         },
         "timeoutInMins": number
      },
      "buildBatchNumber": number,
      "buildBatchStatus": "string",
      "buildGroups": [ 
         { 
            "currentBuildSummary": { 
               "buildStatus": "string",
               "primaryArtifact": { 
                  "[identifier](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ResolvedArtifact.html)": "string",
                  "[location](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ResolvedArtifact.html)": "string",
                  "[type](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ResolvedArtifact.html)": "string"
               },
               "publicBuildAlias": "string",
               "requestedOn": number,
               "secondaryArtifacts": [ 
                  { 
                     "[identifier](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ResolvedArtifact.html)": "string",
                     "[location](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ResolvedArtifact.html)": "string",
                     "[type](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ResolvedArtifact.html)": "string"
                  }
               ]
            },
            "dependsOn": [ "string" ],
            "identifier": "string",
            "ignoreFailure": boolean,
            "priorBuildSummaryList": [ 
               { 
                  "buildStatus": "string",
                  "primaryArtifact": { 
                     "[identifier](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ResolvedArtifact.html)": "string",
                     "[location](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ResolvedArtifact.html)": "string",
                     "[type](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ResolvedArtifact.html)": "string"
                  },
                  "publicBuildAlias": "string",
                  "requestedOn": number,
                  "secondaryArtifacts": [ 
                     { 
                        "[identifier](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ResolvedArtifact.html)": "string",
                        "[location](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ResolvedArtifact.html)": "string",
                        "[type](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ResolvedArtifact.html)": "string"
                     }
                  ]
               }
            ]
         }
      ],
      "buildTimeoutInMinutes": number,
      "complete": boolean,
      "currentPhase": "string",
      "endTime": number,
      "environment": { 
         "computeType": "string",
         "environmentVariables": [ 
            { 
               "[name](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_EnvironmentVariable.html)": "string",
               "[type](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_EnvironmentVariable.html)": "string",
               "[value](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_EnvironmentVariable.html)": "string"
            }
         ],
         "image": "string",
         "type": "string"
      },
      "id": "string",
      "initiator": "string",
      "logsStatus": { 
         "cloudWatchLogsStatus": "string",
         "s3LogsStatus": "string"
      },
      "phases": [ 
         { 
            "[contexts](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BuildBatchPhase.html)": [ 
               { 
                  "[message](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_PhaseContext.html)": "string",
                  "[statusCode](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_PhaseContext.html)": "string"
               }
            ],
            "[durationInSeconds](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BuildBatchPhase.html)": number,
            "[endTime](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BuildBatchPhase.html)": number,
            "[phaseStatus](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BuildBatchPhase.html)": "string",
            "[phaseType](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BuildBatchPhase.html)": "string",
            "[startTime](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BuildBatchPhase.html)": number
         }
      ],
      "projectName": "string",
      "publicBuildBatchAlias": "string",
      "queuedTimeoutInMinutes": number,
      "resolvedSourceVersion": "string",
      "secondaryArtifacts": [ 
         { 
            "artifactIdentifier": "string",
            "packaging": "string",
            "type": "string"
         }
      ],
      "secondarySources": [ 
         { 
            "buildspec": "string",
            "gitCloneDepth": number,
            "gitSubmodulesConfig": { 
               "[fetchSubmodules](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_GitSubmodulesConfig.html)": boolean
            },
            "location": "string",
            "sourceIdentifier": "string",
            "type": "string"
         }
      ],
      "secondarySourceVersions": [ 
         { 
            "[sourceIdentifier](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ProjectSourceVersion.html)": "string",
            "[sourceVersion](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ProjectSourceVersion.html)": "string"
         }
      ],
      "source": { 
         "buildspec": "string",
         "gitCloneDepth": number,
         "gitSubmodulesConfig": { 
            "[fetchSubmodules](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_GitSubmodulesConfig.html)": boolean
         },
         "location": "string",
         "sourceIdentifier": "string",
         "type": "string"
      },
      "sourceVersion": "string",
      "startTime": number
   }
}
```

## Response Elements
<a name="API_GetPublicBuildBatch_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [publicBuildBatch](#API_GetPublicBuildBatch_ResponseSyntax) **   <a name="CodeBuild-GetPublicBuildBatch-response-publicBuildBatch"></a>
Type: [PublicBuildBatch](API_PublicBuildBatch.md) object

## Errors
<a name="API_GetPublicBuildBatch_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](https://docs.aws.amazon.com/codebuild/latest/APIReference/CommonErrors.html).

 **InvalidInputException**   
HTTP Status Code: 400

 **ResourceNotFoundException**   
HTTP Status Code: 400