

# Detach or transfer a Lightsail web address

Detach a Lightsail web address when you no longer want it to serve a resource, or transfer it to a different resource, for example a new distribution that replaces your current one.

**Note**  
Each month, you get 24 hours of free unattached web address time. After that, we charge USD $1 per month for each unattached web address. For more information, see [What do Lightsail web addresses cost?](amazon-lightsail-frequently-asked-questions-faq-billing-and-account-management.md#what-do-lightsail-web-addresses-cost).

## Prerequisites
<a name="transfer-web-address-prerequisites"></a>
+ To transfer a web address, the resource that you transfer it to must meet the same prerequisites as an attach. For more information, see [Prerequisites](amazon-lightsail-create-attach-web-address.md#attach-web-address-prerequisites).
+ If you use IAM policies to control access to Lightsail, you need the following permissions:
  + `lightsail:UpdateSubdomainAssociation` – To detach or transfer a web address.
  + `lightsail:DetachCertificateFromDistribution` – To detach or transfer a web address.
  + `lightsail:AttachCertificateToDistribution` on the distribution – To transfer a web address.

  For more information, see [Grant least-privilege permissions with IAM identity policies in Lightsail](security_iam_id-based-policy-examples.md).

## Detach a web address using the Lightsail console
<a name="detach-web-address"></a>

When you detach a web address, it stops working within a few minutes, and your distribution will only be reachable using its default domain. Your web address will keep its name and will have the **Unattached** status. If you no longer need the web address, delete it. For instructions, see [Delete a Lightsail web address](amazon-lightsail-delete-web-address.md).

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Lightsail web addresses**.

1. Choose the vertical ellipsis (⋮) icon next to the web address that you want to detach, and then choose **Detach**.

1. Choose **Detach** to confirm.  
![The Detach web address dialog for mysite.amazonlightsail.com, with the Detach button.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-web-address-detach-dialog.png)

## Transfer a web address using the Lightsail console
<a name="transfer-web-address"></a>

Transfer a web address to move it to a different distribution in one step, for example when you replace a distribution. You don't need to detach it first, and because it stays attached through the move, it won't incur charges. When you transfer a web address, Lightsail detaches it from its current distribution and attaches it to the distribution that you choose.

**Note**  
A transfer usually takes 5 to 15 minutes, and your web address is unavailable during the transfer.

You can transfer a web address once every 24 hours. This limit applies to each web address, not to your account.

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Lightsail web addresses**.

1. Choose the vertical ellipsis (⋮) icon next to the web address that you want to transfer, and then choose **Transfer to another resource**.

1. For **Select distribution**, choose the resource to transfer the web address to.

1. Choose **Transfer web address**.  
![The Transfer web address dialog for mysite.amazonlightsail.com, with my-new-distribution selected.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-web-address-transfer-dialog.png)

## If a transfer fails
<a name="web-address-transfer-failed"></a>

If a transfer fails before Lightsail detaches your web address from its current distribution, your web address stays attached to that distribution. If the transfer fails after Lightsail detaches it, your web address has the **Unattached** status, and it's charged while it's unattached. Attach it to a distribution again. For instructions, see [Create and attach a Lightsail web address](amazon-lightsail-create-attach-web-address.md).

## Detach or transfer a web address using the AWS CLI
<a name="detach-transfer-web-address-cli"></a>

Complete the following procedure to detach or transfer a web address using the AWS CLI. For more information, see [update-subdomain-association](https://docs.aws.amazon.com/cli/latest/reference/lightsail/update-subdomain-association.html) in the *AWS CLI Command Reference*.

**Note**  
In the Lightsail API and AWS CLI, web addresses are called *subdomains*.

**Note**  
You can run the following commands in AWS CloudShell. CloudShell is a browser-based, pre-authenticated shell that you can launch directly from the Lightsail console. With CloudShell, you can run AWS CLI commands using your preferred shell, such as Bash, PowerShell, or Z shell, without downloading or installing command line tools. For more information, see [Manage Lightsail resources with AWS CloudShell](amazon-lightsail-cloudshell.md).  
To use the AWS CLI on your own computer, install and configure it first. For instructions, see [Set up and configure the AWS CLI for Lightsail operations](lightsail-how-to-set-up-and-configure-aws-cli.md).

1. Open a Terminal, [AWS CloudShell](amazon-lightsail-cloudshell.md), or Command Prompt window.

1. To transfer a web address, enter the following command to get the Amazon Resource Name (ARN) of the distribution to transfer it to.

   ```
   aws lightsail get-distributions --distribution-name {{DistributionName}} --region us-east-1
   ```

   In the command, replace {{DistributionName}} with the name of the distribution. Make a note of the `arn` value in the output.

1. Enter one of the following commands:
   + To detach a web address from its distribution:

     ```
     aws lightsail update-subdomain-association --subdomain-name {{SubdomainName}} --action DISASSOCIATE --region us-east-1
     ```
   + To transfer a web address to a different distribution:

     ```
     aws lightsail update-subdomain-association --subdomain-name {{SubdomainName}} --action TRANSFER --target-resource-arn {{DistributionArn}} --region us-east-1
     ```

   In the command, replace {{SubdomainName}} with the name of your web address, such as `mysite`, and {{DistributionArn}} with the ARN of the distribution.

   The command returns your web address with the `DETACHING` or `TRANSFERRING` state, and an operation.

1. Enter the following command to confirm the state of your web address.

   ```
   aws lightsail get-subdomains --subdomain-name {{SubdomainName}} --region us-east-1
   ```