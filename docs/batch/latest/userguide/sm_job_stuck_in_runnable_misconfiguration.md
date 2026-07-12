# Jobs stuck in `RUNNABLE` due to misconfiguration

**Service environment max resource exceeded**

When a job submitted to AWS Batch via `SubmitServiceJob` reaches the front of
the queue, and it requires more instances than the connected service environment's capacity
limits allow, then AWS Batch will infer a misconfiguration due to exceeding service
environment capacity limits. The service environment `capacityLimits` structure
supports different `capacityUnit` values depending on the scheduling algorithm
configured on the job queue.

| Scheduling algorithm | Service environment<br>`capacityLimits.capacityUnit` | Condition                                                                                                                                                                                                                               |
| -------------------- | ---------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| First-in, first-out  | `NUM_INSTANCES`                                      | Job requests more instances than `maxCapacity`. For example, a<br>service environment is configured with a max capacity of 10 instances and a job is<br>submitted that requests 11 instances.                                           |
| Fair-share           | `NUM_INSTANCES`                                      | Job requests more instances than `maxCapacity`. For example, a<br>service environment is configured with a max capacity of 10 instances and a job is<br>submitted that requests 11 instances.                                           |
| Quota management     | Instance type (for example, `ml.m5.xlarge`)          | Job requests more of an instance type than `maxCapacity` for<br>that type. For example, a service environment has a max capacity of 10<br>`ml.m5.xlarge` instances and a job is submitted that requests 12<br>`ml.m5.xlarge` instances. |

- **`statusReason` message while the job is
  stuck:**
  `MISCONFIGURATION:SERVICE_ENVIRONMENT_MAX_RESOURCE - Service environment(s)
 associated with the job queue cannot meet the capacity requirement of the
 job.`
- **`reason` used for
  `jobStateTimeLimitActions`:**
  `MISCONFIGURATION:SERVICE_ENVIRONMENT_MAX_RESOURCE`
- **`statusReason` message after the job is terminated
  by `jobStateTimeLimitActions`:**
  `Terminated by JobStateTimeLimit action due to reason:
 MISCONFIGURATION:SERVICE_ENVIRONMENT_MAX_RESOURCE`

**Quota share limits exceeded**

When a job submitted to AWS Batch via `SubmitServiceJob` reaches the front of
the queue, and it requires more instances than the quota share's capacity limits allow, then
AWS Batch will infer a misconfiguration due to exceeding quota share capacity limits. This
analysis depends on how the quota share was configured.

| `resourceSharingStrategy` | Condition                                                                                                                                                                                                                                                                                                                                                                                  | `statusReason` while stuck                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| `RESERVE` or `LEND`       | Job requires more of an instance type than the quota share's capacity<br>limits. For example, a job that requests 5 `ml.m5.xlarge` instances<br>submitted to a quota share with a `capacityLimit` of 4<br>`ml.m5.xlarge` instances.                                                                                                                                                        | `MISCONFIGURATION:QUOTA_MANAGEMENT_LIMIT_EXCEEDED<br>• Job requirements<br>exceed quota share capacity limits.`                       |
| `LEND_AND_BORROW`         | Job requires more than capacity + borrow limits combined. For example, a<br>job that requests 5 `ml.m5.xlarge` instances submitted to a quota share<br>with a `capacityLimit` of 2 `ml.m5.xlarge` with a<br>`borrowLimit` of `100` — the largest job this quota share can<br>run is 4 instances.                                                                                           | `MISCONFIGURATION:QUOTA_MANAGEMENT_LIMIT_EXCEEDED<br>• Job requirements<br>exceed quota share capacity limits and borrow limits.`     |
| `LEND_AND_BORROW`         | Job requires borrowing that exceeds all available borrowable capacity<br>across shares. For example, two quota shares A and B each configured to<br>`LEND_AND_BORROW` with a `capacityLimit` of 4<br>`ml.m5.xlarge` instances and a `borrowLimit` of 200. A job<br>submitted to quota share A that requests 10 `ml.m5.xlarge` instances<br>exceeds the max of 8 (own 4 + borrow 4 from B). | `MISCONFIGURATION:QUOTA_MANAGEMENT_LIMIT_EXCEEDED<br>• Job requires<br>borrowing that exceeds all configured borrowable<br>capacity.` |

- **`reason` used for
  `jobStateTimeLimitActions`:**
  `MISCONFIGURATION:QUOTA_MANAGEMENT_LIMIT_EXCEEDED`
- **`statusReason` message after the job is terminated
  by `jobStateTimeLimitActions`:**
  `Terminated by JobStateTimeLimit action due to reason:
 MISCONFIGURATION:QUOTA_MANAGEMENT_LIMIT_EXCEEDED`
