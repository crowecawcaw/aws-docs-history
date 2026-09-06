

# AGENTSEC03-BP01 Implement strong authentication for agent identities
<a name="agentsec03-bp01"></a>

 Shared API keys and one-way TLS give agents enough network reachability to be useful and enough ambiguity to be impersonated. Cryptographic identity for both sides of every call, with automated lifecycle and immediate revocation, is the control that makes every agent communication auditable and reversible. 

 **Desired outcome:** 
+  You authenticate all agent-to-agent and agent-to-service communications using strong cryptographic mechanisms, with mutual authentication that helps prevent impersonation and interception. 
+  You automate certificate lifecycle management so expired certificates don't cause authentication failures or security gaps. 
+  You can revoke affected agent identities immediately, cutting off unauthorized access within minutes. 

 **Common anti-patterns:** 
+  Using shared API keys or static tokens for agent authentication instead of certificate-based or OAuth mechanisms, producing credentials that are hard to rotate and straightforward to exfiltrate. 
+  Implementing one-way TLS (server authentication only) without mutual authentication, so any client on a permitted network path can reach the endpoint without proof of its agent identity. 
+  Managing certificate lifecycles manually, leading to expired certificates that either cause outages or are renewed without proper security review. 

 **Benefits of establishing this best practice:** 
+  Certificate-based or OAuth authentication provides cryptographic proof of identity for both parties in every agent communication. 
+  Automated certificate lifecycle management reduces the risk of expired certificates causing outages or security gaps. 
+  CRL and OCSP revocation provides the ability to cut off unauthorized access within minutes when an agent identity is affected. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Authentication for agents has two distinct jobs: proving the agent is who it claims to be, and proving that to the receiver cryptographically rather than through network-path heuristics. Static credentials fail both tests. They are trivial to copy, hard to rotate, and their holder is indistinguishable from their issuer. The design pattern is cryptographic identity managed centrally, with lifecycle automation and revocation as first-class operations rather than afterthoughts. 

 [Amazon Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-identity.html) handles the OAuth side of that pattern. It provides managed OAuth 2.0 flows and identity federation for agentic workloads, issuing, validating, and rotating tokens without the operational burden of running that infrastructure. Each agent registers in the centralized agent identity directory and receives a unique identity. The GetWorkloadAccessTokenForJWT API issues agent-specific access tokens bound to the requesting agent's identity. The token vault secures OAuth tokens with AWS KMS encryption (customer-managed keys supported) and enforces per-agent access controls so one agent can't retrieve another's tokens. 

 For services that require certificate-based authentication rather than OAuth, AWS Private Certificate Authority (AWS Private CA) is the managed path for issuing internal mTLS client and server certificates. AWS Private CA handles issuance and supports automated renewal lifecycles, and certificate revocation through CRL or OCSP provides the cutoff when an identity is affected. Mutual TLS (mTLS) on AWS Application Load Balancers or Amazon API Gateway configurations gives agent-to-agent traffic symmetric proof: both sides present certificates, both sides verify. Private keys live in AWS Secrets Manager or Parameter Store, a capability of AWS Systems Manager with AWS KMS encryption at rest and automatic rotation policies, so the key itself never becomes a long-lived static credential. 

 Detection rounds out the pattern. Amazon GuardDuty flags unusual authentication patterns, agents authenticating from unexpected IP addresses or at unusual times, and findings route into AWS Security Hub CSPM for centralized event management. That gives the security team a single place to see when an identity is being used in ways that don't match its normal profile, whether the credentials themselves have been revoked. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Deploy AgentCore Identity:** Deploy [Amazon Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-identity.html) for agent authentication, configure identity federation for cross-service access, and register each agent in the centralized identity directory for unique, trackable identities. 

1.  **Secure tokens in the vault:** Configure the AgentCore Identity token vault for OAuth token storage using customer-managed AWS KMS keys for encryption, and enforce strict per-agent access controls for credential retrieval. 

1.  **Issue agent certificates from AWS Private CA:** Set up AWS Private Certificate Authority for agent identity certificates, with automated renewal lifecycles configured. 

1.  **Enforce mutual TLS end-to-end:** Configure mTLS on all agent-to-agent communication endpoints through Application Load Balancers or Amazon API Gateway with mTLS authentication. 

1.  **Store keys in Secrets Manager with rotation:** Store all agent private keys and credentials in AWS Secrets Manager with encryption at rest and automatic rotation policies enabled. 

1.  **Turn on revocation checking:** Implement certificate revocation through CRL or OCSP so affected agent certificates can be invalidated immediately. 

1.  **Alarm on authentication anomalies:** Configure Amazon GuardDuty to detect unusual authentication patterns and route findings to AWS Security Hub CSPM for centralized security event management. 

1.  **Review certificate inventory quarterly:** Identify and remediate certificates approaching expiration or using deprecated algorithms on a quarterly cadence. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTSEC03-BP02 Separate agent and human user permission](agentsec03-bp02.html) 
+  [AGENTSEC03-BP03 Implement least privilege with dynamic boundaries](agentsec03-bp03.html) 
+  [AGENTSEC06-BP01 Encrypt and sign inter-agent messages](agentsec06-bp01.html) 

 **Related documents:** 
+  [Securing AI agents with Amazon Bedrock AgentCore Identity](https://aws.amazon.com/blogs/security/securing-ai-agents-with-amazon-bedrock-agentcore-identity/) 
+  [Amazon Bedrock AgentCore Identity documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-identity.html) 
+  [AgentCore Identity supported authentication patterns](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/common-use-cases.html) 
+  [AWS Private CA documentation](https://docs.aws.amazon.com/privateca/latest/userguide/PcaWelcome.html) 

 **Related services:** 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [AWS Private CA](https://aws.amazon.com/private-ca/) 
+  [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) 
+  [Amazon GuardDuty](https://aws.amazon.com/guardduty/) 
+  [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/) 