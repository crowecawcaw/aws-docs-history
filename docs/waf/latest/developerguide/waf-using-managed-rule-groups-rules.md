**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Retrieving the rules in a

managed rule group

You can retrieve a list of the rules in a managed rule group. The API and CLI
calls return the rules specifications that you can reference in the JSON model
or through AWS CloudFormation.

###### To retrieve the list of rules in a managed rule group

- **Console**
  - (Option) When you add the managed rules group to your protection pack (web ACL),
    you can choose **Edit** to view the rules.
  - (Option) After you've added the managed rule group into your
    protection pack (web ACL), from the **protection packs (web ACLs)** page, choose the
    protection pack (web ACL) you just created. This takes you to the protection pack (web ACL) edit
    page.
    - Choose **Rules**.
    - Select the rule group you want to see a rules list
      for, then choose **Edit**. AWS WAF shows
      the list of rules in the rule group.

- **API** –
  `DescribeManagedRuleGroup`
- **CLI** – `aws wafv2
describe-managed-rule-group --scope=<CLOUDFRONT|REGIONAL> --vendor-name
<vendor> --name <managedrule_name>`
