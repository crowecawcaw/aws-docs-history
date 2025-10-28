# AOSSUS03-BP01 Use Index State Management to manage the

lifecycle of your dataset

Improve data management, meet compliance requirements, and reduce
data loss risk by using Index State Management (ISM) to manage the
lifecycle of your dataset.

**Level of risk exposed if this best practice
is not established:** Medium

**Desired outcome:** The lifecycle of
the dataset is managed using Index State Management (ISM) to support
sustainability goals.

**Benefits of establishing this best practice:**

- Improved data management and organization
- Enhanced ability to meet data compliance and regulatory
  requirements
- Reduced risk of data loss or corruption due to proper data
  lifecycle management

## Implementation guidance

ISM removes the necessity for establishing and overseeing external
processes to run your index operations. It also allows you to
perform operations like moving data from Hot storage to Warm.

- Implement a data classification policy to understand its
  criticality to business outcomes and choose the right
  energy-efficient storage tier. Determine criticality,
  confidentiality, integrity, and availability of data based on
  risk to the organization.
- Evaluate your data characteristics and access pattern to
  collect the key characteristics of your storage needs. Key
  characteristics to consider include:
  - **Data type:** Structured,
    semistructured, unstructured
  - **Data growth:** Bounded,
    unbounded
  - **Data durability:**
    Persistent, ephemeral, transient
  - **Access patterns:** Reads
    or writes, frequency, spiky, or consistent

- Implement an
  [ISM
  policy](../../../opensearch-service/latest/developerguide/ism.md "../../../opensearch-service/latest/developerguide/ism.md") to move data between different storage tiers to
  meet business and regulatory requirements. Additionally,
  implement an
  [ISM
  policy](../../../opensearch-service/latest/developerguide/ism.md "../../../opensearch-service/latest/developerguide/ism.md") to delete unnecessary data. For detailed
  implementation guidance, see [AOSOPS01-BP01](aosops01-bp01.md "aosops01-bp01.md").

## Resources

- [Index
  State Management in Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/ism.md "../../../opensearch-service/latest/developerguide/ism.md")
