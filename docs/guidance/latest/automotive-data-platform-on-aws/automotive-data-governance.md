

# Automotive Data Governance
<a name="automotive-data-governance"></a>

The Automotive Data Governance solution demonstrates how to build a multi-region data governance framework that supports EU Data Act and GDPR compliance requirements while enabling global R&D collaboration. This reference implementation shows how to separate PII data processing in EU regions from anonymized analytics in global regions using AWS Lake Formation, AWS Glue, and Amazon Macie.

We demonstrate this pattern because automotive manufacturers operate under a specific constraint: vehicle telemetry contains PII (precise GPS coordinates, driver behavior, biometric signals) that EU regulations require to stay within EU regions, while R&D teams outside the EU need access to the same fleet’s anonymized signals for product development. This solution shows how to implement technical controls that enforce data sovereignty while enabling cross-region analytics through Lake Formation resource links.

For customers using the [CMS](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/developer-guide.html), the normalized telemetry pipeline can feed directly into this governance framework. A Glue ETL job reads from the CMS S3 datalake sink, classifies each field as PII or non-PII, and writes to separate governed data stores. See the integration guide in the [source repository](https://github.com/aws-solutions-library-samples/guidance-for-automotive-data-platform-on-aws) for deployment instructions and field classification details.

**Note**  
This guidance provides technical architecture patterns and AWS service capabilities that support compliance efforts. Customers are responsible for making their own independent assessment of the information and determining whether their use of AWS services complies with applicable laws and regulations. AWS does not provide legal advice, and customers should consult their own legal counsel regarding compliance requirements.

**Note**  
The v0.2 foundation deploy ships a single-region instance of this governance layer — Lake Formation tag-based access control, Macie classification, CloudTrail data-event logging, and IAM Identity Center groups — as the `governance` stack described in [Platform foundation](platform-foundation.md). That foundation stack is the deployable starting point. The multi-region EU/global split described in this chapter (separate EU producer region for PII, global consumer regions with resource links to anonymized data) is pattern guidance for customers who need to extend beyond what the foundation ships out of the box. If your compliance requirements demand cross-border data sovereignty controls — EU Data Act, GDPR data residency, or China PIPL — this chapter describes the broader architectural pattern you would build on top of the foundation’s single-region core.