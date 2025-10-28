# Use fair-share scheduling to help schedule jobs

Fair-share scheduling provides a set of controls to help schedule jobs.

###### Note

For more information about scheduling policy parameters, see [SchedulingPolicyDetail](../APIReference/API_SchedulingPolicyDetail.md "../APIReference/API_SchedulingPolicyDetail.md").

- **Share decay seconds –** The period of time (in seconds)
  that the AWS Batch scheduler uses to calculate a fair-share percentage for each share
  identifier. A value of zero indicates that only current usage is measured. A longer decay
  time gives more weight to time.

###### Note

The period of time for decay is calculated as: _`shareDecaySeconds +
 OrderMinutes`_ where _`OrderMinutes`_ is the time in the order in minutes.

- **Compute reservation –** Prevents jobs in a single share
  identifier from using up all the resources that are attached to the job queue. The
  reserved ratio is `*(computeReservation/100)^ActiveFairShares*` where `ActiveFairShares` is
  the number of active share identifiers.

###### Note

If a share identifier has jobs in a `SUBMITTED`, `PENDING`,
`RUNNABLE`, `STARTING`, or `RUNNING` state, it's
considered an active share identifier. After the period of time for decay expires, a
share identifier is considered inactive.

- **Weight factor –** The weight factor for the share
  identifier. The default value is 1. A lower value lets jobs from the share identifier run
  or gives additional runtime to the share identifier. For example, jobs that use a share
  identifier with a weight factor of 0.125 (1/8) are assigned eight times the compute
  resources of jobs that use a share identifier with a weight factor of 1.

###### Note

You only need to define this attribute when you need to update the default weight
factor of 1.
When the job queue is active and processing jobs, you can review a list of the first 100 `RUNNABLE` jobs through the Job queue snapshot. For more information, see [View job queue status](job_queue_viewing_status.md "job_queue_viewing_status.md").
