# CreateDataset

Creates an empty dataset and adds it to the specified dataset group.
Use [CreateDatasetImportJob](API_CreateDatasetImportJob.md "API_CreateDatasetImportJob.md") to import your training data to a
dataset.

There are 5 types of datasets:

- Item interactions
- Items
- Users
- Action interactions
- Actions
  Each dataset type has an associated schema with required field types.
  Only the `Item interactions` dataset is required in order to train a
  model (also referred to as creating a solution).

A dataset can be in one of the following states:

- CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE
  FAILED
- DELETE PENDING > DELETE IN_PROGRESS
  To get the status of the dataset, call [DescribeDataset](API_DescribeDataset.md "API_DescribeDataset.md").

###### Related APIs

- [CreateDatasetGroup](API_CreateDatasetGroup.md "API_CreateDatasetGroup.md")
- [ListDatasets](API_ListDatasets.md "API_ListDatasets.md")
- [DescribeDataset](API_DescribeDataset.md "API_DescribeDataset.md")
- [DeleteDataset](API_DeleteDataset.md "API_DeleteDataset.md")

## Request Syntax

```
{
   "datasetGroupArn": "`string`",
   "datasetType": "`string`",
   "name": "`string`",
   "schemaArn": "`string`",
   "tags": [
      {
         "tagKey": "`string`",
         "tagValue": "`string`"
      }
   ]
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[datasetGroupArn](#API_CreateDataset_RequestSyntax "#API_CreateDataset_RequestSyntax")**

The Amazon Resource Name (ARN) of the dataset group to add the dataset
to.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: Yes

**[datasetType](#API_CreateDataset_RequestSyntax "#API_CreateDataset_RequestSyntax")**

The type of dataset.

One of the following (case insensitive) values:

- Interactions
- Items
- Users
- Actions
- Action_Interactions

Type: String

Length Constraints: Maximum length of 256.

Required: Yes

**[name](#API_CreateDataset_RequestSyntax "#API_CreateDataset_RequestSyntax")**

The name for the dataset.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`

Required: Yes

**[schemaArn](#API_CreateDataset_RequestSyntax "#API_CreateDataset_RequestSyntax")**

The ARN of the schema to associate with the dataset. The schema
defines the dataset fields.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: Yes

**[tags](#API_CreateDataset_RequestSyntax "#API_CreateDataset_RequestSyntax")**

A list of [tags](tagging-resources.md "tagging-resources.md") to apply to the dataset.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Array Members: Minimum number of 0 items. Maximum number of 200 items.

Required: No

## Response Syntax

```
{
   "datasetArn": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[datasetArn](#API_CreateDataset_ResponseSyntax "#API_CreateDataset_ResponseSyntax")**

The ARN of the dataset.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

## Errors

**InvalidInputException**

Provide a valid value for the field or parameter.

HTTP Status Code: 400

**LimitExceededException**

The limit on the number of requests per second has been exceeded.

HTTP Status Code: 400

**ResourceAlreadyExistsException**

The specified resource already exists.

HTTP Status Code: 400

**ResourceInUseException**

The specified resource is in use.

HTTP Status Code: 400

**ResourceNotFoundException**

Could not find the specified resource.

HTTP Status Code: 400

**TooManyTagsException**

You have exceeded the maximum number of tags you can apply to this resource.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/CreateDataset.md "../../../goto/cli2/personalize-2018-05-22/CreateDataset.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/personalize-2018-05-22/CreateDataset.md "../../../goto/DotNetSDKV3/personalize-2018-05-22/CreateDataset.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/CreateDataset.md "../../../goto/SdkForCpp/personalize-2018-05-22/CreateDataset.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/CreateDataset.md "../../../goto/SdkForGoV2/personalize-2018-05-22/CreateDataset.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/CreateDataset.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/CreateDataset.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/CreateDataset.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/CreateDataset.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/CreateDataset.md "../../../goto/SdkForKotlin/personalize-2018-05-22/CreateDataset.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/CreateDataset.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/CreateDataset.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/CreateDataset.md "../../../goto/boto3/personalize-2018-05-22/CreateDataset.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/CreateDataset.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/CreateDataset.md")
