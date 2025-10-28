# Choosing the appropriate configuration

Within the console experience, ElastiCache offers an easy way to choose the right instance type based on the memory and cpu requirements of your vector workload.

## Memory consumption

Memory consumption is based on the number of vectors, the number of dimensions, the M-value, and the amount of non-vector data, such as metadata associated to the vector or other data stored within the instance. The total memory required is a combination of the space needed for the actual vector data, and the space required for the vector indices. The space required for Vector data is calculated by measuring the actual capacity required for storing vectors within `HASH` or `JSON` data structures and the overhead to the nearest memory slabs, for optimal memory allocations. Each of the vector indexes uses references to the vector data stored in these data structures as well as an additional copy of the vector in the index. It is advised to plan for this additional space consumption by the index.

The number of vectors depend on how you decide to represent your data as vectors. For instance, you can choose to represent a single document into several chunks, where each chunk represents a vector. Alternatively, you could choose to represent the whole document as a single vector. The number of dimensions of your vectors is dependent on the embedding model you choose. For instance, if you choose to use the AWS Titan embedding model then the number of dimensions would be 1536. Note that you should test the instance type to make sure it fits your requirements.

## Scaling your workload

Vector search supports all three methods of scaling: horizontal, vertical and replicas. When scaling for capacity, vector search behaves just like regular Valkey, i.e., increasing the memory of individual nodes (vertical scaling) or increasing the number of nodes (horizontal scaling) will increase the overall capacity. In cluster mode, the `FT.CREATE` command can be sent to any primary node of the cluster and the system will automatically distribute the new index definition to all cluster members.

However, from a performance perspective, vector search behaves very differently from regular Valkey. The multi-threaded implementation of vector search means that additional CPUs yield up to linear increases in both query and ingestion throughput. Horizontal scaling yields linear increases in ingestion throughput but may reduce query throughput. If additional query throughput is required, scaling through replicas or additional CPUs is required.
