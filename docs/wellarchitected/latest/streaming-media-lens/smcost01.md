

# Storage and delivery costs
<a name="smcost01"></a>

Storage and data transfer often represent the largest cost components. A strategy for lifecycle management and edge caching reduces these costs while maintaining access performance.


| SMCOST01: How do you optimize storage and data transfer costs for your streaming media workload? | 
| --- | 
| [SMCOST01-BP01 Implement lifecycle management for media assets](smcost01-bp01.md) | 
| [SMCOST01-BP02 Optimize content delivery using edge caching and just-in-time packaging](smcost01-bp02.md) | 

## Capability intent
<a name="smcost01-intent"></a>
+ Assets are stored in the most cost-effective tier based on measured access patterns.
+ Edge caching reduces origin requests and data transfer volume.
+ Just-in-time packaging removes the need for pre-packaged format variants for content that doesn't justify them.
+ Lifecycle policies vary by content type rather than applying a single retention rule uniformly.

## Common issues to watch for
<a name="smcost01-issues"></a>
+ A single storage class for all assets regardless of access frequency.
+ Serving all requests from origin without edge caching.
+ Pre-packaging every format variant for content that is rarely watched.
+ Uniform retention policies that keep low-value assets as long as high-value ones.