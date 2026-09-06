

# Using software licenses with Deadline Cloud
<a name="license"></a>

With Deadline Cloud, you can license the applications and renderers that process your jobs in two ways:
+ *Usage-based licensing (UBL)* – Deadline Cloud provides on-demand licenses for supported third-party applications and renderers, billed for the hours that your fleet uses them to process a job. There is no set number of licenses, so your fleet can scale as needed.
+ *Bring your own license (BYOL)* – your workers check out licenses from a license server that you run, so you can use your existing license agreements or software that UBL doesn't cover.

Both methods work on both fleet types. The setup difference is how workers reach the license source: service-managed fleet workers run in infrastructure that AWS manages, outside your VPC, so they reach your license server through a connectivity option that you configure. Customer-managed fleet workers run on your own compute and use your existing network.

The following table summarizes the options. The sections after the table describe each option and link to setup instructions.


| Licensing | Fleet type | How workers get a license | Setup | 
| --- | --- | --- | --- | 
| UBL | Service-managed | Automatic for supported products | None | 
| UBL | Customer-managed | License endpoint in your VPC, for a subset of UBL products | [Connect customer-managed fleets to a license endpoint](cmf-ubl.md) | 
| BYOL | Service-managed | Your license server, reached through a VPC resource endpoint, SSM port forwarding, or the internet | [Connect service-managed fleets to a custom license server](smf-byol.md) | 
| BYOL | Customer-managed | Your license server, over your existing network | Configure license environment variables on your workers | 

## Usage-based licensing
<a name="license-overview-ubl"></a>

UBL licenses cover processing jobs on workers. They don't license the interactive DCC applications on your workstations. For the list of supported products and the per-hour rate for each, see [AWS Deadline Cloud pricing](https://aws.amazon.com/deadline-cloud/pricing/).

On service-managed fleets, UBL is available with no setup: supported products are licensed automatically when they run on a worker. Deadline Cloud sets the license environment variables on each worker when the instance launches, before the worker agent starts and before any host configuration script runs. On customer-managed fleets, you create a *license endpoint* in your VPC to route license requests to Deadline Cloud, and a subset of the UBL products is available. For the product list and setup steps, see [Connect customer-managed fleets to a license endpoint](cmf-ubl.md).

## Bring your own license
<a name="license-overview-byol"></a>

With BYOL, workers request licenses from a license server that you run, the same way your on-premises render farm does. On a customer-managed fleet, your workers are on your own network, so you point each application at your license server with its usual environment variable or configuration setting.

Service-managed fleet workers run outside your VPC, so you connect them to your license server in one of three ways:
+ **VPC resource endpoint** – connect your fleet to a license server in your VPC through VPC Lattice. Workers reach the server using a private domain name. For more information, see [Connect VPC resources to your SMF with VPC resource endpoints](smf-vpc.md).
+ **SSM port forwarding** – a queue environment forwards license ports from each worker to an Amazon EC2 instance in your account that hosts your license server or acts as a proxy for it. For more information, see [Connect service-managed fleets to a custom license server](smf-byol.md).
+ **Internet** – workers connect directly to a license server that is reachable over the internet, such as a software vendor's cloud license service.

The license server doesn't have to be in the same VPC or account as the resource gateway or proxy instance. The gateway or proxy only needs network access to the server, for example through VPC peering, a transit gateway, or a VPN connection. With this approach, service-managed fleet workers can use license servers in a shared networking account.

Your license count doesn't limit how many workers Deadline Cloud starts. To keep concurrent tasks within your available seats, set up a limit. For more information, see [Create resource limits for jobs](build-job-limits.md) and the [Enforce fixed license limits with a Deadline Cloud submission hook](examples-license-limits-hook.md) sample. To turn off UBL entirely for a queue so that jobs only use your license server, see the [Disconnect Deadline Cloud usage-based licensing with a queue environment](examples-queue-env-disconnect-ubl.md) sample.

## Combining BYOL and UBL
<a name="license-overview-combine"></a>

You can list your license server ahead of the UBL endpoint in an application's license configuration so that workers consume your existing licenses first and fall back to UBL when those licenses run out. For more information, see [Combining BYOL and UBL](license-combine-byol-ubl.md).