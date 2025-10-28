**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Migration caveats and limitations

The migration only handles protection pack (web ACL) configurations, and the protection pack (web ACL) migration doesn't bring
over all settings exactly as you have them in AWS WAF Classic. Some configuration items require manual configuration in AWS WAF (v2).
A few things don't map exactly between the two versions, and you'll need to decide how you want
to configure the functionality in AWS WAF (v2). Some settings, like the protection pack (web ACL)'s associations with AWS
resources, are disabled initially in the new version so you can add them when you're ready.

The following list describes the caveats of the migration and describes any steps you might
want to take in response. Use this overview to plan your migration. The detailed
migration steps, later on, walk you through the recommended mitigation steps.

- **Single account migration** – You can only migrate AWS WAF Classic
  resources for any account to AWS WAF resources for the same account.
- **Only protection pack (web ACL) configurations** – The migration only
  migrates protection packs (web ACLs) and resources that the protection packs (web ACLs) are using. To migrate a
  resource, such as a rule group or IP set, that's not used by any migrated web
  ACL, manually create the resource in AWS WAF (v2).
- **No AWS Marketplace managed rules** – The migration doesn't bring over any
  managed rules from AWS Marketplace sellers. Some AWS Marketplace sellers have equivalent managed
  rules for AWS WAF that you can subscribe to again. Before you do this, review the
  AWS Managed Rules that are provided with the latest version of AWS WAF. Most of these are free of charge for AWS WAF users. For
  information about managed rules, see [Using managed rule groups in AWS WAF](waf-managed-rule-groups.md "waf-managed-rule-groups.md").
- **No protection pack (web ACL) associations** – The migration doesn't bring
  over any associations between the protection pack (web ACL) and protected resources. This is by
  design, to avoid affecting your production workload. After you verify that
  everything is migrated correctly, associate the new protection pack (web ACL) with your
  resources.
- **Logging disabled** – Logging for the migrated protection pack (web ACL) is disabled
  by default. This is by design. Enable logging when you are ready to switch over
  from AWS WAF Classic to AWS WAF.
- **No AWS Firewall Manager rule groups** – The migration doesn't
  handle rule groups that are managed by Firewall Manager. You can migrate a protection pack (web ACL) that's
  managed by Firewall Manager, but the migration doesn't bring over the rule group. Instead
  of using the migration tool for these protection packs (web ACLs), recreate the policy for the new
  AWS WAF in Firewall Manager.

###### Note

The rule groups that Firewall Manager managed for AWS WAF Classic were Firewall Manager rule groups. With the new
version of AWS WAF, the rule groups are AWS WAF rule groups. Functionally, they
are the same.

- **AWS WAF Security Automations caveat** – Don't try to migrate any
  AWS WAF Security Automations. The migration doesn't convert Lambda functions, which
  might be in use by the automations. Consider deploying the automations for the latest version instead. For
  information, see [AWS WAF Security Automations](https://aws.amazon.com/solutions/aws-waf-security-automations/ "https://aws.amazon.com/solutions/aws-waf-security-automations/").
