# Configuring logging for Managed Integrations

Managed Integrations provides two types of logs delivered to Amazon CloudWatch Logs in your account:

- _Event logs_ – Cloud-side logs capturing events from Managed Integrations
  workflows. Written to the `/aws/iotmanagedintegrations/EventLog` log
  group.
- _Runtime logs_ – Device-side logs published by your devices or
  hubs. Written to the `/aws/iotmanagedintegrations/RuntimeLog` log
  group.
