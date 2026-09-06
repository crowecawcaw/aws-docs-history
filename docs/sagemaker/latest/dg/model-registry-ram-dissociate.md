

# Dissociate principals from a resource share and remove a resource share
<a name="model-registry-ram-dissociate"></a>

The resource owner can dissociate principals from the resource share for a set of permissions or delete the entire resource share using the AWS CLI or the AWS RAM console. For details about how to dissociate principals from a resource share, see [Update a Resource Share](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing-update.html) in the [AWS RAM](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html) documentation. For details about how to delete a resource share, see [Deleting a resource share](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing-delete.html) in the [AWS RAM](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html) documentation.

## AWS CLI
<a name="model-registry-ram-dissociate-cli"></a>

To dissociate principals from a resource share, use the command [dissociate-resource-share](https://docs.aws.amazon.com/cli/latest/reference/ram/disassociate-resource-share.html) as follows:

```
aws ram disassociate-resource-share --resource-share-arn {{<resource-share-arn>}} --principals {{<principal>}}
```

To delete a resource share, use the command [delete-resource-share](https://docs.aws.amazon.com/cli/latest/reference/ram/delete-resource-share.html) as follows:

```
aws ram delete-resource-share --resource-share-arn {{<resource-share-arn>}}
```

## AWS RAM console
<a name="model-registry-ram-dissociate-ram"></a>

For more details about how to dissociate principals from a resource share, see [Update a Resource Share](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing-update.html) in the [AWS RAM](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html) documentation. For more details about how to delete a resource share, see [Deleting a resource share](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing-delete.html) in the [AWS RAM](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html) documentation.