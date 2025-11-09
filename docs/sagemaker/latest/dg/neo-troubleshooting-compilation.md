# Troubleshoot Neo Compilation Errors

This section contains information about how to understand and prevent common
compilation errors, the error messages they generate, and guidance on how to
resolve these errors.

###### Topics

- [How to Use This Page](#neo-troubleshooting-compilation-how-to-use "#neo-troubleshooting-compilation-how-to-use")
- [Framework-Related Errors](#neo-troubleshooting-compilation-framework-related-errors "#neo-troubleshooting-compilation-framework-related-errors")
- [Infrastructure-Related Errors](#neo-troubleshooting-compilation-infrastructure-errors "#neo-troubleshooting-compilation-infrastructure-errors")
- [Check your compilation log](#neo-troubleshooting-compilation-logs "#neo-troubleshooting-compilation-logs")

## How to Use This Page

Attempt to resolve your error by the going through these sections in the following order:

1. Check that the input of your compilation job satisfies
   the input requirements. See [What input data shapes does SageMaker Neo expect?](neo-compilation-preparing-model.md#neo-job-compilation-expected-inputs "neo-compilation-preparing-model.md#neo-job-compilation-expected-inputs")
2. Check common [framework-specific errors](neo-troubleshooting-compilation.md#neo-troubleshooting-compilation-framework-related-errors "neo-troubleshooting-compilation.md#neo-troubleshooting-compilation-framework-related-errors").
3. Check if your error is an
   [infrastructure error](neo-troubleshooting-compilation.md#neo-troubleshooting-compilation-infrastructure-errors "neo-troubleshooting-compilation.md#neo-troubleshooting-compilation-infrastructure-errors").
4. Check your [compilation log](neo-troubleshooting-compilation.md#neo-troubleshooting-compilation-logs "neo-troubleshooting-compilation.md#neo-troubleshooting-compilation-logs").

## Framework-Related Errors

| Error                                                                                                                                           | Solution                                                                                                                                                                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `InputConfiguration: No h5 file provided in<br><model path>`                                                                                    | Check your h5 file is in the Amazon S3 URI you specified.<br>_Or_<br>Check that the [h5 file is correctly formatted](https://www.tensorflow.org/guide/keras/save_and_serialize#keras_h5_format "https://www.tensorflow.org/guide/keras/save_and_serialize#keras_h5_format"). |
| `InputConfiguration: Multiple h5 files provided,<br><model path>, when only one is allowed`                                                     | Check you are only providing one `h5`<br>file.                                                                                                                                                                                                                               |
| `ClientError: InputConfiguration: Unable to load<br>provided Keras model. Error:<br>'sample_weight_mode'`                                       | Check the Keras version you specified is supported.<br>See, supported frameworks for [cloud instances](neo-supported-cloud.md "neo-supported-cloud.md") and<br>[edge devices](neo-supported-devices-edge.md "neo-supported-devices-edge.md").                                |
| `ClientError: InputConfiguration: Input input has<br>wrong shape in Input Shape dictionary. Input shapes<br>should be provided in NCHW format.` | Check that your model input follows NCHW format. See<br>[What input data shapes does<br>SageMaker Neo expect?](neo-job-compilation.md#neo-job-compilation-expected-inputs "neo-job-compilation.md#neo-job-compilation-expected-inputs")                                      |

| Error                                                                                                                                                 | Solution                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `ClientError: InputConfiguration: Only one<br>parameter file is allowed for MXNet model. Please<br>make sure the framework you select is<br>correct.` | SageMaker Neo will select the first parameter file given<br>for compilation. |

| Error                                                                                                                                                                                                       | Solution                                                                                                                                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `InputConfiguration: Exactly one .pb file is<br>allowed for TensorFlow models.`                                                                                                                             | Make sure you only provide one .pb or .pbtxt<br>file.                                                                                                                                                                                                                                |
| `InputConfiguration: Exactly one .pb or .pbtxt<br>file is allowed for TensorFlow models.`                                                                                                                   | Make sure you only provide one .pb or .pbtxt<br>file.                                                                                                                                                                                                                                |
| `ClientError: InputConfiguration: TVM cannot<br>convert <model zoo> model. Please make sure<br>the framework you selected is correct. The following<br>operators are not implemented: {<operator<br>name>}` | Check the operator you chose is supported. See [SageMaker Neo Supported Frameworks<br>and Operators](https://aws.amazon.com/releasenotes/sagemaker-neo-supported-frameworks-and-operators/ "https://aws.amazon.com/releasenotes/sagemaker-neo-supported-frameworks-and-operators/"). |

| Error                                                                                                                                                                                                             | Solution                                                                                                                                                                                                                                                                                                                                                            |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `InputConfiguration: We are unable to extract<br>DataInputConfig from the model due to<br>`input_config_derivation_error`.<br>Please override by providing a DataInputConfig<br>during compilation job creation.` | Do either of the following:<br>• Specify the name and shape of the expected<br>inputs by providing a `DataInputConfig`<br>definition in your compilation request.<br>• Investigate the error in Amazon CloudWatch Logs. Check the<br>`/aws/sagemaker/CompilationJobs` log<br>group and look for a log stream named<br>``compilationJobName`/model-info-extraction`. |

## Infrastructure-Related Errors

| Error                                                                                                                                                       | Solution                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `ClientError: InputConfiguration: S3 object does not exist. Bucket: <bucket>, Key: <bucket key>`                                                            | Check the Amazon S3 URI your provided.                                 |
| `ClientError: InputConfiguration: Bucket <bucket name> is in region <region name> which<br>is different from AWS Sagemaker service region <service region>` | Create an Amazon S3 bucket that is in the same region as the service.  |
| `ClientError: InputConfiguration: Unable to untar input model. Please confirm the model is a tar.gz file`                                                   | Check that your model in Amazon S3 is compressed into a `tar.gz` file. |

## Check your compilation log

1. Navigate to Amazon CloudWatch at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. Select the region you created the compilation job from the **Region** dropdown list in the top right.
3. In the navigation pane of the Amazon CloudWatch, choose **Logs**. Select **Log groups**.
4. Search for the log group called `/aws/sagemaker/CompilationJobs`. Select the log group.
5. Search for the logstream named after the compilation job name. Select the log stream.
