# Verifying privacy-by-design

| GL-SEC-01: What privacy<br>practices have you adopted relating to the use of<br>data? |
| ------------------------------------------------------------------------------------- |
|                                                                                       |

- **Elevate encryption beyond the basics:** Cloud
  technologies make it simpler and cost effective to encrypt data. Government
  jurisdictions have specific compliance and data classification requirements. For
  example, they might have hardware or software certification requirements, or require
  that cryptographic controls be managed independently of the cloud service provider’s
  managed encryption services.
  - **Improvement plan** – Leverage encryption to
    protect data at transport and at rest. See the AWS Digital Sovereignty Pledge and
    guidance.

- **Document how privacy and end user control has been
  considered:** The possibilities for a personalized government service
  delivery must be balanced with maintaining end user control and privacy to maintain
  public trust. Government services should be designed to be as private as
  possible. Architects can link to data in place, use verifiable claims and credentials
  where possible, to maintain strong privacy controls and minimize any requirement to
  create new copies of data. Validate that sensitive data is protected, removed, or
  obfuscated to limit exposure. Use detection controls so that the operations team knows
  where sensitive data exists in the service. Access to data should require users and
  systems to demonstrate a strong security posture assessment, enforced with fine-grained
  authorization rules and multiple authentication controls.
  - **Improvement plan** – Encourage the organization
    to consider privacy in the design and management of the service.

- **Give end users appropriate control:** To help alleviate
  privacy concerns, provide end users as much control over their experience as possible.
  This control can include the ability to dial up or down the helpfulness of the service,
  for example, the level of prompting, proactive delivery, or other forms of
  personalization. Be transparent about data storage, use, transmission, and access.
  Modern technologies must allow for continuous and informed consent mechanisms where
  users can be involved in the decision to share their data. Make it simple for end users
  to understand what has been shared, with whom, and for what purpose. Enable them to
  revoke consent at will, and verify that access to the data is immediately restricted. 
  - **Improvement plan** – Encourage the organization
    to consider personal agency in the design and management of the service.

- **Minimize data copies where avoidable:** In some
  circumstances, the ability to link to existing data might not be possible. Make use of
  aggregated data, synthetic data, or both. Use techniques such as verifiable claims or
  confidential computing to verify that the service can be operated with similar data to
  what is expected, while minimizing the risk of exposure or re-identification of
  personally identifiable information (PII).  
  - **Improvement plan** – Identify ways to use data
    that leverages verifiable claims, credentials, anonymization, and APIs for
    consideration by the organization.

- **Enforcing exposure consequences:** Verify that vendor
  contracts inherit these obligations, and use legal and contractual means to prohibit the
  sharing, reuse, or storing of the data for any purpose other than delivering the
  government service.
  - **Improvement plan** – Support the organization to
    assess exposure consequences.
