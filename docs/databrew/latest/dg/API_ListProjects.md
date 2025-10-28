# ListProjects

Lists all of the DataBrew projects that are defined.

## Request Syntax

```
GET /projects?maxResults=`MaxResults`&nextToken=`NextToken` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[MaxResults](#API_ListProjects_RequestSyntax "#API_ListProjects_RequestSyntax")**

The maximum number of results to return in this request.

Valid Range: Minimum value of 1. Maximum value of 100.

**[NextToken](#API_ListProjects_RequestSyntax "#API_ListProjects_RequestSyntax")**

The token returned by a previous call to retrieve the next set of results.

Length Constraints: Minimum length of 1. Maximum length of 2000.

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "***string***",
   "Projects": [
      {
         "AccountId": "***string***",
         "CreateDate": ***number***,
         "CreatedBy": "***string***",
         "DatasetName": "***string***",
         "LastModifiedBy": "***string***",
         "LastModifiedDate": ***number***,
         "Name": "***string***",
         "OpenDate": ***number***,
         "OpenedBy": "***string***",
         "RecipeName": "***string***",
         "ResourceArn": "***string***",
         "RoleArn": "***string***",
         "Sample": {
            "Size": ***number***,
            "Type": "***string***"
         },
         "Tags": {
            "***string***" : "***string***"
         }
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Projects](#API_ListProjects_ResponseSyntax "#API_ListProjects_ResponseSyntax")**

A list of projects that are defined .

Type: Array of [Project](API_Project.md "API_Project.md") objects

**[NextToken](#API_ListProjects_ResponseSyntax "#API_ListProjects_ResponseSyntax")**

A token that you can use in a subsequent call to retrieve the next set of
results.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2000.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**ValidationException**

The input parameters for this request failed validation.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/databrew-2017-07-25/ListProjects.md "../../../goto/cli2/databrew-2017-07-25/ListProjects.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/databrew-2017-07-25/ListProjects.md "../../../goto/DotNetSDKV3/databrew-2017-07-25/ListProjects.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/ListProjects.md "../../../goto/SdkForCpp/databrew-2017-07-25/ListProjects.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/databrew-2017-07-25/ListProjects.md "../../../goto/SdkForGoV2/databrew-2017-07-25/ListProjects.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/ListProjects.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/ListProjects.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/ListProjects.md "../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/ListProjects.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/databrew-2017-07-25/ListProjects.md "../../../goto/SdkForKotlin/databrew-2017-07-25/ListProjects.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/databrew-2017-07-25/ListProjects.md "../../../goto/SdkForPHPV3/databrew-2017-07-25/ListProjects.md")
- [AWS SDK for Python](../../../goto/boto3/databrew-2017-07-25/ListProjects.md "../../../goto/boto3/databrew-2017-07-25/ListProjects.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/ListProjects.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/ListProjects.md")
