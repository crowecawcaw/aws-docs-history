# Failure management

In any system of reasonable complexity, it is expected that
failures will occur. Reliability requires that your workload be
aware of failures as they occur and take action to avoid impact on
availability. Workloads must be able to both withstand failures
and automatically repair issues.

With AWS, you can take advantage of automation to react to monitoring data. For example,
when a particular metric crosses a threshold, you can initiate an automated action to
remedy the problem. Also, rather than trying to diagnose and fix a failed resource that is
part of your production environment, you can replace it with a new one and carry out the
analysis on the failed resource out of band. Since the cloud allows you to stand up
temporary versions of a whole system at low cost, you can use automated testing to verify
full recovery processes.

The following questions focus on these considerations for
reliability.

| REL 9:  How do you back up data?                                                                                                                   |
| -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Back up data, applications, and configuration to meet your requirements for<br>recovery time objectives (RTO) and recovery point objectives (RPO). |

| REL 10:  How do you use fault isolation to protect your workload?                                                                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Fault isolation limits the impact of a component or system failure to a defined boundary. With proper isolation, components outside of the boundary are unaffected by the failure. Running your workload across multiple fault isolation boundaries can make it more resilient to failure. |

| REL 11:  How do you design your workload to withstand component<br>failures?                                                   |
| ------------------------------------------------------------------------------------------------------------------------------ |
| Workloads with a requirement for high availability and low mean time to<br>recovery (MTTR) must be architected for resiliency. |

| REL 12:  How do you test reliability?                                                                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| After you have designed your workload to be resilient to the stresses of<br>production, testing is the only way to verify that it will operate as designed,<br>and deliver the resiliency you expect. |

| REL 13:  How do you plan for disaster recovery (DR)?                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Having backups and redundant workload components in place is the start of your DR strategy. [RTO and RPO are your objectives](../reliability-pillar/disaster-recovery-dr-objectives.md "../reliability-pillar/disaster-recovery-dr-objectives.md") for restoration of your workload. Set these based on business needs. Implement a strategy to meet these objectives, considering locations and function of workload resources and data. The probability of disruption and cost of recovery are also key factors that help to inform the business value of providing disaster recovery for a workload. |

Regularly back up your data and test your backup files to verify
that you can recover from both logical and physical errors. A
key to managing failure is the frequent and automated testing of
workloads to cause failure, and then observe how they recover.
Do this on a regular schedule and verify that such testing is also
initiated after significant workload changes. Actively track KPIs,
and also the recovery time objective (RTO) and recovery point
objective (RPO), to assess a workload's resiliency (especially
under failure-testing scenarios). Tracking KPIs will help you
identify and mitigate single points of failure. The objective is
to thoroughly test your workload-recovery processes so that you
are confident that you can recover all your data and continue to
serve your customers, even in the face of sustained problems. Your
recovery processes should be as well exercised as your normal
production processes.
