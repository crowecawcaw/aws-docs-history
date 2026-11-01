

# Creating a resource share in MediaConnect
<a name="creating-endpoint-resource-share"></a>

You share a source endpoint or a destination endpoint by adding it to a resource share in AWS RAM. You can create a new resource share for the endpoint, or add the endpoint to a resource share that you already own.

## Prerequisites
<a name="creating-endpoint-resource-share-prerequisites"></a>
+ You own at least one registered source endpoint or destination endpoint.
+ You have the AWS account ID, organization Amazon Resource Name (ARN), or organizational unit ARN of each principal that you want to share with.

## Procedure
<a name="creating-endpoint-resource-share-procedure"></a><a name="create-endpoint-resource-share-procedure"></a>

**To create a resource share**

1. Open the [MediaConnect console](https://console.aws.amazon.com/mediaconnect/).

1. In the navigation pane, under **Endpoints**, choose **Source endpoints** or **Destination endpoints**.

1. Select one or more endpoints that you want to share.

1. Choose **Share**.

1. For **Sharing method**, choose one of the following:

   1. **Create a resource share** - Enter a **Resource share name**, choose a **Principal type** (**AWS account**, **Organization**, or **Organizational unit**), and enter the **Principal**.

   1. **Add to an existing resource share** - Choose an **Existing resource share**, and review **Principals that will get access**.

1. Choose **Share**.

**Note**  
A resource share holds resources from one AWS Region only. If your selection spans AWS Regions, MediaConnect creates a separate resource share for each Region, and the consuming account accepts each one separately.

When you add an endpoint to a resource share that the consuming account has already accepted, it can use the endpoint without accepting again.

## Next steps
<a name="creating-endpoint-resource-share-next-steps"></a>

After you create a resource share, you can:
+ [Accept the resource share](accepting-endpoint-resource-share.md) in the consuming account.
+ [Review the endpoints that you share](viewing-shared-endpoints.md).

## Additional resources
<a name="creating-endpoint-resource-share-additional-resources"></a>

For more information about resource shares, see the [AWS RAM User Guide](https://docs.aws.amazon.com/ram/latest/userguide/).