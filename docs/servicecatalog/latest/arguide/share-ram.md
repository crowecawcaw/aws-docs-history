

AWS Service Catalog AppRegistry is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Service Catalog AppRegistry availability change](https://docs.aws.amazon.com/servicecatalog/latest/arguide/app-registry-availability-change.html).

# Using AWS Resource Access Manager to share resources
<a name="share-ram"></a>

AppRegistry integrates with AWS Resource Access Manager (AWS RAM) to enable resource sharing. AWS RAM is a service that enables you to share AppRegistry applications and attribute groups with other AWS accounts or through AWS Organizations. 

With AWS RAM you share resources that you own by creating a resource share. A resource share specifies the resources to share, and the consumers with whom to share them. Consumers can include:
+ Specific AWS accounts inside or outside of its organization in AWS Organizations
+ An organizational unit inside its organization in AWS Organizations
+ Its entire organization in AWS Organizations

For more information about AWS RAM, see the [AWS RAM User Guide](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html).

**Topics**
+ [Prerequisites for sharing applications and attributes](#preq-sharing-ram)
+ [Sharing and unsharing applications or attribute groups](#share-unshare-ram)

## Prerequisites for sharing applications and attributes
<a name="preq-sharing-ram"></a>

These are the prerequisites to share applications and attributes:
+ You must own the application or attribute group in your AWS account. This means that the resource must be provisioned in your account. You cannot share an application or attribute group that has been shared with you.
+ You must have access to [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_available-policies.html) and [AWS RAM](https://docs.aws.amazon.com/ram/latest/userguide/security-iam-managed-policies.html).
+ You must enable sharing with AWS Organizations. For more information, see [Enable Sharing with AWS Organizations](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html#getting-started-sharing-orgs) in the *AWS RAM User Guide*.

## Sharing and unsharing applications or attribute groups
<a name="share-unshare-ram"></a>

This section describes how to share or unshare an AppRegistry application or attribute group with AWS RAM. 

When you share an application or attribute group using the AppRegistry console, you create a resource share. A resource share is an AWS RAM resource that lets you share your resources across AWS accounts. It specifies the resources to share, and the consumers with whom they are shared. 

You can share an application or attribute group that you own using the AppRegistry console, AWS RAM console, or the AWS CLI. 
+ To share an application or attribute group that you own using the AppRegistry console, you can either share an application or attribute group when you create it in the AppRegistry console, or you can access **Shares** for the specific application or attribute group you want to share.
+ To share an application or attribute group that you own using the AWS RAM console, see [Creating a Resource Share](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing.html#working-with-sharing-create) in the *AWS RAM User Guide*. 
+ To share an application or attribute group that you own using the AWS CLI, use the [create-resource-share](https://docs.aws.amazon.com/cli/latest/reference/ram/create-resource-share.html) command. For more information, see [AWS Resource Access Manager API Reference](https://docs.aws.amazon.com/cli/latest/reference/ram/index.html).

To unshare a shared application or attribute group that you own, you must remove it from the resource share. You can do unshare using the AppRegistry console, AWS RAM console, or AWS CLI.
+ To unshare a shared application or attribute group using the AppRegistry console, choose the application or attribute group from **Applications** or **Attribute Groups**. Then select **Shares**, and choose **Delete** for that application or attribute group.
+ To unshare a shared an application or attribute group that you own using the AWS RAM console, see [Updating a Resource Share](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing.html#working-with-sharing-update) in the *AWS RAM User Guide*.
+ To unshare a shared an application or attribute group that you own using the AWS CLI, use the [disassociate-resource-share](https://docs.aws.amazon.com/cli/latest/reference/ram/disassociate-resource-share.html) command. For more information, see [AWS Resource Access Manager API Reference](https://docs.aws.amazon.com/cli/latest/reference/ram/index.html).