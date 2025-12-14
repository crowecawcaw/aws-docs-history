# Best Practice 21.1 - Understand and influence business requirements to make sustainability-centric SAP design decisions

Business leaders and SAP architecture teams must make conscious decisions to design
their SAP environments in a more sustainable fashion. They must understand and justify the
rationale behind those choices. If business leaders cannot describe what tradeoffs they must
make in the language of sustainability and energy efficiency, they will have difficulty
making decisions based on those criteria. 

Production SAP workloads are mission critical to most businesses who run SAP, with
companies often prioritizing reliability and performance efficiency over infrastructure
costs. While prioritizing sustainability almost always results in cloud infrastructure cost
reductions, it might not create overall cost savings for an SAP workload. Running SAP
workloads in a more sustainable fashion in AWS can increase the costs of software,
personnel, or overall business functions. To meet sustainability goals, these tradeoffs
along with other priorities must be clearly articulated, agreed upon, and measurable.

**Suggestion 21.1.1 – Define criteria to measure and understand
your sustainability impact**

Understanding your sustainability goals is the first step to ensuring that you focus
on the factors needed to meet those goals. Defining such criteria involves adopting
metrics that can be used to measure and evaluate your current sustainability posture,
report progress against goals, and accelerate improvements. By analyzing the current
environmental impact of the underlying cloud-based SAP infrastructure, you can quantify
the tradeoffs and changes required to meet your sustainability objectives.

For example, the sustainability pillar of the AWS Well-Architected Framework
provides an introduction to emissions accounting, including examples of the scopes defined
by the Greenhouse Gas Protocol. Keep in mind that emissions from your SAP workloads in
AWS would count as a portion of your indirect Scope 3 emissions under these definitions.
Scope 3 emissions can be measured by a sustainability metric known as CO2e (carbon dioxide
equivalent). While not the only measure of sustainability, CO2e is commonly used to
measure and compare emissions from greenhouse gases based on how severely they contribute
to global warming, and shows how much a particular gas would contribute to global warming
if it were carbon dioxide.

Given that the previously mentioned data is not directly obtainable in most SAP
monitoring scenarios, you can use sustainability proxy metrics instead. Proxy metrics
allow SAP architecture teams to evaluate correlated improvements made to a workload
instead of real-time carbon metrics. Defining proxy metrics across compute, storage, and
network infrastructure can help you understand how infrastructure changes can impact
sustainability results. Example proxy metrics include vCPU minutes for compute, GBs
provisioned for storage, and GBs transferred for network traffic. Proxy metrics combined
with business metrics can define sustainability KPIs, which can be used to drive
sustainability optimizations while keeping business needs in focus. One example would be
to measure vCPU minutes per transaction and define an improvement goal to minimize this
metric. Business stakeholders would have to weigh the cost, as reducing vCPUs could
ultimately become detrimental to delivering on business needs. When running SAP workloads
in AWS, the change in these measured resources correlates with a similar change in cost
(except as noted in the following), making overall infrastructure spend a useful proxy
metric.

By agreeing on a set of sustainability metrics, the SAP architect team can evaluate
different technical approaches to reduce environmental impact. A small gap between the
current and target sustainability goals and your chosen metrics might result in small
architectural changes, while a large gap would require more drastic measures.

- Well-Architected Framework [Sustainability]: [Cloud
  sustainability](../sustainability-pillar/cloud-sustainability.md "../sustainability-pillar/cloud-sustainability.md")
- Well-Architected Framework [Sustainability]: [Evaluate specific improvements](../sustainability-pillar/evaluate-specific-improvements.md "../sustainability-pillar/evaluate-specific-improvements.md")
  **Suggestion 21.1.2 – Work with the business to establish more
  sustainable SLAs and only architect for the SLA negotiated**

Many businesses define their SAP Service Level Agreements (SLAs) based on demands for
minimal downtime, point-in-time recoverability, and response times that are as close to
instantaneous as possible. SAP architecture teams can overestimate the risks and impact of
downtime. As a result, they put in place SAP architectures that are likely to achieve a
much higher performance objective or availability target than the agreed-upon business
SLA. For example, a business might establish a [warm Regional standby disaster recovery landscape](../../../sap/latest/general/arch-guide-multi-region-architecture-patterns.md#arch-guide-pattern-7-a-primary-region-with-two-azs-for-production-and-secondary-region-with-compute-and-storage-capacity-deployed-in-a-single-az "../../../sap/latest/general/arch-guide-multi-region-architecture-patterns.md#arch-guide-pattern-7-a-primary-region-with-two-azs-for-production-and-secondary-region-with-compute-and-storage-capacity-deployed-in-a-single-az") when local [cross-AZ (Availability Zone) high availability](../../../sap/latest/general/arch-guide-multi-region-architecture-patterns.md#arch-guide-pattern-5-a-primary-region-with-one-az-for-production-and-secondary-region-containing-a-replica-of-backups-amis "../../../sap/latest/general/arch-guide-multi-region-architecture-patterns.md#arch-guide-pattern-5-a-primary-region-with-one-az-for-production-and-secondary-region-containing-a-replica-of-backups-amis") with backups in another Region
would suffice to meet the RPO and RTO negotiated with the business. Similarly, retaining
multiple backups of SAP test systems that are easily re-created results in the use of
unneeded resources. This extra _insurance_ increases the
environmental impact (along with the cost) beyond what is acceptable for risk mitigation
by the business.

SAP architecture teams can work with the business to negotiate SLAs with
sustainability in mind. For example, rather than having a goal of instantaneous response
for ad hoc queries on an S/4HANA system, a business can dictate that certain queries must
be submitted in batch mode with a much lower SLA for processing. These reports could then
run during periods of lower utilization, reducing the peak processing required and hence
the necessary size of the EC2 instances. As another example, operational SLAs that
prioritize response time over evaluating the environmental impact of the task, such as
overprovisioning storage to avoid having to do so again in the near future, should be
reconsidered with sustainability in mind.

While these changes also align with cost optimization pillar of the SAP Lens,
businesses often prefer higher infrastructure costs when faced with the potential for
lower productivity or increased risk that less stringent SLAs may bring. When a business
prioritizes sustainability, the higher cost of doing business may be acceptable.

- AWS Documentation: [Multi-Region Architecture Patterns](../../../sap/latest/general/arch-guide-multi-region-architecture-patterns.md "../../../sap/latest/general/arch-guide-multi-region-architecture-patterns.md")
- SAP Lens [Performance Efficiency]: [Best Practice 13.1 – Evaluate or
  estimate performance requirements](best-practice-13-1.md "best-practice-13-1.md")
- Well-Architected Framework [Sustainability]: [Align SLAs with sustainability goals](../sustainability-pillar/align-slas-with-sustainability-goals.md "../sustainability-pillar/align-slas-with-sustainability-goals.md")
- Well-Architected Framework [Sustainability]: [Optimize software and architecture for asynchronous and scheduled jobs](../sustainability-pillar/optimize-software-and-architecture-for-asynchronous-and-scheduled-jobs.md "../sustainability-pillar/optimize-software-and-architecture-for-asynchronous-and-scheduled-jobs.md")
  **Suggestion 21.1.3 – Understand how changes to SAP end user
  behavior can result in more sustainable SAP architectures**

Businesses who want to run SAP more sustainably must understand how their end users
are accessing the system regardless of negotiated SLAs. If all users arrive at 9:00 AM and
run large reports simultaneously, this can create a CPU peak that can require resizing to
larger EC2 instances. SAP architecture teams must understand the relationship between SAP
user access patterns and the associated hardware footprint to design an SAP architecture
that minimizes the correlated environmental impact of using more underlying
infrastructure. SAP architecture teams can work with business stakeholders to encourage
changes to user behavior (for example, staggered business start times and financial
chargeback penalties to those with the highest utilization) to promote more sustainable
SAP usage patterns and architectural designs.

Well-Architected Framework [Sustainability]: [User
behavior patterns](../sustainability-pillar/user-behavior-patterns.md "../sustainability-pillar/user-behavior-patterns.md")
