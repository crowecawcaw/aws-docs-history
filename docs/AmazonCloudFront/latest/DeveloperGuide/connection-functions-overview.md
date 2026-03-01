# Overview and workflow

CloudFront Connection Functions are a specialized type of CloudFront Functions that run during the TLS handshake when a client attempts to establish an mTLS connection. Your Connection Function can access client certificate information, mTLS configuration parameters, certificate revocation check results, and the client IP address.

Connection functions are invoked after CloudFront performs standard certificate validation (trust chain, expiry, signature verification) but can run even if certificate revocation checks fail. This allows you to implement custom logic for handling revoked certificates or adding additional validation criteria.

After you create and publish a Connection Function, make sure to add an association for the connection request event type with an mTLS-enabled distribution. This makes the function run each time a client attempts to establish an mTLS connection with CloudFront.

CloudFront Connection Functions follow a two-stage lifecycle that allows you to develop and test functions before deploying them to production. This workflow ensures that your Connection Functions work correctly before they affect live traffic.

###### Topics

- [Function stages](#connection-function-stages "#connection-function-stages")
- [Development workflow](#connection-function-development-workflow "#connection-function-development-workflow")
- [Differences from other function types](#connection-function-differences "#connection-function-differences")

## Function stages

Connection functions exist in one of two stages:

- **DEVELOPMENT** – Functions in this stage can
  be modified, tested, and updated. Use this stage for writing and debugging
  your function code.
- **LIVE** – Functions in this stage are
  read-only and handle production traffic. You cannot modify functions in the
  LIVE stage directly.

When you create a new Connection Function, it starts in the
**DEVELOPMENT** stage. After testing and validation, you
publish the function to move it to the **LIVE** stage.

## Development workflow

Follow this workflow to develop and deploy Connection Functions:

1. **Create** – Create a new Connection Function
   in the DEVELOPMENT stage with your initial code and configuration.
2. **Test** – Use the test functionality to
   validate your function with sample connection events before
   deployment.
3. **Update** – Modify the function code and
   configuration as needed based on test results.
4. **Publish** – When ready for production,
   publish the function to move it from DEVELOPMENT to LIVE stage.
5. **Associate** – Associate the published
   function with your mTLS-enabled distribution to handle live
   connections.

To make changes to a LIVE function, you must update the DEVELOPMENT version and
publish it again. This creates a new version in the LIVE stage.

## Differences from other function types

Connection functions differ from viewer request and viewer response functions in
several important ways:

- Connection functions run after the mTLS handshake, before any HTTP
  processing occurs
- Connection functions have access to TLS certificate information instead of
  HTTP request/response data
- Connection functions can only allow or deny the connection, not modify
  HTTP data
- Connection functions are only invoked for new TLS connections, not for
  connection reuse
- TLS session resumption is not supported with mTLS to ensure certificate
  validation occurs on every connection
- Connection functions run in addition to standard viewer request and viewer
  response functions
- You associate Connection Functions at the distribution level, instead of
  at the cache behavior level.
- Connection functions only support JavaScript runtime 2.0.
