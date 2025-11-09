# Design principles

Well-Architected design principles are a set of considerations used
as the basis for a well-architected workload. We recommend that you
follow these design principles for a successful EUC implementation.

## Evaluate the scope of your EUC use cases

Begin your design process by making an inventory of the various
EUC use cases in your organization. Most organizations will have
multiple user personas that have unique requirements. For example,
the different use cases within the same organization may require
varying:

- Sets of applications
- Peripherals
- Levels of data persistence
- Dependencies on external systems or networks
- Support teams
- Cost concerns
- Availability requirements
- Security risk profiles

Enumerate as much of this data as possible and use this data to
inform the EUC design process.

Based on your inventory of user personas and their requirements,
select the most appropriate EUC service for each use case. Learn
the fundamental aspects of the core AWS EUC services. For optimal
efficiency in implementing diverse use cases within your
organization, you may need to use multiple EUC services.

Engage your AWS account team and the AWS EUC specialist team for
additional guidance during any stage of your EUC journey. For more
information, see Operational excellence.

## Isolate EUC resources and minimize permissions

EUC services typically have different admin teams and security
risk profiles from other AWS workloads. This means deploying EUC
services in isolation by segregating them at the account boundary
level. Consider any data sovereignty or regulatory compliance
needs for your workloads (such as
[HIPAA](https://aws.amazon.com/compliance/hipaa-compliance/ "https://aws.amazon.com/compliance/hipaa-compliance/"),
[PCI](https://aws.amazon.com/compliance/pci-dss-level-1-faqs/ "https://aws.amazon.com/compliance/pci-dss-level-1-faqs/"),
[SOC](https://aws.amazon.com/compliance/soc-faqs/ "https://aws.amazon.com/compliance/soc-faqs/"),
or
[FedRAMP](https://aws.amazon.com/compliance/fedramp/ "https://aws.amazon.com/compliance/fedramp/"))
and use AWS guidance to build compliance-aligned workloads. Remove
or block access to unneeded software. If required, control data
egress using controls built into EUC services, such as client copy
and paste, printer redirection, and upload and download
functionality. Consider forwarding OS or application logs and
using agents to validate security posture. Develop a vulnerability
and patch management strategy to keep your instances and images
secure and up to date with the latest security updates. For more
information, see Security.

## Design EUC solutions that maximize performance

Maximize client performance by deploying your EUC use cases near
the user base. Similarly, deploy EUC use case dependencies (like
directory services and file shares) near your EUC deployment to
maximize application performance. Consider combining similar or
overlapping use cases to reduce deployment and maintenance tasks.
Consider separating use cases based on the different needs from
your EUC use case inventory. For example, if use cases have
different support teams or cost reporting needs, you may want to
place them in different subnets, VPCs, or AWS accounts. When
separating use cases, you still may be able to gain efficiencies
by reusing images. Also, consider abstracting the applications
from the images or creating a library of reusable scripts to
deploy applications automatically. For more detail, see
Performance efficiency.

## Minimize EUC resources to optimize costs

Minimize resources needed to deliver your use cases, including
instance and bundle types and fleet sizes. Review usage
periodically to identify idle or underused resources (such as
unused or over-provisioned instances, oversized fleets, and
inefficient scaling policies). Deploy automated tools, such as the
[Cost
Optimizer for Amazon WorkSpaces](https://aws.amazon.com/solutions/implementations/cost-optimizer-for-amazon-workspaces/ "https://aws.amazon.com/solutions/implementations/cost-optimizer-for-amazon-workspaces/") and the
[Cost
Optimizer for Amazon WorkSpaces Applications](https://github.com/aws-samples/cost-optimizer-for-amazon-appstream2 "https://github.com/aws-samples/cost-optimizer-for-amazon-appstream2"),to help with this
process. Use open-source OSes when use cases allow or bring your
own OS licenses when available. For more detail, see Cost
optimization.
