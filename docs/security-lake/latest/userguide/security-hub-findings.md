# Security Hub CSPM findings in Security Lake

Security Hub CSPM findings help you understand your security posture in AWS and let you check
your environment against security industry standards and best practices. Security Hub CSPM collects
findings from various sources, including integrations with other AWS services,
third-party product integrations, and checks against Security Hub CSPM controls. Security Hub CSPM processes
findings in a standard format called AWS Security Finding Format (ASFF).

When you add Security Hub CSPM findings as a source in Security Lake, Security Lake immediately starts collecting
your findings directly from Security Hub CSPM through an independent and duplicated stream of
events. Security Lake also transforms the findings from ASFF to the [Open Cybersecurity Schema Framework (OCSF) in Security Lake](open-cybersecurity-schema-framework.md "open-cybersecurity-schema-framework.md") (OCSF).

Security Lake doesn't manage your Security Hub CSPM findings or affect your Security Hub CSPM settings. To manage Security Hub CSPM
findings, you must use the Security Hub CSPM service console, API, or AWS CLI. For more information,
see [Findings in
AWS Security Hub CSPM](../../../securityhub/latest/userguide/securityhub-findings.md "../../../securityhub/latest/userguide/securityhub-findings.md") in the _AWS Security Hub User Guide_ .

The following list provides GitHub repository links to the mapping reference for how
Security Lake normalizes Security Hub CSPM findings to OCSF.

###### \*\*GitHub OCSF repository for Security Hub CSPM

findings\*\*

- Source version 1 [(v1.0.0-rc.2)](https://github.com/ocsf/examples/tree/main/mappings/markdown/AWS/v1.0.0-rc.2/Security%20Hub "https://github.com/ocsf/examples/tree/main/mappings/markdown/AWS/v1.0.0-rc.2/Security%20Hub")
- Source version 2 [(v1.1.0)](https://github.com/ocsf/examples/tree/main/mappings/markdown/AWS/v1.1.0/Security%20Hub "https://github.com/ocsf/examples/tree/main/mappings/markdown/AWS/v1.1.0/Security%20Hub")
