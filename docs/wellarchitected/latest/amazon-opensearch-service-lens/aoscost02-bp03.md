# AOSCOST02-BP03 Use the warm storage tier to optimize storage

for a significant amount of read-only data

Reduce costs, improve query performance, and enhance domain
stability by storing a significant amount of read-only data in the
warm tier.

**Level of risk exposed if this best practice
is not established:** Low

**Desired outcome:** The warm tier is
used in OpenSearch Service to store a significant amount of
read-only data, reducing costs while maintaining data availability.

**Benefits of establishing this best
practice:**

- Reduced costs due to optimized storage utilization
- Improved query performance through optimized data retrieval
- Enhanced domain stability by avoiding unnecessary resource
  utilization

## Implementation guidance

Use data lifecycle management policies to move large amounts of
read-only data to UltraWarm tier for low-latency queries and
reduced costs.

To optimize costs and performance in Amazon OpenSearch Service,
you can use the UltraWarm tier for storing a significant amount of
read-only data.

### Implementation steps

- Log in to the
  [AWS Management Console](https://console.aws.amazon.com "https://console.aws.amazon.com").
- Navigate to the Amazon OpenSearch Service console.
- Select the domain name and choose **Actions**, then **Edit
  cluster configuration.**
- Enable UltraWarm:
  - In the Cluster configuration section, look for the
    option Enable warm data nodes located in the Warm and
    cold data storage box.

  ###### Note

  You need to
  have dedicated leader nodes in your domain to be able to
  use warm and cold storage.
  - Toggle on the option to enable UltraWarm nodes.
  - Select the Instance type.
  - Set the number of warm data nodes (it is required to
    have a minimum of three).

- After configuring the settings, review your setup and choose
  **Create** (for a new domain) or **Save changes** (for an
  existing domain).

## Resources

- [UltraWarm
  storage for Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/ultrawarm.md "../../../opensearch-service/latest/developerguide/ultrawarm.md")
