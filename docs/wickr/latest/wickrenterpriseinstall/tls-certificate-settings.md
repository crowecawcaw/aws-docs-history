This guide provides documentation for Wickr Enterprise. If you're using
AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md") or [AWS Wickr
User Guide](../userguide/what-is-wickr.md "../userguide/what-is-wickr.md").

# TLS certificate settings

Upload a PEM certificate and private key for terminating TLS. The Subject Alternative Name
on the certificate must match the hostname configured in the settings of your Wickr Enterprise
deployment.

For the certificate chain field, concatenate any intermediate certificates (if required)
with the root CA certificate **before uploading**.

## Let's Encrypt

Select this option to automatically generate a certificate using [Let's Encrypt](https://letsencrypt.org/ "https://letsencrypt.org/"). Certificates are issued using the [HTTP-01 challenge](https://letsencrypt.org/docs/challenge-types/#http-01-challenge "https://letsencrypt.org/docs/challenge-types/#http-01-challenge")
through the cert-manager operator.

The HTTP-01 challenge requires that the desired DNS name resolves to the ingress point for
your cluster (usually a Load Balancer), and traffic to TCP port 80 is open to the public. These
certificates are short-lived and will be renewed regularly. It is necessary to keep port 80 open
to allow the certificates to renew automatically.

###### Note

This section refers explicitly to the certificate used by the Wickr Enterprise
application itself.

## Pinned Certificate

Wickr Enterprise requires certificate pinning when using self-signed certificates or
certificates not trusted by client devices. If the certificate presented by your Load Balancer
is self-signed or is signed by a different CA than the Wickr Enterprise installation, upload
the CA certificate here to have clients pin to it instead.

In most situations, this setting is not required.

## Certificate Providers

If you plan to purchase a certificate for use with Wickr Enterprise see below for a list
of providers who’s certificates are known to function correctly by default. If a provider is
listed below their certificates have been validated with the software explicitly.

- Digicert
- RapidSSL

## Generating a self-signed

certificate

If you would like to create your own self signed certificate for use with Wickr
Enterprise, the example command below contains all required flags for generation.

```
openssl req -x509 -newkey rsa:4096 -sha256 -days 365 -nodes -keyout $YOUR_DOMAIN.key -out $YOUR_DOMAIN.crt -subj "/CN=$YOUR_DOMAIN" -addext "subjectAltName=DNS:$YOUR_DOMAIN" -addext "extendedKeyUsage = serverAuth"
```

If you would like to create an IP based self signed certificate, use the following command
instead. In order to use the IP based certificate, ensure that the Wildcard Hostname field is
enabled under Ingress settings. For more information, see [Ingress
settings](ingress-settings.md "ingress-settings.md").

```
openssl req -x509 -newkey rsa:4096 -sha256 -days 365 -nodes -keyout $YOUR_DOMAIN.key -out $YOUR_DOMAIN.crt -subj "/CN=$YOUR_DOMAIN" -addext "subjectAltName=IP:$YOUR_DOMAIN" -addext "extendedKeyUsage = serverAuth"
```

###### Note

Replace $YOUR_DOMAIN in the example with the domain name or IP address you intend to
use.
