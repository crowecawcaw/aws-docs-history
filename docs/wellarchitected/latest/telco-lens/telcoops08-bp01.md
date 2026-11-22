

# TELCOOPS08-BP01 Develop and execute thorough failure testing programs that reflect cloud infrastructure characteristics

 Many telco deployments inherit resilience assumptions from on-premises networks with redundant physical paths and binary failures. Cloud infrastructure fails differently, with a spectrum of degradation that aggressive on-premises timers misread. This best practice builds a failure testing program that reflects cloud failure modes and validates that network functions behave correctly under them. 

 **Desired outcome:** 
+  A documented failure testing program that covers cloud-specific failure modes relevant to your telco workloads. 
+  CNF vendors have validated their software under realistic cloud failure modes, including degraded network conditions and partial Availability Zone impairment. 
+  Performance baselines under failure conditions that inform capacity planning and service-level commitments. 

 **Common anti-patterns:** 
+  Limiting failure testing to EC2 instance termination or pod deletion without testing network-layer impairments. 
+  Assuming that on-premises resilience testing results transfer to cloud deployments without re-validation. 
+  Not testing CNF health-monitoring timers under cloud-realistic latency and packet-loss conditions. 
+  Running failure tests only in non-production environments that don't reflect production traffic patterns and scale. 

 **Benefits of establishing this best practice:** 
+  Resilience is evidence-based rather than assumed, giving confidence in system behavior under realistic failure conditions. 
+  Health-check and failover timers are tuned for cloud network characteristics, which reduces unnecessary failovers. 
+  Known failure modes have documented, tested recovery procedures, which reduces incident impact. 
+  ISV software is validated against cloud-specific failure scenarios with documented results, which supports vendor accountability. 

 **Level of risk exposed if this best practice is not established:** High \#\# Implementation guidance On-premises environments tend toward binary failures, where a device is either up or down. On the other hand, cloud environments fail on a spectrum, where latency rises, throughput falls, or a service is partially impaired without failing outright. Many telco CNFs run health-monitoring timers designed for on-premises networks where redundant physical paths make a lost heartbeat a reliable signal of failure. In the cloud, a single impairment can affect several interfaces at once, and a timer calibrated for on-premises certainty fires a false positive and triggers an unnecessary failover. The health-monitoring logic itself is often the failure mode to expose. Generic chaos engineering that terminates instances confirms that automatic scaling works but does not explore how a CNF's SCTP heartbeat or GTP-C echo timer behaves under 30 ms of added latency and 2% packet loss. Design experiments around the specific timers and thresholds that govern each network function's failover behavior. Work with the CNF vendor to identify those thresholds, because you usually can't see them from outside the software. The program's output is a set of tuned timer values with recorded rationale that the vendor agrees to support. Record steady-state behavior (session counts, signaling rates, call-setup times) before injecting failure, so you can interpret the results against the baseline. Run experiments first in pre-production with synthetic traffic, then in production during low-traffic windows, because a failure mode that only appears at production scale will not show up in a lab. \#\#\# Implementation steps 
+  Catalog CNF failure sensitivities: with each vendor, document the health-monitoring timers, failover thresholds, and recovery behaviors for each CNF, including SCTP timers, GTP-C echo intervals, and OAM connectivity thresholds. 
+  Establish steady-state baselines: before injecting failures, record steady-state metrics such as subscriber session counts, signaling message rates, and call-setup times, so failure-state behavior can be compared meaningfully. 
+  Design cloud-realistic experiments: create AWS Fault Injection Service templates that inject transient packet loss, latency spikes, partial AZ degradation, and ENI-level impairments, and map each experiment to a specific CNF sensitivity. 
+  Execute experiments in staged environments: run experiments first in pre-production with synthetic traffic, then in production during low-traffic windows, documenting CNF behavior at each failure threshold. 
+  Tune timers based on results: work with vendors to adjust health-monitoring timers that trigger false-positive failovers under cloud conditions, and record the optimized values and the rationale for each change. 
+  Establish a recurring cadence: schedule periodic failure testing across the full experiment catalog, and repeat it after CNF upgrades, instance-type changes, or new failure modes identified from production incidents. \#\# Resources **Key AWS services:** 
+  [AWS Fault Injection Service (FIS)](https://aws.amazon.com/fis/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [AWS Resilience Hub](https://aws.amazon.com/resilience-hub/) 