

# ADVPERF02-BP03 Consider low-latency node provisioning tools to improve startup and scaling time
<a name="advperf02-bp03"></a>

 Integrate observability metrics to initiate scaling of compute resources. Use just-in-time node provisioning and event-driven automatic scaling, which provide low-startup-latency scaling for container workloads. Traditional cluster automatic scaling with standard warm-up times introduces node provisioning delays that cause pods to queue during advertising traffic bursts. 

 **Desired outcome:** 
+  Your Kubernetes clusters on AWS scale out quickly enough to absorb sudden traffic spikes without pods experiencing resource starvation or elevated latency while waiting for new nodes. 
+  Node provisioning, workload scheduling, and horizontal scaling operate together as a coordinated, low-latency system. 
+  Scaling signals are driven by advertising-specific metrics (bid request queue depth, auction completion rate) rather than lagging infrastructure metrics (CPU utilization) alone. 

 **Common anti-patterns:** 
+  Relying on traditional Kubernetes Cluster Autoscaler with standard Auto Scaling group warm-up times, which introduces node provisioning delays that queue pods during traffic bursts and increase bid response latency. 
+  Scaling compute reactively only after pods are already resource-constrained, rather than provisioning nodes proactively based on leading signals from the Horizontal Pod Autoscaler. 
+  Setting a fixed node pool size without auto scaling, so operators must manually add capacity before major advertising events. 

 **Benefits of establishing this best practice:** 
+  Karpenter integrates directly with AWS APIs, bypassing the intermediary layers that slow traditional auto scaling. Faster node provisioning means your cluster responds to burst traffic before workloads are affected, keeping latency predictable even during demand spikes common in programmatic advertising. 
+  KEDA extends scaling to advertising-specific external signals, enabling scale-out decisions to be driven by queue depth or custom bid metrics rather than CPU utilization alone. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Advertising traffic arrives in bursts correlated with live events, campaign launches, and daypart peaks. When a burst arrives, infrastructure can't respond fast enough. Pending pods queue, bid requests time out, and auction win rates drop. 

 Traditional Kubernetes automatic scaling was designed for workloads where a few minutes of provisioning lag is acceptable. It works through a chain of intermediaries: metrics server detects pod resource pressure, Cluster Autoscaler identifies unschedulable pods, Auto Scaling group requests a new instance, the instance boots and registers with the cluster, and kubelet starts the pod. Each handoff adds latency. The traffic spike has already peaked and subsided before new nodes are ready. 

 Instead of going through Auto Scaling groups, Karpenter calls EC2 APIs directly. At scheduling time, Karpenter selects each instance's type and size from the full EC2 catalog based on the resource requirements of pending pods. This bins pods onto right-sized nodes and reduces wasted capacity. 

 Scaling on CPU utilization is a lagging signal. By the time CPU pressure appears, bid queues are already building. KEDA addresses this by extending Kubernetes HPA to external event sources (Kinesis stream depth, SQS queue length, and custom Prometheus metrics) that reflect actual auction load before it translates into CPU. A workload that scales on CPU might have a 2–3 minute lag from traffic arrival to new pods being ready, whereas a workload that scales on queue depth can begin scaling while the queue is still shallow. 

 Karpenter's flexibility depends on your workloads being instance-type agnostic. Workloads with hard affinities for specific instance types reduce the pool Karpenter can select from and increase the likelihood of Spot interruptions during burst events. Pre-warming with placeholder pods trades cost for latency: deeper pre-warming reduces first-response latency but increases idle infrastructure spend. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Deploy Karpenter for fast, direct node provisioning on [Amazon EKS](https://aws.amazon.com/eks/):** Install Karpenter in your EKS cluster and create NodePool resources that define instance type preferences, availability zone requirements, and resource constraints for your advertising workloads. Configure NodePool with multiple instance type options (both Graviton and x86 variants of the same family) to maximize Spot Instance availability during burst events when capacity in a single instance pool may be constrained. 

1.  **Maintain pre-warmed nodes using pod priority to reduce cold-start latency:** Create low-priority placeholder pods (using PriorityClass with a negative priority value) that occupy a small number of nodes during normal operation. When real advertising workload demand spikes, Karpenter evicts placeholder pods and immediately schedules actual workload pods on the now-available nodes. New nodes for the evicted placeholder pods provision in parallel, maintaining the pre-warmed pool. 

1.  **Integrate Karpenter with Horizontal Pod Autoscaler for proactive scaling:** Configure HPA for each advertising service to scale pod count based on CPU utilization (target 65%) and custom metrics from KEDA. When HPA increases pod count and existing nodes are full, Karpenter automatically provisions new nodes without manual intervention. Verify that Karpenter's NodePool resource constraints (minimum and maximum node counts) are consistent with your HPA scaling range. 

1.  **Deploy KEDA for advertising-specific scaling signals:** Install KEDA and configure ScaledObjects that drive HPA scaling from external event sources. For bid request processing services, scale based on the length of the SQS queue or depth of the Kinesis stream receiving bid events. For auction services, scale based on custom Prometheus metrics representing auction throughput. These leading-indicator metrics scale pods ahead of CPU pressure, reducing the lag between traffic increase and scaling response. 

1.  **Use parallel node provisioning for sudden demand spikes:** Configure Karpenter's batch provisioning settings to provision multiple nodes in parallel when many pods are pending simultaneously (as occurs during a sudden traffic spike from a live event). Monitor Karpenter's node provisioning duration and the time from pod pending to pod running. Set a target of under 60 seconds for this total provisioning time and alert when it exceeds the threshold. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVPERF02-BP02 Consider containerization for scalability, low latency, and cost optimization](advperf02-bp02.md) 
+  [ADVPERF01-BP02 Use appropriate scaling to handle burst traffic with cost considerations](advperf01-bp02.md) 

 **Related documents:** 
+  [Manage scale-to-zero scenarios with Karpenter and Serverless](https://aws.amazon.com/blogs/containers/manage-scale-to-zero-scenarios-with-karpenter-and-serverless/) 
+  [Scalable and Cost-Effective Event-Driven Workloads with KEDA and Karpenter on Amazon EKS](https://aws.amazon.com/blogs/containers/scalable-and-cost-effective-event-driven-workloads-with-keda-and-karpenter-on-amazon-eks/) 
+  [Optimizing your Kubernetes compute costs with Karpenter consolidation](https://aws.amazon.com/blogs/containers/optimizing-your-kubernetes-compute-costs-with-karpenter-consolidation/) 

 **Related services:** 
+  [Amazon Elastic Kubernetes Service](https://aws.amazon.com/eks/) 
+  [Karpenter](https://karpenter.sh/) 