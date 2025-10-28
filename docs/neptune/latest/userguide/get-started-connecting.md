# Connecting to an Amazon Neptune cluster

After creating a Neptune cluster, you can configure the connection methods to access it.

## Setting up `curl` or awscurl

to communicate with your Neptune endpoint

Having a command-line tool for submitting queries to your Neptune DB cluster
is very handy, as illustrated in many of the examples in this documentation. The [curl](https://curl.haxx.se/ "https://curl.haxx.se/") command line tool is an excellent option for
communicating with Neptune endpoints when IAM authentication is not enabled.
Versions starting with 7.75.0 support the `--aws-sigv4` option for
signing requests when IAM authentication is enabled.

For endpoints where IAM authentication _is_ enabled, you can
also use [awscurl](https://github.com/okigan/awscurl "https://github.com/okigan/awscurl"), which uses almost
exactly the same syntax as `curl` but supports signing requests as required
for IAM authentication. Because of the added security that IAM authentication
provides, it is generally a good idea to enable it.

For information about how to use `curl` (or `awscurl`),
see the [curl man page](https://curl.haxx.se/docs/manpage.html "https://curl.haxx.se/docs/manpage.html"),
and the book _[Everything curl](https://ec.haxx.se/ "https://ec.haxx.se/")_.

To connect using HTTPS (which Neptune requires), `curl` needs access
to appropriate certificates. As long as `curl` can locate the appropriate
certificates, it handles HTTPS connections just like HTTP connections, without extra
parameters. The same is true for `awscurl`. Examples in this documentation
are based on that scenario.

To learn how to obtain such certificates and how to format them properly into
a certificate authority (CA) certificate store that `curl` can use, see
[SSL Certificate Verification](https://curl.haxx.se/docs/sslcerts.html "https://curl.haxx.se/docs/sslcerts.html")
in the `curl` documentation.

You can then specify the location of this CA certificate store using the
`CURL_CA_BUNDLE` environment variable. On Windows, `curl`
automatically looks for it in a file named `curl-ca-bundle.crt`. It looks first in
the same directory as `curl.exe` and then elsewhere on the path. For more
information, see [SSL Certificate
Verification](https://curl.haxx.se/docs/sslcerts.html "https://curl.haxx.se/docs/sslcerts.html").

## Different ways to connect to a Neptune DB cluster

An Amazon Neptune DB cluster can _only_ be created in an Amazon Virtual Private Cloud
(Amazon VPC). Unless you enable and set up Neptune public endpoints for the DB cluster, its
endpoints are accessible within that VPC or using a public endpoint.

There are several different ways to set up access to your Neptune DB cluster in
its VPC:

- [Connecting from an Amazon EC2 instance in the same VPC](get-started-connect-ec2-same-vpc.md "get-started-connect-ec2-same-vpc.md")
- [Connecting from an Amazon EC2 instance in another VPC](get-started-connect-ec2-other-vpc.md "get-started-connect-ec2-other-vpc.md")
- [Connecting from a private network](get-started-connect-private-net.md "get-started-connect-private-net.md")
- [Connecting from a public endpoint](neptune-public-endpoints.md "neptune-public-endpoints.md")
