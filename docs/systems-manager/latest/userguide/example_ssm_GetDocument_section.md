• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Use `GetDocument` with a CLI

The following code examples show how to use `GetDocument`.

CLI

**AWS CLI**

**To get document content**

The following `get-document` example displays the content of a Systems Manager document.

```
`aws ssm get-document \
 --name `"AWS-RunShellScript"``

```

Output:

```
{
    "Name": "AWS-RunShellScript",
    "DocumentVersion": "1",
    "Status": "Active",
    "Content": "{\n    \"schemaVersion\":\"1.2\",\n    \"description\":\"Run a shell script or specify the commands to run.\",\n    \"parameters\":{\n        \"commands\":{\n            \"type\":\"StringList\",\n            \"description\":\"(Required) Specify a shell script or a command to run.\",\n            \"minItems\":1,\n            \"displayType\":\"textarea\"\n        },\n        \"workingDirectory\":{\n            \"type\":\"String\",\n            \"default\":\"\",\n            \"description\":\"(Optional) The path to the working directory on your instance.\",\n            \"maxChars\":4096\n        },\n        \"executionTimeout\":{\n            \"type\":\"String\",\n            \"default\":\"3600\",\n            \"description\":\"(Optional) The time in seconds for a command to complete before it is considered to have failed. Default is 3600 (1 hour). Maximum is 172800 (48 hours).\",\n            \"allowedPattern\":\"([1-9][0-9]{0,4})|(1[0-6][0-9]{4})|(17[0-1][0-9]{3})|(172[0-7][0-9]{2})|(172800)\"\n        }\n    },\n    \"runtimeConfig\":{\n        \"aws:runShellScript\":{\n            \"properties\":[\n                {\n                    \"id\":\"0.aws:runShellScript\",\n                    \"runCommand\":\"{{ commands }}\",\n                    \"workingDirectory\":\"{{ workingDirectory }}\",\n                    \"timeoutSeconds\":\"{{ executionTimeout }}\"\n                }\n            ]\n        }\n    }\n}\n",
    "DocumentType": "Command",
    "DocumentFormat": "JSON"
}
```

For more information, see [AWS Systems Manager Documents](sysman-ssm-docs.md "sysman-ssm-docs.md") in the _AWS Systems Manager User Guide_.

- For API details, see
  [GetDocument](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-document.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-document.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example returns the content of a document.**

```
Get-SSMDocument -Name "RunShellScript"

```

**Output:**

```
Content
-------
{...
```

**Example 2: This example displays the complete contents of a document.**

```
(Get-SSMDocument -Name "RunShellScript").Content
{
   "schemaVersion":"2.0",
   "description":"Run an updated script",
   "parameters":{
      "commands":{
         "type":"StringList",
         "description":"(Required) Specify a shell script or a command to run.",
         "minItems":1,
         "displayType":"textarea"
      }
   },
   "mainSteps":[
      {
         "action":"aws:runShellScript",
         "name":"runShellScript",
         "inputs":{
            "commands":"{{ commands }}"
         }
      },
      {
         "action":"aws:runPowerShellScript",
         "name":"runPowerShellScript",
         "inputs":{
            "commands":"{{ commands }}"
         }
      }
   ]
}

```

- For API details, see
  [GetDocument](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example returns the content of a document.**

```
Get-SSMDocument -Name "RunShellScript"

```

**Output:**

```
Content
-------
{...
```

**Example 2: This example displays the complete contents of a document.**

```
(Get-SSMDocument -Name "RunShellScript").Content
{
   "schemaVersion":"2.0",
   "description":"Run an updated script",
   "parameters":{
      "commands":{
         "type":"StringList",
         "description":"(Required) Specify a shell script or a command to run.",
         "minItems":1,
         "displayType":"textarea"
      }
   },
   "mainSteps":[
      {
         "action":"aws:runShellScript",
         "name":"runShellScript",
         "inputs":{
            "commands":"{{ commands }}"
         }
      },
      {
         "action":"aws:runPowerShellScript",
         "name":"runPowerShellScript",
         "inputs":{
            "commands":"{{ commands }}"
         }
      }
   ]
}

```

- For API details, see
  [GetDocument](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
