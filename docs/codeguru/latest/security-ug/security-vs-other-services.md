On November 20, 2025, AWS will discontinue support for Amazon CodeGuru Security. After
November 20, 2025, you will no longer be able to access the /codeguru/security console, service
resources, or documentation. For more information, see [End of support for CodeGuru Security](end-of-support.md "end-of-support.md").

# How is CodeGuru Security different than other AWS security

services?

Amazon CodeGuru Security, which identifies security vulnerabilities in your application resources, adds
to the AWS collection of security services.

- [Amazon Inspector](../../../inspector/latest/user/what-is-inspector.md "../../../inspector/latest/user/what-is-inspector.md") is a vulnerability management service that continuously scans your AWS
  workloads for software vulnerabilities and unintended network exposure. You can run scans on
  your AWS Lambda functions that are powered by CodeGuru Security.
- [Amazon GuardDuty](../../../guardduty/latest/ug/what-is-guardduty.md "../../../guardduty/latest/ug/what-is-guardduty.md") monitors network traffic for threat patterns such as unusual data access in
  Amazon Simple Storage Service or API calls from known malicious IP addresses.
- [Amazon Macie](../../../macie/latest/user/what-is-macie.md "../../../macie/latest/user/what-is-macie.md") scans data storage locations for unencrypted data such as personally
  identifiable information (PII) and financial data.
- [AWS Security Hub](../../../securityhub/latest/userguide/what-is-securityhub.md "../../../securityhub/latest/userguide/what-is-securityhub.md") collects security data from across AWS accounts, services, and supported
  third-party products and helps you analyze your security trends and identify the highest
  priority security issues.
- [Amazon CodeGuru Reviewer](../reviewer-ug/welcome.md "../reviewer-ug/welcome.md")
  scans your code repositories for code defects related to quality, maintainability, and
  security and provides recommendations for how to address them. CodeGuru Security is a
  rearchitected and redesigned version of CodeGuru Reviewer. CodeGuru Security uses hundreds of
  new security detectors to scan your code, in addition to the detectors that were developed for
  CodeGuru Reviewer.
