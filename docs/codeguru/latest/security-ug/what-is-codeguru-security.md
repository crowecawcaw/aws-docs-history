On November 20, 2025, AWS will discontinue support for Amazon CodeGuru Security. After
November 20, 2025, you will no longer be able to access the /codeguru/security console, service
resources, or documentation. For more information, see [End of support for CodeGuru Security](end-of-support.md "end-of-support.md").

# What is Amazon CodeGuru Security?

Amazon CodeGuru Security is a static application security tool that uses machine learning to detect
security policy violations and vulnerabilities. It provides suggestions for addressing security
risks and generates metrics so you can track the security posture of your applications.
CodeGuru Security’s policies, which are informed by years of Amazon.com and AWS security best practices,
help you to create and deploy secure, high-quality applications.

CodeGuru Security is currently supported in several
[AWS Regions](../../../general/latest/gr/codeguru-security.md "../../../general/latest/gr/codeguru-security.md").

## What kind of suggestions does CodeGuru Security provide?

CodeGuru Security identifies security vulnerabilities in your code and suggests remediations to
improve the security of your code base. Examples of security vulnerabilities it detects include
resource leaks, hardcoded credentials, and cross-site scripting. CodeGuru Security can also identify code
quality issues with some integrations. For more information on the types of analysis performed in code scans, see
[Types of code scans](scan-types.md "scan-types.md").

CodeGuru Security scans are powered by Amazon CodeGuru detectors that can identify a range of code
security and code quality issues. For information about these detectors, see the [Amazon CodeGuru Detector
Library](../../detector-library/index.md "../../detector-library/index.md").

## What languages does CodeGuru Security support?

CodeGuru Security supports the following language versions:

- **Java** ‐ Java 17 and earlier
- **JavaScript** ‐ ECMAScript 2021 and earlier
- **Python** ‐ Python 3.11 and earlier, within the Python
  3 series
- **C#** ‐ All versions (.Net 6.0 and later
  recommended)
- **TypeScript** ‐ All versions
- **Ruby** ‐ Ruby 2.7 and 3.2
- **Go** ‐ Go 1.18
- **C** ‐ C11 and earlier
- **C++** ‐ C++17 and earlier
- **PHP** ‐ PHP 8.2 and earlier
- **Kotlin** ‐ Kotlin 2.0.0 and earlier
- **Scala** ‐ Scala 3.2.2 and earlier
- **JSX** ‐ React 17 and earlier
- **Infrastructure as Code (IaC) languages**
  - **AWS CloudFormation** ‐ 2010-09-09
  - **Terraform** ‐ 1.6.2 and earlier
  - **AWS CDK** ‐ TypeScript and Python

CodeGuru Security supports the following languages for automatic code fixes:

- **Java** ‐ Java 17 and earlier
- **JavaScript** ‐ ECMAScript 2021 and earlier
- **Python** ‐ Python 3.11 and earlier, within the Python
  3 series
- **C#** ‐ All versions (.Net 6.0 and later
  recommended)
- **TypeScript** ‐ All versions
- **Infrastructure as Code (IaC) languages**
  - **AWS CloudFormation** ‐ 2010-09-09
  - **Terraform** ‐ 1.6.2 and earlier
  - **AWS CDK** ‐ TypeScript and Python

For a list of the file types supported for secrets detection, see [Supported file types for secrets detection](secrets-detection.md#secrets-detection-file-types "secrets-detection.md#secrets-detection-file-types").

## What IDEs does CodeGuru Security

support?

CodeGuru Security can be used in the following interactive development environments (IDEs). For
notebook IDEs, CodeGuru Security is available through the [Amazon CodeGuru extension](get-started-notebooks-tutorial.md "get-started-notebooks-tutorial.md") for code written in Python.

- Amazon SageMaker AI Studio
- JupyterLab

###### Note

To access security scanning features in Visual Studio Code and JetBrains IDEs, see [Scanning your code
with Amazon Q Developer.](../../../amazonq/latest/qdeveloper-ug/security-scans.md "../../../amazonq/latest/qdeveloper-ug/security-scans.md")

## What integrations does CodeGuru Security support?

CodeGuru Security supports integration with the following products and services:

- GitHub
- GitLab
- Bitbucket
- AWS CLI
- AWS CodePipeline

CodeGuru Security also supports the following services:

- AWS Lambda code scanning with Amazon Inspector. For more information, see
  [Scanning
  AWS Lambda functions with Amazon Inspector](../../../inspector/latest/user/scanning-lambda.md "../../../inspector/latest/user/scanning-lambda.md").

## How is CodeGuru Security different from CodeGuru Reviewer?

CodeGuru Security is a rearchitected and redesigned version of CodeGuru Reviewer. CodeGuru Security uses hundreds of
new security detectors to scan your code, in addition to the detectors that were developed for
CodeGuru Reviewer. CodeGuru Security also includes many additional features such as vulnerability tracking and a
metrics dashboard to help you monitor the security posture of your applications. For more
information, see [CodeGuru Security Features](codeguru-security-features.md "codeguru-security-features.md"). If you are
a CodeGuru Reviewer customer and want to access the most updated code scanning capabilities with new
detectors, enable code quality analysis in your scans. For more information, see [Types of code scans](scan-types.md "scan-types.md").

## How much does CodeGuru Security cost?

Currently, CodeGuru Security is in preview release and is free to use.

## How do I get started with CodeGuru Security?

Currently CodeGuru Security is available through the console, the AWS CLI and AWS SDKs, and through
several integrations. For more information, see [Getting started with CodeGuru Security](getting-started-with-codeguru-security.md "getting-started-with-codeguru-security.md").
