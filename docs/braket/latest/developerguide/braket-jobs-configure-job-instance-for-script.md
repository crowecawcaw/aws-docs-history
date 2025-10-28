# Configure your hybrid job instance

Depending on your algorithm, you may have different requirements. By default,
Amazon Braket runs your algorithm script on an `ml.m5.large`
instance. However, you can customize this instance type when you create a hybrid job using the
following import and configuration argument.

```
from braket.jobs.config import InstanceConfig

job = AwsQuantumJob.create(
    ...
    instance_config=InstanceConfig(instanceType="ml.p3.8xlarge"), # Use NVIDIA Tesla V100 instance with 4 GPUs.
    ...
    ),
```

If you are running an embedded simulation and have specified a local device in the
device configuration, you can additionally request more than one instance in
the `InstanceConfig` by specifying the `instanceCount` and setting it to be greater than one.
The upper limit is 5. For instance, you can choose 3 instances as follows.

```
from braket.jobs.config import InstanceConfig
job = AwsQuantumJob.create(
    ...
    instance_config=InstanceConfig(instanceType="ml.p3.8xlarge", instanceCount=3), # Use 3 NVIDIA Tesla V100
    ...
    ),
```

When you use multiple instances, consider distributing your hybrid job using the data parallel
feature. See the following example notebook for more details on how-to see this [Parallelize training for QML](https://github.com/amazon-braket/amazon-braket-examples/blob/main/examples/hybrid_jobs/5_Parallelize_training_for_QML/Parallelize_training_for_QML.ipynb "https://github.com/amazon-braket/amazon-braket-examples/blob/main/examples/hybrid_jobs/5_Parallelize_training_for_QML/Parallelize_training_for_QML.ipynb") example.

The following three tables list the available instance types and specs for standard,
high performance, and GPU accelerated instances.

###### Note

To view the default classical compute instance quotas for Hybrid Jobs, see the [Amazon Braket Quotas](braket-quotas.md "braket-quotas.md") page.

| Standard Instances         | vCPU | Memory (GiB) |
| -------------------------- | ---- | ------------ | ------------ | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ml.m5.large (default)      | 4    | 16           |
| ml.m5.xlarge               | 4    | 16           |
| ml.m5.2xlarge              | 8    | 32           |
| ml.m5.4xlarge              | 16   | 64           |
| ml.m5.12xlarge             | 48   | 192          |
| ml.m5.24xlarge             | 96   | 384          |
| High performance Instances | vCPU | Memory (GiB) |
| ---                        | ---  | ---          |
| ml.c5.xlarge               | 4    | 8            |
| ml.c5.2xlarge              | 8    | 16           |
| ml.c5.4xlarge              | 16   | 32           |
| ml.c5.9xlarge              | 36   | 72           |
| ml.c5.18xlarge             | 72   | 144          |
| ml.c5n.xlarge              | 4    | 10.5         |
| ml.c5n.2xlarge             | 8    | 21           |
| ml.c5n.4xlarge             | 16   | 32           |
| ml.c5n.9xlarge             | 36   | 72           |
| ml.c5n.18xlarge            | 72   | 192          |
| GPU accelerated Instances  | GPUs | vCPU         | Memory (GiB) | GPU Memory (GiB) |
| ---                        | ---  | ---          | ---          | ---              |
| ml.p3.2xlarge              | 1    | 8            | 61           | 16               |
| ml.p3.8xlarge              | 4    | 32           | 244          | 64               |
| ml.p3.16xlarge             | 8    | 64           | 488          | 128              |
| ml.p4d.24xlarge            | 8    | 96           | 1152         | 320              |
| ml.g4dn.xlarge             | 1    | 4            | 16           | 16               |
| ml.g4dn.2xlarge            | 1    | 8            | 32           | 16               |
| ml.g4dn.4xlarge            | 1    | 16           | 64           | 16               |
| ml.g4dn.8xlarge            | 1    | 32           | 128          | 16               |
| ml.g4dn.12xlarge           | 4    | 48           | 192          | 64               |
| ml.g4dn.16xlarge           | 1    | 64           | 256          | 16               | ###### Note p3 instances are not available in us-west-1. If your hybrid job is unable to provision requested ML compute capacity, use another Region. Each instance uses a default configuration of data storage (SSD) of 30 GB. But you can adjust the storage in the same way that you configure the `instanceType`. The following example shows how to increase the total storage to 50 GB. `from braket.jobs.config import InstanceConfig job = AwsQuantumJob.create( ... instance_config=InstanceConfig( instanceType="ml.p3.8xlarge", volumeSizeInGb=50, ), ... ),` ## Configure the default bucket in `AwsSession` Utilizing your own `AwsSession` instance provides you with enhanced flexibility, such as the ability to specify a custom location for your default Amazon S3 bucket. By default, an `AwsSession` has a pre-configured Amazon S3 bucket location of `"amazon-braket-{id}-{region}"`. However, you have the option to override the default Amazon S3 bucket location when creating an `AwsSession`. Users can optionally pass in an `AwsSession` object into the `AwsQuantumJob.create()` method, by providing the `aws_session` parameter as demonstrated in the following code example. `aws_session = AwsSession(default_bucket="amazon-braket-s3-demo-bucket") # Then you can use that AwsSession when creating a hybrid job job = AwsQuantumJob.create( ... aws_session=aws_session )` |
