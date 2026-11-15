

# Delete a Lightsail web address
<a name="amazon-lightsail-delete-web-address"></a>

Delete a Lightsail web address that you no longer need. You can delete a web address with the **Unattached** or **Create failed** status. If your web address is attached to a resource, detach it first. For instructions, see [Detach a web address using the Lightsail console](amazon-lightsail-detach-transfer-web-address.md#detach-web-address).

**Important**  
After you delete a web address, another account can take its name: right away if it was never attached, or after 30 to 37 days if it was. For more information, see [What happens to the name of a deleted web address](#web-address-cooldown).

## What happens to the name of a deleted web address
<a name="web-address-cooldown"></a>
+ If you delete a web address that was previously attached to a resource, Lightsail holds its name for 30 to 37 days. This cooldown period protects the visitors of your site who still use the old web address, because no other account can create a web address with the name and serve them different content. Your account can create a web address with the same name again during the cooldown period, so if you change your mind, you can get the name back. The deleted web address counts toward your quota during the cooldown period.
+ If your web address was never attached to a resource, its name is available as soon as the deletion finishes.
+ If you delete a web address that still has child web addresses, it changes to the **Implicit** status, and its child web addresses keep working. You aren't charged for an implicit web address, and it doesn't count toward your quota. For more information, see [Child web addresses](amazon-lightsail-web-addresses.md#web-addresses-child).

## Delete a web address using the Lightsail console
<a name="delete-web-address-console"></a>

Complete the following procedure to delete a web address using the Lightsail console.

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Lightsail web addresses**.

1. Choose the vertical ellipsis (⋮) icon next to the web address that you want to delete, and then choose **Delete**.

1. Enter **confirm**, and then choose **Delete web address**.  
![The Delete web address dialog, with confirm entered.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-web-address-delete-dialog.png)

## Delete a web address using the AWS CLI
<a name="delete-web-address-cli"></a>

Complete the following procedure to delete a web address using the AWS CLI. For more information, see [delete-subdomain](https://docs.aws.amazon.com/cli/latest/reference/lightsail/delete-subdomain.html) in the *AWS CLI Command Reference*.

**Note**  
In the Lightsail API and AWS CLI, web addresses are called *subdomains*.

**Note**  
You can run the following commands in AWS CloudShell. CloudShell is a browser-based, pre-authenticated shell that you can launch directly from the Lightsail console. With CloudShell, you can run AWS CLI commands using your preferred shell, such as Bash, PowerShell, or Z shell, without downloading or installing command line tools. For more information, see [Manage Lightsail resources with AWS CloudShell](amazon-lightsail-cloudshell.md).  
To use the AWS CLI on your own computer, install and configure it first. For instructions, see [Set up and configure the AWS CLI for Lightsail operations](lightsail-how-to-set-up-and-configure-aws-cli.md).

1. Open a Terminal, [AWS CloudShell](amazon-lightsail-cloudshell.md), or Command Prompt window.

1. Enter the following command to list your web addresses.

   ```
   aws lightsail get-subdomains --region us-east-1
   ```

   Make a note of the `subdomainName` value of the web address that you want to delete.

1. Enter the following command to delete the web address.

   ```
   aws lightsail delete-subdomain --subdomain-name {{SubdomainName}} --region us-east-1
   ```

   In the command, replace {{SubdomainName}} with the name of your web address.

   The command returns an operation. The web address no longer appears in the output of `get-subdomains`, unless it has child web addresses, in which case its state is `IMPLICIT`.