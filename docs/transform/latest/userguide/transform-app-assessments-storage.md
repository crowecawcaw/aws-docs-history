

# Storage assessments
<a name="transform-app-assessments-storage"></a>

AWS Transform models your storage footprint and recommends AWS storage services and configurations based on your current storage usage and performance requirements. Storage attached to servers is right-sized alongside the compute recommendation, and AWS Transform also models detached storage across block, object, and file storage services.

## Storage data you provide
<a name="transform-app-assessments-storage-inputs"></a>

Every migration assessment includes the storage attached to your servers, priced on Amazon EBS. You don't need to provide anything beyond your server inventory for this estimate.

To assess detached storage, such as file shares, storage arrays, and object stores, provide one of the following:
+ An RVTools export, as an Excel file or a ZIP file of CSV files
+ NetApp Data Infrastructure Insights (DII) query exports, as a ZIP file of CSV files
+ The AWS Transform Assessment Data template, with the storage tabs filled in

For NetApp DII, the queries that you run depend on the storage that you want to assess. For NAS volumes, run the `Disk`, `Internal Volumes`, `Storage`, and `Share` queries. For SAN volumes, run the `Virtual Machines` and `Volumes` queries. Export the results of each set as a single ZIP file. Collect data for at least 7 days. To capture peaks such as batch runs or month-end jobs, collect for up to 30 days.

For more information about inventory formats, see [Uploading inventory data](transform-app-assessments.md#transform-app-assessments-upload-inventory).

## How storage is mapped to AWS services
<a name="transform-app-assessments-storage-mapping"></a>

AWS Transform chooses the target service from the type of storage that your data describes:
+ **File storage**—file servers and NAS arrays map to Amazon FSx for NetApp ONTAP.
+ **Block storage**—volumes attached to servers and virtual machines map to Amazon EBS.
+ **Object storage**—object and backup storage map to Amazon S3.

SAN volumes map by source. SAN volumes from NetApp DII data map to Amazon EBS, and SAN volumes from other sources map to Amazon FSx for NetApp ONTAP. NAS volumes from NetApp DII data map to Amazon FSx for NetApp ONTAP.

A storage assessment prices a single AWS Region. If your configuration specifies no Region, or more than one, the assessment stops with an error rather than returning an estimate. To compare Regions, create a scenario for each.

## Amazon EBS
<a name="transform-app-assessments-storage-ebs"></a>

AWS Transform recommends Amazon Elastic Block Store (Amazon EBS) volume types and configurations for the block storage attached to your migrated servers, based on your current capacity, IOPS, and throughput requirements. AWS Transform accounts for storage capacity, provisioned IOPS, and provisioned throughput when estimating cost. It chooses from the gp3, io2 Block Express, sc1, and st1 volume types.

AWS Transform prices two strategies so that you can compare them:
+ **Cost-optimized**—maps each source volume to one Amazon EBS volume of the most suitable type. Volumes that exceed gp3 limits for capacity, IOPS, or throughput use io2 Block Express.
+ **1-2-many**—splits a high-performance source volume across several gp3 volumes, up to six by default, so that gp3 can serve workloads that would otherwise need io2 Block Express. Each gp3 volume gets its own baseline IOPS and throughput. This strategy requires that your application can span multiple volumes.

For each volume attached to a virtual machine, AWS Transform adds a separate gp3 boot volume, 30 GiB by default. A virtual machine with several attached volumes is charged several boot volumes. When a volume reports provisioned capacity but no used capacity, AWS Transform assumes that 50 percent of the provisioned capacity is in use.

You can set a preferred volume type, such as gp3 for all application volumes, instead of letting AWS Transform choose. Volumes that don't fit the preferred type are still priced on it, and are flagged with a warning.

## Amazon S3
<a name="transform-app-assessments-storage-s3"></a>

AWS Transform models object storage on Amazon Simple Storage Service (Amazon S3). Use Amazon S3 modeling for unstructured data, backups, and archives that do not need to remain on block storage.

By default, AWS Transform distributes capacity across three instant-access storage classes: 20 percent to S3 Standard, 30 percent to S3 Standard-Infrequent Access, and 50 percent to S3 Glacier Instant Retrieval. You can change this allocation to match your access patterns. AWS Transform also adds 20 percent to the capacity by default, to account for metadata and versioning overhead.

## Amazon FSx for NetApp ONTAP
<a name="transform-app-assessments-storage-fsx-ontap"></a>

AWS Transform models file storage on Amazon FSx for NetApp ONTAP, including storage capacity, provisioned IOPS, and provisioned throughput. It assesses both NAS and SAN volumes, and prices both Single-AZ and Multi-AZ deployments.

The estimate includes the following:
+ **Storage tiers**—AWS Transform divides capacity between the SSD tier and the capacity pool tier. For NAS volumes, the split follows the IOPS that each volume needs per GiB of capacity. For SAN volumes, it follows the ratio of frequently accessed to infrequently accessed data.
+ **Provisioned IOPS**—the SSD tier includes 3 IOPS per GiB. AWS Transform prices any additional IOPS that your workloads need.
+ **Throughput**—AWS Transform sizes each file system to the next available throughput tier, with headroom. A requirement above the largest tier means that you need more than one file system.
+ **Data reduction**—for NetApp sources, AWS Transform uses the deduplication and compression savings that your arrays report. For other sources, it assumes 45 percent savings by default.

AWS Transform groups volumes by their source array. NAS and SAN volumes from the same array become separate file systems. The assessment also recommends a tiering policy for each file system, based on how much of its data is infrequently accessed.

## Idle volumes, exclusions, and defaults
<a name="transform-app-assessments-storage-exclusions"></a>

AWS Transform reports which storage it excluded or estimated, so that you can judge how far to rely on the result.
+ **Idle volumes**—on Amazon EBS, a volume is idle when it has no peak IOPS or no peak throughput. Idle volumes from NetApp sources map to sc1, and other idle volumes map to gp3 at minimal configuration. On Amazon FSx for NetApp ONTAP, a SAN volume is idle when both its peak IOPS and its peak throughput are zero, and it is placed almost entirely in the capacity pool tier. Idle volumes stay in the cost estimate and are flagged, because they are often candidates for archiving or decommissioning.
+ **Excluded storage**—storage that can't be mapped, such as a volume with no capacity data, or with requirements that exceed every supported volume type. This capacity is not in the cost estimate.
+ **Defaulted values**—missing fields, such as used capacity or peak performance, are filled with documented defaults, and the estimate may be less precise as a result.

When there is something to report, the assessment overview summarizes the excluded capacity and the count of excluded resources, with the reasons. A per-resource list records each error and warning, with the resource identifier, the reason, the impact, and a recommended next step. Errors mark capacity that is not in the estimate. Warnings mark resources that are in the estimate but had defaults applied or low-confidence data.

## Example prompts
<a name="transform-app-assessments-storage-prompts"></a>
+ "Estimate storage costs for my file servers on Amazon FSx for NetApp ONTAP"
+ "What is the impact of moving from gp3 to io2 volumes?"
+ "Model my backup and archive data on Amazon S3"
+ "Use gp3 for all of my application volumes"