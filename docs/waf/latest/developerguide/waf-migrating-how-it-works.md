**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# How the migration works

You can migrate your web ACLs from AWS WAF Classic to AWS WAF v2 using several methods. Follow these steps to complete your migration.

###### To migrate from AWS WAF Classic to AWS WAF v2

1. Identify your AWS WAF Classic web ACLs:
   - View a list of your web ACLs in the AWS Health dashboard.
   - Use the [AWS WAF Classic web ACL cleanup script](https://github.com/aws-samples/sample-for-waf-classic-to-wafv2-migrate-and-cleanup/tree/main/scripts/waf-classic-cleanup "         https://github.com/aws-samples/sample-for-waf-classic-to-wafv2-migrate-and-cleanup/tree/main/scripts/waf-classic-cleanup          ") to get a list of all your web ACLs and their associations. This helps you identify which web ACLs are actively protecting resources and allows you to delete unused web ACLs.

2. Migrate individual web ACLs:
   - Follow the migration process in the [AWS WAF Developer Guide](waf-migrating-procedure.md "waf-migrating-procedure.md").
   - Use the migration wizard to parse your AWS WAF Classic web ACL and generate an AWS CloudFormation template.
   - Use the generated template to create an equivalent AWS WAF v2 web ACL and complete the migration.

3. For multiple eligible web ACLs:
   - Use the [AWS WAF bulk migration script](https://github.com/aws-samples/sample-for-waf-classic-to-wafv2-migrate-and-cleanup/tree/main/scripts/waf-classic-migration "https://github.com/aws-samples/sample-for-waf-classic-to-wafv2-migrate-and-cleanup/tree/main/scripts/waf-classic-migration          ") to migrate multiple eligible AWS WAF Classic web ACLs simultaneously.

4. For web ACLs managed by AWS Firewall Manager:
   - Firewall Manager policies use AWS WAF Classic web ACLs with AWS WAF Classic policies.
     For Shield Advanced policies created before January 2022, Firewall Manager also uses AWS WAF Classic web ACLs.
     You must migrate these policies to use AWS WAF v2 web ACLs.

   Follow the instructions at [Migrating AWS WAF Classic Web ACLs in Firewall Manager](migrate-waf-classic-fms.md "migrate-waf-classic-fms.md").

###### Important

We recommend reviewing each migrated web ACLto ensure it meets your security requirements before associating it with your resources.
