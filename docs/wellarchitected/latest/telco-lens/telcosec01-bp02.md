

# TELCOSEC01-BP02 Implement encryption for control-plane signaling and classify data-plane traffic by regulatory encryption requirements
<a name="telcosec01-bp02"></a>

 Not all telco traffic needs the same encryption treatment. Control-plane signaling often requires transport encryption by regulation, while data-plane subscriber traffic is usually already encrypted end to end by the application and 3GPP layers. Adding blanket VPN encryption on top of already-encrypted, high-bandwidth data-plane flows imposes packet-per-second limits and cost without a compliance benefit. 

 **Desired outcome:** 
+  Traffic flows are classified by regulatory encryption requirement, distinguishing control-plane signaling that mandates transport encryption from data-plane traffic already covered by application-layer encryption. 
+  Control-plane interfaces between network functions use IPsec or mutual TLS where regulations require encrypted signaling transport. 
+  It is documented which flows require additional transport encryption and which are already compliant through existing application-layer or 3GPP-defined mechanisms. 

 **Common anti-patterns:** 
+  Encrypting all traffic, including GTP-U data plane, with IPsec without confirming a regulatory requirement, which hits per-flow PPS limits and adds cost. 
+  Not distinguishing 3GPP-mandated encryption from operator-chosen additional encryption, so effort goes where it adds no compliance value. 
+  Applying blanket "encrypt everything" policies without understanding the throughput impact on high-bandwidth data-plane interfaces. 
+  Treating data-at-rest encryption as covered by transport encryption, leaving persistent stores unprotected. 

 **Benefits of establishing this best practice:** 
+  Encryption effort is directed by regulatory requirement, so compliance is met without wasted overhead. 
+  Data-plane throughput and packet-per-second headroom are preserved by not double-encrypting already-protected traffic. 
+  Cost is controlled because encryption resources are applied where they are needed rather than uniformly. 
+  Clear per-interface encryption decisions produce an auditable record of why each flow is or isn't additionally encrypted. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 3GPP already specifies encryption at several layers, so stacking transport encryption on top consumes resources without adding security. NAS-level encryption helps protect traffic between the user equipment and the core, 3GPP specifies IPsec on certain interfaces such as N2 and N3 in some deployments, and application-layer TLS helps protect service traffic. Understand what is already encrypted and by which mechanism, then apply transport encryption only where encryption is missing and a regulation requires it. 

 Classify most interfaces with the following three questions: 

1.  Does a regulation mandate transport-layer encryption for this traffic? 

1.  Does 3GPP already specify encryption for this interface? 

1.  Is the traffic already encrypted by application-layer protocols such as TLS or DTLS? 

 Control-plane signaling between network functions (such as N2, N4, and the service-based interfaces) usually warrants IPsec or mutual TLS under operator policy, and sometimes regulation. Because these interfaces carry relatively low bandwidth, the PPS cost of encrypting them is manageable. Inventory data-plane flows per interface before deciding on encryption. Classify every data-plane flow on N3, N6, or N9 by whether it is already encrypted at the application layer (HTTPS, QUIC, TLS, DTLS) or carried in cleartext. Common unencrypted classes include plaintext HTTP, unencrypted DNS, SIP without TLS, and legacy IoT protocols such as unencrypted MQTT or CoAP. Where the inventory shows the traffic is predominantly application-encrypted, wrapping it in IPsec doubles the overhead for no gain. Where a non-trivial unencrypted mix crosses a less-trusted boundary, transport encryption is the correct choice regardless of throughput cost. Some operators still encrypt N3 for defense in depth. Make encryption decisions deliberately, with understood performance tradeoffs. 

 Performance considerations make this decision about both security and cost. Encryption on a high-PPS data-plane interface can push an instance into its packet-per-second ceiling and degrade service performance. 

### Implementation steps
<a name="implementation-steps"></a>
+  Classify every interface by encryption need: assess each interface (N1 through N6, service-based, and roaming) against regulatory requirement, 3GPP-specified encryption, existing application-layer encryption, and operator policy, and record the result. On data-plane interfaces, flag any traffic class carried in cleartext — plaintext HTTP, unencrypted DNS, SIP without TLS, MQTT, CoAP — so the per-interface decision reflects the actual flow mix rather than an assumption. 
+  Encrypt control-plane interfaces where required: apply IPsec or mutual TLS on the control-plane interfaces that need it, provisioning certificates through AWS Certificate Manager and sizing instances for PPS headroom. 
+  Document data-plane decisions: for each data-plane interface, record whether transport encryption is applied and, where it is, the performance impact and the reason, so the choice is auditable. 
+  Encrypt data at rest: apply data-at-rest encryption with AWS KMS customer-managed keys for all persistent stores holding telco data. 
+  Monitor encryption overhead: track IPsec tunnel throughput, PPS usage, and added latency in Amazon CloudWatch, and alert when encrypted interfaces approach instance PPS limits. 

## Resources
<a name="resources"></a>

 **Key AWS services:** 
+  [AWS Key Management Service](https://aws.amazon.com/kms/) 
+  [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/) 
+  [Amazon VPC](https://aws.amazon.com/vpc/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 