# Resource-aware scheduling

AWS Batch schedules jobs based on the vCPU, GPU and the memory availability in the Compute
Environment (CE) associated with the Job Queue (JQ). But sometimes, just the availability of
these CE resources doesn't guarantee that the job will run successfully since it might be dependent
on other required resources, so these jobs are cancelled or terminated. This results in inefficient
use of compute resources. To solve this issue, resource-aware scheduling can check the availability
of dependent, non-CE resources before it schedules the job to run on a CE.

AWS Batch resource-aware scheduling lets you schedule jobs based on consumable resources that
are needed to run your jobs– 3rd party license tokens, database access bandwidth, the need
to throttle calls to a third-party API, and so on. You specify the consumable resources which are
needed for a job to run, and Batch takes these resource dependencies into account when it schedules
a job. You can avoid making manual interventions to eliminate job failures and long waits
caused by a shortage of consumable resources. You can reduce the under-utilization of compute
resources by allocating only the jobs that have all the required resources available.

Resource-aware scheduling is available for both FIFO and Fair-share scheduling policies and
can be used with all compute platforms supported by Batch including EKS, ECS, and Fargate.
It can be used with Array jobs, Multi-node parallel (MNP) jobs, and with regular Batch jobs.

To configure resource-aware scheduling, you first specify all the consumable resources needed
to run your jobs, along with the total count available of each resource. Then, for each job that
requires a consumable resource, you specify the name and required quantities of each resource
needed. Batch keeps track of how many consumable resources are available for the jobs in your
job queues and makes sure that a job is scheduled to run only when all the required consumable
resources are available for the job to run successfully.

###### Topics

- [Create consumable resources](resource-aware-scheduling-how-to-create.md "resource-aware-scheduling-how-to-create.md")
- [Specify the resources needed to run a job](resource-aware-scheduling-how-to-for-jobs.md "resource-aware-scheduling-how-to-for-jobs.md")
- [Check how many resources are
  in-use and available](resource-aware-scheduling-how-to-check-resources-check-resources.md "resource-aware-scheduling-how-to-check-resources-check-resources.md")
- [Update the quantity of a
  resource while it is in use by jobs](resource-aware-scheduling-how-to-update-quantity.md "resource-aware-scheduling-how-to-update-quantity.md")
- [Find the jobs that require a
  specific consumable resource](resource-aware-scheduling-how-to-find-jobs.md "resource-aware-scheduling-how-to-find-jobs.md")
- [Delete a consumable resource](resource-aware-scheduling-how-to-delete.md "resource-aware-scheduling-how-to-delete.md")
