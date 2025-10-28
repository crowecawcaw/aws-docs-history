# Managing storage paths for different

types of instance local storage

Consider the following when setting up storage paths for training jobs in SageMaker AI.

- If you want to store training artifacts for distributed training in the
  `/opt/ml/output/data` directory, you must properly append subdirectories or
  use unique file names for the artifacts through your model definition or training script.
  If the subdirectories and file names are not properly configured, all of the distributed
  training workers might write outputs to the same file name in the same output path in
  Amazon S3.
- If you use a custom training container, make sure you install the [SageMaker Training Toolkit](https://github.com/aws/sagemaker-training-toolkit "https://github.com/aws/sagemaker-training-toolkit")
  that helps set up the environment for SageMaker training jobs. Otherwise, you must specify the
  environment variables explicitly in your Dockerfile. For more information, see [Create a
  container with your own algorithms and models](docker-containers-create.md "docker-containers-create.md").
- When using an ML instance with [NVMe SSD
  volumes](../../../AWSEC2/latest/UserGuide/ssd-instance-store.md#nvme-ssd-volumes "../../../AWSEC2/latest/UserGuide/ssd-instance-store.md#nvme-ssd-volumes"), SageMaker AI doesn't provision Amazon EBS gp2 storage. Available storage is fixed to
  the NVMe-type instance's storage capacity. SageMaker AI configures storage paths for training
  datasets, checkpoints, model artifacts, and outputs to use the entire capacity of the
  instance storage. For example, ML instance families with the NVMe-type instance storage
  include `ml.p4d`, `ml.g4dn`, and `ml.g5`. When using an
  ML instance with the EBS-only storage option and without instance storage, you must define
  the size of EBS volume through the `volume_size` parameter in the SageMaker AI
  estimator class (or `VolumeSizeInGB` if you are using the
  `ResourceConfig` API). For example, ML instance families that use EBS volumes
  include `ml.c5` and `ml.p2`. To look up instance types and their
  instance storage types and volumes, see [Amazon EC2 Instance Types](https://aws.amazon.com/ec2/instance-types/ "https://aws.amazon.com/ec2/instance-types/").
- The default paths for SageMaker training jobs are mounted to Amazon EBS volumes or NVMe SSD
  volumes of the ML instance. When you adapt your training script to SageMaker AI, make sure that
  you use the default paths listed in the previous topic about [SageMaker AI environment variables and the
  default paths for training storage locations](model-train-storage-env-var-summary.md "model-train-storage-env-var-summary.md"). We recommend that you use the
  `/tmp` directory as a scratch space for temporarily storing any large objects
  during training. This means that you must not use directories that are mounted to small
  disk space allocated for system, such as `/user` and `/home`, to
  avoid out-of-space errors.
  To learn more, see the AWS machine learning blog [Choose the best data source for your Amazon SageMaker training job](https://aws.amazon.com/blogs/machine-learning/choose-the-best-data-source-for-your-amazon-sagemaker-training-job/ "https://aws.amazon.com/blogs/machine-learning/choose-the-best-data-source-for-your-amazon-sagemaker-training-job/") that further discusses
  case studies and performance benchmarks of data sources and input modes.
