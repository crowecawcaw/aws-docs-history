

# Best practices for metadata filtering in GraphRAG
<a name="best-practices-graphrag-filters"></a>

 When using Neptune Analytics as the vector store for an Amazon Bedrock Knowledge Base with GraphRAG, you can apply metadata filters during retrieval to narrow down the set of candidate nodes. Choosing the right filter type and structure can have a significant impact on query latency. This page provides guidance on how to use metadata filters effectively. 

 For general information on configuring metadata filters in Amazon Bedrock Knowledge Bases, see [Configure and customize queries and response generation](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html). For details on the `vertexFilter` parameter used by the underlying Neptune Analytics vector search algorithm, see [ .vectors.topK.byEmbedding algorithm](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/vectors.topK.byEmbedding.html). 

## Design metadata attributes for efficient filtering
<a name="best-practices-graphrag-filters-metadata"></a>

 The most effective way to improve filter performance is to design your document metadata with filtering in mind from the start. Neptune Analytics supports String, Number, and Boolean metadata property types. Properties with list values are not supported as document metadata attributes, though `in`/`notIn` filters accept a list of candidate values to match against. Consider the following guidelines: 
+  **Use categorical properties.** Instead of relying on string prefix matching to categorize documents, add explicit categorical metadata attributes (for example, `document_type`, `department`, `region`) that can be filtered with `equals` or `in`. 
+  **Use numeric properties for time-based filtering.** Store timestamps as numeric epoch values so you can use efficient range filters (`greaterThan`, `lessThan`) instead of string-based date comparisons. 
  + Neptune Analytics stores all numeric metadata values as Double internally. Integer values such as `2024` are automatically converted to Double (for example, `2024.0`) during ingestion. This conversion is handled transparently and does not require any changes to your filter queries.
+  **Avoid encoding hierarchy in a single string property.** If your documents have a hierarchical structure (for example, `org/team/project`), break it into separate metadata attributes (`org`, `team`, `project`) rather than using `startsWith` on a path string. 
+  **Keep filter value lists small.** When using `in` or `notIn`, keep the value list reasonably small. Very large lists increase the time needed to check each candidate node against the filter, which adds latency to the overall vector search. 

## Choose the right filter type
<a name="best-practices-graphrag-filters-choose"></a>

 Not all filter types perform equally. The filter type you choose directly affects how Neptune Analytics evaluates candidate nodes during vector search. The following table summarizes the relative performance characteristics of each filter type: 


| Filter type | Supported types | Relative performance | Notes | 
| --- | --- | --- | --- | 
| equals | String, Number, Boolean | Fast | Direct value comparison. Preferred for exact-match filtering on properties or labels. | 
| notEquals | String, Number, Boolean | Fast | Exclusion-based comparison. Similar performance to equals. | 
| in / notIn | String, Number, Boolean list | Fast | Set membership check. Efficient for filtering against a small list of known values. When using the Amazon Bedrock `Retrieve` and `RetrieveAndGenerate` APIs, only string values are supported in the list. | 
| greaterThan, lessThan, greaterThanOrEquals, lessThanOrEquals | Number | Fast | Numeric range comparisons. Efficient for filtering on numeric properties such as timestamps stored as epoch values. | 
| stringContains | String | Moderate | Substring search. Requires scanning string values. Use only when exact match is not possible. | 
| startsWith | String | Slow | Prefix matching on string properties. Can result in significantly higher latency. Avoid when possible; prefer equals or in instead. | 

 Performance can vary depending on value list size, property cardinality, and the selectivity of the filter. The ratings above reflect typical workloads. 

## Combine filters efficiently with `andAll` and `orAll`
<a name="best-practices-graphrag-filters-combine"></a>

 When combining multiple filter conditions, use `andAll` to require all conditions to be met, or `orAll` to require at least one condition. Both `andAll` and `orAll` require a minimum of two filter conditions. Compound filters using `andAll` with fast filter types (such as `equals`, `in`, and numeric range filters) perform well. 

 However, be aware that including a slow filter type (such as `startsWith`) inside an `andAll` or `orAll` group can degrade the performance of the entire filter expression. The overall latency tends to be dominated by the slowest filter in the group. 

Use:

```
{
    "retrievalConfiguration": {
        "vectorSearchConfiguration": {
            "filter": {
                "andAll": [
                    {
                        "equals": {
                            "key": "department",
                            "value": "engineering"
                        }
                    },
                    {
                        "greaterThanOrEquals": {
                            "key": "year",
                            "value": 2024
                        }
                    }
                ]
            }
        }
    }
}
```

 In this example, the filter value `2024` is compared against the stored Double value `2024.0`. No change to the query is required. The conversion is handled automatically. 

Avoid:

```
{
    "retrievalConfiguration": {
        "vectorSearchConfiguration": {
            "filter": {
                "andAll": [
                    {
                        "equals": {
                            "key": "department",
                            "value": "engineering"
                        }
                    },
                    {
                        "startsWith": {
                            "key": "file_path",
                            "value": "/docs/eng/"
                        }
                    }
                ]
            }
        }
    }
}
```

## Avoid using `startsWith` filters when possible
<a name="best-practices-graphrag-filters-startswith"></a>

 The `startsWith` filter can cause significantly higher query latency compared to other filter types. Queries using `startsWith` can experience significantly higher latency than equivalent queries using `equals` or `in`, particularly on large graphs or when the prefix has low selectivity. 

 If you are using `startsWith` to match a known set of prefix values, consider restructuring your metadata so that you can use `equals` or `in` instead. For example: 

Instead of using a `startsWith` filter like this in the Amazon Bedrock `Retrieve` or `RetrieveAndGenerate` API:

```
{
    "retrievalConfiguration": {
        "vectorSearchConfiguration": {
            "filter": {
                "startsWith": {
                    "key": "source_uri",
                    "value": "s3://my-bucket/reports/"
                }
            }
        }
    }
}
```

Add a dedicated metadata attribute (for example, `document_category`) to your documents and use an `equals` filter. Note that adding new metadata attributes requires updating your source documents and re-syncing the knowledge base for the new attributes to take effect.

```
{
    "retrievalConfiguration": {
        "vectorSearchConfiguration": {
            "filter": {
                "equals": {
                    "key": "document_category",
                    "value": "reports"
                }
            }
        }
    }
}
```

 If you must match multiple categories, use `in`: 

```
{
    "retrievalConfiguration": {
        "vectorSearchConfiguration": {
            "filter": {
                "in": {
                    "key": "document_category",
                    "value": ["reports", "summaries"]
                }
            }
        }
    }
}
```

## Scale graph capacity for filter-heavy workloads
<a name="best-practices-graphrag-filters-scaling"></a>

 If your workload relies heavily on metadata filtering, especially with string-based filters, consider increasing the number of memory-optimized Neptune Capacity Units (m-NCUs) allocated to your graph. Metadata filtering adds computational overhead to each vector search operation, and additional capacity helps maintain acceptable latency under load. 

 The number of worker threads available to process queries is determined by your graph size: specifically, m-NCU / 4. For example, a 128 m-NCU graph has 32 worker threads, while a 16 m-NCU graph has only 4. When filter-heavy retrieval requests arrive at a rate that exceeds the available worker threads, queries are queued, and the time spent waiting in the queue adds directly to the overall latency experienced by the caller. For more details on concurrency and queuing behavior, see [ Concurrency and query queuing in Neptune Analytics](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/query-concurrency-queuing.html). 

 Monitor your graph using Amazon CloudWatch metrics. In particular, a sustained non-zero value for `NumQueuedRequestsPerSec` indicates the graph is running at full capacity and may need to be scaled up. A rise in `NumThrottledRequestsPerSec` indicates requests are being rejected. For the full list of available metrics, see [Monitoring Neptune Analytics with CloudWatch](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/monitoring-cw.html). 