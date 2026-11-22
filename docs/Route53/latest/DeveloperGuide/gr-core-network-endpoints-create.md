

# Creating a core network endpoint

To create a core network endpoint, connect a global resolver to a Cloud WAN core network that you own. After you create the endpoint, the core network's segments can be used as access sources for DNS resolution.

**Note**  
A core network endpoint requires a minimum of two AWS Regions, which must be among the Regions where the global resolver operates, and supports a maximum of five private IP addresses.
+ [Console](#gr-core-network-endpoints-create-console)
+ [CLI](#gr-core-network-endpoints-create-cli)

## Creating a core network endpoint (console)
<a name="gr-core-network-endpoints-create-console"></a>

**To create a core network endpoint**

1. Open the Route 53 Global Resolver console at [https://console.aws.amazon.com/route53globalresolver/](https://console.aws.amazon.com/route53globalresolver/).

1. In the navigation pane, choose **Global resolvers**.

1. Select the global resolver that you want to connect to a core network.

1. Choose the **Core network endpoints** tab, and then choose **Create core network endpoint**.

1. For **Core network**, select the Cloud WAN core network to connect to.

1. Choose **Create core network endpoint**.

After the endpoint is created, you can reference the core network's segments as access sources. For more information about access sources, see [Managing access controls with access sources and tokens in Route 53 Global Resolver](gr-managing-access-controls.md).

## Creating a core network endpoint (CLI)
<a name="gr-core-network-endpoints-create-cli"></a>

You can also create and manage core network endpoints with the AWS CLI and the Route 53 Global Resolver API. Use the create operation to connect a global resolver to a core network, the get and list operations to view your endpoints, the update operation to change an endpoint, and the delete operation to disconnect a core network. For the command syntax and parameters, see the [Route 53 Global Resolver section of the *AWS Command Line Interface Reference*](https://docs.aws.amazon.com/cli/latest/reference/route53globalresolver/).