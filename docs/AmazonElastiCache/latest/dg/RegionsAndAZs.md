

# Choosing regions and availability zones for ElastiCache
<a name="RegionsAndAZs"></a>

You can provide additional scalability and reliability to your ElastiCache clusters by designating Regions and Availability Zones using the corresponding endpoint.

AWS Cloud computing resources are housed in highly available data center facilities. To provide additional scalability and reliability, these data center facilities are located in different physical locations. These locations are categorized by *regions* and *Availability Zones*.

AWS Regions are large and widely dispersed into separate geographic locations. Availability Zones are distinct locations within an AWS Region that are engineered to be isolated from failures in other Availability Zones. They provide inexpensive, low-latency network connectivity to other Availability Zones in the same AWS Region.

**Important**  
Each region is completely independent. Any ElastiCache activity you initiate (for example, creating clusters) runs only in your current default region.

To create or work with a cluster in a specific region, use the corresponding regional service endpoint. For service endpoints, see [Supported Regions & endpoints](#SupportedRegions).

![Image: Regions and Availability Zones](http://docs.aws.amazon.com/AmazonElastiCache/latest/dg/images/ElastiCache-RegionsAndAZs.png)


*Regions and Availability Zones*

**Topics**
+ [Availability Zone considerations with Memcached](#CacheNode.Memcached.AvailabilityZones)
+ [Locating your nodes](#RegionsAndAZs.AZMode)
+ [Supported Regions & endpoints](#SupportedRegions)
+ [Using local zones with ElastiCache](Local_zones.md)
+ [Using Outposts with ElastiCache](ElastiCache-Outposts.md)

## Availability Zone considerations with Memcached
<a name="CacheNode.Memcached.AvailabilityZones"></a>

Distributing your Memcached nodes over multiple Availability Zones within a region helps protect you from the impact of a catastrophic failure, such as a power loss within an Availability Zone.

**Serverless Caching**

ElastiCache serverless caching creates a highly available cache that spans multiple Availability Zones. You can specify subnets from different availability zones and same VPC as you create your serverless cluster or ElastiCache will choose subnets automatically from your default VPC. 

**Designing your own ElastiCache for Memcached cluster**

A Memcached cluster can have up to 300 nodes. When you create or add nodes to your Memcached cluster, you can specify a single Availability Zone for all your nodes, allow ElastiCache to choose a single Availability Zone for all your nodes, specify the Availability Zones for each node, or allow ElastiCache to choose an Availability Zone for each node. New nodes can be created in different Availability Zones as you add them to an existing Memcached cluster. Once a cache node is created, its Availability Zone cannot be modified. 

If you want a cluster in a single Availability Zone cluster to have its nodes distributed across multiple Availability Zones, ElastiCache can create new nodes in the various Availability Zones. You can then delete some or all of the original cache nodes. We recommend this approach.

**To migrate Memcached nodes from a single Availability Zone to multiple availability zones**

1. Modify your cluster by creating new cache nodes in the Availability Zones where you want them. In your request, do the following:
   + Set `AZMode` (CLI: `- -az-mode`) to `cross-az`.
   + Set `NumCacheNodes` (CLI: `- -num-cache-nodes`) to the number of currently active cache nodes plus the number of new cache nodes you want to create.
   + Set `NewAvailabilityZones` (CLI: `- -new-availability-zones`) to a list of the zones you want the new cache nodes created in. To let ElastiCache determine the Availability Zone for each new node, don't specify a list.
   +  Set `ApplyImmediately` (CLI: `- -apply-immediately`) to true. 
**Note**  
If you are not using auto discovery, be sure to update your client application with the new cache node endpoints.

   Before moving on to the next step, be sure the Memcached nodes are fully created and available.

1. Modify your cluster by removing the nodes you no longer want in the original Availability Zone. In your request, do the following:
   + Set `NumCacheNodes` (CLI: `- -num-cache-nodes`) to the number of active cache nodes you want after this modification is applied.
   + Set `CacheNodeIdsToRemove` (CLI: `- -nodes-to-remove`) to a list of the cache nodes you want to remove from the cluster.

     The number of cache node IDs listed must equal the number of currently active nodes minus the value in `NumCacheNodes`.
   + (Optional) Set `ApplyImmediately` (CLI: `- -apply-immediately`) to true.

     If you don't set `ApplyImmediately` (CLI: `- -apply-immediately`) to true, the node deletions will take place at your next maintenance window.

## Locating your nodes
<a name="RegionsAndAZs.AZMode"></a>

Amazon ElastiCache supports locating all of a cluster's nodes in a single or multiple Availability Zones (AZs). Further, if you elect to locate your nodes in multiple AZs (recommended), ElastiCache enables you to either choose the AZ for each node, or allow ElastiCache to choose them for you.

By locating the nodes in different AZs, you eliminate the chance that a failure, such as a power outage, in one AZ will cause your entire system to fail. Testing has demonstrated that there is no significant latency difference between locating all nodes in one AZ or spreading them across multiple AZs. 

You can specify an AZ for each node when you create a cluster, or by adding nodes when you modify an existing cluster. When specifying an AZ for each node while creating a cluster, the AZ must be available in that subnet group. For more information, see the following:
+ [Creating a cluster for Memcached](Clusters.Create-mc.md)
+ [Creating a cluster for Valkey or Redis OSS](Clusters.Create.md)
+ [Modifying an ElastiCache cluster](Clusters.Modify.md)
+ [Adding nodes to an ElastiCache cluster](Clusters.AddNode.md)

## Supported Regions & endpoints
<a name="SupportedRegions"></a>

Amazon ElastiCache is available in multiple AWS Regions. This means that you can launch ElastiCache clusters in locations that meet your requirements. For example, you can launch in the AWS Region closest to your customers, or launch in a particular AWS Region to meet certain legal requirements.

Each Region is designed to be completely isolated from the other Regions. Within each Region are multiple Availability Zones (AZ). ElastiCache Serverless caches automatically replicate data across multiple availability zones (except `us-west-1`, where data is replicated in two availability zones) for high availability. When designing your own ElastiCache cluster, you can choose to launch your nodes in different AZs to achieve fault tolerance. For more information on Regions and Availability Zones, see [Choosing regions and availability zones for ElastiCache](#RegionsAndAZs) at the top of this topic.


**Regions where ElastiCache is supported**  

<table>
<thead>
  <tr><th>Region Name/Region</th><th>Endpoint</th><th>Protocol</th><th></th></tr>
</thead>
<tbody>
  <tr><td>US East (Ohio) Region<br /><code>us-east-2</code></td><td><code>elasticache.us-east-2.amazonaws.com</code></td><td>HTTPS</td><td></td></tr>
  <tr><td>US East (N. Virginia) Region<br /><code>us-east-1</code></td><td><code>elasticache.us-east-1.amazonaws.com</code></td><td>HTTPS</td><td></td></tr>
  <tr><td>US West (N. California) Region<br /><code>us-west-1</code></td><td><code>elasticache.us-west-1.amazonaws.com</code></td><td>HTTPS</td><td></td></tr>
  <tr><td>US West (Oregon) Region<br /><code>us-west-2</code></td><td><code>elasticache.us-west-2.amazonaws.com</code></td><td>HTTPS</td><td></td></tr>
  <tr><td>Canada (Central) Region<br /><code>ca-central-1</code></td><td><code>elasticache.ca-central-1.amazonaws.com</code></td><td>HTTPS</td><td></td></tr>
  <tr><td>Canada (West) Region<br /><code>ca-west-1</code></td><td><code>elasticache.ca-west-1.amazonaws.com</code></td><td>HTTPS</td><td></td></tr>
  <tr><td>Asia Pacific (Jakarta)<br /><code>ap-southeast-3</code></td><td><code>elasticache.ap-southeast-3.amazonaws.com</code></td><td>HTTPS</td><td></td></tr>
  <tr><td>Asia Pacific (Mumbai) Region<br /><code>ap-south-1</code></td><td><code>elasticache.ap-south-1.amazonaws.com</code></td><td>HTTPS</td><td></td></tr>
  <tr><td>Asia Pacific (Hyderabad) Region<br /><code>ap-south-2</code></td><td><code>elasticache.ap-south-2.amazonaws.com</code></td><td>HTTPS</td><td></td></tr>
  <tr><td>Asia Pacific (Tokyo) Region<br /><code>ap-northeast-1</code></td><td><code>elasticache.ap-northeast-1.amazonaws.com</code></td><td>HTTPS</td><td></td></tr>
  <tr><td>Asia Pacific (Seoul) Region<br /><code>ap-northeast-2</code></td><td><code>elasticache.ap-northeast-2.amazonaws.com</code></td><td>HTTPS</td><td></td></tr>
  <tr><td>Asia Pacific (Osaka) Region<br /><code>ap-northeast-3</code></td><td><code>elasticache.ap-northeast-3.amazonaws.com</code></td><td>HTTPS</td><td></td></tr>
  <tr><td>Asia Pacific (Singapore) Region<br /><code>ap-southeast-1</code></td><td><code>elasticache.ap-southeast-1.amazonaws.com</code></td><td>HTTPS</td><td></td></tr>
  <tr><td>Asia Pacific (Sydney) Region<br /><code>ap-southeast-2</code></td><td><code>elasticache.ap-southeast-2.amazonaws.com</code></td><td>HTTPS</td><td></td></tr>
  <tr><td>Europe (Frankfurt) Region<br /><code>eu-central-1</code></td><td><code>elasticache.eu-central-1.amazonaws.com</code></td><td>HTTPS</td><td></td></tr>
  <tr><td>Europe (Zurich) Region<br /><code>eu-central-2</code></td><td><code>elasticache.eu-central-2.amazonaws.com</code></td><td>HTTPS</td><td></td></tr>
  <tr><td>Europe (Stockholm) Region<br /><code>eu-north-1</code></td><td><code>elasticache.eu-north-1.amazonaws.com</code></td><td>HTTPS</td><td></td></tr>
  <tr><td>Middle East (Bahrain) Region<br /><code>me-south-1</code></td><td><code>elasticache.me-south-1.amazonaws.com</code></td><td>HTTPS</td><td></td></tr>
  <tr><td>Middle East (UAE) Region<br /><code>me-central-1</code></td><td><code>elasticache.me-central-1.amazonaws.com</code></td><td>HTTPS</td><td></td></tr>
  <tr><td>Europe (Ireland) Region<br /><code>eu-west-1</code></td><td><code>elasticache.eu-west-1.amazonaws.com</code></td><td>HTTPS</td><td></td></tr>
  <tr><td>Europe (London) Region<br /><code>eu-west-2</code></td><td><code>elasticache.eu-west-2.amazonaws.com</code></td><td>HTTPS</td><td></td></tr>
  <tr><td>EU (Paris) Region<br /><code>eu-west-3</code></td><td><code>elasticache.eu-west-3.amazonaws.com</code></td><td>HTTPS</td><td></td></tr>
  <tr><td>Europe (Milan) Region<br /><code>eu-south-1</code></td><td><code>elasticache.eu-south-1.amazonaws.com</code></td><td>HTTPS</td><td></td></tr>
  <tr><td>Europe (Spain) Region<br /><code>eu-south-2</code></td><td><code>elasticache.eu-south-2.amazonaws.com</code></td><td>HTTPS</td><td></td></tr>
  <tr><td>South America (São Paulo) Region<br /><code>sa-east-1</code></td><td><code>elasticache.sa-east-1.amazonaws.com</code></td><td>HTTPS</td><td></td></tr>
  <tr><td>China (Beijing) Region<br /><code>cn-north-1</code></td><td><code>elasticache.cn-north-1.amazonaws.com.cn</code></td><td>HTTPS</td><td></td></tr>
  <tr><td>China (Ningxia) Region<br /><code>cn-northwest-1</code></td><td><code>elasticache.cn-northwest-1.amazonaws.com.cn</code></td><td>HTTPS</td><td></td></tr>
  <tr><td>Asia Pacific (Hong Kong) Region<br /><code>ap-east-1</code></td><td><code>elasticache.ap-east-1.amazonaws.com</code></td><td>HTTPS</td><td></td></tr>
  <tr><td>Africa (Cape Town) Region<br /><code>af-south-1</code></td><td><code>elasticache.af-south-1.amazonaws.com</code></td><td>HTTPS</td><td></td></tr>
  <tr><td>Israel (Tel Aviv) Region<br /><code>il-central-1</code></td><td><code>elasticache.il-central-1.amazonaws.com</code></td><td>HTTPS</td><td></td></tr>
  <tr><td>AWS GovCloud (US-West)<br /><code>us-gov-west-1</code></td><td><code>elasticache.us-gov-west-1.amazonaws.com</code></td><td>HTTPS</td><td></td></tr>
  <tr><td>AWS GovCloud (US-East)<br /><code>us-gov-east-1</code></td><td><code>elasticache.us-gov-east-1.amazonaws.com</code></td><td>HTTPS</td><td></td></tr>
  <tr><td colspan="3">For information on using the AWS GovCloud (US) with ElastiCache, see <a href="https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-elc.html">Services in the AWS GovCloud (US) region: ElastiCache</a>.</td><td></td></tr>
</tbody>
</table>


Some Regions support a subset of node types. For a table of supported node types by AWS Region, see [Supported node types by AWS Region](CacheNodes.SupportedTypes.md#CacheNodes.SupportedTypesByRegion).

Most Regions support establishing a private connection between your VPC and ElastiCache API endpoints, by creating an interface VPC endpoint through AWS PrivateLink. For more information, see [ElastiCache API and interface VPC endpoints (AWS PrivateLink)](elasticache-privatelink.md).

For a table of AWS products and services by region, see [Products and Services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).