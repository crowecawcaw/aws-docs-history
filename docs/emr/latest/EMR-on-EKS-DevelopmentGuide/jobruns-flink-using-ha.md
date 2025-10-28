# Using high availability (HA) for Flink

Operators and Flink Applications

This topic shows how to configure high availability and describes how it works for a few different use cases. These include when you're using the Job manager and when you're
using Flink native kubernetes.

## Flink operator high-availability

We enable _high availability_ for the Flink Operator so that we can fail-over to a
standby Flink Operator to minimize downtime in the operator control loop if failures
occur. High availability is enabled by default and the default number of starting
operator replicas is 2. You can configure the replicas field in your
`values.yaml` file for the helm chart.

The following fields are customizable:

- `replicas` (optional, default is 2): Setting this number to
  greater than 1 creates other standby Operators and allows for faster
  recovery of your job.
- `highAvailabilityEnabled` (optional, default is true): Controls
  whether you want to enable HA. Specifying this parameter as true enables
  multi AZ deployment support, as well as sets the correct
  `flink-conf.yaml` parameters.

You can disable HA for your operator by setting the following configuration in
your `values.yaml` file.

```
...
imagePullSecrets: []

replicas: 1

# set this to false if you don't want HA
highAvailabilityEnabled: false
...
```

**Multi AZ deployment**

We create the operator pods in multiple Availability Zones. This is a soft
constraint, and your operator pods will be scheduled in the same AZ if you don't
have enough resources in a different AZ.

**Determining the leader replica**

If HA is enabled, the replicas use a lease to determine which of the JMs is the
leader and uses a K8s Lease for leader election. You can describe the Lease and look
at the .Spec.Holder Identity field to determine the current leader

```
kubectl describe lease <Helm Install Release Name>-<NAMESPACE>-lease -n <NAMESPACE> | grep "Holder Identity"
```

**Flink-S3 Interaction**

**Configuring access credentials**

Please make sure that you have configured IRSA with appropriate IAM permissions
to access the S3 bucket.

**Fetching job jars from S3 Application mode**

The Flink operator also supports fetching applications jars from S3. You just
provide the S3 location for the jarURI in your FlinkDeployment specification.

You can also use this feature to download other artifacts like PyFlink scripts.
The resulting Python script is dropped under the path
`/opt/flink/usrlib/`.

The following example demonstrates how to use this feature for a PyFlink job. Note
the jarURI and args fields.

```
apiVersion: flink.apache.org/v1beta1
kind: FlinkDeployment
metadata:
  name: python-example
spec:
  image: <YOUR CUSTOM PYFLINK IMAGE>
  emrReleaseLabel: "emr-6.12.0-flink-latest"
  flinkVersion: v1_16
  flinkConfiguration:
    taskmanager.numberOfTaskSlots: "1"
  serviceAccount: flink
  jobManager:
    highAvailabilityEnabled: false
    replicas: 1
    resource:
      memory: "2048m"
      cpu: 1
  taskManager:
    resource:
      memory: "2048m"
      cpu: 1
  job:
    jarURI: "s3://<S3-BUCKET>/scripts/pyflink.py" # Note, this will trigger the artifact download process
    entryClass: "org.apache.flink.client.python.PythonDriver"
    args: ["-pyclientexec", "/usr/local/bin/python3", "-py", "/opt/flink/usrlib/pyflink.py"]
    parallelism: 1
    upgradeMode: stateless
```

**Flink S3 Connectors**

Flink comes packaged with two S3 connectors (listed below). The following sections
discuss when to use which connector.

**Checkpointing: Presto S3 connector**

- Set S3 scheme to s3p://
- The recommended connector to use to checkpoint to s3. For more information, see
  [S3-specific](https://nightlies.apache.org/flink/flink-docs-master/docs/connectors/datastream/filesystem/#s3-specific "https://nightlies.apache.org/flink/flink-docs-master/docs/connectors/datastream/filesystem/#s3-specific")
  in the Apache Flink documentation.

Example FlinkDeployment specification:

```
apiVersion: flink.apache.org/v1beta1
kind: FlinkDeployment
metadata:
  name: basic-example
spec:
  flinkConfiguration:
    taskmanager.numberOfTaskSlots: "2"
    state.checkpoints.dir: s3p://<BUCKET-NAME>/flink-checkpoint/
```

**Reading and writing to S3: Hadoop S3 connector**

- Set S3 scheme to `s3://` or ( `s3a://` )
- The recommended connector for reading and writing files from S3 (only S3
  connector that implements the [Flinks Filesystem interface](https://nightlies.apache.org/flink/flink-docs-master/docs/connectors/datastream/filesystem/ "https://nightlies.apache.org/flink/flink-docs-master/docs/connectors/datastream/filesystem/")).
- By default, we set `fs.s3a.aws.credentials.provider` in the
  `flink-conf.yaml` file, which is
  `com.amazonaws.auth.WebIdentityTokenCredentialsProvider`. If
  you override the d efault `flink-conf` completely and you are
  interacting with S3, make sure to use this provider.

Example FlinkDeployment spec

```
apiVersion: flink.apache.org/v1beta1
kind: FlinkDeployment
metadata:
  name: basic-example
spec:
  job:
    jarURI: local:///opt/flink/examples/streaming/WordCount.jar
    args: [ "--input", "s3a://<INPUT BUCKET>/PATH", "--output", "s3a://<OUTPUT BUCKET>/PATH" ]
    parallelism: 2
    upgradeMode: stateless
```

## Flink Job Manager

High Availability (HA) for Flink Deployments allow jobs to continue making
progress even if a transient error is encountered and your JobManager crashes. The
jobs will restart but from the last successful checkpoint with HA enabled. Without
HA enabled, Kubernetes will restart your JobManager, but your job will start as a
fresh job and will lose its progress. After configuring HA, we can tell Kubernetes
to store the HA metadata in a persistent storage to reference in case of a transient
failure in the JobManager and then resume our jobs from the last successful
checkpoint.

HA is enabled by default for your Flink jobs (the replica count is set to 2, which
will require you to provide an S3 storage location for HA metadata to
persist).

**HA configs**

```
apiVersion: flink.apache.org/v1beta1
kind: FlinkDeployment
metadata:
  name: basic-example
spec:
  flinkConfiguration:
    taskmanager.numberOfTaskSlots: "2"
  executionRoleArn: "<JOB EXECUTION ROLE ARN>"
  emrReleaseLabel: "emr-6.13.0-flink-latest"
  jobManager:
    resource:
      memory: "2048m"
      cpu: 1
    replicas: 2
    highAvailabilityEnabled: true
    storageDir: "s3://<S3 PERSISTENT STORAGE DIR>"
  taskManager:
    resource:
      memory: "2048m"
      cpu: 1
```

The following are descriptions for the above HA configs in Job Manager (defined
under .spec.jobManager):

- `highAvailabilityEnabled` (optional, default is true): Set this
  to `false` if you don't want HA enabled and don’t want to use
  the provided HA configurations. You can still manipulate the "replicas"
  field to manually configure HA.
- `replicas` (optional, default is 2): Setting this number to
  greater than 1 creates other standby JobManagers and allows for faster
  recovery of your job. If you disable HA, you must set replica count to 1, or
  you will keep getting validation errors (only 1 replica is supported if HA
  is not enabled).
- `storageDir` (required): Because we use replica count as 2 by
  default, we have to provide a persistent storageDir. Currently this field
  only accepts S3 paths as the storage location.

**Pod locality**

If you enable HA, we also try to collocate pods in the same AZ, which leads to
improved performance (reduced network latency by having pods in same AZs). This is a
best-effort process, meaning if you don't have enough resources in the AZ where the
majority of your Pods are scheduled, the remaining Pods will still be scheduled but
might end up on a node outside of this AZ.

**Determining the leader replica**

If HA is enabled, the replicas use a lease to determine which of the JMs is the
leader and uses a K8s Configmap as the datastore to store this metadata. If you want
to determine the leader, you can look at the content of the Configmap and look at
the key `org.apache.flink.k8s.leader.restserver` under data to find the
K8s pod with the IP address. You can also use the following bash commands.

```
ip=$(kubectl get configmap -n <NAMESPACE> <JOB-NAME>-cluster-config-map -o json | jq -r ".data[\"org.apache.flink.k8s.leader.restserver\"]" | awk -F: '{print $2}' | awk -F '/' '{print $3}')
kubectl get pods -n `NAMESPACE`  -o json | jq -r ".items[] | select(.status.podIP == \"$ip\") | .metadata.name"
```

## Flink job - native Kubernetes

Amazon EMR 6.13.0 and higher supports Flink native Kubernetes for running Flink
applications in high-availability mode on an Amazon EKS cluster.

###### Note

You must have an Amazon S3 bucket created to store the high-availability metadata
when you submit your Flink job. If you don’t want to use this feature, you can
disable it. It's enabled by default.

To turn on the Flink high-availability feature, provide the following Flink
parameters when you [run
the run-application CLI command](jobruns-flink-native-kubernetes-getting-started.md#jobruns-flink-native-kubernetes-getting-started-run-application "jobruns-flink-native-kubernetes-getting-started.md#jobruns-flink-native-kubernetes-getting-started-run-application"). The parameters are defined
below the example.

```
-Dhigh-availability.type=kubernetes \
-Dhigh-availability.storageDir=`S3://DOC-EXAMPLE-STORAGE-BUCKET` \
-Dfs.s3a.aws.credentials.provider="com.amazonaws.auth.WebIdentityTokenCredentialsProvider" \
-Dkubernetes.jobmanager.replicas=3 \
-Dkubernetes.cluster-id=`example-cluster`
```

- `Dhigh-availability.storageDir`
  – The Amazon S3 bucket where you want to store the high-availability
  metadata for your job.

`Dkubernetes.jobmanager.replicas` – The
number of Job Manager pods to create as an integer greater than
`1`.

`Dkubernetes.cluster-id`
– A unique ID that identifies the Flink cluster.
