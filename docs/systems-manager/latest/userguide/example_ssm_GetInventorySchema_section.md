

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Use `GetInventorySchema` with a CLI
<a name="example_ssm_GetInventorySchema_section"></a>

The following code examples show how to use `GetInventorySchema`.

------
#### [ CLI ]

**AWS CLI**  
**To view your inventory schema**  
This example returns a list of inventory type names for the account.  
Command:  

```
aws ssm get-inventory-schema
```
Output:  

```
{
  "Schemas": [
      {
          "TypeName": "AWS:AWSComponent",
          "Version": "1.0",
          "Attributes": [
              {
                  "Name": "Name",
                  "DataType": "STRING"
              },
              {
                  "Name": "ApplicationType",
                  "DataType": "STRING"
              },
              {
                  "Name": "Publisher",
                  "DataType": "STRING"
              },
              {
                  "Name": "Version",
                  "DataType": "STRING"
              },
              {
                  "Name": "InstalledTime",
                  "DataType": "STRING"
              },
              {
                  "Name": "Architecture",
                  "DataType": "STRING"
              },
              {
                  "Name": "URL",
                  "DataType": "STRING"
              }
          ]
      },
      ...
  ],
  "NextToken": "--token string truncated--"
}
```
**To view the inventory schema for a specific inventory type**  
This example return the inventory schema for a the AWS:AWSComponent inventory type.  
Command:  

```
aws ssm get-inventory-schema --type-name {{"AWS:AWSComponent"}}
```
+  For API details, see [GetInventorySchema](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-inventory-schema.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example returns a list of inventory type names for the account.**  

```
Get-SSMInventorySchema
```
+  For API details, see [GetInventorySchema](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example returns a list of inventory type names for the account.**  

```
Get-SSMInventorySchema
```
+  For API details, see [GetInventorySchema](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.