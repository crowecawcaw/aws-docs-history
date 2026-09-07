

# SCCOST02-BP02 Query and retrieve data by partitions to save cost and improve performance
<a name="sccost02-bp02"></a>

 Optimize data access by using partitioned queries to enhance cost-efficiency and performance in supply chain systems. 

 **Desired outcome:** Data access requirements are taken into consideration while defining data storage strategy.  

 **Benefits of establishing this best practice:** Reduced cost, optimized performance, and better customer satisfaction 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance-49"></a>

 Organize supply chain data by time, geography, or other relevant criteria to enhance storage efficiency and reduce retrieval costs. 

 Implement data partitioning strategies to divide large volumes into manageable chunks based on specific characteristics like time or product ID, focusing query operations on relevant segments and reducing scanned data volume and associated costs. 

### Implementation steps
<a name="implementation-steps-50"></a>

1.  Analyze supply chain data access patterns to identify optimal partitioning strategies based on time, geography, or product categories. 

1.  Implement data partitioning in storage systems to organize data into logical segments that align with query patterns. 

1.  Configure query engines to use partition pruning to scan only relevant data segments during retrieval operations. 

1.  Use AWS Glue for automated data partitioning and Amazon S3's integrated compression options to further reduce costs. 

1.  Implement partition management processes to maintain optimal partition sizes and help prevent partition proliferation. 

1.  Monitor query performance and costs to continuously optimize partitioning strategies and data organization. 