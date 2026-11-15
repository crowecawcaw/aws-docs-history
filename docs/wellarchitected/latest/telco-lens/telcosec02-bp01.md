

# TELCOSEC02-BP01 Use secure control-plane protocols between the network functions (NF)
<a name="telcosec02-bp01"></a>

 The 3rd Generation Partnership Project (3GPP) recommends that telco organizations use secure control-plane protocols between the various network functions (NF) within their 5G core network architecture. This best practice is crucial for maintaining the confidentiality, integrity, and availability of the control-plane communications, which are essential for the proper functioning and management of the network. 

 The control plane is responsible for the exchange of signaling and management information between network elements, handling critical tasks such as session establishment, mobility management, and policy enforcement. By implementing secure control-plane protocols, telco organizations can mitigate the risk of unauthorized access, eavesdropping, and tampering with the control-plane traffic, thereby enhancing the overall security and resilience of the network. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Implement secure communication protocols, such as HTTPS and TLS/DTLS, for control-plane traffic, pinning the minimum version to TLS 1.2 or 1.3 (DTLS 1.2 or later where DTLS applies) to verify encryption and integrity protection. Reject TLS 1.0 and 1.1 at the terminator. Use a trusted and secure mechanism for network function registration and discovery, integrating it with a central registry to maintain an authorized list of network components. Monitor and analyze the control-plane traffic for anomalies using comprehensive logging and advanced analytics, and develop strong incident response procedures to address security incidents related to the control plane, with a focus on automated workflows and rapid remediation. 

### Implementation steps
<a name="implementation-steps"></a>

 Implement secure control-plane protocols: 
+  Configure control-plane protocols — service-based interfaces (SBI), N2 terminators, and Diameter-over-TLS endpoints — to use HTTPS and TLS/DTLS with a minimum version of TLS 1.2 or 1.3 (DTLS 1.2 or later where DTLS applies) for encryption and integrity protection. 
+  Enforce the TLS version floor through a concrete AWS service control: Amazon API Gateway security policies (TLS\_1\_2 minimum), Elastic Load Balancing security policies on ALB or NLB (TLSv1.2 or TLSv1.3 only), or an application-side TLS configuration on self-hosted terminators. 
+  Use AWS Certificate Manager to manage and provision the necessary SSL/TLS certificates for the control-plane protocol endpoints. 

 Secure NF registration and discovery: 
+  Use a secure NF registration and discovery mechanism, such as the ones defined in 3GPP TS 29.510, to enable trusted NFs to discover and communicate with each other. 
+  Integrate the NF registration and discovery process with a registry built on Amazon DynamoDB or with Service Catalog to maintain a secure and up-to-date registry of authorized network functions. 

 Control plane traffic monitoring and anomaly detection: 
+  Implement comprehensive logging and monitoring of the control-plane traffic using Amazon CloudWatch and Amazon OpenSearch Service. 
+  Configure Amazon GuardDuty to detect and alert on anomalous or suspicious activities within the control-plane protocol communications. 
+  Use Amazon CloudWatch Logs Insights to perform advanced analysis and forensics on the control-plane traffic logs. 

 Control plane incident response and remediation: 
+  Develop and test incident response procedures to address security incidents related to the control-plane protocols. 
+  Integrate the control-plane security monitoring and incident response capabilities with the overall security operations and incident management processes. 
+  Use AWS Lambda, AWS Step Functions, and Amazon SNS to automate the incident response workflows and facilitate rapid remediation. 

## Resources
<a name="resources"></a>

 **Key AWS services:** 
+  [AWS Lambda](https://aws.amazon.com/lambda/) 
+  [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/) 
+  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) 
+  [Service Catalog](https://aws.amazon.com/servicecatalog/) 
+  [Amazon OpenSearch Service](https://aws.amazon.com/what-is/elasticsearch/) 
+  [AWS Step Functions](https://aws.amazon.com/step-functions/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Amazon GuardDuty](https://aws.amazon.com/guardduty/) 
+  [Amazon SNS](https://aws.amazon.com/sns/) 