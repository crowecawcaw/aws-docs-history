

# Understanding scaling and concurrency for GPU-accelerated Event Functions

AWS Lambda Managed Instances scales GPU-accelerated Event Functions by adding or removing execution environments based on GPU utilization, CPU utilization, and concurrency. Within each execution environment, `PerExecutionEnvironmentMaxConcurrency` controls how many invocations run concurrently. Tuning these settings together helps you optimize GPU utilization and reduce costs for your workloads.

To avoid paying for idle GPU capacity, you can configure your function to scale to zero by setting `MinExecutionEnvironments` to 0 and `MaxExecutionEnvironments` to a value greater than 0. When traffic resumes, scaling from zero can take several minutes while Lambda provisions new GPU instances, and requests might fail if GPU capacity isn't available. For more information, see [Scaling to zero](lambda-managed-instances-scaling.md#lambda-managed-instances-scale-to-zero).

## GPU scaling behavior
<a name="lambda-managed-instances-gpu-scaling-behavior"></a>

GPU-accelerated Event Functions scale on GPU utilization, in addition to the CPU utilization and concurrency metrics that all functions on Lambda Managed Instances use. Lambda monitors these metrics across your execution environments, adding capacity when any metric exceeds its target and removing capacity when all metrics fall below their targets. The default GPU utilization target is 40%, which is designed to leave headroom for traffic to double within five minutes.

### Overriding the GPU utilization target
<a name="lambda-managed-instances-gpu-scaling-override-target"></a>

You can set your own GPU utilization target using a `TargetTrackingScalingPolicy` on the capacity provider configuration. The target value can be between 0 and 100. Choose a low target for relatively bursty workloads that are latency-sensitive. Alternatively, choose a high target to reduce costs, with the potential trade-off being more invocations being throttled if traffic is bursty.

```bash
aws lambda update-capacity-provider \
  --capacity-provider-name my-gpu-capacity-provider \
  --capacity-provider-scaling-config '{
    "ScalingMode": "Manual",
    "ScalingPolicies": [
      {
        "PredefinedMetricType": "LambdaCapacityProviderAverageGPUUtilization",
        "TargetValue": 70
      }
    ]
  }'
```

## Instance type selection
<a name="lambda-managed-instances-gpu-scaling-instance-selection"></a>

When scaling out, Lambda selects an instance type using the following process:

1. Lambda starts with the latest generation in your `AllowedInstanceTypes` list that has the smallest GPU meeting your function's `AcceleratorMemorySize` requirement.

1. If capacity is unavailable for that instance type (`InsufficientCapacityException`), Lambda falls back to the next newest generation in the list.

1. Lambda repeats this process through the instance types in your list until it launches an instance. If no instance type in your list is available, the launch fails with `InsufficientCapacityException`, and Lambda retries as capacity becomes available. For more information, see [Troubleshooting GPU-accelerated functions on Lambda Managed Instances](lambda-managed-instances-gpu-troubleshooting.md).

1. Lambda continues to request additional instances as long as any monitored metric (CPU utilization, GPU utilization, or concurrency) exceeds its scaling target.

If you consistently see `InsufficientCapacityException`, you can purchase On-Demand Capacity Reservations (ODCRs) for the instance types in your capacity provider. For Availability Zone resiliency, you can purchase ODCRs in multiple Availability Zones. See [Reserve compute capacity with Amazon EC2 On-Demand Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-reservations.html). Ensure that the ODCRs you purchase match the instance types and Availability Zones configured in your capacity provider, and create them with open instance eligibility. Lambda then uses the reserved capacity automatically. Lambda Managed Instances does not support targeted ODCRs.

## Concurrency within an execution environment
<a name="lambda-managed-instances-gpu-scaling-concurrency"></a>

On Lambda Managed Instances, each execution environment can process more than one invocation at a time. For GPU-accelerated functions, `PerExecutionEnvironmentMaxConcurrency` has a default and a maximum value. For these values, see the [Limits](lambda-managed-instances-gpu.md#lambda-managed-instances-gpu-limits) section.

Each execution environment can run multiple worker processes, one per concurrent invocation up to `PerExecutionEnvironmentMaxConcurrency`. All invocations in the execution environment share a single physical GPU. How those worker processes use the GPU depends on how you structure your code. You have two options:
+ **Each worker process loads its own model copy (default).** – With this option, each worker process imports your handler and runs your initialization code independently, holding its own CUDA context and its own copy of the model in GPU memory, so GPU memory use grows with concurrency. Use this option when `PerExecutionEnvironmentMaxConcurrency` copies of your model and working set fit within your accelerator memory.
+ **All worker processes share one model copy.** – With this option, a single inference server process holds the model, and every worker process forwards its requests to that server over local HTTP, so one copy serves all concurrent invocations and GPU memory does not grow with concurrency. Use this option when one copy of your model occupies most of the accelerator memory. The Lambda vLLM and SGLang base images work this way: the image starts the server once per execution environment and the server batches concurrent requests. To add custom logic such as request validation, replace the default handler with your own `handler.py` that forwards to the same server. For more information about the vLLM and SGLang base images, see [GPU base images](lambda-managed-instances-gpu-base-images.md#lambda-managed-instances-gpu-base-images-vllm). With another framework, start the server yourself from your initialization code and forward to it from the handler, as described in [Run one model server for all worker processes](#lambda-managed-instances-gpu-scaling-model-server).

**Note**  
Start with the default concurrency and monitor the `ExecutionEnvironmentGPUMemoryUsed` metric. If GPU memory use approaches the accelerator memory you requested, or invocations fail with a GPU out-of-memory error (for example, `CUDA out of memory`), lower `PerExecutionEnvironmentMaxConcurrency`. If GPU memory use stays well below the accelerator memory and `ExecutionEnvironmentGPUUtilization` is low under load, raise it.

## Run one model server for all worker processes
<a name="lambda-managed-instances-gpu-scaling-model-server"></a>

The Lambda vLLM and SGLang base images start one inference server per execution environment for you, so with those images you only write a handler that forwards to it. With another framework or base image, you start the server yourself. Each worker process imports your handler and loads its own copy of the model, so GPU memory grows with concurrency. For a large model, run one server process that owns the GPU and the model, and have every worker process forward requests to it over local HTTP, so one copy serves all concurrent invocations. Because each worker process initializes independently, use a lock file in `/tmp` so that only one worker process starts the server. The others wait until it's ready.

This example uses one `model_server.py` file.

load\_model() and run() are placeholders for your own model loading and inference. If you use this pattern on the vLLM or SGLang image, set `ENGINE_EXTENSION=off` so that the image does not start its own server. For a handler that forwards to the server the vLLM image starts, see [Customize request handling with your own handler](lambda-managed-instances-gpu-inference.md#lambda-managed-instances-gpu-inference-custom-handler).

```python
import torch, uvicorn
from fastapi import FastAPI, Request
app = FastAPI()
model = load_model().to("cuda").eval()          # one process, one copy in VRAM
@app.post("/infer")
async def infer(r: Request):
    with torch.no_grad():
        return {"result": run(model, await r.json())}
uvicorn.run(app, host="127.0.0.1", port=8000)
```

An `app.py` file defines the handler code and starts the model server only once.

```python
import os, sys, time, socket, subprocess, fcntl, json, urllib.request
PORT, LOCK = 8000, "/tmp/model_server.lock"

def _up():
    with socket.socket() as s:
        s.settimeout(0.2); return s.connect_ex(("127.0.0.1", PORT)) == 0

# Runs once per worker at init. The /tmp lock elects a single worker to start the
# server; the others wait for it to be healthy, then share it.
fd = os.open(LOCK, os.O_CREAT | os.O_RDWR)
fcntl.flock(fd, fcntl.LOCK_EX)
try:
    if not _up():
        subprocess.Popen([sys.executable, "model_server.py"])
        end = time.time() + 600
        while not _up():
            if time.time() > end:
                raise RuntimeError("model server did not start")
            time.sleep(1)
finally:
    fcntl.flock(fd, fcntl.LOCK_UN); os.close(fd)

def handler(event, context):
    req = urllib.request.Request(f"http://127.0.0.1:{PORT}/infer",
        data=json.dumps(event).encode(), headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req) as r:
        return json.load(r)
```