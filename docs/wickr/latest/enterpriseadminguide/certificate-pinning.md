This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Certificate pinning

Certificate pinning is an online application security technique that accepts only authorized
pinned certificates for authentication of client-server connections. With certificate pinning,
the SSL certificate is hard-coded into application code. When the application communicates with
the server, it checks whether the same certificate is present.

- If certificate pinning is enabled, Wickr clients will ONLY trust and connect to
  Enterprise service hosts that present the specified certificate(s).
- If certificate pinning is disabled, Wickr clients will use the standard, platform-based
  certificate validation when connecting to their Enterprise host.

###### Note

Client platforms can vary in what they consider to be valid X.509 certificates. If you plan
on using a private certificate, (certificates not obtained from a Digital Certificate
Authority), we strongly recommend that you enable certificate pinning to ensure that your
certificate is trusted on all client platforms.
