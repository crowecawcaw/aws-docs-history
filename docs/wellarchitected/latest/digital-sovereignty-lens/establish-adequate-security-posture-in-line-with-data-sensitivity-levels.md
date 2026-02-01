# Establish adequate security posture in line with data sensitivity levels

With an ever-increasing number of data-intensive workloads, organizations want full
visibility of where data is stored, control how and with whom data is shared, and audit who
has access and for what duration.

**Key challenges:**

- Managing data at scale requires improving the discoverability, understandability,
  accessibility, and trustworthiness of individual datasets. At the same time, most
  jurisdictions require adherence to strict data privacy legislations, data protection
  requirements, and specific data residency mandates.
- Inadequate protection of citizens' data exposes businesses to severe financial and
  reputational damage when personally identifiable information (PII), protected health
  information (PHI), or confidential information is compromised. Organizations remain
  cautious about migrating to the cloud due to perceived control concerns, often selecting
  on-premises solutions that deliver less speed and flexibility than cloud alternatives.
- Organizations apply a defense in depth strategy to authorize access to data, a best
  practice that aligns with secure by design principles. However, as use cases multiply, the
  number of policies also increases rapidly. This proliferation of policies creates
  technical debt, policy overlaps, and security gaps that pose challenges for data access
  governance.

**Key practices:**

Consider the following key practices to meet the challenges outlined above.

- **Locate and classify sensitive data:** Locate sensitive data
  using automated discovery, classification, and cataloging, augmented with
  human-in-the-loop processes. Build an exhaustive data inventory.
- **Apply security and privacy controls:** Define trust
  boundaries by implementing strict access permissions and network controls. Restrict
  sensitive information sharing to verified accounts and environments. Apply data
  obfuscation techniques like tokenization or masking to balance data utility with security
  controls. Verify access models by analyzing who has access to what, and reconcile this
  with actual operational and business needs.
- **Track data flows:** Track data movement both across and
  within trust boundaries. Monitor traffic within network segments and across private and
  public facing network interfaces. Use data lineage software to track information flow
  through data pipelines and storage systems.
- **Validate and improve controls:** Use threat modeling to
  verify the effectiveness and coverage of security and privacy controls applied to protect
  sensitive data. Source and integrate threat intelligence to augment threat detection.
- **Build evidence:** Retain network flow logs, usage logs,
  access logs, application logs, and security findings for the long-term aligning with
  regulatory needs. Use immutable storage options (write once read many (WORM)) to protect
  the chain of evidence. Retain access-related audit trails long-term.
- **Build in privacy and transparency:** Implement consent
  management systems to track user preferences for personal data use. Collect only what is
  required, and clearly inform users about how data is collected, processed, and retained.
  Create data retention policies that comply with regulations and delete data when no longer
  needed. Build systems that support user rights protection as mandated by data privacy
  legislations, including data access, correction, deletion, and portability. Consider
  conducting data protection impact assessments (DPIAs) to identify privacy risks involved
  in processing personal data.
