On November 20, 2025, AWS will discontinue support for Amazon CodeGuru Security. After
November 20, 2025, you will no longer be able to access the /codeguru/security console, service
resources, or documentation. For more information, see [End of support for CodeGuru Security](end-of-support.md "end-of-support.md").

# Integrate with IDE plugins

You can scan code in your IDE with Amazon Q security scans. To set up Amazon Q in your IDE, see
[Install
Amazon Q](../../../amazonq/latest/qdeveloper-ug/q-in-IDE-setup.md "../../../amazonq/latest/qdeveloper-ug/q-in-IDE-setup.md") in the _Amazon Q Developer
User Guide_.

To learn how to scan your code with Amazon Q, see [Security scans](../../../amazonq/latest/qdeveloper-ug/security-scans.md "../../../amazonq/latest/qdeveloper-ug/security-scans.md") in the
_Amazon Q Developer User Guide_. After scanning your code, you can view findings in the **Problems** tab in VS Code or the **Amazon Q Security
Issues** tab in JetBrains.

To view information about the finding and how to remediate
it, hold your cursor over the underlined code. To address findings, update your code based on the suggested remediation and then run
another scan to check that the vulnerabilities were remediated. For some vulnerabilities, you can
apply code fixes that update your code in-place.
