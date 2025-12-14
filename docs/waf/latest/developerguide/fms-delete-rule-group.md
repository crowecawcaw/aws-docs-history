**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Deleting a rule group from a Firewall Manager DNS Firewall policy

###### Deleting a rule group

To delete a rule group from a Firewall Manager DNS Firewall policy, you must perform the following
steps:

1. Remove the rule group from your Firewall Manager DNS Firewall policy.
2. Unshare the rule group in AWS Resource Access Manager. To unshare a rule group that you own, you must remove it from the resource share. You can do this using the AWS RAM console or the AWS CLI. For information about unsharing a resource, see [Update a resource share in AWS RAM](../../../ram/latest/userguide/working-with-sharing-update.md "../../../ram/latest/userguide/working-with-sharing-update.md") in the _AWS RAM User Guide_.
3. Delete the rule group using the DNS Firewall console or AWS CLI.
