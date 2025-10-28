# Use `DescribePlacementGroups` with a CLI

The following code examples show how to use `DescribePlacementGroups`.

CLI

**AWS CLI**

**To describe your placement groups**

This example command describes all of your placement groups.

Command:

```
`aws ec2 describe-placement-groups`

```

Output:

```
{
    "PlacementGroups": [
        {
            "GroupName": "my-cluster",
            "State": "available",
            "Strategy": "cluster"
        },
        ...
    ]
}
```

- For API details, see
  [DescribePlacementGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-placement-groups.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-placement-groups.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example describes the specified placement group.**

```
Get-EC2PlacementGroup -GroupName my-placement-group

```

**Output:**

```
GroupName             State        Strategy
---------             -----        --------
my-placement-group    available    cluster
```

- For API details, see
  [DescribePlacementGroups](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example describes the specified placement group.**

```
Get-EC2PlacementGroup -GroupName my-placement-group

```

**Output:**

```
GroupName             State        Strategy
---------             -----        --------
my-placement-group    available    cluster
```

- For API details, see
  [DescribePlacementGroups](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
