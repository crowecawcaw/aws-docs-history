On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# InferenceExecutionSummary

Contains information about the specific inference execution, including input and output
data configuration, inference scheduling information, status, and so on.

## Contents

**CustomerResultObject**

The S3 object that the inference execution results were uploaded to.

Type: [S3Object](API_S3Object.md "API_S3Object.md") object

Required: No

**DataEndTime**

Indicates the time reference in the dataset at which the inference execution stopped.

Type: Timestamp

Required: No

**DataInputConfiguration**

Specifies configuration information for the input data for the inference scheduler,
including delimiter, format, and dataset location.

Type: [InferenceInputConfiguration](API_InferenceInputConfiguration.md "API_InferenceInputConfiguration.md") object

Required: No

**DataOutputConfiguration**

Specifies configuration information for the output results from for the inference
execution, including the output Amazon S3 location.

Type: [InferenceOutputConfiguration](API_InferenceOutputConfiguration.md "API_InferenceOutputConfiguration.md") object

Required: No

**DataStartTime**

Indicates the time reference in the dataset at which the inference execution began.

Type: Timestamp

Required: No

**FailedReason**

Specifies the reason for failure when an inference execution has failed.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 5000.

Pattern: `[\P{M}\p{M}]{1,5000}`

Required: No

**InferenceSchedulerArn**

The Amazon Resource Name (ARN) of the inference scheduler being used for the inference
execution.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:inference-scheduler\/.+`

Required: No

**InferenceSchedulerName**

The name of the inference scheduler being used for the inference execution.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `^[0-9a-zA-Z_-]{1,200}$`

Required: No

**ModelArn**

The Amazon Resource Name (ARN) of the machine learning model used for the inference
execution.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:model\/.+`

Required: No

**ModelName**

The name of the machine learning model being used for the inference execution.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `^[0-9a-zA-Z_-]{1,200}$`

Required: No

**ModelVersion**

The model version used for the inference execution.

Type: Long

Valid Range: Minimum value of 1.

Required: No

**ModelVersionArn**

The Amazon Resource Number (ARN) of the model version used for the inference
execution.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `^arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:model\/[0-9a-zA-Z_-]{1,200}\/.+\/model-version\/[0-9]{1,}$`

Required: No

**ScheduledStartTime**

Indicates the start time at which the inference scheduler began the specific inference
execution.

Type: Timestamp

Required: No

**Status**

Indicates the status of the inference execution.

Type: String

Valid Values: `IN_PROGRESS | SUCCESS | FAILED`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/lookoutequipment-2020-12-15/InferenceExecutionSummary.md "../../../goto/SdkForCpp/lookoutequipment-2020-12-15/InferenceExecutionSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/InferenceExecutionSummary.md "../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/InferenceExecutionSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/InferenceExecutionSummary.md "../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/InferenceExecutionSummary.md")
