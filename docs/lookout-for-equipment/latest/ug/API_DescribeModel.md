On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# DescribeModel

Provides a JSON containing the overall information about a specific machine learning
model, including model name and ARN, dataset, training and evaluation information, status,
and so on.

## Request Syntax

```
{
   "ModelName": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[ModelName](#API_DescribeModel_RequestSyntax "#API_DescribeModel_RequestSyntax")**

The name of the machine learning model to be described.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `^[0-9a-zA-Z_-]{1,200}$`

Required: Yes

## Response Syntax

```
{
   "AccumulatedInferenceDataEndTime": ***number***,
   "AccumulatedInferenceDataStartTime": ***number***,
   "ActiveModelVersion": ***number***,
   "ActiveModelVersionArn": "***string***",
   "CreatedAt": ***number***,
   "DataPreProcessingConfiguration": {
      "TargetSamplingRate": "***string***"
   },
   "DatasetArn": "***string***",
   "DatasetName": "***string***",
   "EvaluationDataEndTime": ***number***,
   "EvaluationDataStartTime": ***number***,
   "FailedReason": "***string***",
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
   "LatestScheduledRetrainingAvailableDataInDays": ***number***,
   "LatestScheduledRetrainingFailedReason": "***string***",
   "LatestScheduledRetrainingModelVersion": ***number***,
   "LatestScheduledRetrainingStartTime": ***number***,
   "LatestScheduledRetrainingStatus": "***string***",
   "ModelArn": "***string***",
   "ModelDiagnosticsOutputConfiguration": {
      "KmsKeyId": "***string***",
      "S3OutputConfiguration": {
         "Bucket": "***string***",
         "Prefix": "***string***"
      }
   },
   "ModelMetrics": "***string***",
   "ModelName": "***string***",
   "ModelQuality": "***string***",
   "ModelVersionActivatedAt": ***number***,
   "NextScheduledRetrainingStartDate": ***number***,
   "OffCondition": "***string***",
   "PreviousActiveModelVersion": ***number***,
   "PreviousActiveModelVersionArn": "***string***",
   "PreviousModelVersionActivatedAt": ***number***,
   "PriorModelMetrics": "***string***",
   "RetrainingSchedulerStatus": "***string***",
   "RoleArn": "***string***",
   "Schema": "***string***",
   "ServerSideKmsKeyId": "***string***",
   "SourceModelVersionArn": "***string***",
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

**[AccumulatedInferenceDataEndTime](#API_DescribeModel_ResponseSyntax "#API_DescribeModel_ResponseSyntax")**

Indicates the end time of the inference data that has been accumulated.

Type: Timestamp

**[AccumulatedInferenceDataStartTime](#API_DescribeModel_ResponseSyntax "#API_DescribeModel_ResponseSyntax")**

Indicates the start time of the inference data that has been accumulated.

Type: Timestamp

**[ActiveModelVersion](#API_DescribeModel_ResponseSyntax "#API_DescribeModel_ResponseSyntax")**

The name of the model version used by the inference schedular when running a scheduled
inference execution.

Type: Long

Valid Range: Minimum value of 1.

**[ActiveModelVersionArn](#API_DescribeModel_ResponseSyntax "#API_DescribeModel_ResponseSyntax")**

The Amazon Resource Name (ARN) of the model version used by the inference scheduler when
running a scheduled inference execution.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `^arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:model\/[0-9a-zA-Z_-]{1,200}\/.+\/model-version\/[0-9]{1,}$`

**[CreatedAt](#API_DescribeModel_ResponseSyntax "#API_DescribeModel_ResponseSyntax")**

Indicates the time and date at which the machine learning model was created.

Type: Timestamp

**[DataPreProcessingConfiguration](#API_DescribeModel_ResponseSyntax "#API_DescribeModel_ResponseSyntax")**

The configuration is the `TargetSamplingRate`, which is the sampling rate of
the data after post processing by Amazon Lookout for Equipment. For example, if you provide data that has been
collected at a 1 second level and you want the system to resample the data at a 1 minute
rate before training, the `TargetSamplingRate` is 1 minute.

When providing a value for the `TargetSamplingRate`, you must attach the
prefix "PT" to the rate you want. The value for a 1 second rate is therefore
_PT1S_, the value for a 15 minute rate is _PT15M_,
and the value for a 1 hour rate is _PT1H_

Type: [DataPreProcessingConfiguration](API_DataPreProcessingConfiguration.md "API_DataPreProcessingConfiguration.md") object

**[DatasetArn](#API_DescribeModel_ResponseSyntax "#API_DescribeModel_ResponseSyntax")**

The Amazon Resouce Name (ARN) of the dataset used to create the machine learning model
being described.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:dataset\/[0-9a-zA-Z_-]{1,200}\/.+`

**[DatasetName](#API_DescribeModel_ResponseSyntax "#API_DescribeModel_ResponseSyntax")**

The name of the dataset being used by the machine learning being described.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `^[0-9a-zA-Z_-]{1,200}$`

**[EvaluationDataEndTime](#API_DescribeModel_ResponseSyntax "#API_DescribeModel_ResponseSyntax")**

Indicates the time reference in the dataset that was used to end the subset of
evaluation data for the machine learning model.

Type: Timestamp

**[EvaluationDataStartTime](#API_DescribeModel_ResponseSyntax "#API_DescribeModel_ResponseSyntax")**

Indicates the time reference in the dataset that was used to begin the subset of
evaluation data for the machine learning model.

Type: Timestamp

**[FailedReason](#API_DescribeModel_ResponseSyntax "#API_DescribeModel_ResponseSyntax")**

If the training of the machine learning model failed, this indicates the reason for that
failure.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 5000.

Pattern: `[\P{M}\p{M}]{1,5000}`

**[ImportJobEndTime](#API_DescribeModel_ResponseSyntax "#API_DescribeModel_ResponseSyntax")**

The date and time when the import job was completed. This field appears if the active
model version was imported.

Type: Timestamp

**[ImportJobStartTime](#API_DescribeModel_ResponseSyntax "#API_DescribeModel_ResponseSyntax")**

The date and time when the import job was started. This field appears if the active
model version was imported.

Type: Timestamp

**[LabelsInputConfiguration](#API_DescribeModel_ResponseSyntax "#API_DescribeModel_ResponseSyntax")**

Specifies configuration information about the labels input, including its S3 location.

Type: [LabelsInputConfiguration](API_LabelsInputConfiguration.md "API_LabelsInputConfiguration.md") object

**[LastUpdatedTime](#API_DescribeModel_ResponseSyntax "#API_DescribeModel_ResponseSyntax")**

Indicates the last time the machine learning model was updated. The type of update is
not specified.

Type: Timestamp

**[LatestScheduledRetrainingAvailableDataInDays](#API_DescribeModel_ResponseSyntax "#API_DescribeModel_ResponseSyntax")**

Indicates the number of days of data used in the most recent scheduled retraining run.

Type: Integer

**[LatestScheduledRetrainingFailedReason](#API_DescribeModel_ResponseSyntax "#API_DescribeModel_ResponseSyntax")**

If the model version was generated by retraining and the training failed, this indicates
the reason for that failure.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 5000.

Pattern: `[\P{M}\p{M}]{1,5000}`

**[LatestScheduledRetrainingModelVersion](#API_DescribeModel_ResponseSyntax "#API_DescribeModel_ResponseSyntax")**

Indicates the most recent model version that was generated by retraining.

Type: Long

Valid Range: Minimum value of 1.

**[LatestScheduledRetrainingStartTime](#API_DescribeModel_ResponseSyntax "#API_DescribeModel_ResponseSyntax")**

Indicates the start time of the most recent scheduled retraining run.

Type: Timestamp

**[LatestScheduledRetrainingStatus](#API_DescribeModel_ResponseSyntax "#API_DescribeModel_ResponseSyntax")**

Indicates the status of the most recent scheduled retraining run.

Type: String

Valid Values: `IN_PROGRESS | SUCCESS | FAILED | IMPORT_IN_PROGRESS | CANCELED`

**[ModelArn](#API_DescribeModel_ResponseSyntax "#API_DescribeModel_ResponseSyntax")**

The Amazon Resource Name (ARN) of the machine learning model being described.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:model\/.+`

**[ModelDiagnosticsOutputConfiguration](#API_DescribeModel_ResponseSyntax "#API_DescribeModel_ResponseSyntax")**

Configuration information for the model's pointwise model diagnostics.

Type: [ModelDiagnosticsOutputConfiguration](API_ModelDiagnosticsOutputConfiguration.md "API_ModelDiagnosticsOutputConfiguration.md") object

**[ModelMetrics](#API_DescribeModel_ResponseSyntax "#API_DescribeModel_ResponseSyntax")**

The Model Metrics show an aggregated summary of the model's performance within the
evaluation time range. This is the JSON content of the metrics created when evaluating the
model.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 50000.

**[ModelName](#API_DescribeModel_ResponseSyntax "#API_DescribeModel_ResponseSyntax")**

The name of the machine learning model being described.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `^[0-9a-zA-Z_-]{1,200}$`

**[ModelQuality](#API_DescribeModel_ResponseSyntax "#API_DescribeModel_ResponseSyntax")**

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

**[ModelVersionActivatedAt](#API_DescribeModel_ResponseSyntax "#API_DescribeModel_ResponseSyntax")**

The date the active model version was activated.

Type: Timestamp

**[NextScheduledRetrainingStartDate](#API_DescribeModel_ResponseSyntax "#API_DescribeModel_ResponseSyntax")**

Indicates the date and time that the next scheduled retraining run will start on. Lookout for Equipment
truncates the time you provide to the nearest UTC day.

Type: Timestamp

**[OffCondition](#API_DescribeModel_ResponseSyntax "#API_DescribeModel_ResponseSyntax")**

Indicates that the asset associated with this sensor has been shut off. As long as this
condition is met, Lookout for Equipment will not use data from this asset for training, evaluation, or
inference.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

**[PreviousActiveModelVersion](#API_DescribeModel_ResponseSyntax "#API_DescribeModel_ResponseSyntax")**

The model version that was set as the active model version prior to the current active
model version.

Type: Long

Valid Range: Minimum value of 1.

**[PreviousActiveModelVersionArn](#API_DescribeModel_ResponseSyntax "#API_DescribeModel_ResponseSyntax")**

The ARN of the model version that was set as the active model version prior to the
current active model version.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `^arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:model\/[0-9a-zA-Z_-]{1,200}\/.+\/model-version\/[0-9]{1,}$`

**[PreviousModelVersionActivatedAt](#API_DescribeModel_ResponseSyntax "#API_DescribeModel_ResponseSyntax")**

The date and time when the previous active model version was activated.

Type: Timestamp

**[PriorModelMetrics](#API_DescribeModel_ResponseSyntax "#API_DescribeModel_ResponseSyntax")**

If the model version was retrained, this field shows a summary of the performance of the
prior model on the new training range. You can use the information in this JSON-formatted
object to compare the new model version and the prior model version.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 50000.

**[RetrainingSchedulerStatus](#API_DescribeModel_ResponseSyntax "#API_DescribeModel_ResponseSyntax")**

Indicates the status of the retraining scheduler.

Type: String

Valid Values: `PENDING | RUNNING | STOPPING | STOPPED`

**[RoleArn](#API_DescribeModel_ResponseSyntax "#API_DescribeModel_ResponseSyntax")**

The Amazon Resource Name (ARN) of a role with permission to access the data source for
the machine learning model being described.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`

**[Schema](#API_DescribeModel_ResponseSyntax "#API_DescribeModel_ResponseSyntax")**

A JSON description of the data that is in each time series dataset, including names,
column names, and data types.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1000000.

**[ServerSideKmsKeyId](#API_DescribeModel_ResponseSyntax "#API_DescribeModel_ResponseSyntax")**

Provides the identifier of the AWS KMS key used to encrypt model data by Amazon Lookout
for Equipment.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `arn:aws[a-z\-]*:kms:[a-z0-9\-]*:\d{12}:[\w\-\/]+`

**[SourceModelVersionArn](#API_DescribeModel_ResponseSyntax "#API_DescribeModel_ResponseSyntax")**

The Amazon Resource Name (ARN) of the source model version. This field appears if the
active model version was imported.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `^arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:model\/[0-9a-zA-Z_-]{1,200}\/.+\/model-version\/[0-9]{1,}$`

**[Status](#API_DescribeModel_ResponseSyntax "#API_DescribeModel_ResponseSyntax")**

Specifies the current status of the model being described. Status describes the status
of the most recent action of the model.

Type: String

Valid Values: `IN_PROGRESS | SUCCESS | FAILED | IMPORT_IN_PROGRESS`

**[TrainingDataEndTime](#API_DescribeModel_ResponseSyntax "#API_DescribeModel_ResponseSyntax")**

Indicates the time reference in the dataset that was used to end the subset of training
data for the machine learning model.

Type: Timestamp

**[TrainingDataStartTime](#API_DescribeModel_ResponseSyntax "#API_DescribeModel_ResponseSyntax")**

Indicates the time reference in the dataset that was used to begin the subset of
training data for the machine learning model.

Type: Timestamp

**[TrainingExecutionEndTime](#API_DescribeModel_ResponseSyntax "#API_DescribeModel_ResponseSyntax")**

Indicates the time at which the training of the machine learning model was completed.

Type: Timestamp

**[TrainingExecutionStartTime](#API_DescribeModel_ResponseSyntax "#API_DescribeModel_ResponseSyntax")**

Indicates the time at which the training of the machine learning model began.

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

- [AWS Command Line Interface V2](../../../goto/cli2/lookoutequipment-2020-12-15/DescribeModel.md "../../../goto/cli2/lookoutequipment-2020-12-15/DescribeModel.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/lookoutequipment-2020-12-15/DescribeModel.md "../../../goto/DotNetSDKV3/lookoutequipment-2020-12-15/DescribeModel.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lookoutequipment-2020-12-15/DescribeModel.md "../../../goto/SdkForCpp/lookoutequipment-2020-12-15/DescribeModel.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/DescribeModel.md "../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/DescribeModel.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/DescribeModel.md "../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/DescribeModel.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/DescribeModel.md "../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/DescribeModel.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/DescribeModel.md "../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/DescribeModel.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/DescribeModel.md "../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/DescribeModel.md")
- [AWS SDK for Python](../../../goto/boto3/lookoutequipment-2020-12-15/DescribeModel.md "../../../goto/boto3/lookoutequipment-2020-12-15/DescribeModel.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/DescribeModel.md "../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/DescribeModel.md")
