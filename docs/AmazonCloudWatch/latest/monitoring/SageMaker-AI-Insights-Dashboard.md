

# SageMaker AI Insights dashboard
<a name="SageMaker-AI-Insights-Dashboard"></a>

The SageMaker AI Insights dashboard is organized into three tabs: **Performance**, **Capacity**, and **Reliability**. Each tab provides a focused view of your inference endpoint health.

## Dashboard layout
<a name="SageMaker-AI-Insights-Dashboard-layout"></a>

### Summary bar
<a name="SageMaker-AI-Insights-Dashboard-summary-bar"></a>

The summary bar at the top of the dashboard shows fleet‐wide totals.

![SageMaker AI Insights dashboard header with summary bar showing Invocations, Instances, Inference Components, and Avg AZ Skew.](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/smai_New_Insights_Dashbaord.png)



| Metric | Description | 
| --- | --- | 
| Invocations | Total invocations across all endpoints in the selected time range | 
| Instances | Total number of instances currently serving traffic | 
| Inference Components | Total number of inference components across all endpoints | 
| Avg AZ Skew | Average availability zone distribution imbalance (0% = perfectly balanced) | 

### Filters panel
<a name="SageMaker-AI-Insights-Dashboard-filters"></a>


| Filter | Description | 
| --- | --- | 
| Endpoint | Select a specific endpoint or All endpoints for the fleet view | 
| Instance | Select a specific instance (requires an endpoint selected first) | 
| Inference component | Select a specific IC for granular filtering | 

### Drill-down
<a name="SageMaker-AI-Insights-Dashboard-drill-down"></a>

SageMaker AI Insights supports progressive drill‐down.

1. **Fleet level** (default)—all endpoints visible, summary metrics aggregated

1. **Endpoint level**—select an endpoint from the filter panel or choose an endpoint link in any table

1. **IC level**—select an inference component from the filter panel

### Cross-linking with the SageMaker AI console
<a name="SageMaker-AI-Insights-Dashboard-cross-linking"></a>
+ Choose an endpoint name to open the endpoint detail page in the SageMaker AI console.
+ Choose **View logs** to open CloudWatch Logs filtered to that endpoint or IC.
+ From the SageMaker AI console, choose **View in SageMaker AI Insights** or **Metrics** for a per‐IC row.

## Accessing the dashboard
<a name="SageMaker-AI-Insights-Dashboard-accessing"></a>

You can access the SageMaker AI Insights dashboard from multiple locations in the console.
+ **From the Endpoints list page:** Choose **View in SageMaker AI Insights** to open the dashboard at the fleet level with no filters applied.  
![Endpoints list page showing the View in SageMaker AI Insights button.](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/smai_Observability_Enabled_page.png)
+ **From the endpoint detail page:** Choose **View in SageMaker AI Insights** to open the dashboard filtered to that endpoint.  
![Endpoint detail page showing the View in SageMaker AI Insights button.](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/smai_Endpoint_detail_page.png)
+ **From the inference component detail page:** Choose **View in SageMaker AI Insights** to open the dashboard filtered to that endpoint and inference component.  
![Inference component detail page showing the View in SageMaker AI Insights button.](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/smai_IC_Detaild_page.png)
+ **Direct navigation:** CloudWatch console → **Infrastructure monitoring** → **SageMaker AI Insights**.

## Performance tab
<a name="SageMaker-AI-Insights-Dashboard-performance"></a>

The **Performance** tab answers "is it healthy?" and "why is it slow?"—flowing from fleet‐wide health at the top to per‐IC diagnostics at the bottom.

Performance health  
Honeycombs grouped by AZ showing alarm state for instances, IC copies, and endpoints at a glance.  

![Performance health honeycombs showing alarm state by AZ.](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/smai_Performance_health_AZ_honey_comb.png)


Instance performance table  
Per‐instance breakdown showing TTFT (P50/P99), output TPS (avg/max), concurrent requests (live/max), and KV cache utilization.  

![Instance performance table showing TTFT, output TPS, concurrent requests, and KV cache.](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/smai_Instance_health_performance_tab.png)


Token streaming  
Time‐series chart showing TTFT and inter‐token latency (ITL) with a P50/P99 toggle, broken down by framework.  

![Token streaming chart showing TTFT and ITL P50/P99 over time.](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/smai_Token_streaming.png)


Token throughput  
Input and output tokens per second by framework, with toggles for Input/Output, Percentiles, and By instance views.  

![Token throughput chart showing input and output tokens per second.](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/smai_Token_throughput.png)


Engine and request pressure  
KV cache utilization (%), running requests, and waiting requests over time—key saturation signals for the inference engine.  

![Engine and request pressure panel showing KV cache, running requests, and waiting requests.](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/smai_Engine_and_request_pressure.png)


Traffic distribution  
Per‐instance or per‐IC‐copy table showing invocations per minute, 4XX rate, and 5XX rate to identify routing imbalances.  

![Traffic distribution table showing invocations per minute, 4XX rate, and 5XX rate by instance.](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/smai_Traffic_distribution.png)


Error mix over time  
Line chart showing 4XX, 5XX, and mid‐stream error rates over time per IC.  

![Error mix over time line chart showing 4XX, 5XX, and mid-stream errors.](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/smai_Error_mix_over_time.png)


Latency breakdown over time  
Stacked area chart with tabs for Invoke (model latency \+ overhead latency) and Streaming (first chunk model \+ first chunk overhead), with a P50/P90 toggle.  

![Latency breakdown over time stacked area chart showing model latency and overhead latency.](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/smai_Latency_breakdown_over_time.png)


## Capacity tab
<a name="SageMaker-AI-Insights-Dashboard-capacity"></a>

The **Capacity** tab answers "do I have headroom?" and "is my hardware healthy?"—showing actual utilization compared to reserved capacity.

Capacity health  
The same honeycomb visualization as the **Performance** tab, showing alarm state for instances, IC copies, and endpoints.  

![Capacity health honeycombs showing alarm state by AZ.](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/smai_Capacity_health_honey_comb.png)


Instance capacity table  
Per‐instance utilization bars for GPU, GPU memory, CPU, memory, and disk.  

![Instance capacity table showing GPU, GPU memory, CPU, memory, and disk utilization.](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/smai_Instance_health_capacity_tab.png)


Fleet utilization  
Time‐series showing CPU, GPU, GPU memory, memory, and disk utilization per instance, with toggles for Instance, IC copies, and Endpoint views.  

![Fleet utilization chart showing CPU, GPU, GPU memory, memory, and disk utilization per instance over time.](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/smai_Fleet_Util.png)


## Reliability tab
<a name="SageMaker-AI-Insights-Dashboard-reliability"></a>

The **Reliability** tab answers "is it resilient?" and "why did scaling fail?"—covering AZ distribution, scaling behavior, and provisioning events.

Availability Zone distribution  
Bar chart showing instance or IC copy count per AZ to validate high availability (HA) compliance.  

![Availability Zone distribution bar chart showing instance count per AZ.](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/smai_AZ_distribution.png)


Cold start anatomy  
Horizontal stacked bar showing the breakdown of provisioning time into model download, GPU load, container start, and platform overhead (IC endpoints only).  

![Cold start anatomy showing model download, GPU load, container start, and platform overhead.](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/smai_Cold_start_anatomy.png)


ICE diagnostics  
Insufficient Capacity Error (ICE) count over time with an event table showing time, endpoint, failed instance type, and failed AZ. Non‐zero values indicate capacity constraints.  

![ICE diagnostics panel showing ICE count over time and an event table.](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/smai_ICE_events.png)
