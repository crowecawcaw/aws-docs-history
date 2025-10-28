# AOSPERF03-BP03 Use storage types that provide higher IOPs and

throughput baseline

Improve storage performance with higher baseline IOPs and throughput
using more scalable and efficient volume types.

**Level of risk exposed if this best practice
is not established:** Low

**Desired outcome:** Improved storage
performance, with increased input and output operations Per second
(IOPs) and higher throughput.

**Benefits of establishing this best
practice:**

- **Improved baseline
  performance:** Using gp3 EBS volumes provide higher
  baseline performance compared to gp2 volumes.
- **Scalable high performance:**
  With gp3 volumes, you can provision higher performance
  independently of the volume size, allowing for more scalable and
  efficient performance in your OpenSearch Service domains.

## Implementation guidance

gp3 is the successor to the general-purpose SSD gp2 volume,
offering higher baseline performance and the capability to
provision higher performance independent of volume size.

### Implementation steps

- Log in to the AWS Management Console.
- Navigate to the Amazon OpenSearch Service console.
- For an existing domain, select the domain name and ch**oose
  Actions**, then **Edit cluster configuration**.
- Navigate to Number of data nodes box, and locate EBS
  volume type.
- Change the volume type from General Purpose (SSD) – gp2 to
  General Purpose (SSD) – gp3.

## Resources

- [Making
  configuration changes in Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/managedomains-configuration-changes.md "../../../opensearch-service/latest/developerguide/managedomains-configuration-changes.md")
