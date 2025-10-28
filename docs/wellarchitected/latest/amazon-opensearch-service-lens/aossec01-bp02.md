# AOSSEC01-BP02 Activate node-to-node encryption

Activate encryption for secure transmission of data between nodes,
protecting it from unauthorized access.

**Level of risk exposed if this best practice
is not established:** High

**Desired outcome:** Node-to-node
encryption is activated for OpenSearch Service domains, providing full data
protection in transit.

**Benefits of establishing this best
practice:** Improved security and confidentiality of data
in transit.

## Implementation guidance

Node-to-node encryption add an extra layer of security to the
inherent security features of OpenSearch Service. It incorporates
Transport Layer Security (TLS) to secure all communications
between nodes.

Each OpenSearch Service domain, regardless of whether the domain
uses VPC access, resides within its own dedicated VPC. This
architecture protects traffic between OpenSearch nodes from public
access. However, traffic within the VPC is unencrypted by default.
Node-to-node encryption enables TLS 1.2 encryption for all
communications within the VPC.

If you send data to OpenSearch Service over HTTPS, node-to-node
encryption keeps your data encrypted as OpenSearch distributes
(and redistributes) it throughout the cluster. If data arrives
unencrypted over HTTP, OpenSearch Service encrypts it after it
reaches the cluster. You can require that all traffic to the
domain arrive over HTTPS using the console, AWS CLI, or
configuration API.

If you enable
[fine-grained
access control](../../../opensearch-service/latest/developerguide/fgac.md "../../../opensearch-service/latest/developerguide/fgac.md"), node-to-node encryption is required.

### Implementation steps

- Navigate to the Amazon OpenSearch Service console.
- Create a new domain, or modify an existing domain:
  - For a new domain, choose **Create domain**. For an
    existing domain, select the domain name and choose
    **Actions**, then **Edit security configuration**.
  - If
    [fine-grained
    access control](../../../opensearch-service/latest/developerguide/fgac.md "../../../opensearch-service/latest/developerguide/fgac.md") is enabled, all encryption options
    under the Encryption box will be enabled by default
    and cannot be disabled.
  - If you don't have fine-grained access control enabled,
    then you can enable Node-to-node encryption located in
    the Encryption box.
  - Choose **Save changes**.

## Resources

- [Node-to-node
  encryption for Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/ntn.md "../../../opensearch-service/latest/developerguide/ntn.md")
