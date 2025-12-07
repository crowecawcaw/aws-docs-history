# Auto-optimize

Auto-optimize is a service that automates vector index optimizations, enabling users to balance search quality, speed, and cost without requiring weeks of manual expert tuning. It evaluates index configurations based on user-defined latency and recall requirements and generates optimization recommendations, so minimal expertise is required. Recommendations are typically delivered within 30-60 minutes.

Traditional vector index configuration requires significant expertise and experimentation to achieve optimal performance. Parameters like `ef_construction` (which controls index build quality), `m` (which determines the number of graph connections), `ef_search` (which controls HNSW search), and quantization methods (Binary Quantization (32x, 16x, 8x), Scalar quantization (4x)) significantly impact both search accuracy and resource utilization. Auto-optimize uses hyperparameter optimization algorithms to discover index configurations that are uniquely optimal for your dataset within your defined latency and recall requirements.

## Benefits

Auto-optimize for OpenSearch provides the following benefits:

- **Automated parameter tuning** - Eliminates manual experimentation with algorithm (HNSW), quantization, rescoring and engine parameters, saving time and reducing the learning curve for vector search optimization.
- **Optimize search speed** - By default, OpenSearch is configured for in-memory performance. Auto-optimize discovers favorable trade-offs that improve search quality and cost savings while maintaining acceptable search speed.
- **Cost optimization** - Reduces cost by finding options to reduce your index memory requirements while minimizing search quality and speed trade-offs.
- **Optimize search quality** - Potentially deliver higher recall than default settings, or discover favorable trade-offs that deliver significant cost savings with minimal recall loss.

Auto-optimize works alongside other OpenSearch features such as [GPU-acceleration for vector indexing](gpu-acceleration-vector-index.md "gpu-acceleration-vector-index.md") to provide comprehensive performance optimization for vector search workloads.

## How it works

Auto-optimize operates through a job-based architecture that analyzes your vector data and provides optimization recommendations. Key points:

- Users share their datasets as OpenSearch JSON documents in parquet format in an Amazon S3 bucket.
- They configure serverless auto-optimize jobs by configuring their acceptable recall and latency thresholds. More relaxed thresholds allow the service to discover more significant cost optimizations.
- Auto-optimize jobs run on infrastructure fully-managed by Amazon OpenSearch Service. Jobs don't consume resources on your domain or collections. Workers run in parallel to evaluate index configurations, and use sampling on large datasets to deliver results typically within 30-60 minutes.
- Each job is billed on a predictable flat rate. For pricing information, see [Amazon OpenSearch Service Pricing](https://aws.amazon.com/opensearch-service/pricing/ "https://aws.amazon.com/opensearch-service/pricing/").

## Prerequisites

- **Dataset format and permissions** - You must have dataset available as a set (one or many) parquet files in an Amazon S3 bucket folder. For instance, if the dataset is split into two files called `s3://dataset-bucket-us-east-1/dataset_folder/first_half.parquet` and `s3://dataset-bucket-us-east-1/dataset_folder/second_half.parquet`, then you should place `s3://dataset-bucket-us-east-1/dataset_folder/` here. This dataset will be used to generate the recommendations. Ensure that your federated role has the following Amazon S3 permissions on that resource: `"s3:Get*", "s3:List*", "s3:Describe*"`.
- **Specify correct dataset metadata** - The provided parquet dataset must contain rows of float values. The name of each column and dimensionality of each vector must match the options provided in the console. For example, if the dataset contains vectors that are named `train_data` which are each `768` dimension, these values must match the auto-optimize console.
- **(If using vector ingestion feature)** - If you plan to utilize the ingestion feature (taking auto-optimize recommendations to automatically create index and ingest data), you must configure your OpenSearch cluster to give auto-optimize permission to ingest your parquet dataset into the OpenSearch cluster. For OpenSearch domains with a domain access policy, grant the newly created role access through that policy. For OpenSearch domains with fine-grained access control, add the pipeline role as a backend role. For OpenSearch Serverless collections, add the pipeline role to the data access policy.
- **IAM permissions** - You need the following IAM permissions to use auto-optimize:
  - `opensearch:SubmitAutoOptimizeJob`
  - `opensearch:GetAutoOptimizeJob`
  - `opensearch:DeleteAutoOptimizeJob`
  - `opensearch:CancelAutoOptimizeJob`
  - `opensearch:ListAutoOptimizeJobs`

###### Note

These are identity-based policies. Auto-optimize does not support resource-based policies.

- **Credential expiry** - Configure your federated user session to have a minimum credential expiry of at least 1 hour. For very large datasets or high dimensions, consider increasing the expiration duration up to 3 hours.

## Use cases for auto-optimize

Auto-optimize is particularly valuable in the following scenarios:

###### Initial configuration optimization

When first deploying vector search applications, determining optimal HNSW parameters often requires extensive testing and domain expertise. Auto-optimize eliminates this trial-and-error process by analyzing your data and workload characteristics to recommend production-ready configurations.

This use case is ideal for teams new to vector search or those migrating from other vector database platforms who need to establish baseline configurations quickly.

###### Scaling optimization

As your vector dataset grows from thousands to millions of vectors, parameters that worked well initially may become suboptimal. Auto-optimize recommends adjustments to maintain performance at scale.

###### Cost reduction

Vector indexes can consume significant compute and storage resources, especially with high-dimensional embeddings. Auto-optimize identifies opportunities to reduce costs by finding more efficient parameter configurations that maintain your required performance levels while using fewer resources.

For example, auto-optimize might discover that your current `m` value (graph connectedness) is higher than necessary for your accuracy requirements, allowing you to reduce indexing time and storage without impacting search quality.

###### Performance troubleshooting

When experiencing slow query performance or high latency in vector search operations, auto-optimize can analyze your dataset and identify a more optimal configuration. The service provides specific recommendations to address performance bottlenecks, such as adjusting graph connectivity or search parameters.

## Limitations

- **Regional availability** - Auto-optimize is available only in the following AWS Regions:
  - ap-south-1
  - eu-west-1
  - us-west-2
  - us-east-2
  - us-east-1
  - eu-central-1
  - ap-southeast-2
  - ap-northeast-1
  - ap-southeast-1

- **Collection types** - Auto-optimize is supported only for Vector Search Collections and OpenSearch Domains (2.19, 3.1, and 3.3).
- **Engine support**

| Engine support by deployment type | Engine | Serverless | OpenSearch Managed |
| --------------------------------- | ------ | ---------- | ------------------ |
| Lucene                            | No     | Yes        |
| Faiss                             | Yes    | Yes        |
| Nmslib                            | No     | No         |

- **Algorithm support** - Auto-optimize supports only HNSW-based vector indexes.
- **Concurrent jobs** - You can run up to 10 concurrent optimization jobs per account per Region. No new jobs can be accepted if limit is reached.
- **Job duration** - Optimization jobs can take from 15 minutes to several hours depending on dataset size, dimension, and required performance metrics.
- **Recommendations** - Auto-optimize suggests only up to 3 recommendations.
- **Dataset**
  - Supported formats: parquet
  - Data store: Amazon S3

## Billing and costs

Auto-optimize uses a per-job pricing model where you pay for each successful optimization job irrespective of dataset size and optimization configurations. You won't be charged for failed or cancelled jobs. Additionally, auto-optimize runs on separate infrastructure than managed or serverless OpenSearch clusters, so it does not affect the resource utilization of preexisting clusters.

###### Pricing model

Auto-optimize costs are billed separately from standard OpenSearch Serverless or OpenSearch Managed domain compute and storage costs.

For pricing information, see [Amazon OpenSearch Service Pricing](https://aws.amazon.com/opensearch-service/pricing/ "https://aws.amazon.com/opensearch-service/pricing/").

## Convert JSONL to Parquet

If your data is in JSONL format, you can use the following Python script to convert it to Parquet format for use with auto-optimize:

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
    print(f"✔ Wrote {len(records)} rows to {parquet_path}")


def print_parquet_rows(parquet_path: str, limit: int = 5):
    """Print first N rows from the parquet file."""
    table = pq.read_table(parquet_path)
    df = table.to_pandas()

    print(f"\n=== Showing first {min(limit, len(df))} rows from {parquet_path} ===")
    print(df.head(limit).to_string())
    print("===========================================================\n")


if __name__ == "__main__":
    INPUT_JSON = "movies_10k.json"
    OUTPUT_PARQUET = "movies.parquet"

    # Convert JSON → Parquet
    json_to_parquet(INPUT_JSON, OUTPUT_PARQUET)

    # Print some rows from Parquet
    print_parquet_rows(OUTPUT_PARQUET, limit=3)
```

## Related features

Auto-optimize works together with other Amazon OpenSearch Service features to help you build and optimize vector search applications:

- [GPU-acceleration for vector indexing](gpu-acceleration-vector-index.md "gpu-acceleration-vector-index.md") - Accelerate vector index builds using GPU-acceleration to reduce indexing time and costs.
- [Vector ingestion](serverless-vector-ingestion.md "serverless-vector-ingestion.md") - Quickly ingest and index vector data from Amazon S3 into your domain or collection.
