# Getting started with spark-submit for Amazon EMR on EKS

Amazon EMR 6.10.0 and higher supports spark-submit for running Spark applications on an
Amazon EKS cluster. The section that follows shows you how to submit a command for a Spark application.

## Run a Spark application

To run the Spark application, follow these steps:

1. Before you can run a Spark application with the `spark-submit`
   command, complete the steps in [Setting up spark-submit for Amazon EMR on EKS](spark-submit-setup.md "spark-submit-setup.md").
2. Run a container with an Amazon EMR on EKS base image. See [How to select a base image URI](docker-custom-images-tag.md "docker-custom-images-tag.md") for more information.

```
kubectl run -it `containerName` --image=`EMRonEKSImage` --command -n `namespace` /bin/bash
```

3. Set the values for the following environment variables:

```
export SPARK_HOME=`spark-home`
export MASTER_URL=k8s://`Amazon EKS-cluster-endpoint`
```

4. Now, submit the Spark application with the following command:

```
$SPARK_HOME/bin/spark-submit \
 --class org.apache.spark.examples.SparkPi \
 --master $MASTER_URL \
 --conf spark.kubernetes.container.image=895885662937.dkr.ecr.us-west-2.amazonaws.com/spark/emr-6.10.0:latest \
 --conf spark.kubernetes.authenticate.driver.serviceAccountName=spark \
 --deploy-mode cluster \
 --conf spark.kubernetes.namespace=spark-operator \
 local:///usr/lib/spark/examples/jars/spark-examples.jar 20
```

For more information about submitting applications to Spark, see [Submitting
applications](https://spark.apache.org/docs/latest/submitting-applications.html "https://spark.apache.org/docs/latest/submitting-applications.html") in the Apache Spark documentation.

###### Important

`spark-submit` only supports cluster mode as the submission
mechanism.
