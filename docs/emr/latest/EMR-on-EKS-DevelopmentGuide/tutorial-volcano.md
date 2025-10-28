# Using Volcano as a custom scheduler for Apache Spark

on Amazon EMR on EKS

With Amazon EMR on EKS, you can use Spark operator or spark-submit to run Spark jobs with
Kubernetes custom schedulers. This tutorial covers how to run Spark jobs with a Volcano
scheduler on a custom queue.

## Overview

[Volcano](https://volcano.sh/en/ "https://volcano.sh/en/") can help manage Spark scheduling with advanced functions such as queue
scheduling, fair-share scheduling, and resource reservation. For more information on the
benefits of Volcano, see [Why Spark chooses Volcano as built-in batch scheduler on Kubernetes](https://www.cncf.io/blog/2022/06/30/why-spark-chooses-volcano-as-built-in-batch-scheduler-on-kubernetes/ "https://www.cncf.io/blog/2022/06/30/why-spark-chooses-volcano-as-built-in-batch-scheduler-on-kubernetes/") on The
Linux Foundation’s _CNCF blog_.

## Install and set up Volcano

1. Choose one of the following kubectl commands to install Volcano, depending on
   your architectural needs:

```
# x86_64
kubectl apply -f https://raw.githubusercontent.com/volcano-sh/volcano/v1.5.1/installer/volcano-development.yaml
# arm64:
kubectl apply -f https://raw.githubusercontent.com/volcano-sh/volcano/v1.5.1/installer/volcano-development-arm64.yaml
```

2. Prepare a sample Volcano queue. A queue is a collection of [PodGroups](https://volcano.sh/en/docs/podgroup/ "https://volcano.sh/en/docs/podgroup/"). The queue
   adopts FIFO and is the basis for resource division.

```
cat << EOF > volcanoQ.yaml
apiVersion: scheduling.volcano.sh/v1beta1
kind: Queue
metadata:
  name: sparkqueue
spec:
  weight: 4
  reclaimable: false
  capability:
    cpu: 10
    memory: 20Gi
EOF

kubectl apply -f volcanoQ.yaml
```

3. Upload a sample PodGroup manifest to Amazon S3. PodGroup is a group of pods with
   strong association. You typically use a PodGroup for batch scheduling. Submit
   the following sample PodGroup to the queue that you defined in the previous
   step.

```
cat << EOF > podGroup.yaml
apiVersion: scheduling.volcano.sh/v1beta1
kind: PodGroup
spec:
  # Set minMember to 1 to make a driver pod
  minMember: 1
  # Specify minResources to support resource reservation.
  # Consider the driver pod resource and executors pod resource.
  # The available resources should meet the minimum requirements of the Spark job
  # to avoid a situation where drivers are scheduled, but they can't schedule
  # sufficient executors to progress.
  minResources:
    cpu: "1"
    memory: "1Gi"
  # Specify the queue. This defines the resource queue that the job should be submitted to.
  queue: sparkqueue
EOF

aws s3 mv podGroup.yaml s3://`bucket-name`
```

## Run a Spark application with Volcano

scheduler with the Spark operator

1. If you haven't already, complete the steps in the following sections to get set up:
   1. [Install and set up Volcano](#tutorial-volcano-install "#tutorial-volcano-install")
   2. [Setting up the Spark operator for Amazon EMR on EKS](spark-operator-setup.md "spark-operator-setup.md")
   3. [Install the Spark operator](spark-operator-gs.md#spark-operator-install "spark-operator-gs.md#spark-operator-install")

   Include the following arguments when you run the `helm install
 spark-operator-demo` command:

   ```
   --set batchScheduler.enable=true
   --set webhook.enable=true
   ```

2. Create a `SparkApplication` definition file
   `spark-pi.yaml` with `batchScheduler` configured.

```
apiVersion: "sparkoperator.k8s.io/v1beta2"
kind: SparkApplication
metadata:
  name: spark-pi
  namespace: spark-operator
spec:
  type: Scala
  mode: cluster
  image: "895885662937.dkr.ecr.`us-west-2`.amazonaws.com/spark/`emr-6.10.0:latest`"
  imagePullPolicy: Always
  mainClass: org.apache.spark.examples.SparkPi
  mainApplicationFile: "local:///usr/lib/spark/examples/jars/spark-examples.jar"
  sparkVersion: "3.3.1"
  batchScheduler: "volcano"   #Note: You must specify the batch scheduler name as 'volcano'
  restartPolicy:
    type: Never
  volumes:
    - name: "`test-volume`"
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
      - name: "`test-volume`"
        mountPath: "/tmp"
  executor:
    cores: 1
    instances: 1
    memory: "512m"
    labels:
      version: 3.3.1
    volumeMounts:
      - name: "`test-volume`"
        mountPath: "/tmp"
```

3. Submit the Spark application with the following command. This also creates a
   `SparkApplication` object called `spark-pi`:

```
kubectl apply -f spark-pi.yaml
```

4. Check events for the `SparkApplication` object with the following
   command:

```
kubectl describe pods spark-pi-driver --namespace spark-operator
```

The first pod event will show that Volcano has scheduled the pods:

```
Type    Reason     Age   From                Message
----    ------     ----  ----                -------
Normal  Scheduled  23s   volcano             Successfully assigned default/spark-pi-driver to integration-worker2
```

## Run a Spark application with Volcano

scheduler with `spark-submit`

1. First, complete the steps in the [Setting up spark-submit for Amazon EMR on EKS](spark-submit-setup.md "spark-submit-setup.md") section. You must build your `spark-submit` distribution with Volcano support. For more information, see the **Build section** of [Using Volcano as Customized Scheduler for Spark on Kubernetes](https://spark.apache.org/docs/latest/running-on-kubernetes.html#build "https://spark.apache.org/docs/latest/running-on-kubernetes.html#build") in the _Apache Spark documentation_.
2. Set the values for the following environment variables:

```
export SPARK_HOME=spark-home
export MASTER_URL=k8s://`Amazon-EKS-cluster-endpoint`
```

3. Submit the Spark application with the following command:

```
$SPARK_HOME/bin/spark-submit \
 --class org.apache.spark.examples.SparkPi \
 --master $MASTER_URL \
 --conf spark.kubernetes.container.image=895885662937.dkr.ecr.`us-west-2`.amazonaws.com/spark/`emr-6.10.0:latest` \
 --conf spark.kubernetes.authenticate.driver.serviceAccountName=spark \
 --deploy-mode cluster \
 --conf spark.kubernetes.namespace=spark-operator \
 --conf spark.kubernetes.scheduler.name=volcano \
 --conf spark.kubernetes.scheduler.volcano.podGroupTemplateFile=/path/to/podgroup-template.yaml \
 --conf spark.kubernetes.driver.pod.featureSteps=org.apache.spark.deploy.k8s.features.VolcanoFeatureStep \
 --conf spark.kubernetes.executor.pod.featureSteps=org.apache.spark.deploy.k8s.features.VolcanoFeatureStep \
 local:///usr/lib/spark/examples/jars/spark-examples.jar 20
```

4. Check events for the `SparkApplication` object with the following
   command:

```
kubectl describe pod spark-pi --namespace spark-operator
```

The first pod event will show that Volcano has scheduled the pods:

```
Type    Reason     Age   From                Message
----    ------     ----  ----                -------
Normal  Scheduled  23s   volcano             Successfully assigned default/spark-pi-driver to integration-worker2
```
