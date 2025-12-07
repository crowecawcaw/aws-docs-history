# Exposure findings in Security Hub

An exposure finding in Security Hub represents the correlation of multiple security signals that identify potential security risks in your AWS environment.
Exposure findings help you understand and prioritize security risks by automatically analyzing combinations of vulnerabilities, configurations, threats, and resource relationships.
An exposure finding includes traits and signals. A signal can include one or more types of exposure traits.
Security Hub generates an exposure finding when signals from Security Hub CSPM, Amazon Inspector, GuardDuty, Macie, or other AWS services indicate the presence of an exposure.
A resource can be the primary resource in, at most, one exposure finding.
If a resource doesn't have any exposure traits or has insufficient traits, Security Hub doesn't generate an exposure finding for that resource.

## How exposure findings work

Security Hub generates exposure findings by:

- **Analyzing signals from multiple AWS security services**: Security Hub continuously collects and analyzes security signals from multiple AWS security services. It ingests findings from GuardDuty for threat detection, Amazon Inspector for vulnerability assessment, Security Hub CSPM for configuration checks, and Macie for sensitive data exposure. These signals are processed through advanced correlation engines to identify potential security risks.
- **Evaluating resource configurations and relationships**: The system performs detailed evaluation of resource configurations against security best practices. It examines service-specific settings, compliance requirements, and security controls. This analysis helps identify misconfigurations that could lead to security vulnerabilities when combined with other factors.
- **Assessing network reachability**: A crucial component of exposure findings is the assessment of network reachability. The system evaluates both internet exposure and internal network access paths. It analyzes security group configurations and network ACL settings to determine potential attack vectors. This analysis helps identify resources that might be inadvertently exposed to unauthorized access.
- **Correlating related security issues**: The correlation engine maps relationships between AWS resources, analyzing how they interact and identifying potential security implications. It examines IAM permissions, roles, and resource access patterns to understand the broader security context. This process helps identify security risks that might exist due to the combination of seemingly innocent individual configurations.

## Components of an exposure finding

Each exposure finding includes:

- **Title and description of the potential security risk** - Each exposure finding includes a clear, descriptive title that immediately conveys the nature of the security risk. The description provides detailed information about the potential security impact, affected resources, and the broader context of the exposure. This information helps security teams quickly understand and assess the risk.
- **Severity classification (Critical, High, Medium, Low)**:
  - **Critical severity** indicates immediate attention is required due to high likelihood of exploit and significant potential impact. These findings typically represent easily discoverable and exploitable vulnerabilities.
  - **High severity** suggests priority attention is needed, with moderate to high exploit likelihood and substantial potential impact. These findings might be relatively easy to exploit but might require specific conditions.
  - **Medium severity** indicates scheduled attention is required, with lower exploit likelihood and moderate potential impact. These findings typically require more complex exploitation methods.
  - **Low severity** suggests routine attention is needed, with limited exploit potential and minor impact. These findings are typically difficult to exploit and present minimal risk.

- **Contributing traits that led to the exposure**: Contributing traits represent the primary factors that led to the exposure finding. These include direct security vulnerabilities, configuration issues, network exposure conditions, and resource permission settings. Each trait provides specific details about how it contributes to the overall security risk.
- **Attack path visualization**: The attack path visualization provides an interactive diagram showing how potential attackers could exploit the identified exposure. It maps resource relationships, network paths, and potential impact flow, helping security teams understand the full scope of the risk and plan effective remediation strategies.
- **Detailed remediation guidance**: Each exposure finding includes detailed remediation guidance with specific, actionable steps to address the identified risks. This guidance includes best practice recommendations, configuration correction steps, and prioritized action items. The guidance is tailored to the specific exposure scenario and considers the AWS services involved.
- **Resource configuration details**: Configuration of the resource at the time the finding was created as well as current configuration of the resource in the Security Hub resource inventory dashboard.
- **Contextual traits providing additional security context**: Contextual traits are additional security markers that were identified by Security Hub but were not used to create an exposure finding.

## Severity classification

Exposure findings are classified based on:

- Ease of discovery
- Ease of exploit
- Likelihood of exploit
- Public awareness
- Potential impact

For more information, see [Exposure findings severity classification](exposure-findings-severity.md "exposure-findings-severity.md").

## Benefits of exposure findings

- **Reduced manual analysis through automated correlation**: Exposure findings significantly reduce the time and effort required for security analysis through automated correlation and intelligent risk prioritization. Security Hub continuously monitors your AWS environment, automatically identifying and correlating security risks that might be missed through manual review.
- **Prioritized view of security risks**: Security Hub employs sophisticated risk assessment algorithms to prioritize exposures based on severity, impact, resource criticality, and exploit likelihood. This helps security teams focus their efforts on the most significant risks first, improving the efficiency of security operations.

## Sources of exposure findings

Exposure findings incorporate data from:

- **Amazon GuardDuty integration** provides continuous threat detection capabilities within exposure findings. It monitors for malicious activities, potential account compromises, and behavioral anomalies. The system incorporates these threat findings into the broader exposure analysis, helping identify when threats combine with other security issues to create significant risks.
- **Amazon Inspector** contributes crucial vulnerability assessment data to exposure findings. It provides detailed information about network reachability, software vulnerabilities, and security best practice violations. This integration helps understand how vulnerabilities might be exploited through identified attack paths.
- **Security Hub CSPM integration** ensures that configuration compliance and security standards are considered in exposure analysis. It evaluates resources against established security controls and best practices, providing a foundation for understanding configuration-based risks.
- enhances exposure findings with sensitive data discovery and classification capabilities. It identifies where sensitive data exists within your AWS environment and evaluates potential privacy risks, helping understand the potential impact of identified exposures.

## Best practices

- **Regularly review exposure findings**: Effective exposure management requires structured review processes. Organizations should implement daily reviews of critical exposures, weekly assessments of overall exposure status, monthly trend analysis, and quarterly security posture evaluations. This layered approach ensures appropriate attention to both immediate risks and long-term security trends.
- **Prioritize critical and high-severity exposures**: Successful exposure management depends on effective risk prioritization. Organizations should focus first on critical exposures while considering resource criticality and business impact. This risk-based approach helps ensure security efforts align with business priorities and maximize risk reduction.
- **Implement recommended remediation steps**: Exposure remediation should follow a systematic approach. Organizations should carefully implement recommended remediation steps, maintain detailed documentation of changes, conduct thorough testing of modifications, and validate the effectiveness of implemented fixes. This methodical approach helps ensure successful risk mitigation while avoiding unintended consequences.
- **Configure automated response rules**: Maximizing the value of exposure findings requires effective automation. Organizations should implement automated response rules, configure appropriate notifications, establish efficient workflows, and maintain comprehensive audit trails. This automation helps ensure consistent and timely response to identified exposures while reducing manual effort.
