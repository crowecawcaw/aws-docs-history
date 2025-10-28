# Compile a Model (AWS Command Line Interface)

This section shows how to manage Amazon SageMaker Neo compilation jobs for machine learning
models using AWS Command Line Interface (CLI). You can create, describe, stop, and list the compilation
jobs.

1. Create a Compilation Job

With the [CreateCompilationJob](../APIReference/API_CreateCompilationJob.md "../APIReference/API_CreateCompilationJob.md") API operation, you can specify the data input
format, the S3 bucket in which to store your model, the S3 bucket to which to
write the compiled model, and the target hardware device or platform.

The following table demonstrates how to configure `CreateCompilationJob`
API based on whether your target is a device or a platform.

Device Example

```
{
    "CompilationJobName": "`neo-compilation-job-demo`",
    "RoleArn": "`arn:aws:iam::`<your-account>`:role/service-role/AmazonSageMaker-ExecutionRole-yyyymmddThhmmss`",
    "InputConfig": {
        "S3Uri": "`s3://`<your-bucket>`/sagemaker/neo-compilation-job-demo-data/train`",
        "DataInputConfig":  "`{'data': [1,3,1024,1024]}`",
        "Framework": "`MXNET`"
    },
    "OutputConfig": {
        "S3OutputLocation": "`s3://`<your-bucket>`/sagemaker/neo-compilation-job-demo-data/compile`",
        # A target device specification example for a ml_c5 instance family
        "TargetDevice": "`ml_c5`"
    },
    "StoppingCondition": {
        "MaxRuntimeInSeconds": `300`
    }
}
```

You can optionally specify the framework version you used
with the [`FrameworkVersion`](../APIReference/API_InputConfig.md#sagemaker-Type-InputConfig-FrameworkVersion "../APIReference/API_InputConfig.md#sagemaker-Type-InputConfig-FrameworkVersion") field if you used the PyTorch framework to train
your model and your target device is a `ml_*` target.

```
{
    "CompilationJobName": "neo-compilation-job-demo",
    "RoleArn": "arn:aws:iam::`<your-account>`:role/service-role/AmazonSageMaker-ExecutionRole-yyyymmddThhmmss",
    "InputConfig": {
        "S3Uri": "s3://`<your-bucket>`/sagemaker/neo-compilation-job-demo-data/train",
        "DataInputConfig":  "{'data': [1,3,1024,1024]}",
        "Framework": "PYTORCH",
        "FrameworkVersion": "1.6"
    },
    "OutputConfig": {
        "S3OutputLocation": "s3://`<your-bucket>`/sagemaker/neo-compilation-job-demo-data/compile",
        # A target device specification example for a ml_c5 instance family
        "TargetDevice": "ml_c5",
        # When compiling for ml_* instances using PyTorch framework, use the "CompilerOptions" field in
        # OutputConfig to provide the correct data type ("dtype") of the model’s input. Default assumed is "float32"
        "CompilerOptions": "{'dtype': 'long'}"
    },
    "StoppingCondition": {
        "MaxRuntimeInSeconds": 300
    }
}
```

###### Notes:

    * If you saved your model by using
     PyTorch version 2.0 or later, the
     `DataInputConfig` field is optional. SageMaker AI
     Neo gets the input configuration from the model
     definition file that you create with PyTorch. For more
     information about how to create the definition file, see
     the [PyTorch](neo-compilation-preparing-model.md#how-to-save-pytorch "neo-compilation-preparing-model.md#how-to-save-pytorch") section under
     *Saving Models for SageMaker AI
     Neo*.
    * This API field is only supported for PyTorch.

Platform Example

```
{
    "CompilationJobName": "`neo-test-compilation-job`",
    "RoleArn": "`arn:aws:iam::`<your-account>:`role/service-role/AmazonSageMaker-ExecutionRole-yyyymmddThhmmss`",
    "InputConfig": {
        "S3Uri": "`s3://`<your-bucket>`/sagemaker/neo-compilation-job-demo-data/train`",
        "DataInputConfig":  "`{'data': [1,3,1024,1024]}`",
        "Framework": "`MXNET`"
    },
    "OutputConfig": {
        "S3OutputLocation": "`s3://`<your-bucket>`/sagemaker/neo-compilation-job-demo-data/compile`",
        # A target platform configuration example for a p3.2xlarge instance
        "TargetPlatform": {
            "Os": "`LINUX`",
            "Arch": "`X86_64`",
            "Accelerator": "`NVIDIA`"
        },
        "CompilerOptions": "{`'cuda-ver': '10.0', 'trt-ver': '6.0.1', 'gpu-code': 'sm_70'`}"
    },
    "StoppingCondition": {
        "MaxRuntimeInSeconds": `300`
    }
}
```

###### Note

For the `OutputConfig` API operation,
the `TargetDevice` and `TargetPlatform` API operations are
mutually exclusive. You have to choose one of the two options.

To find the JSON string examples of `DataInputConfig` depending on frameworks,
see [What input data shapes Neo expects](neo-troubleshooting-compilation.md#neo-troubleshooting-errors-preventing "neo-troubleshooting-compilation.md#neo-troubleshooting-errors-preventing").

For more information about setting up the configurations, see the [InputConfig](../APIReference/API_InputConfig.md "../APIReference/API_InputConfig.md"), [OutputConfig](../APIReference/API_OutputConfig.md "../APIReference/API_OutputConfig.md"), and [TargetPlatform](../APIReference/API_TargetPlatform.md "../APIReference/API_TargetPlatform.md") API operations in the SageMaker API
reference. 2. After you configure the JSON file, run the following command to create the compilation job:

```
aws sagemaker create-compilation-job \
--cli-input-json file://job.json \
--region us-west-2

# You should get CompilationJobArn
```

3. Describe the compilation job by running the following command:

```
aws sagemaker describe-compilation-job \
--compilation-job-name $JOB_NM \
--region us-west-2
```

4. Stop the compilation job by running the following command:

```
aws sagemaker stop-compilation-job \
--compilation-job-name $JOB_NM \
--region us-west-2

# There is no output for compilation-job operation
```

5. List the compilation job by running the following command:

```
aws sagemaker list-compilation-jobs \
--region us-west-2
```
