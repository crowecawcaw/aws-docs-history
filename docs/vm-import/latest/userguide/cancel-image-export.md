# Cancel an export image task

After you start an image export using VM Import/Export, you can cancel the export operation if needed.
If you attempt to cancel the export task after it is complete or is in the process of
transferring the final disk image, the cancel operation fails and returns an error.

To describe your export image tasks, see [Monitor an export image task](monitor-image-export.md "monitor-image-export.md").

AWS CLI

###### To cancel an export image task

Use the [cancel-export-task](../../../cli/latest/reference/ec2/cancel-export-task.md "../../../cli/latest/reference/ec2/cancel-export-task.md") command. If the command succeeds, no
output is returned.

```
aws ec2 cancel-export-task \
    --export-task-id `export-ami-1234567890abcdef0`
```

PowerShell

###### To cancel an export image task

Use the [Stop-EC2ExportTask](../../../powershell/latest/reference/items/Stop-EC2ExportTask.md "../../../powershell/latest/reference/items/Stop-EC2ExportTask.md") cmdlet.

```
Stop-EC2ExportTask `
    -ExportTaskId `export-ami-1234567890abcdef0`
```
