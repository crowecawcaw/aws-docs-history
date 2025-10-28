# Use `RefreshTrustedAdvisorCheck` with a CLI

The following code examples show how to use `RefreshTrustedAdvisorCheck`.

CLI

**AWS CLI**

**To refresh an AWS Trusted Advisor check**

The following `refresh-trusted-advisor-check` example refreshes the Amazon S3 Bucket Permissions Trusted Advisor check in your AWS account.

```
`aws support refresh-trusted-advisor-check \
 --check-id `"Pfx0RwqBli"``

```

Output:

```
{
    "status": {
        "checkId": "Pfx0RwqBli",
        "status": "enqueued",
        "millisUntilNextRefreshable": 3599992
    }
}
```

For more information, see [AWS Trusted Advisor](trusted-advisor.md "trusted-advisor.md") in the _AWS Support User Guide_.

- For API details, see
  [RefreshTrustedAdvisorCheck](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/refresh-trusted-advisor-check.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/refresh-trusted-advisor-check.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: Requests a refresh for the specified Trusted Advisor check.**

```
Request-ASATrustedAdvisorCheckRefresh -CheckId "checkid1"

```

- For API details, see
  [RefreshTrustedAdvisorCheck](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: Requests a refresh for the specified Trusted Advisor check.**

```
Request-ASATrustedAdvisorCheckRefresh -CheckId "checkid1"

```

- For API details, see
  [RefreshTrustedAdvisorCheck](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using AWS Support with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
