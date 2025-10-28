AWS Migration Hub will no longer be open to new customers starting November 7, 2025. To continue using the service, sign up prior to November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Discovery with AWS Migration Hub requires the home Region

To start discovery and planning, you can deploy data collectors, such as AWS Application Discovery Agent
(Discovery Agent) or Application Discovery Service Agentless Collector (Agentless Collector), into your
data centers. These tools send data to the AWS Migration Hub service in your home Region, and
the information is displayed in your home Region in the console.

Before you install your data collectors, you must choose an AWS Migration Hub home Region as
described in [Choose an AWS Migration Hub home Region](select-home-region.md "select-home-region.md").
Before collecting data, you must register your collectors in your home Region. If you're
using the AWS CLI, you must set up your AWS CLI to use the home Region as the default
Region.

Discovery Agent discovers data for many types of hardware, hypervisors, and operating systems
including Linux and Windows. An agent must be installed on each host that is targeted
for migration. For specific information about the data fields that are returned by
Discovery Agent, see [Data
collected by Discovery Agent](../../../application-discovery/latest/userguide/agent-data-collected.md "../../../application-discovery/latest/userguide/agent-data-collected.md") in the
_Application Discovery Service User Guide_.

Agentless Collector discovers data for VMware vCenter hosts and systems,
using VMware metadata. For specific information about the data fields that are returned
by Agentless Collector, see [Data collected by Agentless Collector](../../../application-discovery/latest/userguide/agentless-collector-data-collected.md "../../../application-discovery/latest/userguide/agentless-collector-data-collected.md") in the
_Application Discovery Service User Guide_.

Alternatively, you can use Migration Hub import to import details of your on-premises
environment directly into Migration Hub without using Agentless Collector or Discovery Agent.
For more information, see [Migration Hub
import](../../../application-discovery/latest/userguide/discovery-import.md "../../../application-discovery/latest/userguide/discovery-import.md").
