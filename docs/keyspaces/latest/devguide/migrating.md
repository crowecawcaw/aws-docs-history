# Migrating to Amazon Keyspaces (for Apache Cassandra)

Migrating to Amazon Keyspaces (for Apache Cassandra) presents a range of compelling benefits for businesses and organizations. Here are some key advantages
that make Amazon Keyspaces an attractive choice for migration.

- **Scalability** – Amazon Keyspaces is designed to handle massive workloads and scale seamlessly
  to accommodate growing data volumes and traffic. With traditional Cassandra, scaling is not performed on demand and requires planning
  for future peaks. With Amazon Keyspaces, you can easily scale your tables up or down based on demand, ensuring that your applications can handle
  sudden spikes in traffic without compromising performance.
- **Performance** – Amazon Keyspaces offers low-latency data access, enabling applications to
  retrieve and process data with exceptional speed. Its distributed architecture ensures that read and write operations are distributed
  across multiple nodes, delivering consistent, single-digit millisecond response times even at high request rates.
- **Fully managed** – Amazon Keyspaces is a fully managed service provided by AWS. This means
  that AWS handles the operational aspects of database management, including provisioning, configuration, patching, backups, and scaling.
  This allows you to focus more on developing your applications and less on database administration tasks.
- **Serverless architecture** – Amazon Keyspaces is serverless. You pay only for capacity consumed
  with no upfront capacity provisioning required. You don't have servers to manage or instances to choose. This pay-per-request model
  offers cost efficiency and minimal operational overhead, as you only pay for the resources you consume without the need to provision
  and monitor capacity.
- **NoSQL flexibility with schema** – Amazon Keyspaces follows a NoSQL data model, providing
  flexibility in schema design. With Amazon Keyspaces, you can store structured, semi-structured, and unstructured data, making it well-suited
  for handling diverse and evolving data types. Additionally, Amazon Keyspaces performs schema validation on write allowing for a centralized
  evolution of the data model. This flexibility enables faster development cycles and easier adaptation to changing business requirements.
- **High availability and durability** – Amazon Keyspaces replicates data across multiple
  [Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ "https://aws.amazon.com/about-aws/global-infrastructure/regions_az/") within an AWS Region, ensuring high availability and data durability. It automatically handles replication, failover,
  and recovery, minimizing the risk of data loss or service disruptions. Amazon Keyspaces provides an availability SLA of up to 99.999%. For even more
  resiliency and low-latency local reads, Amazon Keyspaces offers [multi-Region replication](multiRegion-replication.md "multiRegion-replication.md").
- **Security and compliance** – Amazon Keyspaces integrates with
  AWS Identity and Access Management for fine-grained access control. It provides encryption at rest and
  in-transit, helping to improve the security of your data. Amazon Keyspaces has been assessed by
  third-party auditors for security and compliance with specific programs, including
  HIPAA, PCI DSS, and SOC, enabling you to meet regulatory requirements. For more
  information, see [Compliance validation for Amazon Keyspaces (for Apache Cassandra)](Keyspaces-compliance.md "Keyspaces-compliance.md").
- **Integration with AWS Ecosystem** – As part of the AWS
  ecosystem, Amazon Keyspaces seamlessly integrates with other AWS services, for example AWS CloudFormation,
  Amazon CloudWatch, and AWS CloudTrail. This integration enables you to build serverless architectures,
  leverage infrastructure as code, and create real-time data-driven applications. For more
  information, see [Monitoring Amazon Keyspaces (for Apache Cassandra)](monitoring-overview.md "monitoring-overview.md").

###### Topics

- [Create a migration plan for migrating from Apache Cassandra to Amazon Keyspaces](migrating-cassandra.md "migrating-cassandra.md")
- [How to select the right tool for bulk uploading or migrating data to Amazon Keyspaces](migrating-tools.md "migrating-tools.md")
