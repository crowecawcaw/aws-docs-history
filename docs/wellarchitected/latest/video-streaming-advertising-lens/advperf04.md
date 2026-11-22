

# Data management design

 Advertising workloads have different data classification, availability, and access latency needs based on their subsystems. Implement a strategy to identify an appropriate AWS data store service option, along with scaling and monitoring considerations. The optimal data management solution for a particular system varies based on data type, access patterns, required throughput, frequency of access, frequency of update, and availability and durability constraints. 


|  ADVPERF04: How do you design your data management strategy to meet the latency, availability, and cost requirements of your workload?  | 
| --- | 
| [ADVPERF04-BP01 Choose a data management strategy that matches your availability, latency, and access requirements](advperf04-bp01.md) | 
| [ADVPERF04-BP02 Consider purpose-built databases for advertising workloads](advperf04-bp02.md) | 
| [ADVPERF04-BP03 Review your distributed database setup (sharding and replication) for performance, cost, and availability needs](advperf04-bp03.md) | 
| [ADVPERF04-BP04 Enable detailed performance and observability monitoring to tune queries and refine compute and storage](advperf04-bp04.md) | 
| [ADVPERF04-BP05 Manage high-volume user profile data](advperf04-bp05.md) | 
| [ADVPERF04-BP06 Optimize privacy-enhanced collaboration queries for performance and service limits](advperf04-bp06.md) | 

## Capability intent
<a name="advperf04-capability-intent"></a>
+  Every datastore in your advertising stack is selected based on a clear understanding of the latency tier, availability requirements, and access patterns of the data it holds. 
+  Real-time bid data, audience segmentation data, and historical reporting data each land in a service optimized for their specific characteristics. 
+  Your distributed database setup (sharding and replication) is designed for your performance, cost, and availability needs, not applied uniformly regardless of data category. 
+  You have detailed performance and observability monitoring configured to tune queries and refine compute and storage allocation. 
+  User profile data is managed with retention policies and geographic placement that bound storage costs while maintaining bid path performance. 
+  [AWS Clean Rooms](https://aws.amazon.com/clean-rooms/) query performance is optimized through data partitioning, aggregation, and filtering before query execution. 

## Common issues to watch for
<a name="advperf04-common-issues-to-watch-for"></a>
+  Using a single database technology across all advertising data categories regardless of their latency profile, forcing low-latency real-time bidding data and high-latency historical reporting data to compete for the same storage resources. 
+  Storing all historical user profile data indefinitely in DynamoDB, paying provisioned or on-demand pricing for data that is rarely queried during bid evaluation. 
+  Replicating user profile data across multiple regions in real time, incurring high cross-region transfer costs for data that is almost never accessed from more than one Region simultaneously. 
+  Deploying bidder nodes and database nodes in different Availability Zones without Availability Zone-aware routing, paying cross-AZ data transfer charges on every database query from the bid path. 
+  Running Clean Rooms queries against large unpartitioned datasets without aggregations or filters, hitting the 5 GB result size limit and generating long query processing times. 