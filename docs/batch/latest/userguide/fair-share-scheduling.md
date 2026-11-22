

# Use fair-share scheduling to help schedule jobs

Fair-share scheduling provides a set of controls to help schedule jobs. For more information about scheduling policy parameters, see [SchedulingPolicyDetail](https://docs.aws.amazon.com/batch/latest/APIReference/API_SchedulingPolicyDetail.html). 
+ **Share decay seconds –** The period of time (in seconds) that the AWS Batch scheduler uses to calculate a fair-share percentage for each share identifier. A value of 600 seconds indicates that usage is measured over a 10-minute window. Any value less than 600, including zero (0), is defaulted to 600 by AWS Batch. A longer decay time accounts for more past usage in the fair-share calculation.
**Note**  
The period of time for decay is calculated as: *`shareDecaySeconds + OrderMinutes`* where *`OrderMinutes `*is the time in the order in minutes.
+ **Compute reservation –** Prevents jobs in a single share identifier from using up all the resources that are attached to the job queue. The reserved ratio is `(computeReservation/100)^ActiveFairShares` where `ActiveFairShares` is the number of active share identifiers.
**Note**  
If a share identifier has jobs in a `SUBMITTED`, `PENDING`, `RUNNABLE`, `STARTING`, or `RUNNING` state, it's considered an active share identifier. After the period of time for decay expires, a share identifier is considered inactive.
+ **Weight factor –** The weight factor for the share identifier. The default value is 1. A lower value lets jobs from the share identifier run or gives additional runtime to the share identifier. For example, jobs that use a share identifier with a weight factor of 0.125 (1/8) are assigned eight times the compute resources of jobs that use a share identifier with a weight factor of 1.
**Note**  
You only need to define this attribute when you need to update the default weight factor of 1.

When the job queue is active and processing jobs, you can review a list of the first 100 `RUNNABLE` jobs through the Job queue snapshot. For more information, see [View a job queue in AWS Batch](job_queue_viewing_status.md). 