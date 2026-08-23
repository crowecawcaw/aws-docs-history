# Recovery plan quotas

The following quotas apply to recovery plans in each AWS account and Region:

| Resource                                              | Quota         |
| ----------------------------------------------------- | ------------- |
| Recovery plans per account, per Region                | 1,000         |
| Steps per recovery plan                               | 20            |
| Source servers per recovery plan, across all<br>steps | 100           |
| Concurrent executions per recovery plan               | 1             |
| Wait step duration                                    | 1–120 minutes |
| Maximum duration of a single execution                | 24 hours      |

The AWS Elastic Disaster Recovery service quotas that apply to an individual recovery, such as the
number of concurrent recovery jobs and the number of source servers per account, also
apply to the recoveries that a plan starts. A plan does not raise or bypass those
quotas.
