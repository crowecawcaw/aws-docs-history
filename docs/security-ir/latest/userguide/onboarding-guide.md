# Onboarding guide

The AWS onboarding guide walks you through prerequisites and AWS Security Incident Response onboarding and containment actions.

###### Important

Prerequisites

1. The only deployment prerequisite is enabling [AWS Organizations](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md")
2. While not required, we recommend enabling [Amazon GuardDuty](../../../guardduty/latest/ug/what-is-guardduty.md "../../../guardduty/latest/ug/what-is-guardduty.md") and [AWS Security Hub CSPM](../../../securityhub/latest/userguide/what-are-securityhub-services.md "../../../securityhub/latest/userguide/what-are-securityhub-services.md")across all accounts and active regions to maximize
   Security Incident Response benefits.
3. Review GuardDuty and Security Incident Response
4. Review [GuardDuty
   best practices guide](../../../guardduty/latest/ug/what-is-guardduty.md "../../../guardduty/latest/ug/what-is-guardduty.md")
   AWS Security Hub CSPM ingests findings from 3rd party endpoint detection and
   response (EDR) vendors (CrowdStrike, FortinetCNAPP (Lacework) and Trend Micro, among
   others. If these findings are ingested into Security Hub CSPM, they will be auto-triaged
   by Security Incident Response for proactive case creation as well. To setup 3rd party
   EDR with Security Hub CSPM, follow our [Detection and Analysis service documentation](detect-and-analyze.md "detect-and-analyze.md")

To setup 3rd party EDR with Security Hub CSPM:

1. Navigate to the Security Hub CSPM Integrations page to validate the 3rd party integration
   exists
2. From the console, navigate to the Security Hub CSPM service page.
3. Choose **Integrations** (using Wiz.IO as an
   example):

![](images/Security_Hub_CSPM.png) 4. Search for the vendor you would like to integrate

![](images/Integrations.png)

###### Note

When prompted, provide your account or subscription information. After you provide this information, Security Incident Response
ingests 3rd party findings. To review pricing for the 3rd party findings ingestion, see the **Integrations** page in Security Hub CSPM.
