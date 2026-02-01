# UpdateDataset

Modifies the definition of an existing DataBrew dataset.

## Request Syntax

```
PUT /datasets/`name` HTTP/1.1
Content-type: application/json

{
   "Format": "`string`",
   "FormatOptions": {
      "Csv": {
         "Delimiter": "`string`",
         "HeaderRow": `boolean`
      },
      "Excel": {
         "HeaderRow": `boolean`,
         "SheetIndexes": [ `number` ],
         "SheetNames": [ "`string`" ]
      },
      "Json": {
         "MultiLine": `boolean`
      }
   },
   "Input": {
      "DatabaseInputDefinition": {
         "DatabaseTableName": "`string`",
         "GlueConnectionName": "`string`",
         "QueryString": "`string`",
         "TempDirectory": {
            "Bucket": "`string`",
            "BucketOwner": "`string`",
            "Key": "`string`"
         }
      },
      "DataCatalogInputDefinition": {
         "CatalogId": "`string`",
         "DatabaseName": "`string`",
         "TableName": "`string`",
         "TempDirectory": {
            "Bucket": "`string`",
            "BucketOwner": "`string`",
            "Key": "`string`"
         }
      },
      "Metadata": {
         "SourceArn": "`string`"
      },
      "S3InputDefinition": {
         "Bucket": "`string`",
         "BucketOwner": "`string`",
         "Key": "`string`"
      }
   },
   "PathOptions": {
      "FilesLimit": {
         "MaxFiles": `number`,
         "Order": "`string`",
         "OrderedBy": "`string`"
      },
      "LastModifiedDateCondition": {
         "Expression": "`string`",
         "ValuesMap": {
            "`string`" : "`string`"
         }
      },
      "Parameters": {
         "`string`" : {
            "CreateColumn": `boolean`,
            "DatetimeOptions": {
               "Format": "`string`",
               "LocaleCode": "`string`",
               "TimezoneOffset": "`string`"
            },
            "Filter": {
               "Expression": "`string`",
               "ValuesMap": {
                  "`string`" : "`string`"
               }
            },
            "Name": "`string`",
            "Type": "`string`"
         }
      }
   }
}
```

## URI Request Parameters

The request uses the following URI parameters.

**[name](#API_UpdateDataset_RequestSyntax "#API_UpdateDataset_RequestSyntax")**

The name of the dataset to be updated.

Length Constraints: Minimum length of 1. Maximum length of 255.

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**[Input](#API_UpdateDataset_RequestSyntax "#API_UpdateDataset_RequestSyntax")**

Represents information on how DataBrew can find data, in either the AWS Glue Data Catalog or
Amazon S3.

Type: [Input](API_Input.md "API_Input.md") object

Required: Yes

**[Format](#API_UpdateDataset_RequestSyntax "#API_UpdateDataset_RequestSyntax")**

The file format of a dataset that is created from an Amazon S3 file or folder.

Type: String

Valid Values: `CSV | JSON | PARQUET | EXCEL | ORC`

Required: No

**[FormatOptions](#API_UpdateDataset_RequestSyntax "#API_UpdateDataset_RequestSyntax")**

Represents a set of options that define the structure of either comma-separated value (CSV),
Excel, or JSON input.

Type: [FormatOptions](API_FormatOptions.md "API_FormatOptions.md") object

Required: No

**[PathOptions](#API_UpdateDataset_RequestSyntax "#API_UpdateDataset_RequestSyntax")**

A set of options that defines how DataBrew interprets an Amazon S3 path of the dataset.

Type: [PathOptions](API_PathOptions.md "API_PathOptions.md") object

Required: No

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "Name": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Name](#API_UpdateDataset_ResponseSyntax "#API_UpdateDataset_ResponseSyntax")**

The name of the dataset that you updated.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**AccessDeniedException**

Access to the specified resource was denied.

HTTP Status Code: 403

**ResourceNotFoundException**

One or more resources can't be found.

HTTP Status Code: 404

**ValidationException**

The input parameters for this request failed validation.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/databrew-2017-07-25/UpdateDataset.md "../../../goto/cli2/databrew-2017-07-25/UpdateDataset.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/databrew-2017-07-25/UpdateDataset.md "../../../goto/DotNetSDKV4/databrew-2017-07-25/UpdateDataset.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/UpdateDataset.md "../../../goto/SdkForCpp/databrew-2017-07-25/UpdateDataset.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/databrew-2017-07-25/UpdateDataset.md "../../../goto/SdkForGoV2/databrew-2017-07-25/UpdateDataset.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/UpdateDataset.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/UpdateDataset.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/UpdateDataset.md "../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/UpdateDataset.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/databrew-2017-07-25/UpdateDataset.md "../../../goto/SdkForKotlin/databrew-2017-07-25/UpdateDataset.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/databrew-2017-07-25/UpdateDataset.md "../../../goto/SdkForPHPV3/databrew-2017-07-25/UpdateDataset.md")
- [AWS SDK for Python](../../../goto/boto3/databrew-2017-07-25/UpdateDataset.md "../../../goto/boto3/databrew-2017-07-25/UpdateDataset.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/UpdateDataset.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/UpdateDataset.md")
