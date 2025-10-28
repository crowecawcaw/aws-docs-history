# How Amazon SageMaker AI Processes Training

Output

As your algorithm runs in a container, it generates output including the status of the
training job and model and output artifacts. Your algorithm should write this
information to the following files, which are located in the container's
`/output` directory. Amazon SageMaker AI processes the information contained
in this directory as follows:

- `/opt/ml/model` – Your algorithm should write all
  final model artifacts to this directory. SageMaker AI copies this data as a single
  object in compressed tar format to the S3 location that you specified in
  the `CreateTrainingJob` request.

If multiple containers in a single training job write to this directory they
should ensure no `file/directory` names clash. SageMaker AI
aggregates the result in a TAR file and uploads to S3 at the end of the
training job.

- `/opt/ml/output/data` – Your algorithm should write
  artifacts you want to store other than the final model to this directory. SageMaker AI
  copies this data as a single object in compressed tar format to the S3 location
  that you specified in the `CreateTrainingJob` request. If multiple
  containers in a single training job write to this directory they should ensure
  no `file/directory` names clash. SageMaker AI aggregates the result in a TAR
  file and uploads to S3 at the end of the training job.
- `/opt/ml/output/failure` – If training fails, after
  all algorithm output (for example, logging) completes, your algorithm should
  write the failure description to this file. In a
  `DescribeTrainingJob` response, SageMaker AI returns the first 1024
  characters from this file as `FailureReason`.
  You can specify either an S3 general purpose or S3 directory bucket to store your training
  output. Directory buckets use only the Amazon S3 Express One Zone storage class, which is designed for workloads
  or performance-critical applications that require consistent single-digit millisecond
  latency. Choose the bucket type that best fits your application and performance
  requirements. For more information on S3 directory buckets, see [Directory
  buckets](../../../AmazonS3/latest/userguide/directory-buckets-overview.md "../../../AmazonS3/latest/userguide/directory-buckets-overview.md") in the _Amazon Simple Storage Service User Guide_.

###### Note

You can only encrypt your SageMaker AI output data in S3 directory buckets with server-side
encryption with Amazon S3 managed keys (SSE-S3). Server-side encryption with AWS KMS keys (SSE-KMS)
isn't currently supported for storing SageMaker AI output data in directory buckets.
