# Configuring logging for Managed integrations

Managed integrations provides two types of logs delivered to Amazon CloudWatch Logs in your account:

- _Event logs_ – Cloud-side logs capturing events from managed integrations
  workflows. Written to the `/aws/iotmanagedintegrations/EventLog` log
  group.
- _Runtime logs_ – Device-side logs published by your devices or
  hubs. Written to the `/aws/iotmanagedintegrations/RuntimeLog` log
  group.
