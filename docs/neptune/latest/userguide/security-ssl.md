# Encrypting connections to your Amazon Neptune database with SSL/HTTPS

Beginning with [engine version 1.0.4.0](engine-releases-1.0.4.md "engine-releases-1.0.4.md"),
Amazon Neptune only allows Secure Sockets Layer (SSL) connections through HTTPS to any
instance or cluster endpoint.

Neptune requires at least TLS version 1.2, using the following strong cipher suites:

- `TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`
- `TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`
- `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`
- `TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`
  Starting with Neptune engine version 1.3.2.0, Neptune supports TLS version 1.3 using the following cipher suites:

- TLS_AES_128_GCM_SHA256
- TLS_AES_256_GCM_SHA384
  Even where HTTP connections are allowed in earlier engine versions,
  any DB cluster that uses a new DB cluster parameter group is required to
  use SSL by default. _To protect your data, Neptune endpoints in engine
  version `1.0.4.0` and above only support HTTPS requests._
  See [Using the HTTP REST endpoint to connect to a
  Neptune DB instance](access-graph-sparql-http-rest.md "access-graph-sparql-http-rest.md") for more information.

Neptune automatically provides SSL certificates for your Neptune DB instances. You don't
need to request any certificates. The certificates are provided when you create a new
instance.

Neptune assigns a single wildcard SSL certificate to the instances in your account for
each AWS Region. The certificate provides entries for the cluster endpoints, cluster read-only
endpoints, and instance endpoints.

###### Certificate Details

The following entries are included in the provided certificate:

- Cluster endpoint —
  `*.cluster-`a1b2c3d4wxyz`.`region`.neptune.amazonaws.com`
- Read-only endpoint —
  `*.cluster-ro-`a1b2c3d4wxyz`.`region`.neptune.amazonaws.com`
- Instance endpoints —
  `*.`a1b2c3d4wxyz`.`region`.neptune.amazonaws.com`
  Only the entries listed here are supported.

###### Proxy Connections

The certificates support only the hostnames that are listed in the previous section.

If you are using a load balancer or a proxy server (such as HAProxy), you must use SSL
termination and have your own SSL certificate on the proxy server.

SSL passthrough doesn't work because the provided SSL certificates don't match the proxy
server hostname.

###### Root CA Certificates

The certificates for Neptune instances are normally validated using the local trust
store of the operating system or SDK (such as the Java SDK).

If you need to provide a root certificate manually, you can download the [Amazon Root CA
certificate](https://www.amazontrust.com/repository/AmazonRootCA1.pem "https://www.amazontrust.com/repository/AmazonRootCA1.pem") in PEM format from the [Amazon Trust Services Policy
Repository](https://www.amazontrust.com/repository/ "https://www.amazontrust.com/repository/").

###### More Information

For more information about connecting to Neptune endpoints with SSL, see [Set up the Gremlin console to connect to a
Neptune DB instance](access-graph-gremlin-console.md "access-graph-gremlin-console.md") and [Using the HTTP REST endpoint to connect to a
Neptune DB instance](access-graph-sparql-http-rest.md "access-graph-sparql-http-rest.md").
