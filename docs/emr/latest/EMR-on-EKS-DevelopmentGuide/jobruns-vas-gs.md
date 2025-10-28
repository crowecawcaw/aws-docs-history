# Getting started with vertical autoscaling for

Amazon EMR on EKS

Use vertical autoscaling for Amazon EMR on EKS when you want automatic tuning of memory and CPU resources to
adapt to your Amazon EMR Spark application workload. For more information, see [Using vertical autoscaling
with Amazon EMR Spark jobs](jobruns-vas.md "jobruns-vas.md").

## Submitting a Spark job with vertical

autoscaling

When you submit a job through the [StartJobRun](../../../emr-on-eks/latest/APIReference/API_StartJobRun.md "../../../emr-on-eks/latest/APIReference/API_StartJobRun.md") API, add
the following two configurations to the driver for your Spark job to turn on vertical
autoscaling:

```
"spark.kubernetes.driver.annotation.emr-containers.amazonaws.com/dynamic.sizing":"true",
"spark.kubernetes.driver.annotation.emr-containers.amazonaws.com/dynamic.sizing.signature":"`YOUR_JOB_SIGNATURE`"
```

In the code above, the first line enables the vertical autoscaling capability. The
next line is a required signature configuration that lets you choose a signature for your
job.

For more information on these configurations and acceptable parameter values, see
[Configuring vertical autoscaling for
Amazon EMR on EKS](jobruns-vas-configure.md "jobruns-vas-configure.md"). By
default, your job submits in the monitoring-only **Off** mode
of vertical autoscaling. This monitoring state lets you compute and view resource
recommendations without performing autoscaling. For more information, see [Vertical autoscaling modes](jobruns-vas-configure.md#jobruns-vas-parameters-opt-mode "jobruns-vas-configure.md#jobruns-vas-parameters-opt-mode").

The following example shows how to complete a sample `start-job-run`
command with vertical autoscaling:

```
aws emr-containers start-job-run \
--virtual-cluster-id $`VIRTUAL_CLUSTER_ID` \
--name $`JOB_NAME` \
--execution-role-arn $`EMR_ROLE_ARN` \
--release-label `emr-6.10.0-latest` \
--job-driver '{
  "sparkSubmitJobDriver": {
     "entryPoint": "local:///usr/lib/spark/examples/src/main/python/pi.py"
   }
 }' \
--configuration-overrides '{
    "applicationConfiguration": [{
        "classification": "spark-defaults",
        "properties": {
          "spark.kubernetes.driver.annotation.emr-containers.amazonaws.com/dynamic.sizing": "true",
          "spark.kubernetes.driver.annotation.emr-containers.amazonaws.com/dynamic.sizing.signature": "`test-signature`"
        }
    }]
  }'
```

## Verifying the vertical autoscaling

functionality

To verify that vertical autoscaling works correctly for the submitted job, use kubectl
to get the `verticalpodautoscaler` custom resource and view your scaling
recommendations. For example, the following command queries for recommendations on the
example job from the [Submitting a Spark job with vertical
autoscaling](#jobruns-vas-spark-submit "#jobruns-vas-spark-submit") section:

```
kubectl get verticalpodautoscalers --all-namespaces \
-l=emr-containers.amazonaws.com/dynamic.sizing.signature=`test-signature`
```

The output from this query should resemble the following:

```
NAME                                                          MODE   CPU         MEM PROVIDED   AGE
ds-jceyefkxnhrvdzw6djum3naf2abm6o63a6dvjkkedqtkhlrf25eq-vpa   Off    3304504865  True           87m
```

If your output doesn't look similar or contains an error code, see [Troubleshooting Amazon EMR on EKS vertical
autoscaling](troubleshooting-vas.md "troubleshooting-vas.md") for steps to help
resolve the issue.
