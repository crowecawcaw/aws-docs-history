

# AI Inference Insights

AI Inference Insights is the CloudWatch Omni observability experience for self-hosted inference engines. It covers inference workloads that run on Amazon ECS and on Amazon EKS.

AI Inference Insights brings together telemetry from the following layers of your inference stack. For how to send this telemetry, see [Collect AI inference telemetry](omni-send-ai-inference-telemetry.md).
+ **Inference engine** – vLLM. Its own Prometheus metrics, under their native `vllm:` prefix. These give you request rate, token throughput, time to first token, end-to-end latency, queue depth, and KV cache usage.
+ **Accelerator** – NVIDIA GPUs, through the DCGM exporter. These give you accelerator utilization, memory, power, and temperature.
+ **Application** – the topology that Omni builds from your traces, which makes the workload appear as a service with an application.

**Note**  
The Amazon CloudWatch console provides this same capability, over the same telemetry, as Accelerated Compute Insights. That console covers Amazon EKS only, while AI Inference Insights also covers Amazon ECS. For more information, see [Accelerated Compute Insights](Accelerated-Compute-Insights.md).

## What you can do
<a name="omni-ai-inference-insights-what-you-can-do"></a>

With AI Inference Insights, you can do the following:
+ **Collect the telemetry** – Publish engine metrics, DCGM accelerator metrics, and traces so that your inference workloads appear. See [Collect AI inference telemetry](omni-send-ai-inference-telemetry.md).
+ **Survey the fleet** – Open the AI Inference fleet page, which shows one row for each inference workload, ranked by fault rate, with aggregate charts for the Region. See [AI Inference fleet page](#omni-ai-inference-insights-fleet-page).
+ **Investigate one workload** – Scope to a single workload for its identity, headline numbers, engine configuration, metrics, traces, and logs. See [Workload insights page](#omni-ai-inference-insights-workload-page).
+ **Judge accelerator efficiency** – Calculate approximate memory bandwidth and math throughput utilization, and get an AI-generated recommendation. See [Workload insights page](#omni-ai-inference-insights-workload-page).
+ **Read the fault numbers correctly** – Learn which engine outcomes AI Inference Insights counts as faults, and which it does not. See [How fault rate is calculated](#omni-ai-inference-insights-fault-rate).

## AI Inference fleet page
<a name="omni-ai-inference-insights-fleet-page"></a>

The AI Inference fleet page shows one row for each inference workload. You can open it in 3 ways:
+ Choose the **AI Inference** tile, described as **Monitor the AI inference fleet**.
+ Use the `>` command completion.
+ Run the `/inference list` command, described as **Open the AI Inference fleet page**.

The table panel title is **Inference workloads ({{N}})**, where {{N}} is the number of rows that the rail filters keep. The table shows 10 rows on each page.

The table has the following columns:
+ **Workload name** – Links to the insights page for that workload.
+ **Application name** – Opens the application map, filtered to that application. A workload that belongs to no application shows **None**. A workload that belongs to several applications shows each of them.
+ **Request rate** – Engine requests for the workload, averaged over the time range.
+ **Token throughput** – Generated tokens for the workload, averaged over the time range, shown as tok/s.
+ **Fault rate** – The share of engine requests that failed. See [How fault rate is calculated](#omni-ai-inference-insights-fault-rate) for the exact definition.
+ **TTFT p95** – Time to first token for the workload, as the 95th percentile over the time range.
+ **Hosted in** – Where the workload runs.

The table opens sorted by **Fault rate**, highest first. You can sort every column from its header. A row with a missing value appears at the bottom in either sort direction.

To narrow the rows that are already loaded, enter text in the **Find** box. It matches the workload name or an application name. **Find** narrows only the rows shown. It does not change the analysis rail facets, and it does not change the count in the panel title.

To filter the table itself, open the **Analyze** rail from the title bar. The rail stays closed until you open it. It offers the facets **Health**, **Instrumentation**, **Application**, **Service Name**, **Environment**, and **Platform**.

### Aggregate fleet charts
<a name="omni-ai-inference-insights-fleet-charts"></a>

The fleet page shows 8 aggregate charts for the fleet after the table, in 2 rows of 4. The accelerator row holds **GPU utilization**, **DRAM active**, **GPU memory-copy utilization**, and **GPU power draw**.

The workload row holds **Token throughput**, **Request rate**, **Time to first token (p95)**, and **End-to-end latency (p99)**.

Keep 2 caveats in mind when you read the accelerator charts:
+ The accelerator charts average across every reporting accelerator in the Region. **GPU power draw** is therefore the draw of one accelerator, not a total for the fleet.
+ **DRAM active** comes from DCGM profiling metrics, which only some accelerators report. This chart can cover fewer accelerators than the other 3 accelerator charts.

## Workload insights page
<a name="omni-ai-inference-insights-workload-page"></a>

The workload insights page always covers one workload. You cannot open it without a service.

To open it from the application map, use any of the following, which are equivalent:
+ Choose the **Inference insights** card in the service drawer.
+ Choose **Inference insights** in the **Actions** menu of the full-page service header.
+ Choose **Inference insights** in the hover popover of the service's node on the map.

You can also reach the page from a **Workload name** link on the fleet page.

The page holds 3 panels in the following order.

### Workload Overview
<a name="omni-ai-inference-insights-workload-overview"></a>

**Workload Overview** gives the workload's identity and its headline numbers. It shows the attributes **Workload**, **Application**, **Served model**, **Hosted in**, **Accelerators**, and **Replicas**. When accelerator capacity data is available, it also shows **Accelerators allocated** and **Accelerators idle**.

The following attributes have specific definitions:
+ **Served model** – The model name that the engine reports.
+ **Replicas** – The number of distinct pods and Amazon ECS tasks that reported most recently.

The panel has 2 sections:
+ **KPI Metrics** – Open by default. It holds the tiles **Request rate**, **TTFT p95**, **Error rate**, and **Gen tok/s**.
+ **Engine Configuration** – Collapsed by default. It holds the engine's startup arguments: model, quantization, data type, max model length, tensor parallel, GPU memory target, eager mode, and prefix caching. Omni masks arguments that carry credentials.

### Accelerator Efficiency Summary
<a name="omni-ai-inference-insights-accelerator-efficiency"></a>

**Accelerator Efficiency Summary** holds 3 calculated values and an AI-generated recommendation. To calculate the values and get an **Efficiency Improvement Recommendation**, choose **Generate Summary** in the panel title.

The panel has the following tiles:
+ **MBU approx.** – The share of the accelerator's peak memory bandwidth that the workload uses.
+ **MFU approx.** – The share of the accelerator's peak compute that the model's calculations use.
+ **Roofline ratio** – Arithmetic intensity divided by the accelerator's ridge point. Below 1x, memory bandwidth limits the work. Above 1x, math throughput limits it.

**Important**  
All 3 values are approximations, not measurements. AI generates the **Efficiency Improvement Recommendation**. We recommend that you confirm any change against your own benchmarks.

### Signals
<a name="omni-ai-inference-insights-signals"></a>

Only the open tab loads its data. The **Signals** panel holds charts and signals on the following 4 tabs:
+ **Workload Metrics** – Holds the sections **Overview**, **Load & scheduling**, and **Cache**.
+ **Accelerator Insights** – Holds the sections **Overview**, **Power & thermals**, and **Interconnect**.
+ **Traces** – Shows the workload's traces.
+ **Logs** – Shows the workload's logs.

## How fault rate is calculated
<a name="omni-ai-inference-insights-fault-rate"></a>

**Fault rate** reads the engine's own request counter, `vllm:request_success_total`. It counts a request that the engine finished with the finish reason `error`.

vLLM sets that finish reason on a request-level internal error, and it returns HTTP 500 for that request. The other finish reasons are not faults. Those reasons are `stop`, `length`, `abort`, and `repetition`.

**Note**  
AI Inference Insights does not count a 5xx response that never reaches the engine. For example, a crashed engine or a router in front of the engine can return 5xx without the engine recording a request.

**Fault rate** has the same basis as the **Error rate** tile on the workload insights page. A row on the fleet page therefore agrees with that workload's own page.

AI Inference Insights derives counts from rates multiplied by the window, so counts are estimates. It rounds them to whole requests.

## Time ranges longer than 24 hours
<a name="omni-ai-inference-insights-time-range-limit"></a>

CloudWatch rejects a range selector longer than 24 hours. When you select a time range longer than 24 hours, AI Inference Insights covers only the last 24 hours of that range.

In that case, the rates and **TTFT p95** cover the last 24 hours of the range. The list of workloads holds only the workloads seen in those last 24 hours. AI Inference Insights covers a range of 24 hours or shorter in full.