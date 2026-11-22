

# TELCOSEC02-BP02 Provide cloud infrastructure support for subscriber identity protection mechanisms defined by 3GPP

 3GPP defines how subscriber identity is concealed (SUCI and SUPI concealment), and the CSP implements those mechanisms in its network functions. The cloud infrastructure supplies the cryptographic services, key management, and hardened compute the mechanisms depend on. 

 **Desired outcome:** 
+  The cloud infrastructure provides the key management services that the SUCI encryption and decryption process requires, with key rotation and access controls appropriate for subscriber identity material. 
+  The compute environment running identity-handling network functions (UDM, AUSF) is hardened with encryption in transit, restricted network access, and isolation. 
+  Audit logging tracks access to subscriber identity decryption keys without logging the decrypted identities themselves. 

 **Common anti-patterns:** 
+  Storing SUPI-to-SUCI mapping keys in application configuration files rather than a dedicated key management service. 
+  Not encrypting the network path between the AMF and UDM or AUSF where decrypted subscriber identities transit. 
+  Logging decrypted subscriber identities in application logs, turning the observability layer into a data-exposure risk. 
+  Leaving identity-handling functions without network isolation, widening the scope of impact of an incident. 

 **Benefits of establishing this best practice:** 
+  A clear responsibility boundary lets the CSP own the mechanism while the infrastructure provides the cryptographic foundation. 
+  Holding identity keys in a dedicated key service keeps them out of memory and configuration, which reduces exposure. 
+  Encrypting the paths that carry decrypted identities helps protect them in transit between functions. 
+  Auditable key access without logging identities gives compliance evidence without creating a new data-protection liability. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 3GPP TS 33.501 specifies subscriber identity protection. The CNF vendor or CSP implements it and decides how concealment works. Supply the infrastructure the mechanism requires (key management, compute isolation, and audit). State explicitly that the mechanism belongs to the operator. 

 Hold the home-network key pair used to conceal and reveal subscriber identity in a hardware-backed key service, and access it through an API. The private key is never stored in a function's memory or configuration file. Functions such as the UDM and AUSF call the key service to perform the cryptographic operation. They do not hold the key. A compromised function exposes the operations it can request. The key material remains in the key service. 

 Record who accessed identity-protection keys and when, without turning the audit trail into a repository of the identities it protects. Log key-usage events, and ensure application logs from identity-handling functions do not record decrypted SUPI values. Vendor defaults might log those values, so configure redaction. 

### Implementation steps
<a name="implementation-steps"></a>
+  Hold identity keys in a managed key service: store the home-network and subscriber-identity keys in AWS KMS or AWS CloudHSM, and configure the UDM and AUSF to access them through the API rather than holding key material locally. 
+  Coordinate key rotation with the vendor: implement key-rotation policies for identity material in step with the CNF vendor's requirements, so rotation doesn't disrupt concealment operations. 
+  Harden and isolate identity-handling functions: restrict network access to the UDM and AUSF with security groups and network policies, and enable encryption in transit (mutual TLS or IPsec) on the N8, N12, and N13 interfaces where identities transit. 
+  Configure audit logging without identity exposure: enable AWS CloudTrail logging for all key-usage events, and verify that application logs don't contain decrypted SUPI values, configuring redaction where vendor defaults include them. 

## Resources
<a name="resources"></a>

 **Key AWS services:** 
+  [AWS Key Management Service](https://aws.amazon.com/kms/) 
+  [AWS CloudHSM](https://aws.amazon.com/cloudhsm/) 
+  [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 