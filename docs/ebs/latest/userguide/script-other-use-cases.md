# Other use cases for Data Lifecycle Manager pre and post scripts

In addition to using pre and post scripts for automating application-consistent
snapshots, you can use pre and post scripts together, or individually, to automate
other administrative tasks before or after snapshot creation. For example:

- Using a pre script to apply patches before creating snapshots. This
  can help you create snapshots after applying your regular weekly or
  monthly software updates.

###### Note

If you choose to run a pre script only, **Default to
crash-consistent snapshots** is enabled by default.

- Using a post script to apply patches after creating snapshots. This
  can help you create snapshots before applying your regular weekly or
  monthly software updates.

## Getting started for other use cases

This section explains the steps you need perform when using pre and/or post scripts
for **uses cases other than application-consistent snapshots**.

###### To prepare your target instances for pre and/or post scripts

1. Install the SSM Agent on your target instances, if it is not already installed.
   If SSM Agent is already installed on your target instances, skip this step.
   - (Linux instances) [Manually installing SSM Agent on EC2 instances for Linux](../../../systems-manager/latest/userguide/manually-install-ssm-agent-linux.md "../../../systems-manager/latest/userguide/manually-install-ssm-agent-linux.md")
   - (Windows instances) [Working with SSM Agent on EC2 instances for Windows Server](../../../systems-manager/latest/userguide/ssm-agent-windows.md "../../../systems-manager/latest/userguide/ssm-agent-windows.md")

2. Ensure that the SSM Agent is running. For more information, see
   [Checking SSM Agent status and starting the agent](../../../systems-manager/latest/userguide/ssm-agent-status-and-restart.md "../../../systems-manager/latest/userguide/ssm-agent-status-and-restart.md").
3. Set up Systems Manager for Amazon EC2 instances. For more information, see [Setting up Systems Manager
   for Amazon EC2 instances](../../../systems-manager/latest/userguide/systems-manager-setting-up-ec2.md "../../../systems-manager/latest/userguide/systems-manager-setting-up-ec2.md") in the _AWS Systems Manager User Guide_.
   You must create an SSM command document that includes the pre and/or post scripts
   with the commands you want to run.

You can create an SSM document using the empty SSM document template below and
add your pre and post script commands in the appropriate document sections.

###### Note the following:

- It is your responsibility to ensure that the SSM document performs the
  correct and required actions for your workload.
- The SSM document must include required fields for `allowedValues`,
  including `pre-script`, `post-script`, and
  `dry-run`. Amazon Data Lifecycle Manager will execute commands on your instance based on
  the contents of those sections. If your SSM document does not have those
  sections, then Amazon Data Lifecycle Manager will treat it as a failed execution.

```
###===============================================================================###
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.

# Permission is hereby granted, free of charge, to any person obtaining a copy of this
# software and associated documentation files (the "Software"), to deal in the Software
# without restriction, including without limitation the rights to use, copy, modify,
# merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
###===============================================================================###
schemaVersion: '2.2'
description: SSM Document Template for Amazon Data Lifecycle Manager Pre/Post script feature
parameters:
  executionId:
    type: String
    default: None
    description: (Required) Specifies the unique identifier associated with a pre and/or post execution
    allowedPattern: ^(None|[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12})$
  command:
  # Data Lifecycle Manager will trigger the pre-script and post-script actions during policy execution.
  # 'dry-run' option is intended for validating the document execution without triggering any commands
  # on the instance. The following allowedValues will allow Data Lifecycle Manager to successfully
  # trigger pre and post script actions.
    type: String
    default: 'dry-run'
    description: (Required) Specifies whether pre-script and/or post-script should be executed.
    allowedValues:
    - pre-script
    - post-script
    - dry-run

mainSteps:
- action: aws:runShellScript
  description: Run Database freeze/thaw commands
  name: run_pre_post_scripts
  precondition:
    StringEquals:
    - platformType
    - Linux
  inputs:
    runCommand:
    - |
      #!/bin/bash

      ###===============================================================================###
      ### Error Codes
      ###===============================================================================###
      # The following Error codes will inform Data Lifecycle Manager of the type of error
      # and help guide handling of the error.
      # The Error code will also be emitted via AWS Eventbridge events in the 'cause' field.
      # 1 Pre-script failed during execution - 201
      # 2 Post-script failed during execution - 202
      # 3 Auto thaw occurred before post-script was initiated - 203
      # 4 Pre-script initiated while post-script was expected - 204
      # 5 Post-script initiated while pre-script was expected - 205
      # 6 Application not ready for pre or post-script initiation - 206

      ###===============================================================================###
      ### Global variables
      ###===============================================================================###
      START=$(date +%s)
      # For testing this script locally, replace the below with OPERATION=$1.
      OPERATION={{ command }}

      # Add all pre-script actions to be performed within the function below
      execute_pre_script() {
          echo "INFO: Start execution of pre-script"
      }

      # Add all post-script actions to be performed within the function below
      execute_post_script() {
          echo "INFO: Start execution of post-script"
      }

      # Debug logging for parameters passed to the SSM document
      echo "INFO: ${OPERATION} starting at $(date) with executionId: ${EXECUTION_ID}"

      # Based on the command parameter value execute the function that supports
      # pre-script/post-script operation
      case ${OPERATION} in
          pre-script)
              execute_pre_script
              ;;
          post-script)
              execute_post_script
              ;;
          dry-run)
              echo "INFO: dry-run option invoked - taking no action"
              ;;
          *)
              echo "ERROR: Invalid command parameter passed. Please use either pre-script, post-script, dry-run."
              exit 1 # return failure
              ;;
      esac

      END=$(date +%s)
      # Debug Log for profiling the script time
      echo "INFO: ${OPERATION} completed at $(date). Total runtime: $((${END} - ${START})) seconds."
```

###### Note

This step is needed if:

- You create or update a pre/post script-enabled snapshot policy that
  uses a custom IAM role.
- You use the command line to create or update a pre/post script-enabled
  snapshot policy that uses the default.
  If you use the console to create or update a pre/post script-enabled snapshot policy
  that uses the default role for managing snapshots (**AWSDataLifecycleManagerDefaultRole**), skip
  this step. In this case, we automatically attach the **AWSDataLifecycleManagerSSMFullAccess**
  policy to that role.

You must ensure that that IAM role that you use for the policy grants Amazon Data Lifecycle Manager permission to
perform the SSM actions required to run pre and post scripts on instances targeted by the
policy.

Amazon Data Lifecycle Manager provides a managed policy (**AWSDataLifecycleManagerSSMFullAccess**)
that includes the required permissions. You can attach this policy to your
IAM role for managing snapshots to ensure that it includes the permissions.

###### Important

The AWSDataLifecycleManagerSSMFullAccess managed policy uses the `aws:ResourceTag`
condition key to restrict access to specific SSM documents when using pre and post scripts.
To allow Amazon Data Lifecycle Manager to access the SSM documents, you must ensure that your SSM documents
are tagged with `DLMScriptsAccess:true`.

Alternatively, you can manually create a custom policy or assign the required
permissions directly to the IAM role that you use. You can use the same permissions
that are defined in the AWSDataLifecycleManagerSSMFullAccess managed policy, however,
the `aws:ResourceTag` condition key is optional. If you decide to not
use that condition key, then you do not need to tag your SSM documents with
`DLMScriptsAccess:true`.

Use one of the following methods to add the **AWSDataLifecycleManagerSSMFullAccess**
policy to your IAM role.

Console

###### To attach the managed policy to your custom role

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation panel, choose **Roles**.
3. Search for and select your custom role for managing snapshots.
4. On the **Permissions** tab, choose **Add
   permissions**, **Attach policies**.
5. Search for and select the **AWSDataLifecycleManagerSSMFullAccess**
   managed policy, and then choose **Add permissions**.

AWS CLI

###### To attach the managed policy to your custom role

Use the [attach-role-policy](../../../cli/latest/reference/iam/attach-role-policy.md "../../../cli/latest/reference/iam/attach-role-policy.md") command. For `---role-name`, specify the
name of your custom role. For `--policy-arn`, specify
`arn:aws:iam::aws:policy/AWSDataLifecycleManagerSSMFullAccess`.

```
`$` aws iam attach-role-policy \
--policy-arn arn:aws:iam::aws:policy/AWSDataLifecycleManagerSSMFullAccess \
--role-name `your_role_name`
```

Console###### To create the snapshot lifecycle policy

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Elastic Block Store**,
   **Lifecycle Manager**, and then choose **Create
   lifecycle policy**.
3. On the **Select policy type** screen, choose **EBS
   snapshot policy** and then choose **Next**.
4. In the **Target resources** section, do the following:
   1. For **Target resource types**, choose `Instance`.
   2. For **Target resource tags**, specify the resource
      tags that identify the instances to back up. Only resources that have
      the specified tags will be backed up.

5. For **IAM role**, either choose **AWSDataLifecycleManagerDefaultRole**
   (the default role for managing snapshots), or choose
   a custom role that you created and prepared for pre
   and post scripts.
6. Configure the schedules and additional options as needed. We recommend that you
   schedule snapshot creation times for time periods that match your workload, such as
   during maintenance windows.
7. In the **Pre and post scripts** section, select **Enable
   pre and post scripts** and then do the following:
   1. Select **Custom SSM document**.
   2. For **Automate option**, choose the option that matches
      the scripts you want to run.
   3. For **SSM document**, select the SSM document that you
      prepared.

8. Configure the following additional options if needed:
   - **Script timeout** — The timeout period after which Amazon Data Lifecycle Manager
     fails the script run attempt if it has not completed. If a script does not complete
     within its timeout period, Amazon Data Lifecycle Manager fails the attempt. The timeout period applies to
     the pre and post scripts individually. The minimum and default timeout period is 10
     seconds. And the maximum timeout period is 120 seconds.
   - **Retry failed scripts** — Select this option to retry
     scripts that do not complete within their timeout period. If the pre script fails,
     Amazon Data Lifecycle Manager retries entire snapshot creation process, including running the pre and post
     scripts. If the post script fails, Amazon Data Lifecycle Manager retries the post script only; in this case,
     the pre script will have completed and the snapshot might have been created.
   - **Default to crash-consistent snapshots** — Select this
     option to default to crash-consistent snapshots if the pre script fails to run. This
     is the default snapshot creation behavior for Amazon Data Lifecycle Manager if pre and post scripts is not
     enabled. If you enabled retries, Amazon Data Lifecycle Manager will default to crash-consistent snapshots only
     after all retry attempts have been exhausted. If the pre script fails and you do not
     default to crash-consistent snapshots, Amazon Data Lifecycle Manager will not create snapshots for the instance
     during that schedule run.

9. Choose **Create default policy**.

###### Note

If you get the `Role with name AWSDataLifecycleManagerDefaultRole already exists` error,
see [Troubleshoot Amazon Data Lifecycle Manager issues](dlm-troubleshooting.md "dlm-troubleshooting.md") for more information.

AWS CLI

###### To create the snapshot lifecycle policy

Use the [create-lifecycle-policy](../../../cli/latest/reference/dlm/create-lifecycle-policy.md "../../../cli/latest/reference/dlm/create-lifecycle-policy.md") command, and include the `Scripts`
parameters in `CreateRule`. For more information about the parameters,
see the [_Amazon Data Lifecycle Manager API Reference_](../../../dlm/latest/APIReference/API_Script.md "../../../dlm/latest/APIReference/API_Script.md").

```
`$` aws dlm create-lifecycle-policy \
--description "`policy_description`" \
--state ENABLED \
--execution-role-arn `iam_role_arn` \
--policy-details file:`//policyDetails.json`
```

Where `policyDetails.json` includes the following.

```
{
    "PolicyType": "EBS_SNAPSHOT_MANAGEMENT",
    "ResourceTypes": [
        "INSTANCE"
    ],
    "TargetTags": [{
        "Key": "`tag_key`",
        "Value": "`tag_value`"
    }],
    "Schedules": [{
        "Name": "`schedule_name`",
        "CreateRule": {
            "CronExpression": "`cron_for_creation_frequency`",
            "Scripts": [{
                "Stages": [`"PRE"` | `"POST"` | `"PRE","POST"`],
                "ExecutionHandlerService":"AWS_SYSTEMS_MANAGER",
                "ExecutionHandler":"`ssm_document_name|arn`",
                "ExecuteOperationOnScriptFailure":`true|false`,
                "ExecutionTimeout":`timeout_in_seconds (10-120)`,
                "MaximumRetryCount":`retries (0-3)`
            }]
        },
        "RetainRule": {
            "Count": `retention_count`
        }
    }]
}
```
