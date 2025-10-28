# Operate

Observability allows you to focus on meaningful data and understand your workload's interactions and output. By concentrating on essential insights and eliminating unnecessary data, you maintain a straightforward approach to understanding workload performance. It's essential not only to collect data but also to interpret it correctly. Define clear baselines, set appropriate alert thresholds, and actively monitor for any deviations. A shift in a key metric, especially when correlated with other data, can pinpoint specific problem areas.
With observability, you're better equipped to foresee and address potential challenges, ensuring that your workload operates smoothly and meets business needs.

Successful operation of a workload is measured by the achievement
of business and customer outcomes. Define expected outcomes,
determine how success will be measured, and identify metrics
that will be used in those calculations to determine if your
workload and operations are successful. Operational health
includes both the health of the workload and the health and
success of the operations activities performed in support of the
workload (for example, deployment and incident response).
Establish metrics baselines for improvement, investigation, and
intervention, collect and analyze your metrics, and then
validate your understanding of operations success and how it
changes over time. Use collected metrics to determine if you are
satisfying customer and business needs, and identify areas for
improvement.

Efficient and effective management of operational events is
required to achieve operational excellence. This applies to both
planned and unplanned operational events. Use established runbooks
for well-understood events, and use playbooks to aid in
investigation and resolution of issues. Prioritize responses to
events based on their business and customer impact. Verify that if
an alert is raised in response to an event, there is an associated
process to run with a specifically identified owner.
Define in advance the personnel required to resolve an event and
include escalation processes to engage additional personnel, as
it becomes necessary, based on urgency and impact. Identify and
engage individuals with the authority to make a decision on
courses of action where there will be a business impact from an
event response not previously addressed.

Communicate the operational status of workloads through dashboards
and notifications that are tailored to the target audience (for
example, customer, business, developers, operations) so that
they may take appropriate action, so that their expectations are
managed, and so that they are informed when normal operations
resume.

In AWS, you can generate dashboard views of your metrics collected
from workloads and natively from AWS. You can leverage CloudWatch
or third-party applications
to aggregate and present business, workload, and operations level
views of operations activities. AWS provides workload insights
through logging capabilities including AWS X-Ray, CloudWatch,
CloudTrail, and VPC Flow Logs to identify
workload issues in support of root cause analysis and remediation.

All of the metrics you collect should be aligned to a business
need and the outcomes they support. Develop scripted responses to
well-understood events and automate their performance in response
to recognizing the event.

###### Topics

- [Utilizing workload observability](utilizing-workload-observability.md "utilizing-workload-observability.md")
- [Understanding operational health](understanding-operational-health.md "understanding-operational-health.md")
- [Responding to events](responding-to-events.md "responding-to-events.md")
