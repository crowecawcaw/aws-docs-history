# Create and manage Amazon EMR clusters on EKS with AWS Step Functions

Learn how to integrate AWS Step Functions with Amazon EMR on EKS using the Amazon EMR on EKS service
integration APIs. The service integration APIs are the same as the corresponding Amazon EMR on
EKS APIs, but not all APIs support all integration patterns, as shown in the following
table.

To learn about integrating with AWS services in Step Functions, see [Integrating services](integrate-services.md "integrate-services.md") and [Passing parameters to a service API in Step Functions](connect-parameters.md "connect-parameters.md").

###### How the Optimized Amazon EMR on EKS integration is different than the Amazon EMR on EKS AWS SDK

integration

- The [Run a Job (.sync)](connect-to-resource.md#connect-sync "connect-to-resource.md#connect-sync") integration
  pattern is supported.
- There are no specific optimizations for the [Request Response](connect-to-resource.md#connect-default "connect-to-resource.md#connect-default") integration pattern.
- The [Wait for a Callback with Task Token](connect-to-resource.md#connect-wait-token "connect-to-resource.md#connect-wait-token")
  integration pattern is not supported.

###### Note

For integration with Amazon EMR, Step Functions has a hard-coded 60 seconds job polling frequency for the first 10 minutes and 300 seconds after that.

| API                  | Request response | Run a job (.sync) |
| -------------------- | ---------------- | ----------------- |
| CreateVirtualCluster | Supported        | _Not supported_   |
| DeleteVirtualCluster | Supported        | Supported         |
| StartJobRun          | Supported        | Supported         |

Supported Amazon EMR on EKS APIs:

###### Quota for input or result data

When sending or receiving data between services, the maximum input or result for a task is 256 KiB of data as a UTF-8 encoded string. See [Quotas related to state
machine executions](service-quotas.md#service-limits-state-machine-executions "service-quotas.md#service-limits-state-machine-executions").

- [`CreateVirtualCluster`](../../../emr-on-eks/latest/APIReference/API_CreateVirtualCluster.md "../../../emr-on-eks/latest/APIReference/API_CreateVirtualCluster.md")
  - [Request syntax](../../../emr-on-eks/latest/APIReference/API_CreateVirtualCluster.md#API_CreateVirtualCluster_RequestSyntax "../../../emr-on-eks/latest/APIReference/API_CreateVirtualCluster.md#API_CreateVirtualCluster_RequestSyntax")
  - [Supported parameters](../../../emr-on-eks/latest/APIReference/API_CreateVirtualCluster.md#API_CreateVirtualCluster_RequestBody "../../../emr-on-eks/latest/APIReference/API_CreateVirtualCluster.md#API_CreateVirtualCluster_RequestBody")
  - [Response syntax](../../../emr-on-eks/latest/APIReference/API_CreateVirtualCluster.md#API_CreateVirtualCluster_ResponseSyntax "../../../emr-on-eks/latest/APIReference/API_CreateVirtualCluster.md#API_CreateVirtualCluster_ResponseSyntax")

- [`DeleteVirtualCluster`](../../../emr-on-eks/latest/APIReference/API_DeleteVirtualCluster.md "../../../emr-on-eks/latest/APIReference/API_DeleteVirtualCluster.md")
  - [Request syntax](../../../emr-on-eks/latest/APIReference/API_DeleteVirtualCluster.md#API_DeleteVirtualCluster_RequestSyntax "../../../emr-on-eks/latest/APIReference/API_DeleteVirtualCluster.md#API_DeleteVirtualCluster_RequestSyntax")
  - [Supported parameters](../../../emr-on-eks/latest/APIReference/API_DeleteVirtualCluster.md#API_DeleteVirtualCluster_RequestParameters "../../../emr-on-eks/latest/APIReference/API_DeleteVirtualCluster.md#API_DeleteVirtualCluster_RequestParameters")
  - [Response syntax](../../../emr-on-eks/latest/APIReference/API_CreateVirtualCluster.md#API_CreateVirtualCluster_ResponseSyntax "../../../emr-on-eks/latest/APIReference/API_CreateVirtualCluster.md#API_CreateVirtualCluster_ResponseSyntax")

- [`StartJobRun`](../../../emr-on-eks/latest/APIReference/API_StartJobRun.md "../../../emr-on-eks/latest/APIReference/API_StartJobRun.md")

      + [Request syntax](../../../emr-on-eks/latest/APIReference/API_StartJobRun.md#API_StartJobRun_RequestSyntax "../../../emr-on-eks/latest/APIReference/API_StartJobRun.md#API_StartJobRun_RequestSyntax")
      + [Supported parameters](../../../emr-on-eks/latest/APIReference/API_StartJobRun.md#API_StartJobRun_RequestParameters "../../../emr-on-eks/latest/APIReference/API_StartJobRun.md#API_StartJobRun_RequestParameters")
      + [Response syntax](../../../emr-on-eks/latest/APIReference/API_StartJobRun.md#API_StartJobRun_ResponseSyntax "../../../emr-on-eks/latest/APIReference/API_StartJobRun.md#API_StartJobRun_ResponseSyntax")

  The following includes a `Task` state that creates a virtual cluster.

```
"Create_Virtual_Cluster": {
  "Type": "Task",
  "Resource": "arn:aws:states:::emr-containers:createVirtualCluster",
  "Arguments": {
    "Name": "MyVirtualCluster",
    "ContainerProvider": {
      "Id": "EKSClusterName",
      "Type": "EKS",
      "Info": {
        "EksInfo": {
          "Namespace": "Namespace"
        }
      }
    }
  },
  "End": true
}
```

The following includes a `Task` state that submits a job to a virtual cluster
and waits for it to complete.

```
"Submit_Job": {
    "Type": "Task",
    "Resource": "arn:aws:states:::emr-containers:startJobRun.sync",
    "Arguments": {
      "Name": "MyJobName",
      "VirtualClusterId": "{% $VirtualClusterId %}",
      "ExecutionRoleArn": "arn:aws:iam::`<accountId>`:role/job-execution-role",
      "ReleaseLabel": "emr-6.2.0-latest",
      "JobDriver": {
        "SparkSubmitJobDriver": {
          "EntryPoint": "s3://`<amzn-s3-demo-bucket>`/jobs/trip-count.py",
          "EntryPointArguments": [
            "60"
          ],
          "SparkSubmitParameters": "--conf spark.driver.cores=2 --conf spark.executor.instances=10 --conf spark.kubernetes.pyspark.pythonVersion=3 --conf spark.executor.memory=10G --conf spark.driver.memory=10G --conf spark.executor.cores=1 --conf spark.dynamicAllocation.enabled=false"
        }
      },
      "ConfigurationOverrides": {
        "ApplicationConfiguration": [
          {
            "Classification": "spark-defaults",
            "Properties": {
              "spark.executor.instances": "2",
              "spark.executor.memory": "2G"
            }
          }
        ],
        "MonitoringConfiguration": {
          "PersistentAppUI": "ENABLED",
          "CloudWatchMonitoringConfiguration": {
            "LogGroupName": "MyLogGroupName",
            "LogStreamNamePrefix": "MyLogStreamNamePrefix"
          },
          "S3MonitoringConfiguration": {
            "LogUri": "s3://`<amzn-s3-demo-logging-bucket1>`"
          }
        }
      },
      "Tags": {
        `"taskType"`: `"jobName"`
      }
    },
    "End": true
}
```

The following includes a `Task` state that deletes a virtual cluster and waits
for the deletion to complete.

```
"Delete_Virtual_Cluster": {
  "Type": "Task",
  "Resource": "arn:aws:states:::emr-containers:deleteVirtualCluster.sync",
  "Arguments": {
    "Id": "{% $states.input.VirtualClusterId %}",
  },
  "End": true
}
```

To learn about configuring IAM permissions when using Step Functions with other AWS services, see [How Step Functions generates IAM policies for integrated
services](service-integration-iam-templates.md "service-integration-iam-templates.md").
