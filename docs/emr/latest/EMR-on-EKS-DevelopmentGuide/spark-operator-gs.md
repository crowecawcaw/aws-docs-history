# Getting started with the Spark operator for

Amazon EMR on EKS

This topic helps you start to use the Spark operator on Amazon EKS by deploying a Spark
application and a Schedule Spark application.

## Install the Spark operator

Use the following steps to install the Kubernetes operator for Apache Spark.

1. If you haven't already, complete the steps in [Setting up the Spark operator for Amazon EMR on EKS](spark-operator-setup.md "spark-operator-setup.md").
2. Authenticate your Helm client to the Amazon ECR registry. In the following command,
   replace the `region-id` values with your preferred
   AWS Region, and the corresponding `ECR-registry-account`
   value for the Region from the [Amazon ECR registry accounts by Region](docker-custom-images-tag.md#docker-custom-images-ECR "docker-custom-images-tag.md#docker-custom-images-ECR") page.

```
aws ecr get-login-password \
--region `region-id` | helm registry login \
--username AWS \
--password-stdin `ECR-registry-account`.dkr.ecr.`region-id`.amazonaws.com
```

3. Install the Spark operator with the following command.

For the Helm chart `--version` parameter, use your Amazon EMR release label with the `emr-` prefix and date suffix removed. For example, with the `emr-6.12.0-java17-latest` release, specify `6.12.0-java17`. The example in the following command uses the `emr-7.12.0-latest` release, so it specifies `7.12.0` for the Helm chart `--version`.

```
helm install spark-operator-demo \
  oci://895885662937.dkr.ecr.`region-id`.amazonaws.com/spark-operator \
  --set emrContainers.awsRegion=`region-id` \
  --version `7.12.0` \
  --namespace spark-operator \
  --create-namespace
```

By default, the command creates service account
`emr-containers-sa-spark-operator` for the Spark operator. To use a
different service account, provide the argument
`serviceAccounts.sparkoperator.name`. For example:

```
--set serviceAccounts.sparkoperator.name `my-service-account-for-spark-operator`
```

If you want to use vertical autoscaling with
the Spark operator, add the following line to the installation command to
allow webhooks for the operator:

```
--set webhook.enable=true
```

4. Verify that you installed the Helm chart with the `helm list`
   command:

```
helm list --namespace spark-operator -o yaml
```

The `helm list` command should return your newly-deployed Helm chart
release information:

```
app_version: v1beta2-1.3.8-3.1.1
chart: spark-operator-`7.12.0`
name: spark-operator-demo
namespace: spark-operator
revision: "1"
status: deployed
updated: 2023-03-14 18:20:02.721638196 +0000 UTC
```

5. Complete installation with any additional options that you require. For more
   informtation, see the [`spark-on-k8s-operator`](https://github.com/GoogleCloudPlatform/spark-on-k8s-operator/blob/master/charts/spark-operator-chart/README.md "https://github.com/GoogleCloudPlatform/spark-on-k8s-operator/blob/master/charts/spark-operator-chart/README.md") documentation on GitHub.

## Run a Spark application

The Spark operator is supported with Amazon EMR 6.10.0 or higher. When you install the
Spark operator, it creates the service account `emr-containers-sa-spark` to
run Spark applications by default. Use the following steps to run a Spark application
with the Spark operator on Amazon EMR on EKS 6.10.0 or higher.

1. Before you can run a Spark application with the Spark operator, complete the
   steps in [Setting up the Spark operator for Amazon EMR on EKS](spark-operator-setup.md "spark-operator-setup.md")
   and [Install the Spark operator](#spark-operator-install "#spark-operator-install").
2. Create a `SparkApplication` definition file
   `spark-pi.yaml` with the following example contents:

```
apiVersion: "sparkoperator.k8s.io/v1beta2"
kind: SparkApplication
metadata:
  name: spark-pi
  namespace: spark-operator
spec:
  type: Scala
  mode: cluster
  image: "895885662937.dkr.ecr.us-west-2.amazonaws.com/spark/emr-6.10.0:latest"
  imagePullPolicy: Always
  mainClass: org.apache.spark.examples.SparkPi
  mainApplicationFile: "local:///usr/lib/spark/examples/jars/spark-examples.jar"
  sparkVersion: "3.3.1"
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
      version: 3.3.1
    serviceAccount: emr-containers-sa-spark
    volumeMounts:
      - name: "test-volume"
        mountPath: "/tmp"
  executor:
    cores: 1
    instances: 1
    memory: "512m"
    labels:
      version: 3.3.1
    volumeMounts:
      - name: "test-volume"
        mountPath: "/tmp"
```

3. Now, submit the Spark application with the following command. This will also
   create a `SparkApplication` object named `spark-pi`:

```
kubectl apply -f spark-pi.yaml
```

4. Check events for the `SparkApplication` object with the following
   command:

```
kubectl describe sparkapplication spark-pi --namespace spark-operator
```

For more information on submitting applications to Spark through the Spark operator,
see [Using a `SparkApplication`](https://www.kubeflow.org/docs/components/spark-operator/user-guide/using-sparkapplication/ "https://www.kubeflow.org/docs/components/spark-operator/user-guide/using-sparkapplication/") in the
`spark-on-k8s-operator` documentation on GitHub.

## Use Amazon S3 for storage

To use Amazon S3 as your file storage option, add the following configurations to your YAML file.

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

If you use Amazon EMR releases 7.2.0 and higher, the configurations are included by default. In that case, you can set the file path
to `s3://`<bucket_name>`/`<file_path>`` instead of
 `local://`<file_path>`` in the Spark application YAML file.

Then submit the Spark application as normal.
