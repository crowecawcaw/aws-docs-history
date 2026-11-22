

# Global rendering across AWS Regions

AWS Deadline Cloud (Deadline Cloud) is available in a subset of AWS Regions. For the current list, see [Deadline Cloud endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/deadlinecloud.html) in the *AWS General Reference*. A team that spans countries can render with Deadline Cloud even when some locations are far from a supported Region.

The following facts control a multi-Region deployment:
+ A farm is a regional resource. Its queues, fleets, and jobs are in one Region.
+ Service-managed fleet workers render in the farm's Region. Submitters, the monitor, and customer-managed fleet workers connect to a farm from any location.
+ Distance affects only the interactions that cross it: asset uploads, output downloads, file transfers to customer-managed fleet workers, monitor responsiveness, and sign-in.

## How components map to Regions
<a name="multi-region-components"></a>

The following diagram shows a deployment with two farms in different Regions, a single AWS IAM Identity Center (IAM Identity Center) instance, and users and compute in locations of their own.

![Diagram of a Deadline Cloud deployment across two AWS Regions, Region A and Region B. User workstations at customer sites sign in through a single AWS IAM Identity Center instance in Region A (flow 1). In each Region, a farm holds queues and a service-managed fleet, and a job attachments bucket is next to the farm. The user workstations connect to the queues in both farms (flow 2) and to the bucket in both Regions (flow 3). Customer-managed fleet workers on customer compute connect to the queues in both farms (flow 4) and to the bucket in both Regions (flow 5). In each farm, the service-managed fleet connects to the queues and to the bucket in its Region.](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/images/multi-region.png)


Solid lines in the diagram represent data flow, and the dashed line represents authentication. The numbered flows show the interactions that cross from your locations into a Region:

1. Workstations run submitters and the AWS Deadline Cloud monitor, and sign in through your IAM Identity Center instance.

1. Workstations submit jobs to a queue in a farm in any Region and monitor those jobs.

1. Workstations exchange job attachment files with the queue's Amazon Simple Storage Service (Amazon S3) bucket. Submitters upload input files, and you download job output after a job finishes.

1. Workers in a customer-managed fleet get their assignments from the queues that their fleet is associated with, in the farm's Region. The workers run on compute that you provide, in any location. Each fleet belongs to one farm, so to render for farms in two Regions on the same compute, create a customer-managed fleet in each farm.

1. Workers in a customer-managed fleet exchange job attachment files with the queue's bucket.

Inside each farm, workers in a service-managed fleet get their assignments from a queue and exchange job attachment files with the queue's bucket, all within the farm's Region.

The diagram reflects the following placement rules:


| Component | Region placement | 
| --- | --- | 
| Farm, queues, fleets, jobs | A farm is a regional resource. Its queues, fleets, and jobs are all in one Region. A farm can't span Regions. To render in more than one Region, create a farm in each Region. | 
| Job attachments bucket | An Amazon S3 bucket in your AWS account that a queue uses for job attachments. The bucket must be in the farm's Region for a queue that uses a service-managed fleet. | 
| Service-managed fleet workers | Always run in the farm's Region. | 
| Customer-managed fleet | You create the fleet in the farm, and you run its workers on compute that you provide. Worker hosts run anywhere with network access to the Deadline Cloud endpoints in the farm's Region, including your own data center and Amazon Elastic Compute Cloud (Amazon EC2) instances in other Regions. For more information, see [Worker host data flow for customer-managed fleets](cmf-network.md). | 
| Submitters and the CLI | Run anywhere. Submitting a job needs only network access to the Deadline Cloud endpoint in the farm's Region. | 
| Monitor and IAM Identity Center | One monitor displays farms in all Regions, except farms in other Regions that use a customer managed key. Your IAM Identity Center instance can be in a different commercial Region than your farms. For more information, see [Monitors and farms in multiple Regions](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/monitors-additional-regions.html) in the Deadline Cloud User Guide. | 

## Where distance matters
<a name="multi-region-latency"></a>

Rendering on a service-managed fleet runs inside the farm's Region, so the distance between your users and the farm affects only the interactions that cross that distance. The following table describes each interaction.


| Interaction | What crosses the distance | Effect of distance | 
| --- | --- | --- | 
| Job submission | API calls, plus a job attachments upload to Amazon S3 in the farm's Region. Assets upload when they change, and later submissions skip files that are already uploaded. | Round-trip latency adds little to a submission. Total upload time depends on throughput, which depends on your network path and is not determined by distance alone. | 
| Rendering on a service-managed fleet | Nothing. Workers, queues, and job data operate within the farm's Region. | None. | 
| Rendering on a customer-managed fleet | Workers download job attachment input files from Amazon S3 in the farm's Region and upload their output to it. | As with uploads from a workstation, transfer time depends on throughput between your compute and the farm's Region. For large assets, consider shared storage that is local to your workers instead of job attachments. For more information, see [Storage profiles and path mapping](storage-profiles-and-path-mapping.md). | 
| Worker scheduling | Workers in a customer-managed fleet connect to the farm's Region to get their assignments. | Polling is asynchronous and scheduling operates on the order of seconds, so distance between your compute and the farm's Region doesn't meaningfully change job start times. | 
| Output download | A download of job output from Amazon S3 in the farm's Region, either in the monitor or with the deadline job download-output command. | Round-trip latency adds little to a download. As with uploads, total download time depends on throughput, which depends on your network path and is not determined by distance alone. | 
| Monitoring | Each monitor operation makes requests to the farm's Region. | Browsing jobs and logs feels slower at a distance but remains responsive. | 
| Sign-in | Authentication requests travel to the IAM Identity Center Region during sign-in. | Distance adds time during sign-in. After sign-in, identity information is cached in the Region for most requests. | 

To evaluate a candidate Region, run a quick test before you commit to a layout: create a farm in that Region, submit a representative job from the location your users work from, browse the job in the monitor, and download its output.

## How Region choice affects data transfer costs
<a name="multi-region-data-transfer"></a>

Most data transfer charges come from data that leaves a Region. That data includes job output that you download and input files that workers outside the farm's Region download. AWS doesn't charge for uploads into AWS. Transfers between Amazon S3 and service-managed fleet workers in the farm's Region also carry no data transfer charge.

To choose a Region that keeps data transfer costs low, consider the following guidelines:
+ Create the farm in the Region where your assets are already stored in Amazon S3.
+ Estimate how much output your team downloads each month, and how much input your customer-managed fleet workers outside AWS download. Data transfer out rates are tiered and differ between Regions. Compare them on the [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/) page.
+ Compare service-managed fleet rates along with data transfer, because they can also differ between Regions. For more information, see [AWS Deadline Cloud pricing](https://aws.amazon.com/deadline-cloud/pricing/).
+ Run customer-managed fleet workers on Amazon EC2 instances in the farm's Region. For on-premises workers, read assets from shared storage on your network instead of downloading them from Amazon S3.

For more information about which transfers are charged and other ways to reduce data transfer costs, see [Data transfer costs](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/cost-management.html#costs-data-transfer) in the *Deadline Cloud User Guide*.

## Choose a deployment
<a name="multi-region-choose"></a>

Most teams use one of the following layouts:
+ **One farm in the closest Region** – The simplest layout and the right starting point for most teams. Create one farm in the supported Region closest to most of your team, and everyone submits to it, including locations without a local Deadline Cloud Region. All jobs, assets, and quotas live in one Region, and everyone shares the same queues and fleets.
+ **Farms in multiple Regions for instance availability** – When capacity in one Region is tight, especially for GPU instances, create farms in more than one Region. One monitor displays all of them unless they use customer managed keys, and users choose a farm at submit time, so they can submit to the Region with the most available instances.
+ **A farm in each Region for isolation** – Choose separate farms when data residency or compliance requirements call for keeping a production's assets in a specific Region, or when you want regional isolation so that each production's resources and identity data stay within one Region. For full regional isolation, keep each production's farm and monitor in the same Region as the IAM Identity Center instance that the production uses.

Quotas apply separately in each Region, so a multi-Region deployment needs quota increases in every Region that you use. Some defaults are sized for initial evaluation. For example, the default is 2 farms in each Region, and the G instance GPU quotas default to 0. Request increases before you scale up a production. For more information, see [Plan quota increases as you scale your farm](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/quota-planning.html) in the *Deadline Cloud User Guide*.