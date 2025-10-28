On November 20, 2025, AWS will discontinue support for Amazon CodeGuru Security. After
November 20, 2025, you will no longer be able to access the /codeguru/security console, service
resources, or documentation. For more information, see [End of support for CodeGuru Security](end-of-support.md "end-of-support.md").

# Working with findings

In CodeGuru Security, a finding is a potential security vulnerability in your code. Findings include
information about the vulnerability that was detected in a code scan, an explanation of the issue,
the suggested remediation, and the suggested code fix or inline code update to remediate the
vulnerability.

You address findings by updating your code based on the suggested remediation. After you make
the changes, you re-run the scan on the revised code resource to see if the vulnerability has been
remediated and to close the finding. By re-scanning updated code resources, you can track findings
across multiple revisions of the same file.

This section covers viewing and addressing findings.

###### Topics

- [View all findings](view-all-findings.md "view-all-findings.md")
- [View finding details](view-finding-details.md "view-finding-details.md")
- [Finding severity](finding-severity.md "finding-severity.md")
- [Address findings](address-findings.md "address-findings.md")
