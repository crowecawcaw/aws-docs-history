

# TELCOREL02-BP05 Optimize failure recovery timers for the shared tenancy and potential for transient network issues in cloud environments
<a name="telcorel02-bp05"></a>

 Network-function vendors often set health-monitoring timers for on-premises networks with redundant physical paths, where a lost heartbeat reliably means failure. In the cloud, transient variance from shared tenancy can trip those aggressive timers and cause failovers even though the function is healthy. This best practice retunes those timers for cloud conditions with the vendors who own them. **Desired outcome:** 
+  Network functions detect, react to, and recover from genuine network issues and failures. 
+  Health-monitoring and failure-recovery timers balance prompt failure detection against resilience to false positives. 
+  Native cloud capabilities supplement vendor-provided failure detection and recovery. **Common anti-patterns:** 
+  Deploying network functions with on-premises timer defaults, so normal cloud network variance triggers unnecessary failovers. 
+  Tuning timers without the vendor, so changes conflict with the function's internal recovery logic. 
+  Relying only on vendor health checks without supplementing them with cloud-based monitoring. 
+  Not testing recovery behavior after retuning, so the new timer values are unvalidated. **Benefits of establishing this best practice:** 
+  False-positive failovers drop because timers tolerate transient cloud variance while still catching real failures. 
+  Failure detection stays prompt where it matters, preserving availability without instability. 
+  Cloud-based monitoring adds detection and recovery paths beyond what the vendor provides alone. 
+  Validated timer values give confidence that recovery behaves correctly under real failure conditions. **Level of risk exposed if this best practice is not established:** Medium \#\# Implementation guidance On-premises, a health-monitoring timer can be aggressive because redundant physical paths make a missed heartbeat a strong signal of genuine failure. In the cloud, shared tenancy introduces normal transient latency and jitter, and a single impairment can touch multiple interfaces at once. An aggressive timer reads that normal variance as a fault and fails over, which is both unnecessary and disruptive. Recalibrate failure detection for the statistical behavior of cloud networks. These timers are implemented in vendor software and interact with the function's recovery logic, so retune them with the vendor. The vendor understands what each timer governs and how changing it affects failover. You know your cloud network's actual behavior. Together, you widen detection windows enough to absorb transient variance, while keeping them tight enough to catch real failures. Preserve the internal state machines that depend on those timers. Supplement vendor mechanisms with cloud-based monitoring. Resource, network, and application-level metrics can distinguish a genuine failure from transient noise and drive cloud-based recovery such as instance replacement or scaling. Validate the retuned timers by injecting realistic cloud failures and observing their behavior. \#\#\# Implementation steps 
+  Engage vendors on timer behavior: work with each network-function vendor to understand their default health-monitoring and recovery timers and what each governs. 
+  Add multi-layered monitoring: use Amazon CloudWatch for resource, network, and application metrics, and AWS Lambda health checks for application-level signals that supplement vendor detection. 
+  Retune detection timers with the vendor: adjust health-check intervals, detection thresholds, and recovery timeouts to tolerate transient cloud variance while still catching real failures, keeping them consistent with the function's internal logic. 
+  Integrate cloud-based recovery: connect vendor recovery to cloud mechanisms such as Amazon EKS self-healing and Auto Scaling, with automated recovery workflows for different failure types. 
+  Validate with fault injection: use AWS Fault Injection Service to inject realistic failures and network impairments, confirm the retuned timers behave correctly, and document the final configuration. \#\# Resources **Key AWS services:** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [AWS Lambda](https://aws.amazon.com/lambda/) 
+  [Amazon EKS (Elastic Kubernetes Service)](https://aws.amazon.com/pm/eks/) 
+  [AWS Fault Injection Service (FIS)](https://aws.amazon.com/fis/) 