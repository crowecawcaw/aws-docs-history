# Stop sharing a AWS Cloud Map namespace

When a namespace is no longer shared, the namespace and any services and instances
 associated with it can no longer be accessed by consumer AWS accounts. This includes
 resources created in the namespace by consumers when they had access to the
 namespace.

To stop sharing a namespace that you own, you must remove it from the resource share.
 You can do this using the AWS RAM console or the AWS CLI.


AWS RAM console
###### To stop sharing a namespace that you own using the AWS RAM
 console


See [Updating
 a Resource Share](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing-update.html "https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing-update.html") in the *AWS RAM User Guide*.



AWS CLI
###### To stop sharing a namespace that you own using the AWS CLI


Use the [disassociate-resource-share](https://docs.aws.amazon.com/cli/latest/reference/ram/disassociate-resource-share.html "https://docs.aws.amazon.com/cli/latest/reference/ram/disassociate-resource-share.html") command.
