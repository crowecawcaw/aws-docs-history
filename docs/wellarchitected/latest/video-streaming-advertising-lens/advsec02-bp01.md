

# ADVSEC02-BP01 Encrypt DSP to SSP communication in transit using TLS

 Programmatic advertising bid traffic crosses organizational and network boundaries between independent companies with their own infrastructure. Application-layer encryption is the only mechanism that can protect this traffic across those boundaries. Network-layer controls that secure traffic within one organization do not address the cross-organization threat model. 

 **Desired outcome:** 
+  You have enforced TLS 1.2 or higher on all bid request and response traffic between your infrastructure and programmatic partners. 
+  Your TLS implementation accounts for latency constraints of real-time bidding, using session resumption and connection pooling to minimize handshake overhead. 
+  You have certificate management processes that scale to hundreds of SSP and DSP partner connections without manual intervention. 

 **Common anti-patterns:** 
+  Accepting unencrypted HTTP connections from partners to reduce latency, which exposes bid pricing and audience signals to network observers. 
+  Using TLS 1.0 or 1.1 with weak cipher suites on legacy partner connections. 
+  Deploying a single wildcard certificate across all partner-facing endpoints, so any certificate rotation becomes a high-risk operation that affects every partner at once. 

 **Benefits of establishing this best practice:** 
+  Helps protect bid pricing signals and audience data from interception during cross-company transit, reducing the risk of competitive intelligence harvesting. 
+  Helps maintain data integrity of bid responses, reducing the risk of manipulation of win notifications or pricing between DSP and SSP. 
+  Produces TLS configuration and certificate evidence for partner connections, which a privacy or legal authority can apply to obligations assessed under regulations such as GDPR or CCPA. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Real-time bidding gives encryption a fixed latency budget. A bid response that arrives after the auction closes earns nothing, so the cost of establishing a connection competes directly with the time you have to price the bid. Full TLS handshakes add one to two round trips against typical latency budgets of 50 to 100 milliseconds. Design for connection reuse, because protocol version and cipher choice affect latency far less than whether a handshake happens. Measure your own figures, because round-trip time depends on where each endpoint is located. 

 The TLS version you enforce depends on partner readiness. A minimum version that rejects older protocols refuses connections from partners still running them, turning a configuration change into a commercial negotiation. Decide who owns that negotiation before you set the minimum, because the alternative is a permanent exception with no scheduled review. 

 Four connectivity models exist for securing bid traffic between partners: 

1.  Public TLS over the internet is the simplest to establish, since partners need only your endpoint URL, and it works for initial integrations, but it exposes traffic to network-layer observers and provides no traffic isolation. 

1.  AWS PrivateLink provides a private encrypted path with no internet transit, which suits high-volume same-cloud partners, but it requires both parties to operate on the same cloud provider and adds endpoint configuration for each partner. 

1.  AWS Direct Connect with MACsec encryption provides point-to-point dedicated bandwidth from on-premises facilities with link-layer encryption, but it requires physical cross-connect provisioning measured in weeks and makes sense only for partners in the same facility or metro area. 

1.  A purpose-built advertising network such as AWS RTB Fabric provides optimized routing between connected participants, but it limits connectivity to participants within that network. 

 Managing hundreds of partner certificates manually leads to rotation failures. A missed rotation on a high-volume partner connection causes an outage that presents as an authentication failure outside business hours and forces an emergency response. Rotation responsibility is often unclear between security, infrastructure engineering, and partner operations teams. 

 Your privacy or legal authority decides which data, purposes, and jurisdictions are in scope, which transfer mechanism or exception applies at each boundary, and what evidence proves those choices. Record that decision before you select a connectivity model, because a path that crosses an unapproved boundary is expensive to change after partner integration. A system serving inventory in more than one jurisdiction can need separate processing paths, each terminating within the boundary approved by the assessment. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Enforce TLS 1.2 or higher on all partner-facing endpoints:** Configure [Application Load Balancer security policies](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html) or Amazon CloudFront security policies to reject TLS 1.0 and TLS 1.1 connections. Select cipher suites that meet your performance requirements for high-throughput bidding traffic, preferring ECDHE key exchange with AES-GCM where hardware acceleration is available. Record the floor, each partner exception, its owner, and its expiry date. 

1.  **Deploy persistent HTTP/2 connections for high-QPS SSP-DSP pairs:** Configure connection pooling to maintain long-lived TLS sessions between your infrastructure and high-volume partners. This amortizes handshake cost across thousands of requests per second. Monitor connection health and implement automatic reconnection with TLS 1.3 0-RTT resumption. 

1.  **Automate certificate lifecycle management:** Use [AWS Certificate Manager managed renewal](https://docs.aws.amazon.com/acm/latest/userguide/managed-renewal.html) for partner-facing certificates. For mutual TLS partner connections, maintain a certificate for each partner with an independent rotation schedule. Configure Amazon CloudWatch alarms for certificates approaching expiration, and name the team that responds to them. 

1.  **Select and configure a connectivity model for each partner:** Choose the model matching the partner's scale, latency requirement, and cloud location from the four described in the guidance. Establish [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/) endpoints for SSP and DSP partners operating on AWS, and configure the optimized private network path for partners connected through AWS RTB Fabric. Record the model chosen for each partner, the reason, and the approved processing boundary it operates within. 

1.  **Enforce region restrictions for cross-border partner traffic:** Apply IAM permissions boundaries with regional conditions and service control policies (SCPs) at the organizational level to restrict which Regions process advertising workloads carrying resident data from jurisdictions with data location requirements, such as the EU or California. These guardrails restrict API use rather than proving where data resides, so verify separately that logs, backups, and derived datasets stay inside the approved boundary. Record the approved boundary, the applicable transfer mechanism, and the evidence artifacts your compliance obligations require. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVSEC01-BP03 Restrict DSP outbound traffic to authorized SSPs only](advsec01-bp03.md) 
+  [ADVSEC05-BP02 Design for compliance across both linear and digital data flows](advsec05-bp02.md) 

 **Related documents:** 
+  [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/) 
+  [AWS Direct Connect MACsec encryption](https://docs.aws.amazon.com/directconnect/latest/UserGuide/MACsec.html) 
+  [ALB security policies for TLS](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html) 

 **Related services:** 
+  [AWS PrivateLink](https://aws.amazon.com/privatelink/) 
+  [AWS Direct Connect](https://aws.amazon.com/directconnect/) 
+  [AWS RTB Fabric](https://aws.amazon.com/rtb-fabric/) 
+  [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/) 