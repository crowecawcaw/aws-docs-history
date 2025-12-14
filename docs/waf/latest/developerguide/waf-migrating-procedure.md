**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Migrating a protection pack (web ACL) from AWS WAF Classic to AWS WAF

The automated migration carries over most of your AWS WAF Classic protection pack (web ACL) configuration,
leaving some things that you need to handle manually.

###### Note

Some protection configurations cannot be automatically migrated, and require
manual configuration in AWS WAF (v2). See the list at [Migration caveats and limitations](waf-migrating-caveats.md "waf-migrating-caveats.md").

The following lists the high-level steps for migrating a protection pack (web ACL).

1. The automated migration reads everything related to your existing protection pack (web ACL), without modifying
   or deleting anything in AWS WAF Classic. It creates a representation of the web
   ACL and its related resources, compatible with AWS WAF. It generates an CloudFormation
   template for the new protection pack (web ACL) and stores it in an Amazon S3 bucket.
2. You deploy the template into CloudFormation, in order to recreate the protection pack (web ACL) and related resources in
   AWS WAF.
3. You review the protection pack (web ACL), and manually complete the migration, making sure
   that your new protection pack (web ACL) takes full advantage of the capabilities of the latest AWS WAF.
4. You manually switch your protected resources over to the new protection pack (web ACL).

###### Topics

- [Migrating a protection pack (web ACL): automated migration](waf-migrating-procedure-automatic.md "waf-migrating-procedure-automatic.md")
- [Migrating a protection pack (web ACL): manual follow-up](waf-migrating-procedure-manual-finish.md "waf-migrating-procedure-manual-finish.md")
- [Migrating a protection pack (web ACL): additional considerations](waf-migrating-procedure-additional.md "waf-migrating-procedure-additional.md")
- [Migrating a protection pack (web ACL): switchover](waf-migrating-procedure-switchover.md "waf-migrating-procedure-switchover.md")
