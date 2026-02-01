# ListDatasets

Lists all of the DataBrew datasets.

## Request Syntax

```
GET /datasets?maxResults=`MaxResults`&nextToken=`NextToken` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[MaxResults](#API_ListDatasets_RequestSyntax "#API_ListDatasets_RequestSyntax")**

The maximum number of results to return in this request.

Valid Range: Minimum value of 1. Maximum value of 100.

**[NextToken](#API_ListDatasets_RequestSyntax "#API_ListDatasets_RequestSyntax")**

The token returned by a previous call to retrieve the next set of results.

Length Constraints: Minimum length of 1. Maximum length of 2000.

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "Datasets": [
      {
         "AccountId": "***string***",
         "CreateDate": ***number***,
         "CreatedBy": "***string***",
         "Format": "***string***",
         "FormatOptions": {
            "Csv": {
               "Delimiter": "***string***",
               "HeaderRow": ***boolean***
            },
            "Excel": {
               "HeaderRow": ***boolean***,
               "SheetIndexes": [ ***number*** ],
               "SheetNames": [ "***string***" ]
            },
            "Json": {
               "MultiLine": ***boolean***
            }
         },
         "Input": {
            "DatabaseInputDefinition": {
               "DatabaseTableName": "***string***",
               "GlueConnectionName": "***string***",
               "QueryString": "***string***",
               "TempDirectory": {
                  "Bucket": "***string***",
                  "BucketOwner": "***string***",
                  "Key": "***string***"
               }
            },
            "DataCatalogInputDefinition": {
               "CatalogId": "***string***",
               "DatabaseName": "***string***",
               "TableName": "***string***",
               "TempDirectory": {
                  "Bucket": "***string***",
                  "BucketOwner": "***string***",
                  "Key": "***string***"
               }
            },
            "Metadata": {
               "SourceArn": "***string***"
            },
            "S3InputDefinition": {
               "Bucket": "***string***",
               "BucketOwner": "***string***",
               "Key": "***string***"
            }
         },
         "LastModifiedBy": "***string***",
         "LastModifiedDate": ***number***,
         "Name": "***string***",
         "PathOptions": {
            "FilesLimit": {
               "MaxFiles": ***number***,
               "Order": "***string***",
               "OrderedBy": "***string***"
            },
            "LastModifiedDateCondition": {
               "Expression": "***string***",
               "ValuesMap": {
                  "***string***" : "***string***"
               }
            },
            "Parameters": {
               "***string***" : {
                  "CreateColumn": ***boolean***,
                  "DatetimeOptions": {
                     "Format": "***string***",
                     "LocaleCode": "***string***",
                     "TimezoneOffset": "***string***"
                  },
                  "Filter": {
                     "Expression": "***string***",
                     "ValuesMap": {
                        "***string***" : "***string***"
                     }
                  },
                  "Name": "***string***",
                  "Type": "***string***"
               }
            }
         },
         "ResourceArn": "***string***",
         "Source": "***string***",
         "Tags": {
            "***string***" : "***string***"
         }
      }
   ],
   "NextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Datasets](#API_ListDatasets_ResponseSyntax "#API_ListDatasets_ResponseSyntax")**

A list of datasets that are defined.

Type: Array of [Dataset](API_Dataset.md "API_Dataset.md") objects

**[NextToken](#API_ListDatasets_ResponseSyntax "#API_ListDatasets_ResponseSyntax")**

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

- [AWS Command Line Interface V2](../../../goto/cli2/databrew-2017-07-25/ListDatasets.md "../../../goto/cli2/databrew-2017-07-25/ListDatasets.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/databrew-2017-07-25/ListDatasets.md "../../../goto/DotNetSDKV4/databrew-2017-07-25/ListDatasets.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/ListDatasets.md "../../../goto/SdkForCpp/databrew-2017-07-25/ListDatasets.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/databrew-2017-07-25/ListDatasets.md "../../../goto/SdkForGoV2/databrew-2017-07-25/ListDatasets.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/ListDatasets.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/ListDatasets.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/ListDatasets.md "../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/ListDatasets.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/databrew-2017-07-25/ListDatasets.md "../../../goto/SdkForKotlin/databrew-2017-07-25/ListDatasets.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/databrew-2017-07-25/ListDatasets.md "../../../goto/SdkForPHPV3/databrew-2017-07-25/ListDatasets.md")
- [AWS SDK for Python](../../../goto/boto3/databrew-2017-07-25/ListDatasets.md "../../../goto/boto3/databrew-2017-07-25/ListDatasets.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/ListDatasets.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/ListDatasets.md")
