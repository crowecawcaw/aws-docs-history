

# Tutorial: Create your first Route 53 Global Resolver with AWS Cloud WAN

This tutorial demonstrates how to create a private-only Route 53 Global Resolver. You create a global resolver with public IP connectivity turned off, connect it to an AWS Cloud WAN core network, and allow DNS queries from a core network segment. As a result, the resolver is reachable only over your private Cloud WAN connections and not over the internet.

When you're finished, you have a global resolver that authorized clients can reach only from a connected Cloud WAN segment.

The following sections describe how to get started with a private-only Route 53 Global Resolver using AWS Cloud WAN.

## Prerequisites
<a name="gr-getting-started-cwan-prerequisites"></a>

Before you begin, make sure that you have the following:
+ Completion of the setup steps. Your system administrator must complete the steps in [Setting up account access for Route 53 Global Resolver](gr-setting-up.md), and then return to this tutorial.
+ An existing AWS Cloud WAN core network that you own. We recommend that its core network policy is at version `2026.10` or later so that DNS queries route to the closest AWS Region. For more information, see [Core network policy versions](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-policies-json.html#cloudwan-version-json).
+ An AWS account and the appropriate permissions to access, view, and edit Route 53 Global Resolver components.

## Step 1: Create a global resolver with public IP connectivity disabled
<a name="gr-getting-started-cwan-step1"></a>

First, create a global resolver instance, select the AWS Regions where it will operate, and turn off public IP connectivity.

1. Open the Route 53 Global Resolver console at [https://console.aws.amazon.com/route53globalresolver/](https://console.aws.amazon.com/route53globalresolver/).

1. Choose **Create global resolver**.

1. For **Name**, enter a descriptive name for your global resolver.

1. For **Description**, optionally enter a description.

1. For **Regions**, select two or more AWS Regions where you want to instantiate the global resolver. Choose Regions closest to your clients for optimal performance.

1. For **Public IP connectivity**, disable public IP connectivity. When public IP connectivity is disabled, the global resolver is reachable only from a connected core network, and not over the internet.

1. Optionally, add tags to help organize and manage your resources.

1. Choose **Create global resolver**.

The global resolver creation process takes a few minutes to complete. Because public IP connectivity is disabled, you connect a Cloud WAN core network in the next step to make the resolver reachable from your private connections.

## Step 2: Connect a Cloud WAN core network
<a name="gr-getting-started-cwan-step2"></a>

Create a core network endpoint to connect your global resolver to an AWS Cloud WAN core network. A core network endpoint requires a minimum of two AWS Regions, which must be among the resolver's Regions, and supports up to five private IP addresses.

1. In the Route 53 Global Resolver console, choose your global resolver.

1. Choose the **Core network endpoints** tab, and then choose **Create core network endpoint**.

1. For **Core network**, select the Cloud WAN core network to connect to.

1. Choose **Create core network endpoint**.

After you connect the core network, its segments can be used as access sources for DNS resolution. For more information about core network endpoints, see [Connecting a global resolver to a core network](gr-core-network-endpoints.md).

## Step 3: Create a DNS view and a segment-based access source
<a name="gr-getting-started-cwan-step3"></a>

Create a DNS view to organize your clients, and then create an access source that selects a Cloud WAN segment. Clients that reach the resolver from that segment are authorized to resolve DNS queries.

1. In the Route 53 Global Resolver console, choose your global resolver.

1. Choose **Create DNS view**.

1. For **Name**, enter a descriptive name for your DNS view.

1. Choose **Create DNS view**.

1. After the DNS view is created, choose **Access source** and then **Create access source**.

1. For the access source type, select **Cloud WAN segment** instead of a CIDR range.

1. For **Segment**, select the core network segment whose clients you want to authorize.

1. Choose **Create Access Source rule**.

For more information about access sources, see [Managing access controls with access sources and tokens in Route 53 Global Resolver](gr-managing-access-controls.md).

## Next steps
<a name="gr-getting-started-cwan-next-steps"></a>

Now that you have a private-only Route 53 Global Resolver connected to a Cloud WAN core network, you can explore additional features:
+ Configure client devices to use your resolver (required for production). Update your client DNS settings to use the private IP addresses of the core network endpoint.
+ Set up logging for monitoring and compliance (recommended for production). Configure logging to Amazon CloudWatch, Amazon S3, or Amazon Data Firehose for monitoring and analysis. For more information, see [Monitoring DNS activity and performance with Route 53 Global Resolver](gr-monitoring.md).
+ Add DNS filtering rules to block malicious domains. For more information, see *DNS filtering*.