

# Infrastructure security in Amazon OpenSearch Memory

As a managed service, Amazon OpenSearch Memory is protected by AWS global network security. For information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/). To design your AWS environment using the best practices for infrastructure security, see [Infrastructure Protection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/infrastructure-protection.html) in the *Security Pillar AWS Well‐Architected Framework*.

You use AWS published API calls to access OpenSearch Memory through the network. Clients must support the following:
+ Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.
+ Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems such as Java 7 and later support these modes.

Additionally, requests must be signed by using an access key ID and a secret access key that is associated with an IAM principal. Or you can use the [AWS Security Token Service](https://docs.aws.amazon.com/STS/latest/APIReference/Welcome.html) (AWS STS) to generate temporary security credentials to sign requests.

## Endpoints
<a name="memory-endpoints"></a>

OpenSearch Memory has two kinds of endpoints:
+ Space and tagging operations use the Regional endpoint `https://osm.{{region}}.api.aws`.
+ Event and memory operations use the endpoint of the space they act on, `https://{{space-id}}.osm.{{region}}.on.aws`.

The AWS CLI and SDKs choose the endpoint for you from the operation and the `spaceId` in the request. If you sign requests yourself, use `osm` as the Signature Version 4 service name. OpenSearch Memory doesn't have FIPS endpoints.