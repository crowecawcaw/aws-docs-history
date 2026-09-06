

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html). 

# Migrating AWS WAF Classic Web ACLs in Firewall Manager
<a name="migrate-waf-classic-fms"></a>

There are two scenarios where Firewall Manager might use AWS WAF Classic WebACLs:

1. With a AWS WAF Classic policy

1. With a Shield Advanced policy created before January 2022

## Migrating Web ACLs in AWS WAF Classic Policies
<a name="migrate-waf-classic-policy"></a>

To migrate web ACLs from a AWS WAF Classic policy, you must first migrate any AWS WAF Classic rule groups to AWS WAF (v2) rule groups. Then you can create a new policy using the migrated rule groups.

1. Migrate your AWS WAF Classic rule groups to AWS WAF (v2) rule groups using this migration script: [AWS WAF bulk migration script](https://github.com/aws-samples/sample-for-waf-classic-to-wafv2-migrate-and-cleanup/tree/main/scripts/waf-classic-migration        ).

1. Create a new AWS WAF policy with the following settings:
   + Use the newly migrated AWS WAF (v2) rule groups
   + Enable automatic remediation

1. For each account you want to migrate:

   1. Remove the account from the old AWS WAF Classic policy

   1. Wait approximately 2-3 minutes

   1. Add the account to the scope of the new AWS WAF policy

   1. (Optional) Use resource tag filtering to narrow the policy scope to specific resources

1. Verify the migration:

   1. Confirm that the new AWS WAF policy has created v2 web ACLs

   1. Verify that Firewall Manager has associated the new web ACLs with the appropriate resources

## Migrating Web ACLs in Shield Advanced Policies
<a name="migrate-shield-policy"></a>

Automatic application layer DDoS mitigation in Firewall Manager works only with web ACLs that were created using AWS WAF (v2). If you want to use automatic mitigation in your Firewall Manager policies, and your policies currently use AWS WAF Classic web ACLs, you must migrate them to AWS WAF (v2). You can either migrate all web ACLs at once or migrate them one account at a time.

### Migrating All Web ACLs at Once
<a name="migrate-shield-all"></a>

To migrate all web ACLs in your Shield Advanced policy at once, you can use the policy's automatic remediation feature:

1. Open the Firewall Manager console at [https://console.aws.amazon.com/wafv2/fms](https://console.aws.amazon.com/wafv2/fms).

1. Choose your Shield Advanced policy.

1. Enable automatic remediation and choose the option to replace AWS WAF Classic web ACLs with AWS WAF (v2) web ACLs.

Firewall Manager creates new AWS WAF (v2) web ACLs as needed and manages the migration of resource associations from Classic to v2 web ACLs.

### Migrating Web ACLs One Account at a Time
<a name="migrate-shield-account"></a>

To migrate web ACLs one account at a time, follow these steps:

1. Create a new Shield Advanced policy with the following settings:
   + Set automatic application layer DDoS mitigation to *Disabled*
   + Enable automatic remediation

1. For each account you want to migrate:

   1. Remove the account from the old Shield Advanced policy

   1. Wait approximately 2-3 minutes

   1. Add the account to the scope of the new Shield Advanced policy

   1. (Optional) Use resource tag filtering to narrow the policy scope to specific resources

1. Verify the migration:

   1. Confirm that the new Shield Advanced policy has created AWS WAF (v2) web ACLs

   1. Verify that Firewall Manager has associated the new web ACLs with the appropriate resources