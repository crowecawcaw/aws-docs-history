# How Amazon SageMaker AI Provides

Training Information

This section explains how SageMaker AI makes training information, such as training data,
hyperparameters, and other configuration information, available to your Docker
container.

When you send a [`CreateTrainingJob`](../APIReference/API_CreateTrainingJob.md "../APIReference/API_CreateTrainingJob.md") request to SageMaker AI to start model training, you
specify the Amazon Elastic Container Registry (Amazon ECR) path of the Docker image that contains the training
algorithm. You also specify the Amazon Simple Storage Service (Amazon S3) location where training data is stored
and algorithm-specific parameters. SageMaker AI makes this information available to the Docker
container so that your training algorithm can use it. This section explains how we make
this information available to your Docker container. For information about creating a
training job, see `CreateTrainingJob`. For more information on the way that
SageMaker AI containers organize information, see [SageMaker Training and Inference Toolkits](amazon-sagemaker-toolkits.md "amazon-sagemaker-toolkits.md").

###### Topics

- [Hyperparameters](#your-algorithms-training-algo-running-container-hyperparameters "#your-algorithms-training-algo-running-container-hyperparameters")
- [Environment Variables](#your-algorithms-training-algo-running-container-environment-variables "#your-algorithms-training-algo-running-container-environment-variables")
- [Input Data Configuration](#your-algorithms-training-algo-running-container-inputdataconfig "#your-algorithms-training-algo-running-container-inputdataconfig")
- [Training Data](#your-algorithms-training-algo-running-container-trainingdata "#your-algorithms-training-algo-running-container-trainingdata")
- [Distributed Training Configuration](#your-algorithms-training-algo-running-container-dist-training "#your-algorithms-training-algo-running-container-dist-training")

## Hyperparameters

SageMaker AI makes the hyperparameters in a `CreateTrainingJob` request
available in the Docker container in the
`/opt/ml/input/config/hyperparameters.json` file.

The following is an example of a hyperparameter configuration in
`hyperparameters.json` to specify the `num_round` and
`eta` hyperparameters in the `CreateTrainingJob` operation
for [XGBoost](xgboost.md "xgboost.md").

```
{
    "num_round": "128",
    "eta": "0.001"
}
```

For a complete list of hyperparameters that can be used for the SageMaker AI built-in
XGBoost algorithm, see [XGBoost
Hyperparameters](xgboost_hyperparameters.md "xgboost_hyperparameters.md").

The hyperparameters that you can tune depend on the algorithm that you are
training. For a list of hyperparameters available for a SageMaker AI built-in algorithm,
find them listed in **Hyperparameters** under the
algorithm link in [Use Amazon SageMaker AI Built-in Algorithms or Pre-trained Models](algos.md "algos.md").

## Environment Variables

SageMaker AI sets the following environment variables in your container:

- TRAINING_JOB_NAME – Specified in the `TrainingJobName`
  parameter of the `CreateTrainingJob` request.
- TRAINING_JOB_ARN – The Amazon Resource Name (ARN) of the training
  job returned as the `TrainingJobArn` in the
  `CreateTrainingJob` response.
- All environment variables specified in the [Environment](../APIReference/API_CreateTrainingJob.md#sagemaker-CreateTrainingJob-request-Environment "../APIReference/API_CreateTrainingJob.md#sagemaker-CreateTrainingJob-request-Environment") parameter in the `CreateTrainingJob`
  request.

## Input Data Configuration

SageMaker AI makes the data channel information in the `InputDataConfig`
parameter from your `CreateTrainingJob` request available in the
`/opt/ml/input/config/inputdataconfig.json` file in your
Docker container.

For example, suppose that you specify three data channels (`train`,
`evaluation`, and `validation`) in your request. SageMaker AI
provides the following JSON:

```

{
  "train" : {"ContentType":  "trainingContentType",
             "TrainingInputMode": "File",
             "S3DistributionType": "FullyReplicated",
             "RecordWrapperType": "None"},
  "evaluation" : {"ContentType":  "evalContentType",
                  "TrainingInputMode": "File",
                  "S3DistributionType": "FullyReplicated",
                  "RecordWrapperType": "None"},
  "validation" : {"TrainingInputMode": "File",
                  "S3DistributionType": "FullyReplicated",
                  "RecordWrapperType": "None"}
}
```

###### Note

SageMaker AI provides only relevant information about each data channel (for example,
the channel name and the content type) to the container, as shown in the
previous example. `S3DistributionType` will be set as
`FullyReplicated` if you specify EFS or FSxLustre as input data
sources.

## Training Data

The `TrainingInputMode` parameter in the
`AlgorithmSpecification` of the [`CreateTrainingJob`](../APIReference/API_CreateTrainingJob.md "../APIReference/API_CreateTrainingJob.md") request specifies how the training
dataset is made available to your container. The following input modes are
available.

- **`File` mode**

If you use `File` mode as your `TrainingInputMode`
value, SageMaker AI sets the following parameters in your container.

    + Your `TrainingInputMode` parameter is written to
     `inputdataconfig.json` as "File".
    + Your data channel directory is written to
     `/opt/ml/input/data/`channel_name``.

If you use `File` mode, SageMaker AI creates a directory for each
channel. For example, if you have three channels named
`training`, `validation`, and `testing`,
SageMaker AI makes the following three directories in your Docker container:

    + `/opt/ml/input/data/training`
    + `/opt/ml/input/data/validation`
    + `/opt/ml/input/data/testing`

`File` mode also supports the following data sources.

    + Amazon Simple Storage Service (Amazon S3)
    + Amazon Elastic File System (Amazon EFS)
    + Amazon FSx for Lustre

###### Note

Channels that use file system data sources such as Amazon EFS and Amazon FSx
must use `File` mode. In this case, the directory path
provided in the channel is mounted at
`/opt/ml/input/data/`channel_name``.

- **`FastFile` mode**

If you use `FastFile` mode as your
`TrainingInputNodeParameter`, SageMaker AI sets the following
parameters in your container.

    + Similar to `File` mode, in `FastFile` mode,
     your `TrainingInputMode` parameter is written to
     `inputdataconfig.json` as "File".
    + Your data channel directory is written to
     `/opt/ml/input/data/`channel_name``.

`FastFile` mode supports the following data sources.

    + Amazon S3

If you use `FastFile` mode, the channel directory is mounted
with read-only permission.

Historically, `File` mode preceded `FastFile` mode.
To ensure backwards compatibility, algorithms that support `File`
mode can also seamlessly work with `FastFile` mode as long as the
`TrainingInputMode` parameter is set to `File` in
`inputdataconfig.json.`.

###### Note

Channels that use `FastFile` mode must use a
`S3DataType` of "S3Prefix".

`FastFile` mode presents a folder view that uses the
forward slash (`/`) as the delimiter for grouping Amazon S3
objects into folders. `S3Uri` prefixes must not correspond to
a partial folder name. For example, if an Amazon S3 dataset contains
`s3://amzn-s3-demo-bucket/train-01/data.csv`, then neither
`s3://amzn-s3-demo-bucket/train` nor
`s3://amzn-s3-demo-bucket/train-01` are allowed as
`S3Uri` prefixes.

A trailing forward slash is recommended to define a channel
corresponding to a folder. For example, the
`s3://amzn-s3-demo-bucket/train-01/` channel for the
`train-01` folder. Without the trailing forward slash,
the channel would be ambiguous if there existed another folder
`s3://amzn-s3-demo-bucket/train-011/` or file
`s3://amzn-s3-demo-bucket/train-01.txt/`.

- **`Pipe` mode**

      + `TrainingInputMode` parameter written to
       `inputdataconfig.json`: "Pipe"
      + Data channel directory in the Docker container:
       `/opt/ml/input/data/`channel_name_epoch_number``
      + Supported data sources: Amazon S3

  You need to read from a separate pipe for each channel. For example, if
  you have three channels named `training`,
  `validation`, and `testing`, you need to read from the
  following pipes:

      + `/opt/ml/input/data/training_0,
       /opt/ml/input/data/training_1, ...`
      + `/opt/ml/input/data/validation_0,
       /opt/ml/input/data/validation_1, ...`
      + `/opt/ml/input/data/testing_0, /opt/ml/input/data/testing_1,
       ...`

  Read the pipes sequentially. For example, if you have a channel called
  `training`, read the pipes in this sequence:

      1. Open `/opt/ml/input/data/training_0` in read
       mode and read it to end-of-file (EOF) or, if you are done with the
       first epoch, close the pipe file early.
      2. After closing the first pipe file, look for
       `/opt/ml/input/data/training_1` and read it
       until you have completed the second epoch, and so on.

  If the file for a given epoch doesn't exist yet, your code may need to
  retry until the pipe is created There is no sequencing restriction across
  channel types. For example, you can read multiple epochs for the
  `training` channel and only start reading the
  `validation` channel when you are ready. Or, you can read
  them simultaneously if your algorithm requires that.

For an example of a Jupyter notebook that shows how to use Pipe mode when
bringing your own container, see [Bring your own pipe-mode algorithm to Amazon SageMaker AI](https://github.com/aws/amazon-sagemaker-examples/blob/main/advanced_functionality/pipe_bring_your_own/pipe_bring_your_own.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/advanced_functionality/pipe_bring_your_own/pipe_bring_your_own.ipynb").

SageMaker AI model training supports high-performance S3 Express One Zone directory buckets as a
data input location for file mode, fast file mode, and pipe mode. To use
S3 Express One Zone, input the location of the S3 Express One Zone directory bucket instead of an
Amazon S3 general purpose bucket. Provide the ARN for the IAM role with the required
access control and permissions policy. Refer to [AmazonSageMakerFullAccesspolicy](../../../aws-managed-policy/latest/reference/AmazonSageMakerFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonSageMakerFullAccess.md") for details. You can only encrypt
your SageMaker AI output data in directory buckets with server-side encryption with Amazon S3
managed keys (SSE-S3). Server-side encryption with AWS KMS keys (SSE-KMS) is not
currently supported for storing SageMaker AI output data in directory buckets. For more information, see
[S3 Express One Zone](../../../AmazonS3/latest/userguide/s3-express-one-zone.md "../../../AmazonS3/latest/userguide/s3-express-one-zone.md").

## Distributed Training Configuration

If you're performing distributed training with multiple containers, SageMaker AI makes
information about all containers available in the
`/opt/ml/input/config/resourceconfig.json` file.

To enable inter-container communication, this JSON file contains information for
all containers. SageMaker AI makes this file available for both `File` and
`Pipe` mode algorithms. The file provides the following
information:

- `current_host`—The name of the current container on the
  container network. For example, `algo-1`. Host values can change
  at any time. Don't write code with specific values for this variable.
- `hosts`—The list of names of all containers on the
  container network, sorted lexicographically. For example,
  `["algo-1", "algo-2", "algo-3"]` for a three-node
  cluster. Containers can use these names to address other containers on the
  container network. Host values can change at any time. Don't write code with
  specific values for these variables.
- `network_interface_name`—The name of the network
  interface that is exposed to your container. For example, containers running
  the Message Passing Interface (MPI) can use this information to set the
  network interface name.
- Do not use the information in `/etc/hostname` or
  `/etc/hosts` because it might be inaccurate.
- Hostname information may not be immediately available to the algorithm
  container. We recommend adding a retry policy on hostname resolution
  operations as nodes become available in the cluster.

The following is an example file on node 1 in a three-node cluster:

```
{
    "current_host": "algo-1",
    "hosts": ["algo-1","algo-2","algo-3"],
    "network_interface_name":"eth1"
}
```
