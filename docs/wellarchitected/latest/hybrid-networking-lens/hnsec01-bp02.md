

# HNSEC01-BP02 Implement encryption in transit
<a name="hnsec01-bp02"></a>

 Encryption in transit is essential for protecting data confidentiality as traffic moves between on-premises networks and cloud environments. All sensitive data traversing untrusted networks should be encrypted using strong protocols like TLS or IPsec. 

 **Desired outcome:** All sensitive data is protected during transmission, meeting regulatory mandates for confidentiality and data integrity. 

 **Level of risk exposed if this best practice is not established:** High 

 **Benefits of establishing this best practice:** 
+  Ensures confidentiality and integrity of sensitive data 
+  Meets requirements in regulations such as HIPAA, GDPR, and PCI DSS 
+  Reduces risk of breaches and compliance penalties 
+  Build customer and auditor trust 

## Implementation guidance
<a name="implementation-guidance-8"></a>
+  Establish encrypted connections between cloud and on-premises environments. 

   For example, you can use services such as AWS Site-to-Site VPN and AWS Direct Connect with MACsec. 
+  Enforce HTTPS/TLS for all application traffic between cloud and on-premises environments. 
+  Manage and rotate encryption keys according to compliance requirements. 

## Resources
<a name="resources-7"></a>
+  [Encryption in AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/encryption-in-transit.html) 
+  [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) 
+  [Choosing an AWS cryptography service](https://docs.aws.amazon.com/decision-guides/latest/cryptography-on-aws-how-to-choose/guide.html) 