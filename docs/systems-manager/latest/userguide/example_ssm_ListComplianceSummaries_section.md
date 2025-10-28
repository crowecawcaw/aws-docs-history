# Use `ListComplianceSummaries` with a CLI

The following code examples show how to use `ListComplianceSummaries`.

CLI

**AWS CLI**

**To list compliance summaries for all compliance types**

This example lists compliance summaries for all compliance types in your account.

Command:

```
`aws ssm list-compliance-summaries`

```

Output:

```
{
  "ComplianceSummaryItems": [
      {
          "ComplianceType": "Association",
          "CompliantSummary": {
              "CompliantCount": 2,
              "SeveritySummary": {
                  "CriticalCount": 0,
                  "HighCount": 0,
                  "MediumCount": 0,
                  "LowCount": 0,
                  "InformationalCount": 0,
                  "UnspecifiedCount": 2
              }
          },
          "NonCompliantSummary": {
              "NonCompliantCount": 0,
              "SeveritySummary": {
                  "CriticalCount": 0,
                  "HighCount": 0,
                  "MediumCount": 0,
                  "LowCount": 0,
                  "InformationalCount": 0,
                  "UnspecifiedCount": 0
              }
          }
      },
      {
          "ComplianceType": "Patch",
          "CompliantSummary": {
              "CompliantCount": 1,
              "SeveritySummary": {
                  "CriticalCount": 0,
                  "HighCount": 0,
                  "MediumCount": 0,
                  "LowCount": 0,
                  "InformationalCount": 0,
                  "UnspecifiedCount": 1
              }
          },
          "NonCompliantSummary": {
              "NonCompliantCount": 1,
              "SeveritySummary": {
                  "CriticalCount": 1,
                  "HighCount": 0,
                  "MediumCount": 0,
                  "LowCount": 0,
                  "InformationalCount": 0,
                  "UnspecifiedCount": 0
              }
          }
      },
              ...
  ],
  "NextToken": "eyJOZXh0VG9rZW4iOiBudWxsLCAiYm90b190cnVuY2F0ZV9hbW91bnQiOiAyfQ=="
}
```

**To list compliance summaries for a specific compliance type**

This example lists the compliance summary for the Patch compliance type.

Command:

```
`aws ssm list-compliance-summaries --filters `"Key=ComplianceType,Values=Patch,Type=EQUAL"``

```

- For API details, see
  [ListComplianceSummaries](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-compliance-summaries.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-compliance-summaries.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example returns a summary count of compliant and non-compliant resources for all compliance types.**

```
Get-SSMComplianceSummaryList

```

**Output:**

```
ComplianceType CompliantSummary                                      NonCompliantSummary
-------------- ----------------                                      -------------------
FleetTotal     Amazon.SimpleSystemsManagement.Model.CompliantSummary Amazon.SimpleSystemsManagement.Model.NonCompliantSummary
Association    Amazon.SimpleSystemsManagement.Model.CompliantSummary Amazon.SimpleSystemsManagement.Model.NonCompliantSummary
Custom:InSpec  Amazon.SimpleSystemsManagement.Model.CompliantSummary Amazon.SimpleSystemsManagement.Model.NonCompliantSummary
Patch          Amazon.SimpleSystemsManagement.Model.CompliantSummary Amazon.SimpleSystemsManagement.Model.NonCompliantSummary
```

- For API details, see
  [ListComplianceSummaries](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example returns a summary count of compliant and non-compliant resources for all compliance types.**

```
Get-SSMComplianceSummaryList

```

**Output:**

```
ComplianceType CompliantSummary                                      NonCompliantSummary
-------------- ----------------                                      -------------------
FleetTotal     Amazon.SimpleSystemsManagement.Model.CompliantSummary Amazon.SimpleSystemsManagement.Model.NonCompliantSummary
Association    Amazon.SimpleSystemsManagement.Model.CompliantSummary Amazon.SimpleSystemsManagement.Model.NonCompliantSummary
Custom:InSpec  Amazon.SimpleSystemsManagement.Model.CompliantSummary Amazon.SimpleSystemsManagement.Model.NonCompliantSummary
Patch          Amazon.SimpleSystemsManagement.Model.CompliantSummary Amazon.SimpleSystemsManagement.Model.NonCompliantSummary
```

- For API details, see
  [ListComplianceSummaries](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
