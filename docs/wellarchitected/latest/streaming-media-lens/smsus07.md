

# Efficient hardware
<a name="smsus07"></a>

The processor family and accelerator you select directly determine how much energy a given amount of work consumes.


| SMSUS07: How do you select and use hardware for sustainable streaming operations? | 
| --- | 
| [SMSUS07-BP01 use energy-efficient computing resources](smsus07-bp01.md) | 

## Capability intent
<a name="smsus07-intent"></a>
+ Workloads run on the most efficient processor family that supports them.
+ Specialized tasks use purpose-built hardware rather than general-purpose compute.
+ Interruption-tolerant batch draws from spare capacity rather than dedicated instances.
+ Hardware choices are revisited as more efficient generations become available.

## Maturity levels
<a name="smsus07-maturity"></a>


| Level | Name | What it looks like | 
| --- | --- | --- | 
| 1 | Initial | Default or legacy instance families used without review. General-purpose compute for all tasks including media processing and ML. | 
| 2 | Emerging | Some workloads validated on newer processor families. Purpose-built media services adopted for new projects but legacy self-managed encoding remains. | 
| 3 | Defined | Eligible workloads run on efficient processors. Purpose-built accelerators handle ML inference and training. GPUs are right-sized to tasks that need them. | 
| 4 | Proactive | Interruption-tolerant batch runs on spot capacity. Compute hours are tracked by instance family. New processor generations are evaluated as they ship. | 
| 5 | Optimized | Hardware selection is revisited on a regular cadence. The share of work on efficient hardware trends upward continuously. | 

## Common issues to watch for
<a name="smsus07-issues"></a>
+ Running on older instance families when a more efficient option exists with no functional change.
+ Self-managed transcoding on general-purpose compute instead of purpose-built media services.
+ Over-allocating GPUs to tasks that don't need them.
+ No tracking of compute hours by instance family.