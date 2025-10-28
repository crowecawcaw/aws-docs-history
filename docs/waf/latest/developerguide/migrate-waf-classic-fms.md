**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Migrating AWS WAF Classic Web ACLs in Firewall Manager

There are two scenarios where Firewall Manager might use AWS WAF Classic WebACLs:

1. With a AWS WAF Classic policy
2. With a Shield Advanced policy created before January 2022

## Migrating Web ACLs in AWS WAF Classic Policies

To migrate web ACLs from a AWS WAF Classic policy, you must first migrate any AWS WAF Classic rule groups to AWS WAF (v2) rule groups. Then you can create a new policy using the migrated rule groups.

1. Migrate your AWS WAF Classic rule groups to AWS WAF (v2) rule groups using this migration script: [AWS WAF bulk migration script](https://github.com/aws-samples/sample-for-waf-classic-to-wafv2-migrate-and-cleanup/tree/main/scripts/waf-classic-migration "https://github.com/aws-samples/sample-for-waf-classic-to-wafv2-migrate-and-cleanup/tree/main/scripts/waf-classic-migration        ").
2. Create a new AWS WAF policy with the following settings:
   - Use the newly migrated AWS WAF (v2) rule groups
   - Enable automatic remediation

3. For each account you want to migrate:
   1. Remove the account from the old AWS WAF Classic policy
   2. Wait approximately 2-3 minutes
   3. Add the account to the scope of the new AWS WAF policy
   4. (Optional) Use resource tag filtering to narrow the policy scope to specific resources

4. Verify the migration:
   1. Confirm that the new AWS WAF policy has created v2 web ACLs
   2. Verify that Firewall Manager has associated the new web ACLs with the appropriate resources

## Migrating Web ACLs in Shield Advanced Policies

Automatic application layer DDoS mitigation in Firewall Manager works only with web ACLs that were created using AWS WAF (v2).
If you want to use automatic mitigation in your Firewall Manager policies, and your policies currently use AWS WAF Classic web ACLs, you must migrate them to AWS WAF (v2).
You can either migrate all web ACLs at once or migrate them one account at a time.

### Migrating All Web ACLs at Once

To migrate all web ACLs in your Shield Advanced policy at once, you can use the policy's automatic remediation feature:

1. Open the Firewall Manager console at [https://console.aws.amazon.com/wafv2/fms](https://console.aws.amazon.com/wafv2/fms "https://console.aws.amazon.com/wafv2/fms").
2. Choose your Shield Advanced policy.
3. Enable automatic remediation and choose the option to replace AWS WAF Classic web ACLs with AWS WAF (v2) web ACLs.

Firewall Manager creates new AWS WAF (v2) web ACLs as needed and manages the migration of resource associations from Classic to v2 web ACLs.

### Migrating Web ACLs One Account at a Time

To migrate web ACLs one account at a time, follow these steps:

1. Create a new Shield Advanced policy with the following settings:
   - Set automatic application layer DDoS mitigation to _Disabled_
   - Enable automatic remediation

2. For each account you want to migrate:
   1. Remove the account from the old Shield Advanced policy
   2. Wait approximately 2-3 minutes
   3. Add the account to the scope of the new Shield Advanced policy
   4. (Optional) Use resource tag filtering to narrow the policy scope to specific resources

3. Verify the migration:
   1. Confirm that the new Shield Advanced policy has created AWS WAF (v2) web ACLs
   2. Verify that Firewall Manager has associated the new web ACLs with the appropriate resources
