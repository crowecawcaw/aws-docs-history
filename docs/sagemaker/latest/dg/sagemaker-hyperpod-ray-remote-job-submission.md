

# Submitting jobs remotely with the toolkit library
<a name="sagemaker-hyperpod-ray-remote-job-submission"></a>

When the `toolkit-for-ray-on-sagemaker-ai` package is installed, Ray's standard Jobs CLI and Python SDK authenticate through the cluster's secured endpoint using the `sagemaker_ray://` address scheme the package registers. You submit and track jobs from a laptop, a CI/CD pipeline, or any environment with AWS credentials, with no `kubectl port-forward` and no direct network path to the cluster. The package is preinstalled in SageMaker Distribution images.

## Prerequisites
<a name="sagemaker-hyperpod-ray-remote-job-submission-prerequisites"></a>
+ An authenticated endpoint on the cluster. For more information, see [Installing the HyperPod Ray Endpoint Operator](sagemaker-hyperpod-ray-endpoint-operator.md).
+ The toolkit package, if you are not in a SageMaker Distribution image:

  ```
  pip install toolkit-for-ray-on-sagemaker-ai
  ```

## Address the cluster
<a name="sagemaker-hyperpod-ray-remote-job-submission-address"></a>

The package adds a `sagemaker_ray` address scheme. You pass it to any `ray job` command with `--address`:

```
sagemaker_ray://{{my-cluster}}/{{my-namespace}}
```

## Submit and list jobs from the CLI
<a name="sagemaker-hyperpod-ray-remote-job-submission-cli"></a>

List the jobs on a cluster, then submit a working directory with an entry script.

```
ray job list --address sagemaker_ray://{{my-cluster}}/{{my-namespace}}

ray job submit \
    --address sagemaker_ray://{{my-cluster}}/{{my-namespace}} \
    --working-dir ./src \
    -- python {{my-script.py}}
```

The endpoint authenticates the request against your identity, so you reach the cluster without a VPN or a forwarded port.

## Submit from Python
<a name="sagemaker-hyperpod-ray-remote-job-submission-python"></a>

To submit from Python, use Ray's standard `JobSubmissionClient` with the `sagemaker_ray` address. When the `toolkit-for-ray-on-sagemaker-ai` package is installed, it registers the address scheme, so no other change is needed.

```
from ray.job_submission import JobSubmissionClient

client = JobSubmissionClient("sagemaker_ray://{{my-cluster}}/{{my-namespace}}")
job_id = client.submit_job(
    entrypoint="python my-script.py",
    runtime_env={"working_dir": "./src"},
)
print(job_id)
```

## Tracking a submitted job
<a name="sagemaker-hyperpod-ray-remote-job-submission-tracking"></a>

The same address manages the job, so a job you submitted remotely is tracked remotely. Each command takes the job ID returned at submission.

```
ray job status {{my-job-id}} --address sagemaker_ray://{{my-cluster}}/{{my-namespace}}

ray job logs {{my-job-id}} --address sagemaker_ray://{{my-cluster}}/{{my-namespace}} --follow

ray job stop {{my-job-id}} --address sagemaker_ray://{{my-cluster}}/{{my-namespace}}
```

`ray job logs --follow` streams output until the job ends. `ray job stop` requests a graceful stop.

The Ray Dashboard **Jobs** view lists every job on the cluster with its status, start time, and logs. In Studio, the **Tasks** tab lists Ray workloads including submitted jobs. For more information, see [Managing Ray workloads with Studio](sagemaker-hyperpod-ray-manage-studio.md).

For the full set of Ray Jobs CLI commands and options, see [Quickstart using the Ray Jobs CLI](https://docs.ray.io/en/latest/cluster/running-applications/job-submission/quickstart.html) in the Ray documentation.