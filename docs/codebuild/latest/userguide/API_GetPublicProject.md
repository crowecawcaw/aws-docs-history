

# GetPublicProject
<a name="API_GetPublicProject"></a>

**Note**  
This API element is not contained in the AWS CLI or AWS SDKs.

## Request Syntax
<a name="API_GetPublicProject_RequestSyntax"></a>

```
{
   "publicProjectAlias": "{{string}}"
}
```

## Request Parameters
<a name="API_GetPublicProject_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](https://docs.aws.amazon.com/codebuild/latest/APIReference/CommonParameters.html).

The request accepts the following data in JSON format.

**Note**  
In the following list, the required parameters are described first.

 ** [publicProjectAlias](#API_GetPublicProject_RequestSyntax) **   <a name="CodeBuild-GetPublicProject-request-publicProjectAlias"></a>
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^[0-9a-zA-Z%+=]+$`   
Required: Yes

## Response Syntax
<a name="API_GetPublicProject_ResponseSyntax"></a>

```
{
   "project": { 
      "artifacts": { 
         "artifactIdentifier": "string",
         "location": "string",
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
      "concurrentBuildLimit": number,
      "description": "string",
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
      "name": "string",
      "queuedTimeoutInMinutes": number,
      "secondaryArtifacts": [ 
         { 
            "artifactIdentifier": "string",
            "location": "string",
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
      "timeoutInMinutes": number,
      "webhook": { 
         "branchFilter": "string",
         "buildType": "string",
         "filterGroups": [ 
            [ 
               { 
                  "[excludeMatchedPattern](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_WebhookFilter.html)": boolean,
                  "[pattern](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_WebhookFilter.html)": "string",
                  "[type](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_WebhookFilter.html)": "string"
               }
            ]
         ],
         "payloadUrl": "string",
         "url": "string"
      }
   }
}
```

## Response Elements
<a name="API_GetPublicProject_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [project](#API_GetPublicProject_ResponseSyntax) **   <a name="CodeBuild-GetPublicProject-response-project"></a>
Type: [PublicProject](API_PublicProject.md) object

## Errors
<a name="API_GetPublicProject_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](https://docs.aws.amazon.com/codebuild/latest/APIReference/CommonErrors.html).

 **InvalidInputException**   
HTTP Status Code: 400

 **ResourceNotFoundException**   
HTTP Status Code: 400