# Choosing Regions and Availability Zones

AWS Cloud computing resources are housed in highly available data center
facilities. To provide additional scalability and reliability, these data center
facilities are located in different physical locations. These locations are
categorized by _regions_ and _Availability Zones_.

AWS Regions are large and widely dispersed into separate geographic locations.
Availability Zones are distinct locations within an AWS Region that are engineered to be
isolated from failures in other Availability Zones. They provide inexpensive, low-latency
network connectivity to other Availability Zones in the same AWS Region.

###### Important

Each region is completely independent. Any MemoryDB activity you initiate (for example,
creating clusters) runs only in your current default region.

To create or work with a cluster in a specific region, use the corresponding regional
service endpoint. For service endpoints, see [MemoryDB Multi-Region](multi-region.md "multi-region.md").

With MemoryDB Multi-Region, you can improve both availability and resiliency while also benefiting from low latency local reads and writes for Multi-Region applications. For information on working with MemoryDB Multi-Region, see [Supported Regions & endpoints](#supportedregions "#supportedregions").

## Locating your nodes

Any cluster that has at least one replica must be spread across AZs. The only way you can locate everything within a single AZ is with a cluster comprised of single-node shards.

By locating the nodes in different AZs, MemoryDB eliminates the chance that a failure,
such as a power outage, in one AZ will cause loss of availability.

- [Creating a MemoryDB cluster](getting-started.md#clusters.create "getting-started.md#clusters.create")
- [Modifying a MemoryDB cluster](clusters.md "clusters.md")

## Supported Regions & endpoints

MemoryDB is available in multiple AWS Regions. This means that you can launch MemoryDB clusters in locations that meet
your requirements. For example, you can launch in the AWS Region closest to your customers, or launch in a particular AWS Region to meet certain legal
requirements. In addition, as MemoryDB expands availability to a new AWS Region, MemoryDB supports the two most recent `MAJOR.MINOR` versions at that time for the new Region. For
more information on MemoryDB versions, see [Engine versions](engine-versions.md "engine-versions.md").

By default, the AWS SDKs, AWS CLI, MemoryDB API, and MemoryDB console reference the US-East (N. Virginia) Region. As MemoryDB expands availability to new regions, new endpoints for these
regions are also available to use in your HTTP requests, the AWS SDKs, AWS CLI, and the
console.

Each Region is designed to be completely isolated from the other Regions.
Within each region are multiple Availability Zones (AZ).
By launching your nodes in different AZs you achieve the greatest possible fault tolerance.
For more information on regions and Availability Zones, see [Choosing Regions and Availability Zones](regionsandazs.md "regionsandazs.md") at the beginning of this topic.

| Regions where MemoryDB is supported                 | Region Name/Region                          | Endpoint | Protocol |
| --------------------------------------------------- | ------------------------------------------- | -------- | -------- |
| US East (Ohio) Region<br>`us-east-2`                | `memory-db.us-east-2.amazonaws.com`         | HTTPS    |
| US East (N. Virginia) Region<br>`us-east-1`         | `memory-db.us-east-1.amazonaws.com`         | HTTPS    |
| US West (N. California) Region<br>`us-west-1`       | `memory-db.us-west-1.amazonaws.com`         | HTTPS    |
| US West (Oregon) Region<br>`us-west-2`              | `memory-db.us-west-2.amazonaws.com`         | HTTPS    |
| Canada (Central) Region<br>`ca-central-1`           | `memory-db.ca-central-1.amazonaws.com`      | HTTPS    |
| Asia Pacific (Hong Kong) Region<br>`ap-east-1`      | `memory-db.ap-eastl-1.amazonaws.com`        | HTTPS    |
| Asia Pacific (Mumbai) Region<br>`ap-south-1`        | `memory-db.ap-south-1.amazonaws.com`        | HTTPS    |
| Asia Pacific (Tokyo) Region<br>`ap-northeast-1`     | `memory-db.ap-northeast-1.amazonaws.com`    | HTTPS    |
| Asia Pacific (Seoul) Region<br>`ap-northeast-2`     | `memory-db.ap-northeast-2.amazonaws.com`    | HTTPS    |
| Asia Pacific (Singapore) Region<br>`ap-southeast-1` | `memory-db.ap-southeast-1.amazonaws.com`    | HTTPS    |
| Asia Pacific (Sydney) Region<br>`ap-southeast-2`    | `memory-db.ap-southeast-2.amazonaws.com`    | HTTPS    |
| Europe (Frankfurt) Region<br>`eu-central-1`         | `memory-db.eu-central-1.amazonaws.com`      | HTTPS    |
| Europe (Ireland) Region<br>`eu-west-1`              | `memory-db.eu-west-1.amazonaws.com`         | HTTPS    |
| Europe (London) Region<br>`eu-west-2`               | `memory-db.eu-west-2.amazonaws.com`         | HTTPS    |
| EU (Paris) Region<br>`eu-west-3`                    | `memory-db.eu-west-3.amazonaws.com`         | HTTPS    |
| Europe (Stockholm) Region<br>`eu-north-1`           | `memory-db.eu-north-1.amazonaws.com`        | HTTPS    |
| Europe (Milan) Region<br>`eu-south-1`               | `memory-db.eu-south-1.amazonaws.com`        | HTTPS    |
| Europe (Spain) Region<br>`eu-south-2`               | `memory-db.eu-south-2.amazonaws.com`        | HTTPS    |
| South America (São Paulo) Region<br>`sa-east-1`     | `memory-db.sa-east-1.amazonaws.com`         | HTTPS    |
| China (Beijing) Region<br>`cn-north-1`              | `memory-db.cn-north-1.amazonaws.com.cn`     | HTTPS    |
| China (Ningxia) Region<br>`cn-northwest-1`          | `memory-db.cn-northwest-1.amazonaws.com.cn` | HTTPS    |

For a table of AWS products and services by region,
see [Products and services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/ "https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/").

For a table of supported Availability Zones within Regions, see [Subnets and subnet groups](subnetgroups.md "subnetgroups.md").
