

# Viewing shared endpoints in MediaConnect
<a name="viewing-shared-endpoints"></a>

You can review endpoint sharing in three places in the MediaConnect console. **Outbound shares** lists the resource shares that your account owns, **Inbound shares** lists the resource shares that other accounts share with your account, and each endpoint's details page shows how that endpoint is shared.

## Prerequisites
<a name="viewing-shared-endpoints-prerequisites"></a>

You own a resource share, or another AWS account has shared one or more endpoints with your account.

## Procedure
<a name="viewing-shared-endpoints-procedure"></a><a name="view-outbound-shares-procedure"></a>

**To view the resource shares that your account owns**

1. Open the [MediaConnect console](https://console.aws.amazon.com/mediaconnect/).

1. In the navigation pane, under **Cross-account sharing**, choose **Outbound shares**.

1. Review the resource shares that you own. Each resource share shows the endpoints that you share and the accounts that you share them with.<a name="view-inbound-shares-procedure"></a>

**To view the resource shares that other accounts share with your account**

1. Open the [MediaConnect console](https://console.aws.amazon.com/mediaconnect/).

1. In the navigation pane, under **Cross-account sharing**, choose **Inbound shares**.

1. Review the resource shares that other accounts share with your account.<a name="view-endpoint-sharing-procedure"></a>

**To view how an endpoint is shared**

1. Open the [MediaConnect console](https://console.aws.amazon.com/mediaconnect/).

1. In the navigation pane, under **Endpoints**, choose **Source endpoints** or **Destination endpoints**.

1. Choose an endpoint to open its details page.

1. On the **Monitoring** tab, review the **Resource sharing** panel. It shows how the endpoint is shared and which account owns it.

## Next steps
<a name="viewing-shared-endpoints-next-steps"></a>

After you review your shared endpoints, you can:
+ [Connect a shared endpoint](connecting-endpoints.md) to another endpoint.
+ [Stop sharing an endpoint](stopping-endpoint-sharing.md) that you own.

## Additional resources
<a name="viewing-shared-endpoints-additional-resources"></a>

For more information about viewing resource shares, see the [AWS RAM User Guide](https://docs.aws.amazon.com/ram/latest/userguide/).