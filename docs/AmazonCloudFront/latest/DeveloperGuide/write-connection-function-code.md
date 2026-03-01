# Write CloudFront Connection Function code for mutual TLS (viewer) validation

CloudFront Connection Functions enable you to write lightweight JavaScript functions for mTLS certificate validation and custom authentication logic. Your Connection Function code can validate client certificates, implement device-specific authentication rules, handle certificate revocation scenarios, and make allow/deny decisions for TLS connections at CloudFront edge locations worldwide.

Connection functions provide a powerful way to extend CloudFront's built-in certificate validation with your own business logic. Unlike viewer request and viewer response functions that process HTTP data, Connection Functions operate at the TLS layer and have access to certificate information, client IP addresses, and TLS connection details. This makes them ideal for implementing zero-trust security models, device authentication systems, and custom certificate validation policies that go beyond standard PKI validation.

Your Connection Function code runs in a secure, isolated environment with submillisecond startup times and can scale to handle millions of connections per second. The runtime is optimized for certificate validation workloads and provides built-in integration with CloudFront KeyValueStore for real-time data lookup operations, enabling sophisticated authentication scenarios like certificate revocation list checking and device allowlist validation.

To help you write effective Connection Function code, see the following topics. For complete code examples and step-by-step tutorials, see the tutorial sections in this guide and explore the Connection Function examples available in the CloudFront console.

###### Topics

- [CloudFront Connection Function use cases and purposes](#connection-function-use-cases "#connection-function-use-cases")
- [CloudFront Connection Function event structure and response format](#connection-function-event-structure "#connection-function-event-structure")
- [CloudFront Connection Functions JavaScript runtime features](#connection-function-javascript-runtime "#connection-function-javascript-runtime")
- [CloudFront Connection Function helper methods and APIs](#connection-function-helper-methods "#connection-function-helper-methods")
- [CloudFront Connection Function KeyValueStore integration](#connection-function-kvs-integration "#connection-function-kvs-integration")
- [Use async and await](#connection-function-async-await "#connection-function-async-await")
- [Connection function code examples](#connection-function-code-examples "#connection-function-code-examples")

## CloudFront Connection Function use cases and purposes

Before writing your CloudFront Connection Function, carefully determine what type of
certificate validation or authentication logic you need to implement. Connection
functions are designed for specific use cases that require custom validation beyond
standard PKI certificate checking. Understanding your use case helps you design
efficient code that meets your security requirements while maintaining optimal
performance.

Common Connection Function use cases include:

- **Certificate revocation handling** –
  Implement custom policies for handling revoked certificates, including grace
  periods for certificate rotation, trusted network exceptions for internal
  devices, or emergency access scenarios where revoked certificates might need
  temporary access.
- **Optional mTLS support** – Handle both mTLS
  and non-mTLS connections with different authentication policies, allowing
  you to provide enhanced security for clients that support certificates while
  maintaining compatibility with legacy clients.
- **IP-based authentication** – Combine
  certificate validation with client IP address checks for enhanced security,
  such as restricting access from specific geographic regions, corporate
  networks, or known malicious IP ranges.
- **Multi-tenant certificate validation** –
  Implement tenant-specific validation rules where different certificate
  authorities or validation criteria apply based on the client certificate
  issuer or subject attributes.
- **Time-based access control** – Enforce
  time-based restrictions where certificates are only valid during specific
  hours, maintenance windows, or business periods, even if the certificate
  itself hasn't expired.

Connection functions run after CloudFront performs standard certificate validation
(trust chain verification, expiry checks, and signature validation) but before the
TLS connection is established. This timing gives you the flexibility to add custom
validation criteria while benefiting from CloudFront's built-in certificate validation.
Your function receives the results of standard validation and can make informed
decisions about whether to allow or deny the connection based on both standard and
custom criteria.

When designing your Connection Function, consider the performance implications of
your validation logic. Functions have a 5-millisecond execution limit, so complex
operations should be optimized for speed. Use KeyValueStore for fast data lookups
rather than complex calculations, and structure your validation logic to fail fast
for invalid certificates.

## CloudFront Connection Function event structure and response format

CloudFront Connection Functions receive a different event structure than viewer request
and viewer response functions. Instead of HTTP request/response data, connection
functions receive certificate and connection information that you can use to make
authentication decisions.

###### Topics

- [Event structure for Connection Functions](#connection-function-event-structure-details "#connection-function-event-structure-details")
- [Connection Functions response format](#connection-function-response-format "#connection-function-response-format")

### Event structure for Connection Functions

Connection Functions receive an event object that contains certificate and
connection information. The event structure of the function is shown
below:

```
{
  "clientCertificate": {
    "certificates": {
      "leaf": {
        "serialNumber": "string",
        "issuer": "string",
        "subject": "string",
        "validity": {
          "notBefore": "string",
          "notAfter": "string",
        },
        "sha256Fingerprint": "string"
      }
    }
  },
  "clientIp": "string",
  "endpoint": "string",
  "distributionId": "string",
  "connectionId": "string"
}
```

Below is an example of the event object structure:

```
{
  "clientCertificate": {
    "certificates": {
      "leaf": {
        "serialNumber": "00:9e:2a:af:16:56:e5:47:25:7d:2e:38:c3:f9:9d:57:fa",
        "issuer": "C=US, O=Ram, OU=Edge, ST=WA, CN=mTLS-CA, L=Snoqualmie",
        "subject": "C=US, O=Ram, OU=Edge, ST=WA, CN=mTLS-CA, L=Snoqualmie",
        "validity": {
          "notBefore": "2025-09-10T23:43:10Z",
          "notAfter": "2055-09-11T00:43:02Z"
        },
        "sha256Fingerprint": "_w6bJ7aOAlGOj7NUhJxTfsfee-ONg_xop3_PTgTJpqs="
      }
    }
  },
  "clientIp": "127.0.0.1",
  "endpoint": "d3lch071jze0cb.cloudfront.net",
  "distributionId": "E1NXS4MQZH501R",
  "connectionId": "NpvTe1925xfj24a67sPQr7ae42BIq03FGhJJKfrQYWZcWZFp96SIIg=="
}
```

### Connection Functions response format

Your Connection Function must return a response object that indicates whether
to allow or deny the connection. Use the helper methods to make connection
decisions:

```
function connectionHandler(connection) {
    // Helper methods to allow or deny connections
    if (/* some logic to determine if function should allow connection */) {
        connection.allow();
    } else {
        connection.deny();
    }
}
```

Unlike viewer request and viewer response functions, Connection Functions
cannot modify HTTP requests or responses. They can only allow or deny the TLS
connection.

## CloudFront Connection Functions JavaScript runtime features

CloudFront Connection Functions use the CloudFront Functions JavaScript runtime 2.0, which
provides a secure and high-performance environment specifically optimized for
certificate validation workloads. The runtime is designed to start in
sub-milliseconds and handle millions of concurrent executions across CloudFront's global
edge network.

The runtime environment includes comprehensive JavaScript language support:

- **ECMAScript 2020 (ES11) support** – Modern
  JavaScript features including optional chaining (?.), nullish coalescing
  (??), and BigInt for handling large certificate serial numbers
- **Built-in objects** – Standard JavaScript
  objects like Object, Array, JSON, Math, and Date
- **Console logging** – Use console.log() for
  debugging and monitoring certificate validation decisions. Logs are
  available in real-time during testing and can help troubleshoot validation
  logic in development
- **KeyValueStore integration** – Native access
  to CloudFront KeyValueStore for ultra-fast data lookup operations, enabling
  real-time certificate revocation checking, device allowlist validation, and
  tenant-specific configuration retrieval

Connection functions are optimized for high-performance for certificate validation
scenarios. The runtime automatically handles memory management, garbage collection,
and resource cleanup to ensure consistent performance across millions of concurrent
connections. All operations are designed to be deterministic and fast, with
KeyValueStore lookups typically completing in microseconds.

The runtime environment is completely isolated between function executions,
ensuring that no data leaks between different client connections. Each function
execution starts with a clean state and has no access to previous execution results
or client data from other connections.

## CloudFront Connection Function helper methods and APIs

CloudFront Connection Functions provide specialized helper methods designed to simplify
certificate validation decisions and enhance observability. These methods are
optimized for the connection validation workflow and integrate seamlessly with
CloudFront's connection logging and monitoring systems.

- **connection.allow()** – Allow the TLS
  connection to proceed. This method signals CloudFront to complete the TLS
  handshake and allow the client to establish the connection. Use this when
  certificate validation passes and any custom authentication logic is
  satisfied
- **connection.deny()** – Deny the TLS
  connection and terminate the handshake. This method immediately closes the
  connection and prevents any HTTP traffic from flowing. The client will
  receive a TLS connection error. Use this for invalid certificates, failed
  authentication, or policy violations
- **connection.logCustomData()** – Add custom
  data to connection logs (up to 800 bytes of UTF-8 text). This method allows
  you to include validation results, certificate details, or decision
  rationale in CloudFront connection logs for security monitoring, compliance
  auditing, and troubleshooting

These methods provide a clean, declarative interface for making connection
decisions and logging relevant information for monitoring and debugging. The
allow/deny pattern ensures that your function's intent is clear and that CloudFront can
optimize connection handling based on your decision. Custom logging data is
immediately available in CloudFront connection logs and can be used with log analysis
tools for security monitoring and operational insights.

Always call either connection.allow() or connection.deny() before your function
completes. If neither method is called, CloudFront will deny the connection by default as
a security precaution.

## CloudFront Connection Function KeyValueStore integration

CloudFront Connection Functions can use CloudFront KeyValueStore to perform ultra-fast data
lookups for certificate validation scenarios. KeyValueStore is particularly powerful
for Connection Functions because it provides global, eventually-consistent data
access with microsecond lookup times across all CloudFront edge locations. This makes it
ideal for maintaining certificate revocation lists, device allowlists, tenant
configurations, and other validation data that needs to be accessible during TLS
handshakes.

KeyValueStore integration is designed specifically for high-performance connection
validation workflows:

- **kvsHandle.exists(key)** – Check if a key
  exists in the KeyValueStore without retrieving the value. This is the most
  efficient method for binary validation scenarios like certificate revocation
  checking, where you only need to know if a certificate serial number is in a
  revocation list
- **kvsHandle.get(key)** – Retrieve a value
  from the KeyValueStore for more complex validation scenarios. Use this when
  you need to access configuration data, validation rules, or metadata
  associated with a certificate or device identifier

KeyValueStore operations are asynchronous and must be used with async/await
syntax. The KeyValueStore has a 10MB total size limit and supports up to 10 million
key-value pairs. KeyValueStore data is eventually consistent across all edge
locations, with updates typically propagating within seconds.

For optimal performance, structure your KeyValueStore keys to minimize lookup
operations. Use certificate serial numbers as keys for simple revocation checking,
or create composite keys combining issuer hash and serial number for multi-CA
environments. Consider the trade-offs between key complexity and KeyValueStore
capacity when designing your data structure.

## Use async and await

Connection functions support asynchronous operations using async/await syntax,
which is essential when working with KeyValueStore operations or other asynchronous
tasks. The async/await pattern ensures that your function waits for KeyValueStore
lookups to complete before making connection decisions, while maintaining the
high-performance characteristics required for TLS handshake processing.

Proper async/await usage is critical for Connection Functions because
KeyValueStore operations, while very fast, are still network operations that require
coordination across CloudFront's distributed infrastructure. The runtime automatically
handles promise resolution and ensures that your function completes within the
5-millisecond execution limit.

###### Example: Async Connection Function with KeyValueStore

```
import cf from 'cloudfront';

async function connectionHandler(connection) {
    const kvsHandle = cf.kvs();

    // Async operation to check KeyValueStore for certificate revocation
    const isRevoked = await kvsHandle.exists(connection.clientCertificate.certificates.leaf.serialNumber);

    if (isRevoked) {
        // Log the revocation decision with certificate details
        connection.logCustomData(`REVOKED_CERT:${connection.clientCertificate.certificates.leaf.serialNumber}:${connection.clientCertificate.certificates.leaf.issuer}`);
        console.log(`Denying connection for revoked certificate: ${connection.clientCertificate.certificates.leaf.serialNumber}`);
        return connection.deny();
    }

    // Log successful validation for monitoring
    connection.logCustomData(`VALID_CERT:${connection.clientCertificate.certificates.leaf.serialNumber}`);
    console.log(`Allowing connection for valid certificate: ${connection.clientCertificate.certificates.leaf.serialNumber}`);
    return connection.allow();
}
```

Always use async/await when calling KeyValueStore methods or other asynchronous
operations. The Connection Function runtime handles promise resolution automatically
and ensures proper execution flow within the strict timing constraints of TLS
handshake processing. Avoid using .then() or callback patterns, as async/await
provides cleaner error handling and better performance in the Connection Function
environment.

When designing async Connection Functions, structure your code to minimize the
number of KeyValueStore operations and perform them as early as possible in your
validation logic. This ensures maximum performance and reduces the risk of timeout
issues during high-traffic periods. Consider batching related validation checks and
using the most efficient KeyValueStore method (exists() vs get()) for your use
case.

## Connection function code examples

The following examples demonstrate common Connection Function patterns for
different validation scenarios. Use these examples as starting points for your own
Connection Function implementations.

###### Example: Device certificate validation

This example validates device serial numbers and certificate subject fields
for IoT devices, gaming consoles, and other client authentication
scenarios:

```
async function connectionHandler(connection) {
    // Custom validation: check device serial number format
    const serialNumber = connection.clientCertificate.certificates.leaf.serialNumber;
    if (!serialNumber.startsWith("DEV")) {
        connection.logCustomData(`INVALID_SERIAL:${serialNumber}`);
        return connection.deny();
    }

    // Validate certificate subject contains required organizational unit
    const subject = connection.clientCertificate.certificates.leaf.subject;
    if (!subject.includes("OU=AuthorizedDevices")) {
        connection.logCustomData(`INVALID_OU:${subject}`);
        return connection.deny();
    }

    // Allow connection for valid devices
    connection.logCustomData(`VALID_DEVICE:${serialNumber}`);
    return connection.allow();
}
```

This function performs multiple validation checks beyond standard certificate
validation, including device serial number format and organizational unit
verification.

###### Example: Optional mTLS with mixed authentication

This example handles both mTLS and non-mTLS connections with different
authentication policies:

```
async function connectionHandler(connection) {
    if (connection.clientCertificate) {
        // mTLS connection - enhanced validation for certificate holders
        const subject = connection.clientCertificate.certificates.leaf.subject;
        connection.logCustomData(`MTLS_SUCCESS:${subject}:${connection.clientIp}`);
        console.log(`mTLS connection from: ${subject}`);
        return connection.allow();
    } else {
        // Non-mTLS connection - apply IP-based restrictions
        const clientIp = connection.clientIp;

        // Only allow non-mTLS from specific IP ranges
        if (clientIp.startsWith("203.0.113.") || clientIp.startsWith("198.51.100.")) {
            connection.logCustomData(`NON_MTLS_ALLOWED:${clientIp}`);
            console.log(`Non-mTLS connection allowed from: ${clientIp}`);
            return connection.allow();
        }

        connection.logCustomData(`NON_MTLS_DENIED:${clientIp}`);
        return connection.deny();
    }
}
```

This function provides enhanced security for clients with certificates while maintaining compatibility with
legacy clients from trusted IP ranges.
