# Incident response

AWS Security Agent is a proactive security testing service designed to identify and prevent vulnerabilities before they can be exploited. The service focuses on preventative security validation through design reviews, code analysis, and penetration testing rather than reactive incident detection or response.

## Incident detection

AWS Security Agent does not provide incident detection capabilities. The service operates as a proactive security testing tool that validates applications for vulnerabilities during development and before deployment. For runtime security monitoring and incident detection, use services such as Amazon GuardDuty, AWS Security Hub, or Amazon CloudWatch.

## Incident alerting

AWS Security Agent does not generate real-time alerts for security incidents. The service delivers security findings through the AWS Console after completing design reviews, code analyses, or penetration testing engagements. These findings represent potential vulnerabilities discovered during testing rather than active security incidents.

## Incident remediation

AWS Security Agent does not provide automated incident remediation. The service identifies security vulnerabilities and provides remediation guidance, including:

- Detailed descriptions of identified vulnerabilities
- Reproducible exploit paths for validated findings
- Specific code fixes and implementation guidance
- Impact analysis for discovered issues

Development and security teams use this guidance to manually address vulnerabilities before they reach production environments.

## Supporting incident response activities

While AWS Security Agent is not designed for incident response, security teams can use the service to support post-incident activities:

**Vulnerability validation**

After a security incident, use AWS Security Agent to test whether similar vulnerabilities exist in other applications or environments.

**Security posture assessment**

Conduct penetration testing to validate security improvements implemented as part of incident remediation.

**Root cause analysis**

Use code security review capabilities to identify how similar vulnerabilities might exist in other codebases.
