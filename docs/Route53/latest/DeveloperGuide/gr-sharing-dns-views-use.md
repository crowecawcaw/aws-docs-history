# Using a DNS view that's shared with you

After another account shares a DNS view with you, and you accept the resource share
invitation if one was sent, you can associate your own Route 53 private hosted zones with the shared
DNS view. The records in those hosted zones then become resolvable through the owner's global
resolver for the clients that the DNS view authorizes.

To find the DNS views that are shared with your account, open the AWS RAM console at [https://console.aws.amazon.com/ram/](https://console.aws.amazon.com/ram/ "https://console.aws.amazon.com/ram/") and choose
**Shared with me**, **Shared resources**. To associate a
private hosted zone with a shared DNS view, use the same procedure that you use for a DNS view
that you own, and specify the of the shared DNS view. For more information, see [Configuring private hosted zone associations with Route 53 Global Resolver](gr-configuring-private-hosted-zone-associations.md "gr-configuring-private-hosted-zone-associations.md").

Note the following about a DNS view that's shared with you:

- You can associate and disassociate your own private hosted zones, but you can't modify or
  delete the DNS view itself unless the owner grants you a that allows those actions.
- The private hosted zone associations that you create belong to your account. You can view,
  update, and remove the associations that you created.
- If the owner stops sharing the DNS view, you can no longer create new associations on the
  view, but the associations that you already created continue to function until you or the owner
  removes them.
