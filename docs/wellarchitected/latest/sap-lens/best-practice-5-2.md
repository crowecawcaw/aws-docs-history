# Best Practice 5.2 – Classify the data

within your SAP workloads

Data sensitivity can impact the controls required to mitigate risk. AWS suggests
referring to standard frameworks within your industry or organization and adopting these
to classify your SAP workloads and the data contained within them.

**Suggestion 5.2.1 - Determine data classification and handling
requirements**

Identify any data classification frameworks already in place in your organization.
These frameworks can help you to categorize data based on the sensitivity of information,
such as data that must be safeguarded for confidentiality, integrity, and availability.
[Standard classification models](../../../whitepapers/latest/data-classification/data-classification-models-and-schemes.md "../../../whitepapers/latest/data-classification/data-classification-models-and-schemes.md") exist,
for example, the US Information Categorization Scheme, that may be customizable based on your
industry, business, or IT requirements.

Understand how data should be handled according to the guidelines appropriate for the
classification. This includes specific security controls related to standards or
regulatory requirements, such as PCI-DSS or GDPR, and common privacy considerations,
such as handling personal identifiable information (PII). The following documents
provide additional information:

- AWS Documentation: [Data Classification: Secure Cloud Adoption Whitepaper](../../../whitepapers/latest/data-classification/data-classification-overview.md "../../../whitepapers/latest/data-classification/data-classification-overview.md")
- AWS Documentation: [General Data Protection Regulation (GDPR) Center](https://aws.amazon.com/compliance/gdpr-center/ "https://aws.amazon.com/compliance/gdpr-center/")
- [NIST
  Security and Privacy Controls for Information Systems and Organizations](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final "https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final")
- [ISO/IEC 27001:2013 FAQs](https://aws.amazon.com/compliance/iso-27001-faqs/ "https://aws.amazon.com/compliance/iso-27001-faqs/")
- Well-Architected Framework [Security]: [Data Protection](../framework/a-data-protection.md "../framework/a-data-protection.md")

**Suggestion 5.2.2 - Identify SAP data types with specific handling
rules**

Based on the business processes supported by your SAP system, there may be
requirements for the handling and storage of data. Familiarize yourself with the guidance
for your location and industry. SAP examples may include:

- Assess whether a digital payments add-on is necessary to protect stored
  cardholder data and ensure PCI compliance.
- Assess HR data for data residency requirements, for example, some countries and
  jurisdictions might require data to be stored within a specific geographical
  location.
- Consider which data may need to be scrambled in non-production systems to obscure
  sensitive data but maintain data integrity.

**Suggestion 5.2.3 - Classify all your workloads according to the
defined framework**

Classify your SAP systems according to their business usage and the existence of
critical data types. Transactional systems such as SAP ERP are more likely to contain
sensitive data than analytical systems such as SAP BW or management systems such as
Solution Manager, although this should be validated by functional and security
experts.

Additionally, assess whether the same controls apply to non-production workloads. For
example, do non-production workloads include production data and therefore must they
adhere to the same security controls?
