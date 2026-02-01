# Definitions

This document contains common definitions and terminology used
across the AWS Well-Architected Digital Sovereignty Lens pillars.

- **Data residency:** The physical
  or geographic location where data is stored and processed. In
  sovereign workloads, this typically means restricting data
  storage and processing to specific AWS Regions within approved
  jurisdictions. For example, an organization subject to European
  regulations might require customer data to remain within
  European Union (EU) regions (like eu-west-1 or eu-central-1) and
  never replicate to regions outside the EU.
- **Data sovereignty:** The concept
  that data is subject to the laws and governance structures of
  the nation or region where it is collected or stored. This
  extends beyond physical location to include legal jurisdiction,
  data access rights, and regulatory adherence. For architects,
  this means designing systems where data handling, encryption key
  management, and operational access comply with local laws, even
  when using global cloud services.
- **General Data Protection Regulation
  (GDPR):** EU regulation on data protection and privacy
  that applies to an organization processing personal data of EU
  residents. Key requirements include data minimization, right to
  erasure, data portability, and mandatory breach notification.
  Solutions must implement technical controls for consent
  management, data deletion, and cross-border transfer
  restrictions.
- **Health Insurance Portability and
  Accountability Act (HIPAA):** US legislation providing
  data privacy and security provisions for safeguarding medical
  information. Requires administrative, physical, and technical
  safeguards including encryption, access controls, audit logging,
  and business associate agreements. Cloud workloads handling PHI
  must implement HIPAA-eligible services and maintain
  comprehensive audit trails.
- **Payment Card Industry Data Security
  Standard (PCI-DSS):** Information security standard for
  organizations that handle credit cards from major card brands.
  Requires network segmentation, encryption of cardholder data,
  regular security testing, access controls, and monitoring.
- **California Consumer Privacy Act
  (CCPA):** California state statute intended to enhance
  privacy rights and consumer protection for California residents.
  Grants consumers rights to know what personal information is
  collected, delete their data, and opt out of data sales.
  Technical implementations require data discovery,
  classification, and automated deletion capabilities.
- **Identity and access management
  (IAM):** Framework for managing identities and access
  permissions. In sovereign contexts, IAM must enforce identity,
  role, and locatiion-based access controls with detailed audit
  logs of access attempts and actions.
- **Attribute-based access control
  (ABAC):** Access control model that uses attributes
  (tags) attached to resources, users, and environment context to
  make authorization decisions. Enables fine-grained permissions
  based on conditions like data classification, user department,
  project, or geographic location. For sovereign workloads, ABAC
  allows dynamic enforcement of data residency by denying access
  to resources tagged with specific regions or sensitivity levels.
  For example, you can create policies that allow users to access
  only resources tagged with their home region or data
  classification level.
- **Role-based access control
  (RBAC):** Access control model based on user roles.
  Simplifies permission management by grouping users into roles
  (such as database administrator, security auditor, or
  application developer) and assigning permissions to roles.
  Critical for sovereign workloads to enforce separation of duties
  and limit access to sensitive data.
- **Multi-factor authentication
  (MFA):** Security process requiring multiple
  verification methods (something you know, something you have,
  something you are) before granting access. Essential for
  sovereign workloads to block unauthorized access, especially for
  privileged operations or access to sensitive data.
- **Least privilege:** Security
  principle of granting only the minimum necessary permissions
  required to perform a specific task. In practice, this means
  using IAM policies, policy boundaries, organization level
  controls, temporary credentials, and just-in-time access rather
  than broad administrative permissions.
- **Zero trust:** Security model
  that requires verification for every access request, regardless
  of whether it originates inside or outside the network
  perimeter. Assumes breach and verifies explicitly using
  identity, device information, location, and other contextual
  information. For sovereign architectures, this means continuous
  authentication and authorization for data access.
- **Preventative controls:**
  Controls designed to block an event from occurring before it
  happens. Examples include service control policies (SCPs) that
  deny launching resources in non-approved regions, IAM policies
  that block cross-region data replication, or network ACLs that
  block traffic to unauthorized destinations.
- **Proactive controls:** Controls
  designed to block the creation of noncompliant resources during
  deployment. Examples include AWS CloudFormation Guard rules that
  validate infrastructure as code template, or AWS Config
  conformance packs that check resource configurations before
  provisioning.
- **Detective controls:** Controls
  designed to detect, log, and alert after an event has occurred.
  Examples include AWS Config rules that identify noncompliant
  resources, AWS CloudTrail logs that record API calls, or Amazon GuardDuty findings that detect suspicious activity. These
  provide visibility and enable rapid response to compliance
  violations.
- **Responsive controls:** Controls
  designed to drive remediation of adverse events or deviations
  from security baselines. Examples include AWS Systems Manager
  Automation documents that automatically remediate noncompliant
  resources, AWS Lambda functions that respond to security
  findings, or AWS Config remediation actions that restore
  compliant configurations.
- **Defense in depth:** Layered
  security approach implementing multiple controls at different
  levels (network, application, data, and identity). If one
  control fails, others provide backup protection. For sovereign
  workloads, this might include network isolation, encryption,
  access controls, and monitoring working together.
- **Key management service (KMS):**
  Service for creating and controlling encryption keys used to
  encrypt data. In sovereign contexts, a KMS must use
  customer-managed keys (CMKs) with key material that never leaves
  the approved region and key policies that restrict access to
  authorized personnel in approved locations.
- **Hardware security module
  (HSM):** Physical device that provides tamper-resistant
  storage and cryptographic operations for encryption keys.
- **Confidential computing:**
  Technology that protects data during processing using isolated
  compute environments such as secure enclaves (like AWS Nitro
  Enclaves). Enables processing of sensitive data while keeping it
  encrypted in memory, protecting against privileged users and
  malicious software.
- **Data loss prevention (DLP):**
  Strategy and tools for blocking unauthorized data transfers or
  exfiltration. Includes content inspection, policy enforcement,
  and blocking of sensitive data transmission through email, web
  uploads, or API calls. Critical for blocking accidental or
  malicious data leakage from sovereign boundaries.
- **Immutable storage:** Storage
  that cannot be modified or deleted for a specified retention
  period. Implemented using features like S3 Object Lock or legal
  hold. Essential for regulatory adherence, forensic
  investigation, and protecting against malicious or un-intended
  deletion.
- **Write once read many (WORM):**
  Storage configuration that allows data to be written once but
  read multiple times, blocking modification or deletion. Used for
  regulatory adherence, legal holds, and archival storage where
  data integrity is paramount.
- **Privacy-enhancing
  technologies:** Technical measures to protect personal
  data while enabling its use. Includes techniques like
  tokenization, pseudonymization, differential privacy,
  homomorphic encryption, and secure multi-party computation.
  Allows organizations to derive value from data while minimizing
  privacy risks.
- **Protected health information
  (PHI):** Health information that can be linked to a
  specific individual, including medical records, treatment
  information, and payment data. Subject to HIPAA regulations
  requiring strict access controls, encryption, and audit logging.
- **Personally identifiable information
  (PII):** Data that can identify a specific individual,
  such as names, email addresses, social security numbers, or IP
  addresses. Requires special handling under various privacy
  regulations including GDPR, CCPA, and sector-specific laws.
- **Data classification:** The
  process of categorizing data based on sensitivity levels (such
  as public, internal, confidential, or restricted). In sovereign
  architectures, classification drives technical controls like
  encryption requirements, access restrictions, geographic
  boundaries, and retention policies. For example, PII might
  require encryption at rest and in transit, while public data
  might have fewer restrictions.
- **Data lineage:** The ability to
  track data movement and transformations throughout its
  lifecycle, from creation through processing, storage, and
  eventual deletion. This is critical for sovereignty as it
  provides auditable evidence that data never left approved
  boundaries and was processed according to regulatory
  requirements.
- **Content delivery network
  (CDN):** Distributed network of servers that deliver
  content to users based on geographic location. For sovereign
  workloads, CDNs must be configured to serve content only from
  approved regions and block caching of sensitive data in
  unauthorized locations.
- **Failover:** Process of
  switching to a redundant or standby system upon failure of the
  primary system. In sovereign architectures, failover targets
  must be in approved regions, and failover procedures must adhere
  to data residency requirements throughout the recovery process.
- **Mean Time to Recovery (MTTR):**
  Average time required to repair a failed component or system and
  restore service. Critical metric for business continuity
  planning.
- **Business continuity:**
  Capability of an organization to continue delivery of products
  or services at acceptable predefined levels following a
  disruptive incident. For sovereign workloads, continuity plans
  must account for regional constraints, locality of operational
  teams, and regulatory requirements during disaster scenarios.
- **Audit trail:** Chronological
  record of system activities that provides documentary evidence
  of operations, procedures, or events. Must be tamper-proof,
  comprehensive, and retained according to regulatory
  requirements. Includes logs of data access, configuration
  changes, authentication events, and administrative actions.
- **Data protection authority
  (DPA):** Regulatory body overseeing data protection
  regulations within a jurisdiction (such as CNIL in France or ICO
  in the UK). Organizations must report data breaches to the
  relevant DPA and may be subject to audits and enforcement
  actions.
- **Third-party risk management
  (TPRM):** Process of identifying, assessing, and
  mitigating risks associated with third-party vendors and service
  providers. Critical for sovereign workloads to verify that
  vendors meet data residency requirements, have appropriate
  security controls, and comply with relevant regulations.
- **Open protocols:** Publicly
  documented communication standards that enable interoperability
  between systems from different vendors. Examples include HTTPS,
  SMTP, and SAML. Important for sovereign architectures to avoid
  vendor lock-in and enable portability across cloud providers or
  on-premises infrastructure.
- **Open data formats:** Publicly
  documented file and data formats that can be read and written by
  multiple tools and platforms without proprietary restrictions.
  Examples include JSON, XML, CSV, Parquet, and ORC. Critical for
  sovereign workloads to maintain data portability and
  interoperability.
- **Open table formats:**
  Vendor-neutral table formats that provide ACID transactions,
  schema evolution, and time travel capabilities for data lakes.
  Examples include Apache Iceberg, Apache Hudi, and Delta Lake
  (with open-source version). These formats enable
  interoperability across different compute engines (like Spark,
  Presto, or Flink) and cloud platforms, allowing organizations to
  avoid lock-in to proprietary data warehouse software. For
  sovereign architectures, open table formats facilitate data
  portability, and provide flexibility to change analytics
  platforms while maintaining data sovereignty requirements.
