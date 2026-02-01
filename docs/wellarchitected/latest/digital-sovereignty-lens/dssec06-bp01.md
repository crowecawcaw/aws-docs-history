# DSSEC06-BP01 Classify data with sovereignty attributes

Data sovereignty attributes are typically derived from storage,
processing, retention, handling, geo-location, transmission and
access control requirements. Attach these attributes as metadata to
your datasets. When combined with data classification tags, these
attributes can be utilized to enforce policy as code (PaC), build
verifiable IAM policies and implement fine grained access controls.
Metadata is typically expressed as labels, tags or model parameters
and is attached to your resources.

**Desired outcome:** Data is
classified and tagged with jurisdiction-specific sovereignty
attributes that govern storage, processing, retention, geo-location,
transmission, and access.

**Common anti-patterns:**

- Relying on manual processes or periodic batch jobs to discover,
  classify and analyse data. This leads to gaps in coverage and
  delayed detection of compliance violations.
- Classification and analysis rules are not reviewed and updated
  periodically to support new data types, regulatory changes, or
  evolving business requirements.
- Even when data is classified, additional data sovereignty
  attributes are not baselined, leading to privacy violations and
  financial penalties.

**Benefits of establishing this best
practice:**

- Security controls can be calibrated to sensitivity levels, data
  sovereignty requirements arrived through rules-based evaluations
  rather than subjective opinions.
- Automated classification and analysis supports consistent
  application of security and privacy controls across your
  environment.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Data sovereignty related requirements are not typically confined
to within a single compliance framework. Instead, they are spread
over multiple frameworks, industry-specific regulations (such as
HIPAA and PCI DSS), sovereign legislations, and local government
policies. They can also materialize through amendments to existing
regulations.

Consider the following while automating the discovery and
qualification of data sovereignty requirements:

- Apply rules-based evaluation methods. Rules evaluate and set
  metadata related to data sovereignty and not just attach data
  sensitivity labels.
- Include a human in the loop (HTIL) step when rules are
  probabilistic. For example, in the case of AI/ML or large
  language model (LLM) based evaluations.
- Implement modular, event-driven data pipelines that
  automatically trigger discovery, analysis and classification
  workflows when new data is created or ingested. A modular
  design allows you to customize classification and analysis
  logic as regulations evolve.

### Implementation steps

The implementation steps below use AWS services including Amazon Macie for automated sensitive data discovery, AWS Glue for data
cataloging and extract, transform, load (ETL) operations, Amazon EventBridge for event routing, and AWS Step Functions for
orchestrating data pipelines. These services integrate to create
resilient, scalable pipelines and can handle diverse data
sources and formats. You can also use alternative ISV tools to
achieve similar outcomes.

1. **Set up a data classification
   model:**
   - Establish a consistent data classification model in line
     with the cybersecurity and privacy requirements of the
     jurisdiction where the data will be stored. For more
     detail, see
     [data
     classification models and schemes](../../../whitepapers/latest/data-classification/data-classification-models-and-schemes.md "../../../whitepapers/latest/data-classification/data-classification-models-and-schemes.md").
   - Review classification models with your designated data
     protection officer (DPO) and data privacy experts.
     Having designated data steward and data owner roles may
     assist in streamlining this process.

2. **Map data classification levels to
   data sovereignty attributes:** Establish clear
   mapping between your classification levels and
   jurisdiction-sensitive data sovereignty attributes. For
   example, data classified as unrestricted (lowest level)
   would have different data sovereignty attributes than data
   classified as sensitive (highest level).
3. **Automatically trigger
   classification**:
   - Configure EventBridge to capture data lifecycle events
     from sources like Amazon S3, Amazon RDS, and Amazon DynamoDB.
   - Set up EventBridge rules to trigger classification and
     analytics workflows when new data is generated or
     ingested.

4. **Deploy modular classification
   components**: Depending on the type of data
   (structured, unstructured) consider using one or more of the
   following options.
   - Use Amazon Macie to automatically
     [discover
     and classify sensitive data types](../../../macie/latest/user/discovery-jobs.md "../../../macie/latest/user/discovery-jobs.md") including
     Personally Identifiable Information (PII), Protected
     Health Information (PHI), and other confidential
     information. The
     [Macie
     documentation](../../../macie/latest/user/discovery-asdd.md "../../../macie/latest/user/discovery-asdd.md") provides a detailed step-by-step
     walkthrough on how to configure automated sensitive data
     discovery. Going beyond default settings and
     [managed
     data identifiers](../../../macie/latest/user/discovery-jobs-mdis-recommended.md "../../../macie/latest/user/discovery-jobs-mdis-recommended.md"), you can also set up custom
     identifiers to detect sensitive data patterns unique to
     your workloads.
   - Implement AWS Glue crawlers to discover data schemas and
     populate the AWS AWS Glue Data Catalog. Then use the
     [Glue
     PII detect functionality](../../../glue/latest/dg/detect-PII.md "../../../glue/latest/dg/detect-PII.md") to detect PII, PHI, and
     other confidential data within Glue-registered tables.
   - Configure
     [Amazon Comprehend](https://aws.amazon.com/comprehend/ "https://aws.amazon.com/comprehend/"), or
     [Amazon Comprehend Medical](https://aws.amazon.com/comprehend/medical/ "https://aws.amazon.com/comprehend/medical/") for advanced text analysis and
     entity recognition over unstructured data.
   - Deploy AWS Lambda functions for custom classification
     logic specific to your industry or regulatory
     requirements.
   - Regardless of which method or AWS services you use, the
     evaluation logic must utilize the jurisdiction-aware
     data classification model described in the first step.

5. **Trigger post-classification
   enrichment jobs**:
   - Run metadata enrichment jobs to apply additional data
     sovereignty tags.
   - Establish a consistent tagging taxonomy in line with
     your data classification model and data sovereignty
     attributes.
   - Set up EventBridge to trigger enrichment jobs, post
     classification. You can then apply downstream processing
     rules to attach one or more data sovereignty related
     tags. Lambda functions, step function workflows, ECS
     tasks are some of the options you can use to apply these
     tags.
   - Apply tag keys and values consistently. Consider
     adopting enforceable
     [tag
     policies](../../../tag-editor/latest/userguide/tag-policies-orgs.md "../../../tag-editor/latest/userguide/tag-policies-orgs.md") using AWS Organizations.
   - Add as many data sovereignty tags as required.

6. **Enable monitoring and
   alerting**:
   - Configure AWS CloudTrail to maintain audit logs of data
     discovery and classification activities.
   - Use AWS Security Hub to aggregate security findings and
     compliance status across your data pipeline. When Amazon Macie publishes findings to AWS Security Hub, it uses
     the AWS Security Finding Format (ASFF). For examples,
     see
     [Examples
     of Macie findings in AWS Security Hub](../../../macie/latest/user/securityhub-integration.md#securityhub-integration-finding-example "../../../macie/latest/user/securityhub-integration.md#securityhub-integration-finding-example").

## Resources

**Related best practices:**

- [SUS04-BP01
  Implement a data classification policy](../sustainability-pillar/sus_sus_data_a2.md "../sustainability-pillar/sus_sus_data_a2.md")
- [SEC07-BP01
  Understand your data classification scheme](../security-pillar/sec_data_classification_identify_data.md "../security-pillar/sec_data_classification_identify_data.md")
- [SEC07-BP02
  Apply data protection controls based on data
  sensitivity](../security-pillar/sec_data_classification_define_protection.md "../security-pillar/sec_data_classification_define_protection.md")
- [SEC07-BP03
  Automate identification and classification](../security-pillar/sec_data_classification_auto_classification.md "../security-pillar/sec_data_classification_auto_classification.md")
- [SEC07-BP04
  Define scalable data lifecycle management](../security-pillar/sec_data_classification_lifecycle_management.md "../security-pillar/sec_data_classification_lifecycle_management.md")

**Related documents:**

- [Amazon Macie User Guide - Discovering sensitive data](../../../macie/latest/user/discovery-jobs.md "../../../macie/latest/user/discovery-jobs.md")
- [AWS Glue Developer Guide - Using crawlers to populate the Data
  Catalog](../../../glue/latest/dg/add-crawler.md "../../../glue/latest/dg/add-crawler.md")
- [Amazon EventBridge User Guide - Creating rules that react to
  events](../../../eventbridge/latest/userguide/eb-create-rule.md "../../../eventbridge/latest/userguide/eb-create-rule.md")
- [AWS Security Best Practices for Data Classification](../../../whitepapers/latest/data-classification/data-classification.md "../../../whitepapers/latest/data-classification/data-classification.md")
- [Detect
  PII data in Amazon Aurora with Amazon Comprehend](https://aws.amazon.com/blogs/database/detect-pii-data-in-amazon-aurora-with-amazon-comprehend/ "https://aws.amazon.com/blogs/database/detect-pii-data-in-amazon-aurora-with-amazon-comprehend/")
- [Creating
  a notification workflow from sensitive data discovery with
  Amazon Macie, Amazon EventBridge, AWS Lambda, and Slack](https://aws.amazon.com/blogs/security/creating-a-notification-workflow-from-sensitive-data-discover-with-amazon-macie-amazon-eventbridge-aws-lambda-and-slack/ "https://aws.amazon.com/blogs/security/creating-a-notification-workflow-from-sensitive-data-discover-with-amazon-macie-amazon-eventbridge-aws-lambda-and-slack/")

**Related tools:**

- [Apache
  Atlas](https://atlas.apache.org/ "https://atlas.apache.org/")

**Related videos:**

- [Best
  practices for protecting sensitive data in AWS with Amazon Macie](https://www.youtube.com/watch?v=1iZYmtFFLnw "https://www.youtube.com/watch?v=1iZYmtFFLnw")
- [AWS Summit SF 2022 - Securing sensitive information with AWS Glue
  Sensitive Data Detection (ANA314)](https://www.youtube.com/watch?v=CADNFjZ_QG8 "https://www.youtube.com/watch?v=CADNFjZ_QG8")
- [AWS re:Inforce 2022 - Amazon Macie for data protection and
  governance (TDR206)](https://www.youtube.com/watch?v=SmMSt0n6a4k "https://www.youtube.com/watch?v=SmMSt0n6a4k")

**Related services:**

- [Amazon Macie](https://aws.amazon.com/macie/ "https://aws.amazon.com/macie/")
- [AWS Glue](https://aws.amazon.com/glue/ "https://aws.amazon.com/glue/")
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/ "https://aws.amazon.com/eventbridge/")
- [AWS Step Functions](https://aws.amazon.com/step-functions/ "https://aws.amazon.com/step-functions/")
- [Amazon Comprehend](https://aws.amazon.com/comprehend/ "https://aws.amazon.com/comprehend/")
- [AWS Security Hub](https://aws.amazon.com/security-hub/ "https://aws.amazon.com/security-hub/")
