# Automate application-consistent snapshots

with Data Lifecycle Manager

You can automate application-consistent snapshots with Amazon Data Lifecycle Manager by enabling pre and post scripts
in your snapshot lifecycle policies that target instances.

Amazon Data Lifecycle Manager integrates with AWS Systems Manager (Systems Manager) to support application-consistent snapshots. Amazon Data Lifecycle Manager
uses Systems Manager (SSM) command documents that include pre and post scripts to automate the
actions needed to complete application-consistent snapshots. Before Amazon Data Lifecycle Manager initiates snapshot
creation, it runs the commands in the pre script to freeze and flush I/O. After Amazon Data Lifecycle Manager
initiates snapshot creation, it runs the commands in the post script to thaw I/O.

Using Amazon Data Lifecycle Manager, you can automate application-consistent snapshots of the following:

- Windows applications using Volume Shadow Copy Service (VSS)
- SAP HANA using an AWS managed SSDM document. For more information, see
  [Amazon EBS snapshots for SAP HANA](../../../sap/latest/sap-hana/ebs-sap-hana.md "../../../sap/latest/sap-hana/ebs-sap-hana.md").
- Self-managed databases, such as MySQL, PostgreSQL or InterSystems IRIS, using SSM document templates

###### Topics

- [Requirements for using pre and post scripts](#app-consistent-prereqs "#app-consistent-prereqs")
- [Getting started with application-consistent
  snapshots](#app-consistent-get-started "#app-consistent-get-started")
- [Considerations for VSS Backups with Amazon Data Lifecycle Manager](#app-consistent-vss "#app-consistent-vss")
- [Shared responsibility for application-consistent
  snapshots](#shared-responsibility "#shared-responsibility")

## Requirements for using pre and post scripts

The following table outlines the requirements for using pre and post
scripts with Amazon Data Lifecycle Manager.

|                                                                                             | Application-consistent snapshots |                     |
| ------------------------------------------------------------------------------------------- | -------------------------------- | ------------------- | --------------- |
| Requirement                                                                                 | VSS Backup                       | Custom SSM document | Other use cases |
| SSM Agent installed and running on target instances                                         | ✓                                | ✓                   | ✓               |
| VSS system requirements met on target instances                                             | ✓                                |                     |                 |
| VSS enabled instance profile associated with target instances                               | ✓                                |                     |                 |
| VSS components installed on target instances                                                | ✓                                |                     |                 |
| Prepare SSM document with pre and post script commands                                      |                                  | ✓                   | ✓               |
| Prepare Amazon Data Lifecycle Manager IAM role run pre and post scripts                     | ✓                                | ✓                   | ✓               |
| Create snapshot policy that targets instances and<br>is configured for pre and post scripts | ✓                                | ✓                   | ✓               |

## Getting started with application-consistent

snapshots

This section explains the steps you need to follow to automate application-consistent
snapshots using Amazon Data Lifecycle Manager.

You need to prepare the targeted instances for application-consistent snapshots using Amazon Data Lifecycle Manager.
Do one of the following, depending on your use case.

Prepare for VSS Backups

###### To prepare your target instances for VSS backups

1. Install the SSM Agent on your target instances, if it is not already installed.
   If SSM Agent is already installed on your target instances, skip this step.

For more information, see [Working with SSM Agent on EC2 instances for Windows server](../../../systems-manager/latest/userguide/ssm-agent-windows.md "../../../systems-manager/latest/userguide/ssm-agent-windows.md"). 2. Ensure that the SSM Agent is running. For more information, see
[Checking SSM Agent status and starting the agent](../../../systems-manager/latest/userguide/ssm-agent-status-and-restart.md "../../../systems-manager/latest/userguide/ssm-agent-status-and-restart.md"). 3. Set up Systems Manager for Amazon EC2 instances. For more information, see [Setting up Systems Manager
for Amazon EC2 instances](../../../systems-manager/latest/userguide/systems-manager-setting-up-ec2.md "../../../systems-manager/latest/userguide/systems-manager-setting-up-ec2.md") in the _AWS Systems Manager User Guide_. 4. [Ensure the system requirements for VSS backups are met](../../../AWSEC2/latest/UserGuide/application-consistent-snapshots-prereqs.md "../../../AWSEC2/latest/UserGuide/application-consistent-snapshots-prereqs.md"). 5. [Attach a VSS-enabled instance profile to the target instances](../../../AWSEC2/latest/UserGuide/vss-iam-reqs.md "../../../AWSEC2/latest/UserGuide/vss-iam-reqs.md"). 6. [Install the VSS components](../../../AWSEC2/latest/UserGuide/application-consistent-snapshots-getting-started.md "../../../AWSEC2/latest/UserGuide/application-consistent-snapshots-getting-started.md").

Prepare for SAP HANA backups

###### To prepare your target instances for SAP HANA backups

1. Prepare the SAP HANA environment on your target instances.
   1. Set up your instance with SAP HANA. If you don't already have an existing SAP HANA environment,
      then you can refer to the [SAP HANA Environment Setup on AWS](../../../sap/latest/sap-hana/std-sap-hana-environment-setup.md "../../../sap/latest/sap-hana/std-sap-hana-environment-setup.md").
   2. Login to the SystemDB as a suitable administrator user.
   3. Create a database backup user to be used with Amazon Data Lifecycle Manager.

   ```
   CREATE USER `username` PASSWORD `password` NO FORCE_FIRST_PASSWORD_CHANGE;
   ```

   For example, the following command creates a user named `dlm_user` with password `password`.

   ```
   CREATE USER dlm_user PASSWORD password NO FORCE_FIRST_PASSWORD_CHANGE;
   ```

   4. Assign the `BACKUP OPERATOR` role to the database backup user that you created in the previous step.

   ```
   GRANT BACKUP OPERATOR TO `username`
   ```

   For example, the following command assigns the role to a user named `dlm_user`.

   ```
   GRANT BACKUP OPERATOR TO dlm_user
   ```

   5. Log in to the operating system as the administrator, for example ``sid`adm`.
   6. Create an `hdbuserstore` entry to store connection information so that the SAP HANA
      SSM document can connect to SAP HANA without users having to enter the information.

   ```
   hdbuserstore set DLM_HANADB_SNAPSHOT_USER localhost:3`hana_instance_number`13 `username` `password`
   ```

   For example:

   ```
   hdbuserstore set DLM_HANADB_SNAPSHOT_USER localhost:30013 dlm_user password
   ```

   7. Test the connection.

   ```
   hdbsql -U DLM_HANADB_SNAPSHOT_USER "select * from dummy"
   ```

2. Install the SSM Agent on your target instances, if it is not already installed.
   If SSM Agent is already installed on your target instances, skip this step.

For more information, see [Manually installing SSM Agent on EC2 instances for Linux](../../../systems-manager/latest/userguide/manually-install-ssm-agent-linux.md "../../../systems-manager/latest/userguide/manually-install-ssm-agent-linux.md"). 3. Ensure that the SSM Agent is running. For more information, see
[Checking SSM Agent status and starting the agent](../../../systems-manager/latest/userguide/ssm-agent-status-and-restart.md "../../../systems-manager/latest/userguide/ssm-agent-status-and-restart.md"). 4. Set up Systems Manager for Amazon EC2 instances. For more information, see [Setting up Systems Manager
for Amazon EC2 instances](../../../systems-manager/latest/userguide/systems-manager-setting-up-ec2.md "../../../systems-manager/latest/userguide/systems-manager-setting-up-ec2.md") in the _AWS Systems Manager User Guide_.

Prepare for custom SSM documents

###### To prepare your target instances custom SSM documents

1. Install the SSM Agent on your target instances, if it is not already installed.
   If SSM Agent is already installed on your target instances, skip this step.
   - (Linux instances) [Manually installing SSM Agent on EC2 instances for Linux](../../../systems-manager/latest/userguide/manually-install-ssm-agent-linux.md "../../../systems-manager/latest/userguide/manually-install-ssm-agent-linux.md")
   - (Windows instances) [Working with SSM Agent on EC2 instances for Windows Server](../../../systems-manager/latest/userguide/ssm-agent-windows.md "../../../systems-manager/latest/userguide/ssm-agent-windows.md")

2. Ensure that the SSM Agent is running. For more information, see
   [Checking SSM Agent status and starting the agent](../../../systems-manager/latest/userguide/ssm-agent-status-and-restart.md "../../../systems-manager/latest/userguide/ssm-agent-status-and-restart.md").
3. Set up Systems Manager for Amazon EC2 instances. For more information, see [Setting up Systems Manager
   for Amazon EC2 instances](../../../systems-manager/latest/userguide/systems-manager-setting-up-ec2.md "../../../systems-manager/latest/userguide/systems-manager-setting-up-ec2.md") in the _AWS Systems Manager User Guide_.

###### Note

This step is required only for custom SSM documents. It is not required for VSS
Backup or SAP HANA. For VSS Backups and SAP HANA, Amazon Data Lifecycle Manager uses the AWS managed SSM
document.

If you are automating application-consistent snapshots for a self-managed database,
such as MySQL, PostgreSQL, or InterSystems IRIS, you must create an SSM command document
that includes a pre script to freeze and flush I/O before snapshot creation is initiated,
and a post script to thaw I/O after snapshot creation is initiated.

If your MySQL, PostgreSQL, or InterSystems IRIS database uses standard configurations,
you can create an SSM command document using the sample SSM document content below. If
your MySQL, PostgreSQL, or InterSystems IRIS database uses a non-standard configuration,
you can use the sample content below as a starting point for your SSM command document
and then customize it to meet your requirements. Alternatively, if you want to create a
new SSM document from scratch, you can use the empty SSM document template below and add
your pre and post commands in the appropriate document sections.

###### Note the following:

- It is your responsibility to ensure that the SSM document performs the
  correct and required actions for your database configuration.
- Snapshots are guaranteed to be application-consistent only if the pre
  and post scripts in your SSM document can successfully freeze, flush, and
  thaw I/O.
- The SSM document must include required fields for `allowedValues`,
  including `pre-script`, `post-script`, and
  `dry-run`. Amazon Data Lifecycle Manager will execute commands on your instance based on
  the contents of those sections. If your SSM document does not have those
  sections, then Amazon Data Lifecycle Manager will treat it as a failed execution.

MySQL sample document content

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
description: Amazon Data Lifecycle Manager Pre/Post script for MySQL databases
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
  description: Run MySQL Database freeze/thaw commands
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

      ###=================================================================###
      ### Global variables
      ###=================================================================###
      START=$(date +%s)
      # For testing this script locally, replace the below with OPERATION=$1.
      OPERATION={{ command }}
      FS_ALREADY_FROZEN_ERROR='freeze failed: Device or resource busy'
      FS_ALREADY_THAWED_ERROR='unfreeze failed: Invalid argument'
      FS_BUSY_ERROR='mount point is busy'

      # Auto thaw is a fail safe mechanism to automatically unfreeze the application after the
      # duration specified in the global variable below. Choose the duration based on your
      # database application's tolerance to freeze.
      export AUTO_THAW_DURATION_SECS="60"

      # Add all pre-script actions to be performed within the function below
      execute_pre_script() {
          echo "INFO: Start execution of pre-script"
          # Check if filesystem is already frozen. No error code indicates that filesystem
          # is not currently frozen and that the pre-script can proceed with freezing the filesystem.
          check_fs_freeze
          # Execute the DB commands to flush the DB in preparation for snapshot
          snap_db
          # Freeze the filesystem. No error code indicates that filesystem was succefully frozen
          freeze_fs

          echo "INFO: Schedule Auto Thaw to execute in ${AUTO_THAW_DURATION_SECS} seconds."
          $(nohup bash -c execute_schedule_auto_thaw  >/dev/null 2>&1 &)
      }

      # Add all post-script actions to be performed within the function below
      execute_post_script() {
          echo "INFO: Start execution of post-script"
          # Unfreeze the filesystem. No error code indicates that filesystem was successfully unfrozen.
          unfreeze_fs
          thaw_db
      }

      # Execute Auto Thaw to automatically unfreeze the application after the duration configured
      # in the AUTO_THAW_DURATION_SECS global variable.
      execute_schedule_auto_thaw() {
          sleep ${AUTO_THAW_DURATION_SECS}
          execute_post_script
      }

      # Disable Auto Thaw if it is still enabled
      execute_disable_auto_thaw() {
          echo "INFO: Attempting to disable auto thaw if enabled"
          auto_thaw_pgid=$(pgrep -f execute_schedule_auto_thaw | xargs -i ps -hp {} -o pgid)
          if [ -n "${auto_thaw_pgid}" ]; then
              echo "INFO: execute_schedule_auto_thaw process found with pgid ${auto_thaw_pgid}"
              sudo pkill -g ${auto_thaw_pgid}
              rc=$?
              if [ ${rc} != 0 ]; then
                  echo "ERROR: Unable to kill execute_schedule_auto_thaw process. retval=${rc}"
              else
                  echo "INFO: Auto Thaw  has been disabled"
              fi
          fi
      }

      # Iterate over all the mountpoints and check if filesystem is already in freeze state.
      # Return error code 204 if any of the mount points are already frozen.
      check_fs_freeze() {
          for target in $(lsblk -nlo MOUNTPOINTS)
          do
              # Freeze of the root and boot filesystems is dangerous and pre-script does not freeze these filesystems.
              # Hence, we will skip the root and boot mountpoints while checking if filesystem is in freeze state.
              if [ $target == '/' ]; then continue; fi
              if [[ "$target" == *"/boot"* ]]; then continue; fi

              error_message=$(sudo mount -o remount,noatime $target 2>&1)
              # Remount will be a no-op without a error message if the filesystem is unfrozen.
              # However, if filesystem is already frozen, remount will fail with busy error message.
              if [ $? -ne 0 ];then
                  # If the filesystem is already in frozen, return error code 204
                  if [[ "$error_message" == *"$FS_BUSY_ERROR"* ]];then
                      echo "ERROR: Filesystem ${target} already frozen. Return Error Code: 204"
                      exit 204
                  fi
                  # If the check filesystem freeze failed due to any reason other than the filesystem already frozen, return 201
                  echo "ERROR: Failed to check_fs_freeze on mountpoint $target due to error - $errormessage"
                  exit 201
              fi
          done
      }

      # Iterate over all the mountpoints and freeze the filesystem.
      freeze_fs() {
          for target in $(lsblk -nlo MOUNTPOINTS)
          do
              # Freeze of the root and boot filesystems is dangerous. Hence, skip filesystem freeze
              # operations for root and boot mountpoints.
              if [ $target == '/' ]; then continue; fi
              if [[ "$target" == *"/boot"* ]]; then continue; fi
              echo "INFO: Freezing $target"
              error_message=$(sudo fsfreeze -f $target 2>&1)
              if [ $? -ne 0 ];then
                  # If the filesystem is already in frozen, return error code 204
                  if [[ "$error_message" == *"$FS_ALREADY_FROZEN_ERROR"* ]]; then
                      echo "ERROR: Filesystem ${target} already frozen. Return Error Code: 204"
                      sudo mysql -e 'UNLOCK TABLES;'
                      exit 204
                  fi
                  # If the filesystem freeze failed due to any reason other than the filesystem already frozen, return 201
                  echo "ERROR: Failed to freeze mountpoint $targetdue due to error - $errormessage"
                  thaw_db
                  exit 201
              fi
              echo "INFO: Freezing complete on $target"
          done
      }

      # Iterate over all the mountpoints and unfreeze the filesystem.
      unfreeze_fs() {
          for target in $(lsblk -nlo MOUNTPOINTS)
          do
              # Freeze of the root and boot filesystems is dangerous and pre-script does not freeze these filesystems.
              # Hence, will skip the root and boot mountpoints during unfreeze as well.
              if [ $target == '/' ]; then continue; fi
              if [[ "$target" == *"/boot"* ]]; then continue; fi
              echo "INFO: Thawing $target"
              error_message=$(sudo fsfreeze -u $target 2>&1)
              # Check if filesystem is already unfrozen (thawed). Return error code 204 if filesystem is already unfrozen.
              if [ $? -ne 0 ]; then
                  if [[ "$error_message" == *"$FS_ALREADY_THAWED_ERROR"* ]]; then
                      echo "ERROR: Filesystem ${target} is already in thaw state. Return Error Code: 205"
                      exit 205
                  fi
                  # If the filesystem unfreeze failed due to any reason other than the filesystem already unfrozen, return 202
                  echo "ERROR: Failed to unfreeze mountpoint $targetdue due to error - $errormessage"
                  exit 202
              fi
              echo "INFO: Thaw complete on $target"
          done
      }

      snap_db() {
          # Run the flush command only when MySQL DB service is up and running
          sudo systemctl is-active --quiet mysqld.service
          if [ $? -eq 0 ]; then
              echo "INFO: Execute MySQL Flush and Lock command."
              sudo mysql -e 'FLUSH TABLES WITH READ LOCK;'
              # If the MySQL Flush and Lock command did not succeed, return error code 201 to indicate pre-script failure
              if [ $? -ne 0 ]; then
                  echo "ERROR: MySQL FLUSH TABLES WITH READ LOCK command failed."
                  exit 201
              fi
              sync
          else
              echo "INFO: MySQL service is inactive. Skipping execution of MySQL Flush and Lock command."
          fi
      }

      thaw_db() {
          # Run the unlock command only when MySQL DB service is up and running
          sudo systemctl is-active --quiet mysqld.service
          if [ $? -eq 0 ]; then
              echo "INFO: Execute MySQL Unlock"
              sudo mysql -e 'UNLOCK TABLES;'
          else
              echo "INFO: MySQL service is inactive. Skipping execution of MySQL Unlock command."
          fi
      }

      export -f execute_schedule_auto_thaw
      export -f execute_post_script
      export -f unfreeze_fs
      export -f thaw_db

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
              execute_disable_auto_thaw
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

PostgreSQL sample document content

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
description: Amazon Data Lifecycle Manager Pre/Post script for PostgreSQL databases
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
  description: Run PostgreSQL Database freeze/thaw commands
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
      OPERATION={{ command }}
      FS_ALREADY_FROZEN_ERROR='freeze failed: Device or resource busy'
      FS_ALREADY_THAWED_ERROR='unfreeze failed: Invalid argument'
      FS_BUSY_ERROR='mount point is busy'

      # Auto thaw is a fail safe mechanism to automatically unfreeze the application after the
      # duration specified in the global variable below. Choose the duration based on your
      # database application's tolerance to freeze.
      export AUTO_THAW_DURATION_SECS="60"

      # Add all pre-script actions to be performed within the function below
      execute_pre_script() {
          echo "INFO: Start execution of pre-script"
          # Check if filesystem is already frozen. No error code indicates that filesystem
          # is not currently frozen and that the pre-script can proceed with freezing the filesystem.
          check_fs_freeze
          # Execute the DB commands to flush the DB in preparation for snapshot
          snap_db
          # Freeze the filesystem. No error code indicates that filesystem was succefully frozen
          freeze_fs

          echo "INFO: Schedule Auto Thaw to execute in ${AUTO_THAW_DURATION_SECS} seconds."
          $(nohup bash -c execute_schedule_auto_thaw  >/dev/null 2>&1 &)
      }

      # Add all post-script actions to be performed within the function below
      execute_post_script() {
          echo "INFO: Start execution of post-script"
          # Unfreeze the filesystem. No error code indicates that filesystem was successfully unfrozen
          unfreeze_fs
      }

      # Execute Auto Thaw to automatically unfreeze the application after the duration configured
      # in the AUTO_THAW_DURATION_SECS global variable.
      execute_schedule_auto_thaw() {
          sleep ${AUTO_THAW_DURATION_SECS}
          execute_post_script
      }

      # Disable Auto Thaw if it is still enabled
      execute_disable_auto_thaw() {
          echo "INFO: Attempting to disable auto thaw if enabled"
          auto_thaw_pgid=$(pgrep -f execute_schedule_auto_thaw | xargs -i ps -hp {} -o pgid)
          if [ -n "${auto_thaw_pgid}" ]; then
              echo "INFO: execute_schedule_auto_thaw process found with pgid ${auto_thaw_pgid}"
              sudo pkill -g ${auto_thaw_pgid}
              rc=$?
              if [ ${rc} != 0 ]; then
                  echo "ERROR: Unable to kill execute_schedule_auto_thaw process. retval=${rc}"
              else
                  echo "INFO: Auto Thaw  has been disabled"
              fi
          fi
      }

      # Iterate over all the mountpoints and check if filesystem is already in freeze state.
      # Return error code 204 if any of the mount points are already frozen.
      check_fs_freeze() {
          for target in $(lsblk -nlo MOUNTPOINTS)
          do
              # Freeze of the root and boot filesystems is dangerous and pre-script does not freeze these filesystems.
              # Hence, we will skip the root and boot mountpoints while checking if filesystem is in freeze state.
              if [ $target == '/' ]; then continue; fi
              if [[ "$target" == *"/boot"* ]]; then continue; fi

              error_message=$(sudo mount -o remount,noatime $target 2>&1)
              # Remount will be a no-op without a error message if the filesystem is unfrozen.
              # However, if filesystem is already frozen, remount will fail with busy error message.
              if [ $? -ne 0 ];then
                  # If the filesystem is already in frozen, return error code 204
                  if [[ "$error_message" == *"$FS_BUSY_ERROR"* ]];then
                      echo "ERROR: Filesystem ${target} already frozen. Return Error Code: 204"
                      exit 204
                  fi
                  # If the check filesystem freeze failed due to any reason other than the filesystem already frozen, return 201
                  echo "ERROR: Failed to check_fs_freeze on mountpoint $target due to error - $errormessage"
                  exit 201
              fi
          done
      }

      # Iterate over all the mountpoints and freeze the filesystem.
      freeze_fs() {
          for target in $(lsblk -nlo MOUNTPOINTS)
          do
              # Freeze of the root and boot filesystems is dangerous. Hence, skip filesystem freeze
              # operations for root and boot mountpoints.
              if [ $target == '/' ]; then continue; fi
              if [[ "$target" == *"/boot"* ]]; then continue; fi
              echo "INFO: Freezing $target"
              error_message=$(sudo fsfreeze -f $target 2>&1)
              if [ $? -ne 0 ];then
                  # If the filesystem is already in frozen, return error code 204
                  if [[ "$error_message" == *"$FS_ALREADY_FROZEN_ERROR"* ]]; then
                      echo "ERROR: Filesystem ${target} already frozen. Return Error Code: 204"
                      exit 204
                  fi
                  # If the filesystem freeze failed due to any reason other than the filesystem already frozen, return 201
                  echo "ERROR: Failed to freeze mountpoint $targetdue due to error - $errormessage"
                  exit 201
              fi
              echo "INFO: Freezing complete on $target"
          done
      }

      # Iterate over all the mountpoints and unfreeze the filesystem.
      unfreeze_fs() {
          for target in $(lsblk -nlo MOUNTPOINTS)
          do
              # Freeze of the root and boot filesystems is dangerous and pre-script does not freeze these filesystems.
              # Hence, will skip the root and boot mountpoints during unfreeze as well.
              if [ $target == '/' ]; then continue; fi
              if [[ "$target" == *"/boot"* ]]; then continue; fi
              echo "INFO: Thawing $target"
              error_message=$(sudo fsfreeze -u $target 2>&1)
              # Check if filesystem is already unfrozen (thawed). Return error code 204 if filesystem is already unfrozen.
              if [ $? -ne 0 ]; then
                  if [[ "$error_message" == *"$FS_ALREADY_THAWED_ERROR"* ]]; then
                      echo "ERROR: Filesystem ${target} is already in thaw state. Return Error Code: 205"
                      exit 205
                  fi
                  # If the filesystem unfreeze failed due to any reason other than the filesystem already unfrozen, return 202
                  echo "ERROR: Failed to unfreeze mountpoint $targetdue due to error - $errormessage"
                  exit 202
              fi
              echo "INFO: Thaw complete on $target"
          done
      }

      snap_db() {
          # Run the flush command only when PostgreSQL DB service is up and running
          sudo systemctl is-active --quiet postgresql
          if [ $? -eq 0 ]; then
              echo "INFO: Execute Postgres CHECKPOINT"
              # PostgreSQL command to flush the transactions in memory to disk
              sudo -u postgres psql -c 'CHECKPOINT;'
              # If the PostgreSQL Command did not succeed, return error code 201 to indicate pre-script failure
              if [ $? -ne 0 ]; then
                  echo "ERROR: Postgres CHECKPOINT command failed."
                  exit 201
              fi
              sync
          else
              echo "INFO: PostgreSQL service is inactive. Skipping execution of CHECKPOINT command."
          fi
      }

      export -f execute_schedule_auto_thaw
      export -f execute_post_script
      export -f unfreeze_fs

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
              execute_disable_auto_thaw
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

InterSystems IRIS sample document content

```
###===============================================================================###
# MIT License
#
# Copyright (c) 2024 InterSystems
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
###===============================================================================###
schemaVersion: '2.2'
description: SSM Document Template for Amazon Data Lifecycle Manager Pre/Post script feature for InterSystems IRIS.
parameters:
  executionId:
    type: String
    default: None
    description: Specifies the unique identifier associated with a pre and/or post execution
    allowedPattern: ^(None|[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12})$
  command:
    type: String
    # Data Lifecycle Manager will trigger the pre-script and post-script actions. You can also use this SSM document with 'dry-run' for manual testing purposes.
    default: 'dry-run'
    description: (Required) Specifies whether pre-script and/or post-script should be executed.
    #The following allowedValues will allow Data Lifecycle Manager to successfully trigger pre and post script actions.
    allowedValues:
    - pre-script
    - post-script
    - dry-run

mainSteps:
- action: aws:runShellScript
  description: Run InterSystems IRIS Database freeze/thaw commands
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
      ### Global variables
      ###===============================================================================###
      DOCKER_NAME=iris
      LOGDIR=./
      EXIT_CODE=0
      OPERATION={{ command }}
      START=$(date +%s)

      # Check if Docker is installed
      # By default if Docker is present, script assumes that InterSystems IRIS is running in Docker
      # Leave only the else block DOCKER_EXEC line, if you run InterSystems IRIS non-containerised (and Docker is present).
      # Script assumes irissys user has OS auth enabled, change the OS user or supply login/password depending on your configuration.
      if command -v docker &> /dev/null
      then
        DOCKER_EXEC="docker exec $DOCKER_NAME"
      else
        DOCKER_EXEC="sudo -i -u irissys"
      fi


      # Add all pre-script actions to be performed within the function below
      execute_pre_script() {
        echo "INFO: Start execution of pre-script"

        # find all iris running instances
        iris_instances=$($DOCKER_EXEC iris qall 2>/dev/null | tail -n +3 | grep '^up' | cut -c5-  | awk '{print $1}')
        echo "`date`: Running iris instances $iris_instances"

        # Only for running instances
        for INST in $iris_instances; do

          echo "`date`: Attempting to freeze $INST"

          # Detailed instances specific log
          LOGFILE=$LOGDIR/$INST-pre_post.log

          #check Freeze status before starting
          $DOCKER_EXEC irissession $INST -U '%SYS' "##Class(Backup.General).IsWDSuspendedExt()"
          freeze_status=$?
          if [ $freeze_status -eq 5 ]; then
            echo "`date`:   ERROR: $INST IS already FROZEN"
            EXIT_CODE=204
          else
            echo "`date`:   $INST is not frozen"
            # Freeze
            # Docs: https://docs.intersystems.com/irislatest/csp/documatic/%25CSP.Documatic.cls?LIBRARY=%25SYS&CLASSNAME=Backup.General#ExternalFreeze
            $DOCKER_EXEC irissession $INST -U '%SYS' "##Class(Backup.General).ExternalFreeze(\"$LOGFILE\",,,,,,600,,,300)"
            status=$?

            case $status in
              5) echo "`date`:   $INST IS FROZEN"
                ;;
              3) echo "`date`:   $INST FREEZE FAILED"
                EXIT_CODE=201
                ;;
              *) echo "`date`:   ERROR: Unknown status code: $status"
                EXIT_CODE=201
                ;;
            esac
            echo "`date`:   Completed freeze of $INST"
          fi
        done
        echo "`date`: Pre freeze script finished"
      }

      # Add all post-script actions to be performed within the function below
      execute_post_script() {
        echo "INFO: Start execution of post-script"

        # find all iris running instances
        iris_instances=$($DOCKER_EXEC iris qall 2>/dev/null | tail -n +3 | grep '^up' | cut -c5-  | awk '{print $1}')
        echo "`date`: Running iris instances $iris_instances"

        # Only for running instances
        for INST in $iris_instances; do

          echo "`date`: Attempting to thaw $INST"

          # Detailed instances specific log
          LOGFILE=$LOGDIR/$INST-pre_post.log

          #check Freeze status befor starting
          $DOCKER_EXEC irissession $INST -U '%SYS' "##Class(Backup.General).IsWDSuspendedExt()"
          freeze_status=$?
          if [ $freeze_status -eq 5 ]; then
            echo "`date`:  $INST is in frozen state"
            # Thaw
            # Docs: https://docs.intersystems.com/irislatest/csp/documatic/%25CSP.Documatic.cls?LIBRARY=%25SYS&CLASSNAME=Backup.General#ExternalFreeze
            $DOCKER_EXEC irissession $INST -U%SYS "##Class(Backup.General).ExternalThaw(\"$LOGFILE\")"
            status=$?

            case $status in
              5) echo "`date`:   $INST IS THAWED"
                  $DOCKER_EXEC irissession $INST -U%SYS "##Class(Backup.General).ExternalSetHistory(\"$LOGFILE\")"
                ;;
              3) echo "`date`:   $INST THAW FAILED"
                  EXIT_CODE=202
                ;;
              *) echo "`date`:   ERROR: Unknown status code: $status"
                  EXIT_CODE=202
                ;;
            esac
            echo "`date`:   Completed thaw of $INST"
          else
            echo "`date`:   ERROR: $INST IS already THAWED"
            EXIT_CODE=205
          fi
        done
        echo "`date`: Post thaw script finished"
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
          # return failure
          EXIT_CODE=1
          ;;
      esac

      END=$(date +%s)
      # Debug Log for profiling the script time
      echo "INFO: ${OPERATION} completed at $(date). Total runtime: $((${END} - ${START})) seconds."
      exit $EXIT_CODE
```

For more information, see the [GitHub repository](https://github.com/intersystems-community/aws/blob/master/README.md "https://github.com/intersystems-community/aws/blob/master/README.md").

Empty document template

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

Once you have your SSM document content, use one of the following procedures to create the custom
SSM document.

Console

###### To create the SSM command document

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com//systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Documents**, then choose
   **Create document**, **Command or Session**.
3. For **Name**, enter a descriptive name for the document.
4. For **Target type**, select **/AWS::EC2::Instance**.
5. For **Document type**, select **Command**.
6. In the **Content** field, select **YAML** and then
   paste the document content.
7. In the **Document tags** section, add a tag with a tag key of
   `DLMScriptsAccess`, and a tag value of `true`.

###### Important

The `DLMScriptsAccess:true` tag is required by the
**AWSDataLifecycleManagerSSMFullAccess** AWS
managed policy used in _Step 3: Prepare Amazon Data Lifecycle Manager IAM role_.
The policy uses the `aws:ResourceTag` condition key to restrict
access to SSM documents that have this tag. 8. Choose **Create document**.

AWS CLI

###### To create the SSM command document

Use the [create-document](../../../cli/latest/reference/ssm/create-document.md "../../../cli/latest/reference/ssm/create-document.md") command. For `--name`, specify a descriptive name for
the document. For `--document-type`, specify `Command`. For
`--content`, specify the path to the .yaml file with the SSM document content.
For `--tags`, specify `"Key=DLMScriptsAccess,Value=true"`.

```
`$` aws ssm create-document \
--content file:`//path/to/file/documentContent.yaml` \
--name "`document_name`" \
--document-type "Command" \
--document-format YAML \
--tags "Key=DLMScriptsAccess,Value=true"
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

You must ensure that the IAM role that you use for policy grants Amazon Data Lifecycle Manager permission to
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
include that condition key, then you do not need to tag your SSM documents with
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

To automate application-consistent snapshots, you must create a snapshot lifecycle
policy that targets instances, and configure pre and post scripts for that policy.

Console

###### To create the snapshot lifecycle policy

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

5. For **IAM role**, either choose **AWSDataLifecycleManagerDefaultRole** (the default role for managing
   snapshots), or choose a custom role that you created and prepared for pre and post
   scripts.
6. Configure the schedules and additional options as needed. We recommend that you
   schedule snapshot creation times for time periods that match your workload, such as
   during maintenance windows.

For SAP HANA, we recommend that you enable fast snapshot restore.

###### Note

If you enable a schedule for VSS Backups, you can't enable **Exclude
specific data volumes** or **Copy tags from source**. 7. In the **Pre and post scripts** section, select **Enable
pre and post scripts**, and then do the following, depending on your
workload:

    * To create application-consistent snapshots of your Windows applications,
     select **VSS Backup**.
    * To create application-consistent snapshots of your SAP HANA workloads, select
     **SAP HANA**.
    * To create application-consistent snapshots of all other databases and workloads,
     including your self-managed MySQL, PostgreSQL, or InterSystems IRIS databases, using
     a custom SSM document, select **Custom SSM document**.




    	1. For **Automate option**, choose **Pre and post
    	 scripts**.
    	2. For **SSM document**, select the SSM document that you
    	 prepared.

8. Depending on the option you selected, configure the following additional options:
   - **Script timeout** — (_Custom SSM document only_) The
     timeout period after which Amazon Data Lifecycle Manager fails the script run attempt if it has not completed. If a script
     does not complete within its timeout period, Amazon Data Lifecycle Manager fails the attempt. The timeout period applies
     to the pre and post scripts individually. The minimum and default timeout period is 10 seconds. And
     the maximum timeout period is 120 seconds.
   - **Retry failed scripts** — Select this option to retry scripts that do
     not complete within their timeout period. If the pre script fails, Amazon Data Lifecycle Manager retries entire snapshot
     creation process, including running the pre and post scripts. If the post script fails, Amazon Data Lifecycle Manager
     retries the post script only; in this case, the pre script will have completed and the snapshot
     might have been created.
   - **Default to crash-consistent snapshots** — Select this option to default
     to crash-consistent snapshots if the pre script fails to run. This is the default snapshot creation
     behavior for Amazon Data Lifecycle Manager if pre and post scripts is not enabled. If you enabled retries, Amazon Data Lifecycle Manager will
     default to crash-consistent snapshots only after all retry attempts have been exhausted. If the pre
     script fails and you do not default to crash-consistent snapshots, Amazon Data Lifecycle Manager will not create snapshots
     for the instance during that schedule run.

   ###### Note

   If you are creating snapshots for SAP HANA, then you might want to disabled this option.
   Crash-consistent snapshots of SAP HANA workloads can't restored in the same manner.

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

Where `policyDetails.json` includes one of the following,
depending on your use case:

- **VSS Backup**

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
                "ExecutionHandler":"AWS_VSS_BACKUP",
                "ExecuteOperationOnScriptFailure":`true|false`,
                "MaximumRetryCount":`retries (0-3)`
            }]
        },
        "RetainRule": {
            "Count": `retention_count`
        }
    }]
}
```

- **SAP HANA backups**

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
                "Stages": ["PRE","POST"],
                "ExecutionHandlerService":"AWS_SYSTEMS_MANAGER",
                "ExecutionHandler":"AWSSystemsManagerSAP-CreateDLMSnapshotForSAPHANA",
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

- **Custom SSM document**

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
                "Stages": ["PRE","POST"],
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

## Considerations for VSS Backups with Amazon Data Lifecycle Manager

With Amazon Data Lifecycle Manager, you can back up and restore VSS (Volume Shadow Copy Service)-enabled
Windows applications running on Amazon EC2 instances. If the application has a VSS writer
registered with Windows VSS, then Amazon Data Lifecycle Manager creates a snapshot that will be application-consistent for that application.

###### Note

Amazon Data Lifecycle Manager currently supports application-consistent snapshots of resources running
on Amazon EC2 only, specifically for backup scenarios where application data can be
restored by replacing an existing instance with a new instance created from the
backup. Not all instance types or applications are supported for VSS backups.
For more information, see [Application-consistent Windows VSS snapshots](../../../AWSEC2/latest/UserGuide/application-consistent-snapshots.md "../../../AWSEC2/latest/UserGuide/application-consistent-snapshots.md") in the
_Amazon EC2 User Guide_.

###### Unsupported instance types

The following Amazon EC2 instance types are not supported for VSS backups. If
your policy targets one of these instance types, Amazon Data Lifecycle Manager might still create VSS
backups, but the snapshots might not be tagged with the required system tags.
Without these tags, the snapshots will not be managed by Amazon Data Lifecycle Manager after creation.
You might need to manually delete these snapshots.

- T3: `t3.nano` | `t3.micro`
- T3a: `t3a.nano` | `t3a.micro`
- T2: `t2.nano` | `t2.micro`

## Shared responsibility for application-consistent

snapshots

###### You must ensure that:

- The SSM Agent is installed, up-to-date, and running on your target instances
- Systems Manager has permissions to perform the required actions on the target instances
- Amazon Data Lifecycle Manager has permissions to perform the Systems Manager actions required to run pre and
  post scripts on the target instances.
- For custom workloads, such as self-managed MySQL, PostgreSQL, or InterSystems
  IRIS databases, the SSM document that you use includes the correct and required
  actions for freezing, flushing, and thawing I/O for your database configuration.
- Snapshot creation times align with your workload schedule. For example, try to
  schedule snapshot creation during scheduled maintenance windows.

###### Amazon Data Lifecycle Manager ensures that:

- Snapshot creation is initiated within 60 minutes of the scheduled snapshot
  creation time.
- Pre scripts run before the snapshot creation is initiated.
- Post scripts run after the pre script succeeds and the snapshot creation has
  been initiated. Amazon Data Lifecycle Manager runs the post script only if the pre script succeeds.
  If the pre script fails, Amazon Data Lifecycle Manager will not run the post script.
- Snapshots are tagged with the appropriate tags on creation.
- CloudWatch metrics and events are emitted when scripts are initiated, and when they
  fail or succeed.
