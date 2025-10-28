# Cancel an import snapshot task

After you start an import snapshot task using VM Import/Export, you can cancel the import
operation if needed.

To describe your snapshot import tasks, see [Monitor an import snapshot task](check-status-import-task.md "check-status-import-task.md").

AWS CLI

###### To cancel an import snapshot task

Use the [cancel-import-task](../../../cli/latest/reference/ec2/cancel-import-task.md "../../../cli/latest/reference/ec2/cancel-import-task.md") command.

```
aws ec2 cancel-import-task \
    --import-task-id `import-snap-1234567890abcdef0`
```

PowerShell

###### To cancel an import snapshot task

Use the [Stop-EC2ImportTask](../../../powershell/latest/reference/items/Stop-EC2ImportTask.md "../../../powershell/latest/reference/items/Stop-EC2ImportTask.md") cmdlet.

```
Stop-EC2ImportTask `
    -ImportTaskId `import-snap-1234567890abcdef0`
```
