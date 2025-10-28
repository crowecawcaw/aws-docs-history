# Run distributed

training on a heterogeneous cluster in Amazon SageMaker AI

Through the `distribution` argument of the SageMaker AI estimator class, you can
assign a specific instance group to run distributed training. For example, assume that
you have the following two instance groups and want to run multi-GPU training on one of
them.

```
from sagemaker.instance_group import InstanceGroup

instance_group_1 = InstanceGroup("instance_group_1", "ml.c5.18xlarge", 1)
instance_group_2 = InstanceGroup("instance_group_2", "ml.p3dn.24xlarge", 2)
```

You can set the distributed training configuration for one of the instance groups. For
example, the following code examples show how to assign `training_group_2`
with two `ml.p3dn.24xlarge` instances to the distributed training
configuration.

###### Note

Currently, only one instance group of a heterogeneous cluster can be specified to
the distribution configuration.

**With MPI**

PyTorch

```
from sagemaker.`pytorch` import `PyTorch`

estimator = `PyTorch`(
    ...
    instance_groups=[`instance_group_1`, `instance_group_2`],
    distribution={
        "mpi": {
            "enabled": True, "processes_per_host": `8`
        },
        "instance_groups": [`instance_group_2`]
    }
)
```

TensorFlow

```
from sagemaker.`tensorflow` import `TensorFlow`

estimator = `TensorFlow`(
    ...
    instance_groups=[`instance_group_1`, `instance_group_2`],
    distribution={
        "mpi": {
            "enabled": True, "processes_per_host": `8`
        },
        "instance_groups": [`instance_group_2`]
    }
)
```

**With the SageMaker AI data parallel library**

PyTorch

```
from sagemaker.`pytorch` import `PyTorch`

estimator = `PyTorch`(
    ...
    instance_groups=[`instance_group_1`, `instance_group_2`],
    distribution={
        "smdistributed": {
            "dataparallel": {
                "enabled": True
            }
        },
        "instance_groups": [`instance_group_2`]
    }
)
```

TensorFlow

```
from sagemaker.`tensorflow` import `TensorFlow`

estimator = `TensorFlow`(
    ...
    instance_groups=[`instance_group_1`, `instance_group_2`],
    distribution={
        "smdistributed": {
            "dataparallel": {
                "enabled": True
            }
        },
        "instance_groups": [`instance_group_2`]
    }
)
```

###### Note

When using the SageMaker AI data parallel library, make sure the instance group consists
of the [supported instance types by the library](distributed-data-parallel-support.md#distributed-data-parallel-supported-instance-types "distributed-data-parallel-support.md#distributed-data-parallel-supported-instance-types").

For more information about the SageMaker AI data parallel library, see [SageMaker AI Data
Parallel Training](data-parallel.md "data-parallel.md").

**With the SageMaker AI model parallel library**

PyTorch

```
from sagemaker.`pytorch` import `PyTorch`

estimator = `PyTorch`(
    ...
    instance_groups=[`instance_group_1`, `instance_group_2`],
    distribution={
        "smdistributed": {
            "modelparallel": {
                "enabled":True,
                "parameters": {
                    ...   # SageMaker AI model parallel parameters
                }
            }
        },
        "instance_groups": [`instance_group_2`]
    }
)
```

TensorFlow

```
from sagemaker.`tensorflow` import `TensorFlow`

estimator = `TensorFlow`(
    ...
    instance_groups=[`instance_group_1`, `instance_group_2`],
    distribution={
        "smdistributed": {
            "modelparallel": {
                "enabled":True,
                "parameters": {
                    ...   # SageMaker AI model parallel parameters
                }
            }
        },
        "instance_groups": [`instance_group_2`]
    }
)
```

For more information about the SageMaker AI model parallel library, see [SageMaker AI Model
Parallel Training](model-parallel.md "model-parallel.md").
