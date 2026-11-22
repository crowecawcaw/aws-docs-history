

# TELCOOPS09-BP01 Implement Prometheus-based observability with Nitro network metrics for telco workload performance baselining

 Telco cloud-based network functions (CNFs) expose Prometheus-compatible metrics as their native observability interface, and accurate baselines depend on collecting those alongside Amazon EC2 instance and Nitro network metrics. A baseline drawn from short benchmarks on a fresh instance overstates real capacity because it misses multitenant contention and instance network limits. 

 **Desired outcome:** 
+  The observability stack collects both CNF-native Prometheus metrics and infrastructure metrics such as Elastic Network Adapter (ENA) allowance counters and network throughput in a unified environment. 
+  Baselines are derived from sustained measurements under production-representative traffic rather than short benchmarks on freshly launched instances. 
+  ENA allowance-exceeded counters are monitored to indicate when the workload approaches instance network limits. 

 **Common anti-patterns:** 
+  Relying on basic Amazon CloudWatch metrics without collecting the CNF's native Prometheus metrics that show application-level performance. 
+  Conducting baselines on single runs or on freshly launched instances, which produces optimistically high results that don't hold under multitenant conditions. 
+  Ignoring ENA driver metrics that signal network saturation before it becomes subscriber-impacting. 
+  Treating pps\_allowance\_exceeded as the sole indicator of saturation without correlating it with actual throughput. 

 **Benefits of establishing this best practice:** 
+  CNF metrics are collected through the Prometheus interface the vendor designs and tests against, which avoids lossy translation. 
+  ENA and Nitro metrics give early warning of network-layer constraints that CNF-level metrics can't detect. 
+  Baselines reflect sustained, multitenant performance, so infrastructure is sized from real behavior rather than optimistic benchmarks. 
+  Measured baselines let vendors distinguish expected multitenant behavior from genuine performance regressions. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Telco CNF vendors expose operational metrics through Prometheus endpoints because that is the format their own engineering teams use for development, testing, and support. Routing those metrics through a different collection path loses granularity and opens a gap between what the operator can observe and what the vendor can support. Scrape the CNF's /metrics endpoints and store the data in a Prometheus-compatible backend so operator and vendor see the same data. Amazon Managed Service for Prometheus provides that backend without the operator running Prometheus servers. 

 Application metrics alone are not enough, because the constraints that limit telco workloads are often below the application. Cloud infrastructure is multitenant: Nitro cards, network bandwidth, and storage I/O are shared, and AWS enforces per-instance limits on bandwidth, packets per second, and connection tracking. The ENA driver exposes counters (such as bw\_in\_allowance\_exceeded, bw\_out\_allowance\_exceeded, pps\_allowance\_exceeded, and conntrack\_allowance\_exceeded) that increment when a workload pushes against those limits, and for a user-plane function processing millions of packets per second these counters are the earliest warning of saturation. These counters are not in Amazon CloudWatch by default, so use a node-exporter or Amazon CloudWatch agent to bring them into the same environment as the CNF metrics. pps\_allowance\_exceeded can increment from microbursts or protocol-specific patterns, not only from a true PPS ceiling, so correlate it with measured throughput before concluding that an instance type is undersized. 

 Shared tenancy means the performance a workload experiences depends on traffic patterns and neighbor activity, so a benchmark on a freshly launched instance with temporary exclusive hardware access produces high numbers that don't hold under production load. A UPF that benchmarks at 10 Mpps on a fresh instance may sustain only 8 Mpps under realistic multitenant load, and capacity planning must use the sustained number. That means measuring for extended periods (72 hours or more) under a realistic protocol mix and packet-size distribution, recording percentiles rather than averages, and sizing from p95 sustained performance with margin for measured variance. \#\#\# Implementation steps 
+  Deploy a Prometheus backend and scrape CNF metrics: create an Amazon Managed Service for Prometheus workspace and deploy a scraper that discovers CNF pod /metrics endpoints, and confirm that session counts, signaling rates, and packet-processing latency are collected. 
+  Collect ENA and Nitro infrastructure metrics by configuring an Amazon CloudWatch agent or Prometheus node-exporter to gather ENA allowance-exceeded counters, and build Amazon Managed Grafana dashboards that correlate them with CNF-level metrics. 
+  Define realistic traffic profiles: document the protocol mix (SCTP, GTP-U, PFCP), packet-size distribution, and flow count that match production, and avoid synthetic benchmarks that use uniform packet sizes or single flows. 
+  Measure sustained baselines by running tests for at least 72 hours under representative traffic, recording p50, p95, and p99 for key metrics, and testing at multiple load levels (for example, 25%, 50%, 75%, 90%) to find where contention effects begin. 
+  Set alerts on baseline percentiles when metrics exceed p95 (early warning) or p99 (immediate investigation), using ENA allowance-exceeded counters as leading indicators that fire before CNF-level degradation appears. 
+  Validate and share with vendors: require vendors to demonstrate published performance on your target instance types, document any gaps, and share measured baselines so their support teams can distinguish expected behavior from genuine regressions. \#\# Resources **Key AWS services:** 
+  [Amazon Managed Service for Prometheus](https://aws.amazon.com/prometheus/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Amazon Managed Grafana](https://aws.amazon.com/grafana/) 
+  [Amazon EC2](https://aws.amazon.com/ec2/) 