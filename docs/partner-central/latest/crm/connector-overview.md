# CRM connector overview

The AWS Partner CRM connector enables you to integrate your Salesforce organization with AWS Partner Central and
AWS Marketplace. Integration enables you to complete AWS Partner Central and AWS Marketplace tasks in Salesforce, such as two-way synching of ACE opportunities and attaching
offers to opportunities.

The CRM connector is available at no charge, and it requires no coding.

The following topics explain the concepts and processes for using the connector.

###### Topics

- [Connector benefits](#connector-benefits "#connector-benefits")
- [Intended users](#connector-audience "#connector-audience")
- [Installation and usage overview](#connector-process "#connector-process")

## Connector benefits

The AWS Partner CRM connector provides the following benefits:

- **AWS Partner Central integration** – Streamlined
  opportunity management. You can use Salesforce to send and receive opportunities from AWS
  Sales, and from other partners. The connector also enables you to send leads to AWS.

###### Note

Partners who receive leads from AWS continue to use their Amazon S3 integrations. For more information, refer to:

    + [Configuring the connector for a CRM with Amazon S3 integration](s3-config.md "s3-config.md") later in this section.
    + [Using an earlier CRM with Amazon S3 integration](custom-integration-using-amazon-s3.md "custom-integration-using-amazon-s3.md") later in this guide.

- **AWS Marketplace integration** – Use Salesforce to
  manage private offers, resale authorizations, and complete other AWS Marketplace tasks.

## Intended users

The CRM connector is intended for use by the following groups:

- Partners looking to streamline the coselling process.
- Independent software vendors (ISVs) selling products on AWS Marketplace.
- AWS Consulting Partners who manage client engagements and opportunities.

## Installation and usage overview

The process of installing and using the AWS Partner CRM connector follows these broad steps:

1. Complete the [Integration prerequisites](crm-integration-setting-up.md "crm-integration-setting-up.md").
2. Install the connector from the Salesforce AppExchange. Refer to [Installing the connector](install-connector.md "install-connector.md"), later in this section, for the installation steps.
3. Configure the connector to exchange data with AWS Partner Central, AWS Marketplace, and earlier Amazon S3 integrations.
   The topics in [Configuring the CRM connector](configure-crm-connector.md "configure-crm-connector.md") explain how to configure the connector for each type of integration.
