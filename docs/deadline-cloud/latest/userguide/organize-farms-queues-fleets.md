# Organize your farms, queues, and fleets

You can start with a single farm that contains one queue and one fleet. As the number of
users and the variety of workloads in your AWS Deadline Cloud (Deadline Cloud) farm grow, it helps to
organize the work more deliberately: a queue for each team or project, a fleet for each
hardware type, or a separate farm for work that must remain isolated.

Three questions drive the design:

- **Who can see, submit, and manage which jobs?**
  Queues are the natural boundary for permissions and budgets.
- **Which hardware runs which jobs?** Fleets group
  workers by capability, and each job's host requirements route it to a fleet that
  can run it.
- **Does any of the work need to be strictly isolated from the
  rest?** For work that must not mix, such as work for different
  clients, create a separate farm for each workload. Separate farms are a hard
  security boundary.

## How queues, fleets, and farms divide the work

Queues and fleets have a many-to-many relationship. You can associate one queue with
several fleets, and one fleet with several queues. When a fleet serves multiple queues,
it divides its workers among them. For more information, see [Associate a queue and fleet](associate-a-queue-and-fleet.md "associate-a-queue-and-fleet.md").

When a queue has more than one fleet, each job's host requirements (such as GPUs,
vCPUs, memory, and operating system) determine which fleets can run it. You do not need
separate queues for GPU jobs and CPU jobs: associate one queue with a GPU fleet and a
CPU fleet, and a render that requires a GPU is scheduled only to the GPU fleet, while
jobs without GPU requirements can run on the CPU fleet. The Deadline Cloud integrated submitters
include host requirements settings, so artists can describe the hardware a job needs
without knowing which fleet provides it.

Queues are also where you control access and spending. You grant users an access
level on each queue separately, so a user can submit jobs to one queue while only
viewing another. You can also set a budget for each queue. For more information, see
[Managing users in Deadline Cloud](managing-users.md "managing-users.md") and [Control costs with a budget](using-budget-manager.md "using-budget-manager.md").

Queue permissions control who can see and manage jobs, but they don't fully isolate
the jobs themselves. Jobs from different queues that share a fleet run on the same
worker hosts, where they can share common resources such as caches of packages and
files. Separate farms are a hard security boundary: farms share no Deadline Cloud resources with
each other, unless you weaken the boundary yourself by sharing an external resource
such as an Amazon Simple Storage Service (Amazon S3) bucket. For more information, see [Isolate workloads with farms, fleets, and queues](farm-structure.md "farm-structure.md").

| Divide with | Best for separating                                                                                  | Considerations                                                                     |
| ----------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Queues      | Teams, shows, or departments that need their own job lists,<br>permissions, and budgets              | Jobs from queues that share a fleet run on the same worker<br>hosts                |
| Fleets      | Hardware and software environments, such as GPU workers,<br>CPU workers, or a customer-managed fleet | A fleet that serves multiple queues divides its workers among<br>them              |
| Farms       | Workloads that need a hard isolation boundary, such as<br>different vendors or clients               | Farms share nothing, so each farm needs its own queues,<br>fleets, and user grants |

## Common patterns

The following layouts cover most organizations. You can combine them, for example a
shared farm for your own teams alongside a separate farm for each vendor.

### One shared farm, one queue per team

Within a single organization, a shared farm with a queue for each team or
workload (such as a show at a studio, or a machine learning training pipeline) is
usually the right starting layout. Everyone sees the whole farm in one
view. You grant each team the contributor level on its own queue and the viewer
level elsewhere, so teams can follow all the work without changing each
other's jobs. Budgets track spending for each queue.

Associate the queues with shared fleets. Shared fleets keep utilization high and
keep workers warm, because a worker that finishes one team's job can pick up
another team's job without waiting for a new instance to start. The tradeoff is
that the teams share worker hosts, which is normally acceptable within one
organization's trust boundary. To add a queue, see [Create a queue](queues.md#create-queue "queues.md#create-queue").

### A farm for each vendor or client

When you work with outside vendors, or run work for multiple clients that must
not mix, create a separate farm for each one. Users granted access to one farm
can't see the others, and jobs in one farm can't run on another farm's fleets or
read its job attachments. Keep the boundary intact: don't share job attachment Amazon S3
buckets, fleets, or other resources across farms. To add a farm, see [Create a farm](farms.md#create-farm "farms.md#create-farm"). For the security details,
see [Isolate workloads with farms, fleets, and queues](farm-structure.md "farm-structure.md"). For the
end-to-end steps to bring a vendor onto your farm, see [Onboard users to your farm](onboarding.md "onboarding.md").

### A restricted fleet for sensitive content

To keep work under a security or privacy restriction on dedicated workers,
create a queue and a fleet for that work, and associate the fleet only with that
queue. Jobs are scheduled only to fleets associated with their queue, so a fleet
associated with a single queue runs that queue's jobs and no others. See [Associate a queue and fleet](associate-a-queue-and-fleet.md "associate-a-queue-and-fleet.md"). For work that must not share
anything with the rest of the studio, use a separate farm instead.

Complete the boundary around the restricted queue:

- Grant access only to approved users and groups. See [Managing users in Deadline Cloud](managing-users.md "managing-users.md").
- Use a dedicated job attachments Amazon S3 bucket or root prefix, with a
  queue role scoped to it. See [Secure job attachment and software buckets](job-attachment-queues.md "job-attachment-queues.md").
- Run jobs as an operating system user that no other queue uses. See
  [Run jobs as dedicated OS users](job-run-as-user.md "job-run-as-user.md").
- Limit who can change the fleet's queue–fleet associations. See
  [Policy to manage queue–fleet associations for a specific fleet](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-qfa "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-qfa").

For more information about the security considerations behind these steps, see
[Isolate workloads with farms, fleets, and queues](farm-structure.md "farm-structure.md").

### Separate queues for service-managed and customer-managed fleets

If your farm has both service-managed and customer-managed fleets, in most cases
create a separate queue for each fleet type. Jobs written for the two fleet types
usually assume different run environments. A queue for service-managed fleets
typically uses the conda queue environment to install applications for each job,
while jobs for a customer-managed fleet expect the software that you preinstalled
on your worker hosts. A job configured for one environment often fails on the
other. Keeping the queues separate also keeps each queue's environment settings
simple. For more information, see [Choose between service-managed and customer-managed fleets](fleet-types.md "fleet-types.md") and [Default conda queue environment](create-queue-environment.md#conda-queue-environment "create-queue-environment.md#conda-queue-environment").
