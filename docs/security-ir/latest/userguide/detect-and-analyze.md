# Detect and Analyze

AWS Security Incident Response monitors, triages, investigates security findings from Amazon GuardDuty and integrations
through AWS Security Hub. Additional actions that can significantly enhance the scope and effectiveness of
AWS Security Incident Response's monitoring and investigation capabilities include:

**Enabling supported sources of detection**

###### Note

AWS Security Incident Response service costs do not include usage and other costs and fees associated with supported sources of detection
or use of other AWS services. Please refer to individual feature or service pages for cost details.

_Amazon GuardDuty_

GuardDuty is a threat detection service that continuously monitors, analyzes, and processes data sources
and logs in your AWS environment. Enabling GuardDuty is not required to use AWS Security Incident Response; however,
to use the proactive response and alert triaging feature Amazon GuardDuty must be enabled.

To enable GuardDuty across your organization, please see the `Setting up GuardDuty` section of the [Amazon GuardDuty User Guide](../../../guardduty/latest/ug/guardduty_settingup.md#guardduty_enable-gd "../../../guardduty/latest/ug/guardduty_settingup.md#guardduty_enable-gd").

We highly recommend that you enable GuardDuty in all supported AWS Regions. This enables GuardDuty to generate
findings about unauthorized or unusual activity even in regions that you are not actively using. For more information,
reference
[Amazon GuardDuty Regions and endpoints](../../../guardduty/latest/ug/guardduty_regions.md "../../../guardduty/latest/ug/guardduty_regions.md")

Enabling GuardDuty provides AWS Security Incident Response access to critical threat detection data, enhancing its ability to identify and
respond to potential security issues in your AWS environment.

_AWS Security Hub_

Security Hub can ingest security findings from several AWS services and supported third-party security solutions.
These integrations can help AWS Security Incident Response monitor and investigate findings coming from other detection tools.

To enable Security Hub with Organizations integration please refer to the
[AWS Security Hub User Guide](../../../securityhub/latest/userguide/securityhub-settingup.md#securityhub-orgs-setup-overviews "../../../securityhub/latest/userguide/securityhub-settingup.md#securityhub-orgs-setup-overviews").

There are multiple ways of enabling integrations on Security Hub. For third-party product integrations, you may need to purchase
the integration from the AWS Marketplace, and then configure the integration. The integration information provides links to complete
these tasks. Learn more about [how to enable AWS Security Hub integrations](../../../securityhub/latest/userguide/securityhub-integration-enable.md "../../../securityhub/latest/userguide/securityhub-integration-enable.md").

AWS Security Incident Response can monitor and investigate findings from the following tools when they're integrated with AWS Security Hub:

- [_CrowdStrike – CrowdStrike Falcon_](../../../securityhub/latest/userguide/securityhub-partner-providers.md#integration-crowdstrike-falcon "../../../securityhub/latest/userguide/securityhub-partner-providers.md#integration-crowdstrike-falcon")
- [_Lacework – Lacework_](../../../securityhub/latest/userguide/securityhub-partner-providers.md#integration-lacework "../../../securityhub/latest/userguide/securityhub-partner-providers.md#integration-lacework")
- [_Trend Micro – Cloud One_](../../../securityhub/latest/userguide/securityhub-partner-providers.md#integration-trend-micro "../../../securityhub/latest/userguide/securityhub-partner-providers.md#integration-trend-micro")

By enabling these integrations, you can significantly enhance the scope and effectiveness of AWS Security Incident Response's monitoring and investigation capabilities.

**Analyzing findings.**

AWS Security Incident Response automations and AWS CIRT service team will analyze all findings
from the supported tools. We will start learning about your environment by communicating with you using AWS Support Cases.
For example, when we need to understand whether a finding is expected behavior or should be escalated to an incident. As we
learn more from your environment, we will customize the service and to reduce the number of communications.

**Reporting an event.**

You can raise a security event through the AWS Security Incident Response service portal. It's important not to wait during a security event.
AWS Security Incident Response uses automated and manual techniques to investigate security events, analyze logs, and look for anomalous patterns.
Your partnership and understanding of your environment accelerates this analysis.

**Communicate.**

AWS Security Incident Response keeps you informed during the investigation by engaging your security contacts through the event case.
Multiple teammates may support your event, all using the event ticket for customer-provided content and AWS updates.

Communication may include automated notifications when a security alert is generated; communication during event analysis;
establishing call bridges; the ongoing analysis of artifacts such as log files; and getting
investigation results to you during the security event.

The service will create AWS Security Incident Response cases to communicate with your teams. We will create cases against your
membership account. This approach centralizes communication from all your accounts into a single place. The
"[Proactive case]" prefix helps identify cases initiated by AWS Security Incident Response.

By engaging actively with these communications and providing timely responses, you can help the AWS Security Incident Response service to:

- Better understand your environment and expected behaviors.
- Reduce false positives over time.
- Improve the accuracy and relevance of alerts.
- Ensure rapid response to genuine security incidents.
- Remember, the effectiveness of the AWS Security Incident Response service improves with your collaboration,
  leading to a more secure and efficiently monitored AWS environment.
