# Using YuniKorn as a custom scheduler for Apache Spark on

Amazon EMR on EKS

With Amazon EMR on EKS, you can use Spark operator or spark-submit to run Spark jobs with
Kubernetes custom schedulers. This tutorial covers how to run Spark jobs with a YuniKorn
scheduler on a custom queue and gang scheduling.

## Overview

[Apache YuniKorn](https://yunikorn.apache.org/ "https://yunikorn.apache.org/") can help manage
Spark scheduling with app-aware scheduling so that you can have fine-grained control on
resource quotas and priorities. With gang scheduling, YuniKorn schedules an app only
when the minimal resource request for the app can be satisfied. For more information,
see [What is
gang scheduling](https://yunikorn.apache.org/docs/user_guide/gang_scheduling/ "https://yunikorn.apache.org/docs/user_guide/gang_scheduling/") on the Apache YuniKorn documentation site.

## Create your cluster and get set up for

YuniKorn

Use the following steps to deploy an Amazon EKS cluster. You can change the AWS Region
(`region`) and Availability Zones (`availabilityZones`).

1. Define the Amazon EKS cluster:

```
cat <<EOF >eks-cluster.yaml
---
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig

metadata:
  name: emr-eks-cluster
  region: `eu-west-1`

vpc:
  clusterEndpoints:
    publicAccess: true
    privateAccess: true

iam:
  withOIDC: true

nodeGroups:
  - name: spark-jobs
    labels: { app: spark }
    instanceType: m5.xlarge
    desiredCapacity: 2
    minSize: 2
    maxSize: 3
    availabilityZones: [`"eu-west-1a"`]
EOF
```

2. Create the cluster:

```
eksctl create cluster -f eks-cluster.yaml
```

3. Create the namespace `spark-job` where you will execute the Spark
   job:

```
kubectl create namespace spark-job
```

4. Next, create a Kubernetes role and role binding. This is required for the
   service account that the Spark job run uses.
   1. Define the service account, role, and role binding for Spark
      jobs.

   ```
   cat <<EOF >emr-job-execution-rbac.yaml
   ---
   apiVersion: v1
   kind: ServiceAccount
   metadata:
     name: spark-sa
     namespace: spark-job
   automountServiceAccountToken: false
   ---
   apiVersion: rbac.authorization.k8s.io/v1
   kind: Role
   metadata:
     name: spark-role
     namespace: spark-job
   rules:
     - apiGroups: ["", "batch","extensions"]
       resources: ["configmaps","serviceaccounts","events","pods","pods/exec","pods/log","pods/portforward","secrets","services","persistentvolumeclaims"]
       verbs: ["create","delete","get","list","patch","update","watch"]
   ---
   apiVersion: rbac.authorization.k8s.io/v1
   kind: RoleBinding
   metadata:
     name: spark-sa-rb
     namespace: spark-job
   roleRef:
     apiGroup: rbac.authorization.k8s.io
     kind: Role
     name: spark-role
   subjects:
     - kind: ServiceAccount
       name: spark-sa
       namespace: spark-job
   EOF
   ```

   2. Apply the Kubernetes role and role binding definition with the
      following command:

   ```
   kubectl apply -f emr-job-execution-rbac.yaml
   ```

## Install and set up YuniKorn

1. Use the following kubectl command to create a namespace
   `yunikorn`to deploy the Yunikorn scheduler:

```
kubectl create namespace yunikorn
```

2. To install the scheduler, execute the following Helm commands:

```
helm repo add yunikorn https://apache.github.io/yunikorn-release
```

```
helm repo update
```

```
helm install yunikorn yunikorn/yunikorn --namespace yunikorn
```

## Run a Spark application with YuniKorn

scheduler with the Spark operator

1. If you haven't already, complete the steps in the following sections to get
   set up:
   1. [Create your cluster and get set up for
      YuniKorn](#tutorial-yunikorn-setup "#tutorial-yunikorn-setup")
   2. [Install and set up YuniKorn](#tutorial-yunikorn-install "#tutorial-yunikorn-install")
   3. [Setting up the Spark operator for Amazon EMR on EKS](spark-operator-setup.md "spark-operator-setup.md")
   4. [Install the Spark operator](spark-operator-gs.md#spark-operator-install "spark-operator-gs.md#spark-operator-install")

   Include the following arguments when you run the `helm install
 spark-operator-demo` command:

   ```
   --set batchScheduler.enable=true
   --set webhook.enable=true
   ```

2. Create a `SparkApplication` definition file
   `spark-pi.yaml`.

To use YuniKorn as a scheduler for your jobs, you must add certain annotations
and labels to your application definition. The annotations and labels specify
the queue for your job and the scheduling strategy that you want to use.

In the following example, the annotation
`schedulingPolicyParameters` sets up gang scheduling for the
application. Then, the example creates **task
groups**, or "gangs" of tasks, to specify the minimum capacity that
must be available before scheduling the pods to start the job execution. And
finally, it specifies in the task group definition to use node groups with the
`"app": "spark"` label, as defined in the [Create your cluster and get set up for
YuniKorn](#tutorial-yunikorn-setup "#tutorial-yunikorn-setup")
section.

```
apiVersion: "sparkoperator.k8s.io/v1beta2"
kind: SparkApplication
metadata:
  name: spark-pi
  namespace: spark-job
spec:
  type: Scala
  mode: cluster
  image: "895885662937.dkr.ecr.`us-west-2`.amazonaws.com/spark/`emr-6.10.0:latest`"
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
    annotations:
      yunikorn.apache.org/schedulingPolicyParameters: "placeholderTimeoutSeconds=30 gangSchedulingStyle=Hard"
      yunikorn.apache.org/task-group-name: "spark-driver"
      yunikorn.apache.org/task-groups: |-
        [{
            "name": "spark-driver",
            "minMember": 1,
            "minResource": {
              "cpu": "1200m",
              "memory": "1Gi"
            },
            "nodeSelector": {
              "app": "spark"
            }
          },
          {
            "name": "spark-executor",
            "minMember": 1,
            "minResource": {
              "cpu": "1200m",
              "memory": "1Gi"
            },
            "nodeSelector": {
              "app": "spark"
            }
        }]
    serviceAccount: spark-sa
    volumeMounts:
      - name: "`test-volume`"
        mountPath: "/tmp"
  executor:
    cores: 1
    instances: 1
    memory: "512m"
    labels:
      version: 3.3.1
    annotations:
      yunikorn.apache.org/task-group-name: "spark-executor"
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
kubectl describe sparkapplication spark-pi --namespace spark-job
```

The first pod event will show that YuniKorn has scheduled the pods:

```
Type    Reason            Age   From                          Message
----    ------            ----  ----                          -------
Normal Scheduling        3m12s yunikorn   spark-operator/org-apache-spark-examples-sparkpi-2a777a88b98b8a95-driver is queued and waiting for allocation
Normal GangScheduling    3m12s yunikorn   Pod belongs to the taskGroup spark-driver, it will be scheduled as a gang member
Normal Scheduled         3m10s yunikorn   Successfully assigned spark
Normal PodBindSuccessful 3m10s yunikorn   Pod spark-operator/
Normal TaskCompleted     2m3s  yunikorn   Task spark-operator/
Normal Pulling           3m10s kubelet    Pulling
```

## Run a Spark application with YuniKorn

scheduler with `spark-submit`

1. First, complete the steps in the [Setting up spark-submit for Amazon EMR on EKS](spark-submit-setup.md "spark-submit-setup.md") section.
2. Set the values for the following environment variables:

```
export SPARK_HOME=spark-home
export MASTER_URL=k8s://`Amazon-EKS-cluster-endpoint`
```

3. Submit the Spark application with the following command:

In the following example, the annotation
`schedulingPolicyParameters` sets up gang scheduling for the
application. Then, the example creates **task
groups**, or "gangs" of tasks, to specify the minimum capacity that
must be available before scheduling the pods to start the job execution. And
finally, it specifies in the task group definition to use node groups with the
`"app": "spark"` label, as defined in the [Create your cluster and get set up for
YuniKorn](#tutorial-yunikorn-setup "#tutorial-yunikorn-setup")
section.

```
$SPARK_HOME/bin/spark-submit \
 --class org.apache.spark.examples.SparkPi \
 --master $MASTER_URL \
 --conf spark.kubernetes.container.image=895885662937.dkr.ecr.`us-west-2`.amazonaws.com/spark/`emr-6.10.0:latest` \
 --conf spark.kubernetes.authenticate.driver.serviceAccountName=spark-sa \
 --deploy-mode cluster \
 --conf spark.kubernetes.namespace=spark-job \
 --conf spark.kubernetes.scheduler.name=yunikorn \
 --conf spark.kubernetes.driver.annotation.yunikorn.apache.org/schedulingPolicyParameters="placeholderTimeoutSeconds=30 gangSchedulingStyle=Hard" \
 --conf spark.kubernetes.driver.annotation.yunikorn.apache.org/task-group-name="spark-driver" \
 --conf spark.kubernetes.executor.annotation.yunikorn.apache.org/task-group-name="spark-executor" \
 --conf spark.kubernetes.driver.annotation.yunikorn.apache.org/task-groups='[{
            "name": "spark-driver",
            "minMember": 1,
            "minResource": {
              "cpu": "1200m",
              "memory": "1Gi"
            },
            "nodeSelector": {
              "app": "spark"
            }
          },
          {
            "name": "spark-executor",
            "minMember": 1,
            "minResource": {
              "cpu": "1200m",
              "memory": "1Gi"
            },
            "nodeSelector": {
              "app": "spark"
            }
        }]' \
 local:///usr/lib/spark/examples/jars/spark-examples.jar 20
```

4. Check events for the `SparkApplication` object with the following
   command:

```
kubectl describe pod `spark-driver-pod` --namespace spark-job
```

The first pod event will show that YuniKorn has scheduled the pods:

```
Type    Reason           Age   From                          Message
----    ------           ----  ----                          -------
Normal Scheduling        3m12s yunikorn   spark-operator/org-apache-spark-examples-sparkpi-2a777a88b98b8a95-driver is queued and waiting for allocation
Normal GangScheduling    3m12s yunikorn   Pod belongs to the taskGroup spark-driver, it will be scheduled as a gang member
Normal Scheduled         3m10s yunikorn   Successfully assigned spark
Normal PodBindSuccessful 3m10s yunikorn   Pod spark-operator/
Normal TaskCompleted     2m3s  yunikorn   Task spark-operator/
Normal Pulling           3m10s kubelet    Pulling
```
