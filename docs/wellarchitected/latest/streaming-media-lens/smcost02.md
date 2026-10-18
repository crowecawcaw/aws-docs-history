

# Content processing costs
<a name="smcost02"></a>

Processing costs scale with encoding volume, instance selection, and utilization efficiency. Baseline measurement, parallel processing, and capacity reservations are the main ways to reduce them.


| SMCOST02: How do you optimize content processing costs for your streaming media workload? | 
| --- | 
| [SMCOST02-BP01 Establish baseline metrics for media processing tasks](smcost02-bp01.md) | 
| [SMCOST02-BP02 Implement parallel processing for media tasks](smcost02-bp02.md) | 
| [SMCOST02-BP03 Optimize AWS Elemental Media Services pricing models](smcost02-bp03.md) | 

## Capability intent
<a name="smcost02-intent"></a>
+ Processing resource requirements are baselined and tracked rather than provisioned on assumption.
+ Batch processing uses parallel execution and spot capacity where interruption tolerance allows.
+ Consistent live encoding workloads use reservations rather than on-demand pricing.
+ Instance types are benchmarked against actual workloads rather than selected by default.

## Common issues to watch for
<a name="smcost02-issues"></a>
+ No real-time-factor or utilization tracking for processing tasks.
+ Sequential processing of large files on a single instance when parallel execution is possible.
+ Persistent channels at on-demand rates without evaluating reservation options.
+ Same instance type used for all tasks without benchmarking alternatives.