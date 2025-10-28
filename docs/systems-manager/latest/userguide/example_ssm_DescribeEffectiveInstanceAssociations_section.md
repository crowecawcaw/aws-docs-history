# Use `DescribeEffectiveInstanceAssociations` with a CLI

The following code examples show how to use `DescribeEffectiveInstanceAssociations`.

CLI

**AWS CLI**

**To get details of the effective associations for an instance**

The following `describe-effective-instance-associations` example retrieves details about the effective associations for an instance.

Command:

```
`aws ssm describe-effective-instance-associations --instance-id `"i-1234567890abcdef0"``

```

Output:

```
{
    "Associations": [
        {
            "AssociationId": "8dfe3659-4309-493a-8755-0123456789ab",
            "InstanceId": "i-1234567890abcdef0",
            "Content": "{\n    \"schemaVersion\": \"1.2\",\n    \"description\": \"Update the Amazon SSM Agent to the latest version or specified version.\",\n    \"parameters\": {\n        \"version\": {\n            \"default\": \"\",\n            \"description\": \"(Optional) A specific version of the Amazon SSM Agent to install. If not specified, the agent will be updated to the latest version.\",\n            \"type\": \"String\"\n        },\n        \"allowDowngrade\": {\n            \"default\": \"false\",\n            \"description\": \"(Optional) Allow the Amazon SSM Agent service to be downgraded to an earlier version. If set to false, the service can be upgraded to newer versions only (default). If set to true, specify the earlier version.\",\n            \"type\": \"String\",\n            \"allowedValues\": [\n                \"true\",\n                \"false\"\n            ]\n        }\n    },\n    \"runtimeConfig\": {\n        \"aws:updateSsmAgent\": {\n            \"properties\": [\n                {\n                \"agentName\": \"amazon-ssm-agent\",\n                \"source\": \"https://s3.{Region}.amazonaws.com/amazon-ssm-{Region}/ssm-agent-manifest.json\",\n                \"allowDowngrade\": \"{{ allowDowngrade }}\",\n                \"targetVersion\": \"{{ version }}\"\n                }\n            ]\n        }\n    }\n}\n",
            "AssociationVersion": "1"
        }
    ]
}
```

- For API details, see
  [DescribeEffectiveInstanceAssociations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-effective-instance-associations.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-effective-instance-associations.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example describes the effective associations for an instance.**

```
Get-SSMEffectiveInstanceAssociationList -InstanceId "i-0000293ffd8c57862" -MaxResult 5

```

**Output:**

```
AssociationId                        Content
-------------                        -------
d8617c07-2079-4c18-9847-1655fc2698b0 {...
```

**Example 2: This example displays the contents of the effective associations for an instance.**

```
(Get-SSMEffectiveInstanceAssociationList -InstanceId "i-0000293ffd8c57862" -MaxResult 5).Content

```

**Output:**

```
{
    "schemaVersion": "1.2",
    "description": "Update the Amazon SSM Agent to the latest version or specified version.",
    "parameters": {
        "version": {
            "default": "",
            "description": "(Optional) A specific version of the Amazon SSM Agent to install. If not specified, the agen
t will be updated to the latest version.",
            "type": "String"
        },
        "allowDowngrade": {
            "default": "false",
            "description": "(Optional) Allow the Amazon SSM Agent service to be downgraded to an earlier version. If set
 to false, the service can be upgraded to newer versions only (default). If set to true, specify the earlier version.",
            "type": "String",
            "allowedValues": [
                "true",
                "false"
            ]
        }
    },
    "runtimeConfig": {
        "aws:updateSsmAgent": {
            "properties": [
                {
                "agentName": "amazon-ssm-agent",
                "source": "https://s3.{Region}.amazonaws.com/amazon-ssm-{Region}/ssm-agent-manifest.json",
                "allowDowngrade": "{{ allowDowngrade }}",
                "targetVersion": "{{ version }}"
                }
            ]
        }
    }
}
```

- For API details, see
  [DescribeEffectiveInstanceAssociations](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example describes the effective associations for an instance.**

```
Get-SSMEffectiveInstanceAssociationList -InstanceId "i-0000293ffd8c57862" -MaxResult 5

```

**Output:**

```
AssociationId                        Content
-------------                        -------
d8617c07-2079-4c18-9847-1655fc2698b0 {...
```

**Example 2: This example displays the contents of the effective associations for an instance.**

```
(Get-SSMEffectiveInstanceAssociationList -InstanceId "i-0000293ffd8c57862" -MaxResult 5).Content

```

**Output:**

```
{
    "schemaVersion": "1.2",
    "description": "Update the Amazon SSM Agent to the latest version or specified version.",
    "parameters": {
        "version": {
            "default": "",
            "description": "(Optional) A specific version of the Amazon SSM Agent to install. If not specified, the agen
t will be updated to the latest version.",
            "type": "String"
        },
        "allowDowngrade": {
            "default": "false",
            "description": "(Optional) Allow the Amazon SSM Agent service to be downgraded to an earlier version. If set
 to false, the service can be upgraded to newer versions only (default). If set to true, specify the earlier version.",
            "type": "String",
            "allowedValues": [
                "true",
                "false"
            ]
        }
    },
    "runtimeConfig": {
        "aws:updateSsmAgent": {
            "properties": [
                {
                "agentName": "amazon-ssm-agent",
                "source": "https://s3.{Region}.amazonaws.com/amazon-ssm-{Region}/ssm-agent-manifest.json",
                "allowDowngrade": "{{ allowDowngrade }}",
                "targetVersion": "{{ version }}"
                }
            ]
        }
    }
}
```

- For API details, see
  [DescribeEffectiveInstanceAssociations](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
