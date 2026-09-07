

# ADVPERF04-BP02 Consider purpose-built and streaming databases
<a name="advperf04-bp02"></a>

 Purpose-built databases offer low latency and can better meet the scaling needs of advertising workloads. 

## Implementation guidance
<a name="implementation-guidance-48"></a>

 Implement low-latency databases with in-memory AWS services (like [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) or Apache Cassandra) or ISV products specialized for adtech (like Aerospike).  

 Implement medium latency data stores with an OLTP database like [Amazon Aurora Global Database](https://aws.amazon.com/rds/aurora/global-database/) to implement a multi-Region availability design.  

## Resources
<a name="resources-43"></a>
+  [Running Ad Tech Workloads on AWS with Aerospike at Petabyte Scale](https://aws.amazon.com/blogs/industries/running-ad-tech-workloads-on-aws-with-aerospike-at-petabyte-scale/) 
+  [Use Amazon Aurora Global Database to build resilient multi-Region applications](https://aws.amazon.com/blogs/database/use-amazon-aurora-global-database-to-build-resilient-multi-region-applications/) 