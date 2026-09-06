

# Auto-optimize
<a name="serverless-auto-optimize"></a>

Auto-optimize is a service that automates vector index optimizations, enabling users to balance search quality, speed, and cost without requiring weeks of manual expert tuning. It evaluates index configurations based on user-defined latency and recall requirements and generates optimization recommendations, so minimal expertise is required. Recommendations are typically delivered within 30-60 minutes.

Traditional vector index configuration requires significant expertise and experimentation to achieve optimal performance. Parameters like `ef_construction` (which controls index build quality), `m` (which determines the number of graph connections), `ef_search` (which controls HNSW search), and quantization methods (Binary Quantization (32x, 16x, 8x), Scalar quantization (4x)) significantly impact both search accuracy and resource utilization. Auto-optimize uses hyperparameter optimization algorithms to discover index configurations that are uniquely optimal for your dataset within your defined latency and recall requirements.

## Benefits
<a name="auto-optimize-benefits"></a>

Auto-optimize for OpenSearch provides the following benefits:
+ **Automated parameter tuning** - Eliminates manual experimentation with algorithm (HNSW), quantization, rescoring and engine parameters, saving time and reducing the learning curve for vector search optimization.
+ **Optimize search speed** - By default, OpenSearch is configured for in-memory performance. Auto-optimize discovers favorable trade-offs that improve search quality and cost savings while maintaining acceptable search speed.
+ **Cost optimization** - Reduces cost by finding options to reduce your index memory requirements while minimizing search quality and speed trade-offs.
+ **Optimize search quality** - Potentially deliver higher recall than default settings, or discover favorable trade-offs that deliver significant cost savings with minimal recall loss.

Auto-optimize works alongside other OpenSearch features such as [GPU-acceleration for vector indexing](gpu-acceleration-vector-index.md) to provide comprehensive performance optimization for vector search workloads.

## How it works
<a name="auto-optimize-how-it-works"></a>

Auto-optimize operates through a job-based architecture that analyzes your vector data and provides optimization recommendations. Key points:
+ Users share their datasets in Parquet or JSONL format in an Amazon S3 bucket.
+ They configure serverless auto-optimize jobs by configuring their acceptable recall and latency thresholds. More relaxed thresholds allow the service to discover more significant cost optimizations.
+ Auto-optimize jobs run on infrastructure fully-managed by Amazon OpenSearch Service. Jobs don't consume resources on your domain or collections. Workers run in parallel to evaluate index configurations, and use sampling on large datasets to deliver results typically within 30-60 minutes.
+ Each job is billed on a predictable flat rate. For pricing information, see [Amazon OpenSearch Service Pricing](https://aws.amazon.com/opensearch-service/pricing/).

## Prerequisites
<a name="auto-optimize-prerequisites"></a>
+ **Dataset format and permissions** - You must have your dataset available as one or more Parquet or JSONL files in an Amazon S3 bucket folder. For example:
  + Parquet: `s3://dataset-bucket-us-east-1/dataset_folder/first_half.parquet` and `s3://dataset-bucket-us-east-1/dataset_folder/second_half.parquet`
  + JSONL: `s3://dataset-bucket-us-east-1/dataset_folder/data.jsonl`

  Provide the enclosing folder URI (for example, `s3://dataset-bucket-us-east-1/dataset_folder/`). The folder must contain files of a single format — do not mix Parquet and JSONL files in the same folder. This dataset will be used to generate the recommendations. Ensure that your federated role has the following Amazon S3 permissions on that resource: `"s3:Get*", "s3:List*", "s3:Describe*"`.
+ **Specify correct dataset metadata** - The provided dataset must contain rows of float values. The name of each column and dimensionality of each vector must match the options provided in the console. For example, if the dataset contains vectors that are named `train_data` which are each `768` dimension, these values must match the auto-optimize console.
+ **(If using vector ingestion feature)** - If you plan to utilize the ingestion feature (taking auto-optimize recommendations to automatically create index and ingest data), you must configure your OpenSearch cluster to give auto-optimize permission to ingest your dataset into the OpenSearch cluster. For OpenSearch domains with a domain access policy, grant the newly created role access through that policy. For OpenSearch domains with fine-grained access control, add the pipeline role as a backend role. For OpenSearch Serverless collections, add the pipeline role to the data access policy.
+ **IAM permissions** - You need the following IAM permissions to use auto-optimize:
  + `opensearch:SubmitAutoOptimizeJob`
  + `opensearch:GetAutoOptimizeJob`
  + `opensearch:DeleteAutoOptimizeJob`
  + `opensearch:CancelAutoOptimizeJob`
  + `opensearch:ListAutoOptimizeJobs`
**Note**  
These are identity-based policies. Auto-optimize does not support resource-based policies.
+ **Credential expiry** - Configure your federated user session to have a minimum credential expiry of at least 1 hour. For very large datasets or high dimensions, consider increasing the expiration duration up to 3 hours.

## Use cases for auto-optimize
<a name="serverless-auto-optimize-use-cases"></a>

Auto-optimize is particularly valuable in the following scenarios:

**Initial configuration optimization**  
When first deploying vector search applications, determining optimal HNSW parameters often requires extensive testing and domain expertise. Auto-optimize eliminates this trial-and-error process by analyzing your data and workload characteristics to recommend production-ready configurations.

This use case is ideal for teams new to vector search or those migrating from other vector database platforms who need to establish baseline configurations quickly.

**Scaling optimization**  
As your vector dataset grows from thousands to millions of vectors, parameters that worked well initially may become suboptimal. Auto-optimize recommends adjustments to maintain performance at scale.

**Cost reduction**  
Vector indexes can consume significant compute and storage resources, especially with high-dimensional embeddings. Auto-optimize identifies opportunities to reduce costs by finding more efficient parameter configurations that maintain your required performance levels while using fewer resources.

For example, auto-optimize might discover that your current `m` value (graph connectedness) is higher than necessary for your accuracy requirements, allowing you to reduce indexing time and storage without impacting search quality.

**Performance troubleshooting**  
When experiencing slow query performance or high latency in vector search operations, auto-optimize can analyze your dataset and identify a more optimal configuration. The service provides specific recommendations to address performance bottlenecks, such as adjusting graph connectivity or search parameters.

## Limitations
<a name="auto-optimize-limitations"></a>
+ **Regional availability** - Auto-optimize is available only in the following AWS Regions:
  + ap-south-1
  + eu-west-1
  + us-west-2
  + us-east-2
  + us-east-1
  + eu-central-1
  + ap-southeast-2
  + ap-northeast-1
  + ap-southeast-1
+ **Collection types** - Auto-optimize is supported only for Vector Search Collections and OpenSearch Domains (2.19, 3.1, and 3.3).
+ **Engine support**  
**Engine support by deployment type**    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-auto-optimize.html)
+ **Algorithm support** - Auto-optimize supports only HNSW-based vector indexes.
+ **Concurrent jobs** - You can run up to 10 concurrent optimization jobs per account per Region. No new jobs can be accepted if limit is reached.
+ **Job duration** - Optimization jobs can take from 15 minutes to several hours depending on dataset size, dimension, and required performance metrics.
+ **Recommendations** - Auto-optimize suggests only up to 3 recommendations.
+ **Dataset**
  + Supported formats: Parquet, JSONL
  + Data store: Amazon S3

## Billing and costs
<a name="auto-optimize-billing"></a>

Auto-optimize uses a per-job pricing model where you pay for each successful optimization job irrespective of dataset size and optimization configurations. You won't be charged for failed or cancelled jobs. Additionally, auto-optimize runs on separate infrastructure than managed or serverless OpenSearch clusters, so it does not affect the resource utilization of preexisting clusters.

**Pricing model**  
Auto-optimize costs are billed separately from standard OpenSearch Serverless or OpenSearch Managed domain compute and storage costs.

For pricing information, see [Amazon OpenSearch Service Pricing](https://aws.amazon.com/opensearch-service/pricing/).

## Supported data formats
<a name="auto-optimize-data-formats"></a>

Auto-optimize supports the following data formats for vector datasets stored in Amazon S3:

### Parquet format
<a name="auto-optimize-parquet-format"></a>

Parquet is a columnar storage format optimized for analytical workloads. Each Parquet file should contain a column of float arrays representing your vector data.

Example Parquet file structure (viewed as a table):

```
| id  | train_data                     |
|-----|--------------------------------|
| 1   | [0.12, 0.45, 0.78, ..., 0.33] |
| 2   | [0.56, 0.89, 0.12, ..., 0.67] |
| 3   | [0.34, 0.67, 0.90, ..., 0.11] |
```

### JSONL format
<a name="auto-optimize-jsonl-format"></a>

JSONL (JSON Lines) is a text format where each line is a valid JSON object. Each line should contain a field with a float array representing your vector data.

Example JSONL file:

```
{"id": 1, "train_data": [0.12, 0.45, 0.78, 0.33]}
{"id": 2, "train_data": [0.56, 0.89, 0.12, 0.67]}
{"id": 3, "train_data": [0.34, 0.67, 0.90, 0.11]}
```

### Converting between formats
<a name="auto-optimize-convert-formats"></a>

If your data is in a different format, you can use the following Python scripts to convert it.

**Convert JSON or JSONL to Parquet**  


```
#!/usr/bin/env python3
import json
import pyarrow as pa
import pyarrow.parquet as pq
from pathlib import Path
from typing import Any, Dict, List


def load_json_any(path: Path) -> List[Dict[str, Any]]:
    """
    Load JSON that can be:
      - a list of objects
      - a single object
      - JSON Lines (one object per line)
    Returns list[dict].
    """
    text = path.read_text().strip()

    # Try full JSON file
    try:
        obj = json.loads(text)
        if isinstance(obj, list):
            return obj
        if isinstance(obj, dict):
            return [obj]
    except json.JSONDecodeError:
        pass

    # Fallback → JSON Lines
    records = []
    for i, line in enumerate(text.splitlines(), start=1):
        line = line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON on line {i}: {e}")
        if not isinstance(rec, dict):
            raise ValueError(f"Line {i} must contain a JSON object")
        records.append(rec)

    return records


def json_to_parquet(json_path: str, parquet_path: str, compression: str = "snappy"):
    """Convert ANY JSON to Parquet (schema inferred)."""
    records = load_json_any(Path(json_path))
    table = pa.Table.from_pylist(records)
    pq.write_table(table, parquet_path, compression=compression)
    print(f"Wrote {len(records)} rows to {parquet_path}")


if __name__ == "__main__":
    INPUT_JSON = "vectors.jsonl"
    OUTPUT_PARQUET = "vectors.parquet"
    json_to_parquet(INPUT_JSON, OUTPUT_PARQUET)
```

**Convert Parquet to JSONL**  


```
#!/usr/bin/env python3
import json
import pyarrow.parquet as pq


def parquet_to_jsonl(parquet_path: str, jsonl_path: str):
    """Convert a Parquet file to JSONL format."""
    table = pq.read_table(parquet_path)
    rows = table.to_pylist()
    with open(jsonl_path, "w") as f:
        for row in rows:
            f.write(json.dumps(row) + "\n")
    print(f"Wrote {len(rows)} rows to {jsonl_path}")


if __name__ == "__main__":
    INPUT_PARQUET = "vectors.parquet"
    OUTPUT_JSONL = "vectors.jsonl"
    parquet_to_jsonl(INPUT_PARQUET, OUTPUT_JSONL)
```

## Related features
<a name="auto-optimize-related-features"></a>

Auto-optimize works together with other Amazon OpenSearch Service features to help you build and optimize vector search applications:
+ [GPU-acceleration for vector indexing](gpu-acceleration-vector-index.md) - Accelerate vector index builds using GPU-acceleration to reduce indexing time and costs.
+ [Vector ingestion](serverless-vector-ingestion.md) - Quickly ingest and index vector data from Amazon S3 into your domain or collection.