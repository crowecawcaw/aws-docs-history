On November 20, 2025, AWS will discontinue support for Amazon CodeGuru Security. After
November 20, 2025, you will no longer be able to access the /codeguru/security console, service
resources, or documentation. For more information, see [End of support for CodeGuru Security](end-of-support.md "end-of-support.md").

# Types of code scans

Amazon CodeGuru Security can perform code security analysis and code quality analysis in code scans.
All code scans perform code security analysis, where CodeGuru Security scans your code and returns
findings about detected security vulnerabilities and hardcoded secrets. You can also configure
your scans to include code quality analysis, which returns findings related to the quality of
your code in addition to security vulnerabilities.

Whereas security findings are used to generate finding and vulnerability resolution metrics
for your account, code quality findings do not affect the metrics in your dashboard data. Rather,
they are labeled as Informational findings that you can choose to address and will not affect how
the security posture of your application is assessed.

This section covers types of code analysis and how to enable them in your scans.

###### Topics

- [Code security analysis](#security-analysis "#security-analysis")
- [Code quality analysis](#quality-analysis "#quality-analysis")
- [Secrets detection](secrets-detection.md "secrets-detection.md")

## Code security analysis

Code security analysis detects potential security policy violations and vulnerabilities in
your code. Code security analysis is powered by Amazon CodeGuru detectors that are informed by
years of Amazon.com and AWS security best practices. Examples of security vulnerabilities
include resource leaks, hardcoded credentials, and cross-site scripting. To learn more about the
security vulnerabilities CodeGuru Security detects, see the [Amazon CodeGuru Detector
Library](../../detector-library/index.md "../../detector-library/index.md").

In addition to security vulnerabilities identified by CodeGuru detectors, security analysis
also includes scanning code and text files for hardcoded secrets. For more information, see
[Secrets detection](secrets-detection.md "secrets-detection.md").

All code scans include code security analysis. You do not need to take any action to enable
security analysis in your scans.

## Code quality analysis

Code quality analysis detects issues related to quality and maintainability in your code.
You can include code quality analysis in addition to security analysis in your scans to ensure
your code is meeting quality best practices. Code quality analysis returns findings with an
Informational severity level that do not impact the security assessment of your code base.

Code quality analysis is available for most, but not all, integrations. The following list
includes the services and integrations in which you can scan your code for both security and
quality findings:

- AWS CLI
- AWS SDKs
- GitHub
- Bitbucket
- GitLab
- AWS CodePipeline
- IDE plugins
- Amazon SageMaker AI Studio and JupyterLab notebooks

Scans created with the console and with Amazon Inspector Lambda code scanning only generate
findings related to security.

### Enable quality analysis

Scans created in IDE plugins and notebook integrations automatically perform both security
and quality analysis.

You can enable quality analysis in scans created with the AWS CLI, AWS SDKs, and the
supported integrations by specifying the analysis type when you create a scan. By default,
these scans only perform security analysis.

Specify `All` for the analysis type to perform both security and quality
analysis in your scans. Specify `Security` to only scan for security
vulnerabilities. For more information, see [CreateScan](../security-api/API_CreateScan.md "../security-api/API_CreateScan.md") in the CodeGuru Security API
Reference.

Choose from the list in the [Getting started with CodeGuru Security](getting-started-with-codeguru-security.md "getting-started-with-codeguru-security.md") section to learn how to configure code
scans to perform quality analysis wherever you are using CodeGuru Security.
