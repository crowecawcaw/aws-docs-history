# Batch forecasting

Batch forecasting, also known as offline inferencing, generates model predictions on a
batch of observations. Batch inference is a good option for large datasets or if you don't
need an immediate response to a model prediction request.

By contrast, online inference (real-time inferencing) generates predictions in real
time.

You can use SageMaker APIs to retrieve the best candidate of an AutoML job and then submit a
batch of input data for inference using that candidate.

1. ###### Retrieve the details of the AutoML job.

The following AWS CLI command example uses the [DescribeAutoMLJobV2](../APIReference/API_DescribeAutoMLJobV2.md "../APIReference/API_DescribeAutoMLJobV2.md") API to obtain details of the AutoML job, including the
information about the best model candidate.

```
aws sagemaker describe-auto-ml-job-v2 --auto-ml-job-name `job-name` --region `region`
```

2. ###### Extract the container definition from [InferenceContainers](../APIReference/API_AutoMLCandidate.md#sagemaker-Type-AutoMLCandidate-InferenceContainers "../APIReference/API_AutoMLCandidate.md#sagemaker-Type-AutoMLCandidate-InferenceContainers") for the best model candidate.

A container definition is the containerized environment used to host the trained
SageMaker AI model for making predictions.

```
BEST_CANDIDATE=$(aws sagemaker describe-auto-ml-job-v2 \
      --auto-ml-job-name `job-name`
      --region `region` \
      --query 'BestCandidate.InferenceContainers[0]' \
      --output json
```

This command extracts the container definition for the best model candidate and
stores it in the `BEST_CANDIDATE` variable. 3. ###### Create a SageMaker AI model using the best candidate container definition.

Use the container definitions from the previous steps to create a SageMaker AI model by
using the [CreateModel](../APIReference/API_CreateModel.md "../APIReference/API_CreateModel.md")
API.

```
aws sagemaker create-model \
      --model-name '`model-name`' \
      --primary-container "$BEST_CANDIDATE"
      --execution-role-arn '`execution-role-arn>`' \
      --region '`region>`
```

The `--execution-role-arn` parameter specifies the IAM role that SageMaker AI
assumes when using the model for inference. For details on the permissions required for
this role, see [CreateModel API: Execution Role Permissions](../../../index.md "../../../index.md"). 4. ###### Create a batch transform job.

The following example creates a transform job using the [CreateTransformJob](../../../cli/latest/reference/sagemaker/create-transform-job.md "../../../cli/latest/reference/sagemaker/create-transform-job.md") API.

```
aws sagemaker create-transform-job \
       --transform-job-name '`transform-job-name`' \
       --model-name '`model-name`'\
       --transform-input file://transform-input.json \
       --transform-output file://transform-output.json \
       --transform-resources file://transform-resources.json \
       --region '`region`'
```

The input, output, and resource details are defined in separate JSON files:

    * `transform-input.json`:



    ```
    {
      "DataSource": {
        "S3DataSource": {
          "S3DataType": "S3Prefix",
          "S3Uri": "s3://my-input-data-bucket/path/to/input/data"
        }
      },
      "ContentType": "text/csv",
      "SplitType": "None"
    }
    ```
    * `transform-output.json`:



    ```
    {
      "S3OutputPath": "s3://my-output-bucket/path/to/output",
      "AssembleWith": "Line"
    }
    ```
    * `transform-resources.json`:


    ###### Note

    We recommend using [m5.12xlarge](https://aws.amazon.com/ec2/instance-types/m5/ "https://aws.amazon.com/ec2/instance-types/m5/") instances for general-purpose workloads and
     `m5.24xlarge` instances for big data forecasting tasks.



    ```
    {
      "InstanceType": "instance-type",
      "InstanceCount": 1
    }
    ```

5. ###### Monitor the progress of your transform job using the [DescribeTransformJob](../APIReference/API_DescribeTransformJob.md "../APIReference/API_DescribeTransformJob.md") API.

See the following AWS CLI command as an example.

```
aws sagemaker describe-transform-job \
      --transform-job-name '`transform-job-name`' \
      --region `region`
```

6. ###### Retrieve the batch transform output.

After the job is finished, the predicted result is available in the
`S3OutputPath`.

The output file name has the following format:
`input_data_file_name.out`. As an example, if your input file is
`text_x.csv`, the output name will be `text_x.csv.out`.

```
aws s3 ls `s3://my-output-bucket/path/to/output/`
```

The following code examples illustrate the use of the AWS SDK for Python (boto3) and
the AWS CLI for batch forecasting.

AWS SDK for Python (boto3)
The following example uses **AWS SDK for Python
(boto3)** to make predictions in batches.

```
import sagemaker
import boto3

session = sagemaker.session.Session()

sm_client = boto3.client('sagemaker', region_name='`us-west-2`')
role = '`arn:aws:iam::1234567890:role/sagemaker-execution-role`'
output_path = '`s3://test-auto-ml-job/output`'
input_data = '`s3://test-auto-ml-job/test_X.csv`'

best_candidate = sm_client.describe_auto_ml_job_v2(AutoMLJobName=job_name)['BestCandidate']
best_candidate_containers = best_candidate['InferenceContainers']
best_candidate_name = best_candidate['CandidateName']

# create model
reponse = sm_client.create_model(
    ModelName = best_candidate_name,
    ExecutionRoleArn = role,
    Containers = best_candidate_containers
)

# Lauch Transform Job
response = sm_client.create_transform_job(
    TransformJobName=f'{best_candidate_name}-transform-job',
    ModelName=model_name,
    TransformInput={
        'DataSource': {
            'S3DataSource': {
                'S3DataType': 'S3Prefix',
                'S3Uri': input_data
            }
        },
        'ContentType': "`text/csv`",
        'SplitType': 'None'
    },
    TransformOutput={
        'S3OutputPath': output_path,
        'AssembleWith': 'Line',
    },
    TransformResources={
        'InstanceType': '`ml.m5.2xlarge`',
        'InstanceCount': `1`,
    },
)
```

The batch inference job returns a response in the following format.

```
{'TransformJobArn': '`arn:aws:sagemaker:us-west-2:1234567890:transform-job/test-transform-job`',
 'ResponseMetadata': {'RequestId': '659f97fc-28c4-440b-b957-a49733f7c2f2',
  'HTTPStatusCode': 200,
  'HTTPHeaders': {'x-amzn-requestid': '659f97fc-28c4-440b-b957-a49733f7c2f2',
   'content-type': 'application/x-amz-json-1.1',
   'content-length': '96',
   'date': 'Thu, 11 Aug 2022 22:23:49 GMT'},
  'RetryAttempts': 0}}
```

AWS Command Line Interface (AWS CLI)

1. **Obtain the best candidate container
   definitions**.

```
aws sagemaker describe-auto-ml-job-v2 --auto-ml-job-name '`test-automl-job`' --region `us-west-2`
```

2. **Create the model**.

```
aws sagemaker create-model --model-name '`test-sagemaker-model`'
--containers '[{
    "Image": "348316444620.dkr.ecr.us-west-2.amazonaws.com/sagemaker-sklearn-automl:2.5-1-cpu-py3",
    "ModelDataUrl": "`s3://amzn-s3-demo-bucket/out/test-job1/data-processor-models/test-job1-dpp0-1-e569ff7ad77f4e55a7e549a/output/model.tar.gz`",
    "Environment": {
        "AUTOML_SPARSE_ENCODE_RECORDIO_PROTOBUF": "1",
        "AUTOML_TRANSFORM_MODE": "feature-transform",
        "SAGEMAKER_DEFAULT_INVOCATIONS_ACCEPT": "application/x-recordio-protobuf",
        "SAGEMAKER_PROGRAM": "sagemaker_serve",
        "SAGEMAKER_SUBMIT_DIRECTORY": "/opt/ml/model/code"
    }
}, {
    "Image": "348316444620.dkr.ecr.us-west-2.amazonaws.com/sagemaker-xgboost:1.3-1-cpu-py3",
    "ModelDataUrl": "`s3://amzn-s3-demo-bucket/out/test-job1/tuning/flicdf10v2-dpp0-xgb/test-job1E9-244-7490a1c0/output/model.tar.gz`",
    "Environment": {
        "MAX_CONTENT_LENGTH": "20971520",
        "SAGEMAKER_DEFAULT_INVOCATIONS_ACCEPT": "text/csv",
        "SAGEMAKER_INFERENCE_OUTPUT": "predicted_label",
        "SAGEMAKER_INFERENCE_SUPPORTED": "predicted_label,probability,probabilities"
    }
}, {
    "Image": "348316444620.dkr.ecr.us-west-2.amazonaws.com/sagemaker-sklearn-automl:2.5-1-cpu-py3",
    "ModelDataUrl": "`s3://amzn-s3-demo-bucket/out/test-job1/data-processor-models/test-job1-dpp0-1-e569ff7ad77f4e55a7e549a/output/model.tar.gz`",
    "Environment": {
        "AUTOML_TRANSFORM_MODE": "inverse-label-transform",
        "SAGEMAKER_DEFAULT_INVOCATIONS_ACCEPT": "text/csv",
        "SAGEMAKER_INFERENCE_INPUT": "predicted_label",
        "SAGEMAKER_INFERENCE_OUTPUT": "predicted_label",
        "SAGEMAKER_INFERENCE_SUPPORTED": "predicted_label,probability,labels,probabilities",
        "SAGEMAKER_PROGRAM": "sagemaker_serve",
        "SAGEMAKER_SUBMIT_DIRECTORY": "/opt/ml/model/code"
    }
}]' \
--execution-role-arn '`arn:aws:iam::1234567890:role/sagemaker-execution-role`' \
--region '`us-west-2`'
```

3. **Create a transform job**.

```
aws sagemaker create-transform-job --transform-job-name '`test-tranform-job`'\
 --model-name '`test-sagemaker-model`'\
 --transform-input '{
        "DataSource": {
            "S3DataSource": {
                "S3DataType": "S3Prefix",
                "S3Uri": "`s3://amzn-s3-demo-bucket/data.csv`"
            }
        },
        "ContentType": "`text/csv`",
        "SplitType": "None"
    }'\
--transform-output '{
        "S3OutputPath": "`s3://amzn-s3-demo-bucket/output/`",
        "AssembleWith": "Line"
    }'\
--transform-resources '{
        "InstanceType": "`ml.m5.2xlarge`",
        "InstanceCount": `1`
    }'\
--region '`us-west-2`'
```

4. **Check the progress of the transform job**.

```
aws sagemaker describe-transform-job --transform-job-name  '`test-tranform-job`' --region `us-west-2`
```

The following is the response from the transform job.

```
{
    "TransformJobName": "`test-tranform-job`",
    "TransformJobArn": "`arn:aws:sagemaker:us-west-2:1234567890:transform-job/test-tranform-job`",
    "TransformJobStatus": "InProgress",
    "ModelName": "`test-model`",
    "TransformInput": {
        "DataSource": {
            "S3DataSource": {
                "S3DataType": "S3Prefix",
                "S3Uri": "`s3://amzn-s3-demo-bucket/data.csv`"
            }
        },
        "ContentType": "`text/csv`",
        "CompressionType": "None",
        "SplitType": "None"
    },
    "TransformOutput": {
        "S3OutputPath": "`s3://amzn-s3-demo-bucket/output/`",
        "AssembleWith": "Line",
        "KmsKeyId": ""
    },
    "TransformResources": {
        "InstanceType": "`ml.m5.2xlarge`",
        "InstanceCount": `1`
    },
    "CreationTime": 1662495635.679,
    "TransformStartTime": 1662495847.496,
    "DataProcessing": {
        "InputFilter": "$",
        "OutputFilter": "$",
        "JoinSource": "None"
    }
}
```

After the `TransformJobStatus` changes to `Completed`,
you can check the inference result in the `S3OutputPath`.
