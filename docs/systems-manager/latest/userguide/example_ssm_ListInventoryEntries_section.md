• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Use `ListInventoryEntries` with a CLI

The following code examples show how to use `ListInventoryEntries`.

CLI

**AWS CLI**

**Example 1: To view specific inventory type entries for an instance**

This following `list-inventory-entries` example lists the inventory entries for the AWS:Application inventory type on a specific instance.

```
`aws ssm list-inventory-entries \
 --instance-id `"i-1234567890abcdef0"` \
 --type-name `"AWS:Application"``

```

Output:

```
{
  "TypeName": "AWS:Application",
  "InstanceId": "i-1234567890abcdef0",
  "SchemaVersion": "1.1",
  "CaptureTime": "2019-02-15T12:17:55Z",
  "Entries": [
    {
      "Architecture": "i386",
      "Name": "Amazon SSM Agent",
      "PackageId": "{88a60be2-89a1-4df8-812a-80863c2a2b68}",
      "Publisher": "Amazon Web Services",
      "Version": "2.3.274.0"
    },
    {
      "Architecture": "x86_64",
      "InstalledTime": "2018-05-03T13:42:34Z",
      "Name": "AmazonCloudWatchAgent",
      "Publisher": "",
      "Version": "1.200442.0"
    }
  ]
}
```

**Example 2: To view custom inventory entries assigned to an instance**

The following `list-inventory-entries` example lists a custom inventory entry assigned to an instance.

```
`aws ssm list-inventory-entries \
 --instance-id `"i-1234567890abcdef0"` \
 --type-name `"Custom:RackInfo"``

```

Output:

```
{
  "TypeName": "Custom:RackInfo",
  "InstanceId": "i-1234567890abcdef0",
  "SchemaVersion": "1.0",
  "CaptureTime": "2021-05-22T10:01:01Z",
  "Entries": [
    {
      "RackLocation": "Bay B/Row C/Rack D/Shelf E"
    }
  ]
}
```

- For API details, see
  [ListInventoryEntries](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-inventory-entries.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-inventory-entries.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example lists all the custom inventory entries for an instance.**

```
Get-SSMInventoryEntriesList -InstanceId "i-0cb2b964d3e14fd9f" -TypeName "Custom:RackInfo"

```

**Output:**

```
CaptureTime   : 2016-08-22T10:01:01Z
Entries       : {Amazon.Runtime.Internal.Util.AlwaysSendDictionary`2[System.String,System.String]}
InstanceId    : i-0cb2b964d3e14fd9f
NextToken     :
SchemaVersion : 1.0
TypeName      : Custom:RackInfo
```

**Example 2: This example lists the details.**

```
(Get-SSMInventoryEntriesList -InstanceId "i-0cb2b964d3e14fd9f" -TypeName "Custom:RackInfo").Entries

```

**Output:**

```
Key          Value
---          -----
RackLocation Bay B/Row C/Rack D/Shelf E
```

- For API details, see
  [ListInventoryEntries](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example lists all the custom inventory entries for an instance.**

```
Get-SSMInventoryEntriesList -InstanceId "i-0cb2b964d3e14fd9f" -TypeName "Custom:RackInfo"

```

**Output:**

```
CaptureTime   : 2016-08-22T10:01:01Z
Entries       : {Amazon.Runtime.Internal.Util.AlwaysSendDictionary`2[System.String,System.String]}
InstanceId    : i-0cb2b964d3e14fd9f
NextToken     :
SchemaVersion : 1.0
TypeName      : Custom:RackInfo
```

**Example 2: This example lists the details.**

```
(Get-SSMInventoryEntriesList -InstanceId "i-0cb2b964d3e14fd9f" -TypeName "Custom:RackInfo").Entries

```

**Output:**

```
Key          Value
---          -----
RackLocation Bay B/Row C/Rack D/Shelf E
```

- For API details, see
  [ListInventoryEntries](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
