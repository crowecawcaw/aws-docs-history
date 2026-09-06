

# Use `GetComplianceSummaryByConfigRule` with a CLI
<a name="example_config-service_GetComplianceSummaryByConfigRule_section"></a>

The following code examples show how to use `GetComplianceSummaryByConfigRule`.

------
#### [ CLI ]

**AWS CLI**  
**To get the compliance summary for your AWS Config rules**  
The following command returns the number of rules that are compliant and the number that are noncompliant:  

```
aws configservice get-compliance-summary-by-config-rule
```
In the output, the value for each `CappedCount` attribute indicates how many rules are compliant or noncompliant.  
Output:  

```
{
    "ComplianceSummary": {
        "NonCompliantResourceCount": {
            "CappedCount": 3,
            "CapExceeded": false
        },
        "ComplianceSummaryTimestamp": 1452204131.493,
        "CompliantResourceCount": {
            "CappedCount": 2,
            "CapExceeded": false
        }
    }
}
```
+  For API details, see [GetComplianceSummaryByConfigRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/get-compliance-summary-by-config-rule.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This sample returns the number of Config rules that are non-compliant.**  

```
Get-CFGComplianceSummaryByConfigRule -Select ComplianceSummary.NonCompliantResourceCount
```
**Output:**  

```
CapExceeded CappedCount
----------- -----------
False       9
```
+  For API details, see [GetComplianceSummaryByConfigRule](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This sample returns the number of Config rules that are non-compliant.**  

```
Get-CFGComplianceSummaryByConfigRule -Select ComplianceSummary.NonCompliantResourceCount
```
**Output:**  

```
CapExceeded CappedCount
----------- -----------
False       9
```
+  For API details, see [GetComplianceSummaryByConfigRule](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using AWS Config with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.