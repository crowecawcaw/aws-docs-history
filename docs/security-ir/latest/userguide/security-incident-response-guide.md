# AWS Security Incident Response Technical Guide

###### Contents

- [Abstract](#abstract "#abstract")
- [Are you Well-Architected?](#are-you-well-architected "#are-you-well-architected")
- [Introduction](introduction.md "introduction.md")
- [Preparation](preparation.md "preparation.md")
- [Operations](operations.md "operations.md")
- [Post-incident activity](post-incident-activity.md "post-incident-activity.md")
- [Conclusion](conclusion.md "conclusion.md")
- [Contributors](contributors.md "contributors.md")
- [Appendix A: Cloud capability definitions](appendix-a-cloud-capability-definitions.md "appendix-a-cloud-capability-definitions.md")
- [Appendix B: AWS incident response resources](appendix-b-incident-response-resources.md "appendix-b-incident-response-resources.md")
- [Notices](notices.md "notices.md")

## Abstract

This guide presents an overview of the fundamentals of responding to security incidents
within a customer’s Amazon Web Services (AWS) Cloud environment. It provides an overview
of cloud security and incident response concepts and identifies cloud capabilities,
services, and mechanisms that are available to customers who respond to security issues.

This guide is intended for those in technical roles and assumes that you are familiar
with the general principles of information security, have a basic understanding of security
incident response in your current on-premises environments, and have some familiarity with cloud services.

## Are you Well-Architected?

The
[AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/ "https://aws.amazon.com/architecture/well-architected/") helps you understand the pros
and cons of the decisions you make when building systems in the
cloud. The six pillars of the Framework allow you to learn
architectural best practices for designing and operating reliable,
secure, efficient, cost-effective, and sustainable systems. Using
the
[AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/ "https://aws.amazon.com/well-architected-tool/"), available at no charge in the
[AWS Well-Architected Tool console](https://console.aws.amazon.com/wellarchitected "https://console.aws.amazon.com/wellarchitected"), you can review your workloads against
these best practices by answering a set of questions for each
pillar.

For more expert guidance and best practices for your cloud
architecture—reference architecture deployments, diagrams, and
whitepapers—refer to the
[AWS Architecture Center](https://aws.amazon.com/architecture/ "https://aws.amazon.com/architecture/").
