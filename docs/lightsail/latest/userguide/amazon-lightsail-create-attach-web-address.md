

# Create and attach a Lightsail web address

Create a Lightsail web address, such as `mysite.amazonlightsail.com`, and then attach it to a resource to serve your content at the web address over HTTPS. You can also add a web address when you create a distribution. For instructions, see [Add a web address when you create a distribution](amazon-lightsail-creating-content-delivery-network-distribution.md#distribution-web-address-create-time).

## Prerequisites
<a name="attach-web-address-prerequisites"></a>

Before you attach a web address, set up the resource that you want to attach it to, and make sure that you have the following:
+ A Lightsail distribution with the **Deployed** status, and you've configured an origin resource for it, such as an instance, bucket, container service, or load balancer. Web addresses attach to distributions. For instructions, see [Create and configure a distribution](amazon-lightsail-creating-content-delivery-network-distribution.md).
+ The distribution isn't currently using a custom domain and isn't attached to a web address. If it uses a custom domain, disable custom domains first. For instructions, see [Switch between a web address and a custom domain](amazon-lightsail-enabling-distribution-custom-domains.md#switch-web-address-custom-domain).
+ If the origin of your distribution is a container service, it must have 3 or fewer domains (shown as custom domains in the console) before you attach. A container service can have up to 4 domains, and Lightsail adds your web address as one of them. For more information, see [Add the default domain of a distribution to a Lightsail container service](amazon-lightsail-adding-distribution-default-domain-to-container-service.md).
+ If you use IAM policies to control access to Lightsail, you need the following permissions:
  + `lightsail:CreateSubdomain` – To create a web address.
  + `lightsail:UpdateSubdomainAssociation` – To attach a web address.
  + `lightsail:AttachCertificateToDistribution` on the distribution – To attach a web address, because Lightsail attaches the certificate of your web address for you.

  For more information, see [Grant least-privilege permissions with IAM identity policies in Lightsail](security_iam_id-based-policy-examples.md).

## Web address naming rules
<a name="web-address-naming-rules"></a>

Choose your name carefully. You can't rename a web address after you create it. Web address names:
+ Must be unique across all AWS accounts.
+ Must contain 1 to 39 characters, including periods.
+ Can have one or two parts, separated by a period (.), such as `mysite` or `blog.mysite`. A name with two parts creates a child web address. For more information, see [Child web addresses](amazon-lightsail-web-addresses.md#web-addresses-child).
+ Can include lowercase letters (a-z), numbers (0-9), and hyphens (-).
+ Must start and end each part with a lowercase letter or number.
+ Can't start a part with `xn--`.
+ Can't use a reserved name. Lightsail reserves names such as brand names, trademarks, AWS service names, and common words. Common words, such as `blog`, are reserved only as one-part names, so you can use one as the first part of a child web address, such as `blog.mysite`.

**Important**  
AWS can take down a web address, or take other action described in the [AWS Acceptable Use Policy](https://aws.amazon.com/aup/), if AWS believes that its name or the content that it serves violates someone else's rights, such as copyrights or trademarks, or doesn't follow that policy. A web address that's taken down stops working.

## Create a web address using the Lightsail console
<a name="create-web-address-console"></a>

Complete the following procedure to create a web address using the Lightsail console.

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Lightsail web addresses**.

1. Choose **Create web address**.

1. For **Web address name**, enter a name for your web address. For the naming rules, see [Web address naming rules](#web-address-naming-rules).

1. (Optional) Choose **Check availability** to check whether the name is available.  
![The Create web address dialog, with the name mysite available.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-web-address-create-dialog.png)

1. Choose **Create web address**.

   Your web address appears on the **Lightsail web addresses** page with the **Creating** status. When your web address is ready, the status changes to **Unattached**.  
![The Lightsail web addresses page, with mysite.amazonlightsail.com in the Unattached status.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-web-addresses-page-unattached.png)
**Note**  
To avoid charges, attach your web address to a resource after you create it. For instructions, see [Attach a web address using the Lightsail console](#attach-web-address).  
Each month, you get 24 hours of free unattached web address time. After that, we charge USD $1 per month for each unattached web address. For more information, see [What do Lightsail web addresses cost?](amazon-lightsail-frequently-asked-questions-faq-billing-and-account-management.md#what-do-lightsail-web-addresses-cost).

## Attach a web address using the Lightsail console
<a name="attach-web-address"></a>

Complete the following procedure to attach a web address to a resource. Make sure that the resource meets the [prerequisites](#attach-web-address-prerequisites).

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Lightsail web addresses**.

1. Choose the vertical ellipsis (⋮) icon next to the web address that you want to attach, and then choose **Attach to a resource**.

1. For **Select distribution**, choose the resource. Resources that you can't attach the web address to are unavailable, and the reason is shown.  
![The dialog to attach mysite.amazonlightsail.com, with a distribution selected.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-web-address-attach-dialog.png)

1. Choose **Attach web address**.

   The status of your web address changes to **Attaching**. An attach usually takes about a minute. The first time that you attach a web address, setting up HTTPS for it can take a few minutes longer. When the status changes to **Attached**, visitors can reach your resource at your web address, such as `https://mysite.amazonlightsail.com`.
**Note**  
If you visited your web address in a browser before it was attached, it can take up to 15 minutes after the status changes to **Attached** before it works for you.

1. (Optional) If the origin of your distribution is a WordPress instance, configure WordPress to use your web address. For instructions, see [Configure WordPress with a Lightsail content delivery network](amazon-lightsail-configure-wordpress-for-distribution.md).

   If your instance uses WordPress packaged by Bitnami, see the [Bitnami version](amazon-lightsail-configure-wordpress-for-distribution-bitnami.md) of that tutorial.

You can also attach a web address from the **Getting started** tab or the **Domains** tab of your distribution's management page. For more information, see [Attach a Lightsail web address to your distribution](amazon-lightsail-distribution-web-address.md).

## If an attach fails
<a name="web-address-attach-failed"></a>

If Lightsail can't attach your web address, for example because the distribution was deleted or didn't finish deploying, your web address returns to the **Unattached** status. Check that the resource meets the [prerequisites](#attach-web-address-prerequisites), and then attach the web address again.

## Create a child web address for an existing web address
<a name="create-child-web-address"></a>

Complete the following procedure to create a child web address, such as `blog.mysite.amazonlightsail.com`, under a web address that you have.

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Lightsail web addresses**.

1. Choose the vertical ellipsis (⋮) icon next to the web address that you want to create a child web address for, and then choose **Create child web address**.

1. For **Web address name**, enter the first part of the child web address, such as `blog`.  
![The Create child web address dialog, with blog entered under mysite.amazonlightsail.com.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-web-address-create-child-dialog.png)

1. Choose **Create child web address**.

   Your child web address has the **Creating** status, and then **Unattached**. Attach it to a different resource than its parent, because a resource can have only one web address.

## Claim an implicit web address
<a name="claim-web-address"></a>

An implicit web address is reserved for your account because you created a child web address under it. Claim it to make it a web address that you can attach to a resource.

**Note**  
After you claim an implicit web address, it's charged like any other web address while it isn't attached, and it counts toward your quota.

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Lightsail web addresses**.

1. Choose the vertical ellipsis (⋮) icon next to the web address with the **Implicit** status, and then choose **Claim this web address**.

1. Choose **Claim web address**.  
![The Claim web address dialog for mysite.amazonlightsail.com.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-web-address-claim-dialog.png)

   Your web address has the **Creating** status, and then **Unattached**. To avoid charges, attach it to a distribution.

## Create and attach a web address using the AWS CLI
<a name="attach-web-address-cli"></a>

Complete the following procedure to check whether a name is available, create a web address, and attach it to a distribution using the AWS CLI.

**Note**  
In the Lightsail API and AWS CLI, web addresses are called *subdomains*.

**Note**  
You can run the following commands in AWS CloudShell. CloudShell is a browser-based, pre-authenticated shell that you can launch directly from the Lightsail console. With CloudShell, you can run AWS CLI commands using your preferred shell, such as Bash, PowerShell, or Z shell, without downloading or installing command line tools. For more information, see [Manage Lightsail resources with AWS CloudShell](amazon-lightsail-cloudshell.md).  
To use the AWS CLI on your own computer, install and configure it first. For instructions, see [Set up and configure the AWS CLI for Lightsail operations](lightsail-how-to-set-up-and-configure-aws-cli.md).

1. Open a Terminal, [AWS CloudShell](amazon-lightsail-cloudshell.md), or Command Prompt window.

1. Enter the following command to check whether a name is available.

   ```
   aws lightsail check-subdomain-availability --subdomain-name {{SubdomainName}} --region us-east-1
   ```

   In the command, replace {{SubdomainName}} with the name that you want, such as `mysite`.

   If the name is available, you should see output similar to the following.

   ```
   {
       "subdomainName": "mysite",
       "available": true
   }
   ```

1. Enter the following command to create the web address.

   ```
   aws lightsail create-subdomain --subdomain-name {{SubdomainName}} --region us-east-1
   ```

   In the command, replace {{SubdomainName}} with the name of your web address. For more information, see [create-subdomain](https://docs.aws.amazon.com/cli/latest/reference/lightsail/create-subdomain.html) in the *AWS CLI Command Reference*.

   If successful, you should see output similar to the following.

   ```
   {
       "subdomain": {
           "subdomainName": "mysite",
           "fqdn": "mysite.amazonlightsail.com",
           "arn": "arn:aws:lightsail:us-east-1:123456789012:Subdomain/83e5fe9b-1234-5678-90ab-12345EXAMPLE",
           "depth": 1,
           "state": "CREATING",
           "createdAt": 1793400000.0,
           "location": {
               "availabilityZone": "all",
               "regionName": "us-east-1"
           }
       },
       "operation": {
           "id": "a1b2c3d4-1234-5678-90ab-12345EXAMPLE",
           "resourceName": "mysite",
           "resourceType": "Subdomain",
           "createdAt": 1793400000.0,
           "location": {
               "availabilityZone": "all",
               "regionName": "us-east-1"
           },
           "isTerminal": false,
           "operationType": "CreateSubdomain",
           "status": "Started"
       }
   }
   ```

1. Enter the following command to confirm that the state of your web address is `UNATTACHED`.

   ```
   aws lightsail get-subdomains --subdomain-name {{SubdomainName}} --region us-east-1
   ```

1. Enter the following command to get the Amazon Resource Name (ARN) of the distribution.

   ```
   aws lightsail get-distributions --distribution-name {{DistributionName}} --region us-east-1
   ```

   In the command, replace {{DistributionName}} with the name of your distribution. Make a note of the `arn` value in the output.

1. Enter the following command to attach the web address to the distribution.

   ```
   aws lightsail update-subdomain-association --subdomain-name {{SubdomainName}} --action ASSOCIATE --target-resource-arn {{DistributionArn}} --region us-east-1
   ```

   In the command, replace {{SubdomainName}} with the name of your web address, and {{DistributionArn}} with the ARN of the distribution. For more information, see [update-subdomain-association](https://docs.aws.amazon.com/cli/latest/reference/lightsail/update-subdomain-association.html) in the *AWS CLI Command Reference*.

   The command returns your web address with the `ATTACHING` state, and an operation.

1. Enter the following command to confirm that the state of your web address is `ATTACHED`.

   ```
   aws lightsail get-subdomains --subdomain-name {{SubdomainName}} --region us-east-1
   ```