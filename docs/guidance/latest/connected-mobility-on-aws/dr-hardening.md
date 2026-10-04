

# If you need more than this
<a name="dr-hardening"></a>

The Guidance is a reference architecture, and its defaults favour a single-Region deployment that is straightforward to operate. Three changes carry most of the benefit if your requirements are stricter:
+  **Raise the Kafka broker count and replication factor together**, with a minimum in-sync replica setting, per the caution above.
+  **Add DynamoDB global tables** for the operational tables that must survive a Region event without a restore step.
+  **Enable Redis snapshots** if rebuilding live state from resumed telemetry is not acceptable in your recovery window.

Test the recovery path rather than assuming it. A redeploy into a second Region is also the fastest way to discover any resource whose name is globally scoped — see [Plan your deployment](plan-your-deployment.md).