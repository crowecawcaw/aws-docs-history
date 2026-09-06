

# Using a DNS view that's shared with you
<a name="gr-sharing-dns-views-use"></a>

After another account shares a DNS view with you, accept any invitation that was sent. You can then associate your own Route 53 private hosted zones with the shared DNS view. The records in those hosted zones then resolve through the owner's global resolver for authorized clients.

To find DNS views shared with your account, open the AWS RAM console at [https://console.aws.amazon.com/ram/](https://console.aws.amazon.com/ram/) and choose **Shared with me**, **Shared resources**. To link a private hosted zone to a shared DNS view, follow the same steps as for a DNS view that you own. Specify the ARN of the shared DNS view. For more information, see [Configuring private hosted zone associations with Route 53 Global Resolver](gr-configuring-private-hosted-zone-associations.md).

Note the following about a DNS view that's shared with you:
+ You can associate and disassociate your own private hosted zones. You can't modify or delete the DNS view itself unless the owner grants you a managed permission that allows those actions.
+ The private hosted zone associations that you create belong to your account. You can view, update, and remove them.
+ If the owner stops sharing the DNS view, you can no longer create new associations on the view. However, existing associations continue to work until you or the owner removes them.