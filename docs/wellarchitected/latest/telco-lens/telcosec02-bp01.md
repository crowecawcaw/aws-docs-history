# TELCOSEC02-BP01 Use secure control plane protocols between the

network functions (NF)

The 3rd Generation Partnership Project (3GPP) recommends that telco organizations use
secure control plane protocols between the various network functions (NF) within their 5G core
network architecture. This best practice is crucial for maintaining the confidentiality,
integrity, and availability of the control plane communications, which are essential for the
proper functioning and management of the network.

The control plane is responsible for the exchange of signaling and management information
between network elements, handling critical tasks such as session establishment, mobility
management, and policy enforcement. By implementing secure control plane protocols, telco
organizations can mitigate the risk of unauthorized access, eavesdropping, and tampering of the
control plane traffic, thereby enhancing the overall security and resilience of the network.

**Level of risk exposed if this best practice is not established:** High

## Implementation guidance

Implement secure communication protocols, such as HTTPS and TLS/DTLS, for control plane
traffic to verify encryption and integrity protection. Use a trusted and secure mechanism
for network function registration and discovery, integrating it with a central registry to
maintain an authorized list of network components. Monitor and analyze the control plane
traffic for anomalies using comprehensive logging and advanced analytics and develop robust
incident response procedures to address security incidents related to the control plane, with
a focus on automated workflows and rapid remediation.

### Implementation steps

Implement secure control plane protocols:

- Verify that the control plane protocols are configured to use secure protocol such
  as HTTPs and secure communication channels, such as TLS/DTLS for encryption and
  integrity protection.
- Use AWS Certificate Manager to manage and provision the necessary SSL/TLS certificates for
  the control plane protocol endpoints.

Secure NF registration and discovery:

- Use a secure NF registration and discovery mechanism, such as the ones defined
  in 3GPP TS 29.510, to enable trusted NFs to discover and communicate with each other.
- Integrate the NF registration and discovery process with AWS Cloud Directory or
  Service Catalog to maintain a secure and up-to-date registry of authorized network functions.

Control plane traffic monitoring and anomaly detection:

- Implement comprehensive logging and monitoring of the control plane traffic using
  Amazon CloudWatch and Amazon OpenSearch Service.
- Configure Amazon GuardDuty to detect and alert on anomalous or suspicious activities
  within the control plane protocol communications.
- Use Amazon CloudWatch Logs Insights to perform advanced analysis and forensics on the
  control plane traffic logs.

Control plane incident response and remediation:

- Develop and test incident response procedures to address security incidents or
  breaches related to the control plane protocols.
- Integrate the control plane security monitoring and incident response capabilities
  with the overall security operations and incident management processes.
- Use AWS Lambda, AWS Step Functions, and Amazon SNS to automate the incident response
  workflows and facilitate rapid remediation.

## Resources

**Key AWS services:**

- [AWS Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/")
- [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/ "https://aws.amazon.com/certificate-manager/")
- [AWS Cloud Directory](https://aws.amazon.com/cloud-directory/ "https://aws.amazon.com/cloud-directory/")
- [Service Catalog](https://aws.amazon.com/servicecatalog/ "https://aws.amazon.com/servicecatalog/")
- [Amazon OpenSearch Service](https://aws.amazon.com/what-is/elasticsearch/ "https://aws.amazon.com/what-is/elasticsearch/")
- [AWS Step Functions](https://aws.amazon.com/step-functions/ "https://aws.amazon.com/step-functions/")
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
- [Amazon GuardDuty](https://aws.amazon.com/guardduty/ "https://aws.amazon.com/guardduty/")
- [Amazon SNS](https://aws.amazon.com/sns/ "https://aws.amazon.com/sns/")
