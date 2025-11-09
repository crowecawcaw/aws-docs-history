AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Use `DescribeAssociationExecutions` with a CLI

The following code examples show how to use `DescribeAssociationExecutions`.

CLI

**AWS CLI**

**Example 1: To get details of all executions for an association**

The following `describe-association-executions` example describes all executions of the specified association.

```
`aws ssm describe-association-executions \
 --association-id `"8dfe3659-4309-493a-8755-0123456789ab"``

```

Output:

```
{
    "AssociationExecutions": [
        {
            "AssociationId": "8dfe3659-4309-493a-8755-0123456789ab",
            "AssociationVersion": "1",
            "ExecutionId": "474925ef-1249-45a2-b93d-0123456789ab",
            "Status": "Success",
            "DetailedStatus": "Success",
            "CreatedTime": 1550505827.119,
            "ResourceCountByStatus": "{Success=1}"
        },
        {
            "AssociationId": "8dfe3659-4309-493a-8755-0123456789ab",
            "AssociationVersion": "1",
            "ExecutionId": "7abb6378-a4a5-4f10-8312-0123456789ab",
            "Status": "Success",
            "DetailedStatus": "Success",
            "CreatedTime": 1550505536.843,
            "ResourceCountByStatus": "{Success=1}"
        },
        ...
    ]
}
```

For more information, see [Viewing association histories](sysman-state-assoc-history.md "sysman-state-assoc-history.md") in the _AWS Systems Manager User Guide_.

**Example 2: To get details of all executions for an association after a specific date and time**

The following `describe-association-executions` example describes all executions of an association after the specified date and time.

```
`aws ssm describe-association-executions \
 --association-id `"8dfe3659-4309-493a-8755-0123456789ab"` \
 --filters `"Key=CreatedTime,Value=2019-02-18T16:00:00Z,Type=GREATER_THAN"``

```

Output:

```
{
    "AssociationExecutions": [
        {
            "AssociationId": "8dfe3659-4309-493a-8755-0123456789ab",
            "AssociationVersion": "1",
            "ExecutionId": "474925ef-1249-45a2-b93d-0123456789ab",
            "Status": "Success",
            "DetailedStatus": "Success",
            "CreatedTime": 1550505827.119,
            "ResourceCountByStatus": "{Success=1}"
        },
        {
            "AssociationId": "8dfe3659-4309-493a-8755-0123456789ab",
            "AssociationVersion": "1",
            "ExecutionId": "7abb6378-a4a5-4f10-8312-0123456789ab",
            "Status": "Success",
            "DetailedStatus": "Success",
            "CreatedTime": 1550505536.843,
            "ResourceCountByStatus": "{Success=1}"
        },
        ...
    ]
}
```

For more information, see [Viewing association histories](sysman-state-assoc-history.md "sysman-state-assoc-history.md") in the _AWS Systems Manager User Guide_.

- For API details, see
  [DescribeAssociationExecutions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-association-executions.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-association-executions.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example returns the executions for the association ID provided**

```
Get-SSMAssociationExecution -AssociationId 123a45a0-c678-9012-3456-78901234db5e

```

**Output:**

```
AssociationId         : 123a45a0-c678-9012-3456-78901234db5e
AssociationVersion    : 2
CreatedTime           : 3/2/2019 8:53:29 AM
DetailedStatus        :
ExecutionId           : 123a45a0-c678-9012-3456-78901234db5e
LastExecutionDate     : 1/1/0001 12:00:00 AM
ResourceCountByStatus : {Success=4}
Status                : Success
```

- For API details, see
  [DescribeAssociationExecutions](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example returns the executions for the association ID provided**

```
Get-SSMAssociationExecution -AssociationId 123a45a0-c678-9012-3456-78901234db5e

```

**Output:**

```
AssociationId         : 123a45a0-c678-9012-3456-78901234db5e
AssociationVersion    : 2
CreatedTime           : 3/2/2019 8:53:29 AM
DetailedStatus        :
ExecutionId           : 123a45a0-c678-9012-3456-78901234db5e
LastExecutionDate     : 1/1/0001 12:00:00 AM
ResourceCountByStatus : {Success=4}
Status                : Success
```

- For API details, see
  [DescribeAssociationExecutions](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
