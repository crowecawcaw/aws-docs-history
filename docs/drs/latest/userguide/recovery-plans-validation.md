# Validation that runs before a server is recovered

AWS Elastic Disaster Recovery validates the source servers in a plan twice: once for the whole plan when
an execution starts, and again for the servers in a server step at the moment that step
begins. The checks are the same as the ones that run when you recover a source server on
its own.

A server fails validation for any of the following reasons:

- The source server no longer exists in the account, for example because it was
  deleted after it was added to the plan.
- The server has no consistent recovery point yet. This is the check that
  catches a server whose initial sync has not finished, and a server whose
  replication has never produced a usable snapshot.
- Another job is already running for the server. A server that is in the middle
  of a recovery, drill, or other operation cannot be recovered again until that
  job finishes.
- The server is in a lifecycle state that cannot be recovered, such as
  disconnected, stopped, or archived.
- The server's disks are missing volume attributes, or those attributes are
  still pending. This affects servers that need marketplace license
  information.
- The server's launch template conflicts with the server. For example, a Windows
  server using its own license is not set to host tenancy, or the instance type
  does not support the server's boot mode.
- A recovery point that you pinned for the server no longer exists.
- The same source server appears more than once in the request.

###### Important

Validation is all or nothing, and impact levels do not apply to it. If any server
in the plan fails the validation that runs when the execution starts, the whole
execution fails. AWS Elastic Disaster Recovery then recovers no servers at all, not even the servers
that you marked **Optional**. If any server fails the
revalidation at the start of a server step, that whole step fails, again regardless
of impact level. AWS Elastic Disaster Recovery recovers none of the servers in that step.

Before you run a plan in recovery mode, confirm that every server in it shows a
healthy replication state and has recovery points available. Running the plan as a drill
first is the most reliable way to find these problems early.
