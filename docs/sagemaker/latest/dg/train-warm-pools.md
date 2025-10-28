# SageMaker AI Managed Warm Pools

SageMaker AI managed warm pools let you retain and reuse provisioned infrastructure after the
completion of a training job to reduce latency for repetitive workloads, such as iterative
experimentation or running many jobs consecutively. Subsequent training jobs that match
specified parameters run on the retained warm pool infrastructure, which speeds up start
times by reducing the time spent provisioning resources.

###### Important

SageMaker AI managed warm pools are a billable resource. For more information, see [Billing](#train-warm-pools-billing "#train-warm-pools-billing").

###### Topics

- [How it works](#train-warm-pools-how-it-works "#train-warm-pools-how-it-works")
- [Considerations](#train-warm-pools-considerations "#train-warm-pools-considerations")
- [Request a warm pool quota increase](train-warm-pools-resource-limits.md "train-warm-pools-resource-limits.md")
- [Use SageMaker AI managed warm pools](train-warm-pools-how-to-use.md "train-warm-pools-how-to-use.md")

## How it works

To use SageMaker AI managed warm pools and reduce latency between similar consecutive training
jobs, create a training job that specifies a `KeepAlivePeriodInSeconds` value
in its `ResourceConfig`. This value represents the duration of time in
seconds to retain configured resources in a warm pool for subsequent training jobs. If
you need to run several training jobs using similar configurations, you can further
reduce latency and billable time by using a dedicated persistent cache directory to
store and re-use your information in a different job.

###### Topics

- [Warm pool lifecycle](#train-warm-pools-lifecycle "#train-warm-pools-lifecycle")
- [Warm pool creation](#train-warm-pools-creation "#train-warm-pools-creation")
- [Matching training jobs](#train-warm-pools-matching-criteria "#train-warm-pools-matching-criteria")
- [Maximum warm pool
  duration](#train-warm-pools-maximum-duration "#train-warm-pools-maximum-duration")
- [Using persistent cache](#train-warm-pools-persistent-cache "#train-warm-pools-persistent-cache")
- [Billing](#train-warm-pools-billing "#train-warm-pools-billing")

### Warm pool lifecycle

1. Create an initial training job with a
   `KeepAlivePeriodInSeconds` value greater than 0. When you run
   this first training job, this “cold-starts” a cluster with typical startup
   times.
2. When the first training job completes, the provisioned resources are kept
   alive in a warm pool for the period specified in the
   `KeepAlivePeriodInSeconds` value. As long as the cluster is
   healthy and the warm pool is within the specified
   `KeepAlivePeriodInSeconds`, then the warm pool status is
   `Available`.
3. The warm pool stays `Available` until it either identifies a
   matching training job for reuse or it exceeds the specified
   `KeepAlivePeriodInSeconds` and is terminated. The maximum
   length of time allowed for the `KeepAlivePeriodInSeconds` is 3600
   seconds (60 minutes). If the warm pool status is `Terminated`,
   then this is the end of the warm pool lifecycle.
4. If the warm pool identifies a second training job with matching
   specifications such as instance count or instance type, then the warm pool
   moves from the first training job to the second training job for reuse. The
   status of the first training job warm pool becomes `Reused`. This
   is the end of the warm pool lifecycle for the first training job.
5. The status of the second training job that reused the warm pool becomes
   `InUse`. After the second training job completes, the warm
   pool is `Available` for the `KeepAlivePeriodInSeconds`
   duration specified in the second training job. A warm pool can continue
   moving to subsequent matching training jobs for a maximum of 28 days.
6. If the warm pool is no longer available to reuse, the warm pool status is
   `Terminated`. Warm pools are no longer available if they are
   terminated by a user, for a patch update, or for exceeding the specified
   `KeepAlivePeriodInSeconds`.

For more information on warm pool status options, see [WarmPoolStatus](../APIReference/API_WarmPoolStatus.md "../APIReference/API_WarmPoolStatus.md") in the _Amazon SageMaker API
Reference_.

### Warm pool creation

If an initial training job successfully completes and has a
`KeepAlivePeriodInSeconds` value greater than 0, this creates a warm
pool. If you stop a training job after a cluster is already launched, a warm pool is
still retained. If the training job fails due to an algorithm or client error, a
warm pool is still retained. If the training job fails for any other reason that
might compromise the health of the cluster, then the warm pool is not created.

To verify successful warm pool creation, check the warm pool status of your
training job. If a warm pool successfully provisions, the warm pool status is
`Available`. If a warm pool fails to provision, the warm pool status
is `Terminated`.

### Matching training jobs

For a warm pool to persist, it must find a matching training job within the time
specified in the `KeepAlivePeriodInSeconds` value. The next training job
is a match if the following values are identical:

- `RoleArn`
- `ResourceConfig` values:
  - `InstanceCount`
  - `InstanceType`
  - `VolumeKmsKeyId`
  - `VolumeSizeInGB`

- `VpcConfig` values:
  - `SecurityGroupIds`
  - `Subnets`

- `EnableInterContainerTrafficEncryption`
- `EnableNetworkIsolation`
- If you passed [session tags](../../../IAM/latest/UserGuide/id_session-tags.md#id_session-tags_operations "../../../IAM/latest/UserGuide/id_session-tags.md#id_session-tags_operations") for your training job with
  `EnableSessionTagChaining` set to `True` in the
  training job's `SessionChainingConfig`, then a matching training
  job must also set `EnableSessionTagChaining` to `True`
  and have identical session keys. For more information, see [Use attribute-based access control (ABAC)
  for multi-tenancy training](model-access-training-data-abac.md "model-access-training-data-abac.md").

All of these values must be the same for a warm pool to move to a subsequent
training job for reuse.

### Maximum warm pool

duration

The maximum `KeepAlivePeriodInSeconds` for a single training job is
3600 seconds (60 minutes) and the maximum length of time that a warm pool cluster
can continue running consecutive training jobs is 28 days.

Each subsequent training job must also specify a
`KeepAlivePeriodInSeconds` value. When the warm pool moves to the
next training job, it inherits the new `KeepAlivePeriodInSeconds` value
specified in that training job’s `ResourceConfig`. In this way, you can
keep a warm pool moving from training job to training job for a maximum of 28
days.

If no `KeepAlivePeriodInSeconds` is specified, then the warm pool spins
down after the training job completes.

### Using persistent cache

When you create a warm pool, SageMaker AI mounts a special directory on the volume that
will persist throughout the lifecycle of the warm pool. This directory can also be
used to store information that you want to re-use in another job.

Using persistent cache can reduce latency and billable time over using warm pools
alone for jobs that require the following:

- multiple interactions with similar configurations
- incremental training jobs
- hyperparameter optimization

For example, you can avoid downloading the same Python dependencies on repeated
runs by setting up a pip cache directory inside the persistent cache directory. You
are fully responsible for managing the contents of this directory. The following are
examples of types of information that you can put in your persistent cache to help
reduce your latency and billable time.

- Dependencies managed by pip.
- Dependencies managed by conda.
- [Checkpoint
  information](model-checkpoints.md "model-checkpoints.md").
- Any additional information generated during training.

The location of the persistent cache is
`/opt/ml/sagemaker/warmpoolcache`. The environment variable
`SAGEMAKER_MANAGED_WARMPOOL_CACHE_DIRECTORY` points to the location
of the persistent cache directory.

The following code example shows you how to set up a warm pool and use persistent
cache to store your pip dependencies for use in a subsequent job. The subsequent job
must run within the time frame given by the parameter
`keep_alive_period_in_seconds`.

```
import sagemakerfrom sagemaker import get_execution_rolefrom sagemaker.tensorflow import TensorFlow
# Creates a SageMaker session and gets execution role
session = sagemaker.Session()
role = get_execution_role()
# Creates an example estimator
estimator = TensorFlow(
    ...
    entry_point='`my-training-script.py`',
    source_dir='`code`',
    role=`role`,
    model_dir='`model_dir`',
    framework_version='`2.2`',
    py_version='`py37`',
    job_name='`my-training-job-1`',
    instance_type='`ml.g4dn.xlarge`',
    instance_count=`1`,
    volume_size=`250`,
    hyperparameters={
"batch-size": `512`,
        "epochs": `1`,
        "learning-rate": `1e-3`,
        "beta_1": `0.9`,
        "beta_2": `0.999`,
    },
    keep_alive_period_in_seconds=`1800`,
    environment={"PIP_CACHE_DIR": "/opt/ml/sagemaker/warmpoolcache/pip"}
)
```

In the previous code example, using the [environment](https://sagemaker.readthedocs.io/en/stable/api/training/estimators.html#estimators "https://sagemaker.readthedocs.io/en/stable/api/training/estimators.html#estimators") parameter exports the environment variable
`PIP_CACHE_DIRECTORY` to point to the directory
`/opt/ml/sagemaker/warmpoolcache/pip`. Exporting this environment
variable will change where pip stores its cache to the new location. Any directory,
including nested directories, that you create inside the persistent cache directory
will be available for re-use during a subsequent training run. In the previous code
example, a directory called `pip` is changed to be the default location
to cache any dependencies installed using pip.

The persistent cache location may also be accessed from within your Python
training script using the environment variable as shown in the following code
example.

```
import os
import shutil
if __name__ == '__main__':
    PERSISTED_DIR = os.environ["SAGEMAKER_MANAGED_WARMPOOL_CACHE_DIRECTORY"]

    # create a file to be persisted
    open(os.path.join(PERSISTED_DIR, "`test.txt`"), 'a').close()
    # create a directory to be persisted
    os.mkdir(os.path.join(PERSISTED_DIR, "`test_dir`"))

    # Move a file to be persisted
    shutil.move("`path/of/your/file.txt`", PERSISTED_DIR)
```

### Billing

SageMaker AI managed warm pools are a billable resource. Retrieve the warm pool status for
your training job to check the billable time for your warm pools. You can check the
warm pool status either through the [Using the Amazon SageMaker AI
console](train-warm-pools-how-to-use.md#train-warm-pools-how-to-use-sagemaker-console "train-warm-pools-how-to-use.md#train-warm-pools-how-to-use-sagemaker-console") or directly
through the [DescribeTrainingJob](../APIReference/API_DescribeTrainingJob.md "../APIReference/API_DescribeTrainingJob.md") API command. For more information, see [WarmPoolStatus](../APIReference/API_WarmPoolStatus.md "../APIReference/API_WarmPoolStatus.md") in the _Amazon SageMaker API
Reference_.

###### Note

After the time specified by the parameter
`KeepAlivePeriodInSeconds` has ended, both the warm pool and
persistent cache will shut down, and the contents will be deleted.

## Considerations

Consider the following items when using SageMaker AI managed warm pools.

- SageMaker AI managed warm pools cannot be used with heterogeneous cluster training.
- SageMaker AI managed warm pools cannot be used with spot instances.
- SageMaker AI managed warm pools are limited to a `KeepAlivePeriodInSeconds`
  value of 3600 seconds (60 minutes).
- If a warm pool continues to successfully match training jobs within the
  specified `KeepAlivePeriodInSeconds` value, the cluster can only
  continue running for a maximum of 28 days.
