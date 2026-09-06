

# Using job submitter classification
<a name="emr-eks-job-submitter"></a>

## Overview
<a name="emr-eks-job-submitter-overview"></a>

The Amazon EMR on EKS `StartJobRun` request creates a *job submitter* pod (also known as the *job-runner* pod) to spawn the Spark driver. You can use the `emr-job-submitter` classification to configure node selectors, add tolerations, customize logging, and make other modifications to the job submitter pod.

The following settings are available under the `emr-job-submitter` classification:

** `jobsubmitter.node.selector.[{{selectorKey}}]` **  
Adds to the node selector of the job submitter pod, with key {{selectorKey}} and the value as the configuration value. For example, you can set ` jobsubmitter.node.selector.identifier` to `myIdentifier` and the job submitter pod will have a node selector with a key `identifier` and a value `myIdentifier`. This can be used to specify which nodes the job submitter pod can be placed on. To add multiple node selector keys, set multiple configurations with this prefix.

** `jobsubmitter.label.[{{labelKey}}]` **  
Adds to the labels of the job submitter pod, with key {{labelKey}} and the value as the configuration value. To add multiple labels, set multiple configurations with this prefix.

** `jobsubmitter.annotation.[{{annotationKey}}]` **  
Adds to the annotations of the job submitter pod, with key {{annotationKey}} and the value as the configuration value. To add multiple annotations, set multiple configurations with this prefix.

** `jobsubmitter.node.toleration.[{{tolerationKey}}]` **  
Adds [ tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) to the job submitter pod. By default there are no tolerations added to the pod. The toleration's key will be {{tolerationKey}} and the toleration's value will be the configuration value. If the configuration value is set to a non-empty string, the operator will be `Equals`. If the configuration value is set to `""`, then the operator will be `Exists`.

** `jobsubmitter.node.toleration.[{{tolerationKey}}].[{{effect}}]` **  
Adds a toleration effect to the prefixed {{tolerationKey}}. This field is required when adding tolerations. The allowed values for the effect field are ` NoExecute`, `NoSchedule`, and `PreferNoSchedule`.

** `jobsubmitter.node.toleration.[{{tolerationKey}}].[{{tolerationSeconds}}]` **  
Adds tolerationSeconds to the prefixed {{tolerationKey}}. Optional field. Only applicable when the effect is `NoExecute`.

** `jobsubmitter.scheduler.name` **  
Sets a custom schedulerName for the job submitter pod.

** `jobsubmitter.logging` **  
Enables or disables logging on the job submitter pod. When this is set to ` DISABLED` the logging container is removed from the job submitter pod, which will disable any logging for this pod specified in the `monitoringConfiguration`, such as `s3MonitoringConfiguration` or `cloudWatchMonitoringConfiguration`. When this setting is not set or is set to any other value, logging on the job submitter pod is enabled.

** `jobsubmitter.logging.image` **  
Sets a custom image to be used for the logging container on the job submitter pod.

** `jobsubmitter.logging.request.cores` **  
Sets a custom value for the number of CPUs, in CPU units, for the logging container on the job submitter pod. By default, this is set to **100m**.

** `jobsubmitter.logging.request.memory` **  
Sets a custom value for the amount of memory, in bytes, for the logging container on the job submitter pod. By default, this is set to **200Mi**. A mebibyte is a unit of measure that's similar to a megabyte.

** `jobsubmitter.container.image` **  
Sets a custom image for the job submitter pod's `job-runner` container.

** `jobsubmitter.container.image.pullPolicy` **  
Sets the [imagePullPolicy](https://kubernetes.io/docs/concepts/containers/images/#image-pull-policy) for the job submitter pod's containers.

** `jobsubmitter.gracefulTermination` **  
By default or when this config is set to `false`, after the job runner pod creates the driver pod it continues running, watches the driver pod, and periodically logs the driver status for the lifetime of the job. When this config is set to `true`, the job runner pod instead terminates immediately after starting the Spark driver pod. This means the job runner pod consumes CPU and memory for less time, but job runner logs are no longer available.

We recommend to place job submitter pods on On-Demand Instances. Placing job submitter pods on Spot instances might result in a job failure if the instance where the job submitter pod runs is subject to a Spot Instance interruption. You can also [place the job submitter pod in a single Availability Zone or use any Kubernetes labels that are applied to the nodes](#emr-eks-job-submitter-ex-ec2).

## Job submitter classification examples
<a name="emr-eks-job-submitter-examples"></a>

**Topics**
+ [`StartJobRun` request with On-Demand node placement for the job submitter pod](#emr-eks-job-submitter-ex-od)
+ [`StartJobRun` request with single-AZ node placement and Amazon EC2 instance type placement for the job submitter pod](#emr-eks-job-submitter-ex-ec2)
+ [`StartJobRun` request with labels, annotations, and a custom scheduler for the job submitter pod](#emr-eks-job-submitter-label-annotation-scheduler)
+ [`StartJobRun` request with a toleration applied to the job submitter pod with key `dedicated`, value `graviton_machines`, effect `NoExecute`, and a `tolerationSeconds` of 60 seconds](#emr-eks-job-submitter-tolerations)
+ [`StartJobRun` request with logging disabled for the job submitter pod](#emr-eks-job-submitter-logging-disabled)
+ [`StartJobRun` request with custom logging container image, CPU, and memory for the job submitter pod](#emr-eks-job-submitter-custom)
+ [`StartJobRun` request with a custom job submitter container image and pull policy](#emr-eks-job-submitter-custom-container)
+ [`StartJobRun` request with graceful termination enabled for the job submitter pod](#emr-eks-job-submitter-graceful-termination)

### `StartJobRun` request with On-Demand node placement for the job submitter pod
<a name="emr-eks-job-submitter-ex-od"></a>

```
cat >spark-python-in-s3-nodeselector-job-submitter.json << EOF
{
  "name": "spark-python-in-s3-nodeselector", 
  "virtualClusterId": "{{virtual-cluster-id}}", 
  "executionRoleArn": "{{execution-role-arn}}", 
  "releaseLabel": "{{emr-6.11.0-latest}}", 
  "jobDriver": {
    "sparkSubmitJobDriver": {
      "entryPoint": "s3://{{S3-prefix}}/trip-count.py", 
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

### `StartJobRun` request with single-AZ node placement and Amazon EC2 instance type placement for the job submitter pod
<a name="emr-eks-job-submitter-ex-ec2"></a>

```
"configurationOverrides": {
  "applicationConfiguration": [
    {
      "classification": "emr-job-submitter",
      "properties": {
        "jobsubmitter.node.selector.topology.kubernetes.io/zone": "{{Availability Zone}}",
        "jobsubmitter.node.selector.node.kubernetes.io/instance-type":"{{m5.4xlarge}}"
      }
    }
  ]
}
```

### `StartJobRun` request with labels, annotations, and a custom scheduler for the job submitter pod
<a name="emr-eks-job-submitter-label-annotation-scheduler"></a>

```
"configurationOverrides": { 
  "applicationConfiguration": [ 
    {
      "classification": "emr-job-submitter", 
      "properties": {
        "jobsubmitter.label.label1": "value1",
        "jobsubmitter.label.label2": "value2",
        "jobsubmitter.annotation.ann1": "value1",
        "jobsubmitter.annotation.ann2": "value2",
        "jobsubmitter.scheduler.name": "custom-scheduler"
      }
    }
  ]
}
```

### `StartJobRun` request with a toleration applied to the job submitter pod with key `dedicated`, value `graviton_machines`, effect `NoExecute`, and a `tolerationSeconds` of 60 seconds
<a name="emr-eks-job-submitter-tolerations"></a>

```
"configurationOverrides": {
  "applicationConfiguration": [
    {
      "classification": "emr-job-submitter",
      "properties": {
        "jobsubmitter.node.toleration.dedicated":"graviton_machines",
        "jobsubmitter.node.toleration.dedicated.effect":"NoExecute",
        "jobsubmitter.node.toleration.dedicated.tolerationSeconds":"60"
      }
    }
  ]
}
```

### `StartJobRun` request with logging disabled for the job submitter pod
<a name="emr-eks-job-submitter-logging-disabled"></a>

```
"configurationOverrides": {
  "applicationConfiguration": [
    {
      "classification": "emr-job-submitter",
      "properties": {
        "jobsubmitter.logging": "DISABLED"
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
```

### `StartJobRun` request with custom logging container image, CPU, and memory for the job submitter pod
<a name="emr-eks-job-submitter-custom"></a>

```
"configurationOverrides": {
  "applicationConfiguration": [
    {
      "classification": "emr-job-submitter",
      "properties": {
        "jobsubmitter.logging.image": "{{YOUR_ECR_IMAGE_URL}}",
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
```

### `StartJobRun` request with a custom job submitter container image and pull policy
<a name="emr-eks-job-submitter-custom-container"></a>

```
"configurationOverrides": {
  "applicationConfiguration": [
    {
      "classification": "emr-job-submitter",
      "properties": {
        "jobsubmitter.container.image": "{{123456789012.dkr.ecr.us-west-2.amazonaws.com/emr6.11_custom_repo}}",
        "jobsubmitter.container.image.pullPolicy": "{{kubernetes pull policy}}"
      }
    }
  ]
}
```

### `StartJobRun` request with graceful termination enabled for the job submitter pod
<a name="emr-eks-job-submitter-graceful-termination"></a>

```
"configurationOverrides": {
  "applicationConfiguration": [
    {
      "classification": "emr-job-submitter",
      "properties": {
        "jobsubmitter.gracefulTermination": "true"
      }
    }
  ]
}
```