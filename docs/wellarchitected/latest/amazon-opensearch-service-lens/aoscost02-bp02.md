# AOSCOST02-BP02 Use instances optimized for heavy indexing use

cases

Improve indexing throughput and cost-effectiveness by using OR1
instances, which provide optimized storage for heavy indexing use
cases.

**Level of risk exposed if this best practice
is not established:** Low

**Desired outcome:** OR1 instances
are used in Amazon OpenSearch Service to deliver price-performance
for heavy indexing use cases.

**Benefits of establishing this best
practice:**

- **Improved indexing throughput:**
  Use OR1 instances in Amazon OpenSearch Service for heavy
  indexing use cases, which provides increased indexing throughput
  due to the optimized storage structure.
- **Cost-effective data storage:**
  Using OR1 instances offers a cost-effective way to store large
  amounts of data, making it an ideal choice for applications with
  high indexing demands.

## Implementation guidance

OR1 is an instance family for Amazon OpenSearch Service that
provides a cost-effective way to store large amounts of data. A
domain with OR1 instances uses Amazon Elastic Block Store (Amazon EBS) volumes for primary storage, with data copied synchronously
to Amazon S3. This storage structure provides increased indexing
throughput with high durability.

You can use OR1 instances with OpenSearch 2.11+ or upgrade to
2.15+ on existing domains.

### Implementation steps

- Log in to the AWS Management Console.
- Navigate to the Amazon OpenSearch Service console.
- Create a new domain or modify an existing domain:
  - For a new domain, choose **Create domain**. For an
    existing domain, select the domain name and choose
    **Actions**, then **Edit cluster configuration**.
  - For new domains, select **Standard create** under Domain
    creation method tab.

- Under Data nodes tab, choose **OR1** from the Instance
  family drop down box.
- Proceed with other options.

## Resources

- [Introducing
  highly durable Amazon OpenSearch Service clusters with 30%
  price/performance improvement](https://aws.amazon.com/blogs/aws/introducing-highly-durable-amazon-opensearch-service-clusters-with-30-price-performance-improvement/ "https://aws.amazon.com/blogs/aws/introducing-highly-durable-amazon-opensearch-service-clusters-with-30-price-performance-improvement/")
- [OR1
  storage for Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/or1.md "../../../opensearch-service/latest/developerguide/or1.md")
- [Amazon OpenSearch Service Under the Hood: OpenSearch Optimized
  Instances (OR1)](https://aws.amazon.com/blogs/big-data/amazon-opensearch-service-under-the-hood-opensearch-optimized-instancesor1/ "https://aws.amazon.com/blogs/big-data/amazon-opensearch-service-under-the-hood-opensearch-optimized-instancesor1/")
- [OpenSearch
  optimized instance (OR1) is game changing for indexing
  performance and cost](https://aws.amazon.com/blogs/big-data/opensearch-optimized-instance-or1-is-game-changing-for-indexing-performance-and-cost/ "https://aws.amazon.com/blogs/big-data/opensearch-optimized-instance-or1-is-game-changing-for-indexing-performance-and-cost/")
- [Improve
  your Amazon OpenSearch Service performance with OpenSearch
  Optimized Instances](https://aws.amazon.com/blogs/big-data/improve-your-amazon-opensearch-service-performance-with-opensearch-optimized-instances/ "https://aws.amazon.com/blogs/big-data/improve-your-amazon-opensearch-service-performance-with-opensearch-optimized-instances/")
