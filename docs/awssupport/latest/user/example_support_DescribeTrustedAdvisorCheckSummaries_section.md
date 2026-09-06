

# Use `DescribeTrustedAdvisorCheckSummaries` with a CLI
<a name="example_support_DescribeTrustedAdvisorCheckSummaries_section"></a>

The following code examples show how to use `DescribeTrustedAdvisorCheckSummaries`.

------
#### [ CLI ]

**AWS CLI**  
**To list the summaries of AWS Trusted Advisor checks**  
The following `describe-trusted-advisor-check-summaries` example lists the results for two Trusted Advisor checks: Amazon S3 Bucket Permissions and IAM Use.  

```
aws support describe-trusted-advisor-check-summaries \
    --check-ids {{"Pfx0RwqBli"}} {{"zXCkfM1nI3"}}
```
Output:  

```
{
    "summaries": [
        {
            "checkId": "Pfx0RwqBli",
            "timestamp": "2020-05-13T21:38:12Z",
            "status": "ok",
            "hasFlaggedResources": true,
            "resourcesSummary": {
                "resourcesProcessed": 44,
                "resourcesFlagged": 0,
                "resourcesIgnored": 0,
                "resourcesSuppressed": 0
            },
            "categorySpecificSummary": {
                "costOptimizing": {
                    "estimatedMonthlySavings": 0.0,
                    "estimatedPercentMonthlySavings": 0.0
                }
            }
        },
        {
            "checkId": "zXCkfM1nI3",
            "timestamp": "2020-05-13T21:38:05Z",
            "status": "ok",
            "hasFlaggedResources": true,
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
            }
        }
    ]
}
```
For more information, see [AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html) in the *AWS Support User Guide*.  
+  For API details, see [DescribeTrustedAdvisorCheckSummaries](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/describe-trusted-advisor-check-summaries.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: Returns the latest summary for the specified Trusted Advisor check.**  

```
Get-ASATrustedAdvisorCheckSummary -CheckId "checkid1"
```
**Example 2: Returns the latest summaries for the specified Trusted Advisor checks.**  

```
Get-ASATrustedAdvisorCheckSummary -CheckId @("checkid1", "checkid2")
```
+  For API details, see [DescribeTrustedAdvisorCheckSummaries](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: Returns the latest summary for the specified Trusted Advisor check.**  

```
Get-ASATrustedAdvisorCheckSummary -CheckId "checkid1"
```
**Example 2: Returns the latest summaries for the specified Trusted Advisor checks.**  

```
Get-ASATrustedAdvisorCheckSummary -CheckId @("checkid1", "checkid2")
```
+  For API details, see [DescribeTrustedAdvisorCheckSummaries](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using AWS Support with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.