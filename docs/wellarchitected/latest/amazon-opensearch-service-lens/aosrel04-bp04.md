# AOSREL04-BP04 Employ cross-cluster replication to achieve

higher availability

Enhance OpenSearch Service domain availability by employing
cross-cluster replication, which replicates user indexes, mappings,
and metadata between domains in different AWS accounts or Regions,
improving disaster recovery capabilities.

**Level of risk exposed if this best practice
is not established:** Medium

**Desired outcome:** Your Amazon OpenSearch Service is enabled with cross-cluster replication to
enhance domain availability.

**Benefits of establishing this best
practice:**

- **Enhanced domain availability**:
  Employing cross-cluster replication for Amazon OpenSearch Service can enhance domain availability by replicating user
  indexes, mappings, and metadata from one OpenSearch Service
  domain to another in another AWS account or Region.
- **Improved disaster recovery**:
  Cross-cluster replication helps with disaster recovery planning
  by allowing you to replicate data across geographically distant
  AWS Regions (data centers) and reduce latency in the event of an
  outage.

## Implementation guidance

With cross-cluster replication in Amazon OpenSearch Service, you
can replicate user indexes, mappings, and metadata from one
OpenSearch Service domain to another domain in another AWS account
or AWS Region. If there is an outage, cross-cluster replication
assists in disaster recovery and replicates data across
geographically distant AWS Regions to reduce latency.

Enabling cross-cluster replication in Amazon OpenSearch Service
involves a multi-step process that includes setting up IAM roles
and configuring both OpenSearch clusters. For a detailed guide on
how to achieve this, see
[Ensure
availability of your data using cross-cluster replication with
Amazon OpenSearch Service](https://aws.amazon.com/blogs/big-data/ensure-availability-of-your-data-using-cross-cluster-replication-with-amazon-opensearch-service/ "https://aws.amazon.com/blogs/big-data/ensure-availability-of-your-data-using-cross-cluster-replication-with-amazon-opensearch-service/").

## Resources

- [Cross-cluster
  replication for Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/replication.md "../../../opensearch-service/latest/developerguide/replication.md")
- [Ensure
  availability of your data using cross-cluster replication with
  Amazon OpenSearch Service](https://aws.amazon.com/blogs/big-data/ensure-availability-of-your-data-using-cross-cluster-replication-with-amazon-opensearch-service/ "https://aws.amazon.com/blogs/big-data/ensure-availability-of-your-data-using-cross-cluster-replication-with-amazon-opensearch-service/")
