# Autoscaler parameter autotuning

This section describes auto-tuning behavior for various Amazon EMR versions. It also goes into detail regarding different auto-scaling configurations.

###### Note

Amazon EMR 7.2.0 and higher uses the open source configuration `job.autoscaler.restart.time-tracking.enabled`
to enable **rescale time estimation**. Rescale time estimation has the same
functionality as Amazon EMR autotuning, so you don't have to manually assign empirical values to the restart time.

You can still use Amazon EMR autotuning if you're using Amazon EMR 7.1.0 or lower.

7.2.0 and higher
Amazon EMR 7.2.0 and higher measures the actual required restart time to apply autoscaling
decisions. In releases 7.1.0 and lower, you had to use the configuration `job.autoscaler.restart.time` to
manually configure estimated maximum restart time. By using the configuration
`job.autoscaler.restart.time-tracking.enabled`, you only need to enter
a restart time for the first scaling. Afterwards, the operator records the
actual restart time and will use it for subsequent scalings.

To enable this tracking, use the following command:

```
job.autoscaler.restart.time-tracking.enabled: true
```

The following are the related configurations for rescale time estimation.

| Configuration                                | Required | Default | Description                                                                                                                                                                                                      |
| -------------------------------------------- | -------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| job.autoscaler.restart.time-tracking.enabled | No       | False   | Indicates whether the Flink Autoscaler should automatically tune configurations over time to optimize scaling descisions.<br>Note that the Autoscaler can only autotune the Autoscaler parameter `restart.time`. |
| job.autoscaler.restart.time                  | No       | 5m      | The expected restart time that Amazon EMR on EKS uses until the operator can determine the actual<br>restart time from previous scalings.                                                                        |
| job.autoscaler.restart.time-tracking.limit   | No       | 15m     | The maximum observed restart time when `job.autoscaler.restart.time-tracking.enabled` is set to `true`.                                                                                                          |

The following is an example deployment spec you can use to try out rescale time estimation:

```
apiVersion: flink.apache.org/v1beta1
kind: FlinkDeployment
metadata:
  name: autoscaling-example
spec:
  flinkVersion: v1_18
  flinkConfiguration:

    # Autoscaler parameters
    job.autoscaler.enabled: "true"
    job.autoscaler.scaling.enabled: "true"
    job.autoscaler.stabilization.interval: "5s"
    job.autoscaler.metrics.window: "1m"

    job.autoscaler.restart.time-tracking.enabled: "true"
    job.autoscaler.restart.time: "2m"
    job.autoscaler.restart.time-tracking.limit: "10m"

    jobmanager.scheduler: adaptive
    taskmanager.numberOfTaskSlots: "1"
    pipeline.max-parallelism: "12"

  executionRoleArn: `<JOB ARN>`
  emrReleaseLabel: emr-7.10.0-flink-latest
  jobManager:
    highAvailabilityEnabled: false
    storageDir: s3://`<s3_bucket>`/flink/autoscaling/ha/
    replicas: 1
    resource:
      memory: "1024m"
      cpu: 0.5
  taskManager:
    resource:
      memory: "1024m"
      cpu: 0.5
  job:
    jarURI: s3://`<s3_bucket>`/some-job-with-back-pressure
    parallelism: 1
    upgradeMode: stateless
```

To simulate backpressure, use the following deployment spec.

```
job:
    jarURI: s3://`<s3_bucket>`/pyflink-script.py
    entryClass: "org.apache.flink.client.python.PythonDriver"
    args: ["-py", "/opt/flink/usrlib/pyflink-script.py"]
    parallelism: 1
    upgradeMode: stateless
```

Upload the following Python script to your S3 bucket.

```
import logging
import sys
import time
import random

from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import StreamTableEnvironment

TABLE_NAME="orders"
QUERY=f"""
CREATE TABLE {TABLE_NAME} (
  id INT,
  order_time AS CURRENT_TIMESTAMP,
  WATERMARK FOR order_time AS order_time - INTERVAL '5' SECONDS
)
WITH (
  'connector' = 'datagen',
  'rows-per-second'='10',
  'fields.id.kind'='random',
  'fields.id.min'='1',
  'fields.id.max'='100'
);
"""

def create_backpressure(i):
    time.sleep(2)
    return i

def autoscaling_demo():
    env = StreamExecutionEnvironment.get_execution_environment()
    t_env = StreamTableEnvironment.create(env)
    t_env.execute_sql(QUERY)
    res_table = t_env.from_path(TABLE_NAME)

    stream =  t_env.to_data_stream(res_table) \
      .shuffle().map(lambda x: create_backpressure(x))\
      .print()
    env.execute("Autoscaling demo")

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.INFO, format="%(message)s")
    autoscaling_demo()
```

To verify that rescale time estimation is working, make sure that `DEBUG` level logging
of the Flink operator is enabled. The example below demonstrates how to update the helm chart
file `values.yaml`. Then reinstall the updated helm chart and run your Flink job again.

```
log4j-operator.properties: |+
  # Flink Operator Logging Overrides
  rootLogger.level = DEBUG
```

Getthe name of your leader pod.

```
ip=$(kubectl get configmap -n $NAMESPACE `<job-name>`-cluster-config-map -o json | jq -r ".data[\"org.apache.flink.k8s.leader.restserver\"]" | awk -F: '{print $2}' | awk -F '/' '{print $3}')

kubectl get pods -n $NAMESPACE -o json | jq -r ".items[] | select(.status.podIP == \"$ip\") | .metadata.name"
```

Run the following command to get the actual restart time used in metrics evaluations.

```
kubectl logs `<FLINK-OPERATOR-POD-NAME>` -c flink-kubernetes-operator -n `<OPERATOR-NAMESPACE>` -f | grep "Restart time used in scaling summary computation"
```

You should see logs similar to the following. Note that only the first scaling uses `job.autoscaler.restart.time`. Subsequent
scalings use the observed restart time.

```
2024-05-16 17:17:32,590 o.a.f.a.ScalingExecutor        [DEBUG][default/autoscaler-example] Restart time used in scaling summary computation: PT2M
2024-05-16 17:19:03,787 o.a.f.a.ScalingExecutor        [DEBUG][default/autoscaler-example] Restart time used in scaling summary computation: PT14S
2024-05-16 17:19:18,976 o.a.f.a.ScalingExecutor        [DEBUG][default/autoscaler-example] Restart time used in scaling summary computation: PT14S
2024-05-16 17:20:50,283 o.a.f.a.ScalingExecutor        [DEBUG][default/autoscaler-example] Restart time used in scaling summary computation: PT14S
2024-05-16 17:22:21,691 o.a.f.a.ScalingExecutor        [DEBUG][default/autoscaler-example] Restart time used in scaling summary computation: PT14S
```

7.0.0 and 7.1.0
The open source built-in Flink Autoscaler uses numerous metrics to make the best scaling decisions. However, the default values it uses for its calculations are
meant to be applicable to most workloads and might not optimal for a given job. The autotuning feature
added into the Amazon EMR on EKS version of the Flink Operator looks at historical trends observed over specific
captured metrics and then accordingly tries to calculate the most optimal value tailored for the given job.

| Configuration                                                         | Required | Default | Description                                                                                                                                                                                                                   |
| --------------------------------------------------------------------- | -------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| kubernetes.operator.job.autoscaler.autotune.enable                    | No       | False   | Indicates whether the Flink Autoscaler should automatically tune configurations over time to optimize autoscalers scaling descisions.<br>Currently, the Autoscaler can only autotune the Autoscaler parameter `restart.time`. |
| kubernetes.operator.job.autoscaler.autotune.metrics.history.max.count | No       | 3       | Indicates how many historical Amazon EMR on EKS metrics the Autoscaler keeps in the Amazon EMR on EKS metrics config map.                                                                                                     |
| kubernetes.operator.job.autoscaler.autotune.metrics.restart.count     | No       | 3       | Indicates how many number of restarts the Autoscaler performs before it starts calculating the average restart time for a given job.                                                                                          |

To enable autotuning, you must have completed the following:

- Set `kubernetes.operator.job.autoscaler.autotune.enable:` to `true`
- Set `metrics.job.status.enable:` to `TOTAL_TIME`
- Followed the setup of [Using Autoscaler for Flink applications](jobruns-flink-autoscaler.md "jobruns-flink-autoscaler.md") to enable Autoscaling.

The following is an example deployment spec you can use to try out autotuning.

```
apiVersion: flink.apache.org/v1beta1
kind: FlinkDeployment
metadata:
  name: autoscaling-example
spec:
  flinkVersion: v1_18
  flinkConfiguration:

    # Autotuning parameters
    kubernetes.operator.job.autoscaler.autotune.enable: "true"
    kubernetes.operator.job.autoscaler.autotune.metrics.history.max.count: "2"
    kubernetes.operator.job.autoscaler.autotune.metrics.restart.count: "1"
    metrics.job.status.enable: TOTAL_TIME

    # Autoscaler parameters
    kubernetes.operator.job.autoscaler.enabled: "true"
    kubernetes.operator.job.autoscaler.scaling.enabled: "true"
    kubernetes.operator.job.autoscaler.stabilization.interval: "5s"
    kubernetes.operator.job.autoscaler.metrics.window: "1m"

    jobmanager.scheduler: adaptive

    taskmanager.numberOfTaskSlots: "1"
    state.savepoints.dir: s3://<S3_bucket>/autoscaling/savepoint/
    state.checkpoints.dir: s3://<S3_bucket>/flink/autoscaling/checkpoint/
    pipeline.max-parallelism: "4"

  executionRoleArn: <JOB ARN>
  emrReleaseLabel: emr-6.14.0-flink-latest
  jobManager:
    highAvailabilityEnabled: true
    storageDir: s3://<S3_bucket>/flink/autoscaling/ha/
    replicas: 1
    resource:
      memory: "1024m"
      cpu: 0.5
  taskManager:
    resource:
      memory: "1024m"
      cpu: 0.5
  job:
    jarURI: s3://<S3_bucket>/some-job-with-back-pressure
    parallelism: 1
    upgradeMode: last-state
```

To simulate backpressure, use the following deployment spec.

```
  job:
    jarURI: s3://<S3_bucket>/pyflink-script.py
    entryClass: "org.apache.flink.client.python.PythonDriver"
    args: ["-py", "/opt/flink/usrlib/pyflink-script.py"]
    parallelism: 1
    upgradeMode: last-state
```

Upload the following Python script to your S3 bucket.

```
import logging
import sys
import time
import random

from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import StreamTableEnvironment

TABLE_NAME="orders"
QUERY=f"""
CREATE TABLE {TABLE_NAME} (
  id INT,
  order_time AS CURRENT_TIMESTAMP,
  WATERMARK FOR order_time AS order_time - INTERVAL '5' SECONDS
)
WITH (
  'connector' = 'datagen',
  'rows-per-second'='10',
  'fields.id.kind'='random',
  'fields.id.min'='1',
  'fields.id.max'='100'
);
"""

def create_backpressure(i):
    time.sleep(2)
    return i

def autoscaling_demo():
    env = StreamExecutionEnvironment.get_execution_environment()
    t_env = StreamTableEnvironment.create(env)
    t_env.execute_sql(QUERY)
    res_table = t_env.from_path(TABLE_NAME)

    stream =  t_env.to_data_stream(res_table) \
      .shuffle().map(lambda x: create_backpressure(x))\
      .print()
    env.execute("Autoscaling demo")

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.INFO, format="%(message)s")
    autoscaling_demo()
```

To verify that your autotuner is working, use the following commands. Note that you must use your own leader pod information for the Flink Operator.

First get the name of your leader pod.

```
ip=$(kubectl get configmap -n $NAMESPACE <job-name>-cluster-config-map -o json | jq -r ".data[\"org.apache.flink.k8s.leader.restserver\"]" | awk -F: '{print $2}' | awk -F '/' '{print $3}')

kubectl get pods -n $NAMESPACE -o json | jq -r ".items[] | select(.status.podIP == \"$ip\") | .metadata.name"
```

Once you have the name of your leader pod, you can run the following command.

```
kubectl logs -n $NAMESPACE  -c flink-kubernetes-operator --follow <`YOUR-FLINK-OPERATOR-POD-NAME`>  | grep -E 'EmrEks|autotun|calculating|restart|autoscaler'
```

You should see logs similar to the following.

```
[m[33m2023-09-13 20:10:35,941[m [36mc.a.c.f.k.o.a.EmrEksMetricsAutotuner[m [36m[DEBUG][flink/autoscaling-example] Using the latest Emr Eks Metric for calculating restart.time for autotuning: EmrEksMetrics(restartMetric=RestartMetric(restartingTime=65, numRestarts=1))

[m[33m2023-09-13 20:10:35,941[m [36mc.a.c.f.k.o.a.EmrEksMetricsAutotuner[m [32m[INFO ][flink/autoscaling-example] Calculated average restart.time metric via autotuning to be: PT0.065S

```
