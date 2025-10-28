# Use `DescribeTrustedAdvisorChecks` with a CLI

The following code examples show how to use `DescribeTrustedAdvisorChecks`.

CLI

**AWS CLI**

**To list the available AWS Trusted Advisor checks**

The following `describe-trusted-advisor-checks` example lists the available Trusted Advisor checks in your AWS account. This information includes the check name, ID, description, category, and metadata. Note that the output is shortened for readability.

```
`aws support describe-trusted-advisor-checks \
 --language `"en"``

```

Output:

```
{
    "checks": [
        {
            "id": "zXCkfM1nI3",
            "name": "IAM Use",
            "description": "Checks for your use of AWS Identity and Access Management (IAM). You can use IAM to create users, groups, and roles in AWS, and you can use permissions to control access to AWS resources. \n<br>\n<br>\n<b>Alert Criteria</b><br>\nYellow: No IAM users have been created for this account.\n<br>\n<br>\n<b>Recommended Action</b><br>\nCreate one or more IAM users and groups in your account. You can then create additional users whose permissions are limited to perform specific tasks in your AWS environment. For more information, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/IAMGettingStarted.html\" target=\"_blank\">Getting Started</a>. \n<br><br>\n<b>Additional Resources</b><br>\n<a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/IAM_Introduction.html\" target=\"_blank\">What Is IAM?</a>",
            "category": "security",
            "metadata": []
        }
    ]
}
```

For more information, see [AWS Trusted Advisor](trusted-advisor.md "trusted-advisor.md") in the _AWS Support User Guide_.

- For API details, see
  [DescribeTrustedAdvisorChecks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/describe-trusted-advisor-checks.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/describe-trusted-advisor-checks.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: Returns the collection of Trusted Advisor checks. You must specify the Language parameter which can accept either "en" for English output or "ja" for Japanese output.**

```
Get-ASATrustedAdvisorCheck -Language "en"

```

- For API details, see
  [DescribeTrustedAdvisorChecks](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: Returns the collection of Trusted Advisor checks. You must specify the Language parameter which can accept either "en" for English output or "ja" for Japanese output.**

```
Get-ASATrustedAdvisorCheck -Language "en"

```

- For API details, see
  [DescribeTrustedAdvisorChecks](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using AWS Support with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
