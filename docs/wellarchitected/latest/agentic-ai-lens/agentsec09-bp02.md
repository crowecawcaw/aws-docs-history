

# AGENTSEC09-BP02 Conduct context-aware penetration testing with multi-agent attack simulation
<a name="agentsec09-bp02"></a>

 Generic scanners miss vulnerabilities that only surface in agent orchestration, tool parameter construction, and inter-agent delegation. Context-aware testing driven by specialized attacker agents that adapt to what the application reveals finds the chained exploits that static scripts can't reach. 

 **Desired outcome:** 
+  You use context-aware, multi-agent attack simulation for penetration testing that adapts to the specific application under test. 
+  The testing system develops deep understanding of the application's architecture, data flows, and agent interactions, then executes sophisticated attack chains combining multiple vulnerability types. 
+  Findings are validated through actual exploitation, prioritized by real-world exploitability, and documented with reproducible attack paths and ready-to-implement fixes. 

 **Common anti-patterns:** 
+  Running generic vulnerability scanners against agentic AI systems without adapting test scenarios to the agent's specific capabilities and tool integrations, missing tool parameter injection, memory poisoning, and delegation-chain privilege escalation. 
+  Testing individual agent components in isolation without exercising multi-agent coordination paths, missing trust boundary violations and cascading failures from a compromised agent in an orchestration chain. 
+  Relying on predefined test scripts that don't adapt based on application responses, missing vulnerabilities that require dynamic exploration because agentic systems behave differently based on context and prior interactions. 

 **Benefits of establishing this best practice:** 
+  Context-aware testing adapts to the specific application, discovering vulnerabilities that static test scripts and generic scanners miss. 
+  Actual exploitation validates findings, reducing false positives and letting teams prioritize based on real risk. 
+  Specialized agents collaborate on reconnaissance, vulnerability analysis, exploit validation, and finding prioritization, identifying chained vulnerabilities that combine information disclosure with privilege escalation. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Penetration testing that chases agent vulnerabilities has to look like the attack it is simulating. Attacker agents don't run the same script on every target. They map the surface, probe for weaknesses, adapt to responses, and chain findings. Testing tools need to do the same or they miss exactly the scenarios that matter most for agentic systems. 

 A multi-agent penetration testing system orchestrates specialized security agents collaboratively. The system begins with baseline scanning to establish coverage, then conducts broad reconnaissance to map the application surface and identify initial attack vectors. Building on these findings, it dynamically generates focused test tasks tailored to the specific application context, reasoning about discovered endpoints, business logic patterns, and potential vulnerability chains. 

 [AWS Security Agent](https://aws.amazon.com/security-agent/) provides on-demand penetration testing with this multi-agent approach. It deploys specialized AI agents that develop application context from provided documentation and credentials, then execute attack chains to identify complex vulnerabilities conventional tools miss. The architecture includes agents for attack surface mapping, business logic analysis, finding validation, and vulnerability prioritization based on actual exploitability scored using the Common Vulnerability Scoring System (CVSS). The system performs chained attacks, combining an information disclosure flaw with privilege escalation to reach sensitive resources, or chaining insecure direct object references with authentication bypass, rather than stopping at single-vulnerability detection. 

 AWS Security Agent starts with the OWASP Top 10 and then customizes its approach based on the context it learns from documents and code. The agent adapts to the responses it receives, building a custom attack plan for each application. Provide target URLs, authentication details, source code, and documentation so the agent can develop deep application understanding before testing begins. 

 Agent-specific scenarios need manual supplementation. Prompt injection chains across agent boundaries, tool parameter manipulation, memory poisoning through crafted tool outputs, and human-in-the-loop bypass techniques all require scenarios that go beyond the OWASP baseline. Use the findings from AGENTSEC07-BP05 to inform the scenario library. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Provide application context to the testing agent:** Configure [AWS Security Agent](https://aws.amazon.com/security-agent/) with target application details including URLs, authentication credentials (stored in AWS Secrets Manager), source code, and architecture documentation. 

1.  **Run tests across the full surface:** Execute on-demand penetration tests that exercise agent orchestration endpoints, tool invocation paths, and multi-agent communication channels. 

1.  **Triage validated findings by exploitability:** Review findings with reproducible attack paths, impact analysis, and suggested code fixes, and prioritize remediation based on CVSS scores and actual exploitability. 

1.  **Add agent-specific scenarios manually:** Supplement automated testing with scenarios targeting prompt injection chains, tool parameter manipulation, and multi-agent trust boundary violations. 

1.  **Track posture over time:** Store penetration test results and compare them across test cycles to measure security posture improvement. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTSEC07-BP05 Regular security assessments and red teaming](agentsec07-bp05.html) 
+  [AGENTSEC02-BP02 Validate tool inputs and outputs](agentsec02-bp02.html) 
+  [AGENTSEC09-BP01 Integrate AI-powered vulnerability scanning across the development lifecycle](agentsec09-bp01.html) 

 **Related documents:** 
+  [Inside AWS Security Agent: A multi-agent architecture for automated penetration testing](https://aws.amazon.com/blogs/security/inside-aws-security-agent-a-multi-agent-architecture-for-automated-penetration-testing/) 
+  [AWS Security Agent FAQs](https://aws.amazon.com/security-agent/faqs/) 
+  [Security Considerations for AWS Security Agent and AI assisted penetration testing](https://docs.aws.amazon.com/securityagent/latest/userguide/security-guidance.html) 
+  [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) 

 **Related services:** 
+  [AWS Security Agent](https://aws.amazon.com/security-agent/) 
+  [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 