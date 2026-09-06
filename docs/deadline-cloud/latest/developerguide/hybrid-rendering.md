

# Extend your on-premises render farm to the cloud
<a name="hybrid-rendering"></a>

You already run a render farm on-premises, and you want extra capacity during peak demand without buying and maintaining more hardware. With AWS Deadline Cloud (Deadline Cloud), you can add cloud workers to the same farm as your on-premises workers and send jobs to either location. Sending overflow work to the cloud in periods of high demand is often called *cloud bursting*.

A hybrid farm combines two kinds of fleets in one farm:
+ Your existing on-premises workers run as a *customer-managed fleet* (CMF). You control the hosts, operating system, and software. A worker can be an on-premises server, a server in a co-location facility, or an Amazon Elastic Compute Cloud (Amazon EC2) instance. For more information, see [Create and use Deadline Cloud customer-managed fleets](manage-cmf.md).
+ Your cloud capacity runs as a *service-managed fleet* (SMF), where Deadline Cloud manages the worker hosts, scaling, and patching for you. You can also run cloud capacity as a customer-managed fleet of Amazon EC2 instances when you need more control. For more information, see [Configure and use Deadline Cloud service-managed fleets](smf.md).

Deadline Cloud sends work to your fleets through queues, so decide how to organize your queues before you extend your farm. Because service-managed fleets and customer-managed fleets install applications differently, you can give each fleet type its own queue or share one queue across both fleet types. For a comparison of the two approaches, see [Choose a queue strategy](#hybrid-environments).

Whichever queue strategy you choose, plan for each of the following layers so that your jobs run correctly on every fleet. The rest of this topic describes each layer and links to detailed instructions.

The following table summarizes how each layer differs across the three kinds of workers you can combine in a hybrid farm. Your on-premises workers and your cloud Amazon EC2 instances are both customer-managed fleets, but they differ in how they reach your data and network, so the table lists them separately.


| Layer | On-premises (customer-managed fleet) | Cloud customer-managed fleet (Amazon EC2) | Service-managed fleet | 
| --- | --- | --- | --- | 
| Worker hosts | You provision and manage your own hardware, operating system, and patching. | You provision and manage Amazon EC2 instances. | Deadline Cloud manages the hosts, operating system, and patching. | 
| Applications | Preinstall applications on your workers, or use a conda channel in Amazon S3. | Preinstall applications, bake them into an Amazon Machine Image (AMI), or use a conda channel in Amazon S3. | Automatically installs popular DCCs from the Deadline Cloud-managed conda channel. To provide custom applications, use host configuration scripts or your own conda channel in Amazon S3. For the list of supported applications, see [Supported software](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/supported-software.html). | 
| Licensing | Connect a license endpoint for UBL, or connect to your own license server for BYOL. | Connect a license endpoint for UBL, or connect to your own license server for BYOL. | UBL is configured automatically. For BYOL, forward the license ports to your server with SSM. | 
| Asset access | Use job attachments, or shared storage that your workers already mount. | Use job attachments, or shared storage in your VPC. | Use job attachments, or connect to shared storage in your VPC with VPC resource endpoints. | 
| Scaling and cost | Fixed capacity that you own. | Use an Amazon EC2 Auto Scaling group to grow and shrink capacity with demand. | Scales automatically between the minimum and maximum worker counts that you set. | 

## Distribute jobs across your fleets
<a name="hybrid-distribute"></a>

When you associate a queue with more than one fleet, Deadline Cloud distributes jobs across the fleets that are compatible with each job. The scheduler compares the host requirements of each step with the [worker capabilities](build-jobs-scheduling.md#jobs-scheduling-compatibility) that each fleet declares, and it runs the step on a fleet that meets those requirements. For more information, see [Schedule jobs in Deadline Cloud](build-jobs-scheduling.md).

To automatically balance capacity between fleets, you can use the capacity manager sample. It uses a Lambda function and EventBridge Scheduler to adjust fleet worker counts while holding a target total capacity. You can adapt the same pattern to shift capacity toward your cloud fleet during peak demand. For more information, see [Manage hybrid Wait and Save plus Spot fleet capacity with CloudFormation](examples-cfn-capacity-manager.md).

**Note**  
Deadline Cloud does not provide a built-in setting to prefer one fleet over another, such as filling your on-premises fleet before your cloud fleet. To steer specific work to a specific location, define distinct worker capabilities on each fleet, and then set matching host requirements on the steps that must run in that location. To approximate fleet prioritization automatically, use the capacity manager sample described in the preceding paragraph.

## Choose a queue strategy
<a name="hybrid-environments"></a>

Service-managed fleets and customer-managed fleets install and manage applications differently, so decide how to organize your queues before you associate fleets with them. On a service-managed fleet, the default conda queue environment automatically installs the conda packages that jobs request. Customer-managed fleets don't have the conda commands installed by default, so the same queue environment causes errors on your customer-managed workers.

You can resolve the difference in one of the following two ways:
+ **Use a separate queue for each fleet type (recommended)** – Associate your service-managed fleet with a queue that uses the default conda queue environment, and associate your customer-managed fleet with a separate queue that doesn't use it. Each fleet type gets the application setup it expects, and you avoid conda errors. You submit each job to the queue for the location where you want the job to run.
+ **Share one queue across both fleet types** – Associate both fleets with the same queue so that Deadline Cloud distributes each job to whichever location has available capacity, without changing where you submit the job. A shared queue takes more setup because you can't use the default conda queue environment. Instead, you provide applications in a way that works on both fleet types. Choose a shared queue when you want peak workloads to overflow to the cloud automatically.

To run applications on a shared queue, create your own conda channel in Amazon Simple Storage Service (Amazon S3) that both fleet types use, or install applications directly on your customer-managed workers and adjust the queue environment so that the applications appear on the job user's path. For more information, see [Create a conda channel using S3](configure-jobs-s3-channel.md) and [Configure jobs using queue environments](configure-jobs.md).

## License applications on both fleets
<a name="hybrid-licensing"></a>

Deadline Cloud provides usage-based licensing (UBL), and you can also bring your own license (BYOL). Both options work on cloud and on-premises workers. For an overview, see [Using software licenses with Deadline Cloud](license.md).
+ UBL is configured automatically on service-managed fleets. To use UBL on a customer-managed fleet, including on-premises workers, connect a license endpoint. For more information, see [Connect customer-managed fleets to a license endpoint](cmf-ubl.md).
+ To use your existing license server with a service-managed fleet, forward the license ports from the workers to your license server or proxy with Amazon EC2 Systems Manager (SSM). For more information, see [Connect service-managed fleets to a custom license server](smf-byol.md).
+ To use your existing licenses first and fall back to UBL when they are exhausted, combine BYOL and UBL. For more information, see [Combining BYOL and UBL](license-combine-byol-ubl.md).

## Give both fleets access to your assets
<a name="hybrid-assets"></a>

Both fleets need access to the data that your jobs read and write. Deadline Cloud supports two approaches, and you can use them together:
+ **Job attachments** – Deadline Cloud uploads the files that a job needs to Amazon S3 and downloads the output afterward. Job attachments require no shared storage setup and work with fleets of any size. If your data already resides on AWS, job attachments add another copy of your data, along with the associated transfer time and storage cost.
+ **Shared storage** – Your workers mount a shared file system that holds your assets. To simplify how your on-premises and cloud workers manage assets, you can connect your service-managed fleet workers to shared storage in your virtual private cloud (VPC) with VPC resource endpoints. Both fleet types then read and write the same files. For more information, see [Connect VPC resources to your SMF with VPC resource endpoints](smf-vpc.md).

Because your on-premises workstations and cloud workers can use different operating systems and file system layouts, use storage profiles to model each configuration. Storage profiles let Deadline Cloud map paths so that a worker can find the data no matter where a job is submitted. For more information, see [Storage profiles and path mapping](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/storage-profiles-and-path-mapping.html).

## Connect cloud workers to your network
<a name="hybrid-network"></a>

Cloud workers often need to reach resources that run in your VPC or on-premises network, such as shared file systems, license servers, and databases. With VPC resource endpoints for service-managed fleets, your workers can connect to these resources over a private connection that uses VPC Lattice. For more information, see [Connect VPC resources to your SMF with VPC resource endpoints](smf-vpc.md).

To mount a file system or configure other network access on a service-managed fleet worker, use a host configuration script. Host configuration scripts run with administrator privileges when a worker starts. For more information, see [Run host configuration scripts with administrator privileges](smf-admin.md).

**Note**  
Traffic through a VPC resource endpoint uses Network Address Translation (NAT), which is not compatible with all resources. For example, Microsoft Active Directory cannot connect over NAT.

## Match applications to each fleet type
<a name="hybrid-applications"></a>

Confirm that each digital content creation (DCC) application your jobs use can run on both fleet types. On service-managed fleets, the Deadline Cloud-managed conda channel provides popular DCCs automatically. For applications that the channel doesn't provide, or for customer-managed workers that can't use the channel, package the applications yourself as described in [Choose a queue strategy](#hybrid-environments). For the list of supported applications, see [Supported software](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/supported-software.html) in the *AWS Deadline Cloud User Guide*.

## Control cloud costs
<a name="hybrid-costs"></a>

To pay for cloud capacity only during peak demand, scale your cloud fleet down when it is idle. Service-managed fleets scale automatically between the minimum and maximum worker counts that you set. For a customer-managed fleet of Amazon EC2 instances, you can configure auto scaling so that the fleet grows and shrinks with demand. For more information, see [Create fleet infrastructure with an Amazon EC2 Auto Scaling group](create-auto-scaling.md).

## Related resources
<a name="hybrid-related"></a>

For guidance on designing an end-to-end Deadline Cloud workflow across job submission, application management, licensing, asset access, and worker infrastructure, see [Deadline Cloud Architecture Guidance](architecture-guidance.md).

For runnable examples, including a reference template that connects a shared file system to a service-managed fleet, see the [deadline-cloud-samples](https://github.com/aws-deadline/deadline-cloud-samples) repository on the GitHub website.