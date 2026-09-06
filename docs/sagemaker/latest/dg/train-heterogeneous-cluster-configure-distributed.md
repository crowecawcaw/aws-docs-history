

# Run distributed training on a heterogeneous cluster in Amazon SageMaker AI
<a name="train-heterogeneous-cluster-configure-distributed"></a>

Through the `distribution` argument of the SageMaker AI ModelTrainer class, you can assign a specific instance group to run distributed training. For example, assume that you have the following two instance groups and want to run multi-GPU training on one of them. 

```
from sagemaker.instance_group import InstanceGroup

instance_group_1 = InstanceGroup("instance_group_1", "ml.c5.18xlarge", 1)
instance_group_2 = InstanceGroup("instance_group_2", "ml.p3dn.24xlarge", 2)
```

You can set the distributed training configuration for one of the instance groups. For example, the following code examples show how to assign `training_group_2` with two `ml.p3dn.24xlarge` instances to the distributed training configuration.

**Note**  
Currently, only one instance group of a heterogeneous cluster can be specified to the distribution configuration. In the SageMaker AI Python SDK v3, the `Torchrun` distributed configuration does not accept an instance group parameter and applies to all instances in the training job.

**With MPI**

**PyTorch**

```
from sagemaker.train import ModelTrainer
from sagemaker.train.distributed import Torchrun

# Note: In v3, Torchrun does not support scoping to a specific instance group.
# It applies to all instances in the training job. Use instance_groups with
# Channel/S3DataSource to control which group receives training data.
model_trainer = ModelTrainer(
    ...
    instance_groups=[{{instance_group_1}}, {{instance_group_2}}],
    distributed=Torchrun()
)
```

**TensorFlow**

```
from sagemaker.train import ModelTrainer
from sagemaker.train.distributed import Torchrun

# Note: In v3, Torchrun does not support scoping to a specific instance group.
# It applies to all instances in the training job. Use instance_groups with
# Channel/S3DataSource to control which group receives training data.
model_trainer = ModelTrainer(
    ...
    instance_groups=[{{instance_group_1}}, {{instance_group_2}}],
    distributed=Torchrun()
)
```

**With the SageMaker AI data parallel library**

**PyTorch**

```
from sagemaker.train import ModelTrainer
from sagemaker.train.distributed import Torchrun

model_trainer = ModelTrainer(
    ...
    instance_groups=[{{instance_group_1}}, {{instance_group_2}}],
    distributed=Torchrun()
)
```

**TensorFlow**

```
from sagemaker.train import ModelTrainer
from sagemaker.train.distributed import Torchrun

model_trainer = ModelTrainer(
    ...
    instance_groups=[{{instance_group_1}}, {{instance_group_2}}],
    distributed=Torchrun()
)
```

**Note**  
When using the SageMaker AI data parallel library, make sure the instance group consists of the [supported instance types by the library](https://docs.aws.amazon.com/sagemaker/latest/dg/distributed-data-parallel-support.html#distributed-data-parallel-supported-instance-types). 

For more information about the SageMaker AI data parallel library, see [SageMaker AI Data Parallel Training](https://docs.aws.amazon.com/sagemaker/latest/dg/data-parallel.html).

**With the SageMaker AI model parallel library**

**PyTorch**

```
from sagemaker.train import ModelTrainer
from sagemaker.train.distributed import Torchrun

model_trainer = ModelTrainer(
    ...
    instance_groups=[{{instance_group_1}}, {{instance_group_2}}],
    distributed=Torchrun()
)
```

**TensorFlow**

```
from sagemaker.train import ModelTrainer
from sagemaker.train.distributed import Torchrun

model_trainer = ModelTrainer(
    ...
    instance_groups=[{{instance_group_1}}, {{instance_group_2}}],
    distributed=Torchrun()
)
```

For more information about the SageMaker AI model parallel library, see [SageMaker AI Model Parallel Training](https://docs.aws.amazon.com/sagemaker/latest/dg/model-parallel.html).