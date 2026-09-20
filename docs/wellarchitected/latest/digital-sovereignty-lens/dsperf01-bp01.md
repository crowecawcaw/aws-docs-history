

# DSPERF01-BP01 Evaluate sovereign solutions using a data-driven approach
<a name="dsperf01-bp01"></a>

 Sovereign workloads require architecture decisions grounded in evidence rather than assumptions. This best practice establishes a three-stage evaluation approach (baseline your sovereignty requirements, define what you expect from your service providers, and document what you need to build on top) that can be tailored to your organization's regulatory environment, risk appetite, and operational maturity. 

 **Desired outcome:** 
+  You have an assessment framework for evaluating sovereign cloud solutions and independent software vendor (ISV) offerings. 
+  Your sovereignty requirements are baselined against each workload. 
+  Your expectations from service providers are defined and documented. 
+  You have a clear record of what is inherited and what you need to implement yourself. 

 **Common anti-patterns:** 
+  Treating a cloud service provider (CSP) solution or independent software vendor (ISV) product as a turnkey answer for digital sovereignty, rather than building a posture around it. 
+  Making architecture decisions without review and approval from legal, compliance, and regional teams who understand jurisdiction-specific requirements. 
+  Failing to document the rationale behind architecture choices, making it difficult to justify decisions to auditors or adapt when requirements change. 

 **Benefits of establishing this best practice:** 
+  Architecture decisions are traceable to documented requirements, supporting audit readiness and regulatory discussions. 
+  Clarity of shared responsibility between what service providers deliver and what you implement, operate, and maintain yourself. 
+  The assessment framework can be reused as new workloads are onboarded or as the organization expands into new jurisdictions. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Sovereignty architecture decisions made without structured evidence tend to result in one of two failure modes. The first is incomplete decomposition: an organization selects a sovereign solution option without first documenting what it needs, what the provider delivers against those needs, and what remains its own responsibility. The second is dimensional conflation: an organization treats sovereignty as a single axis (typically data location) and selects a solution that addresses that one dimension while neglecting others such as continuity and supply chain risks. Both failures result in architectures that can't be traced to requirements or adapted when jurisdictions change. 

 The [introduction](digital-sovereignty-lens.html) to this Lens establishes that sovereignty is a posture built from decisions across products, services, certifications, attestations, and operational practices. These decisions have a logical dependency: defining expectations of a provider requires clarity on your own requirements first, and identifying residual obligations requires understanding what the provider covers. The steps below follow this dependency sequence. An organization adopting the framework for the first time might focus on a single representative workload to build competence before extending across a portfolio. A mature organization with established governance might instead focus on refining existing criteria as it expands into new jurisdictions. 

 AWS provides a continuum of sovereign solution options, from [AWS Regions](https://aws.amazon.com/about-aws/global-infrastructure/) through the [AWS European Sovereign Cloud](https://aws.eu/), [Dedicated Local Zones](https://aws.amazon.com/dedicatedlocalzones/), and [AWS Outposts](https://aws.amazon.com/outposts/), each with a different mix of service availability, operational responsibility, and sovereignty controls. [AWS Artifact](https://aws.amazon.com/artifact/) provides on-demand access to compliance reports and attestations that support evidence gathering. Security and compliance is a [shared responsibility between AWS and the customer](https://aws.amazon.com/compliance/shared-responsibility-model/). AWS is responsible for security *of* the cloud, protecting the infrastructure that runs AWS Cloud services. The customer is responsible for security *in* the cloud, with customer responsibility determined by the AWS Cloud services that a customer selects. In a sovereignty context, this shared responsibility determines where residual sovereignty obligations fall across the continuum of solution options. 

 Each stage of the evaluation involves trade-offs between control, service breadth, and operational burden. Choosing a more localized deployment environment (such as Outposts) places compute and storage at your premises at the cost of [finite capacity that requires planning](https://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/aws-outposts-high-availability-design.html) and additional operational responsibilities including power, networking, and physical security. AWS Regions offer the broadest service availability and include configurable sovereignty controls (such as data residency guardrails, access restrictions, and encryption key management) that organizations tailor to their requirements. The framework is most effective when legal, compliance, and regional stakeholders participate alongside technical teams. 

### Implementation steps
<a name="implementation-steps"></a>

 The following steps are organized in three stages. Steps 1–4 baseline your sovereignty requirements. Steps 5–9 define what you expect from your service providers. Step 10 documents what you need to build on top and establishes ongoing governance. 

 **Note:** The evaluation criteria in each step represent a starting point. Tailor the scope and depth of each step to reflect jurisdiction-specific regulations, organizational structure, and the sovereignty characteristics of your chosen solution options. 

1.  **Identify compliance requirements:** Determine the compliance obligations for each workload within its target jurisdiction. Consider which cybersecurity frameworks, data privacy legislation, and industry-specific regulations apply (for example, [European Union Digital Operational Resilience Act (EU DORA)](https://www.eiopa.europa.eu/digital-operational-resilience-act-dora_en) for financial services, [General Data Protection Regulation (GDPR)](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng) for data privacy). Identify whether operational support staff must be located within a specific jurisdiction or hold security clearances. Determine whether regulatory requirements constrain technology selection, and assess concentration risks this introduces. Establish how compliance will be evidenced on an ongoing basis. 

1.  **Classify workload data:** Understand what data each workload processes, its sensitivity level, and where it is permitted to reside. Determine which data types are subject to data localization and data residency controls. Identify the legal basis governing data transfers between jurisdictions. Map each data type to its permitted storage, processing, transfer, and backup locations. 

1.  **Assess business continuity requirements:** Identify resilience and continuity risks that sovereignty decisions might introduce. Determine whether the workload can tolerate failover to a different jurisdiction or must recover within the same one. Evaluate whether the workload needs to be deployed across multiple AWS Regions, or multiple managed environments, to mitigate dependency on a single jurisdiction or a single geographic region. Consider business continuity risks such as trade barriers, licensing changes, or supply chain dependencies that could affect availability. 

1.  **Align with business objectives:** Confirm how sovereignty requirements connect to broader organizational goals such as geographic expansion or compliance cost reduction. Establish structured processes for evaluating sovereignty requirements when onboarding new workloads and prioritizing investment. Define metrics and key performance indicators (KPIs) that measure the return on investment for sovereignty decisions. 

1.  **Define operational requirements for service providers:** Determine who provides operational support, where they are located, and what access they have to customer content. Clarify whether change control over deployments must be maintained by staff within a specific jurisdiction. Establish whether incidents must be handled by staff within a specific jurisdiction. 

1.  **Establish performance and service requirements:** Identify the infrastructure, application, and analytics services the provider must make available, including service availability in disaster recovery (DR) locations. Evaluate scaling capabilities and the implications if those capabilities vary by solution options. Review service level agreements (SLAs) and pricing models, noting how these vary across sovereign solution options. 

1.  **Define transparency and assurance requirements:** Determine what independent third-party certifications and attestations the provider should hold (for example, [System and Organization Controls (SOC) reports](https://aws.amazon.com/compliance/soc-faqs/), [International Organization for Standardization (ISO) certifications](https://aws.amazon.com/compliance/iso-certified/), jurisdiction-specific attestations such as [Cloud Computing Compliance Criteria Catalogue (C5)](https://aws.amazon.com/compliance/bsi-cloud-computing-compliance-controls-catalogue/)). Identify requirements around network traffic routing within the sovereign boundary, corporate structure, and sub-processor usage. Review whether the provider publishes transparency reports on law enforcement requests, sustainability reports, and service change notifications. 

1.  **Assess interoperability and portability requirements:** Determine whether the workload needs to operate across multiple environments (for example, [AWS Regions](https://aws.amazon.com/about-aws/global-infrastructure/), [Outposts](https://aws.amazon.com/outposts/), or customer-managed infrastructure). Identify regulatory or business requirements mandating migration capability to a different provider or jurisdiction, including acceptable timelines. Evaluate whether the workload should conform to standards-based protocols, storage formats, or open specifications. Document data export requirements including formats, volumes, and transfer time implications. Review contractual provisions for [data portability](https://aws.amazon.com/blogs/aws/free-data-transfer-out-to-internet-when-moving-out-of-aws/). 

1.  **Evaluate service continuity factors:** Review supply chain dependencies that could affect continuity of the service. Examine licensing terms and how changes to those terms are communicated. Assess contractual terms governing the service relationship, including addenda and termination clauses. Identify external dependencies outside the sovereign boundary that could affect the service. 

1.  **Document inherited and self-implemented controls:** Using the answers from the previous steps, produce a responsibility matrix that clearly distinguishes what your service providers deliver from what you need to implement, operate, and maintain yourself. Define the organizational practices, operational processes, and monitoring capabilities needed to maintain your sovereignty posture and support audit readiness. Identify what compliance evidence you need to produce beyond your provider's certifications. Establish periodic review and integrate reassessment into existing governance cycles rather than treating it as a standalone exercise. 

#### Worked example: Financial services workload in the EU
<a name="worked-example-financial-services-workload-in-the-eu"></a>

 **Note:** The following example is illustrative and simplified for clarity. It isn't intended to represent a complete assessment. It isn't legal advice and should not be relied on as such. Regulatory mappings are neither exhaustive nor definitive. Consult your legal and compliance teams when developing your own assessment framework. Don't use these examples to derive compliance positions or architectural decisions. 

 A financial services company based in Germany needs to migrate a customer-facing payments processing workload to the cloud. The workload handles payment card data and personally identifiable information (PII) for EU-based customers. 

##### Stage 1: Baseline sovereignty requirements
<a name="stage-1-baseline-sovereignty-requirements"></a>

 The team identifies the following requirements: 
+  **Compliance:** The workload falls under EU DORA, GDPR, and Payment Card Industry Data Security Standard (PCI DSS). Compliance evidence needs to be produced continuously, not only during audit windows. 
+  **Data sovereignty:** Payment card data and PII are classified as sensitive. Both must remain within the EU for storage, processing, and backup. Cross-border data transfers require a documented legal basis. 
+  **Business continuity:** The regulator requires a documented disaster recovery strategy. Failover to a different EU jurisdiction is acceptable, but failover outside the EU isn't. 
+  **Business objectives:** The company plans to expand into additional EU jurisdictions. The assessment framework needs to support onboarding new jurisdictions without starting from scratch. 

##### Stage 2: Define expectations from service providers
<a name="stage-2-define-expectations-from-service-providers"></a>

 Using the Stage 1 baseline, the team evaluates what the cloud service provider needs to deliver: 
+  **Operations:** Operational support staff with access to the production environment should be EU-resident. Change control for production deployments should be maintained by staff within the EU. 
+  **Availability:** The provider needs to offer the required compute, database, and messaging services in at least two EU locations to support the disaster recovery (DR) strategy. 
+  **Transparency:** The provider should hold SOC 2, ISO 27001, C5, and PCI DSS certifications validated by independent third-party auditors. The team reviews the provider's transparency reports, sub-processor documentation, and critical third-party provider (CTPP) designation status under EU DORA. 
+  **Portability:** The architecture should use open standards where feasible to reduce switching costs. 
+  **Service continuity:** The team reviews contractual terms, licensing, and the Data Processing Agreement to confirm they can meet GDPR and EU DORA requirements. 

##### Stage 3: Document what you need to build on top
<a name="stage-3-document-what-you-need-to-build-on-top"></a>

 The team produces a responsibility matrix (first few lines shown only): 


|  Area  |  Inherited from provider  |  Customer responsibility  | 
| --- | --- | --- | 
|  Data residency controls  |  Region-level configurable data residency controls available  |  Configure to block cross-border replication  | 
|  Compliance evidence  |  Provider certifications (SOC 2, C5, and PCI DSS)  |  Produce workload-specific evidence and automate compliance monitoring  | 
|  Operator access  |  Zero operator access for supported services  |  Design workload so operators don't need access to PII in normal operations  | 
|  Disaster recovery  |  Multi-AZ infrastructure within an AWS Region. Multi-Region within the EU  |  Design cross-Region failover within the EU and test recovery procedures  | 

 The team recommends adopting the AWS European Sovereign Cloud (AWS ESC) as it matches most closely with the requirements. The team notes that AWS ESC can also support potential business expansions into additional EU jurisdictions, as it meets the required data sovereignty requirements. However, the team also notes that the AWS ESC operates out of a single-Region at launch. The team recommends evaluating [sovereign failover options](https://aws.amazon.com/blogs/architecture/sovereign-failover-design-for-digital-sovereignty-using-the-aws-european-sovereign-cloud/) to meet the *at least two EU locations* requirement, or accept Multi-AZ failover support, as a reasonable trade-off. This documentation becomes the basis for the team's sovereignty implementation plan and is reviewed periodically as regulations and the workload evolve. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [PERF01-BP04 Evaluate how trade-offs impact customers and architecture efficiency](https://docs.aws.amazon.com/wellarchitected/latest/framework/perf_architecture_evaluate_trade_offs.html) 
+  [PERF01-BP07 Use a data-driven approach for architectural choices](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_architecture_use_data_driven_approach.html) 
+  [PERF01-BP03 Factor cost into architectural decisions](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_architecture_factor_cost_into_architectural_decisions.html) 
+  [PERF02-BP01 Select the best compute options for your workload](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_compute_hardware_select_best_compute_options.html) 
+  [REL01-BP01 Manage service quotas and constraints](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_manage_service_limits_aware_limits.html) 
+  [DSSEC07-BP01 Enhance your digital sovereignty governance posture](dssec07-bp01.html) 
+  [PERF01-BP01 Learn about and understand available cloud services and features](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_architecture_learn_available_services.html) 
+  [PERF01-BP05 Use policies and reference architectures](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_architecture_use_policies_and_reference_architectures.html) 

 **Related documents:** 
+  [Overview of the AWS European Sovereign Cloud](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-european-sovereign-cloud/introduction.html) 
+  [Exploring the new AWS European Sovereign Cloud: Sovereign Reference Framework](https://aws.amazon.com/blogs/security/exploring-the-new-aws-european-sovereign-cloud-sovereign-reference-framework/) 
+  [AWS Services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/) 
+  [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/) 
+  [AWS Dedicated Local Zones](https://aws.amazon.com/dedicatedlocalzones/) 
+  [AWS Outposts](https://aws.amazon.com/outposts/) 
+  [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/) 
+  [AWS Service Level Agreements](https://aws.amazon.com/legal/service-level-agreements/) 
+  [AWS Data Processing Addendum (DPA)](https://docs.aws.amazon.com/whitepapers/latest/navigating-gdpr-compliance/aws-data-processing-addendum-dpa.html) 
+  [Amazon Information Requests](https://aws.amazon.com/compliance/amazon-information-requests/) 
+  [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/) 
+  [AWS Trust Center](https://aws.amazon.com/trust-center/) 
+  [AWS Sustainability](https://aws.amazon.com/sustainability/) 
+  [AWS Digital Sovereignty Competency Partners](https://aws.amazon.com/compliance/digital-sovereignty/partners/) 