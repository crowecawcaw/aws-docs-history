# Choose between service-managed and customer-managed fleets

When you set up compute for your farm, the first decision is who manages the workers:
Deadline Cloud or you. A _service-managed fleet_ (SMF) is a fleet of Amazon Elastic Compute Cloud
(Amazon EC2) workers that Deadline Cloud provisions, scales, and maintains for you. A
_customer-managed fleet_ (CMF) is a fleet of workers that you
provision and operate yourself. Workers can be Amazon EC2 instances, on-premises machines, or
hardware in a co-located data center.

The following table compares the fleet types. The sections after the table link to
detailed instructions for each.

| Consideration        | Service-managed fleet                                                                                                              | Customer-managed fleet                                                                                                                                         |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Worker management    | Deadline Cloud provisions, scales, and decommissions Amazon EC2 workers for<br>you                                                 | You provision, operate, and decommission the workers                                                                                                           |
| Where workers run    | Amazon EC2 instances that Deadline Cloud manages                                                                                   | Amazon EC2 instances, on-premises machines, or a co-located data<br>center                                                                                     |
| Operating systems    | Linux (AL2023) or Windows Server 2022                                                                                              | Linux, Windows, or macOS                                                                                                                                       |
| Software environment | Worker image maintained by Deadline Cloud; add software with the conda<br>queue environment or host configuration scripts          | You build the worker image and install the software and drivers<br>you need                                                                                    |
| Scaling              | Automatic, based on your fleet's auto scaling<br>configuration                                                                     | You set up auto scaling for Amazon EC2 workers; on-premises capacity is<br>fixed                                                                               |
| Licensing            | For supported software, usage-based licensing (UBL) activates<br>automatically; you can also connect to your own license<br>server | Bring your own licenses, or set up a license endpoint for<br>UBL                                                                                               |
| Storage              | Job attachments, persistent storage volumes, and VPC resource<br>endpoints to reach shared storage in your VPC                     | Any storage you configure, such as your existing network file<br>system                                                                                        |
| Cost model           | Pay for workers only while they process jobs                                                                                       | You pay for your own compute (Amazon EC2 instances or on-premises<br>hardware). Deadline Cloud also charges for each hour a worker is connected to<br>the farm |

You don't have to choose only one fleet type. A farm can contain both, for example
on-premises workers in a CMF plus cloud capacity in an SMF for peak demand. For more
information, see [Extend your
on-premises render farm to the cloud](../developerguide/hybrid-rendering.md "../developerguide/hybrid-rendering.md") in the _Deadline Cloud Developer
Guide_.

## Service-managed fleets

With a service-managed fleet, you choose the instance capabilities, operating system,
and market option (spot, on-demand, or wait-and-save), and Deadline Cloud handles the rest.
Associate the fleet with a queue that uses the default
conda queue environment. Deadline Cloud then configures the workers with packages for supported
digital content creation (DCC) applications and renderers.

For more information, see the following:

- [Service-managed fleets](smf-manage.md "smf-manage.md")
- [Software licensing for service-managed fleets](smf-licensing.md "smf-licensing.md")
- [Persistent storage for service-managed fleets](volumes.md "volumes.md")
- [Understand the cost model for service-managed fleets](cost-model-smf.md "cost-model-smf.md")
- [Configure and use Deadline Cloud
  service-managed fleets](../developerguide/smf.md "../developerguide/smf.md") in the _Deadline Cloud Developer
  Guide_

## Customer-managed fleets

With a customer-managed fleet, you run the workers and Deadline Cloud acts as the repository
and scheduler for your jobs. Each worker runs the Deadline Cloud worker agent and needs access
to the Deadline Cloud service endpoint.

For more information, see the following:

- [Create and use
  Deadline Cloud customer-managed fleets](../developerguide/manage-cmf.md "../developerguide/manage-cmf.md") in the _Deadline Cloud Developer
  Guide_
- [Set up
  auto scaling for customer-managed fleets](../developerguide/create-auto-scaling.md "../developerguide/create-auto-scaling.md") in the _Deadline Cloud
  Developer Guide_
- [Connect
  customer-managed fleets to a license endpoint](../developerguide/cmf-ubl.md "../developerguide/cmf-ubl.md") in the
  _Deadline Cloud Developer Guide_
