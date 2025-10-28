**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Sharing a rule group

You can share a rule group with other acccounts, for use by those accounts.

###### Sharing a rule group

You can share with one or more specific accounts, and you can share
with all accounts in an organization.

To share a rule group, you use the AWS WAF API to create a policy for the rule group sharing that you want.
For more information, see
[PutPermissionPolicy](../APIReference/API_PutPermissionPolicy.md "../APIReference/API_PutPermissionPolicy.md") in the _AWS WAF API Reference_.

###### Using a rule group that's been shared with you

If a rule group has been shared with your account, you can access it through the API
and you can reference it when you create or update your protection packs (web ACLs) through the API.
For more information, see
[GetRuleGroup](../APIReference/API_GetRuleGroup.md "../APIReference/API_GetRuleGroup.md"),
[CreateWebACL](../APIReference/API_CreateWebACL.md "../APIReference/API_CreateWebACL.md"), and
[UpdateWebACL](../APIReference/API_UpdateWebACL.md "../APIReference/API_UpdateWebACL.md")
in the _AWS WAF API Reference_. Rule groups that are shared with you don't appear in your AWS WAF console rule groups listing.
