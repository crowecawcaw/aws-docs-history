

# Digital Sovereignty Lens - AWS Well-Architected Framework
<a name="digital-sovereignty-lens"></a>

Last updated: **September 15, 2026** ([Release notes](release-notes.md))

 The Digital Sovereignty Lens helps you design, build, and operate sovereign workloads on AWS. It provides best practices and guidance for four of the six pillars of the AWS Well-Architected Framework: operational excellence, security, reliability, and performance efficiency. The cost optimization and sustainability pillars are covered by existing Well-Architected guidance. 

## Why this lens
<a name="why-this-lens"></a>

 In our customer conversations, sovereignty discussions tend to stall on hypothetical scenarios rather than driving clear next steps. Legal, compliance, and engineering teams lack a common language. Requirements vary by jurisdiction, and what applies in one country might not apply in another. Digital sovereignty is a multi-disciplinary subject, not just a technical one. A sovereign workload requires input from compliance, security, legal, and IT teams throughout its lifecycle. 

 This lens provides a [risk-based framework](https://docs.aws.amazon.com/wellarchitected/latest/userguide/identify-and-understand-risks.html#managing-risks) that grounds the conversation in evidence, helping you prioritize investments where the regulatory and operational impact is highest. Import the Lens into the [AWS Well-Architected Tool](https://docs.aws.amazon.com/wellarchitected/latest/userguide/intro.html) and [run a review](https://docs.aws.amazon.com/wellarchitected/latest/userguide/running-a-wafr.html) to [identify high and medium risk issues](https://docs.aws.amazon.com/wellarchitected/latest/userguide/identify-and-understand-risks.html). From there, [prioritize and create targeted improvement plans](https://docs.aws.amazon.com/wellarchitected/latest/userguide/improving-your-workload.html). 

## What is a sovereign workload
<a name="what-is-a-sovereign-workload"></a>

 Digital sovereignty means different things to different people. There is no single definition. By listening to customers, partners, and regulators, we have identified four recurring themes: 
+  **Data residency:** You want to know where your data is stored, and control where it is transferred to. 
+  **Operator access restriction:** You want to be sure about who can access your data in the cloud. 
+  **Resiliency and survivability:** You want to sustain operations despite political, economic, and regulatory instability, natural disasters, and technical failures. 
+  **Independence and transparency:** You want to be sure that your data in the cloud meets the operational and assurance requirements of your regulated industry, sector, or location, and that you can deploy your workloads to an environment of your choice. 

 Digital sovereignty requirements tend to coalesce around one or more of these themes. Which themes apply, and to what degree, depend on the jurisdiction, the workload characteristics, and the sector it operates in. 

 The themes describe what customers ask for. To design and test against these requirements, the next section translates them into five architectural questions. 

## Five questions that define a sovereign workload
<a name="five-questions-that-define-a-sovereign-workload"></a>

 A workload can be functionally complete and still not meet a sovereignty requirement. Sovereignty adds five questions to your architecture review, each answered within a specific jurisdiction: 

1.  **Where is my workload located?** (Locality): Where your workloads execute, where data is stored and transferred, and where the people who operate them are located. 

1.  **Who can reach it?** (Access control): Who can access data, from where, and under what authority. 

1.  **Will my workload keep working when conditions change?** (Continuity): How the workload survives technical failures, regulatory changes, geopolitical events, and supply-chain disruption. Continuity encompasses technical resilience but extends to the non-technical forces that can disrupt operations. 

1.  **Can this workload be transferred elsewhere?** (Portability and Interoperability): Whether you can operate across, or exit to, other environments of your choice. 

1.  **Can you prove sovereignty controls are in place?** (Transparency and auditability): What controls and evidence demonstrate the other four are in effect. 

 Which of these questions applies, and to what degree, depends on your jurisdiction and organizational goals. Not all five carry equal weight in every context. 

## Trade-offs and influences
<a name="trade-offs-and-influences"></a>

 The five design concerns trade off and influence one another. 

 **Trade-offs:** A strict residency mandate (*locality*) can limit cross-Region recovery options (*continuity*). Trade-offs can also occur within the same concern. Reducing dependency on a provider due to potential pricing changes addresses one continuity risk but can introduce another. For example, a less mature replacement may bring its own availability concerns. 

 **Influences:** When you choose a service to improve interoperability, its availability across jurisdictions (*continuity*) may shape that choice. Similarly, access control decisions are informed by where data is stored and how it is accessed (*locality*). 

 When you design a sovereign workload, you decide which concern takes precedence, which risk within a concern to accept, and why. Transparency and auditability are the exception. They don't compete with the other four. They prove the other four are in effect. 

 These trade-offs and influences are no different from what you consider when evaluating workloads against the six pillars of the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/). 

## Sovereignty is a posture, not a product
<a name="sovereignty-is-a-posture-not-a-product"></a>

 The AWS Cloud is [sovereign-by-design](https://aws.amazon.com/blogs/security/tag/sovereign-by-design/). While the AWS Cloud provides the necessary foundations, a strong sovereignty posture depends on the locality, access control, continuity, transparency and auditability, and portability and interoperability design concerns unique to your workloads. You implement controls proportionate to your data sensitivity, supported by organizational practices and operational processes to maintain them continuously. 

## Digital sovereignty in practice
<a name="digital-sovereignty-in-practice"></a>

 Building on the [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/), the following areas describe what AWS provides and what you build on top. 

### Locality
<a name="locality"></a>

 Locality covers where your workloads run, where data is stored and transferred, and where the people who operate them are located. It is the first question most customers think of when discussing sovereignty requirements. 

 **What AWS provides:** AWS operates [Regions](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/) in multiple geographic areas around the world. You select Regions that match your jurisdictional requirements and use controls to restrict workloads to those Regions. [AWS Control Tower digital sovereignty controls](https://docs.aws.amazon.com/controltower/latest/controlreference/digital-sovereignty-controls.html) enhance your digital sovereignty governance posture across data residency, granular access, encryption, and resiliency. The [AWS European Sovereign Cloud](https://aws.eu/) is an independent cloud for Europe, designed to help public sector organizations and customers in highly regulated industries meet their evolving sovereignty and compliance needs. [AWS Outposts](https://aws.amazon.com/outposts/) extends AWS infrastructure to your own data center when on-premises residency is required. 

 **What you build on top:** You are responsible for classifying data by residency requirement, selecting Regions accordingly, and enforcing that workloads and data do not leave approved boundaries. Implement Region-deny SCPs, tag resources with residency metadata, and use detective controls to alert on configuration drift. Define and enforce policies for where operating personnel can access workloads from, including restrictions on remote access by jurisdiction. 

### Access control
<a name="access-control"></a>

 Access control in sovereign workloads combines technical and operational controls you apply with capabilities, commitments, and contractual clauses from your cloud service provider. 

 **What AWS provides:** The AWS access control measures include services designed with [zero operator access](https://aws.amazon.com/trust-center/operator-access/), consistent application of the principle of least privilege, continuous monitoring, separation of duties, and secure data centers, providing defense in depth. The [SOC 1, 2, and 3 reports](https://aws.amazon.com/blogs/security/fall-2025-soc-1-2-and-3-reports-are-now-available-with-185-services-in-scope/) and the European Sovereign Cloud [SOC 2 Type 1 and C5 Type 1 reports](https://aws.amazon.com/blogs/security/aws-european-sovereign-cloud-achieves-first-compliance-milestone-soc-2-and-c5-reports-plus-seven-iso-certifications/) detail these measures as well. The [AWS Security Blog](https://aws.amazon.com/blogs/security/) provides updates on certifications and attestations, including posts such as [Five facts about how the CLOUD Act actually works](https://aws.amazon.com/blogs/security/five-facts-about-how-the-cloud-act-actually-works/). 

 Zero operator access is a design principle for how AWS operates its infrastructure and services. You are responsible for designing workloads so your operators don't need access to customer data in the normal course of operations, and for applying time-bound, session-level controls and audit trails where exceptions are necessary. 

 **What you build on top:** Sovereignty adds jurisdictional controls to your security baseline. AWS Cloud provides capabilities you use to apply and maintain verifiable access control over your workloads: 
+  [Monitor, route, and filter traffic](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/welcome.html): Set up routing and inspection points to monitor, channel, and filter East-West (VPC-to-VPC) and North-South (internet ingress and egress) traffic. Use Security Groups and AWS Network Firewall to control traffic entering and leaving your network. 
+  [Data Perimeter on AWS](https://docs.aws.amazon.com/whitepapers/latest/building-a-data-perimeter-on-aws/building-a-data-perimeter-on-aws.html): Use policies to make sure that only *trusted identities* access *trusted resources* from *expected networks*. 
+  [Resource configuration checks](https://docs.aws.amazon.com/cfn-guard/latest/ug/what-is-guard.html): Use [AWS CloudFormation Guard](https://docs.aws.amazon.com/cfn-guard/latest/ug/writing-rules.html) to validate infrastructure templates against compliance policies before deployment. Write rules that check for data residency tags, Region restrictions, and encryption configurations. Integrate them into your continuous integration and continuous delivery (CI/CD) pipelines to block potentially noncompliant or insecure resources before they are provisioned. 
+  [Automated reasoning tools](https://aws.amazon.com/security/provable-security/): Use security assurance backed by mathematical proof (*provable security*) to verify that your access control policies work as intended. [AWS Identity and Access Management (IAM) Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) validates [IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-validation.html) and identifies resources shared with external entities. [VPC Network Access Analyzer](https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/what-is-network-access-analyzer.html) verifies that network configurations match your intended connectivity, helping you detect unintended paths that could cross jurisdictional boundaries. 
+  [Controls around encryption](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html): Use AWS Key Management Service (AWS KMS) with options for [customer managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-mgn-key), [AWS CloudHSM](https://docs.aws.amazon.com/cloudhsm/latest/userguide/introduction.html), and [external key stores (XKS)](https://docs.aws.amazon.com/kms/latest/developerguide/keystore-external.html) for maintaining control over encryption keys within approved jurisdictions. 

### Continuity
<a name="continuity"></a>

 Sovereign workloads are expected to sustain operations despite geopolitical instability, natural disasters, and technical failures. This extends to having continued access to infrastructure, services, and skills required to support your operations. Plan for disruptions beyond technical failures, including changes in the conditions under which your workload is permitted to operate. 

 Regulations such as the EU Digital Operational Resilience Act (EU DORA) address operational resilience for financial entities and their critical ICT providers, making resilience both a compliance consideration and a business necessity in regulated sectors. 

 **What AWS provides:** [AWS Regions](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/), Availability Zones, and [fault isolation boundaries](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/abstract-and-introduction.html) support a wide range of resilience strategies. The [Disaster Recovery of Workloads on AWS whitepaper](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html) describes four strategies (backup and restore, pilot light, warm standby, and multi-site active-active) each aligning with different recovery time objective (RTO) and recovery point objective (RPO) targets. 

 **What you build on top:** Resilience is a design outcome, not a service you enable. You are responsible for defining recovery objectives, architecting for fault isolation, and testing recovery paths. Reconcile residency constraints with recovery strategies. A strict locality mandate can limit cross-Region DR options, so your recovery architecture should account for jurisdictional boundaries. Use [AWS Resilience Hub](https://docs.aws.amazon.com/resilience-hub/latest/userguide/what-is.html) to define, validate, and track resilience against your recovery objectives. Use [AWS Fault Injection Service](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html) to run controlled fault injection experiments that test how your sovereign workloads respond to disruptions, including Region-level failures and dependency disruptions. Use [AWS Observability and Monitoring](https://aws.amazon.com/cloudops/monitoring-and-observability/) services to understand how your workloads fail under various scenarios. 

### Portability and interoperability
<a name="portability-and-interoperability"></a>

 Portability and interoperability concern whether you can operate across, or exit to, other environments of your choice. This matters when regulations change, when contractual terms shift, or when organizational strategy calls for multi-environment flexibility. 

 **What AWS provides:** AWS services expose consistent APIs across Regions where they are available, so a workload built for one Region can typically be deployed to another using the same tools and interfaces. Interoperability and portability planning builds on this foundation and extends to scenarios that require deployment to environments outside AWS. AWS offers services built on open and widely adopted technologies: [Amazon EKS](https://aws.amazon.com/eks/) (Kubernetes), [Amazon MSK](https://aws.amazon.com/msk/) (Apache Kafka), [Amazon RDS](https://aws.amazon.com/rds/) (PostgreSQL, MySQL, MariaDB), [Amazon MQ](https://aws.amazon.com/amazon-mq/) (Apache ActiveMQ, RabbitMQ), [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/) (OpenSearch), and [Apache Iceberg integration in AWS analytics services](https://aws.amazon.com/big-data/datalakes-and-analytics/apache-iceberg-on-aws/). These open foundations give you the option to port workloads to other environments when sovereignty requirements change, though the effort varies by your workload's dependencies. 

 **What you build on top:** You are responsible for designing workloads with portability and interoperability as explicit goals where your risk model requires it. This includes selecting services that use standards-based interfaces, abstracting architectural and AWS Region-specific dependencies, maintaining documented exit plans, regularly testing backup and migration plans, and evaluating that your alternative environment choices remain viable. 

### Transparency and auditability
<a name="transparency-and-auditability"></a>

 Sovereignty without evidence is only an assertion. Transparency demands visibility into what controls exist and how they operate at scale. Auditability means producing verifiable evidence continuously, not only during audit windows. 

 Compliance obligations play a leading role in determining sovereignty requirements. These requirements originate from: 
+  Cybersecurity related directives, standards, and guidelines (for example, [NIS 2](https://digital-strategy.ec.europa.eu/en/policies/nis2-directive) is a directive, and [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) is a standard and a framework). 
+  Data privacy legislation (for example, [Regulation (EU) 2016/679](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679#tit_1), also known as the European Union General Data Protection Regulation (GDPR)). 
+  Industry or sectoral regulations (for example, the [Health Insurance Portability and Accountability Act (HIPAA)](https://www.hhs.gov/hipaa/for-professionals/index.html) is a US federal law that protects sensitive patient health information (PHI), and the EU [Digital Operational Resilience Act](https://www.eiopa.europa.eu/digital-operational-resilience-act-dora_en) (EU DORA) establishes operational resilience requirements for the EU financial sector). 

 **What AWS provides:** AWS demonstrates its security commitments through globally recognized certifications, including ISO 27001, ISO 27017, ISO 27018, SOC 1/2/3, PCI DSS Level 1, and C5, regularly validated by independent third-party auditors. Visit the [AWS Trust Center](https://aws.amazon.com/trust-center/) for details, or access reports directly from [AWS Artifact](https://aws.amazon.com/artifact/). These reports provide inherited evidence that can support your own audit activities. [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) records API activity across your accounts. [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) continuously records resource configurations and alerts you when a resource drifts from baseline. 

 **What you build on top:** Compliance is not just a point-in-time exercise. You are responsible for maintaining a compliance catalog that maps your obligations to implemented controls, automating enforcement through Compliance as Code, and producing evidence continuously, not only during audit windows. The AWS Well-Architected Framework and this Lens provide guidance on baselining your [compliance requirements](https://docs.aws.amazon.com/whitepapers/latest/aws-risk-and-compliance/shared-responsibility-model.html), automating through Compliance as Code (CaC), and detecting and remediating noncompliant resources continuously. 

## How this Lens is organized
<a name="how-this-lens-is-organized"></a>

 The Digital Sovereignty Lens maps sovereignty requirements to four of the six pillars of the AWS Well-Architected Framework: 
+  **Operational excellence** – How do you organize, prepare, operate, and evolve your compliance function across jurisdictions? 
+  **Security** – How do you protect data, control access, detect threats, and respond to incidents within sovereign boundaries? 
+  **Reliability** – How do you plan for business continuity, manage vendor risks, and design for interoperability when jurisdictional conditions change? 
+  **Performance efficiency** – How do you select the right sovereign solution for each workload? 

 The Lens doesn't provide best practices for the Cost Optimization and Sustainability pillars. Best practices already defined in the Well-Architected Framework under those pillars apply to sovereign workloads as well. 

## Scope
<a name="scope"></a>

 A sovereign workload addresses the five design concerns: locality, access control, continuity, transparency and auditability, and interoperability and portability. However, not every workload needs each design concern to the same degree. For example, you might not invest in interoperability and portability initially, choosing instead to focus on locality and access control. 

 The Digital Sovereignty Lens provides a framework to design workloads that address sovereignty requirements while using the flexibility of the AWS Cloud. Digital sovereignty requirements evolve globally, and AWS, along with [partners](https://aws.amazon.com/compliance/digital-sovereignty/partners/), can help you navigate your digital sovereignty needs. 

## Lens availability
<a name="lens-availability"></a>

 To begin reviewing your workload from a digital sovereignty perspective, download and import the [Digital Sovereignty Lens](https://github.com/aws-samples/sample-well-architected-custom-lens/blob/main/digital-sovereignty-lens/digital-sovereignty-lens.json) into AWS WA Tool from the public [AWS Well-Architected custom lens GitHub repository](https://github.com/aws-samples/sample-well-architected-custom-lens). 