AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Use `GetInventorySchema` with a CLI

The following code examples show how to use `GetInventorySchema`.

CLI

**AWS CLI**

**To view your inventory schema**

This example returns a list of inventory type names for the account.

Command:

```
`aws ssm get-inventory-schema`

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
`aws ssm get-inventory-schema --type-name `"AWS:AWSComponent"``

```

- For API details, see
  [GetInventorySchema](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-inventory-schema.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-inventory-schema.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example returns a list of inventory type names for the account.**

```
Get-SSMInventorySchema

```

- For API details, see
  [GetInventorySchema](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example returns a list of inventory type names for the account.**

```
Get-SSMInventorySchema

```

- For API details, see
  [GetInventorySchema](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
