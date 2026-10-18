

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

## Common issues to watch for
<a name="smsus07-issues"></a>
+ Running on older instance families when a more efficient option exists with no functional change.
+ Self-managed transcoding on general-purpose compute instead of purpose-built media services.
+ Over-allocating GPUs to tasks that don't need them.
+ No tracking of compute hours by instance family.