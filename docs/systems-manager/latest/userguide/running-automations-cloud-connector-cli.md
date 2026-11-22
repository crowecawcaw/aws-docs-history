

# Run an automation on Azure or Google Cloud resources (command line)

The following procedure describes how to use the AWS CLI (on Linux or Windows) or AWS Tools for PowerShell to run an automation on Microsoft Azure or Google Cloud resources that a Cloud Connector can reach. The automation uses a single target whose `Key` is `CloudConnector` and whose value is a JSON object. To avoid nested quoting on the command line, keep the JSON in a file.

**To run an automation on Azure or Google Cloud resources**

1. Install and configure the AWS CLI or the AWS Tools for PowerShell, if you haven't already.

   For information, see [Installing or updating the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and [Installing the AWS Tools for PowerShell](https://docs.aws.amazon.com/powershell/latest/userguide/pstools-getting-set-up.html).

1. *Example 1: Azure resources*

   Create a file named `azure-target.json` that describes the connector and the filters. This example finds running and stopped virtual machines (VMs) in one subscription and resource group that have the tag `Env=prod`. Replace the connector ID, subscription ID, and resource group name with your own.

   ```json
   {
       "CloudConnectorId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
       "AzureSubscriptions": ["11111111-2222-3333-4444-555555555555"],
       "AzureResourceGroups": ["my-resource-group"],
       "AzureTag": { "Key": "Env", "Value": "prod" },
       "AzureVmPowerStates": ["RUNNING", "STOPPED", "DEALLOCATED"]
   }
   ```

   For the AWS CLI on Linux, macOS, or Windows, create a file named `start-azure.json` with the full request. The target value is the `azure-target.json` object as a JSON string.

   ```json
   {
       "DocumentName": "AWS-InstallDistributorPackageOnAzure",
       "Targets": [
           {
               "Key": "CloudConnector",
               "Values": ["{\"CloudConnectorId\":\"a1b2c3d4-5678-90ab-cdef-EXAMPLE11111\",\"AzureSubscriptions\":[\"11111111-2222-3333-4444-555555555555\"],\"AzureResourceGroups\":[\"my-resource-group\"],\"AzureTag\":{\"Key\":\"Env\",\"Value\":\"prod\"},\"AzureVmPowerStates\":[\"RUNNING\",\"STOPPED\",\"DEALLOCATED\"]}"]
           }
       ],
       "TargetParameterName": "AzureVmResourceId",
       "MaxConcurrency": "10",
       "MaxErrors": "1",
       "Parameters": {
           "AutomationAssumeRole": ["arn:aws:iam::111122223333:role/service-role/SSM-AzureAssumeRole-MyConnector-a1b2c3d4"],
           "CloudConnector": ["a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"],
           "PackageName": ["MyPackage"]
       }
   }
   ```

   Run the following command.

------
#### [ Linux & macOS ]

   ```sh
   aws ssm start-automation-execution \
       --cli-input-json file://start-azure.json
   ```

------
#### [ Windows ]

   ```sh
   aws ssm start-automation-execution ^
       --cli-input-json file://start-azure.json
   ```

------
#### [ PowerShell ]

   ```powershell
   $Target = New-Object Amazon.SimpleSystemsManagement.Model.Target
   $Target.Key = "CloudConnector"
   $Target.Values = Get-Content -Raw azure-target.json
   
   Start-SSMAutomationExecution `
       -DocumentName "AWS-InstallDistributorPackageOnAzure" `
       -Target $Target `
       -TargetParameterName "AzureVmResourceId" `
       -Parameter @{"AutomationAssumeRole"="arn:aws:iam::111122223333:role/service-role/SSM-AzureAssumeRole-MyConnector-a1b2c3d4";"CloudConnector"="a1b2c3d4-5678-90ab-cdef-EXAMPLE11111";"PackageName"="MyPackage"} `
       -MaxConcurrency "10" `
       -MaxError "1"
   ```

------

1. *Example 2: Google Cloud resources*

   For Google Cloud, replace `MyGcpRunbook` with your own runbook and `InstanceId` with the runbook input that receives each VM ID. Create a file named `gcp-target.json` that describes the connector, the projects, the zones, and the labels to include. Replace the connector ID, project ID, and zone with your own.

   ```json
   {
       "CloudConnectorId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
       "GcpProjects": ["my-project"],
       "Zones": ["us-central1-a"],
       "IncludesLabels": { "env": "prod" }
   }
   ```

   For the AWS CLI on Linux, macOS, or Windows, create a file named `start-gcp.json` with the full request.

   ```json
   {
       "DocumentName": "MyGcpRunbook",
       "Targets": [
           {
               "Key": "CloudConnector",
               "Values": ["{\"CloudConnectorId\":\"a1b2c3d4-5678-90ab-cdef-EXAMPLE11111\",\"GcpProjects\":[\"my-project\"],\"Zones\":[\"us-central1-a\"],\"IncludesLabels\":{\"env\":\"prod\"}}"]
           }
       ],
       "TargetParameterName": "InstanceId",
       "MaxConcurrency": "10",
       "MaxErrors": "1",
       "Parameters": {
           "AutomationAssumeRole": ["arn:aws:iam::111122223333:role/service-role/SSM-GCPAssumeRole-MyConnector-a1b2c3d4"],
           "CloudConnector": ["a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"]
       }
   }
   ```

   Run the following command.

------
#### [ Linux & macOS ]

   ```sh
   aws ssm start-automation-execution \
       --cli-input-json file://start-gcp.json
   ```

------
#### [ Windows ]

   ```sh
   aws ssm start-automation-execution ^
       --cli-input-json file://start-gcp.json
   ```

------
#### [ PowerShell ]

   ```powershell
   $Target = New-Object Amazon.SimpleSystemsManagement.Model.Target
   $Target.Key = "CloudConnector"
   $Target.Values = Get-Content -Raw gcp-target.json
   
   Start-SSMAutomationExecution `
       -DocumentName "MyGcpRunbook" `
       -Target $Target `
       -TargetParameterName "InstanceId" `
       -Parameter @{"AutomationAssumeRole"="arn:aws:iam::111122223333:role/service-role/SSM-GCPAssumeRole-MyConnector-a1b2c3d4";"CloudConnector"="a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"} `
       -MaxConcurrency "10" `
       -MaxError "1"
   ```

------

   The command returns the execution ID of the parent automation.

## View the results
<a name="running-automations-cloud-connector-cli-results"></a>

To list the child automations that the parent automation started, run the following command. Replace {{parent execution ID}} with the execution ID that the `start-automation-execution` command returned.

```sh
aws ssm describe-automation-executions \
    --filters Key=ParentExecutionId,Values={{parent execution ID}}
```

To view the resources that the Cloud Connector target resolved, run the following command. Replace {{parent execution ID}} with your own information.

```sh
aws ssm get-automation-execution \
    --automation-execution-id {{parent execution ID}}
```

In the response, `ResolvedTargets.ParameterValues` holds at most the first 500 resource IDs, and `Truncated` is `true` when the target found more.