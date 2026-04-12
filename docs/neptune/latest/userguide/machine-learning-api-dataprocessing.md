# Data processing using the `dataprocessing` command

You use the Neptune ML `dataprocessing` command to create a data processing job,
check its status, stop it, or list all active data-processing jobs.

## Creating a data-processing job using the Neptune ML `dataprocessing` command

A typical Neptune ML `dataprocessing` command for creating a new job
looks like this:

AWS CLI

```
aws neptunedata start-ml-data-processing-job \
  --endpoint-url https://`your-neptune-endpoint`:`port` \
  --input-data-s3-location "s3://`(S3 bucket name)`/`(path to your input folder)`" \
  --id "`(a job ID for the new job)`" \
  --processed-data-s3-location "s3://`(S3 bucket name)`/`(path to your output folder)`"
```

For more information, see [start-ml-data-processing-job](../../../cli/latest/reference/neptunedata/start-ml-data-processing-job.md "../../../cli/latest/reference/neptunedata/start-ml-data-processing-job.md") in the AWS CLI Command Reference.

SDK

```
import boto3
from botocore.config import Config

client = boto3.client(
    'neptunedata',
    endpoint_url='https://`your-neptune-endpoint`:`port`',
    config=Config(read_timeout=None, retries={'total_max_attempts': 1})
)

response = client.start_ml_data_processing_job(
    inputDataS3Location='s3://`(S3 bucket name)`/`(path to your input folder)`',
    id='`(a job ID for the new job)`',
    processedDataS3Location='s3://`(S3 bucket name)`/`(path to your output folder)`'
)

print(response)
```

awscurl

```
awscurl https://`your-neptune-endpoint`:`port`/ml/dataprocessing \
  --region `us-east-1` \
  --service neptune-db \
  -X POST \
  -H 'Content-Type: application/json' \
  -d '{
        "inputDataS3Location" : "s3://`(S3 bucket name)`/`(path to your input folder)`",
        "id" : "`(a job ID for the new job)`",
        "processedDataS3Location" : "s3://`(S3 bucket name)`/`(path to your output folder)`"
      }'
```

###### Note

This example assumes that your AWS credentials are configured in your
environment. Replace `us-east-1` with the Region of your
Neptune cluster.

curl

```
curl \
  -X POST https://`your-neptune-endpoint`:`port`/ml/dataprocessing \
  -H 'Content-Type: application/json' \
  -d '{
        "inputDataS3Location" : "s3://`(S3 bucket name)`/`(path to your input folder)`",
        "id" : "`(a job ID for the new job)`",
        "processedDataS3Location" : "s3://`(S3 bucket name)`/`(path to your output folder)`"
      }'
```

A command to initiate incremental re-processing looks like this:

AWS CLI

```
aws neptunedata start-ml-data-processing-job \
  --endpoint-url https://`your-neptune-endpoint`:`port` \
  --input-data-s3-location "s3://`(S3 bucket name)`/`(path to your input folder)`" \
  --id "`(a job ID for this job)`" \
  --processed-data-s3-location "s3://`(S3 bucket name)`/`(path to your output folder)`" \
  --previous-data-processing-job-id "`(the job ID of a previously completed job to update)`"
```

For more information, see [start-ml-data-processing-job](../../../cli/latest/reference/neptunedata/start-ml-data-processing-job.md "../../../cli/latest/reference/neptunedata/start-ml-data-processing-job.md") in the AWS CLI Command Reference.

SDK

```
import boto3
from botocore.config import Config

client = boto3.client(
    'neptunedata',
    endpoint_url='https://`your-neptune-endpoint`:`port`',
    config=Config(read_timeout=None, retries={'total_max_attempts': 1})
)

response = client.start_ml_data_processing_job(
    inputDataS3Location='s3://`(S3 bucket name)`/`(path to your input folder)`',
    id='`(a job ID for this job)`',
    processedDataS3Location='s3://`(S3 bucket name)`/`(path to your output folder)`',
    previousDataProcessingJobId='`(the job ID of a previously completed job to update)`'
)

print(response)
```

awscurl

```
awscurl https://`your-neptune-endpoint`:`port`/ml/dataprocessing \
  --region `us-east-1` \
  --service neptune-db \
  -X POST \
  -H 'Content-Type: application/json' \
  -d '{
        "inputDataS3Location" : "s3://`(S3 bucket name)`/`(path to your input folder)`",
        "id" : "`(a job ID for this job)`",
        "processedDataS3Location" : "s3://`(S3 bucket name)`/`(path to your output folder)`",
        "previousDataProcessingJobId" : "`(the job ID of a previously completed job to update)`"
      }'
```

###### Note

This example assumes that your AWS credentials are configured in your
environment. Replace `us-east-1` with the Region of your
Neptune cluster.

curl

```
curl \
  -X POST https://`your-neptune-endpoint`:`port`/ml/dataprocessing \
  -H 'Content-Type: application/json' \
  -d '{
        "inputDataS3Location" : "s3://`(S3 bucket name)`/`(path to your input folder)`",
        "id" : "`(a job ID for this job)`",
        "processedDataS3Location" : "s3://`(S3 bucket name)`/`(path to your output folder)`",
        "previousDataProcessingJobId" : "`(the job ID of a previously completed job to update)`"
      }'
```

###### Parameters for `dataprocessing` job creation

- **`id`**   –  
  (_Optional_) A unique identifier for the new job.

_Type_: string. _Default_: An autogenerated UUID.

- **`previousDataProcessingJobId`**   –  
  (_Optional_) The job ID of a completed data processing job run on an earlier
  version of the data.

_Type_: string. _Default_: _none_.

_Note_: Use this for incremental data processing, to update the
model when graph data has changed (but not when data has been deleted).

- **`inputDataS3Location`**   –  
  (_Required_) The URI of the Amazon S3 location where you want SageMaker AI
  to download the data needed to run the data processing job.

_Type_: string.

- **`processedDataS3Location`**   –  
  (_Required_) The URI of the Amazon S3 location where you want SageMaker AI
  to save the results of a data processing job.

_Type_: string.

- **`sagemakerIamRoleArn`**   –  
  (_Optional_) The ARN of an IAM role for SageMaker AI execution.

_Type_: string. _Note_: This must be
listed in your DB cluster parameter group or an error will occur.

- **`neptuneIamRoleArn`**   –  
  (_Optional_) The Amazon Resource Name (ARN) of an IAM role that SageMaker AI
  can assume to perform tasks on your behalf.

_Type_: string. _Note_: This must be
listed in your DB cluster parameter group or an error will occur.

- **`processingInstanceType`**   –  
  (_Optional_) The type of ML instance used during data processing.
  Its memory should be large enough to hold the processed dataset.

_Type_: string. _Default_: the smallest
`ml.r5` type whose memory is ten times larger than the size of the exported
graph data on disk.

_Note_: Neptune ML can select the instance type automatically.
See [Selecting an instance for data processing](machine-learning-on-graphs-instance-selection.md#machine-learning-on-graphs-processing-instance-size "machine-learning-on-graphs-instance-selection.md#machine-learning-on-graphs-processing-instance-size").

- **`processingInstanceVolumeSizeInGB`**   –  
  (_Optional_) The disk volume size of the processing instance.
  Both input data and processed data are stored on disk, so the volume size must
  be large enough to hold both data sets.

_Type_: integer. _Default_: `0`.

_Note_: If not specified or 0, Neptune ML chooses the
volume size automatically based on the data size.

- **`processingTimeOutInSeconds`**   –  
  (_Optional_) Timeout in seconds for the data processing job.

_Type_: integer. _Default_: `86,400` (1 day).

- **`modelType`**   –  
  (_Optional_) One of the two model types that Neptune ML currently supports:
  heterogeneous graph models (`heterogeneous`), and knowledge graph (`kge`).

_Type_: string. _Default_: _none_.

_Note_: If not specified, Neptune ML chooses the
model type automatically based on the data.

- **`configFileName`**   –  
  (_Optional_) A data specification file that describes how to load
  the exported graph data for training. The file is automatically generated by the
  Neptune export toolkit.

_Type_: string. _Default_: `training-data-configuration.json`.

- **`subnets`**   –  
  (_Optional_) The IDs of the subnets in the Neptune VPC.

_Type_: list of strings. _Default_: _none_.

- **`securityGroupIds`**   –  
  (_Optional_) The VPC security group IDs.

_Type_: list of strings. _Default_: _none_.

- **`volumeEncryptionKMSKey`**   –  
  (_Optional_) The AWS Key Management Service (AWS KMS) key that SageMaker AI uses to
  encrypt data on the storage volume attached to the ML compute instances
  that run the processing job.

_Type_: string. _Default_: _none_.

- **`enableInterContainerTrafficEncryption`**   –  
  (_Optional_) Enable or disable inter-container traffic encryption in training or
  hyper-parameter tuning jobs.

_Type_: boolean. _Default_: _True_.

###### Note

The `enableInterContainerTrafficEncryption` parameter is only available in
[engine release 1.2.0.2.R3](engine-releases-1.2.0.2.R3.md "engine-releases-1.2.0.2.R3.md").

- **`s3OutputEncryptionKMSKey`**   –  
  (_Optional_) The AWS Key Management Service (AWS KMS) key that SageMaker AI uses to
  encrypt the output of the training job.

_Type_: string. _Default_: _none_.

## Getting the status of a data-processing job using the Neptune ML `dataprocessing` command

A sample Neptune ML `dataprocessing` command for the status of a job looks like this:

AWS CLI

```
aws neptunedata get-ml-data-processing-job \
  --endpoint-url https://`your-neptune-endpoint`:`port` \
  --id "`(the job ID)`"
```

For more information, see [get-ml-data-processing-job](../../../cli/latest/reference/neptunedata/get-ml-data-processing-job.md "../../../cli/latest/reference/neptunedata/get-ml-data-processing-job.md") in the AWS CLI Command Reference.

SDK

```
import boto3
from botocore.config import Config

client = boto3.client(
    'neptunedata',
    endpoint_url='https://`your-neptune-endpoint`:`port`',
    config=Config(read_timeout=None, retries={'total_max_attempts': 1})
)

response = client.get_ml_data_processing_job(
    id='`(the job ID)`'
)

print(response)
```

awscurl

```
awscurl https://`your-neptune-endpoint`:`port`/ml/dataprocessing/`(the job ID)` \
  --region `us-east-1` \
  --service neptune-db \
  -X GET
```

###### Note

This example assumes that your AWS credentials are configured in your
environment. Replace `us-east-1` with the Region of your
Neptune cluster.

curl

```
curl -s \
  "https://`your-neptune-endpoint`:`port`/ml/dataprocessing/`(the job ID)`" \
  | python -m json.tool
```

###### Parameters for `dataprocessing` job status

- **`id`**   –  
  (_Required_) The unique identifier of the data-processing job.

_Type_: string.

- **`neptuneIamRoleArn`**   –  
  (_Optional_) The ARN of an IAM role that provides Neptune access to
  SageMaker AI and Amazon S3 resources.

_Type_: string. _Note_: This must be
listed in your DB cluster parameter group or an error will occur.

## Stopping a data-processing job using the Neptune ML `dataprocessing` command

A sample Neptune ML `dataprocessing` command for stopping a job looks like this:

AWS CLI

```
aws neptunedata cancel-ml-data-processing-job \
  --endpoint-url https://`your-neptune-endpoint`:`port` \
  --id "`(the job ID)`"
```

To also clean up Amazon S3 artifacts:

```
aws neptunedata cancel-ml-data-processing-job \
  --endpoint-url https://`your-neptune-endpoint`:`port` \
  --id "`(the job ID)`" \
  --clean
```

For more information, see [cancel-ml-data-processing-job](../../../cli/latest/reference/neptunedata/cancel-ml-data-processing-job.md "../../../cli/latest/reference/neptunedata/cancel-ml-data-processing-job.md") in the AWS CLI Command Reference.

SDK

```
import boto3
from botocore.config import Config

client = boto3.client(
    'neptunedata',
    endpoint_url='https://`your-neptune-endpoint`:`port`',
    config=Config(read_timeout=None, retries={'total_max_attempts': 1})
)

response = client.cancel_ml_data_processing_job(
    id='`(the job ID)`',
    clean=True
)

print(response)
```

awscurl

```
awscurl https://`your-neptune-endpoint`:`port`/ml/dataprocessing/`(the job ID)` \
  --region `us-east-1` \
  --service neptune-db \
  -X DELETE
```

To also clean up Amazon S3 artifacts:

```
awscurl "https://`your-neptune-endpoint`:`port`/ml/dataprocessing/`(the job ID)`?clean=true" \
  --region `us-east-1` \
  --service neptune-db \
  -X DELETE
```

###### Note

This example assumes that your AWS credentials are configured in your
environment. Replace `us-east-1` with the Region of your
Neptune cluster.

curl

```
curl -s \
  -X DELETE "https://`your-neptune-endpoint`:`port`/ml/dataprocessing/`(the job ID)`"
```

Or this:

```
curl -s \
  -X DELETE "https://`your-neptune-endpoint`:`port`/ml/dataprocessing/`(the job ID)`?clean=true"
```

###### Parameters for `dataprocessing` stop job

- **`id`**   –  
  (_Required_) The unique identifier of the data-processing job.

_Type_: string.

- **`neptuneIamRoleArn`**   –  
  (_Optional_) The ARN of an IAM role that provides Neptune access to
  SageMaker AI and Amazon S3 resources.

_Type_: string. _Note_: This must be
listed in your DB cluster parameter group or an error will occur.

- **`clean`**   –  
  (_Optional_) This flag specifies that all Amazon S3 artifacts
  should be deleted when the job is stopped.

_Type_: Boolean. _Default_: `FALSE`.

## Listing active data-processing jobs using the Neptune ML `dataprocessing` command

A sample Neptune ML `dataprocessing` command for listing active jobs looks like this:

AWS CLI

```
aws neptunedata list-ml-data-processing-jobs \
  --endpoint-url https://`your-neptune-endpoint`:`port`
```

To limit the number of results:

```
aws neptunedata list-ml-data-processing-jobs \
  --endpoint-url https://`your-neptune-endpoint`:`port` \
  --max-items 3
```

For more information, see [list-ml-data-processing-jobs](../../../cli/latest/reference/neptunedata/list-ml-data-processing-jobs.md "../../../cli/latest/reference/neptunedata/list-ml-data-processing-jobs.md") in the AWS CLI Command Reference.

SDK

```
import boto3
from botocore.config import Config

client = boto3.client(
    'neptunedata',
    endpoint_url='https://`your-neptune-endpoint`:`port`',
    config=Config(read_timeout=None, retries={'total_max_attempts': 1})
)

response = client.list_ml_data_processing_jobs(
    maxItems=3
)

print(response)
```

awscurl

```
awscurl https://`your-neptune-endpoint`:`port`/ml/dataprocessing \
  --region `us-east-1` \
  --service neptune-db \
  -X GET
```

To limit the number of results:

```
awscurl "https://`your-neptune-endpoint`:`port`/ml/dataprocessing?maxItems=3" \
  --region `us-east-1` \
  --service neptune-db \
  -X GET
```

###### Note

This example assumes that your AWS credentials are configured in your
environment. Replace `us-east-1` with the Region of your
Neptune cluster.

curl

```
curl -s "https://`your-neptune-endpoint`:`port`/ml/dataprocessing"
```

Or this:

```
curl -s "https://`your-neptune-endpoint`:`port`/ml/dataprocessing?maxItems=3"
```

###### Parameters for `dataprocessing` list jobs

- **`maxItems`**   –  
  (_Optional_) The maximum number of items to return.

_Type_: integer. _Default_: `10`.
_Maximum allowed value_: `1024`.

- **`neptuneIamRoleArn`**   –  
  (_Optional_) The ARN of an IAM role that provides Neptune access to
  SageMaker AI and Amazon S3 resources.

_Type_: string. _Note_: This must be
listed in your DB cluster parameter group or an error will occur.
