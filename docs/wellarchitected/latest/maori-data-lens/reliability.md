# Reliability

The Reliability Pillar encompasses the ability of a workload to perform its intended
function correctly and consistently when it's expected to. This includes the ability to operate
and test the workload through its total lifecycle. This document provides in-depth, best
practice guidance for implementing reliable workloads on AWS. If relevant, you can find
prescriptive guidance on implementation in the [Reliability Pillar
whitepaper](../reliability-pillar/welcome.md "../reliability-pillar/welcome.md"). This pillar encompasses the ability of a workload to perform its intended
function correctly and consistently when it's expected to.

###### Design principles

- **Automatically recover from failure:** By monitoring a
  workload for key performance indicators (KPIs), you can run automation when a threshold is
  breached. These KPIs should be a measure of business value, not of the technical aspects of
  the operation of the service. This allows for automatic notification and tracking of
  failures, and for automated recovery processes that work around or repair the failure. With
  more sophisticated automation, it's possible to anticipate and remediate failures before
  they occur.
- **Test recovery procedures:** In an on-premises environment,
  testing is often conducted to prove that the workload works in a particular scenario.
  Testing is not typically used to validate recovery strategies. In the cloud, you can test
  how your workload fails, and you can validate your recovery procedures. You can use
  automation to simulate different failures or to recreate scenarios that led to failures
  before. This approach exposes failure pathways that you can test and fix
  _before_ a real failure scenario occurs, thus reducing risk.
- **Scale horizontally to increase aggregate workload
  availability:** Replace one large resource with multiple small resources to
  reduce the impact of a single failure on the overall workload. Distribute requests across
  multiple, smaller resources to ensure that they don't share a common point of failure.
- **Stop guessing capacity:** A common cause of failure in
  on-premises workloads is resource saturation, when the demands placed on a workload exceed
  the capacity of that workload (this is often the objective of denial of service attacks). In
  the cloud, you can monitor demand and workload utilisation, and automate the addition or
  removal of resources to maintain the optimal level to satisfy demand without over- or
  under-provisioning. There are still limits, but some quotas can be controlled and others can
  be managed.
- **Manage change through automation**: Changes to your
  infrastructure should be made using automation. The changes that need to be managed include
  changes to the automation, which then can be tracked and reviewed.
  From a Māori data perspective, there are other priorities and additional views of why
  reliability is important and how to go about improving reliability. The following specific
  questions and good practices complement best practices in the Reliability Pillar.

###### Topics

- [MD_REL 1 How
  do you safely retain data for future generations?](md_rel-1-how-do-you-safely-retain-data-for-future-generations.md "md_rel-1-how-do-you-safely-retain-data-for-future-generations.md")
- [Resources](md_rel-resources.md "md_rel-resources.md")
