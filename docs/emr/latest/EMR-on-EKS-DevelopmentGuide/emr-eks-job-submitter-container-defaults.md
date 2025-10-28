# Using Amazon EMR container defaults classification

## Overview

The following settings are available under the `emr-containers-defaults` classification:

**`job-start-timeout`**

By default, a job will time out if it cannot start and it waits in the `SUBMITTED` state for 15 minutes. This
configuration changes the number of seconds to wait before the job times out.

**`logging.image`**

Sets a custom image to be used for the logging container on the driver and executor pods.

**`logging.request.cores`**

Sets a custom value for the number of CPUs, in CPU units, for the logging container on the driver and executor pods. By default, this is not set.

**`logging.request.memory`**

Sets a custom value for the amount of memory, in bytes, for the logging container on the driver and
executor pods. By default, this is set to **512Mi**. A mebibyte is a unit of measure that's similar to a megabyte.

## Job submitter classification

examples

###### In this section

- [StartJobRun request with custom job timeout](#emr-eks-job-submitter-container-custom-timeout "#emr-eks-job-submitter-container-custom-timeout")
- [StartJobRun request with custom logging container image, CPU, and memory](#emr-eks-job-submitter-container-custom-image-cpu "#emr-eks-job-submitter-container-custom-image-cpu")

### `StartJobRun` request with custom job timeout

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

### `StartJobRun` request with custom logging container image, CPU, and memory

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
        "classification": "emr-containers-defaults",
        "properties": {
            "logging.image": "`YOUR_ECR_IMAGE_URL`",
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
}
```
