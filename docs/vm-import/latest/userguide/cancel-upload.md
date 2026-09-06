

# Cancel an import image task
<a name="cancel-upload"></a>

After you start an image import task using VM Import/Export, you can cancel the import operation if needed.

To describe your import image tasks, see [Monitor an import image task](check-import-task-status.md).

------
#### [ AWS CLI ]

**To cancel an import image task**  
Use the [cancel-import-task](https://docs.aws.amazon.com/cli/latest/reference/ec2/cancel-import-task.html) command.

```
aws ec2 cancel-import-task \
    --import-task-id {{import-ami-1234567890abcdef0}}
```

------
#### [ PowerShell ]

**To cancel an import image task**  
Use the [Stop-EC2ImportTask](https://docs.aws.amazon.com/powershell/latest/reference/items/Stop-EC2ImportTask.html) cmdlet.

```
Stop-EC2ImportTask `
    -ImportTaskId {{import-ami-1234567890abcdef0}}
```

------