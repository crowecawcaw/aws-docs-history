# Using RAPIDS Accelerator for Apache Spark with

Amazon EMR on EKS

With Amazon EMR on EKS, you can run jobs for the Nvidia RAPIDS Accelerator for Apache Spark. This
tutorial covers how to run Spark jobs using RAPIDS on EC2 graphics processing unit (GPU)
instance types. The tutorial uses the following versions:

- Amazon EMR on EKS release version 6.9.0 and later
- Apache Spark 3.x
  You can accelerate Spark with Amazon EC2 GPU instance types by using the Nvidia [RAPIDS Accelerator for Apache
  Spark](https://docs.nvidia.com/spark-rapids/user-guide/latest/overview.html "https://docs.nvidia.com/spark-rapids/user-guide/latest/overview.html") plugin. When you use these technologies together, you accelerate your data
  science pipelines without having to make any code changes. This reduces the run time needed
  for data processing and model training. By getting more done in less time, you spend less on
  the cost of infrastructure.

Before you begin, make sure you have the following resources.

- Amazon EMR on EKS virtual cluster
- Amazon EKS cluster with a GPU enabled node group
  An Amazon EKS virtual cluster is a registered handle to the Kubernetes namespace on an Amazon EKS
  cluster, and is managed by Amazon EMR on EKS. The handle allows Amazon EMR to use the Kubernetes
  namespace as a destination for running jobs. For more information on how to set up a virtual
  cluster, see [Setting up Amazon EMR on EKS](setting-up.md "setting-up.md") in this guide.

You must configure the Amazon EKS virtual cluster with a node group that has GPU instances. You
must configure the nodes with an Nvidia device plugin. See [managed node groups](../../../eks/latest/userguide/managed-node-groups.md "../../../eks/latest/userguide/managed-node-groups.md") to learn
more.

To configure your Amazon EKS cluster to add GPU-enabled node groups, perform the following
procedure:

###### To add GPU enabled node groups

1. Create a GPU-enabled node group with the following [create-nodegroup](../../../cli/latest/reference/eks/create-nodegroup.md "../../../cli/latest/reference/eks/create-nodegroup.md")
   command. Be sure to substitute the correct parameters for your Amazon EKS cluster. Use an
   instance type that supports Spark RAPIDS, such as P4, P3, G5 or G4dn.

```
aws eks create-nodegroup \
 --cluster-name `EKS_CLUSTER_NAME` \
 --nodegroup-name `NODEGROUP_NAME` \
 --scaling-config minSize=0,maxSize=5,desiredSize=2 `CHOOSE_APPROPRIATELY` \
 --ami-type AL2_x86_64_GPU \
 --node-role `NODE_ROLE` \
 --subnets `SUBNETS_SPACE_DELIMITED`  \
 --remote-access ec2SshKey= `SSH_KEY` \
 --instance-types `GPU_INSTANCE_TYPE` \
 --disk-size `DISK_SIZE` \
 --region `AWS_REGION`
```

2. Install the Nvidia device plugin in your cluster to emit the number of GPUs on
   each node of your cluster and to run GPU-enabled containers in your cluster. Run the
   following code to install the plugin:

```
kubectl apply -f https://raw.githubusercontent.com/NVIDIA/k8s-device-plugin/v0.9.0/nvidia-device-plugin.yml
```

3. To validate how many GPUs are available on each node of your cluster, run the
   following command:

```
kubectl get nodes  "-o=custom-columns=NAME:.metadata.name,GPU:.status.allocatable.nvidia\.com/gpu"
```

###### To run a Spark RAPIDS job

1. Submit a Spark RAPIDS job to your Amazon EMR on EKS cluster. The following code shows an
   example of a command to start the job. The first time you run the job, it might take
   a few minutes to download the image and cache it on the node.

```
aws emr-containers start-job-run \
--virtual-cluster-id `VIRTUAL_CLUSTER_ID` \
--execution-role-arn `JOB_EXECUTION_ROLE` \
--release-label emr-6.9.0-spark-rapids-latest \
--job-driver '{"sparkSubmitJobDriver": {"entryPoint": "local:///usr/lib/spark/examples/jars/spark-examples.jar","entryPointArguments":  ["10000"], "sparkSubmitParameters":"--class org.apache.spark.examples.SparkPi "}}' \
---configuration-overrides '{"applicationConfiguration": [{"classification": "spark-defaults","properties": {"spark.executor.instances": "2","spark.executor.memory": "2G"}}],"monitoringConfiguration": {"cloudWatchMonitoringConfiguration": {"logGroupName": "`LOG_GROUP _NAME`"},"s3MonitoringConfiguration": {"logUri": "`LOG_GROUP_STREAM`"}}}'
```

2. To validate that the Spark RAPIDS Accelerator is enabled, check the Spark driver
   logs. These logs are stored either in CloudWatch or in the S3 location you specify
   when you run the `start-job-run` command. The following example generally
   shows what the log lines look like:

```
22/11/15 00:12:44 INFO RapidsPluginUtils: RAPIDS Accelerator build: {version=22.08.0-amzn-0, user=release, url=, date=2022-11-03T03:32:45Z, revision=, cudf_version=22.08.0, branch=}
22/11/15 00:12:44 INFO RapidsPluginUtils: RAPIDS Accelerator JNI build: {version=22.08.0, user=, url=https://github.com/NVIDIA/spark-rapids-jni.git, date=2022-08-18T04:14:34Z, revision=a1b23cd_sample, branch=HEAD}
22/11/15 00:12:44 INFO RapidsPluginUtils: cudf build: {version=22.08.0, user=, url=https://github.com/rapidsai/cudf.git, date=2022-08-18T04:14:34Z, revision=a1b23ce_sample, branch=HEAD}
22/11/15 00:12:44 WARN RapidsPluginUtils: RAPIDS Accelerator 22.08.0-amzn-0 using cudf 22.08.0.
22/11/15 00:12:44 WARN RapidsPluginUtils: spark.rapids.sql.multiThreadedRead.numThreads is set to 20.
22/11/15 00:12:44 WARN RapidsPluginUtils: RAPIDS Accelerator is enabled, to disable GPU support set `spark.rapids.sql.enabled` to false.
22/11/15 00:12:44 WARN RapidsPluginUtils: spark.rapids.sql.explain is set to `NOT_ON_GPU`. Set it to 'NONE' to suppress the diagnostics logging about the query placement on the GPU.
```

3. To see the operations that will be run on a GPU, perform the following steps to
   enable extra logging. Note the "`spark.rapids.sql.explain :
ALL`" config.

```
aws emr-containers start-job-run \
--virtual-cluster-id `VIRTUAL_CLUSTER_ID` \
--execution-role-arn `JOB_EXECUTION_ROLE` \
--release-label emr-6.9.0-spark-rapids-latest \
--job-driver '{"sparkSubmitJobDriver": {"entryPoint": "local:///usr/lib/spark/examples/jars/spark-examples.jar","entryPointArguments":  ["10000"], "sparkSubmitParameters":"--class org.apache.spark.examples.SparkPi "}}' \
---configuration-overrides '{"applicationConfiguration": [{"classification": "spark-defaults","properties": {"spark.rapids.sql.explain":"ALL","spark.executor.instances": "2","spark.executor.memory": "2G"}}],"monitoringConfiguration": {"cloudWatchMonitoringConfiguration": {"logGroupName": "`LOG_GROUP_NAME`"},"s3MonitoringConfiguration": {"logUri": "`LOG_GROUP_STREAM`"}}}'
```

The previous command is an example of a job that uses the GPU. Its output would
look something like the example below. Refer to this key for help to understand the
output:

    * `*` – marks an operation that works on a GPU
    * `!` – marks an operation that can't run on a GPU
    * `@` – marks an operation that works on a GPU, but won't
     get to run because it's inside a plan that can't run on a GPU

```

 22/11/15 01:22:58 INFO GpuOverrides: Plan conversion to the GPU took 118.64 ms
 22/11/15 01:22:58 INFO GpuOverrides: Plan conversion to the GPU took 4.20 ms
 22/11/15 01:22:58 INFO GpuOverrides: GPU plan transition optimization took 8.37 ms
 22/11/15 01:22:59 WARN GpuOverrides:
    *Exec <ProjectExec> will run on GPU
      *Expression <Alias> substring(cast(date#149 as string), 0, 7) AS month#310 will run on GPU
        *Expression <Substring> substring(cast(date#149 as string), 0, 7) will run on GPU
          *Expression <Cast> cast(date#149 as string) will run on GPU
      *Exec <SortExec> will run on GPU
        *Expression <SortOrder> date#149 ASC NULLS FIRST will run on GPU
        *Exec <ShuffleExchangeExec> will run on GPU
          *Partitioning <RangePartitioning> will run on GPU
            *Expression <SortOrder> date#149 ASC NULLS FIRST will run on GPU
          *Exec <UnionExec> will run on GPU
            !Exec <ProjectExec> cannot run on GPU because not all expressions can be replaced
              @Expression <AttributeReference> customerID#0 could run on GPU
              @Expression <Alias> Charge AS kind#126 could run on GPU
                @Expression <Literal> Charge could run on GPU
              @Expression <AttributeReference> value#129 could run on GPU
              @Expression <Alias> add_months(2022-11-15, cast(-(cast(_we0#142 as bigint) + last_month#128L) as int)) AS date#149 could run on GPU
                ! <AddMonths> add_months(2022-11-15, cast(-(cast(_we0#142 as bigint) + last_month#128L) as int)) cannot run on GPU because GPU does not currently support the operator class org.apache.spark.sql.catalyst.expressions.AddMonths
                  @Expression <Literal> 2022-11-15 could run on GPU
                  @Expression <Cast> cast(-(cast(_we0#142 as bigint) + last_month#128L) as int) could run on GPU
                    @Expression <UnaryMinus> -(cast(_we0#142 as bigint) + last_month#128L) could run on GPU
                      @Expression <Add> (cast(_we0#142 as bigint) + last_month#128L) could run on GPU
                        @Expression <Cast> cast(_we0#142 as bigint) could run on GPU
                          @Expression <AttributeReference> _we0#142 could run on GPU
                        @Expression <AttributeReference> last_month#128L could run on GPU
```
