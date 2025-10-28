# Use `DescribeComplianceByConfigRule` with a CLI

The following code examples show how to use `DescribeComplianceByConfigRule`.

CLI

**AWS CLI**

**To get compliance information for your AWS Config rules**

The following command returns compliance information for each AWS Config rule that is violated by one or more AWS resources:

```
`aws configservice describe-compliance-by-config-rule --compliance-types `NON_COMPLIANT``

```

In the output, the value for each `CappedCount` attribute indicates how many resources do not comply with the related rule. For example, the following output indicates that 3 resources do not comply with the rule named `InstanceTypesAreT2micro`.

Output:

```
{
    "ComplianceByConfigRules": [
        {
            "Compliance": {
                "ComplianceContributorCount": {
                    "CappedCount": 3,
                    "CapExceeded": false
                },
                "ComplianceType": "NON_COMPLIANT"
            },
            "ConfigRuleName": "InstanceTypesAreT2micro"
        },
        {
            "Compliance": {
                "ComplianceContributorCount": {
                    "CappedCount": 10,
                    "CapExceeded": false
                },
                "ComplianceType": "NON_COMPLIANT"
            },
            "ConfigRuleName": "RequiredTagsForVolumes"
        }
    ]
}
```

- For API details, see
  [DescribeComplianceByConfigRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-compliance-by-config-rule.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-compliance-by-config-rule.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example retrieves compliances details for the rule ebs-optimized-instance, for which there is no current evaluation results for the rule, hence it returns INSUFFICIENT_DATA**

```
(Get-CFGComplianceByConfigRule -ConfigRuleName ebs-optimized-instance).Compliance

```

**Output:**

```
ComplianceContributorCount ComplianceType
-------------------------- --------------
                           INSUFFICIENT_DATA
```

**Example 2: This example returns the number of non-compliant resources for the rule ALB_HTTP_TO_HTTPS_REDIRECTION_CHECK.**

```
(Get-CFGComplianceByConfigRule -ConfigRuleName ALB_HTTP_TO_HTTPS_REDIRECTION_CHECK -ComplianceType NON_COMPLIANT).Compliance.ComplianceContributorCount

```

**Output:**

```
CapExceeded CappedCount
----------- -----------
False       2
```

- For API details, see
  [DescribeComplianceByConfigRule](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example retrieves compliances details for the rule ebs-optimized-instance, for which there is no current evaluation results for the rule, hence it returns INSUFFICIENT_DATA**

```
(Get-CFGComplianceByConfigRule -ConfigRuleName ebs-optimized-instance).Compliance

```

**Output:**

```
ComplianceContributorCount ComplianceType
-------------------------- --------------
                           INSUFFICIENT_DATA
```

**Example 2: This example returns the number of non-compliant resources for the rule ALB_HTTP_TO_HTTPS_REDIRECTION_CHECK.**

```
(Get-CFGComplianceByConfigRule -ConfigRuleName ALB_HTTP_TO_HTTPS_REDIRECTION_CHECK -ComplianceType NON_COMPLIANT).Compliance.ComplianceContributorCount

```

**Output:**

```
CapExceeded CappedCount
----------- -----------
False       2
```

- For API details, see
  [DescribeComplianceByConfigRule](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using AWS Config with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
