

# AGENTSEC06-BP01 Encrypt and sign inter-agent messages
<a name="agentsec06-bp01"></a>

 Transport-level encryption stops protecting the payload the moment a message lands in a queue or event bus. Message-level signing and encryption keyed per trust zone gives receiving agents cryptographic proof of sender identity and content integrity no matter how many hops the message made. 

 **Desired outcome:** 
+  You protect inter-agent messages at the message level with encryption and signing, independent of transport-level security. 
+  Receiving agents verify message signatures before acting on instructions from other agents. 
+  Messages stored in queues or event buses are encrypted at rest with keys scoped to the appropriate trust zone. 
+  Agents can't forge messages that appear to originate from other agents in the coordination workflow. 

 **Common anti-patterns:** 
+  Relying solely on transport-level encryption (TLS) without message-level signing, so messages stored in queues or event buses can't be verified for tampering at consumption time. 
+  Using a single shared encryption key across all agents, so one key exposure affects every inter-agent message rather than only those in one trust zone. 
+  Not verifying message signatures before acting on inter-agent instructions, letting an agent act on forged or tampered instructions without any integrity check. 

 **Benefits of establishing this best practice:** 
+  Message-level integrity verification persists beyond the transport layer, so messages stored in queues or event buses can be verified at consumption time. 
+  Scoped key management limits the impact of a key exposure to a single trust zone rather than the entire multi-agent system. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Two distinct properties are at stake: who sent the message (covered by AGENTSEC03-BP01 for authentication) and whether the content is what the sender actually sent. Transport-level encryption provides the second property only while the message is in transit. The moment the message lands in an Amazon SQS queue, Amazon EventBridge bus, or AWS Step Functions state machine, there is no transport to protect it, and any modification between delivery and consumption is invisible. Message-level signing provides cryptographic proof that a specific message was sent by a specific agent and has not been modified, regardless of how many intermediary services it passed through. 

 Scope matters. For direct agent-to-agent communication within a single trust zone, the transport-level security and authentication provided by [Amazon Bedrock AgentCore Runtime](https://aws.amazon.com/blogs/machine-learning/introducing-agent-to-agent-protocol-support-in-amazon-bedrock-agentcore-runtime/) (TLS 1.2\+ with OAuth 2.0 or SigV4) is typically sufficient. Layer message signing on top when payload integrity needs to persist beyond the transport, or when a receiving agent needs cryptographic proof of which specific agent sent an instruction. 

 AWS KMS asymmetric keys are the mechanism. The sending agent signs the message payload through the KMS Sign API, and the receiving agent verifies the signature through the KMS Verify API before acting on the message. This gives end-to-end integrity verification that is independent of the transport layer: even if a message passes through multiple intermediary services (load balancers, queues, event buses), the signature proves it was created by the claimed sender and has not been modified. Separate keys per trust zone limit the scope affected by a single key exposure. 

 For asynchronous agent messaging through Amazon SQS, enable server-side encryption using AWS KMS customer-managed keys. Configure separate keys for different agent trust zones so a key exposure in one zone doesn't affect messages in other zones, and use SQS message attributes to carry the message signature alongside the encrypted payload so receiving agents verify both authenticity and integrity at consumption time. 

 AgentCore Runtime provides session isolation and built-in authentication for agents using the Agent-to-Agent (A2A) protocol. A2A handles authentication for inter-agent interactions, but for messages that cross trust boundaries, carry sensitive data, or pass through intermediary services, message-level signing layers on top of the protocol's built-in protections. 

 AWS PrivateLink routes inter-agent communications through private network endpoints, keeping traffic off the public internet. That complements message-level encryption by reducing the network exposure of inter-agent traffic. Store signing key ARNs in Parameter Store, a capability of AWS Systems Manager, configure automatic key rotation in AWS KMS with a rotation period matching your security requirements, and configure Amazon CloudWatch alarms for key usage anomalies (unexpected signing operations from agents that should only be verifying, signing volume spikes suggesting a runaway loop). 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Create trust-zone-scoped KMS key pairs:** Provision AWS KMS asymmetric key pairs for message signing, with separate keys for each agent trust zone. 

1.  **Sign messages on send:** Implement message signing in sending agents through the AWS KMS Sign API, attaching the signature as a message metadata attribute. 

1.  **Verify signatures on receive:** Implement signature verification in receiving agents through the AWS KMS Verify API, rejecting any message that fails verification before processing. 

1.  **Encrypt SQS queues with customer-managed keys:** Enable server-side encryption on Amazon SQS queues used for asynchronous inter-agent messaging, using customer-managed AWS KMS keys scoped per trust zone. 

1.  **Layer signing on top of A2A for cross-boundary traffic:** For agents on AgentCore Runtime using A2A, add message-level signing for communications that cross trust boundaries on top of the protocol's built-in authentication. 

1.  **Route through PrivateLink:** Configure AWS PrivateLink for inter-agent service communications to keep traffic on private network endpoints. 

1.  **Manage keys and alert on anomalies:** Store signing key ARNs in Parameter Store, a capability of AWS Systems Manager, configure automatic key rotation in AWS KMS, and set Amazon CloudWatch alarms for key usage anomalies. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTSEC03-BP01 Implement strong authentication for agent identities](agentsec03-bp01.html) 
+  [AGENTSEC06-BP02 Implement workflow orchestration security controls](agentsec06-bp02.html) 
+  [AGENTSEC06-BP03 Establish trust boundaries between agents](agentsec06-bp03.html) 

 **Related documents:** 
+  [Introducing agent-to-agent protocol support in Amazon Bedrock AgentCore Runtime](https://aws.amazon.com/blogs/machine-learning/introducing-agent-to-agent-protocol-support-in-amazon-bedrock-agentcore-runtime/) 
+  [Digital signing with the new asymmetric keys feature of AWS KMS](https://aws.amazon.com/blogs/security/digital-signing-asymmetric-keys-aws-kms/) 
+  [Code signing using ACM Private CA and AWS KMS asymmetric keys](https://aws.amazon.com/blogs/security/code-signing-aws-certificate-manager-private-ca-aws-key-management-service-asymmetric-keys/) 
+  [AWS KMS documentation](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) 
+  [Amazon SQS security best practices](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-security-best-practices.html) 

 **Related services:** 
+  [AWS Key Management Service](https://aws.amazon.com/kms/) 
+  [Amazon SQS](https://aws.amazon.com/sqs/) 
+  [AWS Systems Manager](https://aws.amazon.com/systems-manager/) 
+  [AWS PrivateLink](https://aws.amazon.com/privatelink/) 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 