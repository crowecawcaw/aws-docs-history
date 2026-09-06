

# Performance considerations
<a name="transitive-matching-performance"></a>

Transitive matching workflows are slower than non-transitive workflows because records are processed across all rule levels instead of being excluded after their first match. The following factors affect performance:

Rule count  
More rules result in more processing time. Each additional rule level adds merge iterations because the system must propagate match IDs across all levels.

Batch and incremental processing  
Incremental workflows have higher overhead than batch workflows at scale. Larger base record stores require more merge iterations to propagate match IDs across existing and new records.

Data skew  
Datasets with skewed distributions, such as large match groups, amplify overhead. When many records link to the same match group, the system requires more transitive linking operations to resolve all connections.

We recommend that you test transitive matching workflows with representative data volumes before using them in production. This helps you understand the performance characteristics for your specific data and rule configuration.