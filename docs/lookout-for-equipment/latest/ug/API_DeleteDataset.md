On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# DeleteDataset

Deletes a dataset and associated artifacts. The operation will check to see if any
inference scheduler or data ingestion job is currently using the dataset, and if there
isn't, the dataset, its metadata, and any associated data stored in S3 will be deleted.
This does not affect any models that used this dataset for training and evaluation, but
does prevent it from being used in the future.

## Request Syntax

```
{
   "DatasetName": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[DatasetName](#API_DeleteDataset_RequestSyntax "#API_DeleteDataset_RequestSyntax")**

The name of the dataset to be deleted.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `^[0-9a-zA-Z_-]{1,200}$`

Required: Yes

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

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

**ThrottlingException**

The request was denied due to request throttling.

HTTP Status Code: 400

**ValidationException**

The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related AWS
service that's being utilized.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/lookoutequipment-2020-12-15/DeleteDataset.md "../../../goto/cli2/lookoutequipment-2020-12-15/DeleteDataset.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/lookoutequipment-2020-12-15/DeleteDataset.md "../../../goto/DotNetSDKV3/lookoutequipment-2020-12-15/DeleteDataset.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lookoutequipment-2020-12-15/DeleteDataset.md "../../../goto/SdkForCpp/lookoutequipment-2020-12-15/DeleteDataset.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/DeleteDataset.md "../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/DeleteDataset.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/DeleteDataset.md "../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/DeleteDataset.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/DeleteDataset.md "../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/DeleteDataset.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/DeleteDataset.md "../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/DeleteDataset.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/DeleteDataset.md "../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/DeleteDataset.md")
- [AWS SDK for Python](../../../goto/boto3/lookoutequipment-2020-12-15/DeleteDataset.md "../../../goto/boto3/lookoutequipment-2020-12-15/DeleteDataset.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/DeleteDataset.md "../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/DeleteDataset.md")
