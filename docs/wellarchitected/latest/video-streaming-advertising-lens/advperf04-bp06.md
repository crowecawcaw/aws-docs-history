

# ADVPERF04-BP06 Optimize privacy-enhanced collaboration queries for performance and service limits

 [AWS Clean Rooms](https://aws.amazon.com/clean-rooms/) has query result size limits (for example, a 5 GB limit) and query performance that depends on data design. Use partitioning, aggregations, and filters to optimize queries, and account for the processing overhead of cryptographic operations. 

 **Desired outcome:** 
+  Your AWS Clean Rooms collaborations return results within acceptable time bounds with query designs that stay within service limits. 
+  Data is partitioned for efficient processing, and cryptographic operation choices are made with their performance implications in mind. 
+  Analysis templates are pre-optimized for execution efficiency before being templatized for reuse. 

 **Common anti-patterns:** 
+  Running unoptimized, broad queries against large unpartitioned datasets in AWS Clean Rooms without aggregations or filters, hitting the 5 GB result size limit and generating long query processing times. 
+  Designing collaboration frameworks with a large number of collaborators without accounting for the processing overhead each additional participant introduces. 

 **Benefits of establishing this best practice:** 
+  Well-designed Clean Rooms queries return results faster, stay within service limits, and reduce the compute overhead of each collaboration run. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 The 5 GB result size limit is a privacy boundary that restricts raw data extraction. You cannot provision more compute to work around it, so queries must return aggregated outputs. Query execution time is a separate constraint that scales with data volume scanned, number of collaborators, and the cryptographic mode selected. A query within the 5 GB limit can still be slow if it scans unpartitioned data across many participants. 

 Use standard SQL-based analysis in Clean Rooms by default. In standard mode, one party controls the matching logic and sees the analysis results. Promote to cryptographic computing with C3 (Clean Rooms Collaboration with Cryptographic Computing) when neither party may see the other's raw matched records. C3 operations on large datasets can take orders of magnitude longer than equivalent standard Clean Rooms queries. 

 Collaborator topology has a non-linear performance impact. Matching and aggregation logic runs across all participants at once, which drives the cost of a Clean Rooms collaboration. Moving from 5 to 10 collaborators can increase processing time by a factor of 3–5 depending on the query structure and cryptographic mode. Decompose large industry measurement panels (10\+ participants) into paired or small-group collaborations that aggregate their results externally. Reserve full multi-party Clean Rooms queries for cases where joint matching across all parties is required. 

 Analysis templates lock in execution patterns after the collaboration is live. A template that passes functional testing on small datasets can still run slowly at production scale. Once templated, that behavior repeats on every collaboration execution. Benchmark and optimize queries against production-scale data before creating a template. Changing a live template requires renegotiating the collaboration framework with all participants. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Apply aggregations and filters to keep query result sets under 5 GB:** Design queries to return aggregated outputs (audience counts, overlap percentages, segment performance summaries) rather than row-level detail. Apply filters early in the WHERE clause to reduce the dataset scanned. Use minimum aggregation thresholds to limit individual-level data extraction while maintaining statistical utility. 

1.  **Partition datasets on commonly queried dimensions:** Convert shared datasets to Apache Parquet with partitioning on the dimensions most commonly used in collaboration queries (date, campaign ID, audience segment ID, region). Use [AWS Glue](https://aws.amazon.com/glue/) to create partitioned datasets and register them in the Clean Rooms data catalog. Verify that query plans use partition pruning by checking that query execution times decrease proportionally with tighter filter ranges. 

1.  **Consider collaborator count in your collaboration framework design:** Before finalizing a collaboration architecture, model the processing time implications of your target collaborator count under representative query loads. For collaborations with more than 10 participants, evaluate whether the collaboration can be structured as smaller, focused sub-collaborations (publisher-advertiser pairs rather than one-to-many) that run faster and return results within tighter time bounds. 

1.  **Optimize queries before converting them into analysis templates:** Run each query against representative production-scale data volumes and measure execution time before creating an analysis template. Optimize for execution efficiency (remove unnecessary joins, push filters early, validate partition pruning) before templatizing. Once templated, queries run with the same structure on every collaboration execution. Any inefficiency is locked in and repeated. 

1.  **Select cryptographic operations with processing overhead in mind:** AWS Clean Rooms offers multiple cryptographic computing options. Each option adds processing overhead proportional to the complexity of the operation and the size of the dataset. Evaluate the processing time cost of your chosen approach against your collaboration latency requirements and select the option that provides the privacy guarantee you need without adding more processing overhead than your use case requires. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [AWS Clean Rooms proof of concept: media measurement](https://aws.amazon.com/blogs/big-data/aws-clean-rooms-proof-of-concept-scoping-part-1-media-measurement/) 
+  [Data formats for AWS Clean Rooms](https://docs.aws.amazon.com/clean-rooms/latest/userguide/data-formats.html) 

 **Related services:** 
+  [AWS Clean Rooms](https://aws.amazon.com/clean-rooms/) 