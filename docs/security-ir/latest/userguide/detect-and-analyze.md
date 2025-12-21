# Detect and Analyze

AWS Security Incident Response monitors, triages, investigates security findings from Amazon GuardDuty and integrations
through AWS Security Hub CSPM. Additional actions that can significantly enhance the scope and effectiveness of
AWS Security Incident Response's monitoring and investigation capabilities include: Reporting an event, Enabling supported sources of detection, and Communicating with Security Indcident Response engineers.

**Reporting an Event**

You can raise a security event through the AWS Security Incident Response service portal. It's important not to wait during a security event.
AWS Security Incident Response uses automated and manual techniques to investigate security events, analyze logs, and look for anomalous patterns.
Your partnership and understanding of your environment accelerates this analysis.

**Enabling supported sources of detection**

###### Note

AWS Security Incident Response service costs do not include usage and other costs and fees associated with supported sources of detection
or use of other AWS services. Please refer to individual feature or service pages for cost details.

_Amazon GuardDuty_

To enable GuardDuty across your organization, please see the `Setting up GuardDuty` section of the [Amazon GuardDuty User Guide](../../../guardduty/latest/ug/guardduty_settingup.md#guardduty_enable-gd "../../../guardduty/latest/ug/guardduty_settingup.md#guardduty_enable-gd").

We highly recommend that you enable GuardDuty in all supported AWS Regions. This enables GuardDuty to generate
findings about unauthorized or unusual activity even in regions that you are not actively using. For more information,
reference
[Amazon GuardDuty Regions and endpoints](../../../guardduty/latest/ug/guardduty_regions.md "../../../guardduty/latest/ug/guardduty_regions.md")

Enabling GuardDuty provides AWS Security Incident Response access to critical threat detection data, enhancing its ability to identify and
respond to potential security issues in your AWS environment.

_AWS Security Hub CSPM_

Security Hub CSPM can ingest security findings from several AWS services and supported third-party security solutions.
These integrations can help AWS Security Incident Response monitor and investigate findings coming from other detection tools.

To enable Security Hub CSPM with Organizations integration please refer to the
[AWS Security Hub CSPM User Guide](../../../securityhub/latest/userguide/securityhub-settingup.md#securityhub-orgs-setup-overviews "../../../securityhub/latest/userguide/securityhub-settingup.md#securityhub-orgs-setup-overviews").

There are multiple ways of enabling integrations on Security Hub CSPM. For third-party product integrations, you may need to purchase
the integration from the AWS Marketplace, and then configure the integration. The integration information provides links to complete
these tasks. Learn more about [how to enable AWS Security Hub CSPM integrations](../../../securityhub/latest/userguide/securityhub-integration-enable.md "../../../securityhub/latest/userguide/securityhub-integration-enable.md").

AWS Security Incident Response can monitor and investigate findings from the following tools when they're integrated with AWS Security Hub CSPM:

- [_CrowdStrike – CrowdStrike Falcon_](../../../securityhub/latest/userguide/securityhub-partner-providers.md#integration-crowdstrike-falcon "../../../securityhub/latest/userguide/securityhub-partner-providers.md#integration-crowdstrike-falcon")
- [_Lacework – Lacework_](../../../securityhub/latest/userguide/securityhub-partner-providers.md#integration-lacework "../../../securityhub/latest/userguide/securityhub-partner-providers.md#integration-lacework")
- [_Trend Micro – Cloud One_](../../../securityhub/latest/userguide/securityhub-partner-providers.md#integration-trend-micro "../../../securityhub/latest/userguide/securityhub-partner-providers.md#integration-trend-micro")

By enabling these integrations, you can significantly enhance the scope and effectiveness of AWS Security Incident Response's monitoring and investigation capabilities.

**Detection**

AWS Security Incident Response ingests findings from Amazon GuardDuty and AWS Security Hub CSPM through AWS EventBridge rules that are deployed to your accounts during Onboarding.

AWS Security Incident Response automatically archives Amazon GuardDuty findings that are determined during automated triage to be benign or associated with expected activity. You can view archived findings in the Amazon GuardDuty console by selecting Archived from the findings filter. For more information, see [Working with findings](../../../guardduty/latest/ug/guardduty_working-with-findings.md "../../../guardduty/latest/ug/guardduty_working-with-findings.md").

When AWS Security Hub CSPM ingests security findings, the system updates each finding with a note indicating that automated triage has begun. The workflow state changes from NEW to NOTIFIED, which removes the finding from the default AWS Security Hub CSPM findings view. If triage determines that a finding is benign or associated with expected activity, the system adds a note to the finding and updates the workflow state to SUPPRESSED.

**Analysis: Automated Triage**

AWS Security Incident Response automatically triages security findings. The triage process determines whether detected activity represents expected behavior by analyzing data from multiple sources, including the finding payload, AWS service metadata, AWS logging and monitoring data (such as AWS CloudTrail and VPC Flow Logs), AWS threat intelligence, and context that you are invited to provide about your AWS and on-premises environments.

If automated triage determines that the detected activity is expected, the system takes no further investigative action.

**Analysis: Incident Response Security Investigation**

Security Indcident Response engineers are a global, always-available team of security professionals with expertise in AWS and security incident response. If automated triage cannot determine that the activity is expected, Security Indcident Response engineers are engaged to perform a security investigation. If the event was ingested from Security Hub, a note is posted to the related finding stating that Security Indcident Response engineers' investigation is underway.

AWS Security Indcident Response engineers conduct a hands-on security investigation by analyzing additional service metadata and threat intelligence, reviewing insights from past findings and investigations in your environment, and applying incident response expertise. Depending on your Containment preferences (see Contain) Security Indcident Response engineers may engage your organization's Incident Response team through a AWS Security Incident Response case in the AWS Security Incident Response console to verify whether the detected activity is expected and authorized (see [Responding to an AWS generated case](responding-to-an-aws-generated-case.md "responding-to-an-aws-generated-case.md")).

**Communicate**

AWS Security Incident Response keeps you informed during security investigations by engaging with your Incident Response team through a AWS Security Incident Response case. Multiple Security Indcident Response engineers may support an investigation. Communication may include: acknowledgement or notification of the creation of a security investigation; establishing a call bridge; analysis of artifacts such as log files; requests for confirmation of expected activity; and sharing of investigation results.

When AWS Security Incident Response proactively engages your Incident Response team a case is created in your AWS Security Incident Response Membership account, which centralizes communication for all Organizational accounts in one place. These cases contain the "[Proactive case]" prefix in their title, which identifies them as initiated by AWS Security Incident Response. By actively engaging and providing timely responses to these communications, your Incident Response team can assist AWS Security Incident Response to:

- Ensure rapid response to genuine security incidents.
- Understand your environment and expected behaviors.
- Reduce false positive detections over time.

The effectiveness of AWS Security Incident Response improves with your collaboration and results in a more effectively monitored and secure AWS environment.

**Service Tuning**

When your account service quotas permit, AWS Security Incident Response attempts to deploy an Amazon GuardDuty suppression rule ([suppression rules](../../../guardduty/latest/ug/findings_suppression-rule.md "../../../guardduty/latest/ug/findings_suppression-rule.md")) or an AWS Security Hub CSPM automation rule ([automation rules](../../../securityhub/latest/userguide/automation-rules.md "../../../securityhub/latest/userguide/automation-rules.md")). These rules suppress future findings matching the type and source (for example, source IP address, ASN, identity principal, or resource) of known authorized activity. AWS Security Hub CSPM rules are deployed with priority 10, which allows you to override these automations with self-defined rules if needed.

In this way, AWS Security Incident Response tunes detection sources based on expected behavior in your AWS environment. Your Incident Response Team is notified of modifications to these rule-sets, and changes are rolled-back upon request.
