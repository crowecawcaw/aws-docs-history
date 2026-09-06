

# Use `GetComplianceSummaryByResourceType` with a CLI
<a name="example_config-service_GetComplianceSummaryByResourceType_section"></a>

The following code examples show how to use `GetComplianceSummaryByResourceType`.

------
#### [ CLI ]

**AWS CLI**  
**To get the compliance summary for all resource types**  
The following command returns the number of AWS resources that are noncompliant and the number that are compliant:  

```
aws configservice get-compliance-summary-by-resource-type
```
In the output, the value for each `CappedCount` attribute indicates how many resources are compliant or noncompliant.  
Output:  

```
{
    "ComplianceSummariesByResourceType": [
        {
            "ComplianceSummary": {
                "NonCompliantResourceCount": {
                    "CappedCount": 16,
                    "CapExceeded": false
                },
                "ComplianceSummaryTimestamp": 1453237464.543,
                "CompliantResourceCount": {
                    "CappedCount": 10,
                    "CapExceeded": false
                }
            }
        }
    ]
}
```
**To get the compliance summary for a specific resource type**  
The following command returns the number of EC2 instances that are noncompliant and the number that are compliant:  

```
aws configservice get-compliance-summary-by-resource-type --resource-types {{AWS::EC2::Instance}}
```
In the output, the value for each `CappedCount` attribute indicates how many resources are compliant or noncompliant.  
Output:  

```
{
    "ComplianceSummariesByResourceType": [
        {
            "ResourceType": "AWS::EC2::Instance",
            "ComplianceSummary": {
                "NonCompliantResourceCount": {
                    "CappedCount": 3,
                    "CapExceeded": false
                },
                "ComplianceSummaryTimestamp": 1452204923.518,
                "CompliantResourceCount": {
                    "CappedCount": 7,
                    "CapExceeded": false
                }
            }
        }
    ]
}
```
+  For API details, see [GetComplianceSummaryByResourceType](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/get-compliance-summary-by-resource-type.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This sample returns the number of resources that are compliant or noncompliant and converts the output to json.**  

```
Get-CFGComplianceSummaryByResourceType -Select ComplianceSummariesByResourceType.ComplianceSummary | ConvertTo-Json
{
  "ComplianceSummaryTimestamp": "2019-12-14T06:14:49.778Z",
  "CompliantResourceCount": {
    "CapExceeded": false,
    "CappedCount": 2
  },
  "NonCompliantResourceCount": {
    "CapExceeded": true,
    "CappedCount": 100
  }
}
```
+  For API details, see [GetComplianceSummaryByResourceType](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This sample returns the number of resources that are compliant or noncompliant and converts the output to json.**  

```
Get-CFGComplianceSummaryByResourceType -Select ComplianceSummariesByResourceType.ComplianceSummary | ConvertTo-Json
{
  "ComplianceSummaryTimestamp": "2019-12-14T06:14:49.778Z",
  "CompliantResourceCount": {
    "CapExceeded": false,
    "CappedCount": 2
  },
  "NonCompliantResourceCount": {
    "CapExceeded": true,
    "CappedCount": 100
  }
}
```
+  For API details, see [GetComplianceSummaryByResourceType](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using AWS Config with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.