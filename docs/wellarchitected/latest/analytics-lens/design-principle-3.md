# 3 – Designing data platforms for governance and compliance

**How do you protect data in your
organization’s analytics workload?** Privacy by
Design (PbD) is an approach in system engineering that takes
privacy into account throughout the whole engineering process.
PbD especially focuses on systems or applications that capture
and process personal data. Many countries or political unions
enforce data protection regulations. The main data protection
regulations are: GDPR (General Data Protection Regulation),
CCPA (California Consumer Privacy), LGPD (Lei geral da
Protecao de Dados Pessoasis in Brazil), POPIA (South Africa),
Australian Privacy Act and DPA (UK Data Protection Act).

As an organization you must have an understanding what data
protection regulations you must adhere to and implement them
into your solution accordingly. If your organization operates
across territories, then you must adhere to multiple data
regulations.

This whitepaper covers the common themes shared amongst these
regulations; however this is not an exhaustive list. Therefore
you must consult your organization’s Data Protection Office to
determine what additional regional and company-wide data
protection and data governance requirements must be
implemented.

For more details regarding the different types of data
protection regulations, refer to the following:

- GDPR -
  [General
  Data Protection Regulation Center](https://aws.amazon.com/compliance/gdpr-center/ "https://aws.amazon.com/compliance/gdpr-center/")
- CCPA -
  [California
  Consumer Privacy Act](https://aws.amazon.com/compliance/california-consumer-privacy-act/ "https://aws.amazon.com/compliance/california-consumer-privacy-act/")
- LGPD -
  [The
  General Data Protection Law](https://aws.amazon.com/blogs/security/lgpd-workbook-for-aws-customers-managing-personally-identifiable-information-in-brazil/ "https://aws.amazon.com/blogs/security/lgpd-workbook-for-aws-customers-managing-personally-identifiable-information-in-brazil/")
- POPIA -
  [South
  Africa Data Privacy](https://aws.amazon.com/compliance/south-africa-data-privacy/ "https://aws.amazon.com/compliance/south-africa-data-privacy/")

| **ID**      | **Priority** | **Best practice**                                                                               |
| ----------- | ------------ | ----------------------------------------------------------------------------------------------- |
| ☐<br>BP 3.1 | Required     | Privacy by design.                                                                              |
| ☐<br>BP 3.2 | Required     | Classify and protect data                                                                       |
| ☐<br>BP 3.3 | Required     | Understand data classifications and their protection<br>policies.                               |
| ☐<br>BP 3.4 | Required     | Identify the source data owners and have them set the<br>data classifications.                  |
| ☐<br>BP 3.5 | Required     | Record data classifications into the Data Catalog so<br>that analytics workload can understand. |
| ☐<br>BP 3.6 | Required     | Implement encryption policies.                                                                  |
| ☐<br>BP 3.7 | Required     | Implement data retention policies for each class of data<br>in the analytics workload.          |
| ☐<br>BP 3.8 | Recommended  | Enforce downstream systems to honor the data<br>classifications.                                |

For more details, refer to the following information:

- AWS GDPR Center:
  [Introducing
  the New GDPR Center and “Navigating GDPR Compliance on AWS”
  Whitepaper](https://aws.amazon.com/blogs/security/introducing-the-new-gdpr-center-and-navigating-gdpr-compliance-on-aws-whitepaper/ "https://aws.amazon.com/blogs/security/introducing-the-new-gdpr-center-and-navigating-gdpr-compliance-on-aws-whitepaper/")
- AWS Database Blog:
  [Best
  practices for securing sensitive data in AWS data
  stores](https://aws.amazon.com/blogs/database/best-practices-for-securing-sensitive-data-in-aws-data-stores/ "https://aws.amazon.com/blogs/database/best-practices-for-securing-sensitive-data-in-aws-data-stores/")
- AWS Security Blog:
  [Discover
  sensitive data by using custom data identifiers with Amazon Macie](https://aws.amazon.com/blogs/security/discover-sensitive-data-by-using-custom-data-identifiers-with-amazon-macie/ "https://aws.amazon.com/blogs/security/discover-sensitive-data-by-using-custom-data-identifiers-with-amazon-macie/")
- Amazon Macie User Guide:
  [What
  is Amazon Macie?](../../../macie/latest/user/what-is-macie.md "../../../macie/latest/user/what-is-macie.md")
- AWS Key Management Service Developer Guide:
  [What
  is AWS Key Management Service?](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md")
- AWS Whitepaper:
  [Data
  Classification: Secure Cloud Adoption](../../../whitepapers/latest/data-classification/welcome.md "../../../whitepapers/latest/data-classification/welcome.md")
- AWS Clean Rooms: [What is AWS Clean Rooms](../../../clean-rooms/latest/userguide/what-is.md "../../../clean-rooms/latest/userguide/what-is.md")
