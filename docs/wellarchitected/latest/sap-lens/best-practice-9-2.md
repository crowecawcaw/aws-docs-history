# Best Practice 9.2 – Perform periodic

tests for security bugs

As described in the Well-Architected Framework Security Pillar incident response
sections on simulations, assembling a runbook and conducting game days are recommended for all
workloads, including those for SAP on AWS. This type of periodic testing can identify
new attack vectors and vulnerabilities as well as prepare your SAP security resources for
a rapid and effective response in the event of a security incident.

Well-Architected Framework [Security]: [Incident Response – Simulation](../security-pillar/simulate.md "../security-pillar/simulate.md")

**Suggestion 9.2.1 – Include SAP applications as targets in addition
to standard security and penetration testing**

Probative security testing is an important part of maintaining a secure environment.
In addition to conducting standard penetration testing in AWS, make sure to include your
SAP solution as an additional potential target for malicious activities. Keep in mind
SAP-specific software solutions that often are publicly exposed in your architecture such
as SAProuter, Web Dispatcher, Cloud Connector, and SAP Fiori.

- AWS Documentation: [Penetration
  Testing](https://aws.amazon.com/security/penetration-testing/ "https://aws.amazon.com/security/penetration-testing/")
