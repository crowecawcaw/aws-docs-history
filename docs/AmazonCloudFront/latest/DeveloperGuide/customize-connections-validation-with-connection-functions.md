# Customize with CloudFront Connection Functions

CloudFront Connection Functions allow you to write lightweight JavaScript functions for mTLS
certificate validation and custom authentication logic. Your Connection Functions run
during mTLS connection establishment to validate client certificates, implement
device-specific authentication rules, and handle certificate revocation scenarios. The
Connection Functions runtime environment offers submillisecond startup times, scales
immediately to handle millions of connections per second, and is highly secure.
Connection Functions are a native feature of CloudFront, which means you can build, test, and
deploy your code entirely within CloudFront.

When you associate a Connection Function with an mTLS-enabled CloudFront distribution, CloudFront intercepts TLS connection requests at CloudFront edge locations and passes certificate information to your function. You can invoke Connection Functions when the following event occurs:

- During TLS connection establishment (connection request) - for mutual TLS (mTLS) connections
  For more information about Connection Functions, see the following topics.

###### Topics

- [Overview and workflow](connection-functions-overview.md "connection-functions-overview.md")
- [Configuration and limits](connection-function-configuration-limits.md "connection-function-configuration-limits.md")
- [Create CloudFront Connection Functions for mutual TLS (viewer) validation](create-connection-functions.md "create-connection-functions.md")
- [Write CloudFront Connection Function code for mutual TLS (viewer) validation](write-connection-function-code.md "write-connection-function-code.md")
- [Test CloudFront Connection Functions before deployment](test-connection-functions.md "test-connection-functions.md")
- [Associate Connection Functions with distributions](associate-connection-functions.md "associate-connection-functions.md")
- [Implement certificate revocation for mutual TLS (viewer) with CloudFront Functions and KeyValueStore](implement-certificate-revocation.md "implement-certificate-revocation.md")
