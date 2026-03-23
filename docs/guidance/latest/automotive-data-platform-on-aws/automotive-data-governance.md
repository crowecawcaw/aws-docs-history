# Automotive Data Governance

The Automotive Data Governance solution demonstrates how to build a multi-region data governance framework that supports EU Data Act and GDPR compliance requirements while enabling global R&D collaboration. This reference implementation shows how to separate PII data processing in EU regions from anonymized analytics in global regions using AWS Lake Formation, AWS Glue, and Amazon Macie.

We demonstrate this pattern because automotive manufacturers face unique challenges: vehicle data contains sensitive PII that must remain in specific regions for compliance, yet R&D teams worldwide need access to anonymized data for product development. This solution shows how to implement technical controls that enforce data sovereignty while enabling cross-region analytics through Lake Formation resource links.

For customers using the [Connected Mobility Guidance](../connected-mobility-on-aws/developer-guide.md "../connected-mobility-on-aws/developer-guide.md"), the normalized telemetry pipeline can feed directly into this governance framework. A Glue ETL job reads from the CMS S3 datalake sink, classifies each field as PII or non-PII, and writes to separate governed data stores. See the integration guide in the [source repository](https://github.com/aws-solutions-library-samples/guidance-for-automotive-data-platform-on-aws "https://github.com/aws-solutions-library-samples/guidance-for-automotive-data-platform-on-aws") for deployment instructions and field classification details.

###### Note

This guidance provides technical architecture patterns and AWS service capabilities that support compliance efforts. Customers are responsible for making their own independent assessment of the information and determining whether their use of AWS services complies with applicable laws and regulations. AWS does not provide legal advice, and customers should consult their own legal counsel regarding compliance requirements.
