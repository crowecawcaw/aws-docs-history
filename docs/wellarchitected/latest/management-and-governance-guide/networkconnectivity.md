# Network connectivity

Workloads often exist in multiple locations or environments, both
publicly accessible and private. Managing networks in AWS might
require connecting many AWS-hosted VPCs from many accounts to
specific enterprise networks, and to the internet. Your network
strategy must allow for the interoperability of workloads while also
aligning to your security architecture. The careful planning and
management of your network design forms the foundation of how you
provide isolation and resource boundaries within your workload. We
think of network connectivity in three different groupings:
connectivity between your on-premises network and your AWS
environment, connectivity to and from the internet, and connectivity
across your AWS environments—primarily between VPCs.

Where connectivity between VPCs is required, the M&G Guide
recommends a hub and spoke model for your network design to connect
to your existing environment. Intra-application connectivity
requires multiple account network patterns that can be reusable for
scale. Account types can include sandbox accounts that might require
a separate network than the network used for your workload accounts.
Regulatory requirements might require you to separate production
data into distinct accounts and keep it separate from research and
development activities in your sandbox accounts. To reinforce your
data governance, you might restrict access using distinct network
boundaries, along with specific controls. These
boundaries could include controlling traffic with security groups
and NACLs, implementation of firewalls, and implementing limited
route configurations. Beyond data governance, your workload accounts
might need further network refinement for regulated and
non-regulated workloads.

Have a mechanism to enforce the use of non-overlapping private
subnets when provisioning new accounts and VPCs in your
multi-account framework. This automation should also encompass the
definition of which network controls and patterns are implemented as
you provision (and update) your AWS accounts and workloads. This
automation would include definitions of which Regions are included
and excluded from your network, as well as which mechanisms of
access are allowed in your environments. Using AWS Control Tower,
you can select a guardrail to detect if SSH or RDP is enabled for
internet connections within your network, while specifically
defining which Regions are allowed for the account and related VPC
to operate. SSH and RDP traffic can also be restricted through
security groups and NACLs.

Define and catalog your VPC in an infrastructure as code template
such as AWS CloudFormation. Doing so will allow you to automate its
provisioning as well as help with the necessary distributions of
future version updates. AWS Control Tower provides a default VPC, or
you can use the
[Scalable
VPC Architecture](https://aws.amazon.com/quickstart/architecture/vpc/ "https://aws.amazon.com/quickstart/architecture/vpc/") from AWS Quick Starts as a building block
for your own deployments. This template is also available within
your console in the
[Service Catalog Getting Started Library](https://console.aws.amazon.com/servicecatalog/home?portfolios%3FactiveTab=gslAdminPortfolios&region=us-east-1#getting-started-library "https://console.aws.amazon.com/servicecatalog/home?portfolios%3FactiveTab=gslAdminPortfolios®ion=us-east-1#getting-started-library").
