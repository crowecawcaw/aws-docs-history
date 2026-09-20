

# Jobs stuck in `RUNNABLE` due to misconfiguration
<a name="sm_job_stuck_in_runnable_misconfiguration"></a>

**Service environment max resource exceeded**  
When a job submitted to AWS Batch via `SubmitServiceJob` reaches the front of the queue, and it requires more instances than the connected service environment's capacity limits allow, then AWS Batch will infer a misconfiguration due to exceeding service environment capacity limits. The service environment `capacityLimits` structure supports different `capacityUnit` values depending on the scheduling algorithm configured on the job queue.  


<table>
<thead>
  <tr><th>Scheduling algorithm</th><th>Service environment <code>capacityLimits.capacityUnit</code></th><th>Condition</th></tr>
</thead>
<tbody>
  <tr><td>First-in, first-out</td><td><code>NUM_INSTANCES</code></td><td>Job requests more instances than <code>maxCapacity</code>. For example, a service environment is configured with a max capacity of 10 instances and a job is submitted that requests 11 instances.</td></tr>
  <tr><td>Fair-share</td><td><code>NUM_INSTANCES</code></td><td>Job requests more instances than <code>maxCapacity</code>. For example, a service environment is configured with a max capacity of 10 instances and a job is submitted that requests 11 instances.</td></tr>
  <tr><td>Quota management</td><td>Instance type (for example, <code>ml.m5.xlarge</code>)</td><td>Job requests more of an instance type than <code>maxCapacity</code> for that type. For example, a service environment has a max capacity of 10 <code>ml.m5.xlarge</code> instances and a job is submitted that requests 12 <code>ml.m5.xlarge</code> instances.</td></tr>
</tbody>
</table>

+ **`statusReason` message while the job is stuck:** `MISCONFIGURATION:SERVICE_ENVIRONMENT_MAX_RESOURCE - Service environment(s) associated with the job queue cannot meet the capacity requirement of the job.`
+ **`reason` used for `jobStateTimeLimitActions`:** `MISCONFIGURATION:SERVICE_ENVIRONMENT_MAX_RESOURCE`
+ **`statusReason` message after the job is terminated by `jobStateTimeLimitActions`:** `Terminated by JobStateTimeLimit action due to reason: MISCONFIGURATION:SERVICE_ENVIRONMENT_MAX_RESOURCE`

**Quota share limits exceeded**  
When a job submitted to AWS Batch via `SubmitServiceJob` reaches the front of the queue, and it requires more instances than the quota share's capacity limits allow, then AWS Batch will infer a misconfiguration due to exceeding quota share capacity limits. This analysis depends on how the quota share was configured.  


<table>
<thead>
  <tr><th><code>resourceSharingStrategy</code></th><th>Condition</th><th><code>statusReason</code> while stuck</th></tr>
</thead>
<tbody>
  <tr><td><code>RESERVE</code> or <code>LEND</code></td><td>Job requires more of an instance type than the quota share's capacity limits. For example, a job that requests 5 <code>ml.m5.xlarge</code> instances submitted to a quota share with a <code>capacityLimit</code> of 4 <code>ml.m5.xlarge</code> instances.</td><td><code>MISCONFIGURATION:QUOTA_MANAGEMENT_LIMIT_EXCEEDED - Job requirements exceed quota share capacity limits.</code></td></tr>
  <tr><td><code>LEND_AND_BORROW</code></td><td>Job requires more than capacity + borrow limits combined. For example, a job that requests 5 <code>ml.m5.xlarge</code> instances submitted to a quota share with a <code>capacityLimit</code> of 2 <code>ml.m5.xlarge</code> with a <code>borrowLimit</code> of <code>100</code> — the largest job this quota share can run is 4 instances.</td><td><code>MISCONFIGURATION:QUOTA_MANAGEMENT_LIMIT_EXCEEDED - Job requirements exceed quota share capacity limits and borrow limits.</code></td></tr>
  <tr><td><code>LEND_AND_BORROW</code></td><td>Job requires borrowing that exceeds all available borrowable capacity across shares. For example, two quota shares A and B each configured to <code>LEND_AND_BORROW</code> with a <code>capacityLimit</code> of 4 <code>ml.m5.xlarge</code> instances and a <code>borrowLimit</code> of 200. A job submitted to quota share A that requests 10 <code>ml.m5.xlarge</code> instances exceeds the max of 8 (own 4 + borrow 4 from B).</td><td><code>MISCONFIGURATION:QUOTA_MANAGEMENT_LIMIT_EXCEEDED - Job requires borrowing that exceeds all configured borrowable capacity.</code></td></tr>
</tbody>
</table>

+ **`reason` used for `jobStateTimeLimitActions`:** `MISCONFIGURATION:QUOTA_MANAGEMENT_LIMIT_EXCEEDED`
+ **`statusReason` message after the job is terminated by `jobStateTimeLimitActions`:** `Terminated by JobStateTimeLimit action due to reason: MISCONFIGURATION:QUOTA_MANAGEMENT_LIMIT_EXCEEDED`