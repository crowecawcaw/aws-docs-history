# Cancel an instance export task

After you start an instance export task using VM Import/Export, you can cancel the export operation
if needed. The cancel operation removes all artifacts of the export, including any partially
created Amazon S3 objects. If the export task is complete or is in the process of transferring
the final disk image, the cancel operation fails and returns an error.

To describe your instance export tasks, see [Monitor an instance export task](vmexport-monitor.md "vmexport-monitor.md").

AWS CLI

###### To cancel an instance export task

Use the [cancel-export-task](../../../cli/latest/reference/ec2/cancel-export-task.md "../../../cli/latest/reference/ec2/cancel-export-task.md") command.

```
aws ec2 cancel-export-task \
    --export-task-id `export-i-1234567890abcdef0`
```

PowerShell

###### To cancel an instance export task

Use the [Stop-EC2ExportTask](../../../powershell/latest/reference/items/Stop-EC2ExportTask.md "../../../powershell/latest/reference/items/Stop-EC2ExportTask.md") cmdlet.

```
Stop-EC2ExportTask `
    -ExportTaskId `export-i-1234567890abcdef0`
```
