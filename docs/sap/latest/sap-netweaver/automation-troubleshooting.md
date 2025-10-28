# Automation troubleshooting

If you encounter errors related to SAP automation, refer to the [Troubleshooting Systems Manager Automation](../../../systems-manager/latest/userguide/automation-troubleshooting.md "../../../systems-manager/latest/userguide/automation-troubleshooting.md") documentation in the _AWS Systems Manager User Guide_. There, you will find an action-specific failures reference as well as information about common errors such as access denied errors and errors related to timed out or failed statuses after the execution started.

## Logging installation steps

You can log individual automated installation steps with the code below. In this example, logs are added to `$SSM_LOG_FILE` for each `run` command.

```
action: "aws:runShellScript"
name: "Validate_Installation"
inputs:
runCommand:
- #!/bin/bash
- sid=echo {{ Sid }} | tr '[:upper:]' '[:lower:]'}``
- SID=echo {{ Sid }} | tr '[:lower:]' '[:upper:]'}``
- HOSTNAME=hostname``
- SIDADM=${sid}adm
- su - $SIDADM -c "stopsap $HOSTNAME" | tee -a $SSM_LOG_FILE
- su - $SIDADM -c "startsap $HOSTNAME" | tee -a $SSM_LOG_FILE
- sleep 15
- _SAP_UP=$(netstat -an | grep 3200 | grep tcp | grep LISTEN | wc -l )
- echo "This is the value of SAP_UP - $_SAP_UP" | tee -a $SSM_LOG_FILE
- if [ "$_SAP_UP" -eq 1 ]
- then
-   echo "$(date) __ done installing ASCS." | tee -a $SSM_LOG_FILE
-   exit 0
- else
-   echo "$(date) __ ASCS could not be installed successfully. Fix the issue and rerun the automation" | tee -a $SSM_LOG_FILE
-   exit 1
- fi
```
