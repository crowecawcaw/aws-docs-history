# Sustainability as a non-functional requirement

Adding sustainability to your list of business requirements can
result in more cost-effective solutions. Focusing on getting more
value from the resources you use and using fewer of them directly
translates to cost savings on AWS as you pay only for what you use.

Meeting sustainability targets might not require equivalent
trade-offs in one or more other traditional metrics such as uptime,
availability, or response time. You can achieve significant gains in
sustainability with no measurable impact on service levels. Where
minor trade-offs are required, the sustainability improvements
gained by these trade-offs can outweigh the change in quality of
service.

Encourage your team members to continually experiment with
sustainability improvements as they develop functional requirements.
Teams should also embed proxy metrics when setting goals to ensure
that they evaluate resource intensity when developing their
workloads.

The following are example trade-offs that can reduce the cloud
resources you consume:

**Adjust quality of result:** You can
trade Quality of Results (QoR) for a reduction in workload intensity
with approximate computing. The practice of approximate computing
looks for opportunities to exploit the gap between what customers
need and what you actually produce. For example, if you place your
data in a *set* data structure, you can drop the
ORDER BY operator in SQL to remove unnecessary processing, saving
resources while still providing an acceptable answer.

**Adjust response time:** An answer
with a slower response time can reduce carbon by minimizing shared
overhead. Processing ad hoc, ephemeral tasks can incur startup
overhead. Group and process tasks in batches instead of paying for
overhead each time a task arrives. Batch processing trades increased
response time for a reduction in the shared overhead of spinning up
an instance, downloading the source code, and running the process.

**Adjust availability:** With AWS, you can add redundancy and
meet high-availability targets with just a few clicks. You can increase redundancy through
techniques like static stability by provisioning idle resources that always result in decreased
utilization. Evaluate the needs of the business when setting targets. Relatively minor
trade-offs in availability can result in much larger improvements in utilization. For example,
the static stability architecture pattern involves provisioning idle failover capacity to
immediately take on load after a component fault. Relaxing the availability requirement can
remove the need for idle online capacity by allowing time for automation to deploy replacement
resources. Adding failover capacity on-demand drives higher overall utilization with no impact
to the business during normal operations and has the secondary benefit of reducing costs.
