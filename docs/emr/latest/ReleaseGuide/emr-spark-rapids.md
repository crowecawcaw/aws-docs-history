# Use the Nvidia RAPIDS Accelerator for Apache

Spark

With Amazon EMR release 6.2.0 and later, you can use the [RAPIDS Accelerator for Apache
Spark](https://docs.nvidia.com/spark-rapids/user-guide/latest/overview.html "https://docs.nvidia.com/spark-rapids/user-guide/latest/overview.html") plugin by Nvidia to accelerate Spark using EC2 graphics processing
unit (GPU) instance types. RAPIDS Accelerator will GPU-accelerate your Apache Spark 3.0
data science pipelines without code changes, and speed up data processing and model
training while substantially lowering infrastructure costs.

The following sections guide you through configuring your EMR cluster to use the
Spark-RAPIDS Plugin for Spark.

## Choose instance types

To use the Nvidia Spark-RAPIDS plugin for Spark, the core and task instance groups
must use EC2 GPU instance types that meet the [Hardware requirements](https://nvidia.github.io/spark-rapids/ "https://nvidia.github.io/spark-rapids/") of
Spark-RAPIDS. To view a complete list of Amazon EMR supported GPU instance types, please
see [Supported
instance types](../ManagementGuide/emr-supported-instance-types.md "../ManagementGuide/emr-supported-instance-types.md") in the _Amazon EMR Management Guide_. Instance
type for the primary instance group can be either GPU or non-GPU types, but ARM
instance types aren't supported.

## Set up application configurations for

your cluster

**1. Enable Amazon EMR to install the plugins on your new
cluster**

To install plugins, supply the following configuration when you create your
cluster:

```
{
	"Classification":"spark",
	"Properties":{
		"enableSparkRapids":"true"
	}
}
```

**2. Configure YARN to use GPU**

For details on how to use GPU on YARN, see [Using GPU on YARN](https://hadoop.apache.org/docs/r3.2.1/hadoop-yarn/hadoop-yarn-site/UsingGpus.html "https://hadoop.apache.org/docs/r3.2.1/hadoop-yarn/hadoop-yarn-site/UsingGpus.html") in Apache Hadoop documentation. The following
examples show sample YARN configurations for Amazon EMR 6.x and 7.x releases:

Amazon EMR 7.x
**Example YARN configuration for Amazon EMR
7.x**

```
{
    "Classification":"yarn-site",
    "Properties":{
        "yarn.nodemanager.resource-plugins":"yarn.io/gpu",
        "yarn.resource-types":"yarn.io/gpu",
        "yarn.nodemanager.resource-plugins.gpu.allowed-gpu-devices":"auto",
        "yarn.nodemanager.resource-plugins.gpu.path-to-discovery-executables":"/usr/bin",
        "yarn.nodemanager.linux-container-executor.cgroups.mount":"true",
        "yarn.nodemanager.linux-container-executor.cgroups.mount-path":"/spark-rapids-cgroup",
        "yarn.nodemanager.linux-container-executor.cgroups.hierarchy":"yarn",
        "yarn.nodemanager.container-executor.class":"org.apache.hadoop.yarn.server.nodemanager.LinuxContainerExecutor"
    }
},{
    "Classification":"container-executor",
    "Properties":{

    },
    "Configurations":[
        {
            "Classification":"gpu",
            "Properties":{
                "module.enabled":"true"
            }
        },
        {
            "Classification":"cgroups",
            "Properties":{
                "root":"/spark-rapids-cgroup",
                "yarn-hierarchy":"yarn"
            }
        }
    ]
}
```

Amazon EMR 6.x
**Example YARN configuration for Amazon EMR
6.x**

```
{
    "Classification":"yarn-site",
    "Properties":{
        "yarn.nodemanager.resource-plugins":"yarn.io/gpu",
        "yarn.resource-types":"yarn.io/gpu",
        "yarn.nodemanager.resource-plugins.gpu.allowed-gpu-devices":"auto",
        "yarn.nodemanager.resource-plugins.gpu.path-to-discovery-executables":"/usr/bin",
        "yarn.nodemanager.linux-container-executor.cgroups.mount":"true",
        "yarn.nodemanager.linux-container-executor.cgroups.mount-path":"/sys/fs/cgroup",
        "yarn.nodemanager.linux-container-executor.cgroups.hierarchy":"yarn",
        "yarn.nodemanager.container-executor.class":"org.apache.hadoop.yarn.server.nodemanager.LinuxContainerExecutor"
    }
},{
    "Classification":"container-executor",
    "Properties":{

    },
    "Configurations":[
        {
            "Classification":"gpu",
            "Properties":{
                "module.enabled":"true"
            }
        },
        {
            "Classification":"cgroups",
            "Properties":{
                "root":"/sys/fs/cgroup",
                "yarn-hierarchy":"yarn"
            }
        }
    ]
}
```

**3. Configure Spark to use RAPIDS**

Here are the required configurations to enable Spark to use RAPIDS plugin:

```
{
	"Classification":"spark-defaults",
	"Properties":{
		"spark.plugins":"com.nvidia.spark.SQLPlugin",
		"spark.executor.resource.gpu.discoveryScript":"/usr/lib/spark/scripts/gpu/getGpusResources.sh",
		"spark.executor.extraLibraryPath":"/usr/local/cuda/targets/x86_64-linux/lib:/usr/local/cuda/extras/CUPTI/lib64:/usr/local/cuda/compat/lib:/usr/local/cuda/lib:/usr/local/cuda/lib64:/usr/lib/hadoop/lib/native:/usr/lib/hadoop-lzo/lib/native:/docker/usr/lib/hadoop/lib/native:/docker/usr/lib/hadoop-lzo/lib/native"
	}
}
```

[XGBoost4J-Spark library](https://xgboost.readthedocs.io/en/latest/jvm/xgboost4j_spark_tutorial.html "https://xgboost.readthedocs.io/en/latest/jvm/xgboost4j_spark_tutorial.html") in XGBoost documentation is also available when
the Spark RAPIDS plugin is enabled on your cluster. You can use the following
configuration to integrate XGBoost with you Spark job:

```
{
	"Classification":"spark-defaults",
	"Properties":{
		"spark.submit.pyFiles":"/usr/lib/spark/jars/xgboost4j-spark_3.0-1.4.2-0.3.0.jar"
	}
}
```

For additional Spark configurations that you can use to tune a GPU-accelerated
EMR cluster, please refer to the [Rapids
Accelerator for Apache Spark tuning guide](https://docs.nvidia.com/spark-rapids/user-guide/latest/tuning-guide.html "https://docs.nvidia.com/spark-rapids/user-guide/latest/tuning-guide.html") in Nvidia.github.io
documentation.

**4. Configure YARN Capacity Scheduler**

`DominantResourceCalculator` must be configured to enable GPU
scheduling and isolation. For more information, please refer to [Using GPU on YARN](https://hadoop.apache.org/docs/r3.2.1/hadoop-yarn/hadoop-yarn-site/UsingGpus.html "https://hadoop.apache.org/docs/r3.2.1/hadoop-yarn/hadoop-yarn-site/UsingGpus.html") in Apache Hadoop documentation.

```
{
	"Classification":"capacity-scheduler",
	"Properties":{
		"yarn.scheduler.capacity.resource-calculator":"org.apache.hadoop.yarn.util.resource.DominantResourceCalculator"
	}
}

```

**5. Create a JSON file to include your
configurations**

You can create a JSON file that contains your configuration to use the RAPIDS
plugin for your Spark cluster. You supply the file later when you launch your
cluster.

You can store the file locally or on S3. For more information of how to supply
application configurations for your clusters, see [Configure applications](emr-configure-apps.md "emr-configure-apps.md").

Use the following sample files as templates to build your own
configurations.

Amazon EMR 7.x
**Example `my-configurations.json` file for Amazon EMR
7.x**

```
[
    {
        "Classification":"spark",
        "Properties":{
            "enableSparkRapids":"true"
        }
    },
    {
        "Classification":"yarn-site",
        "Properties":{
            "yarn.nodemanager.resource-plugins":"yarn.io/gpu",
            "yarn.resource-types":"yarn.io/gpu",
            "yarn.nodemanager.resource-plugins.gpu.allowed-gpu-devices":"auto",
            "yarn.nodemanager.resource-plugins.gpu.path-to-discovery-executables":"/usr/bin",
            "yarn.nodemanager.linux-container-executor.cgroups.mount":"true",
            "yarn.nodemanager.linux-container-executor.cgroups.mount-path":"/spark-rapids-cgroup",
            "yarn.nodemanager.linux-container-executor.cgroups.hierarchy":"yarn",
            "yarn.nodemanager.container-executor.class":"org.apache.hadoop.yarn.server.nodemanager.LinuxContainerExecutor"
        }
    },
    {
        "Classification":"container-executor",
        "Properties":{

        },
        "Configurations":[
            {
                "Classification":"gpu",
                "Properties":{
                    "module.enabled":"true"
                }
            },
            {
                "Classification":"cgroups",
                "Properties":{
                    "root":"/spark-rapids-cgroup",
                    "yarn-hierarchy":"yarn"
                }
            }
        ]
    },
    {
        "Classification":"spark-defaults",
        "Properties":{
            "spark.plugins":"com.nvidia.spark.SQLPlugin",
            "spark.executor.resource.gpu.discoveryScript":"/usr/lib/spark/scripts/gpu/getGpusResources.sh",
            "spark.executor.extraLibraryPath":"/usr/local/cuda/targets/x86_64-linux/lib:/usr/local/cuda/extras/CUPTI/lib64:/usr/local/cuda/compat/lib:/usr/local/cuda/lib:/usr/local/cuda/lib64:/usr/lib/hadoop/lib/native:/usr/lib/hadoop-lzo/lib/native:/docker/usr/lib/hadoop/lib/native:/docker/usr/lib/hadoop-lzo/lib/native",
            "spark.submit.pyFiles":"/usr/lib/spark/jars/xgboost4j-spark_3.0-1.4.2-0.3.0.jar",
            "spark.rapids.sql.concurrentGpuTasks":"1",
            "spark.executor.resource.gpu.amount":"1",
            "spark.executor.cores":"2",
            "spark.task.cpus":"1",
            "spark.task.resource.gpu.amount":"0.5",
            "spark.rapids.memory.pinnedPool.size":"0",
            "spark.executor.memoryOverhead":"2G",
            "spark.locality.wait":"0s",
            "spark.sql.shuffle.partitions":"200",
            "spark.sql.files.maxPartitionBytes":"512m"
        }
    },
    {
        "Classification":"capacity-scheduler",
        "Properties":{
            "yarn.scheduler.capacity.resource-calculator":"org.apache.hadoop.yarn.util.resource.DominantResourceCalculator"
        }
    }
]
```

Amazon EMR 6.x
**Example `my-configurations.json` file for Amazon EMR
6.x**

```
[
    {
        "Classification":"spark",
        "Properties":{
            "enableSparkRapids":"true"
        }
    },
    {
        "Classification":"yarn-site",
        "Properties":{
            "yarn.nodemanager.resource-plugins":"yarn.io/gpu",
            "yarn.resource-types":"yarn.io/gpu",
            "yarn.nodemanager.resource-plugins.gpu.allowed-gpu-devices":"auto",
            "yarn.nodemanager.resource-plugins.gpu.path-to-discovery-executables":"/usr/bin",
            "yarn.nodemanager.linux-container-executor.cgroups.mount":"true",
            "yarn.nodemanager.linux-container-executor.cgroups.mount-path":"/sys/fs/cgroup",
            "yarn.nodemanager.linux-container-executor.cgroups.hierarchy":"yarn",
            "yarn.nodemanager.container-executor.class":"org.apache.hadoop.yarn.server.nodemanager.LinuxContainerExecutor"
        }
    },
    {
        "Classification":"container-executor",
        "Properties":{

        },
        "Configurations":[
            {
                "Classification":"gpu",
                "Properties":{
                    "module.enabled":"true"
                }
            },
            {
                "Classification":"cgroups",
                "Properties":{
                    "root":"/sys/fs/cgroup",
                    "yarn-hierarchy":"yarn"
                }
            }
        ]
    },
    {
        "Classification":"spark-defaults",
        "Properties":{
            "spark.plugins":"com.nvidia.spark.SQLPlugin",
            "spark.executor.resource.gpu.discoveryScript":"/usr/lib/spark/scripts/gpu/getGpusResources.sh",
            "spark.executor.extraLibraryPath":"/usr/local/cuda/targets/x86_64-linux/lib:/usr/local/cuda/extras/CUPTI/lib64:/usr/local/cuda/compat/lib:/usr/local/cuda/lib:/usr/local/cuda/lib64:/usr/lib/hadoop/lib/native:/usr/lib/hadoop-lzo/lib/native:/docker/usr/lib/hadoop/lib/native:/docker/usr/lib/hadoop-lzo/lib/native",
            "spark.submit.pyFiles":"/usr/lib/spark/jars/xgboost4j-spark_3.0-1.4.2-0.3.0.jar",
            "spark.rapids.sql.concurrentGpuTasks":"1",
            "spark.executor.resource.gpu.amount":"1",
            "spark.executor.cores":"2",
            "spark.task.cpus":"1",
            "spark.task.resource.gpu.amount":"0.5",
            "spark.rapids.memory.pinnedPool.size":"0",
            "spark.executor.memoryOverhead":"2G",
            "spark.locality.wait":"0s",
            "spark.sql.shuffle.partitions":"200",
            "spark.sql.files.maxPartitionBytes":"512m"
        }
    },
    {
        "Classification":"capacity-scheduler",
        "Properties":{
            "yarn.scheduler.capacity.resource-calculator":"org.apache.hadoop.yarn.util.resource.DominantResourceCalculator"
        }
    }
]
```

## Add a bootstrap action for your

cluster

For more information on how to supply bootstrap action scripts when you create
your cluster, see [Bootstrap
action basics](../ManagementGuide/emr-plan-bootstrap.md#bootstrapUses "../ManagementGuide/emr-plan-bootstrap.md#bootstrapUses") in the _Amazon EMR Management Guide_.

The following example scripts show how to make a bootstrap action file for Amazon EMR
6.x and 7.x:

Amazon EMR 7.x
**Example
`my-bootstrap-action.sh` file for Amazon EMR
7.x**

To use YARN to manage GPU resources with Amazon EMR 7.x releases, you must
manually mount CGroup v1 on your cluster. You can do this
with as bootstrap action script, as shown in this example.

```
#!/bin/bash
set -ex

sudo mkdir -p /spark-rapids-cgroup/devices
sudo mount -t cgroup -o devices cgroupv1-devices /spark-rapids-cgroup/devices
sudo chmod a+rwx -R /spark-rapids-cgroup
```

Amazon EMR 6.x
**Example
`my-bootstrap-action.sh` file for Amazon EMR
6.x**

For Amazon EMR 6.x releases, you must open CGroup
permissions to YARN on your cluster. You can do this with a bootstrap
action script, as shown in this example.

```
#!/bin/bash
set -ex

sudo chmod a+rwx -R /sys/fs/cgroup/cpu,cpuacct
sudo chmod a+rwx -R /sys/fs/cgroup/devices
```

## Launch your cluster

The last step is to launch your cluster with the cluster configurations mentioned
above. Here's an example command to launch a cluster from the Amazon EMR CLI:

```
 aws emr create-cluster \
--release-label emr-7.11.0 \
--applications Name=Hadoop Name=Spark \
--service-role EMR_DefaultRole_V2 \
--ec2-attributes KeyName=my-key-pair,InstanceProfile=EMR_EC2_DefaultRole \
--instance-groups InstanceGroupType=MASTER,InstanceCount=1,InstanceType=m4.4xlarge \
                  InstanceGroupType=CORE,InstanceCount=1,InstanceType=g4dn.2xlarge \
                  InstanceGroupType=TASK,InstanceCount=1,InstanceType=g4dn.2xlarge \
--configurations file:///my-configurations.json \
--bootstrap-actions Name='My Spark Rapids Bootstrap action',Path=s3://amzn-s3-demo-bucket/my-bootstrap-action.sh

```
