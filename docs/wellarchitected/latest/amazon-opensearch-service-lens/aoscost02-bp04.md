# AOSCOST02-BP04 Use the cold tier storage option to store and

retrieve infrequently accessed or historical data

Reduce costs and improve data management by storing infrequently
accessed or historical data in the cold tier, maintaining efficient
data retrieval.

**Level of risk exposed if this best practice
is not established:** Low

**Desired outcome:** The cold tier
storage option is used in Amazon OpenSearch Service to store and
retrieve infrequently accessed or historical data efficiently,
reducing costs while maintaining data availability.

**Benefits of establishing this best
practice:**

- **Cost reduction**: Using the
  cold tier storage option in Amazon OpenSearch Service helps
  reduce costs associated with storing and retrieving infrequently
  accessed or historical data.
- **Efficient data management**: By
  using cold tier for infrequently accessed data, you can
  efficiently manage your data storage, making it easier to
  maintain data availability while minimizing storage expenses.

## Implementation guidance

If you have data that must be preserved for compliance or
regulatory reasons and or have historical value you can use cold
tier to store such data at a lower cost than other storage tiers.
cold storage is appropriate if you need to do periodic research or
forensic analysis on your older data.

To optimize costs and performance in Amazon OpenSearch Service,
you can use the cold tier storage option for storing and
retrieving infrequently accessed or historical data.

### Implementation steps

- Log in to the
  [AWS Management Console](https://console.aws.amazon.com "https://console.aws.amazon.com").
- Navigate to the Amazon OpenSearch Service console.
- Select the domain name and choose **Actions**, then **Edit
  cluster configuration.**
- Enable UltraWarm:
  - In the Cluster configuration section, look for the
    option **Enable warm data nodes** located in the Warm and
    cold data storage box.

  ###### Note

  You need to
  have dedicated leader nodes in your domain to be able to
  use warm and cold storage.
  - Toggle on the option to enable UltraWarm nodes.
  - Select the **Instance type.**
  - Set the number of warm data nodes (required to have a
    minimum of three).
  - Toggle on the option **Enable cold storage.**

- After configuring the settings, review your setup and choose
  **Create** (for a new domain) or **Save changes** (for an
  existing domain).

## Resources

- [Cold
  storage for Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/cold-storage.md "../../../opensearch-service/latest/developerguide/cold-storage.md")
