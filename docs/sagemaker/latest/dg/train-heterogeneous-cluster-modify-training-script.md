# Modify your

training script to assign instance groups

With the heterogeneous cluster configuration in the previous sections, you have
prepared the SageMaker training environment and instances for your training job. To further
assign the instance groups to certain training and data processing tasks, the next step
is to modify your training script. By default, the training job simply makes training
script replicas for all nodes regardless the size of the instance, and this might lead
to performance loss.

For example, if you mix CPU instances and GPU instances in a heterogeneous cluster
while passing a deep neural network training script to the `entry_point`
argument of the SageMaker AI estimator, the `entry_point` script is replicated to
each instance. This means that, without proper task assignments, CPU instances also run
the entire script and start the training job that’s designed for distributed training on
GPU instances. Therefore, you must make changes in specific processing functions that
you want to offload and run on the CPU instances. You can use the SageMaker AI environment
variables to retrieve the information of the heterogeneous cluster and let specific
processes to run accordingly.

When your training job starts, your training script reads SageMaker training
environment information that includes heterogeneous cluster configuration. The
configuration contains information such as the current instance groups, the current
hosts in each group, and in which group the current host resides.

You can query instance group information during the initialization phase of a SageMaker AI
training job in the following ways.

**(Recommended) Reading instance group information with the
SageMaker training toolkit**

Use the environment Python module that the [SageMaker training toolkit
library](https://github.com/aws/sagemaker-training-toolkit "https://github.com/aws/sagemaker-training-toolkit") provides. The toolkit library is preinstalled in the [SageMaker framework containers](https://github.com/aws/deep-learning-containers/blob/master/available_images.md#sagemaker-framework-containers-sm-support-only "https://github.com/aws/deep-learning-containers/blob/master/available_images.md#sagemaker-framework-containers-sm-support-only") for TensorFlow and PyTorch, so you don’t
need an additional installation step when using the prebuilt containers. This is the
recommended way to retrieve the SageMaker AI environment variables with fewer code changes
in your training script.

```
from sagemaker_training import environment

env = environment.Environment()
```

Environment variables related to general SageMaker training and heterogeneous
clusters:

- `env.is_hetero` – Returns a Boolean result whether a
  heterogeneous cluster is configured or not.
- `env.current_host` – Returns the current host.
- `env.current_instance_type` – Returns the type of
  instance of the current host.
- `env.current_instance_group` – Returns the name of the
  current instance group.
- `env.current_instance_group_hosts` – Returns a list of
  hosts in current instance group.
- `env.instance_groups` – Returns a list of instance group
  names used for training.
- `env.instance_groups_dict` – Returns the entire
  heterogeneous cluster configuration of the training job.
- `env.distribution_instance_groups` – Returns a list of
  instance groups assigned to the `distribution` parameter of the
  SageMaker AI estimator class.
- `env.distribution_hosts` – Returns a list of hosts
  belonging to the instance groups assigned to the `distribution`
  parameter of the SageMaker AI estimator class.
  For example, consider the following example of a heterogeneous cluster that
  consists of two instance groups.

```
from sagemaker.instance_group import InstanceGroup

instance_group_1 = InstanceGroup(
    "instance_group_1", "ml.c5.18xlarge", 1)
instance_group_2 = InstanceGroup(
    "instance_group_2", "ml.p3dn.24xlarge", 2)
```

The output of `env.instance_groups_dict` of the example heterogeneous
cluster should be similar to the following.

```
{
    "instance_group_1": {
        "hosts": [
            "algo-2"
        ],
        "instance_group_name": "instance_group_1",
        "instance_type": "ml.c5.18xlarge"
    },
    "instance_group_2": {
        "hosts": [
            "algo-3",
            "algo-1"
        ],
        "instance_group_name": "instance_group_2",
        "instance_type": "ml.p3dn.24xlarge"
    }
}
```

**(Optional) Reading instance group information from the
resource configuration JSON file**

If you prefer to retrieve the environment variables in JSON format, you can
directly use the resource configuration JSON file. The JSON file in a SageMaker training
instance is located at `/opt/ml/input/config/resourceconfig.json` by
default.

```
file_path = '/opt/ml/input/config/resourceconfig.json'
config = read_file_as_json(file_path)
print(json.dumps(config, indent=4, sort_keys=True))
```
