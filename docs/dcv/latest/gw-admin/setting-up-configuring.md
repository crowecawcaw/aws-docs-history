# Configuring the Amazon DCV Connection Gateway

This section describes how to configure the Amazon DCV Connection Gateway. It introduces the _configuration
file_ used by the Connection Gateway and describes the basic configuration required to run the Connection Gateway service.
For more information about all the available configuration options, see the
[Configuration File Reference](config-reference.md "config-reference.md") section.

The Amazon DCV Connection Gateway configuration file is located at `/etc/dcv-connection-gateway/dcv-connection-gateway.conf`.
The file uses the [TOML format](https://toml.io "https://toml.io") and is organized in sections which control different aspects of the Connection Gateway.

You can edit the configuration file using your preferred text editor.

A basic configuration file will have the following content.

```
[gateway]
web-listen-endpoints = ["0.0.0.0:8443", "[::]:8445"]
quic-listen-endpoints = ["0.0.0.0:8443"]

[resolver]
url = "https://localhost:8081"

[web-resources]
url = "https://localhost:8080"

```

## Configuring the Connection Gateway Listener

The `[gateway]` section controls how the Amazon DCV Connection Gateway accepts incomig connections from the clients.

```
[gateway]
web-listen-endpoints = ["0.0.0.0:8443", "[::]:8445"]
quic-listen-endpoints = ["0.0.0.0:8443"]
...

```

This section includes two parameters: `web-listen-endpoints` and `quic-listen-endpoints`
which define the list of TCP and UDP endpoints (respectively) that the Connection Gateway service will bind to and listen on.
In the above example, the Connection Gateway is configured to listen for incoming TCP connections on all available IPv4 addresses on TCP port `8443`,
and on all available IPv6 addresses on port `8445`.
Also, the Connection Gateway is configured to listen for incoming UDP connections on all available IPv4 addresses on UDP port `8443`.
The `web-listen-endpoints` parameter is required to be set and non-empty.
If the `quic-listen-endpoint` parameter is not set or empty, QUIC support is disabled.

This section also allows you to configure the certificates that Amazon DCV Connection Gateway presents to the clients:

```
[gateway]
cert-file = "/path/to/cert.pem"
cert-key-file = "/path/to/key.pem"
...

```

`cert-file` and `cert-key-file` respectively specify the path of the x.509 public certificate in PEM format
and the path of the file containing the private SSL key in PKCS8 representation. If these parameters are not specified, the Connection Gateway
will generate and use a _self-signed_ certificate.

## Configuring the Session Resolver

The `[resolver]` section controls how the Amazon DCV Connection Gateway interacts with a _Session Resolver_
responsible for mapping _Session IDs_ to a destination host running the Amazon DCV server

```
...
[resolver]
url = "https://localhost:8081"
...

```

This section includes a _mandatory_ `url` parameter which specifies the
HTTP end-point of the resolver. See [Implementing a Session Resolver](session-resolver.md#implementing-session-resolver "session-resolver.md#implementing-session-resolver")
for more information about the implementation of this end-point.

Depending on where your session resolver end-point is located and how it authenticates connections, you may
need to specify additional configuration parameters: in particular if the end point has a certificate signed by
a private Certification Authority, you may provide the corresponding `ca-file` with the path of the x.509 CA
certificate in PEM format:

```
...
[resolver]
ca-file = "/path/to/resolver_ca.pem"
...

```

Or if it fits your security requirements, you can accept untrusted certificates:

```
...
[resolver]
tls-strict = false
...

```

If the session resolver HTTP end-point is configured to require mutual TLS authentication,
you will also need to specify the certificate and key that the Connection Gateway uses to prove its identity to
the resolver. These files can be the same as the ones specified in the `[gateway]` section.

```
...
[resolver]
cert-file = "/path/to/cert.pem"
cert-key-file = "/path/to/key.pem"
...

```

## Configuring the DCV target servers

The `[dcv]` section allows to specify options used by the Amazon DCV Connection Gateway to connect to the Amazon DCV server hosts.

If you are using the Amazon DCV server with the automatically generated self-signed certificates, you can use the `tls-strict`
setting to allow the Connection Gateway to connect:

```
...
[dcv]
tls-strict = false
...

```

Similarly to the `[resolver]` section, you can also use the `ca-file` setting if your fleet of
DCV servers use certificates signed by a private Certificate Authority.

The `[web-resources]` section controls how the Amazon DCV Connection Gateway forwards HTTP requests to an external Web Server.
In particular, the Web Server is used to host the files of a DCV Web Client, so that when a browser connects to the Connection Gateway it can
retrieve the `html`, `css` and `javascript` files of the DCV Web Client.

```
...
[web-resources]
url = "https://localhost:8080"
...

```
