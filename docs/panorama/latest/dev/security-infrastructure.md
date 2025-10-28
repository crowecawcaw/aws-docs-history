End of support notice: On May 31, 2026, AWS will end support for
AWS Panorama. After May 31, 2026, you will no longer be able to access the AWS Panorama console or AWS Panorama
resources. For more information, see [AWS Panorama end of support](panorama-end-of-support.md "panorama-end-of-support.md").

# Infrastructure security in AWS Panorama

As a managed service, AWS Panorama is protected by AWS global network security. For
information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/ "https://aws.amazon.com/security/"). To design your AWS
environment using the best practices for infrastructure security, see [Infrastructure
Protection](../../../wellarchitected/latest/security-pillar/infrastructure-protection.md "../../../wellarchitected/latest/security-pillar/infrastructure-protection.md") in _Security Pillar AWS Well‐Architected
Framework_.

You use AWS published API calls to access AWS Panorama through the network. Clients must
support the following:

- Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.
- Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral
  Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems
  such as Java 7 and later support these modes.

## Deploying the AWS Panorama Appliance in your datacenter

The AWS Panorama Appliance needs internet access to communicate with AWS services. It also needs access to your
internal network of cameras. It is important to consider your network configuration carefully and only provide
each device the access that it needs. Be careful if your configuration allows the AWS Panorama Appliance to act as a bridge
to a sensitive IP camera network.

You are responsible for the following:

- The physical and logical network security of the AWS Panorama Appliance.
- Securely operating the network-attached cameras when you use the AWS Panorama Appliance.
- Keeping the AWS Panorama Appliance and camera software updated.
- Complying with any applicable laws or regulations associated with the content of the videos and images
  you gather from your production environments, including those related to privacy.

The AWS Panorama Appliance uses unencrypted RTSP camera streams. For more information on connecting the AWS Panorama Appliance to
your network, see [Connecting the AWS Panorama Appliance to your network](appliance-network.md "appliance-network.md"). For details on
encryption, see [Data protection in AWS Panorama](security-dataprotection.md "security-dataprotection.md").
