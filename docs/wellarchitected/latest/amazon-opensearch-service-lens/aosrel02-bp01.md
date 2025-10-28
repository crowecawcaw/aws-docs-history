# AOSREL02-BP01 Create Multi-AZ with Standby OpenSearch Service domains

Provide high availability and reliability in Amazon OpenSearch Service by
creating Multi-AZ with Standby domains, minimizing downtime and
simplifying domain management.

**Level of risk exposed if this best practice
is not established:** High

**Desired outcome:** A highly
available OpenSearch Service domain is created using Multi-AZ with
Standby.

**Benefits of establishing this best
practice:**

- **Improved availability:**
  Creating Multi-AZ with Standby OpenSearch Service domains can
  provide improved high availability, minimizing downtime and
  improving overall system reliability.
- **Simplified domain management:**
  This deployment option simplifies domain management by using
  multiple Availability Zones and best practices, making it easier
  to manage and maintain your OpenSearch Service domain.

## Implementation guidance

Multi-AZ with Standby is a deployment option for Amazon OpenSearch Service that offers 99.99% availability, consistent performance
for production workloads, and simplified domain management by
using multiple Availability Zones and best practices.

### Implementation steps

- Log in to AWS Management Console.
- Navigate to the Amazon OpenSearch Service console.
- Create a new domain or modify an existing domain:
  - For a new domain, choose **Create domain**.
    - You can use the Easy create method available under
      Domain creation method, which creates a new
      domain with Multi-AZ with Standby enabled by
      default.
    - If you want to have more control over different
      creation options, then you can choose **Standard
      create** and select **Domain with standby** in the
      Deployment option(s) box.

  - For an existing domain, select the domain name and
    choose **Actions**, then select **Edit cluster
    configuration**.
  - For an existing domain, choose **Domain with standby**
    under Deployment option(s) box.

- You will need to have a minimum of three data nodes to use
  Multi-AZ with Standby.
- Proceed with other options.

## Resources

- [AWS announces Multi-AZ with Standby for Amazon OpenSearch Service](https://aws.amazon.com/about-aws/whats-new/2023/05/aws-multi-az-standby-amazon-opensearch-service/ "https://aws.amazon.com/about-aws/whats-new/2023/05/aws-multi-az-standby-amazon-opensearch-service/")
- [Amazon OpenSearch Service Under the Hood: Multi-AZ with
  Standby](https://aws.amazon.com/blogs/big-data/amazon-opensearch-service-under-the-hood-multi-az-with-standby/ "https://aws.amazon.com/blogs/big-data/amazon-opensearch-service-under-the-hood-multi-az-with-standby/")
- [Configuring
  a Multi-AZ domain in Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/managedomains-multiaz.md "../../../opensearch-service/latest/developerguide/managedomains-multiaz.md")
