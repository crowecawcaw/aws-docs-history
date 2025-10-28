# DescribeDataset

Returns the definition of a specific DataBrew dataset.

## Request Syntax

```
GET /datasets/`name` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[name](#API_DescribeDataset_RequestSyntax "#API_DescribeDataset_RequestSyntax")**

The name of the dataset to be described.

Length Constraints: Minimum length of 1. Maximum length of 255.

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
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
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Input](#API_DescribeDataset_ResponseSyntax "#API_DescribeDataset_ResponseSyntax")**

Represents information on how DataBrew can find data, in either the AWS Glue Data Catalog or
Amazon S3.

Type: [Input](API_Input.md "API_Input.md") object

**[Name](#API_DescribeDataset_ResponseSyntax "#API_DescribeDataset_ResponseSyntax")**

The name of the dataset.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

**[CreateDate](#API_DescribeDataset_ResponseSyntax "#API_DescribeDataset_ResponseSyntax")**

The date and time that the dataset was created.

Type: Timestamp

**[CreatedBy](#API_DescribeDataset_ResponseSyntax "#API_DescribeDataset_ResponseSyntax")**

The identifier (user name) of the user who created the dataset.

Type: String

**[Format](#API_DescribeDataset_ResponseSyntax "#API_DescribeDataset_ResponseSyntax")**

The file format of a dataset that is created from an Amazon S3 file
or folder.

Type: String

Valid Values: `CSV | JSON | PARQUET | EXCEL | ORC`

**[FormatOptions](#API_DescribeDataset_ResponseSyntax "#API_DescribeDataset_ResponseSyntax")**

Represents a set of options that define the structure of either comma-separated value (CSV),
Excel, or JSON input.

Type: [FormatOptions](API_FormatOptions.md "API_FormatOptions.md") object

**[LastModifiedBy](#API_DescribeDataset_ResponseSyntax "#API_DescribeDataset_ResponseSyntax")**

The identifier (user name) of the user who last modified the dataset.

Type: String

**[LastModifiedDate](#API_DescribeDataset_ResponseSyntax "#API_DescribeDataset_ResponseSyntax")**

The date and time that the dataset was last modified.

Type: Timestamp

**[PathOptions](#API_DescribeDataset_ResponseSyntax "#API_DescribeDataset_ResponseSyntax")**

A set of options that defines how DataBrew interprets an Amazon S3
path of the dataset.

Type: [PathOptions](API_PathOptions.md "API_PathOptions.md") object

**[ResourceArn](#API_DescribeDataset_ResponseSyntax "#API_DescribeDataset_ResponseSyntax")**

The Amazon Resource Name (ARN) of the dataset.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

**[Source](#API_DescribeDataset_ResponseSyntax "#API_DescribeDataset_ResponseSyntax")**

The location of the data for this dataset, Amazon S3 or the
AWS Glue Data Catalog.

Type: String

Valid Values: `S3 | DATA-CATALOG | DATABASE`

**[Tags](#API_DescribeDataset_ResponseSyntax "#API_DescribeDataset_ResponseSyntax")**

Metadata tags associated with this dataset.

Type: String to string map

Map Entries: Maximum number of 200 items.

Key Length Constraints: Minimum length of 1. Maximum length of 128.

Value Length Constraints: Maximum length of 256.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**ResourceNotFoundException**

One or more resources can't be found.

HTTP Status Code: 404

**ValidationException**

The input parameters for this request failed validation.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/databrew-2017-07-25/DescribeDataset.md "../../../goto/cli2/databrew-2017-07-25/DescribeDataset.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/databrew-2017-07-25/DescribeDataset.md "../../../goto/DotNetSDKV3/databrew-2017-07-25/DescribeDataset.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/DescribeDataset.md "../../../goto/SdkForCpp/databrew-2017-07-25/DescribeDataset.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/databrew-2017-07-25/DescribeDataset.md "../../../goto/SdkForGoV2/databrew-2017-07-25/DescribeDataset.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/DescribeDataset.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/DescribeDataset.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/DescribeDataset.md "../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/DescribeDataset.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/databrew-2017-07-25/DescribeDataset.md "../../../goto/SdkForKotlin/databrew-2017-07-25/DescribeDataset.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/databrew-2017-07-25/DescribeDataset.md "../../../goto/SdkForPHPV3/databrew-2017-07-25/DescribeDataset.md")
- [AWS SDK for Python](../../../goto/boto3/databrew-2017-07-25/DescribeDataset.md "../../../goto/boto3/databrew-2017-07-25/DescribeDataset.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/DescribeDataset.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/DescribeDataset.md")
