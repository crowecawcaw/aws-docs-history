

# ADVCOST04-BP04 Use cost-efficient data types and configurations for collaborative data environments

 Use efficient storage formats and query patterns to reduce data scanning, duplication, and transfer costs in collaborative analytics environments for advertising measurement and audience analysis. 

 **Desired outcome:** 
+  Datasets shared in collaborative analytics environments use compressed columnar formats with logical partitioning that allows query engines to scan only relevant data. 
+  Queries use partition pruning and avoid full table scans, minimizing bytes scanned and associated query costs. 
+  Collaborations are configured within the same Region to avoid inter-region transfer costs. 

 **Common anti-patterns:** 
+  Storing shared datasets in row-oriented formats (CSV, JSON) that force query engines to scan entire files regardless of which columns are needed. 
+  Running queries with SELECT \* patterns or cross-joins that scan and transfer far more data than the analysis requires. 
+  Configuring AWS Clean Rooms collaborations across regions when all participants have data in the same Region. 

 **Benefits of establishing this best practice:** 
+  Reduced per-query costs in scan-based pricing models (Athena, Clean Rooms) by minimizing bytes scanned. 
+  Lower storage costs from compressed columnar formats compared to raw text formats. 
+  Elimination of inter-region data transfer charges for collaborative workloads. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Collaborative analytics environments price queries by bytes scanned. Under that model, your data format, partitioning strategy, and query patterns multiply what you spend. When five collaboration members query one poorly structured dataset, each query scans the same inefficient layout, and the cost compounds across the group. 

 Columnar formats (Parquet, ORC) store data by column, so a query engine reads only the columns a query references. Row-oriented formats like CSV or JSON force a full-file scan regardless of the columns needed. A 500 GB dataset queried for three columns out of fifty scans roughly 30 GB in Parquet against the full 500 GB in CSV, and the savings widen as datasets grow. Compression (Snappy for speed, ZSTD for ratio) shrinks the bytes the engine reads. 

 Partitioning further reduces scans by organizing data into path segments that the query engine can prune before reading. The best partition keys match the WHERE clause predicates your workload uses most often. Over-partitioning can backfire when too many small files raise metadata overhead and reduce compression efficiency. Daily date partitions work for most advertising measurement workloads. Adding a second key such as campaign or region pays off only when queries consistently filter on that dimension. 

 [AWS Clean Rooms](https://docs.aws.amazon.com/clean-rooms/latest/userguide/what-is.html) charges per query based on the bytes scanned from configured tables. Cross-Region data transfer adds a charge on every query, and that charge appears on the data owner's bill, not the querying member's. Store contributed tables in the same Region as the collaboration. 

 Analysis rules in Clean Rooms control which query patterns members can run. Without them, a collaborator can run SELECT \* or broad cross-joins that scan entire datasets. Well-chosen rules limit data exposure and cap scan costs. Overly restrictive rules push members to run several narrow queries to answer one business question, which can scan more than a single well-structured query would. To define good rules, understand both the questions members want to answer and how much each query shape costs to run. 

 If you skip format conversion during onboarding, you might notice a cost problem only after the collaboration is live and several members have built analysis templates against the raw layout. Fixing the format then means re-registering tables, updating those templates, and coordinating across organizations. Converting data before you share it into a collaboration avoids that coordination. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Convert shared datasets to Parquet or ORC with compression:** Use AWS Glue ETL jobs to convert existing CSV or JSON advertising datasets to Parquet with Snappy compression. Schedule weekly conversion jobs for incrementally arriving data. Verify compression ratios: target 5-10x reduction compared to raw JSON, which directly reduces Athena scan costs. 

1.  **Implement logical partitioning by common query filter dimensions:** Partition advertising collaboration datasets by year=YYYY/month=MM/day=DD/campaign\_id=XXX. Add partition keys to AWS Glue Data Catalog. Validate that Athena queries use partition pruning (check the execution plan shows partition filters applied before data scan). 

1.  **Configure Clean Rooms collaborations within the same Region:** Before creating Clean Rooms collaborations, verify that all participant datasets are stored in the same AWS Region. Document the Region requirement in collaboration onboarding processes. Use the Clean Rooms console to confirm all data sources resolve to the same Region. 

1.  **Optimize queries before converting them to analysis templates:** Run each candidate query against representative production-scale data. Measure execution time and bytes scanned. Optimize to reduce scan volume (add partition filters, remove unused columns, replace SELECT \* with explicit column lists). Only templatize queries that have been validated for cost efficiency. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVCOST04-BP01 Consider lower-cost storage for older user profile data](advcost04-bp01.md) 

 **Related documents:** 
+  [Data formats for AWS Clean Rooms](https://docs.aws.amazon.com/clean-rooms/latest/userguide/data-formats.html) 
+  [Data Analytics Lens](https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-10.4---partition-your-data-to-avoid-unnecessary-file-reads.html) 

 **Related services:** 
+  [AWS Clean Rooms](https://aws.amazon.com/clean-rooms/) 
+  [AWS Glue](https://aws.amazon.com/glue/) 
+  [Amazon Athena](https://aws.amazon.com/athena/) 