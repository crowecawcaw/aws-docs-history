

# Tutorial: Create your first Route 53 Global Resolver
<a name="gr-getting-started"></a>

This getting started guide demonstrates the basic components of Route 53 Global Resolver and optionally creating a simple DNS filtering setup. This tutorial covers the core concepts but doesn't include production requirements like client configuration, logging, or private domain resolution.

When you're finished, you'll have a basic Route 53 Global Resolver setup that can filter DNS queries and block malicious domains.

The following sections describe how to quickly get started with DNS security and filtering using Route 53 Global Resolver.

## Prerequisites
<a name="gr-getting-started-prerequisites"></a>

Before you can use Route 53 Global Resolver, you need an AWS account and the appropriate permissions to access, view, and edit Route 53 Global Resolver components. Your system administrator must complete the steps in [Setting up account access for Route 53 Global Resolver](gr-setting-up.md), and then return to this tutorial.

## Step 1: Create a global resolver
<a name="gr-getting-started-step1"></a>

First, create a global resolver instance and select the AWS Regions where it will operate.

1. Open the Route 53 Global Resolver console at [https://console.aws.amazon.com/route53globalresolver/](https://console.aws.amazon.com/route53globalresolver/).

1. Choose **Create global resolver**.

1. For **Name**, enter a descriptive name for your global resolver.

1. For **Description**, optionally enter a description.

1. For **Regions**, select two or more AWS Regions where you want to instantiate the global resolver. Choose Regions closest to your clients for optimal performance.

1. For **IP address type**, choose the IP address type for this resolver.
   + **IPv4** - Includes only IPv4 addresses.
   + **Dualstack** - Includes IPv4 and IPv6 addresses.

1. Optionally, add tags to help organize and manage your resources.

1. Choose **Create global resolver**.

You'll receive anycast IPv4 addresses immediately that your clients can use to reach the resolver. The global resolver creation process takes a few minutes to complete before the addresses become functional.

## Step 2: Create a DNS view and configure authentication
<a name="gr-getting-started-step2"></a>

Create a DNS view to organize your clients and configure authentication using IP Access Sources. This tutorial uses IP-based authentication. You can also use access tokens for DoH/DoT protocols.

1. In the Route 53 Global Resolver console, choose your global resolver.

1. Choose **Create DNS view**.

1. For **Name**, enter a descriptive name for your DNS view.

1. For **Description**, optionally enter a description.

1. Choose **Create DNS view**.

1. After the DNS view is created, choose **Access source** and then **Create access source**.

1. For **CIDR block**, enter the IP address range for your clients (for example, `203.0.113.0/24`).

1. For **Protocol**, choose **Do53** (DNS over port 53) for basic setup.

1. Choose **Create Access Source rule**.

## Step 3: Configure DNS filtering rules (optional)
<a name="gr-getting-started-step3"></a>

Set up basic DNS filtering rules to block access to malicious domains.

1. In your DNS view, choose **Firewall rules** and then **Create firewall rule**.

1. For **Name**, enter a descriptive name for the rule.

1. For **Priority**, enter `100` (lower numbers have higher priority).

1. For **Action**, choose **Block**.

1. For **Domain list type**, choose **AWS Managed Domain List**.

1. For **Managed domain list**, choose **AmazonGuardDutyThreatList** and **Malware and Botnet Command and Control** to block known malicious domains (you can add other managed lists or create custom lists later).

1. Choose **Create firewall rule**.

## Step 4: Test your configuration
<a name="gr-getting-started-step4"></a>

Test that your Route 53 Global Resolver configuration is working correctly.

1. From a client machine within your configured CIDR range, test DNS resolution using the anycast IP addresses provided by your global resolver:

   ```
   nslookup example.com <anycast-ip-address>
   ```

1. Verify that legitimate domains resolve correctly.

1. Test that blocked domains are properly filtered. You can create a custom domain list with a test domain to verify your firewall rules are working correctly. For more information about Managed Domain Lists, see [Managed Domain Lists](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-managed-domain-lists.html).

1. Check the Route 53 Global Resolver console for query logs and filtering activity.

For comprehensive testing procedures and troubleshooting, see *Troubleshooting Route 53 Global Resolver*.

## Step 5: Monitoring DNS activity
<a name="gr-getting-started-step5"></a>

Configure logging for your DNS activity.

1. Choose an Observability Region.

1. Select the destination for query logs.

For comprehensive testing procedures and troubleshooting, see *Testing and troubleshooting Route 53 Global Resolver*.

## Step 6: Clean up (optional)
<a name="gr-getting-started-cleanup"></a>

If you created this configuration for testing purposes and don't want to continue using Route 53 Global Resolver, clean up the resources to avoid ongoing charges.

1. In the Route 53 Global Resolver console, delete any firewall rules you created.

1. Delete any Access Source rules you created.

1. Delete the DNS view.

1. Delete the global resolver.

**Important**  
Deleting these resources will stop DNS resolution for any clients configured to use them. Update your client configurations before deleting the resolver or removing access rules.

## Next steps
<a name="gr-getting-started-next-steps"></a>

Now that you have a basic Route 53 Global Resolver configuration, you can explore additional features:
+ Configure client devices to use your resolver (required for production). Update your client DNS settings to use the anycast IP addresses provided by your global resolver.
+ Set up logging for monitoring and compliance (recommended for production). Configure logging to Amazon CloudWatch, Amazon S3, or Amazon Data Firehose for monitoring and analysis. For more information, see [Monitoring DNS activity and performance with Route 53 Global Resolver](gr-monitoring.md).
+ Configure private hosted zone forwarding for internal domains (required if you have private AWS resources). For more information, see *Working with private hosted zones*.
+ Set up encrypted DNS connectivity using DNS-over-HTTPS (DoH) or DNS-over-TLS (DoT). For more information, see *Configuring encrypted DNS*.
+ Create custom domain lists and advanced filtering rules. For more information, see *DNS filtering*.