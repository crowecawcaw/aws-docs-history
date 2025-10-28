# Creating and configuring

customer managed domains

Domain configurations let you specify a custom fully qualified domain name (FQDN) to
connect to AWS IoT Core. There are many benefits of using customer managed domains (also
known as custom domains): you can expose your own domain or your company's own domain to
customers for branding purposes; you can easily change your own domain to point to a new
broker; you can support multi-tenancy to serve customers with different domains within
the same AWS account; and you can manage your own server certificates details, such as
the root certificate authority (CA) used to sign the certificate, the signature
algorithm, the certificate chain depth, and the lifecycle of the certificate.

The workflow to set up a domain configuration with a custom domain consists of the
following three stages.

1. [Registering Server Certificates in AWS Certificate Manager](#iot-custom-endpoints-configurable-custom-register-certificate "#iot-custom-endpoints-configurable-custom-register-certificate")
2. [Creating a Domain Configuration](#iot-custom-endpoints-configurable-custom-domain-config "#iot-custom-endpoints-configurable-custom-domain-config")
3. [Creating DNS
   Records](#iot-custom-endpoints-configurable-custom-dns "#iot-custom-endpoints-configurable-custom-dns")

## Registering server certificates in AWS certificate manager

Before you create a domain configuration with a custom domain, you must register
your server certificate chain in [AWS Certificate Manager (ACM)](../../../acm/latest/userguide/acm-overview.md "../../../acm/latest/userguide/acm-overview.md"). You can use the following three types of server
certificates.

- [ACM Generated Public Certificates](#iot-custom-endpoints-configurable-custom-register-certificate-acm "#iot-custom-endpoints-configurable-custom-register-certificate-acm")
- [External Certificates Signed by a Public CA](#iot-custom-endpoints-configurable-custom-register-certificate-pubext "#iot-custom-endpoints-configurable-custom-register-certificate-pubext")
- [External Certificates Signed by a Private CA](#iot-custom-endpoints-configurable-custom-register-certificate-privext "#iot-custom-endpoints-configurable-custom-register-certificate-privext")

###### Note

AWS IoT Core considers a certificate to be signed by a public CA if it's included
in [Mozilla's trusted ca-bundle](https://hg.mozilla.org/mozilla-central/raw-file/tip/security/nss/lib/ckfw/builtins/certdata.txt?raw=1 "https://hg.mozilla.org/mozilla-central/raw-file/tip/security/nss/lib/ckfw/builtins/certdata.txt?raw=1").

### Certificate requirements

See [Prerequisites for Importing Certificates](../../../acm/latest/userguide/import-certificate-prerequisites.md "../../../acm/latest/userguide/import-certificate-prerequisites.md") for the requirements
for importing certificates into ACM. In addition to these requirements,
AWS IoT Core adds the following requirements.

- The leaf certificate must include the **Extended Key Usage** x509
  v3 extension with a value of **serverAuth**
  (TLS Web Server Authentication). If you request the certificate from
  ACM, this extension is automatically added.
- The maximum certificate chain depth is 5 certificates.
- The maximum certificate chain size is 16KB.
- The cryptographic algorithms and key sizes that are supported include RSA 2048 bit (RSA_2048)
  and ECDSA 256 bit (EC_prime256v1).

### Using one certificate for multiple domains

If you plan to use one certificate to cover multiple subdomains, use a
wildcard domain in the common name (CN) or Subject Alternative Names (SAN)
field. For example, use `*.iot.example.com` to cover
dev.iot.example.com, qa.iot.example.com, and prod.iot.example.com. Each FQDN
requires its own domain configuration, but more than one domain configuration
can use the same wildcard value. Either the CN or the SAN must cover the FQDN
that you want to use as a custom domain. If SANs are present, the CN is ignored
and a SAN must cover the FQDN that you want to use as a custom domain. This
coverage can be an exact match or a wildcard match. After a wildcard certificate
has been validated and registered to an account, other accounts in the region
are blocked from creating custom domains that overlap with the
certificate.

The following sections describe how to get each type of certificate. Every
certificate resource requires an Amazon Resource Name (ARN) registered with ACM
that you use when you create your domain configuration.

### ACM-generated public certificates

You can generate a public certificate for your custom domain by using the
[RequestCertificate](../../../acm/latest/APIReference/API_RequestCertificate.md "../../../acm/latest/APIReference/API_RequestCertificate.md") API. When you generate a certificate in this
way, ACM validates your ownership of the custom domain. For more
information, see [Request
a Public Certificate](../../../acm/latest/userguide/gs-acm-request-public.md "../../../acm/latest/userguide/gs-acm-request-public.md") in the
_AWS Certificate Manager User Guide_.

### External certificates signed by a public CA

If you already have a server certificate that is signed by a public CA (a
CA that is included in Mozilla's trusted ca-bundle), you can import the
certificate chain directly into ACM by using the [ImportCertificate](../../../acm/latest/APIReference/API_ImportCertificate.md "../../../acm/latest/APIReference/API_ImportCertificate.md")
API. To learn more about this task and the prerequisites and certificate
format requirements, see [Importing Certificates](../../../acm/latest/userguide/import-certificate.md "../../../acm/latest/userguide/import-certificate.md").

### External certificates signed by a private CA

If you already have a server certificate that is signed by a private CA or
self-signed, you can use the certificate to create your domain
configuration, but you also must create an extra public certificate in ACM
to validate ownership of your domain. To do this, register your server
certificate chain in ACM using the [ImportCertificate](../../../acm/latest/APIReference/API_ImportCertificate.md "../../../acm/latest/APIReference/API_ImportCertificate.md")
API. To learn more about this task and the prerequisites and certificate
format requirements, see [Importing Certificates](../../../acm/latest/userguide/import-certificate.md "../../../acm/latest/userguide/import-certificate.md").

### Creating a validation certificate

After you import your certificate to ACM, generate a public certificate
for your custom domain by using the [RequestCertificate](../../../acm/latest/APIReference/API_RequestCertificate.md "../../../acm/latest/APIReference/API_RequestCertificate.md") API. When you generate a certificate in this
way, ACM validates your ownership of the custom domain. For more
information, see [Request
a Public Certificate](../../../acm/latest/userguide/gs-acm-request-public.md "../../../acm/latest/userguide/gs-acm-request-public.md"). When you create your domain configuration,
use this public certificate as your validation certificate.

## Creating a

domain configuration

You create a configurable endpoint on a custom domain by using the [CreateDomainConfiguration](../apireference/API_CreateDomainConfiguration.md "../apireference/API_CreateDomainConfiguration.md") API. A domain configuration for a custom
domain consists of the following:

- `domainConfigurationName`

A user-defined name that
identifies the domain configuration. Domain configuration names starting with `IoT:` are
reserved for default endpoints and can't be used. Also, this value must
be unique to your AWS Region.

- `domainName`

The FQDN that your devices use to connect to AWS IoT Core. AWS IoT Core
leverages the server name indication (SNI) TLS extension to apply domain
configurations. Devices must use this extension when connecting and pass a
server name that is identical to the domain name that is specified in the
domain configuration.

- `serverCertificateArns`

The ARN of the server
certificate chain that you registered with ACM. AWS IoT Core currently
supports only one server certificate.

- `validationCertificateArn`

The ARN of the public
certificate that you generated in ACM to validate ownership of your
custom domain. This argument isn't required if you use a publicly signed
or ACM-generated server certificate.

- `defaultAuthorizerName (optional)`

The name of the custom authorizer to use on the endpoint.

- `allowAuthorizerOverride`

A Boolean value that
specifies whether devices can override the default authorizer by
specifying a different authorizer in the HTTP header of the request.
This value is required if a value for `defaultAuthorizerName`
is specified.

- `serviceType`

AWS IoT Core currently supports only the `DATA` service type. When you specify
`DATA`, AWS IoT returns an endpoint with an endpoint type of
`iot:Data-ATS`.

- `TlsConfig` (optional)

An object that specifies the TLS configuration for a domain. For more
information, see [Configuring TLS settings in domain
configurations](iot-endpoints-tls-config.md "iot-endpoints-tls-config.md").

- `serverCertificateConfig` (optional)

An object that specifies the server certificate configuration for a
domain. For more information, see [Server certificate configuration for
OCSP stapling](iot-custom-endpoints-cert-config.md "iot-custom-endpoints-cert-config.md").

The following AWS CLI command creates a domain configuration for **iot.example.com**.

```
aws iot create-domain-configuration --domain-configuration-name "`myDomainConfigurationName`" --service-type "DATA"
--domain-name "iot.example.com" --server-certificate-arns `serverCertARN` --validation-certificate-arn `validationCertArn`
```

###### Note

After you create your domain configuration, it might take up to 60 minutes
until AWS IoT Core serves your custom server certificates.

For more information, see [Managing domain configurations](iot-custom-endpoints-managing.md "iot-custom-endpoints-managing.md").

## Creating DNS

records

After you register your server certificate chain and create your domain
configuration, create a DNS record so that your custom domain points to an
AWS IoT domain. This record must point to an AWS IoT endpoint of type
`iot:Data-ATS`. You can get your endpoint by using the
[DescribeEndpoint](../apireference/API_DescribeEndpoint.md "../apireference/API_DescribeEndpoint.md")
API.

The following AWS CLI command shows how to get your endpoint.

```
aws iot describe-endpoint --endpoint-type iot:Data-ATS
```

After you get your `iot:Data-ATS` endpoint, create a `CNAME`
record from your custom domain to this AWS IoT endpoint. If you create multiple custom
domains in the same AWS account, alias them to this same `iot:Data-ATS`
endpoint.

## Troubleshooting

If you have trouble connecting devices to a custom domain, make sure that AWS IoT Core has accepted and applied your server certificate.
You can verify that AWS IoT Core has accepted your certificate by using either the AWS IoT Core console or the AWS CLI.

To use the AWS IoT Core console, navigate to the **Domain
configurations** page and select the domain configuration name. In the
**Server certificate details** section, check the status and
status details. If the certificate is invalid, replace it in ACM with a
certificate that meets the [certificate
requirements](#certificate-requirements "#certificate-requirements") listed in the previous section. If the certificate has the
same ARN, AWS IoT Core will be pick it up and apply it automatically.

To check the certificate status by using the AWS CLI, call the
[DescribeDomainConfiguration](../apireference/API_DescribeDomainConfiguration.md "../apireference/API_DescribeDomainConfiguration.md") API
and specify your domain configuration name.

###### Note

If your certificate is invalid, AWS IoT Core will continue to serve the last valid certificate.

You can check which certificate is being served on your endpoint by using the following openssl command.

`openssl s_client -connect `custom-domain-name`:8883 -showcerts 
 -servername `custom-domain-name``
