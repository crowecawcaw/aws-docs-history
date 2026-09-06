

# Run jobs as dedicated OS users
<a name="job-run-as-user"></a>

Each queue can specify an operating system (OS) user and its primary group, called the job run as user. The worker agent runs every job process submitted to the queue as that OS user, so the jobs inherit that user's OS permissions, including access to files and other resources on the worker host.

Give the queue user the least-privilege OS permissions that the queue's workloads need. A dedicated user for each queue keeps a job's files and processes separated from jobs in other queues, from other installed software, and from other users with access to the worker host.

The two fleet types handle the queue user differently:
+ On a customer-managed fleet, you create the OS users on your worker hosts. Use a separate user for each queue unless the queues are in the same security boundary.
+ On a service-managed fleet, the service manages the worker hosts, and all jobs run as a single OS user. The hosts are dedicated to your account and run only jobs from the queues that you associate with the fleet, so you separate queues by giving them separate fleets instead of separate users.

When a queue doesn't specify a user, its jobs run as the worker agent user. The worker agent user can impersonate (`sudo`) any queue user, so a queue without a user can escalate privileges to any other queue's user and data.

On a customer-managed fleet, the worker agent enforces the boundary between queue users with operating system permissions. The agent creates each session's working directory so that only the agent user and the job user's primary group can access it. The agent also stores each queue's role credentials in a queue-specific directory with the same access restriction. When each queue has its own user and primary group, a job can't read another queue's session files or AWS credentials.

Standard operating system user permissions on a shared kernel separate queue users on a shared worker host. Give workloads that require stronger separation, such as virtual machine isolation, their own fleets.