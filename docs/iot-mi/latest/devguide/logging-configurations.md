

# Configuring logging for Managed Integrations

Managed Integrations provides two types of logs delivered to Amazon CloudWatch Logs in your account:
+ *Event logs* – Cloud-side logs capturing events from Managed Integrations workflows. Written to the `/aws/iotmanagedintegrations/EventLog` log group.
+ *Runtime logs* – Device-side logs published by your devices or hubs. Written to the `/aws/iotmanagedintegrations/RuntimeLog` log group.