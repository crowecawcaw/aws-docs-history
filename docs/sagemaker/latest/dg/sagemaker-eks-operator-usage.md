# Using the training operator to run jobs

To use kubectl to run the job, you must create a job.yaml to specify the job specifications and run
`kubectl apply -f job.yaml` to submit the job. In this YAML file, you can specify custom
configurations in the `logMonitoringConfiguration` argument to define automated monitoring
rules that analyze log outputs from the distributed training job to detect problems and recover.

```
apiVersion: sagemaker.amazonaws.com/v1
kind: HyperPodPyTorchJob
metadata:
  labels:
    app.kubernetes.io/name: HyperPod
    app.kubernetes.io/managed-by: kustomize
  name: &jobname xxx
  annotations:
    XXX: XXX
    ......
spec:
  nprocPerNode: "X"
  replicaSpecs:
    - name: 'XXX'
      replicas: 16
      template:
        spec:
          nodeSelector:
            beta.kubernetes.io/instance-type: ml.p5.48xlarge
          containers:
            - name: XXX
              image: XXX
              imagePullPolicy: Always
              ports:
                - containerPort: 8080 # This is the port that HyperPodElasticAgent listens to
              resources:
                limits:
                  nvidia.com/gpu: 8
                  hugepages-2Mi: 5120Mi
                requests:
                  nvidia.com/gpu: 8
                  hugepages-2Mi: 5120Mi
                  memory: 32000Mi
          ......
  runPolicy:
    jobMaxRetryCount: 50
    restartPolicy:
      numRestartBeforeFullJobRestart: 3
      evalPeriodSeconds: 21600
      maxFullJobRestarts: 1
    cleanPodPolicy: "All"
    logMonitoringConfiguration:
      - name: "JobStart"
        logPattern: ".*Experiment configuration.*" # This is the start of the training script
        expectedStartCutOffInSeconds: 120 # Expected match in the first 2 minutes
      - name: "JobHangingDetection"
        logPattern: ".*\\[Epoch 0 Batch \\d+.*'training_loss_step': (\\d+(\\.\\d+)?).*"
        expectedRecurringFrequencyInSeconds: 300 # If next batch is not printed within 5 minute, consider it hangs. Or if loss is not decimal (e.g. nan) for 2 minutes, mark it hang as well.
        expectedStartCutOffInSeconds: 600 # Allow 10 minutes of job startup time
      - name: "NoS3CheckpointingDetection"
        logPattern: ".*The checkpoint is finalized. All shards is written.*"
        expectedRecurringFrequencyInSeconds: 600 # If next checkpoint s3 upload doesn't happen within 10 mins, mark it hang.
        expectedStartCutOffInSeconds: 1800 # Allow 30 minutes for first checkpoint upload
      - name: "LowThroughputDetection"
        logPattern: ".*\\[Epoch 0 Batch \\d+.*'samples\\/sec': (\\d+(\\.\\d+)?).*"
        metricThreshold: 80 # 80 samples/sec
        operator: "lteq"
        metricEvaluationDataPoints: 25 # if throughput lower than threshold for 25 datapoints, kill the job

```

If you want to use the log monitoring options, make sure that you’re emitting the training log to `sys.stdout`.
HyperPod elastic agent monitors training logs in sys.stdout, which is saved at `/tmp/hyperpod/`. You can use the following command
to emit training logs.

```
logging.basicConfig(format="%(asctime)s [%(levelname)s] %(name)s: %(message)s", level=logging.INFO, stream=sys.stdout)
```

The following table describes all of the possible log monitoring configurations:

| Parameter                                     | Usage                                                                                                                                                                                                                                                                                                        |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| jobMaxRetryCount                              | Maximum number of restarts at the process level.                                                                                                                                                                                                                                                             |
| restartPolicy: numRestartBeforeFullJobRestart | Maximum number of restarts at the process level before the operator restarts at the job level.                                                                                                                                                                                                               |
| restartPolicy: evalPeriodSeconds              | The period of evaluating the restart limit in seconds                                                                                                                                                                                                                                                        |
| restartPolicy: maxFullJobRestarts             | Maximum number of full job restarts before the job fails.                                                                                                                                                                                                                                                    |
| cleanPodPolicy                                | Specifies the pods that the operator should clean. Accepted values are<br>`All`, `OnlyComplete`, and `None`.                                                                                                                                                                                                 |
| logMonitoringConfiguration                    | The log monitoring rules for slow and hanging job detection                                                                                                                                                                                                                                                  |
| expectedRecurringFrequencyInSeconds           | Time interval between two consecutive LogPattern matches after which the rule evaluates to HANGING. If not specified, no time constraint exists between consecutive LogPattern matches.                                                                                                                      |
| expectedStartCutOffInSeconds                  | Time to first LogPattern match after which the rule evaluates to HANGING. If not specified, no time constraint exists for the first LogPattern match.                                                                                                                                                        |
| logPattern                                    | Regular expression that identifies log lines that the rule applies to when the rule is active                                                                                                                                                                                                                |
| metricEvaluationDataPoints                    | Number of consecutive times a rule must evaluate to SLOW before marking a job as SLOW. If not specified, the default is 1.                                                                                                                                                                                   |
| metricThreshold                               | Threshold for value extracted by LogPattern with a capturing group. If not specified, metric evaluation is not performed.                                                                                                                                                                                    |
| operator                                      | The inequality to apply to the monitoring configuration. Accepted values are<br>`gt`, `gteq`, `lt`, `lteq`, and `eq`.                                                                                                                                                                                        |
| stopPattern                                   | Regular expresion to identify the log line at which to deactivate the rule. If not specified, the rule will always be active.                                                                                                                                                                                |
| faultOnMatch                                  | Indicates whether a match of LogPattern should immediately trigger a job fault. When true, the job will be marked as faulted as soon as the LogPattern is matched,<br>regardless of other rule parameters. When false or not specified, the rule will evaluate to SLOW or HANGING based on other parameters. |

For more training resiliency, specify spare node configuration details.
If your job fails, the operator works with Kueue to use nodes reserved in advance to continue running the job.
Spare node configurations require Kueue, so if you try to submit a job with spare nodes but don’t have Kueue installed,
the job will fail. The following example is a sample `job.yaml` file that contains spare node configurations.

```

apiVersion: sagemaker.amazonaws.com/v1
kind: HyperPodPyTorchJob
metadata:
  labels:
    kueue.x-k8s.io/queue-name: user-queue # Specify the queue to run the job.
  name: hyperpodpytorchjob-sample
spec:
  nprocPerNode: "1"
  runPolicy:
    cleanPodPolicy: "None"
  replicaSpecs:
    - name: pods
      replicas: 1
      spares: 1 # Specify how many spare nodes to reserve.
      template:
        spec:
          containers:
            - name: XXX
              image: XXX

              imagePullPolicy: Always
              ports:
                - containerPort: 8080
              resources:
                requests:
                  nvidia.com/gpu: "0"
                limits:
                  nvidia.com/gpu: "0"

```

## Monitoring

The Amazon SageMaker HyperPod is integrated with [observability with Amazon Managed Grafana and Amazon Managed Service for Prometheus](sagemaker-hyperpod-observability-addon.md "sagemaker-hyperpod-observability-addon.md"), so you can
set up monitoring to collect and feed metrics into these observability tools.

Alternatively, you can scrape metrics through Amazon Managed Service for Prometheus without managed observability.
To do so, include the metrics that you want to monitor into your `job.yaml`
file when you run jobs with `kubectl`.

```
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: hyperpod-training-operator
  namespace: aws-hyperpod
spec:
  ......
  endpoints:
    - port: 8081
      path: /metrics
      interval: 15s
```

The following are events that the training operator emits that you can feed into Amazon Managed Service for Prometheus to monitor your training jobs.

| Event                                                   | Description                                             |
| ------------------------------------------------------- | ------------------------------------------------------- |
| hyperpod_training_operator_jobs_created_total           | Total number of jobs that the training operator has run |
| hyperpod_training_operator_jobs_restart_latency         | Current job restart latency                             |
| hyperpod_training_operator_jobs_fault_detection_latency | Fault detection latency                                 |
| hyperpod_training_operator_jobs_deleted_total           | Total number of deleted jobs                            |
| hyperpod_training_operator_jobs_successful_total        | Total number of completed jobs                          |
| hyperpod_training_operator_jobs_failed_total            | Total number of failed jobs                             |
| hyperpod_training_operator_jobs_restarted_total         | Total number of auto-restarted jobs                     |

## Sample docker configuration

The following is a sample docker file that you can run with the `hyperpod run` command.

```
export AGENT_CMD="--backend=nccl"
exec hyperpodrun --server-host=${AGENT_HOST} --server-port=${AGENT_PORT} \
    --tee=3 --log_dir=/tmp/hyperpod \
    --nnodes=${NNODES} --nproc-per-node=${NPROC_PER_NODE} \
    --pre-train-script=/workspace/echo.sh --pre-train-args='Pre-training script' \
    --post-train-script=/workspace/echo.sh --post-train-args='Post-training script' \
    /workspace/mnist.py --epochs=1000 ${AGENT_CMD}
```

## Sample log monitoring configurations

**Job hang detection**

To detect hang jobs, use the following configurations. It uses the following parameters:

- expectedStartCutOffInSeconds – how long the monitor should wait before expecting the first logs
- expectedRecurringFrequencyInSeconds – the time interval to wait for the next batch of logs

With these settings, the log monitor expects to see a log line matching the regex pattern `.*Train Epoch.*`
within 60 seconds after the training job starts. After the
first appearance, the monitor expects to see matching log lines every 10 seconds. If the first logs don't appear within
60 seconds or subsequent logs don't appear every 10 seconds, the HyperPod elastic agent treats the container
as stuck and coordinates with the training operator to restart the job.

```
runPolicy:
    jobMaxRetryCount: 10
    cleanPodPolicy: "None"
    logMonitoringConfiguration:
      - name: "JobStartGracePeriod"
        # Sample log line: [default0]:2025-06-17 05:51:29,300 [INFO] __main__: Train Epoch: 5 [0/60000 (0%)]       loss=0.8470
        logPattern: ".*Train Epoch.*"
        expectedStartCutOffInSeconds: 60
      - name: "JobHangingDetection"
        logPattern: ".*Train Epoch.*"
        expectedRecurringFrequencyInSeconds: 10 # if the next batch is not printed within 10 seconds
```

**Training loss spike**

The following monitoring configuration emits training logs with the pattern `xxx training_loss_step xx`.
It uses the parameter `metricEvaluationDataPoints`, which lets you specify a threshold of data points
before the operator restarts the job. If the training loss value is more than 2.0, the operator restarts the job.

```
runPolicy:
  jobMaxRetryCount: 10
  cleanPodPolicy: "None"
  logMonitoringConfiguration:
    - name: "LossSpikeDetection"
      logPattern: ".*training_loss_step (\\d+(?:\\.\\d+)?).*"   # training_loss_step 5.0
      metricThreshold: 2.0
      operator: "gt"
      metricEvaluationDataPoints: 5 # if loss higher than threshold for 5 data points, restart the job
```

**Low TFLOPs detection**

The following monitoring configuration emits training logs with the pattern `xx TFLOPs xx` every five seconds.
If TFLOPs is less than 100 for 5 data points, the operator restarts the training job.

```
runPolicy:
  jobMaxRetryCount: 10
  cleanPodPolicy: "None"
  logMonitoringConfiguration:
    - name: "TFLOPs"
      logPattern: ".* (.+)TFLOPs.*"    # Training model, speed: X TFLOPs...
      expectedRecurringFrequencyInSeconds: 5
      metricThreshold: 100       # if Tflops is less than 100 for 5 data points, restart the job
      operator: "lt"
      metricEvaluationDataPoints: 5
```

**Training script error log detection**

The following monitoring configuration detects if the pattern specified in `logPattern` is present in the training logs. As soon as the training operator encounters
the error pattern, the training operator treats it as a fault and restarts the job.

```
runPolicy:
  jobMaxRetryCount: 10
  cleanPodPolicy: "None"
  logMonitoringConfiguration:
    - name: "GPU Error"
      logPattern: ".*RuntimeError.*out of memory.*"
      faultOnMatch: true
```
