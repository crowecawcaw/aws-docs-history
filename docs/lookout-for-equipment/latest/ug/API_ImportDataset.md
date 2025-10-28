On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# ImportDataset

Imports a dataset.

## Request Syntax

```
{
   "ClientToken": "`string`",
   "DatasetName": "`string`",
   "ServerSideKmsKeyId": "`string`",
   "SourceDatasetArn": "`string`",
   "Tags": [
      {
         "Key": "`string`",
         "Value": "`string`"
      }
   ]
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[ClientToken](#API_ImportDataset_RequestSyntax "#API_ImportDataset_RequestSyntax")**

A unique identifier for the request. If you do not set the client request token,
Amazon Lookout for Equipment generates one.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `\p{ASCII}{1,256}`

Required: Yes

**[DatasetName](#API_ImportDataset_RequestSyntax "#API_ImportDataset_RequestSyntax")**

The name of the machine learning dataset to be created. If the dataset already exists,
Amazon Lookout for Equipment overwrites the existing dataset. If you don't specify this field, it is filled
with the name of the source dataset.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `^[0-9a-zA-Z_-]{1,200}$`

Required: No

**[ServerSideKmsKeyId](#API_ImportDataset_RequestSyntax "#API_ImportDataset_RequestSyntax")**

Provides the identifier of the AWS KMS key key used to encrypt model data by Amazon Lookout for Equipment.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Pattern: `^[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,2048}$`

Required: No

**[SourceDatasetArn](#API_ImportDataset_RequestSyntax "#API_ImportDataset_RequestSyntax")**

The Amazon Resource Name (ARN) of the dataset to import.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:dataset\/[0-9a-zA-Z_-]{1,200}\/.+`

Required: Yes

**[Tags](#API_ImportDataset_RequestSyntax "#API_ImportDataset_RequestSyntax")**

Any tags associated with the dataset to be created.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Array Members: Minimum number of 0 items. Maximum number of 200 items.

Required: No

## Response Syntax

```
{
   "DatasetArn": "***string***",
   "DatasetName": "***string***",
   "JobId": "***string***",
   "Status": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[DatasetArn](#API_ImportDataset_ResponseSyntax "#API_ImportDataset_ResponseSyntax")**

The Amazon Resource Name (ARN) of the dataset that was imported.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:dataset\/[0-9a-zA-Z_-]{1,200}\/.+`

**[DatasetName](#API_ImportDataset_ResponseSyntax "#API_ImportDataset_ResponseSyntax")**

The name of the created machine learning dataset.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `^[0-9a-zA-Z_-]{1,200}$`

**[JobId](#API_ImportDataset_ResponseSyntax "#API_ImportDataset_ResponseSyntax")**

A unique identifier for the job of importing the dataset.

Type: String

Length Constraints: Maximum length of 32.

Pattern: `[A-Fa-f0-9]{0,32}`

**[Status](#API_ImportDataset_ResponseSyntax "#API_ImportDataset_ResponseSyntax")**

The status of the `ImportDataset` operation.

Type: String

Valid Values: `CREATED | INGESTION_IN_PROGRESS | ACTIVE | IMPORT_IN_PROGRESS`

## Errors

**AccessDeniedException**

The request could not be completed because you do not have access to the resource.

HTTP Status Code: 400

**ConflictException**

The request could not be completed due to a conflict with the current state of the
target resource.

HTTP Status Code: 400

**InternalServerException**

Processing of the request has failed because of an unknown error, exception or failure.

HTTP Status Code: 500

**ResourceNotFoundException**

The resource requested could not be found. Verify the resource ID and retry your
request.

HTTP Status Code: 400

**ServiceQuotaExceededException**

Resource limitations have been exceeded.

HTTP Status Code: 400

**ThrottlingException**

The request was denied due to request throttling.

HTTP Status Code: 400

**ValidationException**

The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related AWS
service that's being utilized.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/lookoutequipment-2020-12-15/ImportDataset.md "../../../goto/cli2/lookoutequipment-2020-12-15/ImportDataset.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/lookoutequipment-2020-12-15/ImportDataset.md "../../../goto/DotNetSDKV3/lookoutequipment-2020-12-15/ImportDataset.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lookoutequipment-2020-12-15/ImportDataset.md "../../../goto/SdkForCpp/lookoutequipment-2020-12-15/ImportDataset.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/ImportDataset.md "../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/ImportDataset.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/ImportDataset.md "../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/ImportDataset.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/ImportDataset.md "../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/ImportDataset.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/ImportDataset.md "../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/ImportDataset.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/ImportDataset.md "../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/ImportDataset.md")
- [AWS SDK for Python](../../../goto/boto3/lookoutequipment-2020-12-15/ImportDataset.md "../../../goto/boto3/lookoutequipment-2020-12-15/ImportDataset.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/ImportDataset.md "../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/ImportDataset.md")
