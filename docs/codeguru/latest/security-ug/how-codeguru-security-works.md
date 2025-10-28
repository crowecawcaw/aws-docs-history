On November 20, 2025, AWS will discontinue support for Amazon CodeGuru Security. After
November 20, 2025, you will no longer be able to access the /codeguru/security console, service
resources, or documentation. For more information, see [End of support for CodeGuru Security](end-of-support.md "end-of-support.md").

# How CodeGuru Security works

Amazon CodeGuru Security scans your applications, detects security vulnerabilities, and provides
suggestions for how to remediate them in your code. After updating your code, you rerun the scan
to make sure the security vulnerability has been remediated and to close the finding. By revising
code and re-running scans, you generate security metrics you can track to continuously improve the
security posture of your applications.

**Scans**

Code scans are powered by detectors in the Amazon CodeGuru Detector Library. Each detector
corresponds to a type of code defect and can detect a range of issues related to a defect. For
more information, visit the [Amazon CodeGuru Detector
Library](../../detector-library/index.md "../../detector-library/index.md").

You can run code scans directly in the CodeGuru Security console, use the AWS CLI, use AWS SDKs, or
integrate with another service to detect security issues where you build your applications. For
instructions on how to integrate CodeGuru Security with other services, see [Getting started with CodeGuru Security](getting-started-with-codeguru-security.md "getting-started-with-codeguru-security.md").

**Findings**

When CodeGuru Security detects security vulnerabilities, it returns findings, which include
information about security issues in your code, where they are, and suggestions for how to
remediate them. If the suggested remediation includes a change to your code, CodeGuru Security highlights
the vulnerable lines of code to remove and suggests inline code fixes as replacements. For more
information, see [Working with findings](working-with-findings.md "working-with-findings.md").

**Metrics**

The CodeGuru Security Dashboard provides metrics to track the security posture of your application,
including open critical findings, the severity distribution of findings, and an assessment of what
vulnerabilities are most common. CodeGuru Security tracks the vulnerabilities and trends across multiple
revisions of the same code resources using the scan name you provide when a scan is created. For
more information, see [Understanding dashboard metrics](understanding-dashboard-metrics.md "understanding-dashboard-metrics.md").

You can also choose individual scans in the console to view security data. This includes the
number of open and closed findings and an assessment of what vulnerabilities appear in a
particular scan. For more information about scans, see [Working with code scans](working-with-code-scans.md "working-with-code-scans.md").
