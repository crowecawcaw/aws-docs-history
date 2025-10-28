# Using pod templates

Beginning with Amazon EMR versions 5.33.0 or 6.3.0, Amazon EMR on EKS supports Spark’s pod template
feature. A pod is a group of one or more containers, with shared storage and network
resources, and a specification for how to run the containers. Pod templates are specifications
that determine how to run each pod. You can use pod template files to define the driver or
executor pod’s configurations that Spark configurations do not support. For more information
about the Spark’s pod template feature, see [Pod
Template](https://spark.apache.org/docs/latest/running-on-kubernetes.html#pod-template "https://spark.apache.org/docs/latest/running-on-kubernetes.html#pod-template").

###### Note

The pod template feature only works with driver and executor pods. You cannot configure
job submitter pods using the pod template.

## Common scenarios

You can define how to run Spark jobs on shared EKS clusters by using pod templates with
Amazon EMR on EKS and save costs and improve resource utilization and performance.

- To reduce costs, you can schedule Spark driver tasks to run on Amazon EC2 On-Demand
  Instances while scheduling Spark executor tasks to run on Amazon EC2 Spot Instances.
- To increase resource utilization, you can support multiple teams running their
  workloads on the same EKS cluster. Each team will get a designated Amazon EC2 node group to
  run their workloads on. You can use pod templates to apply a corresponding toleration to
  their workload.
- To improve monitoring, you can run a separate logging container to forward logs to
  your existing monitoring application.

For example, the following pod template file demonstrates a common usage scenario.

```
apiVersion: v1
kind: Pod
spec:
  volumes:
    - name: source-data-volume
      emptyDir: {}
    - name: metrics-files-volume
      emptyDir: {}
  nodeSelector:
    eks.amazonaws.com/nodegroup: emr-containers-nodegroup
  containers:
  - name: spark-kubernetes-driver # This will be interpreted as driver Spark main container
    env:
      - name: RANDOM
        value: "random"
    volumeMounts:
      - name: shared-volume
        mountPath: /var/data
      - name: metrics-files-volume
        mountPath: /var/metrics/data
  - name: custom-side-car-container # Sidecar container
    image: <side_car_container_image>
    env:
      - name: RANDOM_SIDECAR
        value: random
    volumeMounts:
      - name: metrics-files-volume
        mountPath: /var/metrics/data
    command:
      - /bin/sh
      - '-c'
      -  <command-to-upload-metrics-files>
  initContainers:
  - name: spark-init-container-driver # Init container
    image: <spark-pre-step-image>
    volumeMounts:
      - name: source-data-volume # Use EMR predefined volumes
        mountPath: /var/data
    command:
      - /bin/sh
      - '-c'
      -  <command-to-download-dependency-jars>

```

The pod template completes the following tasks:

- Add a new [init
  container](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/ "https://kubernetes.io/docs/concepts/workloads/pods/init-containers/") that is executed before the Spark main container starts. The init
  container shares the [EmptyDir
  volume](https://kubernetes.io/docs/concepts/storage/volumes/#emptydir "https://kubernetes.io/docs/concepts/storage/volumes/#emptydir") called `source-data-volume` with the Spark main container.
  You can have your init container run initialization steps, such as downloading
  dependencies or generating input data. Then the Spark main container consumes the
  data.
- Add another [sidecar container](https://kubernetes.io/docs/concepts/workloads/pods/#how-pods-manage-multiple-containers "https://kubernetes.io/docs/concepts/workloads/pods/#how-pods-manage-multiple-containers") that is executed along with the Spark main container. The
  two containers are sharing another `EmptyDir` volume called
  `metrics-files-volume`. Your Spark job can generate metrics, such as
  Prometheus metrics. Then the Spark job can put the metrics into a file and have the
  sidecar container upload the files to your own BI system for future analysis.
- Add a new environment variable to the Spark main container. You can have your job
  consume the environment variable.
- Define a [node
  selector](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/ "https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/"), so that the pod is only scheduled on the
  `emr-containers-nodegroup` node group. This helps to isolate compute
  resources across jobs and teams.

## Enabling pod templates with Amazon EMR on EKS

To enable the pod template feature with Amazon EMR on EKS, configure the Spark properties
`spark.kubernetes.driver.podTemplateFile` and
`spark.kubernetes.executor.podTemplateFile` to point to the pod template files
in Amazon S3. Spark then downloads the pod template file and uses it to construct driver and
executor pods.

###### Note

Spark uses the job execution role to load the pod template, so the job execution role
must have permissions to access Amazon S3 to load the pod templates. For more information, see
[Create a job execution role](creating-job-execution-role.md "creating-job-execution-role.md").

You can use the `SparkSubmitParameters` to specify the Amazon S3 path to the pod
template, as the following job run JSON file demonstrates.

```
{
  "name": "myjob",
  "virtualClusterId": "123456",
  "executionRoleArn": "iam_role_name_for_job_execution",
  "releaseLabel": "`release_label`",
  "jobDriver": {
    "sparkSubmitJobDriver": {
      "entryPoint": "entryPoint_location",
      "entryPointArguments": ["`argument1`", "`argument2`", ...],
       "sparkSubmitParameters": "--class <main_class> \
         --conf spark.kubernetes.driver.podTemplateFile=s3://`path_to_driver_pod_template` \
         --conf spark.kubernetes.executor.podTemplateFile=s3://`path_to_executor_pod_template` \
         --conf spark.executor.instances=2 \
         --conf spark.executor.memory=2G \
         --conf spark.executor.cores=2 \
         --conf spark.driver.cores=1"
    }
  }
}
```

Alternatively, you can use the `configurationOverrides` to specify the Amazon S3
path to the pod template, as the following job run JSON file demonstrates.

```
{
  "name": "myjob",
  "virtualClusterId": "123456",
  "executionRoleArn": "iam_role_name_for_job_execution",
  "releaseLabel": "`release_label`",
  "jobDriver": {
    "sparkSubmitJobDriver": {
      "entryPoint": "entryPoint_location",
      "entryPointArguments": ["`argument1`", "`argument2`", ...],
       "sparkSubmitParameters": "--class <main_class> \
         --conf spark.executor.instances=2 \
         --conf spark.executor.memory=2G \
         --conf spark.executor.cores=2 \
         --conf spark.driver.cores=1"
    }
  },
  "configurationOverrides": {
    "applicationConfiguration": [
      {
        "classification": "spark-defaults",
        "properties": {
          "spark.driver.memory":"2G",
          "spark.kubernetes.driver.podTemplateFile":"s3://`path_to_driver_pod_template`",
          "spark.kubernetes.executor.podTemplateFile":"s3://`path_to_executor_pod_template`"
         }
      }
    ]
  }
}
```

###### Note

1. You need to follow the security guidelines when using the pod template feature
   with Amazon EMR on EKS, such as isolating untrusted application code. For more information,
   see [Amazon EMR on EKS security best practices](security-best-practices.md "security-best-practices.md").
2. You cannot change the Spark main container names by using
   `spark.kubernetes.driver.podTemplateContainerName` and
   `spark.kubernetes.executor.podTemplateContainerName`, because these names
   are hardcoded as `spark-kubernetes-driver` and
   `spark-kubernetes-executors`. If you want to customize the Spark main
   container, you must specify the container in a pod template with these hardcoded
   names.

## Pod template fields

Consider the following field restrictions when configuring a pod template with
Amazon EMR on EKS.

- Amazon EMR on EKS allows only the following fields in a pod template to enable proper job
  scheduling.

These are the allowed pod level fields:

    + `apiVersion`
    + `kind`
    + `metadata`
    + `spec.activeDeadlineSeconds`
    + `spec.affinity`
    + `spec.containers`
    + `spec.enableServiceLinks`
    + `spec.ephemeralContainers`
    + `spec.hostAliases`
    + `spec.hostname`
    + `spec.imagePullSecrets`
    + `spec.initContainers`
    + `spec.nodeName`
    + `spec.nodeSelector`
    + `spec.overhead`
    + `spec.preemptionPolicy`
    + `spec.priority`
    + `spec.priorityClassName`
    + `spec.readinessGates`
    + `spec.runtimeClassName`
    + `spec.schedulerName`
    + `spec.subdomain`
    + `spec.terminationGracePeriodSeconds`
    + `spec.tolerations`
    + `spec.topologySpreadConstraints`
    + `spec.volumes`

These are the allowed Spark main container level fields:

    + `env`
    + `envFrom`
    + `name`
    + `lifecycle`
    + `livenessProbe`
    + `readinessProbe`
    + `resources`
    + `startupProbe`
    + `stdin`
    + `stdinOnce`
    + `terminationMessagePath`
    + `terminationMessagePolicy`
    + `tty`
    + `volumeDevices`
    + `volumeMounts`
    + `workingDir`

When you use any disallowed fields in the pod template, Spark throws an exception
and the job fails. The following example shows an error message in the Spark controller
log due to disallowed fields.

```
Executor pod template validation failed.
Field container.command in Spark main container not allowed but specified.
```

- Amazon EMR on EKS predefines the following parameters in a pod template. The fields that
  you specify in a pod template must not overlap with these fields.

These are the predefined volume names:

    + `emr-container-communicate`
    + `config-volume`
    + `emr-container-application-log-dir`
    + `emr-container-event-log-dir`
    + `temp-data-dir`
    + `mnt-dir`
    + `home-dir`
    + `emr-container-s3`

These are the predefined volume mounts that only apply to the Spark main
container:

    + Name: `emr-container-communicate`; MountPath:
     `/var/log/fluentd`
    + Name: `emr-container-application-log-dir`; MountPath:
     `/var/log/spark/user`
    + Name: `emr-container-event-log-dir`; MountPath:
     `/var/log/spark/apps`
    + Name: `mnt-dir`; MountPath: `/mnt`
    + Name: `temp-data-dir`; MountPath: `/tmp`
    + Name: `home-dir`; MountPath: `/home/hadoop`

These are the predefined environment variables that only apply to the Spark main
container:

    + `SPARK_CONTAINER_ID`
    + `K8S_SPARK_LOG_URL_STDERR`
    + `K8S_SPARK_LOG_URL_STDOUT`
    + `SIDECAR_SIGNAL_FILE`

###### Note

You can still use these predefined volumes and mount them into your additional
sidecar containers. For example, you can use
`emr-container-application-log-dir` and mount it to your own sidecar
container defined in the pod template.

If the fields you specify conflict with any of the predefined fields in the pod
template, Spark throws an exception and the job fails. The following example shows an
error message in the Spark application log due to conflicts with the predefined fields.

```
Defined volume mount path on main container must not overlap with reserved mount paths: [<reserved-paths>]
```

## Sidecar container considerations

Amazon EMR controls the lifecycle of the pods provisioned by Amazon EMR on EKS. The sidecar
containers should follow the same lifecycle of the Spark main container. If you inject
additional sidecar containers into your pods, we recommend that you integrate with the pod
lifecycle management that Amazon EMR defines so that the sidecar container can stop itself when
the Spark main container exits.

To reduce costs, we recommend that you implement a process that prevents driver pods
with sidecar containers from continuing to run after your job completes. The Spark driver
deletes executor pods when the executor is done. However, when a driver program completes,
the additional sidecar containers continue to run. The pod is billed until Amazon EMR on EKS cleans
up the driver pod, usually less than one minute after the driver Spark main container
completes. To reduce costs, you can integrate your additional sidecar containers with the
lifecycle management mechanism that Amazon EMR on EKS defines for both driver and executor pods, as
described in the following section.

Spark main container in driver and executor pods sends `heartbeat` to a file
`/var/log/fluentd/main-container-terminated` every two seconds. By adding the
Amazon EMR predefined `emr-container-communicate` volume mount to your sidecar
container, you can define a sub-process of your sidecar container to periodically track the
last modified time for this file. The sub-process then stops itself if it discovers that the
Spark main container stops the `heartbeat` for a longer duration.

The following example demonstrates a sub-process that tracks the heartbeat file and
stops itself. Replace `your_volume_mount` with the path where you
mount the predefined volume. The script is bundled inside the image used by sidecar
container. In a pod template file, you can specify a sidecar container with the following
commands `sub_process_script.sh` and `main_command`.

```
MOUNT_PATH="`your_volume_mount`"
FILE_TO_WATCH="$MOUNT_PATH/main-container-terminated"
INITIAL_HEARTBEAT_TIMEOUT_THRESHOLD=60
HEARTBEAT_TIMEOUT_THRESHOLD=15
SLEEP_DURATION=10

function terminate_main_process() {
  # Stop main process
}

# Waiting for the first heartbeat sent by Spark main container
echo "Waiting for file $FILE_TO_WATCH to appear..."
start_wait=$(date +%s)
while ! [[ -f "$FILE_TO_WATCH" ]]; do
    elapsed_wait=$(expr $(date +%s) - $start_wait)
    if [ "$elapsed_wait" -gt "$INITIAL_HEARTBEAT_TIMEOUT_THRESHOLD" ]; then
        echo "File $FILE_TO_WATCH not found after $INITIAL_HEARTBEAT_TIMEOUT_THRESHOLD seconds; aborting"
        terminate_main_process
        exit 1
    fi
    sleep $SLEEP_DURATION;
done;
echo "Found file $FILE_TO_WATCH; watching for heartbeats..."

while [[ -f "$FILE_TO_WATCH" ]]; do
    LAST_HEARTBEAT=$(stat -c %Y $FILE_TO_WATCH)
    ELAPSED_TIME_SINCE_AFTER_HEARTBEAT=$(expr $(date +%s) - $LAST_HEARTBEAT)
    if [ "$ELAPSED_TIME_SINCE_AFTER_HEARTBEAT" -gt "$HEARTBEAT_TIMEOUT_THRESHOLD" ]; then
        echo "Last heartbeat to file $FILE_TO_WATCH was more than $HEARTBEAT_TIMEOUT_THRESHOLD seconds ago at $LAST_HEARTBEAT; terminating"
        terminate_main_process
        exit 0
    fi
    sleep $SLEEP_DURATION;
done;
echo "Outside of loop, main-container-terminated file no longer exists"

# The file will be deleted once the fluentd container is terminated

echo "The file $FILE_TO_WATCH doesn't exist any more;"
terminate_main_process
exit 0
```
