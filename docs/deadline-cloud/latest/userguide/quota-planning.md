

# Plan quota increases as you scale your farm
<a name="quota-planning"></a>

Scaling up a farm can require increases to several related quotas. Review these quotas as a set and request any needed increases together. Quota limits fall into two groups: limits that block fleet creation or updates, and limits that appear only when jobs run. The second group includes license session limits, which are easy to miss because fleet setup can succeed even when a job can't get a license.

The following table maps what you're scaling to the quotas that apply and when each limit takes effect. For the full list of quotas and their current values in your account, see the table in [Service quotas and throttling for Deadline Cloud](deadline-cloud-quotas.md).


| What you're scaling | Quotas that apply | When the limit takes effect | 
| --- | --- | --- | 
| Compute in service-managed fleets | vCPU and GPU quotas. Each purchasing option (on-demand, spot, and wait and save) has its own quota. | Creating or updating the fleet fails. | 
| Worker storage in service-managed fleets | Root volume storage, and persistent volume storage if the fleet uses [Persistent storage](volumes.md). Both grow with the same worker count as the compute quotas. | Creating or updating the fleet fails. | 
| Workers in a farm | Workers for each farm. Counts workers in both service-managed and customer-managed fleets. | Creating or updating the fleet fails. | 
| Jobs that use usage-based licensing | License sessions for each license endpoint. | Tasks fail to get a license at render time. | 
| Compute in customer-managed fleets | Your Amazon Elastic Compute Cloud (Amazon EC2) quotas, because those workers run in your own account. | Instance launches fail in your account. | 

## Request related increases together
<a name="quota-planning-together"></a>

The compute and storage quotas grow with the same maximum worker count, so a fleet that needs a vCPU or GPU increase often needs a storage increase as well. If you request only the compute increase, creating the fleet fails again on the storage quota and you wait through a second request. When you plan an increase, review the following quotas as a set:
+ The vCPU or GPU quota for the fleet's purchasing option.
+ Root volume storage.
+ Persistent volume storage, if the fleet uses persistent volumes.
+ Workers for each farm.
+ License sessions for each license endpoint, if your jobs use usage-based licensing.

The Deadline Cloud console helps you catch these limits early. When a fleet configuration exceeds a quota, the create and edit fleet pages show a warning that names the quota, explains the calculation, and links to the request page.

Quotas apply for each AWS Region, so a farm in a new Region starts from the default values. Increase requests can take time to process, so request them ahead of a deadline rather than during one. To view your applied values and request increases, see [Service quotas and throttling for Deadline Cloud](deadline-cloud-quotas.md).

## How Deadline Cloud sizes a fleet against quotas
<a name="quota-planning-sizing"></a>

Deadline Cloud counts a fleet against the compute quotas at its worst case: the maximum worker count multiplied by the largest worker the configuration can launch. If the fleet allows specific instance types, the largest allowed instance type that fits the fleet's other capability ranges sets the size for each worker. Otherwise, the configured maximum vCPU or GPU count sets it. A fleet that sets neither is assumed to use the largest supported worker, so it can count far more vCPUs against your quota than its workers ever use.

Usage is then added up across all of your service-managed fleets in the Region. To reduce how much a fleet counts against your quotas, restrict its allowed instance types or narrow its vCPU, memory, and GPU ranges. For more information about fleet configuration, see [Deadline Cloud fleets](manage-fleets.md).

## License sessions appear only at render time
<a name="quota-planning-licenses"></a>

If your jobs use usage-based licensing, each worker that renders with a licensed product checks out a license session. Deadline Cloud doesn't check the license session quota when you create a fleet, so a fleet sized past it is created successfully. When the fleet scales up, workers beyond the limit start but can't get a license, and their tasks fail.

The license session quota applies only to usage-based licensing. If your workers check out licenses from your own license server, or run software that needs no license, the quota doesn't affect them. Customer-managed fleets usually bring their own licenses.

If your fleet can run more workers than the quota allows, request an increase or lower the fleet's maximum worker count. For a comparison of usage-based licensing and bringing your own licenses, see [Using software licenses with Deadline Cloud](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/license.html) in the *AWS Deadline Cloud Developer Guide*.