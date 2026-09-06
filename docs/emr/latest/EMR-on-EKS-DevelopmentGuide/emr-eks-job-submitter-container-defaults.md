

# Using Amazon EMR container defaults classification
<a name="emr-eks-job-submitter-container-defaults"></a>

## Overview
<a name="emr-eks-job-submitter-container-defaults-overview"></a>

The following settings are available under the `emr-containers-defaults` classification:

** `job-start-timeout` **  
By default, a job will time out if it cannot start and it waits in the ` SUBMITTED` state for 15 minutes. This configuration changes the number of seconds to wait before the job times out.

** `executor.logging` **  
Enables or disables logging on the executor pods. When this is set to ` DISABLED` the logging container is removed from the executor pods, which will disable any logging for these pods specified in the `monitoringConfiguration`, such as `s3MonitoringConfiguration` or `cloudWatchMonitoringConfiguration`. When this setting is not set or is set to any other value, logging on the executor pods is enabled.

** `logging.image` **  
Sets a custom image to be used for the logging container on the driver and executor pods.

** `logging.request.cores` **  
Sets a custom value for the number of CPUs, in CPU units, for the logging container on the driver and executor pods. By default, this is not set.

** `logging.request.memory` **  
Sets a custom value for the amount of memory, in bytes, for the logging container on the driver and executor pods. By default, this is set to **512Mi**. A mebibyte is a unit of measure that's similar to a megabyte.

** `logging.eventLog.dir` **  
Use this configuration to enable Persistent App UI and save Spark event logs to your own S3 location. Set `logging.eventLog.dir` to the S3 path for your event logs. In the `monitoringConfiguration`, set `persistentAppUI` to `ENABLED`. Don't set `spark.eventLog.dir` when you use `logging.eventLog.dir`; these two configurations are incompatible. If `spark.eventLog.dir` is set, that configuration takes priority and the logging container is unable to replicate Spark event logs. This means your S3 location specified by `logging.eventLog.dir` won't receive event logs and the Persistent App UI also won't work.

** `logging.nativeSidecar` **  
When you set this property to `ENABLED` for Amazon EMR release 6.8.0 or higher, Amazon EMR configures the logging container on your Spark driver and executor pods as a Kubernetes native sidecar container (see details on the [Kubernetes website](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/)) instead of a regular container. This means the logging container automatically restarts on failure and logging container failures won't cause the pod to fail.  
**Node version requirement**  
Your Amazon EKS nodes must be running Kubernetes version 1.29 or higher. Your EKS cluster version can differ from your node version. If your nodes are running a version lower than 1.29, Kubernetes does not enable the native sidecar feature and the logging container prevents the driver from starting, which leads to job timeouts.

## Job submitter classification examples
<a name="emr-eks-job-submitter-container-examples"></a>

**Topics**
+ [`StartJobRun` request with custom job timeout](#emr-eks-job-submitter-container-custom-timeout)
+ [`StartJobRun` request with logging disabled for executor pods](#emr-eks-executor-logging-disabled)
+ [`StartJobRun` request with custom logging container image, CPU, and memory for the driver and executor pods](#emr-eks-job-submitter-container-custom-image-cpu)
+ [`StartJobRun` request with Spark event log Amazon S3 destination](#emr-eks-job-submitter-container-event-log-dir)
+ [`StartJobRun` request with native sidecar logging](#emr-eks-job-submitter-container-native-sidecar)

### `StartJobRun` request with custom job timeout
<a name="emr-eks-job-submitter-container-custom-timeout"></a>

```
{
  "name": "spark-python", 
  "virtualClusterId": "{{virtual-cluster-id}}", 
  "executionRoleArn": "{{execution-role-arn}}", 
  "releaseLabel": "{{emr-6.11.0-latest}}", 
  "jobDriver": {
    "sparkSubmitJobDriver": {
      "entryPoint": "s3://{{S3-prefix}}/trip-count.py"
    }
  }, 
  "configurationOverrides": {
    "applicationConfiguration": [
      {
        "classification": "emr-containers-defaults", 
        "properties": {
          "job-start-timeout": "1800"
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

### `StartJobRun` request with logging disabled for executor pods
<a name="emr-eks-executor-logging-disabled"></a>

```
"configurationOverrides": {
  "applicationConfiguration": [
    {
      "classification": "emr-containers-defaults", 
      "properties": {
        "executor.logging": "DISABLED"
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

### `StartJobRun` request with custom logging container image, CPU, and memory for the driver and executor pods
<a name="emr-eks-job-submitter-container-custom-image-cpu"></a>

```
"configurationOverrides": {
  "applicationConfiguration": [
    {
      "classification": "emr-containers-defaults", 
      "properties": {
        "logging.image": "{{YOUR_ECR_IMAGE_URL}}",
        "logging.request.memory": "200Mi",
        "logging.request.cores": "0.5"
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

**Note**  
If the Fluentd logging container encounters an out-of-memory (OOM) error, increase the `logging.request.memory` value. For example, set it to `1Gi` to allocate more memory to the logging container and prevent OOM issues.

### `StartJobRun` request with Spark event log Amazon S3 destination
<a name="emr-eks-job-submitter-container-event-log-dir"></a>

The following example saves Spark event logs to your own Amazon S3 bucket while also enabling Persistent App UI. The `persistentAppUI` setting is `ENABLED` by default.

```
"configurationOverrides": {
  "applicationConfiguration": [
    {
      "classification": "emr-containers-defaults", 
      "properties": {
        "logging.eventLog.dir": "s3://{{my-bucket}}/{{event-logs}}/"
      }
    }
  ], 
  "monitoringConfiguration": {
    "persistentAppUI": "ENABLED"
  }
}
```

**Note**  
Don't set `spark.eventLog.dir` in the `spark-defaults` classification when you use `logging.eventLog.dir`. These two configurations are incompatible. If `spark.eventLog.dir` is set, that configuration takes priority and the logging container is unable to replicate Spark event logs. This means your S3 location specified by `logging.eventLog.dir` won't receive event logs and the Persistent App UI also won't work.

### `StartJobRun` request with native sidecar logging
<a name="emr-eks-job-submitter-container-native-sidecar"></a>

The following example enables native sidecar mode for the logging container on Spark driver and executor pods. When enabled, the logging container runs as a Kubernetes native sidecar that automatically restarts on failure and doesn't affect the state of your Spark pods.

```
"configurationOverrides": {
  "applicationConfiguration": [
    {
      "classification": "emr-containers-defaults", 
      "properties": {
        "logging.nativeSidecar": "ENABLED"
      }
    }
  ], 
  "monitoringConfiguration": {
    "s3MonitoringConfiguration": {
      "logUri": "s3://{{my-bucket}}/{{logs}}/"
    }
  }
}
```

**Node version requirement**  
Your Amazon EKS nodes must be running Kubernetes version 1.29 or higher. Your EKS cluster version can differ from your node version. If your nodes are running a version lower than 1.29, Kubernetes does not enable the native sidecar feature and the logging container prevents the driver from starting, which leads to job timeouts.