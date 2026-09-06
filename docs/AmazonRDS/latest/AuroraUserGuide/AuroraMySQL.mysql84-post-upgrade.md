

# Post-upgrade cleanup for Aurora MySQL version 8.4
<a name="AuroraMySQL.mysql84-post-upgrade"></a>

After you finish upgrading your Aurora MySQL version 3 cluster to version 8.4, perform the following cleanup actions:
+ **Migrate users to caching\_sha2\_password.** The default `authentication_policy` is `*:caching_sha2_password` in Aurora MySQL version 8.4. We recommend migrating any remaining users from `mysql_native_password` to `caching_sha2_password` before the upgrade is complete.
+ **Update monitoring and automation.** Update any CloudWatch alarms, setup scripts, and automation that use removed replication status variables (such as `Com_show_slave_status` or `Com_slave_start`). Use the replacement status variables instead.
+ **Update CloudFormation templates.** Update any CloudFormation templates to remove references to removed parameters and use the replacement parameters.