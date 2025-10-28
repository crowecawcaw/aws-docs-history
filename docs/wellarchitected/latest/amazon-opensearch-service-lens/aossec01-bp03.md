# AOSSEC01-BP03 Enable encryption at rest

Protect data stored in OpenSearch by enabling encryption, keeping
your data confidential even when not in transit.

**Level of risk exposed if this best practice
is not established:** High

**Desired outcome:** Improving data
protection at rest and helping you to meet compliance requirements
for data protection.

**Benefits of establishing this best
practice:** Improved security and confidentiality of data
at rest.

## Implementation guidance

OpenSearch Service domains offer encryption of data at rest, a
security feature that helps prevent unauthorized access to your
data. The feature uses AWS Key Management Service to
store and manage your encryption keys and the Advanced Encryption
Standard algorithm with 256-bit keys (AES-256) to perform the
encryption. If enabled, the feature encrypts the following aspects
of a domain:

- All indexes (including those in UltraWarm storage)
- OpenSearch logs
- Swap files
- All other data in the application directory
- Automated snapshots

### Implementation steps

- Navigate to the Amazon OpenSearch Service console.
- Create a new domain or modify an existing domain:
  - For a new domain, choose **Create domain**. For an
    existing domain, select the domain name and choose
    **Actions**, then **Edit security configuration**.
  - If
    [fine-grained
    access control](../../../opensearch-service/latest/developerguide/fgac.md "../../../opensearch-service/latest/developerguide/fgac.md") is enabled, all encryption options
    under the Encryption box will be enabled by default
    and cannot be disabled.
  - If you don't have fine-grained access control enabled,
    then you can enable Enable encryption of data at rest
    located in the Encryption box.
  - Choose **Save changes**.

## Resources

- [Encryption
  of data at rest for Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/encryption-at-rest.md "../../../opensearch-service/latest/developerguide/encryption-at-rest.md")
