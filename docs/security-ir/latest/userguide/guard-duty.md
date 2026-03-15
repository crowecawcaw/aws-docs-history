# GuardDuty findings and suppression rules

AWS Security Incident Response proactively ingests, triages, and responds to all Amazon GuardDuty findings and AWS Security Hub CSPM findings from CrowdStrike, FortinetCNAPP (Lacework), and Trend Micro. Our auto-triage technology eliminates internal analysis requirements. The service creates suppression and auto-archive rules in GuardDuty and Security Hub CSPM for benign findings. View or modify these rules under "Findings" in the Amazon GuardDuty console.

To review enabled GuardDuty Suppression Rules, complete the following steps:

1. Open the Amazon GuardDuty console.
2. Choose **Findings**.
3. In the navigation pane, choose **Suppression rules**. The **Suppression rules** page displays a list of all the suppression rules for your account.
4. To review or change the settings for a rule, choose the rule, and then choose **Update suppression rule** from the **Actions** menu.

###### Note

Organizations using SIEM technology have significantly reduced GuardDuty finding volumes over time, improving both Security Incident Response service and SIEM efficiency.
