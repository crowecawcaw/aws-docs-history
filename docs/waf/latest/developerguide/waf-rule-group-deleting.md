**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Deleting a rule group

Follow the guidance in this section to delete a rule group.

###### Deleting referenced sets and rule groups

When you delete an entity that you can use in a protection pack (web ACL), like an IP set, regex
pattern set, or rule group, AWS WAF checks to see if the entity is currently being
used in a protection pack (web ACL). If it finds that it is in use, AWS WAF warns you. AWS WAF is almost
always able to determine if an entity is being referenced by a protection pack (web ACL). However, in
rare cases it might not be able to do so. If you need to be sure that nothing is
currently using the entity, check for it in your protection packs (web ACLs) before deleting
it. If the entity is a referenced set, also check that no rule groups are using it.

###### To delete a rule group

1. Sign in to the AWS Management Console and open the AWS WAF console at
   [https://console.aws.amazon.com/wafv2/homev2](https://console.aws.amazon.com/wafv2/homev2 "https://console.aws.amazon.com/wafv2/homev2").
2. In the navigation pane, choose **Rule groups**.
3. Choose the rule group that you want to delete, and then choose
   **Delete**.

###### Note

If you don't see the rule group that you want to delete, check the Region selection inside the **Rule groups** section. For rule groups used to protect Amazon CloudFront distributions, use the **Global (CloudFront)** setting.
