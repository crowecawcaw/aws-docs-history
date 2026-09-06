

# DescribeBuildsForPublicProject
<a name="API_DescribeBuildsForPublicProject"></a>

**Note**  
This API element is not contained in the AWS CLI or AWS SDKs.

## Request Syntax
<a name="API_DescribeBuildsForPublicProject_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "publicProjectAlias": "{{string}}",
   "sortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeBuildsForPublicProject_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](https://docs.aws.amazon.com/codebuild/latest/APIReference/CommonParameters.html).

The request accepts the following data in JSON format.

**Note**  
In the following list, the required parameters are described first.

 ** [publicProjectAlias](#API_DescribeBuildsForPublicProject_RequestSyntax) **   <a name="CodeBuild-DescribeBuildsForPublicProject-request-publicProjectAlias"></a>
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^[0-9a-zA-Z%+=]+$`   
Required: Yes

 ** [maxResults](#API_DescribeBuildsForPublicProject_RequestSyntax) **   <a name="CodeBuild-DescribeBuildsForPublicProject-request-maxResults"></a>
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [nextToken](#API_DescribeBuildsForPublicProject_RequestSyntax) **   <a name="CodeBuild-DescribeBuildsForPublicProject-request-nextToken"></a>
Type: String  
Required: No

 ** [sortOrder](#API_DescribeBuildsForPublicProject_RequestSyntax) **   <a name="CodeBuild-DescribeBuildsForPublicProject-request-sortOrder"></a>
Type: String  
Valid Values:` ASCENDING | DESCENDING`   
Required: No

## Response Syntax
<a name="API_DescribeBuildsForPublicProject_ResponseSyntax"></a>

```
{
   "builds": [ 
      { 
         "artifacts": { 
            "artifactIdentifier": "string",
            "packaging": "string",
            "type": "string"
         },
         "buildComplete": boolean,
         "buildNumber": number,
         "buildStatus": "string",
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
               "[contexts](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BuildPhase.html)": [ 
                  { 
                     "[message](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_PhaseContext.html)": "string",
                     "[statusCode](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_PhaseContext.html)": "string"
                  }
               ],
               "[durationInSeconds](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BuildPhase.html)": number,
               "[endTime](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BuildPhase.html)": number,
               "[phaseStatus](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BuildPhase.html)": "string",
               "[phaseType](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BuildPhase.html)": "string",
               "[startTime](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BuildPhase.html)": number
            }
         ],
         "projectName": "string",
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
         "startTime": number,
         "timeoutInMinutes": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeBuildsForPublicProject_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [builds](#API_DescribeBuildsForPublicProject_ResponseSyntax) **   <a name="CodeBuild-DescribeBuildsForPublicProject-response-builds"></a>
Type: Array of [PublicBuild](API_PublicBuild.md) objects

 ** [nextToken](#API_DescribeBuildsForPublicProject_ResponseSyntax) **   <a name="CodeBuild-DescribeBuildsForPublicProject-response-nextToken"></a>
Type: String

## Errors
<a name="API_DescribeBuildsForPublicProject_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](https://docs.aws.amazon.com/codebuild/latest/APIReference/CommonErrors.html).

 **InvalidInputException**   
HTTP Status Code: 400

 **ResourceNotFoundException**   
HTTP Status Code: 400