

# GetPresignedUrlsForPublicBuild
<a name="API_GetPresignedUrlsForPublicBuild"></a>

**Note**  
This API element is not contained in the AWS CLI or AWS SDKs.

## Request Syntax
<a name="API_GetPresignedUrlsForPublicBuild_RequestSyntax"></a>

```
{
   "publicBuildAlias": "{{string}}"
}
```

## Request Parameters
<a name="API_GetPresignedUrlsForPublicBuild_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](https://docs.aws.amazon.com/codebuild/latest/APIReference/CommonParameters.html).

The request accepts the following data in JSON format.

**Note**  
In the following list, the required parameters are described first.

 ** [publicBuildAlias](#API_GetPresignedUrlsForPublicBuild_RequestSyntax) **   <a name="CodeBuild-GetPresignedUrlsForPublicBuild-request-publicBuildAlias"></a>
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^[0-9a-zA-Z%+=]+:\p{XDigit}{8}(-\p{XDigit}{4}){3}-\p{XDigit}{12}$`   
Required: Yes

## Response Syntax
<a name="API_GetPresignedUrlsForPublicBuild_ResponseSyntax"></a>

```
{
   "artifacts": { 
      "expiredAt": number,
      "identifier": "string",
      "md5Checksum": "string",
      "presignedUrl": "string",
      "s3Arn": "string",
      "sha256Checksum": "string"
   },
   "log": { 
      "expiredAt": number,
      "identifier": "string",
      "md5Checksum": "string",
      "presignedUrl": "string",
      "s3Arn": "string",
      "sha256Checksum": "string"
   },
   "secondaryArtifacts": [ 
      { 
         "expiredAt": number,
         "identifier": "string",
         "md5Checksum": "string",
         "presignedUrl": "string",
         "s3Arn": "string",
         "sha256Checksum": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetPresignedUrlsForPublicBuild_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [artifacts](#API_GetPresignedUrlsForPublicBuild_ResponseSyntax) **   <a name="CodeBuild-GetPresignedUrlsForPublicBuild-response-artifacts"></a>
Type: [S3Downloadable](API_S3Downloadable.md) object

 ** [log](#API_GetPresignedUrlsForPublicBuild_ResponseSyntax) **   <a name="CodeBuild-GetPresignedUrlsForPublicBuild-response-log"></a>
Type: [S3Downloadable](API_S3Downloadable.md) object

 ** [secondaryArtifacts](#API_GetPresignedUrlsForPublicBuild_ResponseSyntax) **   <a name="CodeBuild-GetPresignedUrlsForPublicBuild-response-secondaryArtifacts"></a>
Type: Array of [S3Downloadable](API_S3Downloadable.md) objects

## Errors
<a name="API_GetPresignedUrlsForPublicBuild_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](https://docs.aws.amazon.com/codebuild/latest/APIReference/CommonErrors.html).

 **InvalidInputException**   
HTTP Status Code: 400

 **ResourceNotFoundException**   
HTTP Status Code: 400