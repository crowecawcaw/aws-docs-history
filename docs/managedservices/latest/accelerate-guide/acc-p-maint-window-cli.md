# Create a maintenance window with the Systems Manager command line interface (CLI) for AMS Accelerate

To create an AMS Accelerate maintenance window with the command line interface:

1. Follow the SSM
   [Tutorial: Create and configure a maintenance window (AWS CLI)](../../../systems-manager/latest/userguide/maintenance-windows-cli-tutorials-create.md "../../../systems-manager/latest/userguide/maintenance-windows-cli-tutorials-create.md") . For each step of the tutorial, here are sample CLI commands for patching.

###### Note

These examples are specific to Linux or macOS. The commands can also be run from AWS CloudShell which may be simpler than configuring `awscli` on a local machine. For details, see
[Working with AWS CloudShell](../../../cloudshell/latest/userguide/working-with-cloudshell.md "../../../cloudshell/latest/userguide/working-with-cloudshell.md").

    1. In step 1 of the tutorial, to create a maintenance window:



    ```
    aws ssm create-maintenance-window \
                    --name Sample-Maintenance-Window \
                    --schedule "cron(0 30 23 ? * TUE#2 *)" \
                    --duration 4 \
                    --cutoff 1 \
                    --allow-unassociated-targets \
                    --tags "Key=Environment,Value=Production"
    ```

    On successful completion, `window-id` is returned.
    2. In step 2 of the tutorial, to register a target node:



    ```
    aws ssm register-target-with-maintenance-window \
                    --window-id "mw-`xxxxxxxxx`" \
                    --resource-type "INSTANCE" \
                    --target "Key=tag:Environment,Values=Prod"
    ```

    On successful completion, `WindowTargetID`s are returned.
    3. In step 3 of the tutorial, to register a task:



    ```
    aws ssm register-task-with-maintenance-window \
        --window-id "mw-`xxxxxx`" \
        --targets "Key=WindowTargetIds,Values=`63d4f63c-xxxxxx-9b1d-xxxxxfff`" \
        --task-arn "AWSManagedServices-PatchInstance" \
        --service-role-arn "arn:aws:iam::`AWS-Account-ID`:role/ams_ssm_automation_role" \
        --task-invocation-parameters "{\"Automation\":{\"DocumentVersion\":\"\$DEFAULT\",\"Parameters\":{\"InstanceId\":[\"{{`TARGET_ID`}}\"],\"StartInactiveInstances\":[\"True\"]}}}" \
        --max-concurrency 50 \
        --max-errors 50 \
        --name "AutomationExample" \
        --description "Sample Description" \
        --task-type=AUTOMATION
    ```
