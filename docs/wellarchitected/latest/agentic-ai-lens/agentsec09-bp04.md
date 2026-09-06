

# AGENTSEC09-BP04 Establish scoped and controlled testing environments for agent security assessments
<a name="agentsec09-bp04"></a>

 Penetration testing that runs real exploit attempts against production agents can trigger tool calls, corrupt memory, or expose sensitive data. Scoped test environments with dedicated credentials and isolated agent state let teams run thorough assessments without risking production impact. 

 **Desired outcome:** 
+  You conduct security assessments for agentic AI systems in controlled environments with clearly defined scope, dedicated credentials, and isolation from production systems. 
+  You manage test credentials through secure vaulting services with automatic rotation, and testing activities are logged in your account for full auditability. 
+  The testing environment replicates production agent behavior closely enough to produce valid findings while containing the scope of exploit attempts. 

 **Common anti-patterns:** 
+  Running penetration tests directly against production agentic systems without scope controls, risking agents executing tool calls against production databases, sending messages to real users, or triggering downstream workflows in response to test inputs. 
+  Using shared or long-lived credentials for security testing, creating credential exposure risk where test credentials could be captured in logs, test artifacts, or finding reports. 
+  Not isolating test agent instances from production agent memory and state, letting test inputs and attack payloads pollute production agent memory and influence future agent behavior for real users. 

 **Benefits of establishing this best practice:** 
+  Environment isolation allows thorough security assessment, including real exploit attempts, without risking production impact or data corruption. 
+  Vaulting services limit credential exposure during testing and support automatic rotation after assessment cycles. 
+  Test logs stored in your account provide full visibility into testing activities for compliance and incident investigation. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 An agent under security test is an agent executing exploit attempts. In production, an agent running an exploit payload will actually call the tool it was told to call, send the email it was told to send, and write to the memory it was told to modify. The containment requirement is therefore structural: the test environment needs to look enough like production to produce valid findings, and it needs to be separated enough from production that exploit attempts can't reach real resources. 

 Provision dedicated testing environments that replicate the agent architecture, tool integrations, and data flows of production while maintaining isolation. Use separate agent instances with their own memory stores, tool endpoints, and permission boundaries. Configure test environments to use mock or sandboxed versions of external services where full production connectivity isn't required for valid testing results. 

 Manage test credentials through AWS Secrets Manager, storing static credentials (username and password) securely and supporting dynamic credential provisioning through AWS Lambda functions for more complex authentication scenarios. [AWS Security Agent](https://aws.amazon.com/security-agent/) supports both static credentials stored in AWS Secrets Manager and dynamic credentials accessed through AWS Lambda functions, giving flexible authentication that adapts to different application architectures. Rotate test credentials after each assessment cycle and audit credential access logs to detect any unauthorized usage. 

 Scope definition is a precondition, not an afterthought. Specify before each assessment which agent endpoints, tool integrations, and data stores are in scope and which are explicitly excluded. For AWS Security Agent penetration testing, provide target URLs, authentication details, source code, and documentation so the agent can develop application context within the defined scope. All test logs are stored in Amazon CloudWatch in your account for full visibility. 

 For multi-agent systems, test agent-to-agent communication paths in isolation before testing the full orchestration chain. That approach identifies trust boundary violations and delegation issues at the individual interaction level before they compound in complex multi-agent scenarios. Network segmentation and IAM policies help prevent test agent instances from reaching production resources. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Provision isolated test environments:** Replicate production agent architecture with isolated memory stores, tool endpoints, and permission boundaries. 

1.  **Manage credentials in Secrets Manager:** Store test credentials in AWS Secrets Manager with automatic rotation policies, or use AWS Lambda functions for dynamic credential provisioning for complex authentication scenarios. 

1.  **Define and document test scope:** Specify in-scope agent endpoints, tool integrations, and data stores for each assessment, with explicit exclusions for sensitive production resources. 

1.  **Contain the scope at the network and IAM layers:** Configure network segmentation and IAM policies that help prevent test agent instances from accessing production resources. 

1.  **Verify test logging in CloudWatch:** Confirm all test logs are captured in Amazon CloudWatch in your account, and review logs after each assessment to confirm scope adherence and identify unintended interactions. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTSEC09-BP02 Conduct context-aware penetration testing with multi-agent attack simulation](agentsec09-bp02.html) 
+  [AGENTSEC03-BP03 Implement least privilege with dynamic boundaries](agentsec03-bp03.html) 
+  [AGENTSEC07-BP04 Behavioral anomaly detection and agent containment](agentsec07-bp04.html) 

 **Related documents:** 
+  [Security Considerations for AWS Security Agent and AI assisted penetration testing](https://docs.aws.amazon.com/securityagent/latest/userguide/security-guidance.html) 
+  [AWS Security Agent FAQs](https://aws.amazon.com/security-agent/faqs/) 
+  [AWS Secrets Manager documentation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) 
+  [AWS Well-Architected Framework, Security Pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) 

 **Related services:** 
+  [AWS Security Agent](https://aws.amazon.com/security-agent/) 
+  [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) 
+  [AWS Lambda](https://aws.amazon.com/lambda/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [AWS Identity and Access Management](https://aws.amazon.com/iam/) 