

# Best practices for TLS certificate verification in Amazon MQ for RabbitMQ
<a name="verify-broker-certificate-rabbitmq"></a>

Amazon MQ brokers present a server certificate that identifies the broker by its fully qualified domain name (FQDN). Your client is responsible for verifying this certificate when it establishes a TLS connection.

**Example FQDN:**

```
b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9.mq.ap-southeast-2.amazonaws.com
```

We recommend that you configure your client to verify the broker certificate as described in [RFC 9525, Service Identity in TLS](https://www.rfc-editor.org/rfc/rfc9525.html). When your client connects to an Amazon MQ broker, it should do the following:
+ **Use the broker endpoint FQDN as the reference identifier.** Use the FQDN from the broker endpoint returned by the `DescribeBroker` operation, or shown on the broker details page in the Amazon MQ console. Do not derive the identifier from an IP address or from a DNS alias of your own.
+ **Verify the identifier against the `subjectAltName` extension.** Match the broker FQDN against the `dNSName` entries in the certificate `subjectAltName` (SAN) extension.
+ **Do not use the Common Name (CN).** The CN does not identify the broker, and it cannot contain the broker FQDN. Clients that match only the CN, or that require a specific value in the CN, might fail to connect.

**Important**  
Do not disable certificate verification, and do not pin an individual broker certificate or a specific certificate subject. Amazon MQ rotates broker certificates, and the contents of the certificate subject can change. Clients that pin a certificate or a subject value might fail to connect after a certificate is rotated.

**Note**  
Most TLS client libraries verify the broker FQDN against the `subjectAltName` extension by default when you supply the broker endpoint host name. If your client overrides the verification hostname, or supplies its own verification callback, make sure that it uses the broker FQDN and matches against `subjectAltName`.

For more information about Amazon MQ broker certificates, including the certificate types that Amazon MQ issues and annotated examples of each, see [Amazon MQ broker TLS certificates](amazon-mq-certificates.md).