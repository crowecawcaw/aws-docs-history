# Dissociate principals from a

resource share and remove a resource share

The resource owner can dissociate principals from the resource share for a set
of permissions or delete the entire resource share using the AWS CLI or the AWS RAM
console. For details about how to dissociate principals from a resource share,
see [Update a
Resource Share](../../../ram/latest/userguide/working-with-sharing-update.md "../../../ram/latest/userguide/working-with-sharing-update.md") in the [AWS RAM](../../../ram/latest/userguide/what-is.md "../../../ram/latest/userguide/what-is.md") documentation. For
details about how to delete a resource share, see [Deleting a
resource share](../../../ram/latest/userguide/working-with-sharing-delete.md "../../../ram/latest/userguide/working-with-sharing-delete.md") in the [AWS RAM](../../../ram/latest/userguide/what-is.md "../../../ram/latest/userguide/what-is.md") documentation.

## AWS CLI

To dissociate principals from a resource share, use the command [dissociate-resource-share](../../../cli/latest/reference/ram/disassociate-resource-share.md "../../../cli/latest/reference/ram/disassociate-resource-share.md") as follows:

```
aws ram disassociate-resource-share --resource-share-arn `<resource-share-arn>` --principals `<principal>`
```

To delete a resource share, use the command [delete-resource-share](../../../cli/latest/reference/ram/delete-resource-share.md "../../../cli/latest/reference/ram/delete-resource-share.md") as follows:

```
aws ram delete-resource-share --resource-share-arn `<resource-share-arn>`
```

## AWS RAM console

For more details about how to dissociate principals from a resource share,
see [Update a
Resource Share](../../../ram/latest/userguide/working-with-sharing-update.md "../../../ram/latest/userguide/working-with-sharing-update.md") in the [AWS RAM](../../../ram/latest/userguide/what-is.md "../../../ram/latest/userguide/what-is.md") documentation. For
more details about how to delete a resource share, see [Deleting a resource share](../../../https:/docs.aws.amazon.com/ram/latest/userguide/working-with-sharing-delete.md "../../../https:/docs.aws.amazon.com/ram/latest/userguide/working-with-sharing-delete.md") in the [AWS RAM](../../../ram/latest/userguide/what-is.md "../../../ram/latest/userguide/what-is.md")
documentation.
