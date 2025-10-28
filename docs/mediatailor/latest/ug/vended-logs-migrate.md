# Migrating your AWS Elemental MediaTailor logging strategy

If you change the log strategy from Legacy CloudWatch to vended logs, MediaTailor will make this
change as soon as you save the updates. To avoid interruptions in your logging workflow, use
the following steps to migrate your logging strategy.

1. Follow the steps as described in [Using vended logs](vended-logs.md "vended-logs.md"). For [Enable vended logs in MediaTailor](vended-logs.md#vended-logs-config "vended-logs.md#vended-logs-config"), select _both_ logging strategies
   (**Vended logs** and **Legacy CloudWatch**).

MediaTailor will send logs through both vended logs and directly to CloudWatch Logs. 2. Make the necessary changes in your workflow that are dependent on your logging
strategy and delivery destination. 3. Revisit [Enable vended logs in MediaTailor](vended-logs.md#vended-logs-config "vended-logs.md#vended-logs-config") and remove **Legacy
CloudWatch** from the **Logging strategies**.
