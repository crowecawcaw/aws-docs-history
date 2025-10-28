# ADVPERF04-BP02 Consider purpose-built and streaming databases

Purpose-built databases offer low latency and can better meet the
scaling needs of advertising workloads.

## Implementation guidance

Implement low-latency databases with in-memory AWS services
(like [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") or Apache Cassandra) or ISV products specialized
for adtech (like Aerospike). 

Implement medium latency data stores with an OLTP database like
[Amazon Aurora Global Database](https://aws.amazon.com/rds/aurora/global-database/ "https://aws.amazon.com/rds/aurora/global-database/") to implement a multi-Region
availability design. 

## Resources

- [Running
  Ad Tech Workloads on AWS with Aerospike at Petabyte Scale](https://aws.amazon.com/blogs/industries/running-ad-tech-workloads-on-aws-with-aerospike-at-petabyte-scale/ "https://aws.amazon.com/blogs/industries/running-ad-tech-workloads-on-aws-with-aerospike-at-petabyte-scale/")
- [Use
  Amazon Aurora Global Database to build resilient multi-Region applications](https://aws.amazon.com/blogs/database/use-amazon-aurora-global-database-to-build-resilient-multi-region-applications/ "https://aws.amazon.com/blogs/database/use-amazon-aurora-global-database-to-build-resilient-multi-region-applications/")
