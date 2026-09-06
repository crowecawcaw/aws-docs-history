

# Set up managed Prometheus collectors for Amazon OpenSearch Service
<a name="prom-opensearch-integration"></a>

The Amazon Managed Service for Prometheus managed collector for Amazon OpenSearch Service automatically scrapes Prometheus-compatible metrics from your OpenSearch Service domain and forwards them to your destination. Amazon Managed Service for Prometheus manages the collector for you, giving you the scalability, security, and reliability that you need, without having to manage any instances, agents, or scrapers yourself. Your destination can be an Amazon Managed Service for Prometheus workspace or Amazon CloudWatch.

You can also create a scraper that integrates with Amazon Elastic Kubernetes Service or with Amazon Managed Streaming for Apache Kafka. For more information, see [Integrate Amazon EKS](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector-how-to.html) and [Integrate Amazon MSK](https://docs.aws.amazon.com/prometheus/latest/userguide/prom-msk-integration.html).

## Create a scraper
<a name="prom-opensearch-create-scraper"></a>

This procedure assumes that you are familiar with Amazon OpenSearch Service domain administration and Amazon Virtual Private Cloud networking concepts.

There are a few prerequisites for creating a scraper for an OpenSearch Service domain:
+ An Amazon OpenSearch Service domain with Amazon Virtual Private Cloud access. Managed collectors support only OpenSearch Service domains that have VPC access. Domains with public access are not supported.
+ Security groups that allow the managed collector to reach your OpenSearch Service domain endpoint over HTTPS (port 443). Add an inbound rule to the domain's security group that allows HTTPS traffic from the security group that you provide for the collector.

To tell the scraper which OpenSearch Service domain to collect from, you specify the domain in the `exporters` field of the request. The `exporters` field takes a list of exporter configurations; for an OpenSearch Service domain, provide an `openSearchConfiguration` with the `domainArn` of the domain. You provide the networking (subnets and security group) separately in the `source` field, as shown in the following examples.

**Note**  
The scraper uses the domain's VPC endpoint as resolved when you create the scraper. If you recreate the domain, it gets a new endpoint, so you must create a new scraper or update the existing one with [UpdateScraper](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_UpdateScraper.html) to collect from it.

You provide a scrape configuration when you create the scraper. The managed collector connects to the domain that you specify and collects its metrics automatically, so you do not specify scrape targets in the configuration. The configuration must include a `scrape_configs` section with a job whose `job_name` is exactly `opensearch-exporter`. A configuration that does not contain a job named `opensearch-exporter` is rejected. Use the scrape configuration to set the scrape interval and, optionally, to filter or relabel the collected metrics. The following is an example scrape configuration:

```
global:
  external_labels:
    domain_name: {{my-opensearch-domain}}

scrape_configs:
  - job_name: opensearch-exporter
    scrape_interval: 60s
```

For more information about the supported scrape configuration options, see [Scraper configuration](AMP-collector-how-to.md#AMP-collector-configuration).

------
#### [ To create a scraper using the AWS API ]

Use the `CreateScraper` API operation to create a scraper with the AWS API. The following example creates a scraper in the US East (N. Virginia) Region that collects metrics from an OpenSearch Service domain and sends them to an Amazon Managed Service for Prometheus workspace. Replace the {{example}} content with your own domain, networking, and workspace information, and provide your scraper configuration.

**Note**  
Configure the security group and subnets to match the Amazon VPC of your OpenSearch Service domain. Include at least two subnets across two Availability Zones.

```
POST /scrapers HTTP/1.1

{
    "alias": "{{myScraper}}",
    "source": {
        "vpcConfiguration": {
            "securityGroupIds": ["{{sg-security-group-id}}"],
            "subnetIds": ["{{subnet-subnet-id-1}}", "{{subnet-subnet-id-2}}"]
        }
    },
    "exporters": [
        {
            "openSearchConfiguration": {
                "domainArn": "arn:aws:es:{{us-east-1}}:{{123456789012}}:domain/{{my-opensearch-domain}}"
            }
        }
    ],
    "destination": {
        "ampConfiguration": {
            "workspaceArn": "arn:aws:aps:{{us-east-1}}:{{123456789012}}:workspace/{{ws-workspace-id}}"
        }
    },
    "scrapeConfiguration": {
        "configurationBlob": "{{base64-encoded-blob}}"
    }
}
```

To send the metrics to Amazon CloudWatch instead of an Amazon Managed Service for Prometheus workspace, replace the `destination` with a CloudWatch configuration:

```
    "destination": {
        "cloudWatchConfiguration": {
            "datasetArn": "arn:aws:cloudwatch:{{us-east-1}}:{{123456789012}}:dataset/default"
        }
    }
```

The `scrapeConfiguration` parameter requires a base64-encoded Prometheus configuration YAML file. Run one of the following commands to convert the YAML file to base64. You can also use any online base64 converter to convert the file.

**Example Linux/macOS**  

```
base64 -w0 {{scraper-config.yaml}}
```

**Example Windows PowerShell**  

```
[Convert]::ToBase64String([System.IO.File]::ReadAllBytes("{{scraper-config.yaml}}"))
```

------
#### [ To create a scraper using the AWS CLI ]

Use the `create-scraper` command to create a scraper using the AWS Command Line Interface. The following example creates a scraper in the US East (N. Virginia) Region. Replace the {{example}} content with your own domain, networking, and workspace information, and provide your scraper configuration.

**Note**  
Configure the security group and subnets to match the Amazon VPC of your OpenSearch Service domain. Include at least two subnets across two Availability Zones.

```
aws amp create-scraper \
 --source '{"vpcConfiguration":{"securityGroupIds":["{{sg-security-group-id}}"],"subnetIds":["{{subnet-subnet-id-1}}","{{subnet-subnet-id-2}}"]}}' \
 --exporters '[{"openSearchConfiguration":{"domainArn":"arn:aws:es:{{us-east-1}}:{{123456789012}}:domain/{{my-opensearch-domain}}"}}]' \
 --scrape-configuration configurationBlob={{base64-encoded-blob}} \
 --destination '{"ampConfiguration":{"workspaceArn":"arn:aws:aps:{{us-east-1}}:{{123456789012}}:workspace/{{ws-workspace-id}}"}}'
```

------
+ The following is a full list of the scraper operations that you can use with the AWS API:

  Create a scraper with the [CreateScraper](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_CreateScraper.html) API operation.
+ List your existing scrapers with the [ListScrapers](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_ListScrapers.html) API operation.
+ Update the alias, configuration, or destination of a scraper with the [UpdateScraper](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_UpdateScraper.html) API operation.
+ Delete a scraper with the [DeleteScraper](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DeleteScraper.html) API operation.
+ Get more details about a scraper with the [DescribeScraper](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DescribeScraper.html) API operation.

## Cross-account setup
<a name="prom-opensearch-cross-account"></a>

To create a scraper in a cross-account setup, when the OpenSearch Service domain that you want to collect metrics from is in a different account from the Amazon Managed Service for Prometheus collector, use the following procedure.

For example, you have two accounts: a source account `account_id_source` where the OpenSearch Service domain is located, and a target account `account_id_target` where the Amazon Managed Service for Prometheus workspace resides.

**Note**  
The trust policies in the following steps refer to the scraper by its ARN, which includes a {{scraper-id}} that does not exist until you create the scraper. To avoid this ordering problem, first create the roles with a wildcard (`scraper/*`) in place of the specific scraper ARN, create the scraper, and then update both trust policies to replace the wildcard with the actual scraper ARN that `CreateScraper` returns.

**To create a scraper in a cross-account setup**

1. In the source account, create a role `arn:aws:iam::{{111122223333}}:role/Source` and add the following trust policy.

   ```
   {
       "Effect": "Allow",
       "Principal": {
       "Service": [
           "scraper.aps.amazonaws.com"
        ]
       },
       "Action": "sts:AssumeRole",
       "Condition": {
           "ArnEquals": {
               "aws:SourceArn": "arn:aws:aps:{{aws-region}}:{{111122223333}}:scraper/{{scraper-id}}"
           },
           "StringEquals": {
               "AWS:SourceAccount": "{{111122223333}}"
           }
       }
   }
   ```

1. In the target account, create a role `arn:aws:iam::{{444455556666}}:role/Target` and add the following trust policy, which allows the source role to assume it.

   ```
   {
     "Effect": "Allow",
     "Principal": {
        "AWS": "arn:aws:iam::{{111122223333}}:role/Source"
     },
     "Action": "sts:AssumeRole",
     "Condition": {
        "StringEquals": {
           "sts:ExternalId": "arn:aws:aps:{{aws-region}}:{{111122223333}}:scraper/{{scraper-id}}"
         }
     }
   }
   ```

   Attach a permissions policy to the target role that allows it to write to your destination. If your destination is an Amazon Managed Service for Prometheus workspace, attach [AmazonPrometheusRemoteWriteAccess](https://docs.aws.amazon.com/prometheus/latest/userguide/security-iam-awsmanpol.html) (which grants `aps:RemoteWrite`). If your destination is Amazon CloudWatch, attach a policy that grants `cloudwatch:PutMetricData` on the dataset.

1. Create a scraper with the `--role-configuration` option.

   ```
   aws amp create-scraper \
    --source '{"vpcConfiguration":{"securityGroupIds":["{{sg-security-group-id}}"],"subnetIds":["{{subnet-subnet-id-1}}","{{subnet-subnet-id-2}}"]}}' \
    --exporters '[{"openSearchConfiguration":{"domainArn":"arn:aws:es:{{aws-region}}:{{111122223333}}:domain/{{my-opensearch-domain}}"}}]' \
    --scrape-configuration configurationBlob={{<base64-encoded-blob>}} \
    --destination '{"ampConfiguration":{"workspaceArn":"arn:aws:aps:{{aws-region}}:{{444455556666}}:workspace/{{ws-workspace-id}}"}}' \
    --role-configuration '{"sourceRoleArn":"arn:aws:iam::{{111122223333}}:role/Source", "targetRoleArn":"arn:aws:iam::{{444455556666}}:role/Target"}'
   ```

1. Validate the scraper creation.

   ```
   aws amp list-scrapers
   ```

## Find and delete scrapers
<a name="prom-opensearch-delete-scraper"></a>

You can use the AWS API or the AWS CLI to list the scrapers in your account or to delete them.

**Note**  
Make sure that you are using the latest version of the AWS CLI or SDK. The latest version provides you with the latest features and functionality, as well as security updates. Alternatively, use [AWS CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html), which provides an always up-to-date command line experience, automatically.

To list all the scrapers in your account, use the [ListScrapers](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_ListScrapers.html) API operation. Alternatively, with the AWS CLI, call:

```
aws amp list-scrapers
```

To delete a scraper, find the `scraperId` for the scraper that you want to delete, using the `ListScrapers` operation, and then use the [DeleteScraper](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DeleteScraper.html) operation to delete it. Alternatively, with the AWS CLI, call:

```
aws amp delete-scraper --scraper-id {{scraperId}}
```

## Metrics collected from Amazon OpenSearch Service
<a name="prom-opensearch-metrics"></a>

When you integrate with Amazon OpenSearch Service, the Amazon Managed Service for Prometheus collector automatically scrapes Prometheus-compatible metrics that describe the health and performance of your domain. The collector emits several hundred metrics; the following tables list representative metrics from each category. The `opensearch_indices_` metrics in the following tables are aggregated across the domain, and many have primary-only and total variants (suffixed `_primary` or `_total`). The collector also emits the same statistics per index, prefixed `opensearch_index_stats_`, and per-shard metrics prefixed `opensearch_indices_shards_`.

### Cluster metrics
<a name="opensearch-cluster-metrics"></a>


| Metric | Description / Purpose | 
| --- | --- | 
| opensearch\_cluster\_health\_status | Cluster health status (green, yellow, or red). | 
| opensearch\_cluster\_health\_number\_of\_nodes | Number of nodes in the cluster. | 
| opensearch\_cluster\_health\_number\_of\_data\_nodes | Number of data nodes in the cluster. | 
| opensearch\_cluster\_health\_active\_primary\_shards | Number of active primary shards. | 
| opensearch\_cluster\_health\_active\_shards | Total number of active shards, including primary and replica shards. | 
| opensearch\_cluster\_health\_relocating\_shards | Number of shards that are relocating between nodes. | 
| opensearch\_cluster\_health\_initializing\_shards | Number of shards that are initializing. | 
| opensearch\_cluster\_health\_unassigned\_shards | Number of shards that are not assigned to a node. | 
| opensearch\_cluster\_health\_delayed\_unassigned\_shards | Number of unassigned shards whose assignment is delayed. | 
| opensearch\_cluster\_health\_number\_of\_pending\_tasks | Number of cluster-level tasks that are queued and waiting to run. | 
| opensearch\_cluster\_health\_number\_of\_in\_flight\_fetch | Number of shard fetch requests in progress. | 
| opensearch\_cluster\_health\_task\_max\_waiting\_in\_queue\_millis | Longest time that a task has waited in the queue, in milliseconds. | 

### Node metrics
<a name="opensearch-node-metrics"></a>


| Metric | Description / Purpose | 
| --- | --- | 
| opensearch\_os\_cpu\_percent | Percentage of CPU used by the operating system on the node. | 
| opensearch\_os\_load1 | Operating system load average over the last 1 minute. The collector also emits `opensearch_os_load5` and `opensearch_os_load15`. | 
| opensearch\_os\_mem\_used\_bytes | Amount of physical memory used, in bytes. The collector also emits `opensearch_os_mem_free_bytes`, `opensearch_os_mem_actual_used_bytes`, and `opensearch_os_mem_actual_free_bytes`. | 
| opensearch\_jvm\_memory\_used\_bytes | Amount of JVM memory used, in bytes, by memory area (heap and non-heap). Related metrics include `opensearch_jvm_memory_committed_bytes` and `opensearch_jvm_memory_max_bytes`. | 
| opensearch\_jvm\_gc\_collection\_seconds\_count | Total number of JVM garbage collection events. Use with `opensearch_jvm_gc_collection_seconds_sum`, the total time spent in garbage collection. | 
| opensearch\_jvm\_uptime\_seconds | JVM uptime, in seconds. | 
| opensearch\_thread\_pool\_active\_count | Number of active threads in each thread pool. Related metrics include `opensearch_thread_pool_queue_count`, `opensearch_thread_pool_rejected_count`, and `opensearch_thread_pool_completed_count`. | 
| opensearch\_filesystem\_data\_available\_bytes | Amount of disk space available to the node, in bytes. Related metrics include `opensearch_filesystem_data_free_bytes` and `opensearch_filesystem_data_size_bytes`. | 
| opensearch\_filesystem\_io\_stats\_device\_read\_operations\_count | Number of disk read operations. The collector also emits write and total operation counts and read and write sizes (for example, `opensearch_filesystem_io_stats_device_read_size_kilobytes_sum`). | 
| opensearch\_process\_cpu\_percent | Percentage of CPU used by the OpenSearch process. | 
| opensearch\_process\_mem\_resident\_size\_bytes | Resident memory size of the OpenSearch process, in bytes. | 
| opensearch\_process\_open\_files\_count | Number of file descriptors open by the OpenSearch process. | 
| opensearch\_breakers\_tripped | Total number of times each circuit breaker has tripped. Related metrics include `opensearch_breakers_estimated_size_bytes` and `opensearch_breakers_limit_size_bytes`. | 
| opensearch\_transport\_rx\_size\_bytes\_total | Total amount of data received over the transport layer between nodes, in bytes. The collector also emits `opensearch_transport_tx_size_bytes_total` and packet counts. | 
| opensearch\_indexing\_pressure\_current\_all\_in\_bytes | Current memory consumed by indexing requests, in bytes, with `opensearch_indexing_pressure_limit_in_bytes` as the configured limit. | 

### Index metrics
<a name="opensearch-index-metrics"></a>


| Metric | Description / Purpose | 
| --- | --- | 
| opensearch\_indices\_docs | Number of documents. Related metrics include `opensearch_indices_docs_deleted`, `opensearch_indices_docs_primary`, and `opensearch_indices_docs_total`. | 
| opensearch\_indices\_store\_size\_bytes | Total size of the indices on disk, in bytes, with `opensearch_indices_store_size_bytes_primary` and `opensearch_indices_store_size_bytes_total` variants. | 
| opensearch\_indices\_indexing\_index\_total | Total number of documents indexed. Use with `opensearch_indices_indexing_index_time_seconds_total` for indexing latency. | 
| opensearch\_indices\_indexing\_is\_throttled | Indicates whether indexing is currently throttled, with `opensearch_indices_indexing_throttle_time_seconds_total` for the total throttled time. | 
| opensearch\_indices\_search\_query\_total | Total number of search queries. Use with `opensearch_indices_search_query_time_seconds` for query latency. | 
| opensearch\_indices\_search\_fetch\_total | Total number of fetch operations, with `opensearch_indices_search_fetch_time_seconds` for fetch latency. | 
| opensearch\_indices\_get\_total | Total number of get operations, with `opensearch_indices_get_time_seconds` for get latency. | 
| opensearch\_indices\_merges\_total | Total number of segment merges completed. Related metrics include `opensearch_indices_merges_current` and `opensearch_indices_merges_total_time_seconds_total`. | 
| opensearch\_indices\_refresh\_total | Total number of index refresh operations, with `opensearch_indices_refresh_time_seconds_total` for refresh time. | 
| opensearch\_indices\_flush\_total | Total number of index flush operations, with `opensearch_indices_flush_time_seconds` for flush time. | 
| opensearch\_indices\_segments\_count | Number of segments. The collector also emits per-segment memory metrics (for example, `opensearch_indices_segments_memory_bytes` and `opensearch_indices_segment_terms_memory_total`). | 
| opensearch\_indices\_translog\_operations | Number of operations in the transaction log, with `opensearch_indices_translog_size_in_bytes` for its size. | 
| opensearch\_indices\_fielddata\_memory\_size\_bytes | Memory used by the field data cache, in bytes, with `opensearch_indices_fielddata_evictions` for evictions. | 
| opensearch\_indices\_query\_cache\_memory\_size\_bytes | Memory used by the query cache, in bytes. Related metrics include `opensearch_indices_query_cache_count` and `opensearch_indices_query_cache_evictions`. | 
| opensearch\_indices\_request\_cache\_memory\_size\_bytes | Memory used by the request cache, in bytes. Related metrics include `opensearch_indices_request_cache_count` and `opensearch_indices_request_cache_evictions`. | 

## Limitations
<a name="prom-opensearch-limitations"></a>

The Amazon OpenSearch Service integration with Amazon Managed Service for Prometheus has the following limitations:
+ Only supported for OpenSearch Service domains that have Amazon Virtual Private Cloud access. Domains with public access are not supported.
+ A scraper collects metrics from a single OpenSearch Service domain. To collect metrics from more than one domain, create a separate scraper for each domain.