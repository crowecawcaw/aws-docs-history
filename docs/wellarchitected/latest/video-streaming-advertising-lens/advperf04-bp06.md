

# ADVPERF04-BP06 Consider AWS Clean Rooms collaboration
<a name="advperf04-bp06"></a>

 AWS Clean Rooms have limits on query result size (for example, AWS Clean Rooms has a 5GB limit), so consider using aggregations and filters to reduce result sets. 

## Implementation guidance
<a name="ig-advperf04-bp06"></a>

 Large datasets can impact query performance. Partition data effectively. 

 A higher number of collaborators in a collaboration channel impacts processing time. Consider this as one of the factors for designing the collaboration framework with collaborators in play. 

AWS Clean Rooms offers analysis templates work to support parameterized queries assisting in performance improvement through query reuse. Optimize queries before creating templates. Consider the choice of cryptographic operations for secure computation, as it adds to processing time.

## Key AWS services
<a name="key-aws-services-38"></a>
+ AWS Clean Rooms

## Resources
<a name="resources-57"></a>
+  [Guidelines for the C3R encryption client](https://docs.aws.amazon.com/clean-rooms/latest/userguide/crypto-computing-guidelines.html) 