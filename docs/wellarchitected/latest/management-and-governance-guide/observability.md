# Monitoring and observability

Like security, monitoring and observability are required for all
teams who operate and administer cloud applications and services. As
described in the [Operational
Excellence Pillar whitepaper](../operational-excellence-pillar/welcome.md "../operational-excellence-pillar/welcome.md"), your teams must
define, capture, and analyze operations metrics to gain visibility
into workload events so that you can take appropriate action. In the
management layer, this also means understanding operational metrics
as you provide guardrails, network, security, and identity services
in your management platform.

All of your teams, whether responsible for many cloud environments
or a single application, must be able to understand the health of
their operations easily. Your teams will want to use metrics based
on operations outcomes to gain useful insights. You should use these
metrics to make informed decisions, and as key inputs into each of
the eight M&G Guide capabilities. AWS makes it easier to bring
together and analyze your operations logs so that you can generate
metrics, know the status of your operations, and gain insight from
operations over time. These activities are supported centrally when
you provide an observability solution for consumption, storage,
analysis, and presentation of operational data for analysis.

As described in [Responding to
Events](../operational-excellence-pillar/responding-to-events.md "../operational-excellence-pillar/responding-to-events.md"), you should anticipate both planned operational events (such
as, sales promotions, deployments, and failure tests) and unplanned
ones (such as, surges in utilization and component failures). Use
simulations, custom runbooks, and playbooks, and iterate to deliver
consistent results when you respond to alerts. Defined alerts should
be owned by a role or a team that is accountable for the response
and escalations. You will also want to know the business impact of
your system components and use this to target efforts when needed.
Perform a root cause analysis (RCA) after events, and then introduce
necessary changes and controls to prevent recurrence of failures or
document workarounds.

In many enterprises, technical teams share integrated systems to
monitor the services or infrastructure they manage. Shared
observability systems bring together all the performance data for an
entire organization, enabling teams to visualize the connections
between services and components, collaborate with real-time data,
and quickly identify the source of performance or security issues.

Observability systems collect data directly from applications, and
AWS logging and service metric capabilities. AWS provides several
services that can help increase your monitoring and observability
posture. These services include
[AWS CloudTrail](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/"),
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/"),
[Amazon Managed
Service for Prometheus](https://aws.amazon.com/prometheus/ "https://aws.amazon.com/prometheus/"),
[VPC
Flow Logs](../../../vpc/latest/userguide/flow-logs.md "../../../vpc/latest/userguide/flow-logs.md"),
[AWS X-Ray
traces](https://aws.amazon.com/xray/features/ "https://aws.amazon.com/xray/features/"),
[Amazon EventBridge events](../../../eventbridge/latest/userguide/eb-events.md "../../../eventbridge/latest/userguide/eb-events.md"), Amazon Managed Grafana,
[ELB](https://aws.amazon.com/elasticloadbalancing/ "https://aws.amazon.com/elasticloadbalancing/"), and
[AWS Network Firewall](https://aws.amazon.com/network-firewall/ "https://aws.amazon.com/network-firewall/").
