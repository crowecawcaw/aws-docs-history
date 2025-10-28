# Onboarding Guide

The AWS onboarding guide will walk you through prerequisites, security incident response onboarding and CIRT containment actions to perform threat containment actions during onboarding.

###### Important

Prerequisites

1. The only deployment prerequisite is enabling [AWS Organizations](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md")
2. While not required, we recommend enabling [Amazon
   GuardDuty](../../../guardduty/latest/ug/what-is-guardduty.md "../../../guardduty/latest/ug/what-is-guardduty.md") and [AWS Security Hub CSPM](../../../securityhub/latest/userguide/what-are-securityhub-services.md "../../../securityhub/latest/userguide/what-are-securityhub-services.md") across all accounts and active regions to maximize
   Security Incident Response benefits.
3. Review [GuardDuty and Security Incident Response](../../../securityincidentresponse/latest/userguide/guardduty-integration.md "../../../securityincidentresponse/latest/userguide/guardduty-integration.md")
4. Review [GuardDuty
   best practices guide](../../../guardduty/latest/ug/what-is-guardduty.md "../../../guardduty/latest/ug/what-is-guardduty.md")
   Security Hub CSPM will ingest findings from 3rd party endpoint detection and response
   (EDR) vendors (CrowdStrike, FortinetCNAPP (Lacework) and Trend Micro. If these findings are
   ingested into Security Hub CSPM, they will be auto-triaged by Security Incident Response for
   proactive case creation as well. To setup 3rd party EDR with Security Hub CSPM, follow our
   [Detection and Analysis service documentation](detect-and-analyze.md "detect-and-analyze.md") steps.

###### Note

The specific steps may vary depending on the AWS service and the actions you're trying to perform.
