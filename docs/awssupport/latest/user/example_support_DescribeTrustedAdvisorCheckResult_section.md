# Use `DescribeTrustedAdvisorCheckResult` with a CLI

The following code examples show how to use `DescribeTrustedAdvisorCheckResult`.

CLI

**AWS CLI**

**To list the results of an AWS Trusted Advisor check**

The following `describe-trusted-advisor-check-result` example lists the results of the IAM Use check.

```
`aws support describe-trusted-advisor-check-result \
 --check-id `"zXCkfM1nI3"``

```

Output:

```
{
    "result": {
        "checkId": "zXCkfM1nI3",
        "timestamp": "2020-05-13T21:38:05Z",
        "status": "ok",
        "resourcesSummary": {
            "resourcesProcessed": 1,
            "resourcesFlagged": 0,
            "resourcesIgnored": 0,
            "resourcesSuppressed": 0
        },
        "categorySpecificSummary": {
            "costOptimizing": {
                "estimatedMonthlySavings": 0.0,
                "estimatedPercentMonthlySavings": 0.0
            }
        },
        "flaggedResources": [
            {
                "status": "ok",
                "resourceId": "47DEQpj8HBSa-_TImW-5JCeuQeRkm5NMpJWZEXAMPLE",
                "isSuppressed": false
            }
        ]
    }
}
```

For more information, see [AWS Trusted Advisor](trusted-advisor.md "trusted-advisor.md") in the _AWS Support User Guide_.

- For API details, see
  [DescribeTrustedAdvisorCheckResult](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/describe-trusted-advisor-check-result.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/describe-trusted-advisor-check-result.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: Returns the results of a Trusted Advisor check. The list of available Trusted Advisor checks can be obtained using Get-ASATrustedAdvisorChecks. The output is the overall status of the check, the timestamp at which the check was last run and the unique checkid for the specific check. To have the results output in Japanese, add the -Language "ja" parameter.**

```
Get-ASATrustedAdvisorCheckResult -CheckId "checkid1"

```

- For API details, see
  [DescribeTrustedAdvisorCheckResult](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: Returns the results of a Trusted Advisor check. The list of available Trusted Advisor checks can be obtained using Get-ASATrustedAdvisorChecks. The output is the overall status of the check, the timestamp at which the check was last run and the unique checkid for the specific check. To have the results output in Japanese, add the -Language "ja" parameter.**

```
Get-ASATrustedAdvisorCheckResult -CheckId "checkid1"

```

- For API details, see
  [DescribeTrustedAdvisorCheckResult](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using AWS Support with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
