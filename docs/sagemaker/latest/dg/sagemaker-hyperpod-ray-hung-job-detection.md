

# Hung job detection
<a name="sagemaker-hyperpod-ray-hung-job-detection"></a>

Distributed Ray Train jobs can stall without producing an error. A single worker fails silently, and every other worker blocks at the next collective operation, waiting indefinitely. GPUs remain allocated with model weights loaded but produce no useful compute. Because there is no error message or crash, the stall often goes unnoticed for hours until someone checks job progress manually.

HyperPod hung job detection continuously monitors GPU utilization patterns and training worker activity across your cluster to identify jobs that have stopped making forward progress. When a stall is detected, the system surfaces it within minutes rather than hours, so you can recover the job or free the capacity for other work.

## How it works
<a name="sagemaker-hyperpod-ray-hung-job-detection-default"></a>

By default, all Ray Train workers on HyperPod are monitored using platform defaults with no code changes required. The platform correlates GPU utilization patterns with training worker output activity to distinguish between a job that is idle because it is stalled and one that is idle because it is performing I/O or checkpointing. When a stall is detected, a notification is delivered to your HyperPod Observability Grafana dashboard and CloudWatch. For more information, see [Viewing detection events](#sagemaker-hyperpod-ray-hung-job-detection-monitoring).

The default action is *notify*: HyperPod logs the detection event but does not terminate the job. To enable automatic recovery, configure custom rules with the `cancel` action as described in the following section.

When you configure custom detection rules, they *replace* the default detection for that job. The action you specify in your custom configuration applies to all detections from your custom rules. Default detection continues to run for any job that does not configure custom rules.

## Configuring custom detection rules
<a name="sagemaker-hyperpod-ray-hung-job-detection-custom-rules"></a>

For more control over detection behavior, you can define log pattern rules with configurable timeouts and actions. Custom rules let you detect domain-specific stalls (for example, no new training-step log line for 10 minutes) or error conditions (for example, OOM) and choose whether HyperPod should notify or automatically cancel the hung worker.

Follow these steps to enable custom detection rules.

1. 

**Add the host IP environment variable to your RayCluster manifest**

   Add the following environment variable to both `headGroupSpec` and `workerGroupSpecs` in your RayCluster YAML. This allows the Python library running inside the training container to communicate with the job monitoring service on the host.

   ```
   spec:
     headGroupSpec:
       template:
         spec:
           containers:
           - name: ray-head
             env:
             - name: HYPERPOD_JMA_HOST
               valueFrom:
                 fieldRef:
                   fieldPath: status.hostIP
     workerGroupSpecs:
     - template:
         spec:
           containers:
           - name: ray-worker
             env:
             - name: HYPERPOD_JMA_HOST
               valueFrom:
                 fieldRef:
                   fieldPath: status.hostIP
   ```
**Note**  
This environment variable is only required for custom detection rules. Default detection works without it.

1. 

**Install the toolkit library in your training container image**

   Add the [toolkit-for-ray-on-sagemaker-ai](https://pypi.org/project/toolkit-for-ray-on-sagemaker-ai/) package from the PyPI website to your training container image. The library is preinstalled in SageMaker Distribution images.

   ```
   pip install toolkit-for-ray-on-sagemaker-ai
   ```

1. 

**Add monitoring to your training function**

   Call `SageMakerLogMonitoring.start()` inside your training function *before* doing any meaningful work. This ensures monitoring is active from the start of training and can detect hangs that occur during model loading or the first forward pass.

   ```
   from toolkit_for_ray_on_sagemaker_ai.log_monitoring import (
       SageMakerLogMonitoring,
       LogMonitorConfig,
   )
   from ray.train import RunConfig, FailureConfig, ScalingConfig
   from ray.train.torch import TorchTrainer
   
   def train_func():
       # Start monitoring BEFORE any meaningful work
       SageMakerLogMonitoring(config=LogMonitorConfig(
           enabled=True,
           rules=[
               {
                   "name": "training_progress",
                   "type": "log_pattern",
                   "enabled": True,
                   "log_pattern": "(Epoch|Step|Iteration) \\d+",
                   "timeout_minutes": 10,
                   "start_timeout_minutes": 30,
                   "stop_pattern": "Training complete",
                   "fault_on_match": False,
               },
               {
                   "name": "oom_detection",
                   "type": "log_pattern",
                   "enabled": True,
                   "log_pattern": "CUDA out of memory|OutOfMemoryError|OOM",
                   "fault_on_match": True,
               },
           ],
           action="cancel",
       )).start()
   
       # ... your training loop
       for epoch in range(num_epochs):
           print(f"Epoch {epoch}")  # This output is what the rule monitors
           train_one_epoch(model, dataloader)
   
       print("Training complete")  # Matches stop_pattern, deactivates the rule
   
   # Configure FailureConfig so Ray Train automatically restarts all workers
   # when the cancel action terminates a hung worker.
   trainer = TorchTrainer(
       train_func,
       scaling_config=ScalingConfig(num_workers=4, use_gpu=True),
       run_config=RunConfig(
           failure_config=FailureConfig(max_failures=3),
       ),
   )
   ```

   When the `cancel` action terminates a hung worker, Ray Train's [FailureConfig](https://docs.ray.io/en/latest/train/user-guides/fault-tolerance.html) in the Ray documentation detects the worker failure and restarts all workers from the last checkpoint. Set `max_failures` to the number of automatic recovery attempts you want before the job fails permanently. Without `FailureConfig`, a single worker termination fails the entire job.

   Because Ray Train restores from the last saved checkpoint on restart, no training progress is lost beyond the work since the most recent checkpoint. If your training code saves checkpoints periodically (for example, at each epoch boundary), the job resumes from the last saved state automatically.

### Rule fields
<a name="sagemaker-hyperpod-ray-hung-job-detection-rule-fields"></a>


| Field | Type | Required | Description | 
| --- | --- | --- | --- | 
| name | string | Yes | Human-readable identifier for the rule. | 
| type | string | Yes | Rule type. Use log\_pattern for log-based detection. | 
| enabled | bool | No | Whether this rule is active. Defaults to false. | 
| log\_pattern | string | Yes | Regex pattern to match in worker stdout (RE2 syntax, max 256 characters). | 
| timeout\_minutes | float | No | Maximum minutes between consecutive pattern matches before declaring a hang. | 
| start\_timeout\_minutes | float | No | Maximum minutes from job start for the first pattern match. Useful for allowing startup time (model loading, data download). If the pattern has not appeared within this window, the job is considered hung. | 
| stop\_pattern | string | No | Regex that deactivates this rule when matched (for example, "Training complete"). | 
| fault\_on\_match | bool | No | If true, declares a hang immediately when the pattern matches. Use for error patterns like OOM. When true, timeout\_minutes is not required. | 
| metric\_evaluation\_data\_points | int | No | Number of consecutive evaluation cycles that must confirm the condition before declaring a hang. Defaults to 1. | 

### Actions
<a name="sagemaker-hyperpod-ray-hung-job-detection-actions"></a>


| Action | Description | 
| --- | --- | 
| notify | Emit a detection event to CloudWatch and Grafana but take no automatic action. This is the default. | 
| cancel | Terminate the hung worker process. Ray Train's built-in FailureConfig restarts all workers from the last checkpoint. To use this action, configure FailureConfig with sufficient retries in your RunConfig. | 

### Opting out of detection
<a name="sagemaker-hyperpod-ray-hung-job-detection-opt-out"></a>

To disable all hung job detection for a specific job, including both default detection and any custom rules:

```
from toolkit_for_ray_on_sagemaker_ai.log_monitoring import (
    SageMakerLogMonitoring,
    LogMonitorConfig,
)

def train_func():
    SageMakerLogMonitoring(config=LogMonitorConfig(enabled=False)).start()
    # ... training continues with no monitoring
```

## Viewing detection events
<a name="sagemaker-hyperpod-ray-hung-job-detection-monitoring"></a>

When a hung job is detected, the event appears in the following locations:
+ **CloudWatch Logs**: Log group `/aws/sagemaker/Clusters/{{cluster-name}}/{{cluster-id}}`, log stream `SageMakerHangJobDetectionEvents/{{instance-group-name}}/{{instance-id}}`. Search for `HANG_DETECTED` to find detection events.
+ **Grafana**: If the HyperPod Observability add-on is installed, detection events appear in the Ray Train dashboard under the Hung job detection panel. For more information, see [Observability](sagemaker-hyperpod-ray-observability.md).

Each detection event includes the job ID, the evidence that triggered the detection, and the action taken (`notify` or `cancel`).