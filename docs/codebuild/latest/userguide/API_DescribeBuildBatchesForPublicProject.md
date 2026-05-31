# DescribeBuildBatchesForPublicProject

###### Note

This API element is not contained in the AWS CLI or AWS SDKs.

## Request Syntax

```
{
   "filter": {
      "status": "`string`"
   },
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

**[publicProjectAlias](#API_DescribeBuildBatchesForPublicProject_RequestSyntax "#API_DescribeBuildBatchesForPublicProject_RequestSyntax")**

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `^[0-9a-zA-Z%+=]+$`

Required: Yes

**[filter](#API_DescribeBuildBatchesForPublicProject_RequestSyntax "#API_DescribeBuildBatchesForPublicProject_RequestSyntax")**

Specifies filters when retrieving batch builds.

Type: [BuildBatchFilter](../APIReference/API_BuildBatchFilter.md "../APIReference/API_BuildBatchFilter.md") object

Required: No

**[maxResults](#API_DescribeBuildBatchesForPublicProject_RequestSyntax "#API_DescribeBuildBatchesForPublicProject_RequestSyntax")**

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 100.

Required: No

**[nextToken](#API_DescribeBuildBatchesForPublicProject_RequestSyntax "#API_DescribeBuildBatchesForPublicProject_RequestSyntax")**

Type: String

Required: No

**[sortOrder](#API_DescribeBuildBatchesForPublicProject_RequestSyntax "#API_DescribeBuildBatchesForPublicProject_RequestSyntax")**

Type: String

Valid Values: `ASCENDING | DESCENDING`

Required: No

## Response Syntax

```
{
   "nextToken": "***string***",
   "publicBuildBatches": [
      {
         "buildBatchNumber": ***number***,
         "buildBatchStatus": "***string***",
         "endTime": ***number***,
         "publicBuildBatchAlias": "***string***",
         "sourceVersion": "***string***",
         "startTime": ***number***
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[nextToken](#API_DescribeBuildBatchesForPublicProject_ResponseSyntax "#API_DescribeBuildBatchesForPublicProject_ResponseSyntax")**

Type: String

**[publicBuildBatches](#API_DescribeBuildBatchesForPublicProject_ResponseSyntax "#API_DescribeBuildBatchesForPublicProject_ResponseSyntax")**

Type: Array of [BuildBatchForDescribeBuildBatchesPublic](API_BuildBatchForDescribeBuildBatchesPublic.md "API_BuildBatchForDescribeBuildBatchesPublic.md") objects

## Errors

For information about the errors that are common to all actions, see [Common Errors](../APIReference/CommonErrors.md "../APIReference/CommonErrors.md").

**InvalidInputException**

HTTP Status Code: 400

**ResourceNotFoundException**

HTTP Status Code: 400
