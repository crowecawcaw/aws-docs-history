# Sharing an AWS Cloud Map namespace

 When you share an AWS Cloud Map namespace that you own with other AWS accounts
 (consumers), you enable these accounts to discover the up-to-date network locations of
 services in the namespace without the need for temporary credentials.

To share a namespace, you must add it to a resource share. A resource share is an
 AWS RAM resource that lets you share your resources across AWS accounts. A resource
 share specifies the resources to share, and the consumers with whom they are shared. To
 add the namespace to a new resource share, you must first create the resource share
 using the [AWS RAM console](https://console.aws.amazon.com/ram "https://console.aws.amazon.com/ram").

If you are part of an organization in AWS Organizations and sharing within your organization is
 enabled, consumers in your organization are automatically granted access to the shared
 namespace. Otherwise, consumers receive an invitation to join the resource share and
 are granted access to the shared namespace after accepting the invitation.

You can share a namespace that you own using the AWS RAM console or the AWS CLI.


AWS RAM console
###### To share a namespace that you own using the AWS RAM console


See [Creating
 a resource share in AWS RAM](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing-create.html "https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing-create.html") in the
 *AWS RAM User Guide*.



AWS CLI
###### To share a namespace that you own using the AWS CLI


Use the AWS RAM [create-resource-share](https://docs.aws.amazon.com/cli/latest/reference/ram/create-resource-share.html "https://docs.aws.amazon.com/cli/latest/reference/ram/create-resource-share.html") command.
