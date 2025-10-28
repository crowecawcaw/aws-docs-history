# Documentation and infrastructure

When running a WAFR, you may find that for many of the best
practices you are following, you will have a documented process,
standard operating procedure (SOP), runbook, or playbook. During the
WAFR, record information and context in the notes field within the
Well-Architected Tool (WA Tool). You can save time during the review
by gathering all relevant documentation artifacts that relate to the
workload in advance.

Consider the following questions as you consider your documentation:

- What documentation exists about the workload?
- What documentation is missing?
- What tools would be used to create and store these artifacts?
- Who would be involved in the creation and maintenance of these
  artifacts?

Some examples of documentation about your workload include:

- Workload wiki pages
- Architectural diagrams
- Architectural decision record (ADR)
- Standard operating procedures (SOPs)
- Infrastructure as code (IaC) repositories
- Networking topology
- Playbooks and runbooks
- Organization or team structure
- Multi-account strategy documentation
- Central identity provider configuration
- Central monitoring solution configuration
- Documentation for dependent workloads
- API reference guide
- Software library versions
- Correction of errors (COE) process and history
- Chaos engineering strategy
- Load testing team details
- Threat model
- Team retrospectives
- Game day documents

## Anti-patterns

If none of these resources exist, you can still run the WAFR as a
discovery mechanism. However, the process can take longer without
these artifacts. Creating documentation assets can be the first
step towards architectural health improvement.

## Workload discovery

It's difficult to efficiently review an architecture without
knowing its components and resources. Legacy workloads often
evolve over time or change ownership, and they may not have been
defined using infrastructure as code (IaC) tools like AWS CloudFormation, AWS CDK, or Terraform.

Before discussing improvements, understand the different
architectural components of the workload and its dependencies, and
create a visual representation to provide a shared understanding.

There are many third party discovery and auto-diagramming tools
available directly from the software vendors, from
[AWS Marketplace](https://aws.amazon.com/marketplace/search/results/ "https://aws.amazon.com/marketplace/search/results/"), or as open source solutions.

## Resources

- [AWS Reference Architecture Diagrams](https://aws.amazon.com/architecture/reference-architecture-diagrams "https://aws.amazon.com/architecture/reference-architecture-diagrams")
- [Architectural
  Decision Record Process](../../../prescriptive-guidance/latest/architectural-decision-records/adr-process.md "../../../prescriptive-guidance/latest/architectural-decision-records/adr-process.md")
- [ADR GitHub
  Home](https://adr.github.io/ "https://adr.github.io/")
- [Why
  you should develop a correction of error (COE)](https://aws.amazon.com/blogs/mt/why-you-should-develop-a-correction-of-error-coe/ "https://aws.amazon.com/blogs/mt/why-you-should-develop-a-correction-of-error-coe/")
- [Workload
  Discovery On AWS Solution](https://aws.amazon.com/solutions/implementations/workload-discovery-on-aws/ "https://aws.amazon.com/solutions/implementations/workload-discovery-on-aws/")
