

# Cost-effective resources

 Cost optimization means providing the performance a workload requires at the lowest possible price point, not just reducing spend. For advertising workloads, this means using ARM processors for faster and more cost-effective bidder nodes, compression to reduce network traffic and storage costs, provisioned capacity for predictable workloads, and Spot Instances for fault-tolerant bidding-as-a-service workloads. 


|  ADVCOST02: How do you select and configure cost-effective compute, storage, and network resources for your advertising workloads?  | 
| --- | 
| [ADVCOST02-BP01 Use ARM processors for faster and more cost-effective bidder nodes](advcost02-bp01.md) | 
| [ADVCOST02-BP02 Use compression to reduce network traffic and storage costs](advcost02-bp02.md) | 
| [ADVCOST02-BP03 Use provisioned resource allocation for campaigns with predictable capacity, and use dynamic allocation for unexpected capacity](advcost02-bp03.md) | 
| [ADVCOST02-BP04 Use interruptible spare capacity to reduce compute cost for fault-tolerant bidding workloads](advcost02-bp04.md) | 

## Capability intent
<a name="advcost02-capability-intent"></a>
+  AWS Graviton-based instances are used for eligible RTB workloads, delivering up to 40% better price-performance over comparable x86 instances. 
+  Compression is applied across API responses, log storage, message queues, and data lake ingestion to measurably reduce data transfer and storage costs. 
+  Provisioned capacity is used for predictable workloads and on-demand or serverless for variable workloads, not a one-size-fits-all approach. 
+  Spot Instances are used for interruptible RTB workloads (batch analytics, model training) with proper fault-tolerance mechanisms. 

## Common issues to watch for
<a name="advcost02-common-issues-to-watch-for"></a>
+  Defaulting to x86 On-Demand instances for all RTB workloads without evaluating Graviton alternatives. 
+  Storing all advertising data in uncompressed formats, inflating both storage costs and data transfer costs between services. 
+  Using On-Demand capacity for all workloads regardless of traffic pattern, both over-spending on predictable workloads (should use provisioned) and under-spending on unpredictable workloads (should use serverless). 