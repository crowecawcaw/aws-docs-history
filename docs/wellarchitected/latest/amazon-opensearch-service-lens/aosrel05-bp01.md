

# AOSREL05-BP01 Implement appropriate compute sizing for production workloads
<a name="aosrel05-bp01"></a>

 Improve OpenSearch Service domain performance by implementing compute sizing that meets production workload requirements. This practice helps you avoid CPU throttling due to depleted burst credits and minimize risks. 

 **Level of risk exposed if this best practice is not established:** Medium 

 **Desired outcome**: Your OpenSearch Service domain is running on instance families that meet the required performance and resource needs. 

 **Benefits of establishing this best practice:** 
+  Avoid CPU throttling if burst credits are depleted 
+  Improve your ability to maintain performance and minimize risks 

## Implementation guidance
<a name="implementation-guidance-28"></a>

 Avoid using t2 or t3.small instances for production domains, as they can become unstable under sustained heavy load. t3.medium instances are an option for small production workloads (both as data nodes and as dedicated leader nodes). 

## Resources
<a name="resources-26"></a>
+  [Operational best practices for Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/bp.html#bp-cost-optimization-instances) 