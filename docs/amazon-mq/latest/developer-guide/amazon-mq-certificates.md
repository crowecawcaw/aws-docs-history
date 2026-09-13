

# Amazon MQ broker TLS certificates
<a name="amazon-mq-certificates"></a>

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

The rest of this topic describes the certificate that the broker presents in more detail.

## Broker identity
<a name="amazon-mq-certificates-broker-identity"></a>

A broker is identified by its fully qualified domain name (FQDN). Obtain the FQDN from the broker endpoint, which is available from the `DescribeBroker` operation in `BrokerInstances[].Endpoints`, and from the **Endpoint** field on the broker details page in the Amazon MQ console. Broker endpoints are full URIs, for example:

```
amqps://b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9.mq.ap-southeast-2.amazonaws.com:5671
```

In this example the broker FQDN is `b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9.mq.ap-southeast-2.amazonaws.com`. The endpoint is different for every broker and every AWS Region, so use the value that Amazon MQ advertises for the specific broker that you are connecting to. Do not derive the identifier from an IP address or from a DNS alias of your own.

## Certificate types
<a name="amazon-mq-certificates-types"></a>

To enhance security, Amazon MQ is replacing shared regional wildcard certificates with a separate certificate for each broker.
+ **Per-broker certificate.** A certificate issued for a single broker. The broker FQDN appears in the `subjectAltName` (SAN) extension.
+ **Regional wildcard certificate (legacy).** A certificate shared by the brokers in an AWS Region, whose only `subjectAltName` entry is a wildcard name. This certificate type is being retired.

Verifying the broker FQDN against the `subjectAltName` extension, as described in this topic, works with both certificate types.

## Common name and subject alternative names
<a name="amazon-mq-certificates-subject"></a>

The certificate Common Name (CN) is limited to 64 characters, which a broker FQDN can exceed. On a per-broker certificate the CN therefore contains an opaque label, and the broker FQDN is present in the `subjectAltName` (SAN) extension.

The SAN extension is the field used for hostname verification. The following example shows the relevant fields of a per-broker certificate. The broker FQDN appears as a `DNS` entry in `subjectAltName`, and not in the CN.

```
Issuer: C=US, O=Amazon, CN=Amazon RSA 2048 M01
Subject: CN=3vmdzfkzqk64xsf3uxk6szu0wiv59w8t.mq.ap-southeast-2.amazonaws.com
X509v3 Subject Alternative Name:
    DNS:3vmdzfkzqk64xsf3uxk6szu0wiv59w8t.mq.ap-southeast-2.amazonaws.com,
    DNS:b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9.mq.ap-southeast-2.amazonaws.com
X509v3 Extended Key Usage: TLS Web Server Authentication
X509v3 Basic Constraints: critical
    CA:FALSE
```

For comparison, a legacy regional wildcard certificate carries the wildcard name in both the CN and the SAN extension, and does not contain any broker FQDN:

```
Issuer: C=US, O=Amazon, CN=Amazon RSA 2048 M01
Subject: CN=*.mq.ap-southeast-2.amazonaws.com
X509v3 Subject Alternative Name:
    DNS:*.mq.ap-southeast-2.amazonaws.com
X509v3 Extended Key Usage: TLS Web Server Authentication
X509v3 Basic Constraints: critical
    CA:FALSE
```

Amazon MQ for ActiveMQ certificates additionally cover the per-instance host names that an active/standby deployment uses, so a client connecting through the Failover Transport verifies successfully against whichever endpoint it uses:

```
X509v3 Subject Alternative Name:
    DNS:3vmdzfkzqk64xsf3uxk6szu0wiv59w8t.mq.ap-southeast-2.amazonaws.com,
    DNS:b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9.mq.ap-southeast-2.amazonaws.com,
    DNS:b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9-1.mq.ap-southeast-2.amazonaws.com,
    DNS:b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9-2.mq.ap-southeast-2.amazonaws.com
```