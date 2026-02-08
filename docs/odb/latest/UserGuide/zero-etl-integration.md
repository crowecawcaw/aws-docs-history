# Oracle Database@AWS Zero-ETL integration with Amazon Redshift

Zero-ETL integration is a fully managed solution that makes transactional and operational
data available in Amazon Redshift from multiple sources. With this solution, you can replicate data to Amazon Redshift
from your Oracle databases running on Oracle Exadata or Autonomous Database on Dedicated Exadata
Infrastructure. The automatic synchronization avoids the traditional extract, transform, and
load (ETL) process. It also enables real-time analytics and AI workloads. For more information,
see [Zero-ETL
integrations](../../../redshift/latest/mgmt/zero-etl-using.md "../../../redshift/latest/mgmt/zero-etl-using.md") in the _Amazon Redshift Management Guide_.

Zero-ETL integration provides the following benefits:

- **Real-time data replication** – Continuous data synchronization from Oracle databases to Amazon Redshift with minimal latency
- **Elimination of complex ETL pipelines** – No need to build and maintain custom data integration solutions
- **Reduced operational overhead** – Automated setup and management through AWS APIs
- **Simplified data integration architecture** – Seamless
  integration between Oracle Database@AWS and AWS analytics services
- **Enhanced security** – Built-in encryption and AWS IAM
  access controls
  Amazon Redshift doesn't charge an additional fee for the zero-ETL integration with Oracle Database@AWS. You pay for
  the existing Amazon Redshift resources used to create and process the change data created as part of a
  zero-ETL integration. For more information, see [Amazon Redshift pricing](https://aws.amazon.com/redshift/pricing/ "https://aws.amazon.com/redshift/pricing/").

## Supported database versions for Zero-ETL

integration in Oracle Database@AWS

Zero-ETL integration supports the following Oracle database versions:

- **Oracle Exadata** – Oracle Database 19c
- **Autonomous Database on Dedicated Infrastructure** –
  Oracle Database 19c and 23ai

## How Zero-ETL integration works in Oracle Database@AWS

Zero-ETL integration allows Oracle Database@AWS to replicate data to Amazon Redshift. The integration leverages
Amazon VPC Lattice to create secure network connectivity. Change data capture (CDC) technology ensures
real-time data synchronization. You manage the integration through AWS Glue APIs.

The Zero-ETL integration architecture includes the following:

- **Secure connectivity** – Uses SSL/TLS encryption
  over TLS port 2484 for data transfer
- **AWS Secrets Manager** – Stores database credentials and
  certificates securely using AWS Key Management Service
- **AWS Glue integration** – Provides unified
  management interface for zero-ETL integrations

Replication proceeds through the following steps:

1. Establishing secure connection to the Oracle database using SSL on port 2484
2. Performing an initial full dump of selected databases, schemas, and tables
3. Setting up change data capture (CDC) for ongoing real-time replication
4. Writing the replicated data to the target Amazon Redshift cluster

###### Important

Zero-ETL integration isn't enabled by default. You must configure it using AWS Glue APIs. You
can't set up zero-ETL integration directly using Oracle Database@AWS APIs.
