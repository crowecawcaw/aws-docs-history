

# Jobs stuck in `RUNNABLE` due to capacity
<a name="sm_job_stuck_in_runnable_capacity"></a>

The following scenario describes how AWS Batch identifies insufficient capacity conditions.

**Insufficient instance capacity**  
AWS Batch interprets two sets of responses received by SageMaker Training jobs as cases of insufficient instance capacity. Whenever these are received, AWS Batch sets a corresponding `statusReason` of `CAPACITY:INSUFFICIENT_INSTANCE_CAPACITY`.  
In both cases, the time the corresponding AWS Batch job spent in `SCHEDULED` between job submission and failure accumulates between job submissions for comparison against `maxTimeSeconds`.      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/batch/latest/userguide/sm_job_stuck_in_runnable_capacity.html)
If either of these cases is hit, AWS Batch will consider the job to be encountering insufficient capacity.  
+ **`statusReason` message while the job is stuck:** `CAPACITY:INSUFFICIENT_INSTANCE_CAPACITY - Unable to provision requested compute resources`
+ **`reason` used for `jobStateTimeLimitActions`:** `CAPACITY:INSUFFICIENT_INSTANCE_CAPACITY`
+ **`statusReason` message after the job is terminated by `jobStateTimeLimitActions`:** `Terminated by JobStateTimeLimit action due to reason: CAPACITY:INSUFFICIENT_INSTANCE_CAPACITY`