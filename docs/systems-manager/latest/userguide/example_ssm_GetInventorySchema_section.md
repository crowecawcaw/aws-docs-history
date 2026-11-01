

# Use `GetInventorySchema` with a CLI
<a name="example_ssm_GetInventorySchema_section"></a>

The following code examples show how to use `GetInventorySchema`.

------
#### [ CLI ]

**AWS CLI**  
**Example 1: To view your inventory schema**  
The following `get-inventory-schema` example returns a list of inventory type names for the account.  

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
    }
    ],
    "NextToken": "--token string truncated--"
}
```
For more information, see [Metadata collected by Inventory](https://docs.aws.amazon.com/systems-manager/latest/userguide/inventory-schema.html) in the *AWS Systems Manager User Guide*.  
**Example 2: To view the inventory schema for a specific inventory type**  
The following `get-inventory-schema` example returns the inventory schema for the `AWS:AWSComponent` inventory type.  

```
aws ssm get-inventory-schema \
    --type-name {{"AWS:AWSComponent"}}
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
        }
    ]
}
```
For more information, see [Metadata collected by Inventory](https://docs.aws.amazon.com/systems-manager/latest/userguide/inventory-schema.html) in the *AWS Systems Manager User Guide*.  
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