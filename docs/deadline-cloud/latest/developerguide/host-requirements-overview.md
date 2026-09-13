

# Host requirements and fleet capabilities
<a name="host-requirements-overview"></a>

Capabilities and host requirements are complements. A fleet's capabilities advertise what its workers support, and a step's host requirements state what the step needs. Three concepts explain how they interact:
+ **Requirements are matched to fleets, not to workers** – The scheduler compares a step's requirements against each fleet's declared capabilities. It never inspects individual workers.
+ **Capabilities schedule; only service-managed fleet capabilities also configure hardware** – On a service-managed fleet, the instance capabilities additionally determine which Amazon EC2 instance types launch. On a customer-managed fleet, capabilities are a self-reported declaration and don't change your machines.
+ **Requirements never provide hardware** – A host requirement filters which fleets can run the step. It doesn't launch larger instances or change auto scaling decisions.


| Mechanism | Where you set it | What it does | What it doesn't do | 
| --- | --- | --- | --- | 
| Fleet instance capabilities (service-managed fleet) | Fleet configuration (`instanceCapabilities`) | Configures the hardware: the set of Amazon EC2 instance types that can launch. Also advertises the fleet's capabilities for scheduling | Doesn't pick one size within the set – any instance type that satisfies the configuration can launch | 
| Fleet worker capabilities (customer-managed fleet) | Fleet configuration (`workerCapabilities`) | Advertises the fleet's capabilities for scheduling; a self-reported declaration of what every worker in the fleet provides | Doesn't configure or verify hardware – updating the declaration doesn't change your machines | 
| Step host requirements | Job template (`hostRequirements`) | States what the step needs; matched against fleet capabilities when the job is created to select compatible fleets | Doesn't launch larger instances, change auto scaling decisions, or match against individual workers | 
| Worker-advertised capabilities | Reported by the worker agent at startup | Records the hardware a worker reports, such as `amount.worker.memory`, for visibility and debugging | Not used for scheduling or hardware configuration | 

## Fleet configuration provides the hardware
<a name="host-requirements-overview-fleet-config"></a>

For a service-managed fleet, the `instanceCapabilities` configuration (memory, vCPUs, GPUs, and the allowed and excluded instance type lists) defines the set of instance types the fleet can launch. When the fleet scales out, any instance type in that set can launch, including the smallest. To guarantee a hardware floor, raise the configuration minimums, such as `memoryMiB.min`, or limit `allowedInstanceTypes`. For more information, see [Service-managed fleets](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/smf-manage.html) in the *Deadline Cloud User Guide*.

Service-managed instance capabilities are the only mechanism that configures hardware. On a customer-managed fleet, the `workerCapabilities` declaration is self-reported: it advertises the hardware that you state every worker in the fleet provides, and updating the declaration doesn't change your machines. For more information, see [Create a customer-managed fleet](create-a-cmf.md).

## Host requirements select a fleet
<a name="host-requirements-overview-select-fleet"></a>

When you create a job, the scheduler compares each step's `hostRequirements` against the capabilities of the fleets associated with the queue. A fleet that satisfies the requirements can run the step; if no fleet does, the step is marked `NOT_COMPATIBLE`.

Matching is fleet-level only. For example, if a step requires 16 GiB of memory and a fleet declares a memory capability of 8–32 GiB, the fleet is not compatible – even if a worker in that fleet has 32 GiB. The scheduler never inspects individual workers, so design fleets around guaranteed hardware tiers and let each step's requirements route it to the right fleet. For more information, see [Determine fleet compatibility](build-jobs-scheduling.md#jobs-scheduling-compatibility) and [Fleet design best practices](build-jobs-scheduling.md#jobs-scheduling-fleet-design).

## Worker capabilities are informational
<a name="host-requirements-overview-select-worker"></a>

Each worker reports the hardware it detected at startup, such as `amount.worker.memory`. These values are for visibility and debugging. The scheduler doesn't use them: compatibility comes from the fleet's declared capabilities, and hardware comes from the fleet configuration. In particular, a requirement such as `amount.worker.memory` doesn't cause a fleet to launch a larger instance. Treat the step requirement as a statement of need and the fleet configuration as the guarantee.

## Auto scaling counts tasks
<a name="host-requirements-overview-scaling"></a>

The auto scaler sizes a service-managed fleet based on two factors: the number of tasks ready for that fleet, and the fleet's minimum and maximum worker counts. It chooses how *many* workers to run; the fleet configuration determines what each worker is. For more information, see [Fleet scaling](build-jobs-scheduling.md#jobs-scheduling-scaling).

Host requirements are part of the Open Job Description specification. For the full field reference, see [Template Schemas](https://github.com/OpenJobDescription/openjd-specifications/wiki/2023-09-Template-Schemas) on the GitHub website.