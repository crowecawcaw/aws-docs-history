

# Understand distribution origins in Amazon Lightsail
<a name="amazon-lightsail-distribution-origins"></a>

<a name="distribution-origin-resource"></a>An *origin* is the definitive source of content for your distribution. When you create your distribution, you choose the Lightsail instance, container service, bucket, or load balancer (with one or more instances attached to it) that hosts the content of your website or web application. This section explains the origin settings you configure for a distribution and links to related origin tasks.

You can choose only one origin per distribution. You can change the origin at any time after you create your distribution. For more information, see [Change the origin of your distribution](amazon-lightsail-changing-distribution-origin.md). Depending on the type of origin resource you choose, your distribution communicates with it using **IPv4-only**, **Dual-stack**, or **IPv6-only**. For more information, see [Origin IP address type](#distribution-origin-ip-address-type).

![Distribution origin selector](https://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-distribution-choose-origin.png)


## Origin protocol policy
<a name="distribution-origin-protocol-policy"></a>

The origin protocol policy is the protocol policy that your distribution uses when pulling content from your origin. After you choose an origin for your distribution, you should determine if your distribution should use Hypertext Transfer Protocol (HTTP) or Hypertext Transfer Protocol Secure (HTTPS) when pulling content from your origin. If your origin is not configured for HTTPS, then you must use HTTP.

You can choose one of the following origin protocol policies for your distribution:
+ **HTTP Only** - Your distribution uses only HTTP to access the origin. This is the default setting.
+ **HTTPS Only** - Your distribution uses only HTTPS to access the origin.

The steps to edit your origin protocol policy are included in the [Create a distribution](amazon-lightsail-creating-content-delivery-network-distribution.md#creating-a-distribution) section of the [Create and configure a distribution](amazon-lightsail-creating-content-delivery-network-distribution.md) guide.

**Note**  
When you select a Lightsail bucket as the origin of your distribution, the **Origin protocol policy** defaults to **HTTP only**. You cannot change the origin protocol policy when a bucket is the origin of your distribution.

## Origin IP address type
<a name="distribution-origin-ip-address-type"></a>

The origin IP address type determines which Internet Protocol version your distribution uses when communicating with your origin resource. After you choose an origin for your distribution, you can select the IP address type that your distribution should use to connect to the origin.

You can choose one of the following origin IP address types for your distribution:
+ **IPv4-only** - Your distribution uses only IPv4 to communicate with the origin. For instance origins, a static IP must be attached.
+ **Dual-stack** - Your distribution can use either IPv4 or IPv6 to communicate with the origin. For instance origins, a static IP must be attached.
+ **IPv6-only** - Your distribution uses only IPv6 to communicate with the origin. For instance origins, no static IP is required, but the instance must have IPv6 connectivity.

**Note**  
The Origin IP address type setting is only available for instance origins. When you select a bucket, container service, or load balancer as the origin, the **Origin IP address type** defaults to **IPv4-only** and cannot be changed.

## Topics
<a name="distribution-origins-topics-toc"></a>
+ [Use distributions with buckets](amazon-lightsail-using-distributions-with-buckets.md)
+ [Change the origin of your distribution](amazon-lightsail-changing-distribution-origin.md)