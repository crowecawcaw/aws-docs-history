# Run a Flink

application

With Amazon EMR 6.13.0 and higher, you can run a Flink application with the Flink Kubernetes
operator in Application mode on Amazon EMR on EKS. With Amazon EMR 6.15.0 and higher, you can also run a
Flink application in Session mode. This page describes both methods that you can use to run a
Flink application with Amazon EMR on EKS.

###### Topics

###### Note

You must have an Amazon S3 bucket created to store the high-availability metadata when you
submit your Flink job. If you don’t want to use this feature, you can disable it. It's
enabled by default.

**Prerequisite** – Before you can run a Flink application with the Flink Kubernetes operator, complete
the steps in [Setting up the Flink Kubernetes
operator for Amazon EMR on EKS](jobruns-flink-kubernetes-operator-setup.md "jobruns-flink-kubernetes-operator-setup.md") and [Install the Kubernetes operator](jobruns-flink-kubernetes-operator-getting-started.md#jobruns-flink-kubernetes-operator-getting-started-install-operator "jobruns-flink-kubernetes-operator-getting-started.md#jobruns-flink-kubernetes-operator-getting-started-install-operator").

Application mode
With Amazon EMR 6.13.0 and higher, you can run a Flink application with the Flink Kubernetes
operator in Application mode on Amazon EMR on EKS.

1. Create a `FlinkDeployment` definition file
   `basic-example-app-cluster.yaml` like in the following example. If you
   activated and use one of the [opt-in AWS Regions](../../../controltower/latest/userguide/opt-in-region-considerations.md "../../../controltower/latest/userguide/opt-in-region-considerations.md"),
   make sure you uncomment and configure
   the configuration `fs.s3a.endpoint.region`.

```
apiVersion: flink.apache.org/v1beta1
kind: FlinkDeployment
metadata:
  name: basic-example-app-cluster
spec:
  flinkConfiguration:
    taskmanager.numberOfTaskSlots: "2"
    #fs.s3a.endpoint.region: `OPT_IN_AWS_REGION_NAME`
    state.checkpoints.dir: `CHECKPOINT_S3_STORAGE_PATH`
    state.savepoints.dir: `SAVEPOINT_S3_STORAGE_PATH`
  flinkVersion: v1_17
  executionRoleArn: `JOB_EXECUTION_ROLE_ARN`
  emrReleaseLabel: "emr-6.13.0-flink-latest" # 6.13 or higher
  jobManager:
    storageDir: `HIGH_AVAILABILITY_STORAGE_PATH`
    resource:
      memory: "2048m"
      cpu: 1
  taskManager:
    resource:
      memory: "2048m"
      cpu: 1
  job:
    # if you have your job jar in S3 bucket you can use that path as well
    jarURI: local:///opt/flink/examples/streaming/StateMachineExample.jar
    parallelism: 2
    upgradeMode: savepoint
    savepointTriggerNonce: 0
  monitoringConfiguration:
    cloudWatchMonitoringConfiguration:
       logGroupName: `LOG_GROUP_NAME`

```

2. Submit the Flink deployment with the following command. This will also create a
   `FlinkDeployment` object named `basic-example-app-cluster`.

```
kubectl create -f basic-example-app-cluster.yaml -n <NAMESPACE>
```

3. Access the Flink UI.

```
kubectl port-forward deployments/basic-example-app-cluster 8081 -n `NAMESPACE`
```

4. Open `localhost:8081` to view your Flink jobs locally.
5. Clean up the job. Remember to clean up the S3 artifacts that were created for this
   job, such as checkpointing, high-availability, savepointing metadata, and CloudWatch
   logs.

For more information on submitting applications to Flink through the Flink Kubernetes
operator, see [Flink
Kubernetes operator examples](https://github.com/apache/flink-kubernetes-operator/tree/main/examples "https://github.com/apache/flink-kubernetes-operator/tree/main/examples") in the `apache/flink-kubernetes-operator`
folder on GitHub.

Session mode
With Amazon EMR 6.15.0 and higher, you can run a Flink application with the Flink Kubernetes
operator in Session mode on Amazon EMR on EKS.

1. Create a `FlinkDeployment` definition file named
   `basic-example-app-cluster.yaml` like in the following example. If you
   activated and use one of the [opt-in AWS Regions](../../../controltower/latest/userguide/opt-in-region-considerations.md "../../../controltower/latest/userguide/opt-in-region-considerations.md"),
   make sure you uncomment and configure
   the configuration `fs.s3a.endpoint.region`.

```
apiVersion: flink.apache.org/v1beta1
kind: FlinkDeployment
metadata:
  name: basic-example-session-cluster
spec:
  flinkConfiguration:
    taskmanager.numberOfTaskSlots: "2"
    #fs.s3a.endpoint.region: `OPT_IN_AWS_REGION_NAME`
    state.checkpoints.dir: `CHECKPOINT_S3_STORAGE_PATH`
    state.savepoints.dir: `SAVEPOINT_S3_STORAGE_PATH`
  flinkVersion: v1_17
  executionRoleArn: `JOB_EXECUTION_ROLE_ARN`
  emrReleaseLabel: "`emr-6.15.0`-flink-latest"
  jobManager:
    storageDir: `HIGH_AVAILABILITY_S3_STORAGE_PATH`
    resource:
      memory: "2048m"
      cpu: 1
  taskManager:
    resource:
      memory: "2048m"
      cpu: 1
  monitoringConfiguration:
    s3MonitoringConfiguration:
       logUri:
    cloudWatchMonitoringConfiguration:
       logGroupName: `LOG_GROUP_NAME`
```

2. Submit the Flink deployment with the following command. This will also create a
   `FlinkDeployment` object named `basic-example-session-cluster`.

```
kubectl create -f basic-example-app-cluster.yaml -n `NAMESPACE`
```

3. Use the following command to confirm that the session cluster `LIFECYCLE` is `STABLE`:

```
kubectl get flinkdeployments.flink.apache.org basic-example-session-cluster -n `NAMESPACE`
```

The output should be similar to the following example:

```
NAME                              JOB STATUS   LIFECYCLE STATE
basic-example-session-cluster                          STABLE
```

4. Create a `FlinkSessionJob` custom definition resource file `basic-session-job.yaml` with the following example content:

```
apiVersion: flink.apache.org/v1beta1
kind: FlinkSessionJob
metadata:
  name: basic-session-job
spec:
  deploymentName: basic-session-deployment
  job:
    # If you have your job jar in an S3 bucket you can use that path.
    # To use jar in S3 bucket, set
    # OPERATOR_EXECUTION_ROLE_ARN (--set emrContainers.operatorExecutionRoleArn=$`OPERATOR_EXECUTION_ROLE_ARN`)
    # when you install Spark operator
    jarURI: https://repo1.maven.org/maven2/org/apache/flink/flink-examples-streaming_2.12/1.16.1/flink-examples-streaming_2.12-1.16.1-TopSpeedWindowing.jar
    parallelism: 2
    upgradeMode: stateless
```

5. Submit the Flink session job with the following command. This will create a `FlinkSessionJob` object `basic-session-job`.

```
kubectl apply -f basic-session-job.yaml -n $NAMESPACE
```

6. Use the following command to confirm that the session cluster `LIFECYCLE` is `STABLE`, and the `JOB STATUS` is `RUNNING`:

```
kubectl get flinkdeployments.flink.apache.org basic-example-session-cluster -n `NAMESPACE`
```

The output should be similar to the following example:

```
NAME                              JOB STATUS   LIFECYCLE STATE
basic-example-session-cluster     RUNNING      STABLE
```

7. Access the Flink UI.

```
kubectl port-forward deployments/basic-example-session-cluster 8081 -n `NAMESPACE`
```

8. Open `localhost:8081` to view your Flink jobs locally.
9. Clean up the job. Remember to clean up the S3 artifacts that were created for this
   job, such as checkpointing, high-availability, savepointing metadata, and CloudWatch
   logs.
