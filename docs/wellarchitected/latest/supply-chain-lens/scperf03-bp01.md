# SCPERF03-BP01 Select your database architecture based on workload

Purpose-built data storage for your workloads can help increase
the performance efficiency of the overall system, as well to be
more resilient in case of failures.

**Desired outcome:** Purpose-built
data storage. Increased performance efficiency of the overall
system.

**Benefits of establishing this best
practice:** Scalability, resilience, and end user
performance improvement.

**Level of risk exposed if this best
practice is not established:** High.

## Implementation guidance

Select database options that align with your performance
requirements, using different database technologies for
different purposes, such as Amazon Timestream time-series
database for storing ticking market data, rather than a
one-size-fits-all use of traditional relational databases. Also,
Amazon RDS is a straightforward relational database service
optimized for total cost of ownership. It is simple to set up,
operate, and scale with demand. Amazon RDS automates the
undifferentiated database management tasks, such as
provisioning, configuring, backups, and patching.

### Implementation steps

1. Analyze supply chain data access patterns and performance
   requirements to determine optimal database architectures.
2. Implement purpose-built databases for specific use cases,
   such as time-series databases for IoT sensor data and
   document databases for product catalogs.
3. Configure Amazon RDS for transactional supply chain data
   that requires ACID compliance and complex queries.
4. Deploy NoSQL databases like Amazon DynamoDB for
   high-throughput, low-latency applications such as
   inventory tracking.
5. Establish database performance monitoring and optimization
   processes to maintain continued efficiency as data volumes
   grow.
6. Implement automated backup and disaster recovery
   strategies to maintain data availability and business
   continuity.
