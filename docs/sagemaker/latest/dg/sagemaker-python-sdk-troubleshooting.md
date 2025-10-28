# SageMaker Python SDK Troubleshooting

Guide

You can use the SageMaker Python SDK to interact with Amazon SageMaker AI within your Python scripts or
Jupyter notebooks. Despite the SDK providing a simplified workflow, you might encounter
various exceptions or errors. This troubleshooting guide aims to help you understand and
resolve common issues that might arise when working with the SageMaker Python SDK. It covers
scenarios related to creating training jobs, processing jobs, and endpoints, as well as
general exception handling practices. By following the guidance provided in the following
sections, you can effectively diagnose and address common issues.

The SageMaker Python SDK acts as a wrapper for the low level SageMaker API operations. The IAM
role that you're using to access the SDK must be able to access the underlying operations.
Adding the SageMaker AI Full Access Policy to your IAM role is the most straightforward way to
make sure you have permissions to use the SageMaker Python SDK. For more information about the
SageMaker AI Full Access Policy, see [Amazon SageMaker AI Full
Access](../../../aws-managed-policy/latest/reference/AmazonSageMakerFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonSageMakerFullAccess.md").

While less convenient, providing more granular permissions is a secure approach to using
the SDK. Each of the following sections has information about the permissions
required.

## Create a

Training Job

###### Important

If you're not adding the SageMaker AI Full Access policy to your IAM role, it must have
permissions to call the [CreateTrainingJob](../APIReference/API_CreateTrainingJob.md "../APIReference/API_CreateTrainingJob.md") and [DescribeTrainingJob](../APIReference/API_DescribeTrainingJob.md "../APIReference/API_DescribeTrainingJob.md") operations.

It also requires permissions to:

- Access input/output data in S3
- Run Amazon EC2 instances
- Log CloudWatch metrics
  If your SageMaker training job needs to access resources in an Amazon Virtual Private Cloud (Amazon VPC),
  make sure that you configure the necessary VPC settings and security groups when you
  create the processing job.

When you're creating a training job, you might run into `botocore.exceptions.ClientError` or `ValueError` exceptions.

ValueError
`ValueError` exceptions occur when there's an issue with the values or
parameters that you're passing to a function. Use the following list to see examples of
`ValueError` exceptions and how to fix them.

- `ValueError: either image_uri or algorithm_arn is required. None was
provided`:
  - If you're using the `AlgorithmEstimator` function, provide
    the `algorithm_arn`.
  - If you're using the `Estimator` function, provide the
    `estimator_arn`.

- `ValueError: Unknown input channel: train is not supported by:
scikit-decision-trees-15423055-57b73412d2e93e9239e4e16f83298b8f`

You get this error when you provide an invalid input channel. An input channel
is a data source or parameter that the model expects.

On the [Types of Algorithms](algorithms-choose.md "algorithms-choose.md")
page, you can navigate to the model to find information about the model's input
channels.

You can also find information about the input channels within the
**Usage** section on the AWS Marketplace page of the algorithm.

Use the following procedure to get information about an algorithm's input channels.

###### To get information about an algorithm's input channels

    1. Navigate to the [SageMaker AI console](https://console.aws.amazon.com/sagemaker "https://console.aws.amazon.com/sagemaker").
    2. On the left-hand navigation, choose **Training**.
    3. Select **Algorithms**.
    4. Choose **Find algorithm**.
    5. Find your algorithm in the resulting list.
    6. Select the **Usage** tab.
    7. Navigate to the **Channel specification** heading.

botocore.exceptions.ClientError
`botocore.exceptions.ClientError` exceptions occur when an underlying AWS service throws an
exception. This could be due to various reasons such as incorrect parameters,
permissions issues, or resource constraints. Use the following list for context on
`botocore.exceptions.ClientError` exceptions and information on how to fix them.

- `ResourceLimitExceeded` – Your AWS account doesn't have
  access to the Amazon EC2 instances needed to run the training job. To get access,
  request a quota increase. For information about quota increases, see [Service Quotas](../../../general/latest/gr/sagemaker.md#limits_sagemaker "../../../general/latest/gr/sagemaker.md#limits_sagemaker"). Use the following list for information about
  `botocore.exceptions.ClientError` exceptions.
- `ValidationException` – Validation exceptions come up when
  you've used the wrong Amazon EC2 instance type for the training job. They can also
  come up when the IAM role that you're using doesn't have permissions for the
  training job.

## Update a

Training Job

###### Important

If you're not adding the SageMaker AI Managed Policy to your IAM role, you must give the
role access to the following permissions:

- `s3:GetObject` – Provides permissions to read the model
  artifacts from Amazon S3 buckets
- `s3:PutObject` – If applicable, provides permissions to
  write updates to the model artifacts
- `iam:GetRole` – Provides permissions to get information
  about the IAM role needed to run the training job
- `sagemaker:UpdateTrainingJob` – Provides permissions to
  modify the training jobs using the [UpdateTrainingJob](../APIReference/API_UpdateTrainingJob.md "../APIReference/API_UpdateTrainingJob.md") operation.
- `logs:PutLogEvents` – Provides permissions to write
  logs to Amazon CloudWatch logs during the update process.

When you update a training job, you might run into a `botocore.exceptions.ParamValidationError` or a `botocore.exceptions.ClientError`.

botocore.exceptions.ClientError
The `ClientError` has the following message:

```

botocore.exceptions.ClientError: An error occurred (ValidationException) when calling the UpdateTrainingJob operation: Invalid UpdateTrainingJobRequest, the request cannot be empty

```

If you're running into this error, you must include one of the following parameters
along with the name of the training job:

- `profiler_rule_configs` (list) – A list of profiler rule
  configurations. By default, there are no profiler rule configurations.
- `profiler_config` (dict) – The configuration for SageMaker AI
  Profiler collects metrics and send them out. By default, there is no profiler
  configuration.
- `resource_config` (dict) – The configuration for the training
  job resources. You can update the keep-alive period if the warm pool status is
  `Available`. No other fields can be updated.
- `remote_debug_config` (dict) – Configuration for
  `RemoteDebug`. The dictionary can contain
  `EnableRemoteDebug`(bool).

botocore.exceptions.ParamValidationError
The `botocore.exceptions.ParamValidationError` has the following error:

```

botocore.exceptions.ParamValidationError: Parameter validation failed:
Invalid type for parameter ProfilerRuleConfigurations, value: {'DisableProfiler': False}, type: <class 'dict'>, valid types: <class 'list'>, <class 'tuple'>

```

This exception can occur if the parameter is not provided in the expected format by
the `update_training_job` function. For example, it expects the
`profiler_rule_configs` parameter to be a list. If the parameter is
passed as a dictionary instead, it raises the error.

## Create a

Processing Job

###### Important

If you're not adding the SageMaker AI Managed Policy to your IAM role, you must give the
role access to the following permissions:

- `sagemaker:CreateProcessingJob` – Provides permissions to
  create a processing job
- `sagemaker:DescribeProcessingJob` – Provides permissions
  to get information about a processing job
- `s3:GetObject` – Provides permissions to read the model
  artifacts from Amazon S3 buckets
- `s3:PutObject` – If applicable, provides permissions to
  write updates to the model artifacts
- `logs:PutLogEvents` – Provides permissions to writing
  logs to Amazon CloudWatch logs during the update process.
  If your processing job needs to access resources within an Amazon Virtual Private Cloud, you must
  specify its `security_group_ids` and `subnets` within the
  estimator that you create. For an example of how you can access resources within a
  Amazon VPC, see [Secure Training and Inference with VPC](https://sagemaker.readthedocs.io/en/stable/overview.html#secure-training-and-inference-with-vpc "https://sagemaker.readthedocs.io/en/stable/overview.html#secure-training-and-inference-with-vpc").

When you're creating a processing job, you might run into a `ValueError`, an
`UnexpectedStatusException`, or a `botocore.exceptions.ClientError`.

ValueError
The following is an example of a `ValueError`:

```

ValueError: code preprocess.py wasn't found. Please make sure that the file exists.

```

The path that you've specified wasn't correct. You can specify either a relative path
or an absolute path to your script file. For more information about specifying paths to
your files, see [sagemaker.processing.RunArgs](https://sagemaker.readthedocs.io/en/stable/api/training/processing.html#sagemaker.processing.RunArgs "https://sagemaker.readthedocs.io/en/stable/api/training/processing.html#sagemaker.processing.RunArgs").

UnexpectedStatusException
The following is an example of an `UnexpectedStatusException`:

```

UnexpectedStatusException: Error for Processing job sagemaker-scikit-learn-2024-07-02-14-08-55-993: Failed. Reason: AlgorithmError: , exit code: 1

```

The traceback accompanying the exception can help you identify the root cause:

```

Traceback (most recent call last):
  File "/opt/ml/processing/input/code/preprocessing.py", line 51, in <module>
    df = pd.read_csv(input_data_path)
  .
  .
  .
  File "pandas/_libs/parsers.pyx", line 689, in pandas._libs.parsers.TextReader._setup_parser_source
FileNotFoundError: [Errno 2] File b'/opt/ml/processing/input/census-income.csv' does not exist: b'/opt/ml/processing/input/census-income.csv'

```

The error `"FileNotFoundError: [Errno 2] File
 b'/opt/ml/processing/input/census-income.csv' does not exist"` indicates that
the input file `census-income.csv` is not found in the specified path
`/opt/ml/processing/input/`. Verify that the input data is correctly
provided and that the preprocessing script is copying the data to the expected
path.

botocore.exceptions.ClientError
The following is an example of a `botocore.exceptions.ClientError`:

```

botocore.exceptions.ClientError: An error occurred (ValidationException) when calling the CreateProcessingJob operation: RoleArn: Cross-account pass role is not allowed.

```

The `"Cross-account pass role is not allowed in create processing job"`
error occurs when you attempt to create a SageMaker Processing job using an IAM role from a
different AWS account. This security feature ensures roles and permissions are managed
within each account. To resolve the issue, do the following:

1. Verify the IAM role is in the same account as the processing job.
   Cross-account roles require explicit allowance
2. If using a role from another account, update its trust policy to allow the
   account creating the processing job to assume the role.
3. Ensure the role has necessary permissions for processing jobs, such as
   `sagemaker:CreateProcessingJob` or
   `iam:PassRole`.

## Create an

Endpoint

###### Important

If you're not adding the SageMaker AI Managed Policy to your IAM role, you must give the
role access to the following permissions:

- `sagemaker:CreateModel` – Provides permissions to create
  the model that you're deploying to the endpoint
- `sagemaker:CreateEndpointConfig` – Provides permissions
  to create an endpoint configuration that define the endpoint's behavior,
  such as the instance type and count
- `sagemaker:CreateEndpoint` – Provides permissions to
  create the endpoint configuration using the endpoint that you've
  specified
  Additionally, you need permissions to describe and list the models, endpoints, and
  endpoint configurations.

When you're creating an endpoint, you might run into an
`UnexpectedStatusException` or a `botocore.exceptions.ClientError`.

The following is an example of an `UnexpectedStatusException`:

```

UnexpectedStatusException: Error hosting endpoint gpt2-large-2024-07-03-15-28-20-448: Failed. Reason: The primary container for production variant AllTraffic did not pass the ping health check. Please check CloudWatch logs for this endpoint.. Try changing the instance type or reference the troubleshooting page https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference-troubleshooting.html

```

The error message tells you to check the Amazon CloudWatch logs. Use the following procedure to check the logs.

###### To check the CloudWatch logs

1. Navigate to the [Amazon SageMaker AI console](https://console.aws.amazon.com/sagemaker "https://console.aws.amazon.com/sagemaker").
2. On the left hand navigation, choose **Endpoints**.
3. Select the endpoint that has failed.
4. On the **Endpoint details** page, choose **View logs in CloudWatch**.

After you've found the logs, look for the specific issue. The following is an example of a CloudWatch log:

```

NotImplementedError: gptq quantization is not supported for AutoModel, you can try to quantize it with text-generation-server quantize ORIGINAL_MODEL_ID NEW_MODEL_ID

```

For information about resolving the `botocore.exceptions.ClientError`, see [Guidance on exception handling](#sagemaker-python-sdk-troubleshooting-exception-handling "#sagemaker-python-sdk-troubleshooting-exception-handling").

## Update an

Endpoint

###### Important

If you're not adding the SageMaker AI Managed Policy to your IAM role, you must give the
role access to the following permissions:

- `sagemaker:UpdateEndpoint` – Provides permissions to update an existing endpoint, such as changing the endpoint's instance type or count
- `sagemaker:UpdateEndpointWeightsAndCapacities` – Provides permissions
  to create an endpoint configuration that define the endpoint's behavior,
  such as the instance type and count
- `sagemaker:DescribeEndpoint` – Provides permissions to
  describe the current configuration of the endpoint, which is often required before the update
  Additionally, you might need permissions to describe and list the endpoints and
  endpoint configurations.

You can run into a `ValueError`, such as the following:

```

ValueError: Endpoint with name 'abc' does not exist; please use an existing endpoint name

```

The error indicates that the specified endpoint name does not match any existing endpoints in your AWS account. Use the following procedure to troubleshoot the error:

###### To troubleshoot a Value Error

1. Use the following code to list all of your endpoints:

```
import sagemaker
sagemaker_session = sagemaker.Session()
# List all endpoints
endpoints = sagemaker_session.sagemaker_client.list_endpoints()
print(endpoints)

```

2. Verify that the endpoint you've specified to the `update_endpoint` function is in the list.
3. Make sure that you're operating in the correct AWS Region. SageMaker AI endpoints are region-specific.
4. Make sure that the IAM role that you're using has permissions to list, describe, or update the endpoints.

## Guidance on exception handling

If you can't find information to help you fix your specific issue, the following code examples can give you inspiration for how you handle exceptions.

The following is a generic example that you can use to catch most exceptions.

```
import sagemaker
from botocore.exceptions import ParamValidationError, ClientError

try:
    sagemaker.some_api_call(SomeParam='some_param')

except ClientError as error:
    # Put your error handling logic here
    raise error

except ParamValidationError as error:
    raise ValueError('The parameters you provided are incorrect: {}'.format(error))

except ValueError as error:
    # Catch generic ValueError exceptions

```

There are two main categories of errors:

- Errors specific to the SageMaker Python SDK
- Errors specific to the underlying AWS service

Errors specific to the underlying AWS service are always `botocore.exceptions.ClientError` exceptions. The `botocore.exceptions.ClientError` has an `Error` object and a `ResponseMetadata` object. The following shows the template of a client error:

```
{
    'Error': {
        'Code': 'SomeServiceException',
        'Message': 'Details/context around the exception or error'
    },
    'ResponseMetadata': {
        'RequestId': '1234567890ABCDEF',
        'HostId': 'host ID data will appear here as a hash',
        'HTTPStatusCode': 400,
        'HTTPHeaders': {'header metadata key/values will appear here'},
        'RetryAttempts': 0
    }
}


```

The following is an example of the specific error handling that you can do with the `botocore.exceptions.ClientError`:

```
try:
    sagemaker.some_api_call(SomeParam='some_param')

except botocore.exceptions.ClientError as err:
    if err.response['Error']['Code'] == 'InternalError': # Generic error
        # We grab the message, request ID, and HTTP code to give to customer support
        print('Error Message: {}'.format(err.response['Error']['Message']))
        print('Request ID: {}'.format(err.response['ResponseMetadata']['RequestId']))
        print('Http code: {}'.format(err.response['ResponseMetadata']['HTTPStatusCode']))
        raise err
    else if err.response['Error']['Code'] == 'ValidationException':
       raise ValueError(err.response['Error']['Message'])


```

For more information about how you can handle `ClientError` exceptions, see [Parsing error responses and catching exceptions from AWS services](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/error-handling.html#parsing-error-responses-and-catching-exceptions-from-aws-services "https://boto3.amazonaws.com/v1/documentation/api/latest/guide/error-handling.html#parsing-error-responses-and-catching-exceptions-from-aws-services").
