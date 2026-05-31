# GetPresignedUrlsForPublicBuild

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

**[publicBuildAlias](#API_GetPresignedUrlsForPublicBuild_RequestSyntax "#API_GetPresignedUrlsForPublicBuild_RequestSyntax")**

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `^[0-9a-zA-Z%+=]+:\p{XDigit}{8}(-\p{XDigit}{4}){3}-\p{XDigit}{12}$`

Required: Yes

## Response Syntax

```
{
   "artifacts": {
      "expiredAt": ***number***,
      "identifier": "***string***",
      "md5Checksum": "***string***",
      "presignedUrl": "***string***",
      "s3Arn": "***string***",
      "sha256Checksum": "***string***"
   },
   "log": {
      "expiredAt": ***number***,
      "identifier": "***string***",
      "md5Checksum": "***string***",
      "presignedUrl": "***string***",
      "s3Arn": "***string***",
      "sha256Checksum": "***string***"
   },
   "secondaryArtifacts": [
      {
         "expiredAt": ***number***,
         "identifier": "***string***",
         "md5Checksum": "***string***",
         "presignedUrl": "***string***",
         "s3Arn": "***string***",
         "sha256Checksum": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[artifacts](#API_GetPresignedUrlsForPublicBuild_ResponseSyntax "#API_GetPresignedUrlsForPublicBuild_ResponseSyntax")**

Type: [S3Downloadable](API_S3Downloadable.md "API_S3Downloadable.md") object

**[log](#API_GetPresignedUrlsForPublicBuild_ResponseSyntax "#API_GetPresignedUrlsForPublicBuild_ResponseSyntax")**

Type: [S3Downloadable](API_S3Downloadable.md "API_S3Downloadable.md") object

**[secondaryArtifacts](#API_GetPresignedUrlsForPublicBuild_ResponseSyntax "#API_GetPresignedUrlsForPublicBuild_ResponseSyntax")**

Type: Array of [S3Downloadable](API_S3Downloadable.md "API_S3Downloadable.md") objects

## Errors

For information about the errors that are common to all actions, see [Common Errors](../APIReference/CommonErrors.md "../APIReference/CommonErrors.md").

**InvalidInputException**

HTTP Status Code: 400

**ResourceNotFoundException**

HTTP Status Code: 400
