# Pricing and billing

With AWS Security Agent, you pay for penetration testing in _task hours_. Task hours measure the time the agent spends reasoning and acting, not the time you wait for a run to finish. This topic explains what accrues task hours so that you can predict and track what a penetration test costs.

For current rates and worked billing examples, see [AWS Security Agent pricing](https://aws.amazon.com/security-agent/pricing/ "https://aws.amazon.com/security-agent/pricing/").

## Billable capabilities

The following table describes which capabilities AWS Security Agent bills for.

| Capability          | How AWS Security Agent charges you                                  |
| ------------------- | ------------------------------------------------------------------- |
| Penetration testing | AWS Security Agent meters each task hour by the second of task time |
| Code review         | No charge while in preview                                          |
| Design review       | No charge while in preview                                          |
| Threat modeling     | No charge while in preview                                          |

AWS Security Agent bills penetration testing for each second of task time. It converts the total to hours on your bill, so you pay for partial hours.

## What counts as a task hour

A task hour measures the time of active work performed by AWS Security Agent within a task.

## Task hours compared to duration

The run summary and the **All runs** table both report duration and task hours. They measure different things.

**Duration** is the elapsed time from when a run starts until it finishes. This represents how long you wait for results.

**Task hours** are the agent work inside that run. Task hours have no fixed relationship to duration.

Task hours exceed duration when the agent runs many tasks at the same time.

## Find the task hours for a run

Open the penetration test in the AWS Security Agent web application. The **All runs** table reports task hours for every run alongside its duration and job type. Select a run to see the same values in its run summary.

To see which tasks accrued the task hours, select the **Logs** tab. Each task in the list reports its own task hours, and the task detail panel shows both its duration and its task hours.

To track charges across runs, use AWS Cost Explorer. To get notified when charges pass a threshold that you set, create a budget in AWS Budgets. For more information, see [Analyzing your costs with AWS Cost Explorer](../../../cost-management/latest/userguide/ce-what-is.md "../../../cost-management/latest/userguide/ce-what-is.md") and [Managing your costs with AWS Budgets](../../../cost-management/latest/userguide/budgets-managing-costs.md "../../../cost-management/latest/userguide/budgets-managing-costs.md").

The `PentestExecutionDuration` metric that AWS Security Agent publishes to Amazon CloudWatch reports duration in seconds. For more information, see [Logging and monitoring in AWS Security Agent](logging-monitoring.md "logging-monitoring.md").

## Service quotas are not spending limits

AWS Security Agent applies monthly quotas to design reviews and pull request code reviews. It also applies configuration quotas to resources such as Agent Spaces and penetration test projects. These quotas limit capacity, not spending. Reaching a monthly quota blocks additional reviews until the next month. It doesn’t cap what you spend on penetration testing, and a quota increase doesn’t change your rate. For more information, see [Service Quotas](quotas.md "quotas.md").

## Control penetration testing costs

Task hours depend on how much reasoning and acting you ask the agent to do. To reduce the task hours that a run consumes, do the following:

- **Narrow the test scope** – Target specific URL paths rather than an entire domain, and list URLs that you want to exclude. For more information, see [Create a penetration test](perform-penetration-test.md "perform-penetration-test.md").
- **Select only the risk types you need** – Each additional risk type adds tasks to the run.
- **Stop a run that is off track** – Monitor the penetration test logs as a run progresses. If the logs show that the agent is exploring areas you don’t care about, stop the run. For more information, see [Review findings from a penetration test](review-penetration-findings.md "review-penetration-findings.md").
- **Reuse a configuration to build a baseline** – Penetration test configurations are reusable. Compare the task hours across runs of the same configuration to learn what a target typically costs.

## Pricing FAQ

### Why don’t the task hours for my job match its duration?

A job’s task hours reflect the total cumulative work done by AWS Security Agent across all concurrent tasks. Duration is the elapsed time from when a job starts until it finishes. Task hours can exceed duration when the agent runs many tasks at the same time.

### Which capabilities does AWS Security Agent charge for?

Penetration testing. AWS doesn’t charge for code reviews, design reviews, or threat models while those capabilities are in preview. Quotas still apply to those capabilities. For more information, see [Service Quotas](quotas.md "quotas.md").

### Does reaching a quota stop my charges?

No. Quotas limit how many resources you can create and how many reviews you can run. They don’t limit how much you can spend. For more information, see [Service Quotas](quotas.md "quotas.md").

### Can I estimate what a penetration test will cost before I start it?

There is no precise estimation. Task hours depend on the breadth of the target application and the risk types you select. The agent also adapts its plan as it explores your application. If you have run the same configuration before, use the task hours from those runs as a baseline. For worked examples, see [AWS Security Agent pricing](https://aws.amazon.com/security-agent/pricing/ "https://aws.amazon.com/security-agent/pricing/").

### If I stop a run before it finishes, am I charged?

Yes, the task hours that accrue until the job stops are charged.
