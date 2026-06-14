# Agent vulnerability scanning and penetration testing

Agentic AI systems introduce new attack surfaces that traditional
application security testing doesn't cover. Agents reason about
inputs, chain multi-step actions, interact with tools and APIs,
and operate with varying degrees of autonomy. These behaviors
create complex vulnerability paths that rule-based scanners and
periodic manual assessments can't address. Automated vulnerability
scanning and penetration testing tailored to agentic workloads
help you identify exploitable weaknesses across the full
development lifecycle, from design documents and code through to
running applications, and validate that security controls hold up
under realistic attack scenarios.

| AGENTSEC09: How do you perform vulnerability scanning and<br>penetration testing for agentic AI systems? |
| -------------------------------------------------------------------------------------------------------- |
|                                                                                                          |

## Capability intent

- Security testing covers the full agentic AI development
  lifecycle, from design documents through pull requests and
  into running applications, so vulnerabilities are caught at
  the point where remediation is cheapest.
- Vulnerability scanning and penetration testing reason about
  agent behavior, including tool invocations, multi-agent
  delegation, memory handling, and prompt injection chains,
  rather than relying only on signatures for known web
  application flaws.
- Findings are validated through actual exploitation, ranked
  by real-world exploitability, and paired with reproducible
  attack paths and ready-to-implement fixes so that
  development teams can remediate without waiting for
  specialist intervention.
- Security assessments run in dedicated testing environments
  with scoped credentials, logged activity, and
  impact-containment controls, so realistic attack simulation
  doesn't put production agents, memory, or downstream systems
  at risk.
- Runtime threat detection, vulnerability scanning, and
  penetration test findings are correlated in a unified view,
  with automated remediation workflows that tighten mean time
  to detection and mean time to remediation.

## Maturity levels

These levels summarize what each stage of maturity looks like
for agent vulnerability scanning and penetration testing as a
whole.

| Level | Name      | What it looks like                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ----- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | Initial   | Security scanning is limited to rule-based static<br>analysis against known vulnerability signatures, run<br>late in the development lifecycle or only before<br>release. Penetration testing, if it happens, targets<br>generic web application flaws and doesn't exercise<br>agent-specific attack surfaces. Testing runs against<br>shared or production-like environments with long-lived<br>credentials, and findings are delivered without<br>reproducible attack paths or fix guidance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 2     | Emerging  | Design documents and pull requests receive security<br>review, often manually, and a baseline scanner runs in<br>the build pipeline. Penetration testing uses a<br>documented scenario library but runs on a periodic<br>cadence that lags agent capability changes. Test<br>environments are separated from production for high-risk<br>assessments, and test credentials are stored in<br>[AWS Secrets Manager](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md"). Findings are tracked to<br>remediation but the handoff between security and<br>development teams is still manual.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 3     | Defined   | AI-powered vulnerability scanning runs across design,<br>development, and deployment phases, using tools such as<br>[AWS Security Agent](../../../securityagent/latest/userguide/what-is.md "../../../securityagent/latest/userguide/what-is.md") to evaluate architecture<br>documents, pull requests, and running applications<br>against organization-wide security requirements.<br>[On-demand<br>penetration testing](../../../securityagent/latest/userguide/enable-penetration-test.md "../../../securityagent/latest/userguide/enable-penetration-test.md") exercises agent orchestration<br>endpoints, tool invocation paths, and multi-agent<br>communication channels, with findings carrying<br>[CVSS<br>scores](../../../securityhub/latest/userguide/exposure-findings-severity.md "../../../securityhub/latest/userguide/exposure-findings-severity.md") and reproducible attack paths. Test<br>environments replicate production behavior with isolated<br>memory stores and scoped credentials, and findings from<br>[Amazon GuardDuty](../../../guardduty/latest/ug/what-is-guardduty.md "../../../guardduty/latest/ug/what-is-guardduty.md"),<br>[Amazon Macie](../../../macie/latest/user/what-is-macie.md "../../../macie/latest/user/what-is-macie.md"), and<br>[Amazon Inspector](../../../inspector/latest/user/what-is-inspector.md "../../../inspector/latest/user/what-is-inspector.md") are aggregated in<br>[AWS Security Hub CSPM](../../../securityhub/latest/userguide/what-is-securityhub.md "../../../securityhub/latest/userguide/what-is-securityhub.md"). |
| 4     | Proactive | Security validation is integrated into CI/CD and runs<br>whenever agent system prompts, tool registrations,<br>permission scopes, orchestration patterns, or code are<br>modified.<br>[AWS Security Agent delivers code fix suggestions](../../../securityagent/latest/APIReference/API_StartCodeRemediation.md "../../../securityagent/latest/APIReference/API_StartCodeRemediation.md")<br>alongside validated findings, and regression testing<br>confirms that fixes are effective.<br>[Amazon GuardDuty Extended Threat Detection](../../../guardduty/latest/ug/guardduty-extended-threat-detection.md "../../../guardduty/latest/ug/guardduty-extended-threat-detection.md") correlates<br>multi-step attack sequences across API activity, network<br>behavior, and data access. Automated remediation<br>workflows capture forensic state, apply containment, and<br>route fixes through a tracked pipeline.<br>[Amazon CloudWatch composite alarms](../../../AmazonCloudWatch/latest/monitoring/Create_Composite_Alarm.md "../../../AmazonCloudWatch/latest/monitoring/Create_Composite_Alarm.md") combine<br>[Amazon<br>Bedrock AgentCore evaluation](../../../bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.md "../../../bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.md") score drift with<br>runtime threat findings for high-confidence detection.                                                                                                                                                                                                  |
| 5     | Optimized | Vulnerability scanning, penetration testing, runtime<br>threat detection, and agent evaluations operate as a<br>single feedback loop that continuously refines detection<br>logic, remediation automation, and scenario coverage.<br>Penetration testing runs on-demand and feeds measurable<br>improvement in mean time to detection and mean time to<br>remediation. Test environments, scoped credentials, and<br>impact-containment controls are validated through<br>controlled failure injection, and purple team outcomes<br>flow back into scanner heuristics and detection rules.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

## Common issues to watch for

- Security testing concentrates on deployment-time scans of a
  production build, skipping design-phase review and
  pull-request analysis, so architectural flaws and
  agent-behavior issues are found late when remediation is
  most expensive.
- Scanners and pentests are adapted from traditional web
  applications and don't exercise agent-specific surfaces such
  as tool parameter manipulation, memory poisoning,
  multi-agent trust boundaries, and prompt injection chains,
  leaving the most distinctive agentic risks untested.
- Test activities run against production agents, shared memory
  stores, or downstream systems because no scoped testing
  environment exists, and realistic attack simulation is
  avoided to protect live data rather than because controls
  are known to work.
- Vulnerability findings reach development teams without
  validated exploit paths, severity context, or suggested
  fixes, so remediation is slow, inconsistent, and often
  addresses symptoms rather than the underlying issue.
- Pre-deployment scans, penetration test findings, and runtime
  threat signals live in separate tools with no correlation,
  so known vulnerabilities that are being actively exploited
  are not prioritized ahead of theoretical ones.

###### Best practices

- [AGENTSEC09-BP01 Integrate AI-powered vulnerability scanning across the development lifecycle](agentsec09-bp01.md "agentsec09-bp01.md")
- [AGENTSEC09-BP02 Conduct context-aware penetration testing with multi-agent attack simulation](agentsec09-bp02.md "agentsec09-bp02.md")
- [AGENTSEC09-BP03 Implement continuous security validation with automated remediation](agentsec09-bp03.md "agentsec09-bp03.md")
- [AGENTSEC09-BP04 Establish scoped and controlled testing environments for agent security assessments](agentsec09-bp04.md "agentsec09-bp04.md")
- [AGENTSEC09-BP05 Implement runtime threat detection, security event correlation, and automated remediation for agents](agentsec09-bp05.md "agentsec09-bp05.md")
