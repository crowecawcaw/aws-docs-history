# Best Practice 7.4 – Implement logging

and reporting for user access and authorization changes and events

User access and authorization events in your SAP systems should be logged, analyzed,
and audited regularly. Consolidate and correlate security events from your SAP applications
and database with other components of your architecture. This can allow for end-to-end
tracing in the event of a critical security problem or breach. Automate analysis of events
in a central Security Information and Event Management (SIEM) system. This can allow your
operations team to understand if any unexpected or suspicious activity occurs outside of the
bounds of normal system controls. They can then remediate as needed.

**Suggestion 7.4.1 – Log AWS Identity and Access Management (IAM)
events**

Consider keeping a historical log of AWS IAM events. This can be used in detection
or audit of user and authorization changes within AWS accounts. Determine your log
retention period and types of events to log based on your organizations required security
policies.

Enable your operations team to answer audit questions at the infrastructure level for
your SAP system:

- When and by whom was the new AWS console/CLI user created?
- When and by whom was the AWS IAM role modified?
- When did the AWS user last successfully sign in?
- Is there a suspicious number of failed sign-in attempts to the AWS
  account?
  For further information, consider the following:

- AWS Documentation: [IAM Best Practices: Monitor activity in your AWS account](../../../IAM/latest/UserGuide/best-practices.md#keep-a-log "../../../IAM/latest/UserGuide/best-practices.md#keep-a-log")
- AWS Documentation: [Logging IAM and AWS STS API
  calls with AWS CloudTrail](../../../IAM/latest/UserGuide/cloudtrail-integration.md "../../../IAM/latest/UserGuide/cloudtrail-integration.md")
- AWS Well-Architected Framework [Security]: [Detection](../framework/sec-detection.md "../framework/sec-detection.md")
- AWS Security Blog: [Visualizing Amazon GuardDuty
  findings](https://aws.amazon.com/blogs/security/visualizing-amazon-guardduty-findings/ "https://aws.amazon.com/blogs/security/visualizing-amazon-guardduty-findings/")
- AWS Security Blog:[Amazon GuardDuty Enhances Detection of EC2 Instance Credential Exfiltration](https://aws.amazon.com/blogs/aws/amazon-guardduty-enhances-detection-of-ec2-instance-credential-exfiltration/ "https://aws.amazon.com/blogs/aws/amazon-guardduty-enhances-detection-of-ec2-instance-credential-exfiltration/")

**Suggestion 7.4.2 – Log user and authorization changes in your
operating system**

Consider keeping a historical log of operating system (OS) user and authorization
events such that they can be used in detection or audit. Determine your log retention
period and types of events to log based on your organizations required security
policies.

Enable your operations team to answer audit questions at the operating system level
for your SAP system such as:

- When and by whom was the new superuser OS account created?
- When and by whom was the OS account permissions modified?
- When did the OS user last successfully sign in?
- Is there a suspicious number of failed sign-in attempts for the OS account?
- When did your OS user last use elevated permissions?
  For further information on auditing at the operating system consider:

| Operating System             | Guidance                                                                                                                                                                                                                                                                                                                                                                                              |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SUSE Linux Enterprise Server | [Setting Up the Linux Audit Framework                                                                                                                                                                                                                                                                                                                                                                 | Security Guide](https://documentation.suse.com/sles/12-SP4/html/SLES-all/cha-audit-setup.html "https://documentation.suse.com/sles/12-SP4/html/SLES-all/cha-audit-setup.html")                                                                                                                        |
| Red Hat Enterprise Linux     | [Chapter 14. Auditing the system Red Hat Enterprise Linux 8                                                                                                                                                                                                                                                                                                                                           | Security<br>Guide](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/security_hardening/auditing-the-system_security-hardening "https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/security_hardening/auditing-the-system_security-hardening") |
| Microsoft Windows            | [Windows Audit Policy Recommendations](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/audit-policy-recommendations "https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/audit-policy-recommendations")                                                                                                           |
| Oracle Enterprise Linux      | [Oracle Linux 8 Enhancing System Security<br>• Using System Auditing and Monitoring](https://docs.oracle.com/en/operating-systems/oracle-linux/8/security/security-ImplementingAdditionalSecurityFeaturesandBestPractices.html#ol-s4-syssec "https://docs.oracle.com/en/operating-systems/oracle-linux/8/security/security-ImplementingAdditionalSecurityFeaturesandBestPractices.html#ol-s4-syssec") |

**Suggestion 7.4.3 – Log SAP application and database user and
authorization events**

Consider keeping a historical log of SAP user and authorization events such that they
can be used in detection or audit. Consider both the application stack (for example, ABAP
authorizations) and your database (for example, SAP HANA). Determine your log retention
period and types of events to log based on your organizations required security
policies.

Enable your operations team to answer audit questions at the SAP application and
database level for events such as:

- When and by whom was the new SAP or database account created?
- When and by whom was the SAP or database account permissions modified?
- When did the SAP or database user last successfully sign in?
- Is there a suspicious number of failed sign-in attempts for the account?
- What sensitive transaction codes or tools did the account last use?
  For further information consider the following:

- SAP Documentation: [SAP Access Control
  and Governance | User Access](https://www.sap.com/australia/products/access-control.html "https://www.sap.com/australia/products/access-control.html")
- SAP Documentation: [SAP NetWeaver ABAP: The Security Audit Log](https://help.sap.com/viewer/280f016edb8049e998237fcbd80558e7/LATEST/en-US/4d41bec4aa601c86e10000000a42189b.html "https://help.sap.com/viewer/280f016edb8049e998237fcbd80558e7/LATEST/en-US/4d41bec4aa601c86e10000000a42189b.html")
- SAP Documentation: [SAP NetWeaver JAVA: The Security Audit Log](https://help.sap.com/viewer/56bf1265a92e4b4d9a72448c579887af/LATEST/en-US/c769bcb7f36611d3a6510000e835363f.html "https://help.sap.com/viewer/56bf1265a92e4b4d9a72448c579887af/LATEST/en-US/c769bcb7f36611d3a6510000e835363f.html")
- SAP Documentation: [SAP HANA: Auditing Activity in SAP HANA](https://help.sap.com/viewer/b3ee5778bc2e4a089d3299b82ec762a7/LATEST/en-US/ddcb6ed2bb5710148183db80e4aca49b.html "https://help.sap.com/viewer/b3ee5778bc2e4a089d3299b82ec762a7/LATEST/en-US/ddcb6ed2bb5710148183db80e4aca49b.html")

**Suggestion 7.4.4 – Consolidate user and authorization events in a
Security Information and Event Management (SIEM) system for analysis**

Consider sending all your user and authorization events from across your SAP workload
components into a central SIEM tool to allow correlation and analysis. Use tools like SAP
Enterprise Threat Detection, third-party add-ons or directly ship your SAP audit logs from
your application and database servers to an ingestion and analysis tool.

Establish baseline behaviors for your workload and monitor for abnormalities to
improve detection of security incidents.

Consider [AWS Marketplace
SIEM solutions](https://aws.amazon.com/marketplace/solutions/control-tower/siem/ "https://aws.amazon.com/marketplace/solutions/control-tower/siem/") to monitor your workload in real-time, identify security issues,
and expedite root-cause analysis and remediation.

For further information, consider the following resources:

- AWS Marketplace: [SIEM
  Solutions](https://aws.amazon.com/marketplace/solutions/control-tower/siem/ "https://aws.amazon.com/marketplace/solutions/control-tower/siem/")
- AWS Documentation: [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/?aws-security-hub-blogs.sort-by=item.additionalFields.createdDate&aws-security-hub-blogs.sort-order=desc "https://aws.amazon.com/security-hub/?aws-security-hub-blogs.sort-by=item.additionalFields.createdDate&aws-security-hub-blogs.sort-order=desc")
- SAP Documentation: [SAP Enterprise Threat Detection](https://help.sap.com/viewer/eb42e48f5e9c4c9ab58a7ad73ff3bc66/LATEST/en-US/e12aa17b106c4c6193b7d593328aad48.html "https://help.sap.com/viewer/eb42e48f5e9c4c9ab58a7ad73ff3bc66/LATEST/en-US/e12aa17b106c4c6193b7d593328aad48.html")
- Well-Architected Framework [Security]: [Security Incident Response](../framework/sec-incresp.md "../framework/sec-incresp.md")
- AWS Documentation: [AWS Security Incident Response - Technical Whitepaper](../../../whitepapers/latest/aws-security-incident-response-guide/welcome.md "../../../whitepapers/latest/aws-security-incident-response-guide/welcome.md")
