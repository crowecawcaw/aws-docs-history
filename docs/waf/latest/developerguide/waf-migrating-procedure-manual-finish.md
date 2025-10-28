**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Migrating a protection pack (web ACL): manual follow-up

After the automated migration is complete, review the newly created protection pack (web ACL) and fill in the
components that the migration doesn't bring over for you. The following procedure covers
the aspects of protection pack (web ACL) management that the migration doesn't handle. For the list, see
[Migration caveats and limitations](waf-migrating-caveats.md "waf-migrating-caveats.md").

###### To finish the basic migration - manual steps

1.  Sign in to the AWS Management Console and open the AWS WAF console at
    [https://console.aws.amazon.com/wafv2/homev2](https://console.aws.amazon.com/wafv2/homev2 "https://console.aws.amazon.com/wafv2/homev2").
2.  The console should automatically use the latest version of AWS WAF. To verify this, in the
    navigation pane, check that you can see the option **Switch to AWS WAF Classic**.
    If you see **Switch to new AWS WAF**, choose that to switch to the latest version.
3.  In the navigation pane, choose **protection packs (web ACLs)**.
4.  In the **protection packs (web ACLs)** page, locate your new protection pack (web ACL) in the list for the
    Region where you created it. Choose the protection pack (web ACL)'s name to bring up the
    settings for the protection pack (web ACL).
5.  Review all of the settings for the new protection pack (web ACL) against your prior AWS WAF Classic web
    ACL. By default, logging and protected resource associations are disabled.
    You enable those when you're ready to switch over.
6.  If your AWS WAF Classic protection pack (web ACL) had a managed rule group, the rule group inclusion wasn't
    brought over in the migration. You can add managed rule groups to the new
    protection pack (web ACL). Review the information about managed rule groups, including the
    list of AWS Managed Rules that are available with the new version of AWS WAF, at
    [Using managed rule groups in AWS WAF](waf-managed-rule-groups.md "waf-managed-rule-groups.md"). To add a managed rule group,
    do the following:

        1. In your protection pack (web ACL) settings page, choose the protection pack (web ACL)
         **Rules** tab.
        2. Choose **Add rules**, then choose **Add
         managed rule groups**.
        3. Expand the listing for the vendor of your choice and select the rule groups that you
         want to add. For AWS Marketplace sellers, you might need to subscribe to the
         rule groups. For more information about using managed rule groups in
         your protection pack (web ACL), see [Using managed rule groups in AWS WAF](waf-managed-rule-groups.md "waf-managed-rule-groups.md") and [Using protection packs (web ACLs) with rules and rule groups in AWS WAF](web-acl-processing.md "web-acl-processing.md").

    After you finish the basic migration process, we recommend that you review your needs and
    consider additional options, to be sure that the new configuration is as efficient
    as possible and that it's using the latest available security options. See [Migrating a protection pack (web ACL): additional considerations](waf-migrating-procedure-additional.md "waf-migrating-procedure-additional.md").
