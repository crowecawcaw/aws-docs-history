

# Use `DescribeTrustedAdvisorCheckRefreshStatuses` with a CLI
<a name="example_support_DescribeTrustedAdvisorCheckRefreshStatuses_section"></a>

The following code examples show how to use `DescribeTrustedAdvisorCheckRefreshStatuses`.

------
#### [ CLI ]

**AWS CLI**  
**To list the refresh statuses of AWS Trusted Advisor checks**  
The following `describe-trusted-advisor-check-refresh-statuses` example lists the refresh statuses for two Trusted Advisor checks: Amazon S3 Bucket Permissions and IAM Use.  

```
aws support describe-trusted-advisor-check-refresh-statuses \
    --check-id {{"Pfx0RwqBli"}} {{"zXCkfM1nI3"}}
```
Output:  

```
{
    "statuses": [
        {
            "checkId": "Pfx0RwqBli",
            "status": "none",
            "millisUntilNextRefreshable": 0
        },
        {
            "checkId": "zXCkfM1nI3",
            "status": "none",
            "millisUntilNextRefreshable": 0
        }
    ]
}
```
For more information, see [AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html) in the *AWS Support User Guide*.  
+  For API details, see [DescribeTrustedAdvisorCheckRefreshStatuses](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/describe-trusted-advisor-check-refresh-statuses.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: Returns the current status of refresh requests for the specified checks. Request-ASATrustedAdvisorCheckRefresh can be used to request that the status information of the checks be refreshed.**  

```
Get-ASATrustedAdvisorCheckRefreshStatus -CheckId @("checkid1", "checkid2")
```
+  For API details, see [DescribeTrustedAdvisorCheckRefreshStatuses](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: Returns the current status of refresh requests for the specified checks. Request-ASATrustedAdvisorCheckRefresh can be used to request that the status information of the checks be refreshed.**  

```
Get-ASATrustedAdvisorCheckRefreshStatus -CheckId @("checkid1", "checkid2")
```
+  For API details, see [DescribeTrustedAdvisorCheckRefreshStatuses](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using AWS Support with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.