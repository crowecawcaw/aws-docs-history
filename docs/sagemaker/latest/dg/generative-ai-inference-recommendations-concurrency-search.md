

# Find the maximum concurrency an endpoint can serve under an SLA
<a name="generative-ai-inference-recommendations-concurrency-search"></a>

When you benchmark a generative artificial intelligence (generative AI) endpoint, you often want to find its maximum *concurrency*. Concurrency is the number of simultaneous requests the endpoint handles while still meeting a performance target, such as a latency ceiling. You can explore concurrency in two ways in a single benchmark job:
+ **Concurrency list** – Benchmark a fixed set of concurrency levels (for example, 1, 10, and 100) in one job. Use this when you already know the levels you want to compare.
+ **Find-max-concurrency search** – Use this option to find the largest concurrency that still satisfies one or more service-level agreement (SLA) thresholds, without manually specifying the levels to test.

## SLA parameters
<a name="concurrency-search-slas"></a>

Specify one or more SLA thresholds in the workload configuration parameters. The winning concurrency must satisfy *all* of the thresholds that you set.


| Parameter | Meaning | Requires streaming | 
| --- | --- | --- | 
| ttft\_sla\_ms | Maximum time to first token, in milliseconds | Yes | 
| tpot\_sla\_ms | Maximum time per output token (inter-token latency), in milliseconds | Yes | 
| e2e\_sla\_ms | Maximum end-to-end request latency, in milliseconds | No | 
| error\_rate\_sla | Maximum fraction of failed requests (for example, 0.01 for 1 percent) | No | 

**Note**  
Set `search_stat` to choose the statistic that the latency SLA is evaluated on: `avg` (default), `p50`, `p90`, `p95`, or `p99`. Bound the search with the optional `concurrency_min` and `concurrency_max` parameters, and cap cost with `search_max_iterations`.

## Benchmark a list of concurrency levels
<a name="concurrency-list-example"></a>

Pass a list to the `concurrency` parameter of the workload configuration. The benchmark runs each level and writes per-level results under `concurrency_{{N}}/` directories in the output.

**Python (Boto3)**

```
client.create_ai_workload_config(
    AIWorkloadConfigName="concurrency-list-config",
    AIWorkloadConfigs={"WorkloadSpec": {"Inline": json.dumps({
        "benchmark": {"type": "aiperf"},
        "parameters": {
            "tokenizer": "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
            "streaming": True,
            "prompt_input_tokens_mean": 128,
            "output_tokens_mean": 256,
            "concurrency": [1, 10, 100],   # list -> sweep each level in one job
            "request_count": 100,
        },
    })}},
)
```

## Search for the maximum concurrency under an SLA
<a name="concurrency-search-example"></a>

Set `search_recipe` to `max-concurrency-under-sla` and provide at least one SLA threshold. Do *not* also set a fixed `concurrency` value; the search selects it.

**Python (Boto3)**

```
client.create_ai_workload_config(
    AIWorkloadConfigName="find-max-config",
    AIWorkloadConfigs={"WorkloadSpec": {"Inline": json.dumps({
        "benchmark": {"type": "aiperf"},
        "parameters": {
            "tokenizer": "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
            "streaming": True,
            "prompt_input_tokens_mean": 128,
            "output_tokens_mean": 256,
            "search_recipe": "max-concurrency-under-sla",
            "e2e_sla_ms": 5000,        # end-to-end latency ceiling (ms)
            "ttft_sla_ms": 1000,       # time-to-first-token ceiling (ms)
            "search_stat": "p99",      # evaluate the SLA on p99
            "concurrency_min": 1,
            "concurrency_max": 256,
            "search_max_iterations": 15,
        },
    })}},
)
```

Create a benchmark job that references the workload configuration and targets your endpoint, and then poll it to a terminal state. For the full `create_ai_benchmark_job` and `describe_ai_benchmark_job` sequence, see [Benchmark generative AI inference endpoints](generative-ai-inference-recommendations-benchmark.md).

**Important**  
The `error_rate_sla` threshold requires a benchmarking tooling version that reports the request error-rate metric on runs that have no errors. On tooling versions that do not report this metric, the service treats every candidate concurrency as failing the SLA and finds no feasible level. Until your account's tooling is updated, gate the search on latency SLAs (`ttft_sla_ms`, `tpot_sla_ms`, or `e2e_sla_ms`). Then review the winning level's error rate in the results.

## Read the search result
<a name="concurrency-search-results"></a>

A find-max-concurrency search writes a `search_history.json` file at the root of the job's output. The winning concurrency is at `boundary_summary.feasible_max.value`, which is the largest level that satisfied every SLA. If no level met the SLA, `feasible_max` is `null` and `boundary_summary.infeasible_min` records the smallest level that breached it.

**Python (Boto3)**

```
import io, json, tarfile

resp = client.describe_ai_benchmark_job(AIBenchmarkJobName="find-max-job")
location = resp["OutputConfig"]["S3OutputLocation"]     # s3://bucket/prefix/
bucket, _, prefix = location.replace("s3://", "").partition("/")

obj = s3.list_objects_v2(Bucket=bucket, Prefix=prefix)["Contents"]
tar_key = next(o["Key"] for o in obj if o["Key"].endswith("output.tar.gz"))
body = s3.get_object(Bucket=bucket, Key=tar_key)["Body"].read()

with tarfile.open(fileobj=io.BytesIO(body), mode="r:gz") as tar:
    member = next(m for m in tar.getnames() if m.endswith("search_history.json"))
    history = json.loads(tar.extractfile(member).read())

boundary = history["boundary_summary"]
feasible_max = boundary.get("feasible_max")
if feasible_max and feasible_max.get("value") is not None:
    print("Max concurrency under SLA:", feasible_max["value"])
else:
    print("No level met the SLA. Smallest breaching level:",
          boundary.get("infeasible_min", {}).get("value"))
```