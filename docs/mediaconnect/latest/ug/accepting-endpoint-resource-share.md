

# Accepting a resource share in MediaConnect
<a name="accepting-endpoint-resource-share"></a>

You can accept a resource share invitation to use endpoints that another AWS account shares with you, or reject it to decline. Invitations appear under **Inbound shares** in the MediaConnect console.

## Prerequisites
<a name="accepting-endpoint-resource-share-prerequisites"></a>

Another AWS account has shared one or more endpoints with your account.

## Procedure
<a name="accepting-endpoint-resource-share-procedure"></a><a name="accept-endpoint-resource-share-procedure"></a>

**To accept or reject a resource share invitation**

1. Open the [MediaConnect console](https://console.aws.amazon.com/mediaconnect/).

1. In the navigation pane, under **Cross-account sharing**, choose **Inbound shares**.

1. Select a resource share with the status **Invitation pending**.

1. Choose **Accept** to use the shared endpoints, or **Reject** to decline. If you choose **Reject**, confirm by choosing **Reject** in the **Reject resource share** dialog box.

After you accept, the shared endpoints appear in your endpoint registry with **Ownership** set to **Consumed**. You can then connect a shared endpoint the same way that you connect any other endpoint.

Pending invitations expire if you don't accept or reject them. If an invitation expires or you reject it, the sharing account must send a new invitation before you can accept it.

You can also accept or reject the invitation in the AWS RAM console.

## Next steps
<a name="accepting-endpoint-resource-share-next-steps"></a>

After you accept a resource share, you can:
+ [Connect a shared endpoint](connecting-endpoints.md) to another endpoint.
+ [Review the endpoints that other accounts share with you](viewing-shared-endpoints.md).

## Additional resources
<a name="accepting-endpoint-resource-share-additional-resources"></a>

For more information about accepting resource share invitations, see the [AWS RAM User Guide](https://docs.aws.amazon.com/ram/latest/userguide/).