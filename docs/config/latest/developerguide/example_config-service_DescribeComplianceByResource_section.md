

# Use `DescribeComplianceByResource` with a CLI
<a name="example_config-service_DescribeComplianceByResource_section"></a>

The following code examples show how to use `DescribeComplianceByResource`.

------
#### [ CLI ]

**AWS CLI**  
**To get compliance information for your AWS resources**  
The following command returns compliance information for each EC2 instance that is recorded by AWS Config and that violates one or more rules:  

```
aws configservice describe-compliance-by-resource --resource-type {{AWS::EC2::Instance}} --compliance-types {{NON_COMPLIANT}}
```
In the output, the value for each `CappedCount` attribute indicates how many rules the resource violates. For example, the following output indicates that instance `i-1a2b3c4d` violates 2 rules.  
Output:  

```
{
    "ComplianceByResources": [
        {
            "ResourceType": "AWS::EC2::Instance",
            "ResourceId": "i-1a2b3c4d",
            "Compliance": {
                "ComplianceContributorCount": {
                    "CappedCount": 2,
                    "CapExceeded": false
                },
                "ComplianceType": "NON_COMPLIANT"
            }
        },
        {
            "ResourceType": "AWS::EC2::Instance",
            "ResourceId": "i-2a2b3c4d ",
            "Compliance": {
                "ComplianceContributorCount": {
                    "CappedCount": 3,
                    "CapExceeded": false
                },
                "ComplianceType": "NON_COMPLIANT"
            }
        }
    ]
}
```
+  For API details, see [DescribeComplianceByResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-compliance-by-resource.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example checks the `AWS::SSM::ManagedInstanceInventory` resource type for 'COMPLIANT' compliance type.**  

```
Get-CFGComplianceByResource -ComplianceType COMPLIANT -ResourceType AWS::SSM::ManagedInstanceInventory
```
**Output:**  

```
Compliance                            ResourceId          ResourceType
----------                            ----------          ------------
Amazon.ConfigService.Model.Compliance i-0123bcf4b567890e3 AWS::SSM::ManagedInstanceInventory
Amazon.ConfigService.Model.Compliance i-0a1234f6f5d6b78f7 AWS::SSM::ManagedInstanceInventory
```
+  For API details, see [DescribeComplianceByResource](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example checks the `AWS::SSM::ManagedInstanceInventory` resource type for 'COMPLIANT' compliance type.**  

```
Get-CFGComplianceByResource -ComplianceType COMPLIANT -ResourceType AWS::SSM::ManagedInstanceInventory
```
**Output:**  

```
Compliance                            ResourceId          ResourceType
----------                            ----------          ------------
Amazon.ConfigService.Model.Compliance i-0123bcf4b567890e3 AWS::SSM::ManagedInstanceInventory
Amazon.ConfigService.Model.Compliance i-0a1234f6f5d6b78f7 AWS::SSM::ManagedInstanceInventory
```
+  For API details, see [DescribeComplianceByResource](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using AWS Config with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.