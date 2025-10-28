# Unshare an Image Builder resource from AWS RAM

To unshare an Image Builder resource that you own, such as a shared component, image, or recipe,
you must remove it from the AWS Resource Access Manager resource share. You can do this using the AWS RAM
console or the AWS CLI.

###### Note

Owners cannot delete a shared resource until it is no longer shared. An owner
cannot unshare these resources until none of the consumers depend on them.

###### To unshare a shared component, image, or recipe that you own using the

AWS Resource Access Manager console

See [Updating a Resource Share](../../../ram/latest/userguide/working-with-sharing.md#working-with-sharing-update "../../../ram/latest/userguide/working-with-sharing.md#working-with-sharing-update") in the _AWS RAM User Guide_.

###### To unshare a shared component, image, or recipe that you own using the

AWS CLI

Use the **[disassociate-resource-share](../../../cli/latest/reference/ram/disassociate-resource-share.md "../../../cli/latest/reference/ram/disassociate-resource-share.md")** command to stop sharing the resource.
