

# Cancel an import snapshot task
<a name="cancel-import-task"></a>

After you start an import snapshot task using VM Import/Export, you can cancel the import operation if needed.

To describe your snapshot import tasks, see [Monitor an import snapshot task](check-status-import-task.md).

------
#### [ AWS CLI ]

**To cancel an import snapshot task**  
Use the [cancel-import-task](https://docs.aws.amazon.com/cli/latest/reference/ec2/cancel-import-task.html) command.

```
aws ec2 cancel-import-task \
    --import-task-id {{import-snap-1234567890abcdef0}}
```

------
#### [ PowerShell ]

**To cancel an import snapshot task**  
Use the [Stop-EC2ImportTask](https://docs.aws.amazon.com/powershell/latest/reference/items/Stop-EC2ImportTask.html) cmdlet.

```
Stop-EC2ImportTask `
    -ImportTaskId {{import-snap-1234567890abcdef0}}
```

------