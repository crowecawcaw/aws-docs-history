On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# DescribeModelVersion

Retrieves information about a specific machine learning model version.

## Request Syntax

```
{
   "ModelName": "`string`",
   "ModelVersion": `number`
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[ModelName](#API_DescribeModelVersion_RequestSyntax "#API_DescribeModelVersion_RequestSyntax")**

The name of the machine learning model that this version belongs to.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `^[0-9a-zA-Z_-]{1,200}$`

Required: Yes

**[ModelVersion](#API_DescribeModelVersion_RequestSyntax "#API_DescribeModelVersion_RequestSyntax")**

The version of the machine learning model.

Type: Long

Valid Range: Minimum value of 1.

Required: Yes

## Response Syntax

```
{
   "AutoPromotionResult": "***string***",
   "AutoPromotionResultReason": "***string***",
   "CreatedAt": ***number***,
   "DataPreProcessingConfiguration": {
      "TargetSamplingRate": "***string***"
   },
   "DatasetArn": "***string***",
   "DatasetName": "***string***",
   "EvaluationDataEndTime": ***number***,
   "EvaluationDataStartTime": ***number***,
   "FailedReason": "***string***",
   "ImportedDataSizeInBytes": ***number***,
   "ImportJobEndTime": ***number***,
   "ImportJobStartTime": ***number***,
   "LabelsInputConfiguration": {
      "LabelGroupName": "***string***",
      "S3InputConfiguration": {
         "Bucket": "***string***",
         "Prefix": "***string***"
      }
   },
   "LastUpdatedTime": ***number***,
   "ModelArn": "***string***",
   "ModelDiagnosticsOutputConfiguration": {
      "KmsKeyId": "***string***",
      "S3OutputConfiguration": {
         "Bucket": "***string***",
         "Prefix": "***string***"
      }
   },
   "ModelDiagnosticsResultsObject": {
      "Bucket": "***string***",
      "Key": "***string***"
   },
   "ModelMetrics": "***string***",
   "ModelName": "***string***",
   "ModelQuality": "***string***",
   "ModelVersion": ***number***,
   "ModelVersionArn": "***string***",
   "OffCondition": "***string***",
   "PriorModelMetrics": "***string***",
   "RetrainingAvailableDataInDays": ***number***,
   "RoleArn": "***string***",
   "Schema": "***string***",
   "ServerSideKmsKeyId": "***string***",
   "SourceModelVersionArn": "***string***",
   "SourceType": "***string***",
   "Status": "***string***",
   "TrainingDataEndTime": ***number***,
   "TrainingDataStartTime": ***number***,
   "TrainingExecutionEndTime": ***number***,
   "TrainingExecutionStartTime": ***number***
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[AutoPromotionResult](#API_DescribeModelVersion_ResponseSyntax "#API_DescribeModelVersion_ResponseSyntax")**

Indicates whether the model version was promoted to be the active version after
retraining or if there was an error with or cancellation of the retraining.

Type: String

Valid Values: `MODEL_PROMOTED | MODEL_NOT_PROMOTED | RETRAINING_INTERNAL_ERROR | RETRAINING_CUSTOMER_ERROR | RETRAINING_CANCELLED`

**[AutoPromotionResultReason](#API_DescribeModelVersion_ResponseSyntax "#API_DescribeModelVersion_ResponseSyntax")**

Indicates the reason for the `AutoPromotionResult`. For example, a model
might not be promoted if its performance was worse than the active version, if there was an
error during training, or if the retraining scheduler was using `MANUAL` promote
mode. The model will be promoted in `MANAGED` promote mode if the performance is
better than the previous model.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

**[CreatedAt](#API_DescribeModelVersion_ResponseSyntax "#API_DescribeModelVersion_ResponseSyntax")**

Indicates the time and date at which the machine learning model version was
created.

Type: Timestamp

**[DataPreProcessingConfiguration](#API_DescribeModelVersion_ResponseSyntax "#API_DescribeModelVersion_ResponseSyntax")**

The configuration is the `TargetSamplingRate`, which is the sampling rate of
the data after post processing by Amazon Lookout for Equipment. For example, if you provide data that has been
collected at a 1 second level and you want the system to resample the data at a 1 minute
rate before training, the `TargetSamplingRate` is 1 minute.

When providing a value for the `TargetSamplingRate`, you must attach the
prefix "PT" to the rate you want. The value for a 1 second rate is therefore
_PT1S_, the value for a 15 minute rate is _PT15M_,
and the value for a 1 hour rate is _PT1H_

Type: [DataPreProcessingConfiguration](API_DataPreProcessingConfiguration.md "API_DataPreProcessingConfiguration.md") object

**[DatasetArn](#API_DescribeModelVersion_ResponseSyntax "#API_DescribeModelVersion_ResponseSyntax")**

The Amazon Resource Name (ARN) of the dataset used to train the model version.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:dataset\/[0-9a-zA-Z_-]{1,200}\/.+`

**[DatasetName](#API_DescribeModelVersion_ResponseSyntax "#API_DescribeModelVersion_ResponseSyntax")**

The name of the dataset used to train the model version.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `^[0-9a-zA-Z_-]{1,200}$`

**[EvaluationDataEndTime](#API_DescribeModelVersion_ResponseSyntax "#API_DescribeModelVersion_ResponseSyntax")**

The date on which the data in the evaluation set began being gathered. If you imported
the version, this is the date that the evaluation set data in the source version finished
being gathered.

Type: Timestamp

**[EvaluationDataStartTime](#API_DescribeModelVersion_ResponseSyntax "#API_DescribeModelVersion_ResponseSyntax")**

The date on which the data in the evaluation set began being gathered. If you imported
the version, this is the date that the evaluation set data in the source version began
being gathered.

Type: Timestamp

**[FailedReason](#API_DescribeModelVersion_ResponseSyntax "#API_DescribeModelVersion_ResponseSyntax")**

The failure message if the training of the model version failed.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 5000.

Pattern: `[\P{M}\p{M}]{1,5000}`

**[ImportedDataSizeInBytes](#API_DescribeModelVersion_ResponseSyntax "#API_DescribeModelVersion_ResponseSyntax")**

The size in bytes of the imported data. This field appears if the model version was
imported.

Type: Long

Valid Range: Minimum value of 0.

**[ImportJobEndTime](#API_DescribeModelVersion_ResponseSyntax "#API_DescribeModelVersion_ResponseSyntax")**

The date and time when the import job completed. This field appears if the model version
was imported.

Type: Timestamp

**[ImportJobStartTime](#API_DescribeModelVersion_ResponseSyntax "#API_DescribeModelVersion_ResponseSyntax")**

The date and time when the import job began. This field appears if the model version was
imported.

Type: Timestamp

**[LabelsInputConfiguration](#API_DescribeModelVersion_ResponseSyntax "#API_DescribeModelVersion_ResponseSyntax")**

Contains the configuration information for the S3 location being used to hold label
data.

Type: [LabelsInputConfiguration](API_LabelsInputConfiguration.md "API_LabelsInputConfiguration.md") object

**[LastUpdatedTime](#API_DescribeModelVersion_ResponseSyntax "#API_DescribeModelVersion_ResponseSyntax")**

Indicates the last time the machine learning model version was updated.

Type: Timestamp

**[ModelArn](#API_DescribeModelVersion_ResponseSyntax "#API_DescribeModelVersion_ResponseSyntax")**

The Amazon Resource Name (ARN) of the parent machine learning model that this version
belong to.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:model\/.+`

**[ModelDiagnosticsOutputConfiguration](#API_DescribeModelVersion_ResponseSyntax "#API_DescribeModelVersion_ResponseSyntax")**

The Amazon S3 location where Amazon Lookout for Equipment saves the pointwise model diagnostics for the model version.

Type: [ModelDiagnosticsOutputConfiguration](API_ModelDiagnosticsOutputConfiguration.md "API_ModelDiagnosticsOutputConfiguration.md") object

**[ModelDiagnosticsResultsObject](#API_DescribeModelVersion_ResponseSyntax "#API_DescribeModelVersion_ResponseSyntax")**

Contains the Amazon S3 object path where Amazon Lookout for Equipment writes the model diagnostics results for the
model version. The format is
`User_Provided_Prefix/Model_Name/Model_Version/model_diagnostics_results.json.gz`.

`User_Provided_Prefix` is the prefix that you specify in the
`ModelDiagnosticsOutputConfiguration` request parameter to the
`CreateModel` or `UpdateModel` operations.

Type: [S3Object](API_S3Object.md "API_S3Object.md") object

**[ModelMetrics](#API_DescribeModelVersion_ResponseSyntax "#API_DescribeModelVersion_ResponseSyntax")**

Shows an aggregated summary, in JSON format, of the model's performance within the
evaluation time range. These metrics are created when evaluating the model.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 50000.

**[ModelName](#API_DescribeModelVersion_ResponseSyntax "#API_DescribeModelVersion_ResponseSyntax")**

The name of the machine learning model that this version belongs to.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `^[0-9a-zA-Z_-]{1,200}$`

**[ModelQuality](#API_DescribeModelVersion_ResponseSyntax "#API_DescribeModelVersion_ResponseSyntax")**

Provides a quality assessment for a model that uses labels. If Lookout for Equipment determines that the
model quality is poor based on training metrics, the value is
`POOR_QUALITY_DETECTED`. Otherwise, the value is
`QUALITY_THRESHOLD_MET`.

If the model is unlabeled, the model quality can't
be assessed and the value of `ModelQuality` is
`CANNOT_DETERMINE_QUALITY`. In this situation, you can get a model quality
assessment by adding labels to the input dataset and retraining the model.

For information about using labels with your models, see [Understanding labeling](understanding-labeling.md "understanding-labeling.md").

For information about improving the quality of a model, see [Best practices with
Amazon Lookout for Equipment](best-practices.md "best-practices.md").

Type: String

Valid Values: `QUALITY_THRESHOLD_MET | CANNOT_DETERMINE_QUALITY | POOR_QUALITY_DETECTED`

**[ModelVersion](#API_DescribeModelVersion_ResponseSyntax "#API_DescribeModelVersion_ResponseSyntax")**

The version of the machine learning model.

Type: Long

Valid Range: Minimum value of 1.

**[ModelVersionArn](#API_DescribeModelVersion_ResponseSyntax "#API_DescribeModelVersion_ResponseSyntax")**

The Amazon Resource Name (ARN) of the model version.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `^arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:model\/[0-9a-zA-Z_-]{1,200}\/.+\/model-version\/[0-9]{1,}$`

**[OffCondition](#API_DescribeModelVersion_ResponseSyntax "#API_DescribeModelVersion_ResponseSyntax")**

Indicates that the asset associated with this sensor has been shut off. As long as this
condition is met, Lookout for Equipment will not use data from this asset for training,
evaluation, or inference.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

**[PriorModelMetrics](#API_DescribeModelVersion_ResponseSyntax "#API_DescribeModelVersion_ResponseSyntax")**

If the model version was retrained, this field shows a summary of the performance of the
prior model on the new training range. You can use the information in this JSON-formatted
object to compare the new model version and the prior model version.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 50000.

**[RetrainingAvailableDataInDays](#API_DescribeModelVersion_ResponseSyntax "#API_DescribeModelVersion_ResponseSyntax")**

Indicates the number of days of data used in the most recent scheduled retraining run.

Type: Integer

**[RoleArn](#API_DescribeModelVersion_ResponseSyntax "#API_DescribeModelVersion_ResponseSyntax")**

The Amazon Resource Name (ARN) of the role that was used to train the model
version.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`

**[Schema](#API_DescribeModelVersion_ResponseSyntax "#API_DescribeModelVersion_ResponseSyntax")**

The schema of the data used to train the model version.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1000000.

**[ServerSideKmsKeyId](#API_DescribeModelVersion_ResponseSyntax "#API_DescribeModelVersion_ResponseSyntax")**

The identifier of the AWS KMS key key used to encrypt model version data by
Amazon Lookout for Equipment.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `arn:aws[a-z\-]*:kms:[a-z0-9\-]*:\d{12}:[\w\-\/]+`

**[SourceModelVersionArn](#API_DescribeModelVersion_ResponseSyntax "#API_DescribeModelVersion_ResponseSyntax")**

If model version was imported, then this field is the arn of the source model
version.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `^arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:model\/[0-9a-zA-Z_-]{1,200}\/.+\/model-version\/[0-9]{1,}$`

**[SourceType](#API_DescribeModelVersion_ResponseSyntax "#API_DescribeModelVersion_ResponseSyntax")**

Indicates whether this model version was created by training or by importing.

Type: String

Valid Values: `TRAINING | RETRAINING | IMPORT`

**[Status](#API_DescribeModelVersion_ResponseSyntax "#API_DescribeModelVersion_ResponseSyntax")**

The current status of the model version.

Type: String

Valid Values: `IN_PROGRESS | SUCCESS | FAILED | IMPORT_IN_PROGRESS | CANCELED`

**[TrainingDataEndTime](#API_DescribeModelVersion_ResponseSyntax "#API_DescribeModelVersion_ResponseSyntax")**

The date on which the training data finished being gathered. If you imported the
version, this is the date that the training data in the source version finished being
gathered.

Type: Timestamp

**[TrainingDataStartTime](#API_DescribeModelVersion_ResponseSyntax "#API_DescribeModelVersion_ResponseSyntax")**

The date on which the training data began being gathered. If you imported the version,
this is the date that the training data in the source version began being gathered.

Type: Timestamp

**[TrainingExecutionEndTime](#API_DescribeModelVersion_ResponseSyntax "#API_DescribeModelVersion_ResponseSyntax")**

The time when the training of the version completed.

Type: Timestamp

**[TrainingExecutionStartTime](#API_DescribeModelVersion_ResponseSyntax "#API_DescribeModelVersion_ResponseSyntax")**

The time when the training of the version began.

Type: Timestamp

## Errors

**AccessDeniedException**

The request could not be completed because you do not have access to the resource.

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

- [AWS Command Line Interface V2](../../../goto/cli2/lookoutequipment-2020-12-15/DescribeModelVersion.md "../../../goto/cli2/lookoutequipment-2020-12-15/DescribeModelVersion.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/lookoutequipment-2020-12-15/DescribeModelVersion.md "../../../goto/DotNetSDKV3/lookoutequipment-2020-12-15/DescribeModelVersion.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lookoutequipment-2020-12-15/DescribeModelVersion.md "../../../goto/SdkForCpp/lookoutequipment-2020-12-15/DescribeModelVersion.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/DescribeModelVersion.md "../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/DescribeModelVersion.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/DescribeModelVersion.md "../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/DescribeModelVersion.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/DescribeModelVersion.md "../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/DescribeModelVersion.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/DescribeModelVersion.md "../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/DescribeModelVersion.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/DescribeModelVersion.md "../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/DescribeModelVersion.md")
- [AWS SDK for Python](../../../goto/boto3/lookoutequipment-2020-12-15/DescribeModelVersion.md "../../../goto/boto3/lookoutequipment-2020-12-15/DescribeModelVersion.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/DescribeModelVersion.md "../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/DescribeModelVersion.md")
