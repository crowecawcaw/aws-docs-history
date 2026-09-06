

# Jobs stuck in `RUNNABLE` due to misconfiguration
<a name="sm_job_stuck_in_runnable_misconfiguration"></a>

**Service environment max resource exceeded**  
When a job submitted to AWS Batch via `SubmitServiceJob` reaches the front of the queue, and it requires more instances than the connected service environment's capacity limits allow, then AWS Batch will infer a misconfiguration due to exceeding service environment capacity limits. The service environment `capacityLimits` structure supports different `capacityUnit` values depending on the scheduling algorithm configured on the job queue.      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/batch/latest/userguide/sm_job_stuck_in_runnable_misconfiguration.html)
+ **`statusReason` message while the job is stuck:** `MISCONFIGURATION:SERVICE_ENVIRONMENT_MAX_RESOURCE - Service environment(s) associated with the job queue cannot meet the capacity requirement of the job.`
+ **`reason` used for `jobStateTimeLimitActions`:** `MISCONFIGURATION:SERVICE_ENVIRONMENT_MAX_RESOURCE`
+ **`statusReason` message after the job is terminated by `jobStateTimeLimitActions`:** `Terminated by JobStateTimeLimit action due to reason: MISCONFIGURATION:SERVICE_ENVIRONMENT_MAX_RESOURCE`

**Quota share limits exceeded**  
When a job submitted to AWS Batch via `SubmitServiceJob` reaches the front of the queue, and it requires more instances than the quota share's capacity limits allow, then AWS Batch will infer a misconfiguration due to exceeding quota share capacity limits. This analysis depends on how the quota share was configured.      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/batch/latest/userguide/sm_job_stuck_in_runnable_misconfiguration.html)
+ **`reason` used for `jobStateTimeLimitActions`:** `MISCONFIGURATION:QUOTA_MANAGEMENT_LIMIT_EXCEEDED`
+ **`statusReason` message after the job is terminated by `jobStateTimeLimitActions`:** `Terminated by JobStateTimeLimit action due to reason: MISCONFIGURATION:QUOTA_MANAGEMENT_LIMIT_EXCEEDED`