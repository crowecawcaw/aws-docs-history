

# Choose between service-managed and customer-managed fleets
<a name="fleet-types"></a>

When you set up compute for your farm, the first decision is who manages the workers: Deadline Cloud or you. A *service-managed fleet* (SMF) is a fleet of Amazon Elastic Compute Cloud (Amazon EC2) workers that Deadline Cloud provisions, scales, and maintains for you. A *customer-managed fleet* (CMF) is a fleet of workers that you provision and operate yourself. Workers can be Amazon EC2 instances, on-premises machines, or hardware in a co-located data center.

The following table compares the fleet types. The sections after the table link to detailed instructions for each.


| Consideration | Service-managed fleet | Customer-managed fleet | 
| --- | --- | --- | 
| Worker management | Deadline Cloud provisions, scales, and decommissions Amazon EC2 workers for you | You provision, operate, and decommission the workers | 
| Where workers run | Amazon EC2 instances that Deadline Cloud manages | Amazon EC2 instances, on-premises machines, or a co-located data center | 
| Operating systems | Linux (AL2023) or Windows Server 2022 | Linux, Windows, or macOS | 
| Software environment | Worker image maintained by Deadline Cloud; add software with the conda queue environment or host configuration scripts | You build the worker image and install the software and drivers you need | 
| Scaling | Automatic, based on your fleet's auto scaling configuration | You set up auto scaling for Amazon EC2 workers; on-premises capacity is fixed | 
| Licensing | For supported software, usage-based licensing (UBL) activates automatically; you can also connect to your own license server | Bring your own licenses, or set up a license endpoint for UBL | 
| Storage | Job attachments, persistent storage volumes, and VPC resource endpoints to reach shared storage in your VPC | Any storage you configure, such as your existing network file system | 
| Cost model | Pay for workers only while they process jobs | You pay for your own compute (Amazon EC2 instances or on-premises hardware). Deadline Cloud also charges for each hour a worker is connected to the farm | 

You don't have to choose only one fleet type. A farm can contain both, for example on-premises workers in a CMF plus cloud capacity in an SMF for peak demand. For more information, see [Extend your on-premises render farm to the cloud](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/hybrid-rendering.html) in the *Deadline Cloud Developer Guide*.

## Service-managed fleets
<a name="fleet-types-smf"></a>

With a service-managed fleet, you choose the instance capabilities, operating system, and market option (spot, on-demand, or wait-and-save), and Deadline Cloud handles the rest. Associate the fleet with a queue that uses the default conda queue environment. Deadline Cloud then configures the workers with packages for supported digital content creation (DCC) applications and renderers.

For more information, see the following:
+ [Service-managed fleets](smf-manage.md)
+ [Software licensing for service-managed fleets](smf-licensing.md)
+ [Persistent storage for service-managed fleets](volumes.md)
+ [Understand the cost model for service-managed fleets](cost-model-smf.md)
+ [Configure and use Deadline Cloud service-managed fleets](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/smf.html) in the *Deadline Cloud Developer Guide*

## Customer-managed fleets
<a name="fleet-types-cmf"></a>

With a customer-managed fleet, you run the workers and Deadline Cloud acts as the repository and scheduler for your jobs. Each worker runs the Deadline Cloud worker agent and needs access to the Deadline Cloud service endpoint.

For more information, see the following:
+ [Create and use Deadline Cloud customer-managed fleets](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/manage-cmf.html) in the *Deadline Cloud Developer Guide*
+ [Set up auto scaling for customer-managed fleets](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/create-auto-scaling.html) in the *Deadline Cloud Developer Guide*
+ [Connect customer-managed fleets to a license endpoint](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/cmf-ubl.html) in the *Deadline Cloud Developer Guide*