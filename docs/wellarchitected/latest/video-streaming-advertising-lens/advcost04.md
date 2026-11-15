

# Data storage and collaboration cost
<a name="advcost04"></a>

 User profile databases tend to be large, holding anywhere from 100-200 million to 5 billion user profiles, and they contain a wide range of data about users' online activities and interactions. Storing and accessing this data can increase cost substantially. How you store, cache, and replicate user profile data directly affects the largest database cost components in RTB architectures. Privacy-enhanced collaboration adds another cost dimension. Collaborative analytics environments price queries by bytes scanned, so data format, partitioning strategy, and query patterns have a direct and multiplicative effect on spend. 


|  ADVCOST04: How do you optimize the cost of database storage and access for your advertising user profile and campaign data?  | 
| --- | 
| [ADVCOST04-BP01 Consider lower-cost storage for older user profile data](advcost04-bp01.md) | 
| [ADVCOST04-BP02 Consider multi-level caching for user profile data](advcost04-bp02.md) | 
| [ADVCOST04-BP03 Store profiles in a single Region and replicate asynchronously](advcost04-bp03.md) | 
| [ADVCOST04-BP04 Use cost-efficient data types and configurations for collaborative data environments](advcost04-bp04.md) | 

## Capability intent
<a name="advcost04-capability-intent"></a>
+  User profile data uses cost-optimized storage tiers: high-performance storage for the most recent 30 days, progressively lower-cost storage for older data. 
+  Multi-level caching (DynamoDB Accelerator, ElastiCache) reduces read capacity unit consumption and database query costs for frequently accessed profiles. 
+  User profile data is stored in a single primary region and replicated asynchronously to secondary regions on a scheduled basis, minimizing cross-region data transfer costs. 
+  Datasets shared in collaborative analytics environments use compressed columnar formats with logical partitioning that allows query engines to scan only relevant data. 
+  AWS Clean Rooms collaborations are configured within the same Region to avoid inter-region transfer costs. 
+  Queries use partition pruning and avoid full table scans, minimizing bytes scanned in scan-based pricing models. 

## Common issues to watch for
<a name="advcost04-common-issues-to-watch-for"></a>
+  Retaining user profile data in DynamoDB indefinitely, paying provisioned or on-demand pricing for data that is rarely queried during bid evaluation. 
+  Enabling real-time cross-region replication for user profiles when users are rarely in two geographic locations simultaneously, incurring ongoing replication costs without corresponding benefit. 
+  Storing shared datasets in row-oriented formats (CSV, JSON) that force query engines to scan entire files regardless of which columns are needed. 
+  Configuring AWS Clean Rooms collaborations across regions when all participants have data in the same Region, incurring unnecessary inter-region transfer costs. 