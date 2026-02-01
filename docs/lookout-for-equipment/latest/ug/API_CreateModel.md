On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# CreateModel

Creates a machine learning model for data inference.

A machine-learning (ML) model is a mathematical model that finds patterns in your data.
In Amazon Lookout for Equipment, the model learns the patterns of normal behavior and detects abnormal
behavior that could be potential equipment failure (or maintenance events). The models are
made by analyzing normal data and abnormalities in machine behavior that have already
occurred.

Your model is trained using a portion of the data from your dataset and uses that data
to learn patterns of normal behavior and abnormal patterns that lead to equipment failure.
Another portion of the data is used to evaluate the model's accuracy.

## Request Syntax

```
{
   "ClientToken": "`string`",
   "DataPreProcessingConfiguration": {
      "TargetSamplingRate": "`string`"
   },
   "DatasetName": "`string`",
   "DatasetSchema": {
      "InlineDataSchema": "`string`"
   },
   "EvaluationDataEndTime": `number`,
   "EvaluationDataStartTime": `number`,
   "LabelsInputConfiguration": {
      "LabelGroupName": "`string`",
      "S3InputConfiguration": {
         "Bucket": "`string`",
         "Prefix": "`string`"
      }
   },
   "ModelDiagnosticsOutputConfiguration": {
      "KmsKeyId": "`string`",
      "S3OutputConfiguration": {
         "Bucket": "`string`",
         "Prefix": "`string`"
      }
   },
   "ModelName": "`string`",
   "OffCondition": "`string`",
   "RoleArn": "`string`",
   "ServerSideKmsKeyId": "`string`",
   "Tags": [
      {
         "Key": "`string`",
         "Value": "`string`"
      }
   ],
   "TrainingDataEndTime": `number`,
   "TrainingDataStartTime": `number`
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[ClientToken](#API_CreateModel_RequestSyntax "#API_CreateModel_RequestSyntax")**

A unique identifier for the request. If you do not set the client request token, Amazon
Lookout for Equipment generates one.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `\p{ASCII}{1,256}`

Required: Yes

**[DataPreProcessingConfiguration](#API_CreateModel_RequestSyntax "#API_CreateModel_RequestSyntax")**

The configuration is the `TargetSamplingRate`, which is the sampling rate of
the data after post processing by Amazon Lookout for Equipment. For example, if you provide data that has been
collected at a 1 second level and you want the system to resample the data at a 1 minute
rate before training, the `TargetSamplingRate` is 1 minute.

When providing a value for the `TargetSamplingRate`, you must attach the
prefix "PT" to the rate you want. The value for a 1 second rate is therefore
_PT1S_, the value for a 15 minute rate is _PT15M_,
and the value for a 1 hour rate is _PT1H_

Type: [DataPreProcessingConfiguration](API_DataPreProcessingConfiguration.md "API_DataPreProcessingConfiguration.md") object

Required: No

**[DatasetName](#API_CreateModel_RequestSyntax "#API_CreateModel_RequestSyntax")**

The name of the dataset for the machine learning model being created.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `^[0-9a-zA-Z_-]{1,200}$`

Required: Yes

**[DatasetSchema](#API_CreateModel_RequestSyntax "#API_CreateModel_RequestSyntax")**

The data schema for the machine learning model being created.

Type: [DatasetSchema](API_DatasetSchema.md "API_DatasetSchema.md") object

Required: No

**[EvaluationDataEndTime](#API_CreateModel_RequestSyntax "#API_CreateModel_RequestSyntax")**

Indicates the time reference in the dataset that should be used to end the subset of
evaluation data for the machine learning model.

Type: Timestamp

Required: No

**[EvaluationDataStartTime](#API_CreateModel_RequestSyntax "#API_CreateModel_RequestSyntax")**

Indicates the time reference in the dataset that should be used to begin the subset of
evaluation data for the machine learning model.

Type: Timestamp

Required: No

**[LabelsInputConfiguration](#API_CreateModel_RequestSyntax "#API_CreateModel_RequestSyntax")**

The input configuration for the labels being used for the machine learning model that's
being created.

Type: [LabelsInputConfiguration](API_LabelsInputConfiguration.md "API_LabelsInputConfiguration.md") object

Required: No

**[ModelDiagnosticsOutputConfiguration](#API_CreateModel_RequestSyntax "#API_CreateModel_RequestSyntax")**

The Amazon S3 location where you want Amazon Lookout for Equipment to save the pointwise model diagnostics.

You must also specify the `RoleArn` request parameter.

Type: [ModelDiagnosticsOutputConfiguration](API_ModelDiagnosticsOutputConfiguration.md "API_ModelDiagnosticsOutputConfiguration.md") object

Required: No

**[ModelName](#API_CreateModel_RequestSyntax "#API_CreateModel_RequestSyntax")**

The name for the machine learning model to be created.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `^[0-9a-zA-Z_-]{1,200}$`

Required: Yes

**[OffCondition](#API_CreateModel_RequestSyntax "#API_CreateModel_RequestSyntax")**

Indicates that the asset associated with this sensor has been shut off. As long as this
condition is met, Lookout for Equipment will not use data from this asset for training,
evaluation, or inference.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Required: No

**[RoleArn](#API_CreateModel_RequestSyntax "#API_CreateModel_RequestSyntax")**

The Amazon Resource Name (ARN) of a role with permission to access the data source
being used to create the machine learning model.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`

Required: No

**[ServerSideKmsKeyId](#API_CreateModel_RequestSyntax "#API_CreateModel_RequestSyntax")**

Provides the identifier of the AWS KMS key used to encrypt model data by Amazon Lookout
for Equipment.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Pattern: `^[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,2048}$`

Required: No

**[Tags](#API_CreateModel_RequestSyntax "#API_CreateModel_RequestSyntax")**

Any tags associated with the machine learning model being created.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Array Members: Minimum number of 0 items. Maximum number of 200 items.

Required: No

**[TrainingDataEndTime](#API_CreateModel_RequestSyntax "#API_CreateModel_RequestSyntax")**

Indicates the time reference in the dataset that should be used to end the subset of
training data for the machine learning model.

Type: Timestamp

Required: No

**[TrainingDataStartTime](#API_CreateModel_RequestSyntax "#API_CreateModel_RequestSyntax")**

Indicates the time reference in the dataset that should be used to begin the subset of
training data for the machine learning model.

Type: Timestamp

Required: No

## Response Syntax

```
{
   "ModelArn": "***string***",
   "Status": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[ModelArn](#API_CreateModel_ResponseSyntax "#API_CreateModel_ResponseSyntax")**

The Amazon Resource Name (ARN) of the model being created.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:model\/.+`

**[Status](#API_CreateModel_ResponseSyntax "#API_CreateModel_ResponseSyntax")**

Indicates the status of the `CreateModel` operation.

Type: String

Valid Values: `IN_PROGRESS | SUCCESS | FAILED | IMPORT_IN_PROGRESS`

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

- [AWS Command Line Interface V2](../../../goto/cli2/lookoutequipment-2020-12-15/CreateModel.md "../../../goto/cli2/lookoutequipment-2020-12-15/CreateModel.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/lookoutequipment-2020-12-15/CreateModel.md "../../../goto/DotNetSDKV4/lookoutequipment-2020-12-15/CreateModel.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lookoutequipment-2020-12-15/CreateModel.md "../../../goto/SdkForCpp/lookoutequipment-2020-12-15/CreateModel.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/CreateModel.md "../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/CreateModel.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/CreateModel.md "../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/CreateModel.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/CreateModel.md "../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/CreateModel.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/CreateModel.md "../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/CreateModel.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/CreateModel.md "../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/CreateModel.md")
- [AWS SDK for Python](../../../goto/boto3/lookoutequipment-2020-12-15/CreateModel.md "../../../goto/boto3/lookoutequipment-2020-12-15/CreateModel.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/CreateModel.md "../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/CreateModel.md")
