This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Custom TCP calling port

Calling and messaging services in Wickr Enterprise utilize the same TCP port 443. To
prevent collision when deploying Wickr Enterprise in Low Resource Mode, a custom calling port
must be configured.

The Replicated console provides a configuration field `callingTcpPort`, which you
must set before deploying the service. If no value is specified, the default is TCP 443. This
extra field is passed into Wickr's calling service as an environment variable. Any firewalls in
place must support inbound traffic on that port. Dynamic port changes are not supported. If an
administrator changes the `callingTcpPort` value, it is necessary to restart the
Orville and TCPProxy pods.
