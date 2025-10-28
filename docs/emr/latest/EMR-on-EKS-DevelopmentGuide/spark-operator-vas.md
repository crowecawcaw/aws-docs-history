# Use vertical autoscaling with the Spark operator for

Amazon EMR on EKS

Starting with Amazon EMR 7.0, you can use Amazon EMR on EKS vertical autoscaling to simplify resource management. It automatically tunes
memory and CPU resources to adapt to the needs of the workload that you provide for Amazon EMR
Spark applications. For more information, see [Using vertical autoscaling with Amazon EMR Spark jobs](jobruns-vas.md "jobruns-vas.md").

This section describes how to configure the Spark operator to use vertical
autoscaling.

## Prerequisites

Before you configure monitoring, be sure to complete the following setup tasks:

- Complete the steps in [Setting up the Spark operator for Amazon EMR on EKS](spark-operator-setup.md "spark-operator-setup.md").
- (optional) If you previously installed an older version of the Spark operator,
  delete the SparkApplication/ScheduledSparkApplication CRD.

```
kubectl delete crd sparkApplication
kubectl delete crd scheduledSparkApplication
```

- Complete the steps in [Install the Spark operator](spark-operator-gs.md#spark-operator-install "spark-operator-gs.md#spark-operator-install"). In step 3, add the following line to the
  installation command to allow webhooks for the operator:

```
--set webhook.enable=true
```

- Complete the steps in [Setting up vertical autoscaling for Amazon EMR on EKS](jobruns-vas-setup.md "jobruns-vas-setup.md").
- Give access to the files in your Amazon S3 location:
  1.  Annotate your driver and operator service account with the `JobExecutionRole` that
      has S3 permissions.

  ```
  kubectl annotate serviceaccount -n spark-operator emr-containers-sa-spark eks.amazonaws.com/role-arn=`JobExecutionRole`
  kubectl annotate serviceaccount -n spark-operator emr-containers-sa-spark-operator eks.amazonaws.com/role-arn=`JobExecutionRole`
  ```

  2.  Update the trust policy of your job execution role in that namespace.

  ```
  aws emr-containers update-role-trust-policy \
  --cluster-name cluster \
  --namespace ${Namespace}\
  --role-name iam_role_name_for_job_execution
  ```

  3.  Edit the IAM role trust policy of your job execution role and update the `serviceaccount` from
      `emr-containers-sa-spark-*-*-xxxx` to `emr-containers-sa-*`.

  ```
  {
      "Effect": "Allow",
      "Principal": {
          "Federated": "`OIDC-provider`"
      },
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Condition": {
          "StringLike": {
              "`OIDC`": "system:serviceaccount:${Namespace}:emr-containers-sa-*"
          }
      }
  }
  ```

  4.  If you're using Amazon S3 as your file storage, add the following defaults to your yaml file.

  ```
  hadoopConf:
  # EMRFS filesystem
    fs.s3.customAWSCredentialsProvider: com.amazonaws.auth.WebIdentityTokenCredentialsProvider
    fs.s3.impl: com.amazon.ws.emr.hadoop.fs.EmrFileSystem
    fs.AbstractFileSystem.s3.impl: org.apache.hadoop.fs.s3.EMRFSDelegate
    fs.s3.buffer.dir: /mnt/s3
    fs.s3.getObject.initialSocketTimeoutMilliseconds: "2000"
    mapreduce.fileoutputcommitter.algorithm.version.emr_internal_use_only.EmrFileSystem: "2"
    mapreduce.fileoutputcommitter.cleanup-failures.ignored.emr_internal_use_only.EmrFileSystem: "true"
  sparkConf:
   # Required for EMR Runtime
   spark.driver.extraClassPath: /usr/lib/hadoop-lzo/lib/*:/usr/lib/hadoop/hadoop-aws.jar:/usr/share/aws/aws-java-sdk/*:/usr/share/aws/emr/emrfs/conf:/usr/share/aws/emr/emrfs/lib/*:/usr/share/aws/emr/emrfs/auxlib/*:/usr/share/aws/emr/security/conf:/usr/share/aws/emr/security/lib/*:/usr/share/aws/hmclient/lib/aws-glue-datacatalog-spark-client.jar:/usr/share/java/Hive-JSON-Serde/hive-openx-serde.jar:/usr/share/aws/sagemaker-spark-sdk/lib/sagemaker-spark-sdk.jar:/home/hadoop/extrajars/*
   spark.driver.extraLibraryPath: /usr/lib/hadoop/lib/native:/usr/lib/hadoop-lzo/lib/native:/docker/usr/lib/hadoop/lib/native:/docker/usr/lib/hadoop-lzo/lib/native
   spark.executor.extraClassPath: /usr/lib/hadoop-lzo/lib/*:/usr/lib/hadoop/hadoop-aws.jar:/usr/share/aws/aws-java-sdk/*:/usr/share/aws/emr/emrfs/conf:/usr/share/aws/emr/emrfs/lib/*:/usr/share/aws/emr/emrfs/auxlib/*:/usr/share/aws/emr/security/conf:/usr/share/aws/emr/security/lib/*:/usr/share/aws/hmclient/lib/aws-glue-datacatalog-spark-client.jar:/usr/share/java/Hive-JSON-Serde/hive-openx-serde.jar:/usr/share/aws/sagemaker-spark-sdk/lib/sagemaker-spark-sdk.jar:/home/hadoop/extrajars/*
   spark.executor.extraLibraryPath: /usr/lib/hadoop/lib/native:/usr/lib/hadoop-lzo/lib/native:/docker/usr/lib/hadoop/lib/native:/docker/usr/lib/hadoop-lzo/lib/native
  ```

## Run a job with vertical autoscaling on the Spark

operator

Before you can run a Spark application with the Spark operator, you must complete the
steps in [Prerequisites](#spark-operator-vas-prereqs "#spark-operator-vas-prereqs").

To use vertical autoscaling with the Spark operator, add the following configuration to the driver
for your Spark Application spec to turn on vertical autoscaling:

```
dynamicSizing:
  mode: Off
  signature: "my-signature"
```

This configuration enables vertical autoscaling and is a required signature configuration
that lets you choose a signature for your job.

For more information on the configurations and parameter values, see
[Configuring vertical autoscaling for Amazon EMR on EKS](jobruns-vas-configure.md "jobruns-vas-configure.md").
By default, your job submits in the monitoring-only **Off**
mode of vertical autoscaling. This monitoring state lets you compute and view resource recommendations
without performing autoscaling. For more information, see [Vertical autoscaling modes](jobruns-vas-configure.md#jobruns-vas-parameters-opt-mode "jobruns-vas-configure.md#jobruns-vas-parameters-opt-mode").

The following is a sample `SparkApplication` definition file named `spark-pi.yaml`
with the required configurations to use vertical autoscaling.

```
apiVersion: "sparkoperator.k8s.io/v1beta2"
kind: SparkApplication
metadata:
  name: spark-pi
  namespace: spark-operator
spec:
  type: Scala
  mode: cluster
  image: "895885662937.dkr.ecr.us-west-2.amazonaws.com/spark/emr-7.9.0:latest"
  imagePullPolicy: Always
  mainClass: org.apache.spark.examples.SparkPi
  mainApplicationFile: "local:///usr/lib/spark/examples/jars/spark-examples.jar"
  sparkVersion: "3.4.1"
  dynamicSizing:
    mode: Off
    signature: "my-signature"
  restartPolicy:
    type: Never
  volumes:
    - name: "test-volume"
      hostPath:
        path: "/tmp"
        type: Directory
  driver:
    cores: 1
    coreLimit: "1200m"
    memory: "512m"
    labels:
      version: 3.4.1
    serviceAccount: emr-containers-sa-spark
    volumeMounts:
      - name: "test-volume"
        mountPath: "/tmp"
  executor:
    cores: 1
    instances: 1
    memory: "512m"
    labels:
      version: 3.4.1
    volumeMounts:
      - name: "test-volume"
        mountPath: "/tmp"
```

Now, submit the Spark application with the following command. This will also create a
`SparkApplication` object named `spark-pi`:

```
kubectl apply -f spark-pi.yaml
```

For more information on submitting applications to Spark through the Spark operator,
see [Using a `SparkApplication`](https://www.kubeflow.org/docs/components/spark-operator/user-guide/using-sparkapplication/ "https://www.kubeflow.org/docs/components/spark-operator/user-guide/using-sparkapplication/") in the `spark-on-k8s-operator`
documentation on GitHub.

## Verifying the vertical autoscaling

functionality

To verify that vertical autoscaling works correctly for the submitted job, use kubectl
to get the `verticalpodautoscaler` custom resource and view your scaling
recommendations.

```
kubectl get verticalpodautoscalers --all-namespaces \
-l=emr-containers.amazonaws.com/dynamic.sizing.signature=`my-signature`
```

The output from this query should resemble the following:

```
NAMESPACE        NAME                                                          MODE   CPU   MEM         PROVIDED   AGE
spark-operator   ds-p73j6mkosvc4xeb3gr7x4xol2bfcw5evqimzqojrlysvj3giozuq-vpa   Off          580026651   True       15m
```

If your output doesn't look similar or contains an error code, see [Troubleshooting Amazon EMR on EKS vertical
autoscaling](troubleshooting-vas.md "troubleshooting-vas.md") for steps to help
resolve the issue.

To remove the pods and applications, run the following command:

```
kubectl delete sparkapplication spark-pi
```
