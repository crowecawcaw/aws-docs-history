# Using job submitter classification

## Overview

The Amazon EMR on EKS `StartJobRun` request creates a _job submitter_ pod (also known as the _job-runner_ pod) to spawn the Spark driver.
You can use `emr-job-submitter` classification to configure node selectors for your job submitter pod, as well as set the image, CPU, and memory for the
job submitter pod’s logging container.

The following settings are available under the `emr-job-submitter`
classification:

**`jobsubmitter.node.selector.[`labelKey`]`**

Adds to the node selector of the job submitter pod, with key
`labelKey` and the value as the
configuration value for the configuration. For example, you can set
`jobsubmitter.node.selector.identifier` to `myIdentifier`
and the job submitter pod will have a node selector with a key identifier value of
`myIdentifier`. This can be used to specify which nodes the job submitter pod can be placed on. To add multiple node
selector keys, set multiple configurations with this prefix.

**`jobsubmitter.logging.image`**

Sets a custom image to be used for the logging container on the job submitter pod.

**`jobsubmitter.logging.request.cores`**

Sets a custom value for the number of CPUs, in CPU units, for the logging container on the job submitter pod. By default, this is
set to **100m**.

**`jobsubmitter.logging.request.memory`**

Sets a custom value for the amount of memory, in bytes, for the logging container on the job submitter pod. By default, this is
set to **200Mi**. A mebibyte is a unit of measure that's similar to a megabyte.

We recommend to place job submitter pods on On-Demand Instances. Placing job submitter pods on Spot instances might result in a job failure if the instance where the job
submitter pod runs is subject to a Spot Instance interruption. You can also [place the job submitter pod in a single
Availability Zone](#emr-eks-job-submitter-ex-1az "#emr-eks-job-submitter-ex-1az"), or [use any Kubernetes
labels that are applied to the nodes](#emr-eks-job-submitter-ex-ec2 "#emr-eks-job-submitter-ex-ec2").

## Job submitter classification

examples

###### In this section

- [StartJobRun request with
  On-Demand node placement for the job submitter pod](#emr-eks-job-submitter-ex-od "#emr-eks-job-submitter-ex-od")
- [StartJobRun request with
  single-AZ node placement for the job submitter pod](#emr-eks-job-submitter-ex-1az "#emr-eks-job-submitter-ex-1az")
- [StartJobRun request with
  single-AZ and Amazon EC2 instance type placement for the job submitter pod](#emr-eks-job-submitter-ex-ec2 "#emr-eks-job-submitter-ex-ec2")
- [StartJobRun request with
  custom logging container image, CPU, and memory](#emr-eks-job-submitter-custom "#emr-eks-job-submitter-custom")
- [StartJobRun request with
  with custom container image](#emr-eks-job-submitter-custom-container "#emr-eks-job-submitter-custom-container")

### `StartJobRun` request with

On-Demand node placement for the job submitter pod

```
cat >spark-python-in-s3-nodeselector-job-submitter.json << EOF
{
  "name": "spark-python-in-s3-nodeselector",
  "virtualClusterId": "`virtual-cluster-id`",
  "executionRoleArn": "`execution-role-arn`",
  "releaseLabel": "`emr-6.11.0-latest`",
  "jobDriver": {
    "sparkSubmitJobDriver": {
      "entryPoint": "s3://`S3-prefix`/trip-count.py",
       "sparkSubmitParameters": "--conf spark.driver.cores=5  --conf spark.executor.memory=20G --conf spark.driver.memory=15G --conf spark.executor.cores=6"
    }
  },
  "configurationOverrides": {
    "applicationConfiguration": [
      {
        "classification": "spark-defaults",
        "properties": {
          "spark.dynamicAllocation.enabled":"false"
         }
      },
      {
        "classification": "emr-job-submitter",
        "properties": {
            "jobsubmitter.node.selector.eks.amazonaws.com/capacityType": "ON_DEMAND"
        }
      }
    ],
    "monitoringConfiguration": {
      "cloudWatchMonitoringConfiguration": {
        "logGroupName": "/emr-containers/jobs",
        "logStreamNamePrefix": "demo"
      },
      "s3MonitoringConfiguration": {
        "logUri": "s3://joblogs"
      }
    }
  }
}
EOF
aws emr-containers start-job-run --cli-input-json file:///spark-python-in-s3-nodeselector-job-submitter.json
```

### `StartJobRun` request with

single-AZ node placement for the job submitter pod

```
cat >spark-python-in-s3-nodeselector-job-submitter-az.json << EOF
{
  "name": "spark-python-in-s3-nodeselector",
  "virtualClusterId": "`virtual-cluster-id`",
  "executionRoleArn": "`execution-role-arn`",
  "releaseLabel": "`emr-6.11.0-latest`",
  "jobDriver": {
    "sparkSubmitJobDriver": {
      "entryPoint": "s3://`S3-prefix`/trip-count.py",
       "sparkSubmitParameters": "--conf spark.driver.cores=5  --conf spark.executor.memory=20G --conf spark.driver.memory=15G --conf spark.executor.cores=6"
    }
  },
  "configurationOverrides": {
    "applicationConfiguration": [
      {
        "classification": "spark-defaults",
        "properties": {
          "spark.dynamicAllocation.enabled":"false"
         }
      },
      {
        "classification": "emr-job-submitter",
        "properties": {
            "jobsubmitter.node.selector.topology.kubernetes.io/zone": "`Availability Zone`"
        }
      }
    ],
    "monitoringConfiguration": {
      "cloudWatchMonitoringConfiguration": {
        "logGroupName": "/emr-containers/jobs",
        "logStreamNamePrefix": "demo"
      },
      "s3MonitoringConfiguration": {
        "logUri": "s3://joblogs"
      }
    }
  }
}
EOF
aws emr-containers start-job-run --cli-input-json file:///spark-python-in-s3-nodeselector-job-submitter-az.json
```

### `StartJobRun` request with

single-AZ and Amazon EC2 instance type placement for the job submitter pod

```
{
  "name": "spark-python-in-s3-nodeselector",
  "virtualClusterId": "`virtual-cluster-id`",
  "executionRoleArn": "`execution-role-arn`",
  "releaseLabel": "`emr-6.11.0-latest`",
  "jobDriver": {
    "sparkSubmitJobDriver": {
      "entryPoint": "s3://`S3-prefix`/trip-count.py",
       "sparkSubmitParameters": "--conf spark.driver.cores=5  --conf spark.kubernetes.pyspark.pythonVersion=3 --conf spark.executor.memory=20G --conf spark.driver.memory=15G --conf spark.executor.cores=6 --conf spark.sql.shuffle.partitions=1000"
    }
  },
  "configurationOverrides": {
    "applicationConfiguration": [
      {
        "classification": "spark-defaults",
        "properties": {
          "spark.dynamicAllocation.enabled":"false",
         }
      },
      {
        "classification": "emr-job-submitter",
        "properties": {
            "jobsubmitter.node.selector.topology.kubernetes.io/zone": "`Availability Zone`",
            "jobsubmitter.node.selector.node.kubernetes.io/instance-type":"`m5.4xlarge`"
        }
      }
    ],
    "monitoringConfiguration": {
      "cloudWatchMonitoringConfiguration": {
        "logGroupName": "/emr-containers/jobs",
        "logStreamNamePrefix": "demo"
      },
      "s3MonitoringConfiguration": {
        "logUri": "s3://joblogs"
      }
    }
  }
}
```

### `StartJobRun` request with

custom logging container image, CPU, and memory

```
{
  "name": "spark-python",
  "virtualClusterId": "virtual-cluster-id",
  "executionRoleArn": "execution-role-arn",
  "releaseLabel": "emr-6.11.0-latest",
  "jobDriver": {
    "sparkSubmitJobDriver": {
      "entryPoint": "s3://S3-prefix/trip-count.py"
    }
  },
  "configurationOverrides": {
    "applicationConfiguration": [
      {
        "classification": "emr-job-submitter",
        "properties": {
            "jobsubmitter.logging.image": "`YOUR_ECR_IMAGE_URL`",
            "jobsubmitter.logging.request.memory": "200Mi",
            "jobsubmitter.logging.request.cores": "0.5"
        }
      }
    ],
    "monitoringConfiguration": {
      "cloudWatchMonitoringConfiguration": {
        "logGroupName": "/emr-containers/jobs",
        "logStreamNamePrefix": "demo"
      },
      "s3MonitoringConfiguration": {
        "logUri": "s3://joblogs"
      }
    }
  }
}
```

### `StartJobRun` request with

with custom container image

```
cat >spark-python-in-s3-nodeselector-custom-container-image-job-submitter.json << EOF
{
  "name": "spark-python-in-s3-nodeselector",
  "virtualClusterId": "`virtual-cluster-id`",
  "executionRoleArn": "`execution-role-arn`",
  "releaseLabel": "`emr-6.11.0-latest`",
  "jobDriver": {
    "sparkSubmitJobDriver": {
      "entryPoint": "s3://`S3-prefix`/trip-count.py",
       "sparkSubmitParameters": "--conf spark.driver.cores=5  --conf spark.executor.memory=20G --conf spark.driver.memory=15G --conf spark.executor.cores=6"
    }
  },
  "configurationOverrides": {
    "applicationConfiguration": [
      {
        "classification": "spark-defaults",
        "properties": {
          "spark.dynamicAllocation.enabled":"false"
         }
      },
      {
        "classification": "emr-job-submitter",
        "properties": {
            "jobsubmitter.container.image": "`123456789012.dkr.ecr.us-west-2.amazonaws.com/emr6.11_custom_repo`",
            "jobsubmitter.container.image.pullPolicy": "`kubernetes pull policy`"
        }
      }
    ],
    "monitoringConfiguration": {
      "cloudWatchMonitoringConfiguration": {
        "logGroupName": "/emr-containers/jobs",
        "logStreamNamePrefix": "demo"
      },
      "s3MonitoringConfiguration": {
        "logUri": "s3://joblogs"
      }
    }
  }
}
EOF
aws emr-containers start-job-run --cli-input-json file:///spark-python-in-s3-nodeselector-custom-container-image-job-submitter.json
```
