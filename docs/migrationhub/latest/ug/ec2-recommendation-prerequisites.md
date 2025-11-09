AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Prerequisites for getting Amazon EC2

instance recommendations in AWS Migration Hub

Before you can get Amazon EC2 instance recommendations, you must have data about your
on-premises servers in Migration Hub. This data can come from the discovery tools
Application Discovery Service Agentless Collector (Agentless Collector) or AWS Application Discovery Agent
(Discovery Agent), or from Migration Hub import.

- [Migration Hub import](../../../application-discovery/latest/userguide/discovery-import.md "../../../application-discovery/latest/userguide/discovery-import.md")
  – This allows you to import details of your on-premises environment
  directly into Migration Hub using a predefined CSV template. For more information, see
  [Migration Hub
  import](../../../application-discovery/latest/userguide/discovery-import.md "../../../application-discovery/latest/userguide/discovery-import.md").
- [Agentless Collector](../../../application-discovery/latest/userguide/discovery-connector.md "../../../application-discovery/latest/userguide/discovery-connector.md") – This is a VMware appliance
  that can collect information only about VMware virtual machines (VMs). For more
  information, see [Application Discovery Service Agentless Collector](../../../application-discovery/latest/userguide/agentless-collector.md "../../../application-discovery/latest/userguide/agentless-collector.md") in the
  _Application Discovery Service User Guide_
- [Discovery Agent](../../../application-discovery/latest/userguide/discovery-agent.md "../../../application-discovery/latest/userguide/discovery-agent.md") –
  This is AWS software that you install on on-premises servers and VMs targeted
  for discovery and migration. For more information, see [AWS Application Discovery Agent](../../../application-discovery/latest/userguide/discovery-agent.md "../../../application-discovery/latest/userguide/discovery-agent.md") in the
  _Application Discovery Service User Guide_.
