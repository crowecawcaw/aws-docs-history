# Incident management in AMS Accelerate

In AMS Accelerate, you use the **AWS Support Center Console** to
file incident reports. Incidents are AWS service performance issues that impact your managed
environment, as determined by AMS Accelerate or you. Incidents identified by the AMS Accelerate
team are first received as _events_ (a change in system state
captured by monitoring). If a configured threshold is breached, the event triggers an alarm,
also called an alert. The AMS Accelerate operations team determines if the event is
non-impacting, or an incident (a service interruption or degradation), or a problem (the
underlying root cause of one or more incidents).

###### Note

The AMS Accelerate team also receives incidents created by you programmatically using the
[AWS Support API](../../../awssupport/latest/user/Welcome.md "../../../awssupport/latest/user/Welcome.md")
with service code `service-ams-operations-report-incident`.

For information about using Support, see [Getting started with Support](../../../awssupport/latest/user/getting-started.md "../../../awssupport/latest/user/getting-started.md").

## How incident response and resolution work

AMS Accelerate uses IT service management (ITSM) incident management best practices to restore service,
when needed, as quickly as possible.

We provide 24/7/365 follow-the-sun support through operations centers around the world
with dedicated operators actively watching monitoring dashboards and incident queues.

Our operations engineers use internal incident tracking tools to identify, log, categorize, prioritize, diagnose,
resolve, and close incidents; we provide you with updates on all of these activities through AWS Support Center and
through the AWS Support API. Our operators leverage a variety of internal AWS support tools to help with all of
those activities. These operators are deeply familiar with AMS Accelerate-supported infrastructure and have expert-level
technical skills to address identified support issues. In the event our operators need assistance, the Premium
Support and AWS service teams are available.

After your incident is received by the AMS Accelerate operations team, we validate the priority and classification
working with you if there are any clarifications required. For example, if the incident report is better classified as a
service request, it's reclassified and the AMS Accelerate service request team takes over
and you're notified. If the incident can be resolved by the receiving operator, steps are
taken to quickly resolve the incident. AMS Accelerate operators consult internal documentation for a
resolution and, if needed, escalate the incident to other support resources until the incident
is resolved. After it's resolved, the AMS Accelerate
operations team documents the incident and resolution for future use.

In cases where critical severity incidents are impacting your critical workloads, AMS Accelerate may recommend an
infrastructure restore. There is often a trade-off between troubleshooting an issue and simply restoring from a known
functional backup, and your risks and impacts from service downtime are the deciding factors. If you have time to
devote to troubleshooting issues, AMS Accelerate will assist you, and your cloud service delivery manager (CSDM) may get
involved, but if the urgency to restore is high, AMS Accelerate can initiate a restore right away.
