# Run jobs as dedicated OS users

Each queue can specify an operating system (OS) user and its primary group, called the
job run as user. The worker agent runs every job process submitted to the queue as that OS
user, so the jobs inherit that user's OS permissions, including access to files and other
resources on the worker host.

Give the queue user the least-privilege OS permissions that the queue's workloads need.
A dedicated user for each queue keeps a job's files and processes separated from jobs in
other queues, from other installed software, and from other users with access to the
worker host.

The two fleet types handle the queue user differently:

- On a customer-managed fleet, you create the OS users on your worker hosts. Use a
  separate user for each queue unless the queues are in the same security
  boundary.
- On a service-managed fleet, the service manages the worker hosts, and all jobs
  run as a single OS user. The hosts are dedicated to your account and run only jobs
  from the queues that you associate with the fleet, so you separate queues by giving
  them separate fleets instead of separate users.
  When a queue doesn't specify a user, its jobs run as the worker agent user. The worker
  agent user can impersonate (`sudo`) any queue user, so a queue without a user
  can escalate privileges to any other queue's user and data.
