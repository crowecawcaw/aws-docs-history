

# Set up managed Prometheus collectors for Amazon MSK
<a name="prom-msk-integration"></a>

To use an Amazon Managed Service for Prometheus collector, you create a scraper that discovers and pulls metrics in your Amazon Managed Streaming for Apache Kafka cluster. You can also create a scraper that integrates with Amazon Elastic Kubernetes Service or with Amazon OpenSearch Service. For more information, see [Integrate Amazon EKS](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector-how-to.html) and [Integrate Amazon OpenSearch Service](https://docs.aws.amazon.com/prometheus/latest/userguide/prom-opensearch-integration.html).

## Create a scraper
<a name="prom-msk-create-scraper"></a>

An Amazon Managed Service for Prometheus collector consists of a scraper that discovers and collects metrics from an Amazon MSK cluster. Amazon Managed Service for Prometheus manages the scraper for you, giving you the scalability, security, and reliability that you need, without having to manage any instances, agents, or scrapers yourself.

You can create a scraper using either the AWS API or the AWS CLI as described in the following procedures.

There are a few prerequisites for creating your own scraper:
+ You must have an Amazon MSK cluster created.
+ Configure your Amazon MSK cluster's security group to allow inbound traffic on ports **11001 (JMX Exporter)** and **11002 (Node Exporter)** within your Amazon VPC, as the scraper requires access to these DNS records to collect Prometheus metrics.
+ The Amazon VPC in which the Amazon MSK cluster resides must have [DNS enabled](https://docs.aws.amazon.com/vpc/latest/userguide/AmazonDNS-concepts.html).

**Note**  
The cluster will be associated with the scraper by its Amazon resource name (ARN). If you delete a cluster, and then create a new one with the same name, the ARN will be reused for the new cluster. Because of this, the scraper will attempt to collect metrics for the new cluster. You [delete scrapers](#prom-msk-delete-scraper) separately from deleting the cluster.

------
#### [ To create a scraper using the AWS API ]

Use the `CreateScraper` API operation to create a scraper with the AWS API. The following example creates a scraper in the US East (N. Virginia) Region. Replace the {{example}} content with your Amazon MSK cluster information, and provide your scraper configuration.

**Note**  
Configure the security group and subnets to match your target cluster. Include at least two subnets across two availability zones.

```
                POST /scrapers HTTP/1.1
Content-Length: 415 
Authorization: AUTHPARAMS
X-Amz-Date: 20201201T193725Z
User-Agent: aws-cli/1.18.147 Python/2.7.18 Linux/5.4.58-37.125.amzn2int.x86_64 botocore/1.18.6

{
    "alias": "{{myScraper}}",
    "destination":  {
        "ampConfiguration": {
            "workspaceArn": "arn:aws:aps:{{us-east-1}}:{{123456789012}}:workspace/{{ws-workspace-id}}"
        }
    },
    "source": {
        "vpcConfiguration": {
            "securityGroupIds": ["{{sg-security-group-id}}"],
            "subnetIds": ["{{subnet-subnet-id-1}}", "{{subnet-subnet-id-2}}"]
        }
    },
    "scrapeConfiguration": {
        "configurationBlob": {{base64-encoded-blob}}
    }
}
```

In the example, the `scrapeConfiguration` parameter requires a base64-encoded Prometheus configuration YAML file that specifies the DNS records of the MSK cluster.

Each DNS record represents a broker endpoint in a specific Availability Zone, allowing clients to connect to brokers distributed across your chosen AZs for high availability.

The number of DNS records in your MSK cluster properties corresponds to the number of broker nodes and Availability Zones in your cluster configuration:
+ **Default configuration** – 3 broker nodes across 3 AZs = 3 DNS records
+ **Custom configuration** – 2 broker nodes across 2 AZs = 2 DNS records

To get the DNS records for your MSK cluster, open the MSK console at [https://console.aws.amazon.com/msk/home?region=us-east-1\#/home/](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/). Go to your MSK cluster. Choose **Properties**, **Brokers**, and **Endpoints**.

You have two options for configuring Prometheus to scrape metrics from your MSK cluster:

1. **Cluster-level DNS resolution (Recommended)** – Use the cluster's base DNS name to automatically discover all brokers. If your broker endpoint is `b-1.clusterName.xxx.xxx.xxx`, use `clusterName.xxx.xxx.xxx` as the DNS record. This allows Prometheus to automatically scrape all brokers in the cluster.

   **Individual broker endpoints** – Specify each broker endpoint individually for granular control. Use the full broker identifiers (b-1, b-2) in your configuration. For example:

   ```
   dns_sd_configs:
     - names:
       - b-1.clusterName.xxx.xxx.xxx
       - b-2.clusterName.xxx.xxx.xxx  
       - b-3.clusterName.xxx.xxx.xxx
   ```

**Note**  
Replace `clusterName.xxx.xxx.xxx` with your actual MSK cluster endpoint from the AWS Console.

For more information, see [<dns\_sd\_config>](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#dns_sd_config) in the *Prometheus* documentation.

The following is an example of the scraper configuration file:

```
global:
  scrape_interval: 30s
  external_labels:
    clusterArn: msk-test-1

scrape_configs:
  - job_name: msk-jmx
    scheme: http
    metrics_path: /metrics
    scrape_timeout: 10s
    dns_sd_configs:
      - names:
          - {{dns-record-1}}
          - {{dns-record-2}}
          - {{dns-record-3}}
        type: A
        port: 11001
    relabel_configs:
      - source_labels: [__meta_dns_name]
        target_label: broker_dns
      - source_labels: [__address__]
        target_label: instance
        regex: '(.*)'
        replacement: '${1}'

  - job_name: msk-node
    scheme: http
    metrics_path: /metrics
    scrape_timeout: 10s
    dns_sd_configs:
      - names:
          - {{dns-record-1}}
          - {{dns-record-2}}
          - {{dns-record-3}}
        type: A
        port: 11002
    relabel_configs:
      - source_labels: [__meta_dns_name]
        target_label: broker_dns
      - source_labels: [__address__]
        target_label: instance
        regex: '(.*)'
        replacement: '${1}'
```

Run one of the following commands to convert the YAML file to base64. You can also use any online base64 converter to convert the file.

**Example Linux/macOS**  

```
echo -n {{scraper config updated with dns records}} | base64 
```

**Example Windows PowerShell**  

```
[Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes({{scraper config updated with dns records}}))
```

------
#### [ To create a scraper using the AWS CLI ]

Use the `create-scraper` command to create a scraper using the AWS Command Line Interface. The following example creates a scraper in the US East (N. Virginia) Region. Replace the {{example}} content with your Amazon MSK cluster information, and provide your scraper configuration.

**Note**  
Configure the security group and subnets to match your target cluster. Include at least two subnets across two availability zones.

```
aws amp create-scraper \
 --source vpcConfiguration="{securityGroupIds=['{{sg-security-group-id}}'],subnetIds=['{{subnet-subnet-id-1}}', '{{subnet-subnet-id-2}}']}" \ 
--scrape-configuration configurationBlob={{base64-encoded-blob}} \
 --destination ampConfiguration="{workspaceArn='arn:aws:aps:{{us-west-2}}:{{123456789012}}:workspace/{{ws-workspace-id}}'}"
```

------
+ The following is a full list of the scraper operations that you can use with the AWS API:

  Create a scraper with the [CreateScraper](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_CreateScraper.html) API operation.
+ List your existing scrapers with the [ListScrapers](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_ListScrapers.html) API operation.
+ Update the alias, configuration, or destination of a scraper with the [UpdateScraper](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_UpdateScraper.html) API operation.
+ Delete a scraper with the [DeleteScraper](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DeleteScraper.html) API operation.
+ Get more details about a scraper with the [DescribeScraper](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DescribeScraper.html) API operation.

## Cross-account setup
<a name="prom-msk-cross-account"></a>

To create a scraper in a cross-account setup when your Amazon MSK cluster from which you want to collect metrics is in a different account from the Amazon Managed Service for Prometheus collector, use the procedure below.

For example, when you have two accounts, the first source account `account_id_source` where the Amazon MSK is located, and a second target account `account_id_target` where the Amazon Managed Service for Prometheus workspace resides.

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

1. On every combination of source (Amazon MSK cluster) and target (Amazon Managed Service for Prometheus workspace), you need to create a role `arn:aws:iam::{{444455556666}}:role/Target` and add the following trust policy with permissions for [AmazonPrometheusRemoteWriteAccess](https://docs.aws.amazon.com/prometheus/latest/userguide/security-iam-awsmanpol.html).

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

1. Create a scraper with the `--role-configuration` option.

   ```
   aws amp create-scraper \ --source vpcConfiguration="{subnetIds={{[subnet-subnet-id]}}, "securityGroupIds": ["{{sg-security-group-id}}"]}" \ --scrape-configuration configurationBlob={{<base64-encoded-blob>}} \ --destination ampConfiguration="{workspaceArn='arn:aws:aps:{{aws-region}}:{{444455556666}}:workspace/{{ws-workspace-id}}'}"\ --role-configuration '{"sourceRoleArn":"arn:aws:iam::{{111122223333}}:role/Source", "targetRoleArn":"arn:aws:iam::{{444455556666}}:role/Target"}'
   ```

1. Validate the scraper creation.

   ```
   aws amp list-scrapers
   {
       "scrapers": [
           {
               "scraperId": "s-example123456789abcdef0",
               "arn": "arn:aws:aps:{{aws-region}}:111122223333:scraper/s-example123456789abcdef0": "arn:aws:iam::111122223333:role/Source",
               "status": "ACTIVE",
               "creationTime": "2025-10-27T18:45:00.000Z",
               "lastModificationTime": "2025-10-27T18:50:00.000Z",
               "tags": {},
               "statusReason": "Scraper is running successfully",
               "source": {
                   "vpcConfiguration": {
                       "subnetIds": ["subnet-subnet-id"],
                       "securityGroupIds": ["sg-security-group-id"]
                   }
               },
               "destination": {
                   "ampConfiguration": {
                       "workspaceArn": "arn:aws:aps:{{aws-region}}:444455556666:workspace/ws-workspace-id'"
                   }
               },
               "scrapeConfiguration": {
                   "configurationBlob": "<base64-encoded-blob>"
               }
           }
       ]
   }
   ```

## Changing between RoleConfiguration and service-linked role
<a name="prom-msk-changing-roles"></a>

When you want to switch back to a service-linked role instead of the `RoleConfiguration` to write to an Amazon Managed Service for Prometheus workspace, you must update the `UpdateScraper` and provide a workspace in the same account as the scraper without the `RoleConfiguration`. The `RoleConfiguration` will be removed from the scraper and the service-linked role will be used.

When you are changing workspaces in the same account as the scraper and you want to continue using the `RoleConfiguration`, you must again provide the `RoleConfiguration` on `UpdateScraper`.

## Find and delete scrapers
<a name="prom-msk-delete-scraper"></a>

You can use the AWS API or the AWS CLI to list the scrapers in your account or to delete them.

**Note**  
Make sure that you are using the latest version of the AWS CLI or SDK. The latest version provides you with the latest features and functionality, as well as security updates. Alternatively, use [AWS CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html), which provides an always up-to-date command line experience, automatically.

To list all the scrapers in your account, use the [ListScrapers](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_ListScrapers.html) API operation.

Alternatively, with the AWS CLI, call:

```
aws amp list-scrapers
```

`ListScrapers` returns all of the scrapers in your account, for example:

```
{
    "scrapers": [
        {
            "scraperId": "s-1234abcd-56ef-7890-abcd-1234ef567890",
            "arn": "arn:aws:aps:{{aws-region}}:123456789012:scraper/s-1234abcd-56ef-7890-abcd-1234ef567890",
            "roleArn": "arn:aws:iam::123456789012:role/aws-service-role/AWSServiceRoleForAmazonPrometheusScraper_1234abcd-2931",
            "status": {
                "statusCode": "DELETING"
            },
            "createdAt": "2023-10-12T15:22:19.014000-07:00",
            "lastModifiedAt": "2023-10-12T15:55:43.487000-07:00",
            "tags": {},
            "source": {
                "vpcConfiguration": {
                   "securityGroupIds": [
                        "sg-1234abcd5678ef90"
                    ],
                    "subnetIds": [
                        "subnet-abcd1234ef567890", 
                        "subnet-1234abcd5678ab90"
                    ]
                }
            },
            "destination": {
                "ampConfiguration": {
                    "workspaceArn": "arn:aws:aps:{{aws-region}}:123456789012:workspace/ws-1234abcd-5678-ef90-ab12-cdef3456a78"
                }
            }
        }
    ]
}
```

To delete a scraper, find the `scraperId` for the scraper that you want to delete, using the `ListScrapers` operation, and then use the [DeleteScraper](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_DeleteScraper.html) operation to delete it.

Alternatively, with the AWS CLI, call:

```
aws amp delete-scraper --scraper-id {{scraperId}}
```

## Metrics collected from Amazon MSK
<a name="prom-msk-metrics"></a>

When you integrate with Amazon MSK, the Amazon Managed Service for Prometheus collector automatically scrapes the following metrics:

### Metrics: jmx\_exporter and pod\_exporter jobs
<a name="broker-metrics"></a>


| Metric | Description / Purpose | 
| --- | --- | 
| jmx\_config\_reload\_failure\_total | Total number of times the JMX exporter failed to reload its configuration file. | 
| jmx\_scrape\_duration\_seconds | Time taken to scrape JMX metrics in seconds for the current collection cycle. | 
| jmx\_scrape\_error | Indicates whether an error occurred during JMX metric scraping (1 = error, 0 = success). | 
| java\_lang\_Memory\_HeapMemoryUsage\_used | Amount of heap memory (in bytes) currently used by the JVM. | 
| java\_lang\_Memory\_HeapMemoryUsage\_max | Maximum amount of heap memory (in bytes) that can be used for memory management. | 
| java\_lang\_Memory\_NonHeapMemoryUsage\_used | Amount of non-heap memory (in bytes) currently used by the JVM. | 
| kafka\_cluster\_Partition\_Value | Current state or value related to Kafka cluster partitions, broken down by partition ID and topic. | 
| kafka\_consumer\_consumer\_coordinator\_metrics\_assigned\_partitions | Number of partitions currently assigned to this consumer. | 
| kafka\_consumer\_consumer\_coordinator\_metrics\_commit\_latency\_avg | Average time taken to commit offsets in milliseconds. | 
| kafka\_consumer\_consumer\_coordinator\_metrics\_commit\_rate | Number of offset commits per second. | 
| kafka\_consumer\_consumer\_coordinator\_metrics\_failed\_rebalance\_total | Total number of failed consumer group rebalances. | 
| kafka\_consumer\_consumer\_coordinator\_metrics\_last\_heartbeat\_seconds\_ago | Number of seconds since the last heartbeat was sent to the coordinator. | 
| kafka\_consumer\_consumer\_coordinator\_metrics\_rebalance\_latency\_avg | Average time taken for consumer group rebalances in milliseconds. | 
| kafka\_consumer\_consumer\_coordinator\_metrics\_rebalance\_total | Total number of consumer group rebalances. | 
| kafka\_consumer\_consumer\_fetch\_manager\_metrics\_bytes\_consumed\_rate | Average number of bytes consumed per second by the consumer. | 
| kafka\_consumer\_consumer\_fetch\_manager\_metrics\_fetch\_latency\_avg | Average time taken for a fetch request in milliseconds. | 
| kafka\_consumer\_consumer\_fetch\_manager\_metrics\_fetch\_rate | Number of fetch requests per second. | 
| kafka\_consumer\_consumer\_fetch\_manager\_metrics\_records\_consumed\_rate | Average number of records consumed per second. | 
| kafka\_consumer\_consumer\_fetch\_manager\_metrics\_records\_lag\_max | Maximum lag in terms of number of records for any partition in this consumer. | 
| kafka\_consumer\_consumer\_metrics\_connection\_count | Current number of active connections. | 
| kafka\_consumer\_consumer\_metrics\_incoming\_byte\_rate | Average number of bytes received per second from all servers. | 
| kafka\_consumer\_consumer\_metrics\_last\_poll\_seconds\_ago | Number of seconds since the last consumer poll() call. | 
| kafka\_consumer\_consumer\_metrics\_request\_rate | Number of requests sent per second. | 
| kafka\_consumer\_consumer\_metrics\_response\_rate | Number of responses received per second. | 
| kafka\_consumer\_group\_ConsumerLagMetrics\_Value | Current consumer lag value for a consumer group, indicating how far behind the consumer is. | 
| kafka\_controller\_KafkaController\_Value | Current state or value of the Kafka controller (1 = active controller, 0 = not active). | 
| kafka\_controller\_ControllerEventManager\_Count | Total number of controller events processed. | 
| kafka\_controller\_ControllerEventManager\_Mean | Mean (average) time taken to process controller events. | 
| kafka\_controller\_ControllerStats\_MeanRate | Mean rate of controller statistics operations per second. | 
| kafka\_coordinator\_group\_GroupMetadataManager\_Value | Current state or value of the group metadata manager for consumer groups. | 
| kafka\_log\_LogFlushStats\_Count | Total number of log flush operations. | 
| kafka\_log\_LogFlushStats\_Mean | Mean (average) time taken for log flush operations. | 
| kafka\_log\_LogFlushStats\_MeanRate | Mean rate of log flush operations per second. | 
| kafka\_network\_RequestMetrics\_Count | Total count of network requests processed. | 
| kafka\_network\_RequestMetrics\_Mean | Mean (average) time taken to process network requests. | 
| kafka\_network\_RequestMetrics\_MeanRate | Mean rate of network requests per second. | 
| kafka\_network\_Acceptor\_MeanRate | Mean rate of accepted connections per second. | 
| kafka\_server\_Fetch\_queue\_size | Current size of the fetch request queue. | 
| kafka\_server\_Produce\_queue\_size | Current size of the produce request queue. | 
| kafka\_server\_Request\_queue\_size | Current size of the general request queue. | 
| kafka\_server\_BrokerTopicMetrics\_Count | Total count of broker topic operations (messages in/out, bytes in/out). | 
| kafka\_server\_BrokerTopicMetrics\_MeanRate | Mean rate of broker topic operations per second. | 
| kafka\_server\_BrokerTopicMetrics\_OneMinuteRate | One-minute moving average rate of broker topic operations. | 
| kafka\_server\_DelayedOperationPurgatory\_Value | Current number of delayed operations in the purgatory (waiting to be completed). | 
| kafka\_server\_DelayedFetchMetrics\_MeanRate | Mean rate of delayed fetch operations per second. | 
| kafka\_server\_FetcherLagMetrics\_Value | Current lag value for replica fetcher threads (how far behind the leader). | 
| kafka\_server\_FetcherStats\_MeanRate | Mean rate of fetcher operations per second. | 
| kafka\_server\_ReplicaManager\_Value | Current state or value of the replica manager. | 
| kafka\_server\_ReplicaManager\_MeanRate | Mean rate of replica manager operations per second. | 
| kafka\_server\_LeaderReplication\_byte\_rate | Rate of bytes replicated per second for partitions where this broker is the leader. | 
| kafka\_server\_group\_coordinator\_metrics\_group\_completed\_rebalance\_count | Total number of completed consumer group rebalances. | 
| kafka\_server\_group\_coordinator\_metrics\_offset\_commit\_count | Total number of offset commit operations. | 
| kafka\_server\_group\_coordinator\_metrics\_offset\_commit\_rate | Rate of offset commit operations per second. | 
| kafka\_server\_socket\_server\_metrics\_connection\_count | Current number of active connections. | 
| kafka\_server\_socket\_server\_metrics\_connection\_creation\_rate | Rate of new connection creation per second. | 
| kafka\_server\_socket\_server\_metrics\_connection\_close\_rate | Rate of connection closures per second. | 
| kafka\_server\_socket\_server\_metrics\_failed\_authentication\_total | Total number of failed authentication attempts. | 
| kafka\_server\_socket\_server\_metrics\_incoming\_byte\_rate | Rate of incoming bytes per second. | 
| kafka\_server\_socket\_server\_metrics\_outgoing\_byte\_rate | Rate of outgoing bytes per second. | 
| kafka\_server\_socket\_server\_metrics\_request\_rate | Rate of requests per second. | 
| kafka\_server\_socket\_server\_metrics\_response\_rate | Rate of responses per second. | 
| kafka\_server\_socket\_server\_metrics\_network\_io\_rate | Rate of network I/O operations per second. | 
| kafka\_server\_socket\_server\_metrics\_io\_ratio | Fraction of time spent in I/O operations. | 
| kafka\_server\_controller\_channel\_metrics\_connection\_count | Current number of active connections for controller channels. | 
| kafka\_server\_controller\_channel\_metrics\_incoming\_byte\_rate | Rate of incoming bytes per second for controller channels. | 
| kafka\_server\_controller\_channel\_metrics\_outgoing\_byte\_rate | Rate of outgoing bytes per second for controller channels. | 
| kafka\_server\_controller\_channel\_metrics\_request\_rate | Rate of requests per second for controller channels. | 
| kafka\_server\_replica\_fetcher\_metrics\_connection\_count | Current number of active connections for replica fetcher. | 
| kafka\_server\_replica\_fetcher\_metrics\_incoming\_byte\_rate | Rate of incoming bytes per second for replica fetcher. | 
| kafka\_server\_replica\_fetcher\_metrics\_request\_rate | Rate of requests per second for replica fetcher. | 
| kafka\_server\_replica\_fetcher\_metrics\_failed\_authentication\_total | Total number of failed authentication attempts for replica fetcher. | 
| kafka\_server\_ZooKeeperClientMetrics\_Count | Total count of ZooKeeper client operations. | 
| kafka\_server\_ZooKeeperClientMetrics\_Mean | Mean latency of ZooKeeper client operations. | 
| kafka\_server\_KafkaServer\_Value | Current state or value of the Kafka server (typically indicates server is running). | 
| node\_cpu\_seconds\_total | Total seconds the CPUs spent in each mode (user, system, idle, etc.), broken down by CPU and mode. | 
| node\_disk\_read\_bytes\_total | Total number of bytes read successfully from disks, broken down by device. | 
| node\_disk\_reads\_completed\_total | Total number of reads completed successfully for disks, broken down by device. | 
| node\_disk\_writes\_completed\_total | Total number of writes completed successfully for disks, broken down by device. | 
| node\_disk\_written\_bytes\_total | Total number of bytes written successfully to disks, broken down by device. | 
| node\_filesystem\_avail\_bytes | Available filesystem space in bytes for non-root users, broken down by device and mount point. | 
| node\_filesystem\_size\_bytes | Total size of the filesystem in bytes, broken down by device and mount point. | 
| node\_filesystem\_free\_bytes | Free filesystem space in bytes, broken down by device and mount point. | 
| node\_filesystem\_files | Total number of file nodes (inodes) on the filesystem, broken down by device and mount point. | 
| node\_filesystem\_files\_free | Number of free file nodes (inodes) on the filesystem, broken down by device and mount point. | 
| node\_filesystem\_readonly | Indicates whether the filesystem is mounted read-only (1 = read-only, 0 = read-write). | 
| node\_filesystem\_device\_error | Indicates whether an error occurred while getting filesystem statistics (1 = error, 0 = success). | 

## Limitations
<a name="prom-msk-limitations"></a>

The current Amazon MSK integration with Amazon Managed Service for Prometheus has the following limitations:
+ Only supported for Amazon MSK Provisioned clusters (not available for Amazon MSK Serverless)
+ Not supported for Amazon MSK clusters with public access enabled in combination with KRaft metadata mode
+ Currently supports a 1:1 mapping between Amazon MSK clusters and Amazon Managed Service for Prometheus collectors/workspaces