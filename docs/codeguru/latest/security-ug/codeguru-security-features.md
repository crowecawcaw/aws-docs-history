On November 20, 2025, AWS will discontinue support for Amazon CodeGuru Security. After
November 20, 2025, you will no longer be able to access the /codeguru/security console, service
resources, or documentation. For more information, see [End of support for CodeGuru Security](end-of-support.md "end-of-support.md").

# Features

This section outlines common features of Amazon CodeGuru Security and how they help mitigate security risk
in your applications.

**High precision vulnerability detection**

CodeGuru Security uses machine learning based on years of AWS and Amazon.com security best
practices to detect security vulnerabilities in your code with Amazon CodeGuru detectors. These detectors look for code
vulnerabilities like injection flaws, leaking data, weak cryptography, or missing encryption. As
we update our security policies and add new detectors, code scans automatically incorporate the
new policies. Detected vulnerabilities are returned as findings, which include details about the
security risk and how to remediate it.

**Automatic code fixes**

For certain vulnerabilities, CodeGuru Security uses generative AI to create plug-and-play code
blocks that can directly replace your vulnerable lines of code. You can download a code patch
from the console to apply to your file, or you can remove the vulnerable code and then paste
suggested code updates into your file. With Amazon Inspector Lambda code
scanning, you can apply code fixes that update your code in-place.

**Vulnerability tracking**

CodeGuru Security utilizes a machine learning based vulnerability tracking feature which tracks a
vulnerability even if it moves to a different location within a file or to another file. After a
vulnerability is initially detected, the vulnerability tracking feature can detect if it is still
present across subsequent scans, or if it has been remediated. When vulnerability tracking
detects that a vulnerability has been remediated, it automatically changes the status of the
finding to Closed. This status update is passed to any integrated notification system. No user
action is required.

**Secrets detection**

CodeGuru Security integrates with AWS Secrets Manager to use a secrets detector that finds unprotected secrets
in your code and text files, including hardcoded passwords, database connection strings, user
names, and more. Secrets detection is automatically enabled in scans, so you don't need to turn
it on. For more information, see [Secrets detection](secrets-detection.md "secrets-detection.md").

**Integrations**

In addition to running code scans directly in the console, you can integrate CodeGuru Security with
several other products and services. By integrating with your existing workflow, you can automate
vulnerability detection without disrupting your software development process. For a list of IDEs
and services you can use with CodeGuru Security, see [IDEs supported by
CodeGuru Security](what-is-codeguru-security.md#supported-IDEs "what-is-codeguru-security.md#supported-IDEs") and [Integrations supported by
CodeGuru Security](what-is-codeguru-security.md#supported-integrations "what-is-codeguru-security.md#supported-integrations"). For instructions on how to integrate with a service, see [Getting started with CodeGuru Security](getting-started-with-codeguru-security.md "getting-started-with-codeguru-security.md"), or go to the Integrations page in the
CodeGuru Security console.

**Metrics dashboard**

CodeGuru Security analyzes findings across your account and generates metrics that are presented in
a high-level dashboard. The dashboard displays data about your findings like the average time to
close findings, what types of vulnerabilities are present in your scans, and the severity
distribution of your findings. With the vulnerability tracking feature, the Metrics dashboard is
able to maintain an up-to-date representation of the security posture of your code
resources.

You can use these metrics to track the progress of your application security, identify
vulnerabilities during software development, and track the lifecycle of vulnerabilities. You can
also communicate the status of application security, and collaborate with other teams to address
security issues. For information about how these metrics are calculated and where to find them,
see [Understanding dashboard metrics](understanding-dashboard-metrics.md "understanding-dashboard-metrics.md").

**Security posture over time**

Findings metrics in the dashboard let you monitor progress toward remediation of findings
and view trends over time to see if SLAs for remediation are being met.

**Prioritization of security vulnerabilities**

Findings are categorized by severity, which lets you focus on the security vulnerabilities
that you want address first or where you want to concentrate your remediation efforts.

**Code quality scanning**

In addition to detecting security vulnerabilities in your code, you can enable code quality
scanning to maintain the quality of your codebase. For more information, see
[Types of code scans](scan-types.md "scan-types.md").

**Continually scan your environment for
vulnerabilities**

Enable automatic code scanning in your workflow to scan files as you develop your
applications and catch security vulnerabilities early in the development process.

**No machine learning expertise needed**

CodeGuru Security uses machine learning models that AWS manages to detect security vulnerabilities
in your code. These models make sure that your code abides by security policies, follows best
practices, and takes advantage of AWS code security expertise.

**Management of scans and findings in customizable
views**

In addition to the Dashboard, you can view the Scans page and Findings page in the console
for a list of all scans and findings in your account. The Scans page gives an overview of all
scans in an account. You can choose individual scans for information about the findings generated
by the scan. For more information, see [Working with code scans](working-with-code-scans.md "working-with-code-scans.md"). The Findings page lists findings based on a chosen
severity level. You can view individual findings for information about the security vulnerability
and suggested remediation. For more information, see [Working with findings](working-with-findings.md "working-with-findings.md").
