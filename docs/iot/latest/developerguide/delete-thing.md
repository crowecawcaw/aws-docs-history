

# Delete a thing
<a name="delete-thing"></a>

You can use the **DeleteThing** command to delete a thing:

```
$ aws iot delete-thing --thing-name "MyThing"
```

This command returns successfully with no error if the deletion is successful or you specify a thing that doesn't exist.

For more information, see [delete-thing](https://docs.aws.amazon.com/cli/latest/reference/iot/delete-thing.html) from the AWS CLI Command Reference.