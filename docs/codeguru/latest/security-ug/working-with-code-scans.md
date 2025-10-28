On November 20, 2025, AWS will discontinue support for Amazon CodeGuru Security. After
November 20, 2025, you will no longer be able to access the /codeguru/security console, service
resources, or documentation. For more information, see [End of support for CodeGuru Security](end-of-support.md "end-of-support.md").

# Working with code scans

In CodeGuru Security, a scan is an analysis of a code resource for potential security policy
violations and vulnerabilities. When you create a code scan, CodeGuru Security analyzes your code and
generates findings with information about security vulnerabilities and how to remediate them.

Before scanning your code, CodeGuru Security filters out unsupported code languages, test code, and
any open source or third-party code that is present in your code resource. This ensures that
findings are only generated on code that is relevant and that you own. The amount of code that can
be scanned per scan is limited, and varies by programming language. For information on code scan
limits, see [Quotas for Amazon CodeGuru Security](quotas.md "quotas.md").

You can monitor the security posture of your code over time by choosing a scan in the console
and viewing the data in the Metrics panel. For more information, see [View code scan details](view-code-scan-details.md "view-code-scan-details.md").

You can create code scans in the CodeGuru Security console, with the AWS CLI and AWS SDKs, or through
integrations with CodeGuru Security. Before you begin scanning, make sure you’ve completed the steps in
[Setting up Amazon CodeGuru Security](setting-up-codeguru-security.md "setting-up-codeguru-security.md") and
[Getting started with CodeGuru Security](getting-started-with-codeguru-security.md "getting-started-with-codeguru-security.md").

This section covers creating, configuring, viewing, and understanding code scans.

###### Topics

- [Types of code scans](scan-types.md "scan-types.md")
- [Create code scans](create-code-scans.md "create-code-scans.md")
- [Tag code scans](tag-code-scans.md "tag-code-scans.md")
- [View all code scans](view-all-code-scans.md "view-all-code-scans.md")
- [View code scan details](view-code-scan-details.md "view-code-scan-details.md")
