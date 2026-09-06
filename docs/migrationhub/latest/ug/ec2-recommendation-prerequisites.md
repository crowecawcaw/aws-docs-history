

AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform).

# Prerequisites for getting Amazon EC2 instance recommendations in AWS Migration Hub
<a name="ec2-recommendation-prerequisites"></a>

Before you can get Amazon EC2 instance recommendations, you must have data about your on-premises servers in Migration Hub. This data can come from the discovery tools Application Discovery Service Agentless Collector (Agentless Collector) or AWS Application Discovery Agent (Discovery Agent), or from Migration Hub import. 
+ [Migration Hub import](https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-import.html) – This allows you to import details of your on-premises environment directly into Migration Hub using a predefined CSV template. For more information, see [Migration Hub import](https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-import.html).
+ [Agentless Collector](https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-connector.html) – This is a VMware appliance that can collect information only about VMware virtual machines (VMs). For more information, see [Application Discovery Service Agentless Collector](https://docs.aws.amazon.com/application-discovery/latest/userguide/agentless-collector.html) in the *Application Discovery Service User Guide*
+ [Discovery Agent](https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-agent.html) – This is AWS software that you install on on-premises servers and VMs targeted for discovery and migration. For more information, see [AWS Application Discovery Agent](https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-agent.html) in the *Application Discovery Service User Guide*.