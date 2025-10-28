This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Calling

The **Calling** section has the following available features for
users:

- **Audio Calling Control:** Disables calling for users. At a minimum users
  must be able to share audio to start or join a call. Enabled by default.
- **Video Calling Control:** Is used if disabled users cannot share their
  camera feed or their screen. Enabled by default.
- **Force TCP Calling:** Forces users to connect to calls over TCP instead
  of the default UDP connection. Clients will try UDP first and then fall back to TCP
  automatically, but this will save time for users if UDP is known to be blocked.
- **Use Hosted Federated Calls:** For Global Federation. Disabled by
  default. If this setting is enabled, users within the Enterprise deployment will connect to the
  external, federated infrastructure for calls instead of the local infrastructure. It is useful
  for isolated environments where outside users can't connect to the Enterprise
  infrastructure.
