

# Understand estimated and actual costs for Deadline Cloud
<a name="cost-management"></a>

AWS Deadline Cloud budgets and the usage explorer estimate costs for your jobs. The estimates don't guarantee the amount that you owe for Deadline Cloud or other AWS services. Your actual bill can differ because of calculation limitations and charges from connected AWS services.

## Why estimates differ from actual costs
<a name="cost-estimate-differences"></a>

The estimates in the usage explorer and budgets might differ from your actual costs for the following reasons:
+ Customer-owned resources – The tools don't calculate the actual cost of resources that you provide from AWS, on-premises infrastructure, or another cloud provider.
+ Idle workers – The estimate doesn't include time when a worker has an `IDLE` status. Idle time can occur when a fleet has a minimum worker count greater than zero or while workers transition between jobs.
+ Worker start and stop time – The estimate doesn't include the time that workers spend starting or transitioning from `IDLE` to `STOPPING` and then to `STOPPED`.
+ Promotional credits, discounts, and custom pricing agreements – The tools don't automatically account for private pricing agreements or other discounts. Use the [Adjust usage explorer and budget estimates with the cost scale factor](using-usage-explorer.md#cost-scale-factor) to align displayed estimates with your organization's pricing.
+ Storage and connected services – The estimate doesn't include asset storage or charges from connected AWS services. The following table identifies common charges.
+ Price changes – The tools use the most recent publicly available prices, but a delay can occur after a price changes.
+ Taxes – The estimate doesn't include taxes applied to your purchase of the service.
+ Rounding – The tools round pricing and usage data during calculations.
+ Currency conversion – Estimates use U.S. dollars. Exchange-rate changes affect values that you convert to another currency.
+ Pre-purchased licenses – The tools can't account for licenses that you provide. For more information, see [Software licensing for service-managed fleets](smf-licensing.md).

## Costs incurred alongside Deadline Cloud
<a name="costs-alongside-deadline-cloud"></a><a name="cost-management-best-practices"></a>

Using Deadline Cloud creates charges from other AWS services, such as storing job attachments in Amazon S3 and collecting task logs in CloudWatch Logs. These charges aren't reflected in Deadline Cloud budgets or the usage explorer. They appear on your AWS bill as the underlying service, based on your usage of that service.

To track detailed costs across Deadline Cloud and the other AWS services that you use with it, activate [AWS cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html).

**Note**  
The table lists common connected-service costs, but it isn't exhaustive. The final cost of using Deadline Cloud depends on your configuration, the amount of work that you process, and the AWS Region where you run your jobs. The practices in the following sections are guidelines and might not significantly reduce costs.

The following table maps each cost to when you incur it and where it appears on your bill.


| Cost | When you incur it | Appears on your bill as | 
| --- | --- | --- | 
| [Storage costs](#costs-storage) | When you submit jobs that upload job attachments, and for as long as assets, job attachments, output, and exported logs stay stored. | [Amazon Simple Storage Service](https://aws.amazon.com/s3/pricing/) | 
| [Compute costs](#costs-compute) | While workers in an EC2-backed customer-managed fleet run on instances that you own. | [Amazon Elastic Compute Cloud](https://aws.amazon.com/ec2/pricing/) | 
| [Logging costs](#costs-logging) | When workers send task and worker logs, and for as long as those logs stay stored. | [Amazon CloudWatch Logs](https://aws.amazon.com/cloudwatch/pricing/) | 
| [PrivateLink costs](#costs-endpoints) | Per hour, for each PrivateLink interface endpoint or usage-based licensing endpoint, for as long as the endpoint exists—even when it's idle. | [AWS PrivateLink](https://aws.amazon.com/privatelink/pricing/) and [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/pricing/) | 
| [Service-managed fleet VPC connection costs](#costs-smf-vpc) | While resources in your VPC are connected to a service-managed fleet, and for the traffic that flows through the connection. | [VPC Lattice](https://aws.amazon.com/vpc-lattice/pricing/) | 
| [Encryption key costs](#costs-encryption) | When you encrypt your farm with a customer managed key, based on how the key is used. The default AWS owned key is free. | [AWS Key Management Service](https://aws.amazon.com/kms/pricing/) | 

### Storage costs
<a name="costs-storage"></a><a name="best-practice-s3"></a>

Deadline Cloud uses Amazon S3 to store assets for processing, job attachments, output, and logs that you export from CloudWatch Logs. You incur storage charges when jobs upload attachments and output, when you export logs, and for as long as the files stay stored. These charges appear on your bill as [Amazon Simple Storage Service](https://aws.amazon.com/s3/pricing/).

Job attachments use content-addressable storage. If an unchanged file is already available, Deadline Cloud doesn't upload it again. Content-addressable storage limits repeated uploads and storage growth during iterative workflows. For more information, see [Use job attachments to share files](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/build-jobs-attachments.html) in the *Deadline Cloud Developer Guide*.

To reduce storage costs, reduce the amount of data that you store:
+ Only store assets that are currently in use or that will be used shortly. 
+ Use an [S3 Lifecycle configuration](https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-configuration-examples.html) to automatically delete unused files from an S3 bucket.

### Compute costs
<a name="costs-compute"></a><a name="best-practice-ec2"></a>

If your customer-managed fleet uses Amazon EC2 instances, those instances appear on your bill as [Amazon Elastic Compute Cloud](https://aws.amazon.com/ec2/pricing/) for as long as they run. If your workers run on premises, in a co-location facility, or with another cloud provider, you are responsible for the costs of operating that infrastructure. Those costs aren't tracked by the Deadline Cloud cost management tools.

Compute for service-managed fleets is billed at [AWS Deadline Cloud pricing](https://aws.amazon.com/deadline-cloud/pricing/) rates and is tracked by the Deadline Cloud cost management tools.

To reduce compute costs for service-managed fleets and EC2-backed customer-managed fleets:
+ For service-managed fleets, you can choose to have one or more instances available at all times by setting the minimum worker count for the fleet. When you set the minimum worker count above 0, the fleet always has this many workers running. With this setting, you can reduce the time it takes for Deadline Cloud to start processing jobs. However, AWS charges you for the instance's idle time while it waits for work.
+ For service-managed fleets, set a maximum size for the fleet. This setting limits the number of instances that a fleet can auto scale to. Fleets won't grow past this size even if there are more jobs waiting to be processed. 
+ Choose Amazon EC2 instance types that match your workload. Smaller instances cost less per minute, but might take longer to complete a job. Conversely, a larger instance costs more per minute, but can reduce the time to complete a job. Understanding the demands that your jobs place on an instance can help reduce your costs.
+ When possible, use Amazon EC2 Spot capacity. Spot capacity costs less than On-Demand capacity, but it can be interrupted. AWS charges for On-Demand instances by the second, and they are not interrupted.

For an overview of the controls that cap peak compute, see [Control spending and capacity](manage-costs.md#cost-concurrency-controls).

### Logging costs
<a name="costs-logging"></a>

Deadline Cloud sends worker and task logs to CloudWatch Logs. You incur charges to collect logs while workers run tasks, and to store and analyze those logs afterward. These charges appear on your bill as [Amazon CloudWatch Logs](https://aws.amazon.com/cloudwatch/pricing/).

When you create a queue or fleet, Deadline Cloud creates a CloudWatch Logs log group with the following names:
+ `/aws/deadline/{{<FARM_ID>}}/{{<FLEET_ID>}}`
+ `/aws/deadline/{{<FARM_ID>}}/{{<QUEUE_ID>}}`

To reduce logging costs, log only the minimum amount of data required to monitor your tasks. By default, these logs never expire. You can adjust the retention policy of log groups to remove old logs and help reduce storage costs. You can also export logs to Amazon S3. Amazon S3 storage costs are lower than those for CloudWatch. For more information, see [Exporting log data to Amazon S3](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/S3Export.html).

### PrivateLink costs
<a name="costs-endpoints"></a><a name="best-practice-privateline"></a>

Two optional Deadline Cloud configurations create VPC endpoints in your account. You incur an hourly charge for each endpoint, for as long as it exists—even when it's idle. These charges appear on your bill as [AWS PrivateLink](https://aws.amazon.com/privatelink/pricing/) and [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/pricing/).
+ You can use AWS PrivateLink to create a connection between your VPC and Deadline Cloud using an interface endpoint. When you create a connection, you can call all of the Deadline Cloud API actions. AWS charges you per hour for each endpoint that you create. If you use PrivateLink, you must create at least three endpoints. Depending on your configuration, you might need up to five.
+ <a name="best-practice-vpc"></a>When you use usage-based licensing for your customer-managed fleet, you create a Deadline Cloud license endpoint, which is a Amazon VPC endpoint created in your account.

To reduce these costs, remove endpoints when you are not using them. For example, remove license endpoints when you are not using usage-based licenses.

These endpoints are separate from the VPC resource endpoints that connect a service-managed fleet to your VPC. For those costs, see [Service-managed fleet VPC connection costs](#costs-smf-vpc).

### Service-managed fleet VPC connection costs
<a name="costs-smf-vpc"></a>

You can connect resources in your VPC, such as file systems and license servers, to a service-managed fleet with VPC resource endpoints. The connection uses VPC Lattice and a resource gateway that you create in your account. You incur charges while the resource gateway exists and for the traffic that flows through the connection. These charges appear on your bill as [VPC Lattice](https://aws.amazon.com/vpc-lattice/pricing/). Connections between Availability Zones carry no additional charge.

To reduce these costs, remove the resource gateway and resource configuration when you are no longer connecting VPC resources to your fleet.

For more information, see [Connect VPC resources to your SMF with VPC resource endpoints](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/smf-vpc.html) in the *Deadline Cloud Developer Guide*.

### Encryption key costs
<a name="costs-encryption"></a><a name="best-practice-kms"></a>

By default, Deadline Cloud encrypts your data with an AWS owned key. You are not charged for this key.

You might choose to use a customer managed key to encrypt your data. When you use your own key, you incur charges based on how your key is used. If you use an existing key, the additional use is an incremental cost. These charges appear on your bill as [AWS Key Management Service](https://aws.amazon.com/kms/pricing/).