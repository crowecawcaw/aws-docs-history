

# PERF01-BP03 Derive and establish KPIs that validate adherence to your performance requirements

 Key performance indicators turn raw operational metrics into business-relevant signals that show whether a workload meets its goals. 

 **Desired outcome:** 
+  You have a defined set of KPIs that measure whether the workload meets its performance requirements. 
+  Your KPIs align with business objectives and rest on specific operational metrics. 
+  Your KPIs are measurable and actionable, giving teams concrete data to act on. 
+  You review and adjust KPIs on a cadence as business needs and the workload change. 

 **Common anti-patterns:** 
+  Teams deploy a monitoring solution without the observability, logging, and tracing needed to support it. 
+  Teams rely on a single high-level metric such as average response time and miss the full range of performance behavior. 
+  Teams apply one set of KPIs to every workload instead of tailoring them to each one. 
+  Teams treat performance validation as a one-time task with no feedback loop for improvement. 
+  Teams define KPIs that are not tied to performance requirements or business objectives. 

 **Benefits of establishing this best practice:** 
+  Workload performance ties directly to business needs through aligned measurement. 
+  Teams make informed decisions about optimization and resource allocation from concrete data. 
+  Granular metrics beneath each KPI speed root-cause analysis when performance drops. 
+  Regular review keeps the KPIs relevant as the workload and the business evolve. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 A metric is a raw measurement: CPU utilization, queue depth, disk I/O, request count. A KPI is a business-oriented indicator built from one or more metrics. It answers a stakeholder question, such as whether users get a responsive experience or whether the daily batch completes within its window. Figure 1 shows this relationship. <a name="perf01-bp03-fig1"></a>

![Diagram showing how one or more raw metrics combine into a KPI that answers a business-oriented question.](https://docs.aws.amazon.com/wellarchitected/latest/framework/images/bp03.png)

*Relationship between metrics and KPIs*


 An average can hide patterns - for example, a mean response time of 200 milliseconds can conceal that one user in twenty waits three seconds. Percentile-based indicators such as p95 and p99 help avoid this. A real-time web application depends on latency percentiles, a batch pipeline on completion time and throughput, and a machine learning inference service on both latency and cost per prediction. 

 Each indicator needs a baseline from historical data, a target range tied to your performance requirements and any service-level agreements, and thresholds that separate acceptable performance from warning and critical states. Set these values with input from business stakeholders and, where relevant, external service providers. 

 Business needs shift, traffic grows, and a KPI that was meaningful last quarter can lose relevance. Treat KPI definition as a cycle: measure, compare against targets, act on deviations, and refine to stay aligned with business goals. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Understand your workload and business objectives:** Classify the workload type, such as a real-time web application, a batch pipeline, or a machine learning service, because each type demands different performance measures. Identify the business objectives the workload supports so your KPIs can trace back to them. 

1.  **Select KPIs and supporting metrics:** Choose primary KPIs that reflect business outcomes, such as response time or latency, throughput, error rate, cost per transaction, or user satisfaction. For each KPI, identify the operational metrics that feed it, and add custom KPIs where your domain requires them. 

1.  **Set targets, baselines, and thresholds:** Establish a baseline from historical data and a target range for each KPI based on your performance requirements and service-level agreements. Define thresholds for acceptable, warning, and critical performance with input from business stakeholders. 

1.  **Instrument collection and monitoring:** Decide how you will collect the data for each KPI through monitoring tools, logs, or instrumentation, and confirm the underlying observability is in place. Configure collection at intervals that match how quickly the workload can change. 

1.  **Validate KPIs through performance testing:** Run performance tests and benchmarks under varied load to confirm your KPIs and targets hold up. Use the results to find bottlenecks and to correct any KPI or target that testing shows to be unrealistic. 

1.  **Monitor, analyze, and act on deviations:** Track KPI data for trends and anomalies, and correlate it with underlying metrics, logs, and events for deeper insight. When a KPI moves outside its target range, investigate the root cause and apply the necessary optimization. 

1.  **Review, refine, and communicate:** Reassess the relevance of each KPI on a cadence, retire or add indicators as requirements change, and share KPI data with product, business, and operations stakeholders to keep engineering aligned with business goals. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [PERF01-BP01 Validate requirements align to business needs](perf01-bp01.md) 
+  [PERF01-BP04 Establish criteria for performance degradation alerts and tolerances](perf01-bp04.md) 
+  [PERF05-BP02 Evaluate your workload performance](perf05-bp02.md) 
+  [PERF05-BP05 Review metrics at regular intervals](perf05-bp05.md) 

 **Related documents:** 
+  [Navigating the Cloud: Key Performance Indicators for Success](https://aws.amazon.com/blogs/enterprise-strategy/navigating-the-cloud-key-performance-indicators-for-success/) 
+  [KPIs – Enterprise Journey from Technology to Business](https://aws.amazon.com/blogs/mt/kpis-enterprise-journey-from-technology-to-business/) 