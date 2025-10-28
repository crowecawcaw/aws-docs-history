# AOSCOST02-BP01 Use the latest Amazon EBS gp3 volumes with your

OpenSearch Service nodes

Improve baseline performance and scalability by using the latest
Amazon EBS gp3 volumes, which offer higher baseline performance and
more scalable high performance.

**Level of risk exposed if this best practice
is not established:** Low

**Desired outcome:** The latest
Amazon EBS gp3 volumes are used with OpenSearch Service nodes to
provide optimal performance, durability, and cost-effectiveness.

**Benefits of establishing this best
practice:**

- **Improved baseline
  performance:** Using gp3 EBS volumes provides higher
  baseline performance compared to gp2 volumes.
- **Scalable high performance:**
  With gp3 volumes, you can provision higher performance
  independently of the volume size, allowing for more scalable and
  efficient performance in your OpenSearch Service domains.

## Implementation guidance

OpenSearch Service launched support for the next generation,
general purpose SSD (gp3) EBS volumes. OpenSearch Service data
nodes require low latency and high throughput storage to provide
fast indexing and query. We recommend that you consider gp3 as an
effective Amazon EBS option for price, performance, and
flexibility.

For more details about implementing this best practice for cost
optimization, see [AOSPERF03-BP03](aosperf03-bp03.md "aosperf03-bp03.md").

## Resources

- [Making
  configuration changes in Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/managedomains-configuration-changes.md "../../../opensearch-service/latest/developerguide/managedomains-configuration-changes.md")
