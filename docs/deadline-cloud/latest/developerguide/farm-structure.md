

# Isolate workloads with farms, fleets, and queues
<a name="farm-structure"></a>

You can arrange Deadline Cloud farms, fleets, and queues many ways. The arrangement you choose sets the isolation boundaries between your workloads, so decide how much separation your teams, shows, or clients need before you build.

Two facts about fleets drive the decision:
+ When a fleet is associated with more than one queue, jobs from all of those queues run on the same worker hosts. After a job runs, data can remain on the host, such as files in a temporary directory or the queue user's home directory, and a job can leave processes running that later jobs can observe.

  Some of that data remains by design. A job can cache data under the job user's home directory so that later sessions reuse it. For example, the conda queue environment caches downloaded packages there. On a service-managed fleet, all jobs run as one user, so every queue on the fleet shares those caches. Cached data remains until the worker shuts down, or across worker replacement when the fleet uses persistent storage. For more information, see [Sessions](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/build-jobs-scheduling.html#jobs-scheduling-sessions) in the *Deadline Cloud Developer Guide* and [Persistent storage](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/volumes.html) in the *Deadline Cloud User Guide*.
+ Worker hosts run jobs as an operating system user. On a customer-managed fleet, you can give each queue its own user, so queues can share a fleet while their jobs' files and processes stay separated. On a service-managed fleet, all jobs run as a single user, so give queues that need separation their own fleets. In both cases, the hosts run only jobs from queues in your farm.

With those facts in mind, choose the arrangement that fits your isolation needs:
+ **Separate farms** – A farm doesn't share Deadline Cloud resources such as fleets, queues, and storage profiles with other farms, so separate farms give workloads the strongest separation. The tradeoff is more resources to set up and manage, and worker capacity that one farm can't lend to another. Sharing external AWS resources, such as an Amazon S3 bucket, between farms weakens the boundary, so give each farm its own.
+ **One farm, a fleet for each queue** – Queues that need separation from each other each get their own fleet, so their jobs never share worker hosts. You keep a single farm to manage, and monitor users can be scoped to each queue. For more information about scoping users, see [Managing users](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/managing-users.html) in the *Deadline Cloud User Guide*. The tradeoff is partitioned capacity: idle workers in one fleet can't pick up another queue's jobs.
+ **One farm, queues sharing fleets** – Sharing fleets gives you the simplest setup and the best worker utilization. Because the queues share worker hosts, treat all queues that share a fleet as one security boundary. On a customer-managed fleet you can also give each queue a distinct operating system user to separate job processes and files from each other.

Whichever arrangement you choose, keep resource sharing within a security boundary:
+ Share an Amazon S3 bucket and root prefix for job attachments only between queues in the same security boundary. For more information, see [Secure job attachment and software buckets](job-attachment-queues.md).
+ Share an operating system user only between queues in the same security boundary. For more information, see [Run jobs as dedicated OS users](job-run-as-user.md).
+ Apply the same boundary to any other AWS resources that you integrate into the farm, such as shared file systems.