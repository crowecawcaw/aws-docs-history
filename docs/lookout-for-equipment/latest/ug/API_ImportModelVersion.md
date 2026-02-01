On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# ImportModelVersion

Imports a model that has been trained successfully.

## Request Syntax

```
{
   "ClientToken": "`string`",
   "DatasetName": "`string`",
   "InferenceDataImportStrategy": "`string`",
   "LabelsInputConfiguration": {
      "LabelGroupName": "`string`",
      "S3InputConfiguration": {
         "Bucket": "`string`",
         "Prefix": "`string`"
      }
   },
   "ModelName": "`string`",
   "RoleArn": "`string`",
   "ServerSideKmsKeyId": "`string`",
   "SourceModelVersionArn": "`string`",
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

**[ClientToken](#API_ImportModelVersion_RequestSyntax "#API_ImportModelVersion_RequestSyntax")**

A unique identifier for the request. If you do not set the client request token,
Amazon Lookout for Equipment generates one.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `\p{ASCII}{1,256}`

Required: Yes

**[DatasetName](#API_ImportModelVersion_RequestSyntax "#API_ImportModelVersion_RequestSyntax")**

The name of the dataset for the machine learning model being imported.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `^[0-9a-zA-Z_-]{1,200}$`

Required: Yes

**[InferenceDataImportStrategy](#API_ImportModelVersion_RequestSyntax "#API_ImportModelVersion_RequestSyntax")**

Indicates how to import the accumulated inference data when a model version is imported.
The possible values are as follows:

- NO_IMPORT – Don't import the data.
- ADD_WHEN_EMPTY – Only import the data from the source model if there is no
  existing data in the target model.
- OVERWRITE – Import the data from the source model and overwrite the
  existing data in the target model.

Type: String

Valid Values: `NO_IMPORT | ADD_WHEN_EMPTY | OVERWRITE`

Required: No

**[LabelsInputConfiguration](#API_ImportModelVersion_RequestSyntax "#API_ImportModelVersion_RequestSyntax")**

Contains the configuration information for the S3 location being used to hold label
data.

Type: [LabelsInputConfiguration](API_LabelsInputConfiguration.md "API_LabelsInputConfiguration.md") object

Required: No

**[ModelName](#API_ImportModelVersion_RequestSyntax "#API_ImportModelVersion_RequestSyntax")**

The name for the machine learning model to be created. If the model already exists,
Amazon Lookout for Equipment creates a new version. If you do not specify this field, it is filled with the
name of the source model.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `^[0-9a-zA-Z_-]{1,200}$`

Required: No

**[RoleArn](#API_ImportModelVersion_RequestSyntax "#API_ImportModelVersion_RequestSyntax")**

The Amazon Resource Name (ARN) of a role with permission to access the data source being
used to create the machine learning model.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`

Required: No

**[ServerSideKmsKeyId](#API_ImportModelVersion_RequestSyntax "#API_ImportModelVersion_RequestSyntax")**

Provides the identifier of the AWS KMS key key used to encrypt model data by Amazon Lookout for Equipment.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Pattern: `^[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,2048}$`

Required: No

**[SourceModelVersionArn](#API_ImportModelVersion_RequestSyntax "#API_ImportModelVersion_RequestSyntax")**

The Amazon Resource Name (ARN) of the model version to import.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `^arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:model\/[0-9a-zA-Z_-]{1,200}\/.+\/model-version\/[0-9]{1,}$`

Required: Yes

**[Tags](#API_ImportModelVersion_RequestSyntax "#API_ImportModelVersion_RequestSyntax")**

The tags associated with the machine learning model to be created.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Array Members: Minimum number of 0 items. Maximum number of 200 items.

Required: No

## Response Syntax

```
{
   "ModelArn": "***string***",
   "ModelName": "***string***",
   "ModelVersion": ***number***,
   "ModelVersionArn": "***string***",
   "Status": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[ModelArn](#API_ImportModelVersion_ResponseSyntax "#API_ImportModelVersion_ResponseSyntax")**

The Amazon Resource Name (ARN) of the model being created.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:model\/.+`

**[ModelName](#API_ImportModelVersion_ResponseSyntax "#API_ImportModelVersion_ResponseSyntax")**

The name for the machine learning model.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `^[0-9a-zA-Z_-]{1,200}$`

**[ModelVersion](#API_ImportModelVersion_ResponseSyntax "#API_ImportModelVersion_ResponseSyntax")**

The version of the model being created.

Type: Long

Valid Range: Minimum value of 1.

**[ModelVersionArn](#API_ImportModelVersion_ResponseSyntax "#API_ImportModelVersion_ResponseSyntax")**

The Amazon Resource Name (ARN) of the model version being created.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `^arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:model\/[0-9a-zA-Z_-]{1,200}\/.+\/model-version\/[0-9]{1,}$`

**[Status](#API_ImportModelVersion_ResponseSyntax "#API_ImportModelVersion_ResponseSyntax")**

The status of the `ImportModelVersion` operation.

Type: String

Valid Values: `IN_PROGRESS | SUCCESS | FAILED | IMPORT_IN_PROGRESS | CANCELED`

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

- [AWS Command Line Interface V2](../../../goto/cli2/lookoutequipment-2020-12-15/ImportModelVersion.md "../../../goto/cli2/lookoutequipment-2020-12-15/ImportModelVersion.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/lookoutequipment-2020-12-15/ImportModelVersion.md "../../../goto/DotNetSDKV4/lookoutequipment-2020-12-15/ImportModelVersion.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lookoutequipment-2020-12-15/ImportModelVersion.md "../../../goto/SdkForCpp/lookoutequipment-2020-12-15/ImportModelVersion.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/ImportModelVersion.md "../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/ImportModelVersion.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/ImportModelVersion.md "../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/ImportModelVersion.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/ImportModelVersion.md "../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/ImportModelVersion.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/ImportModelVersion.md "../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/ImportModelVersion.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/ImportModelVersion.md "../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/ImportModelVersion.md")
- [AWS SDK for Python](../../../goto/boto3/lookoutequipment-2020-12-15/ImportModelVersion.md "../../../goto/boto3/lookoutequipment-2020-12-15/ImportModelVersion.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/ImportModelVersion.md "../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/ImportModelVersion.md")
