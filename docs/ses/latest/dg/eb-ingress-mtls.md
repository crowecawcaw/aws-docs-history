

# Mutual TLS ingress points

A mutual TLS (mTLS) ingress endpoint requires each SMTP client to present a certificate during STARTTLS. The certificate must chain to a certificate authority (CA) in the ingress endpoint trust store. A client without a certificate, with an untrusted certificate, or with a revoked certificate cannot complete the TLS handshake.

Use mTLS for system-to-system integrations that use certificates to establish client identity. Continue to use a restrictive traffic policy because certificate authentication and traffic-policy evaluation control different parts of the SMTP session.

## Connecting to an mTLS ingress point
<a name="eb-ingress-mtls-connection"></a>

The following table lists the supported connection settings.


| Network | Ports | STARTTLS | Server name | 
| --- | --- | --- | --- | 
| Public | 25 | Required | The hostname returned in ARecord. | 
| Private | 25, 587 | Required | A DNS name returned by the associated Amazon VPC endpoint. | 

An mTLS ingress endpoint uses `REQUIRED` outside US and Canada Regions and `FIPS` in US and Canada Regions. `OPTIONAL` is not supported. For the complete TLS policy comparison, see [TLS policies for ingress points](eb-ingress.md#eb-ingress-tls-policy).

## Configuring the trust store
<a name="eb-ingress-mtls-trust-store"></a>

Set `IngressPointConfiguration.TlsAuthConfiguration.TrustStore` when you create or update an mTLS ingress endpoint. The following table describes the trust store fields.


| Field | Required | Description | 
| --- | --- | --- | 
| CAContent | Yes | A PEM-encoded bundle of trusted CA certificates. The value can contain multiple certificates and can contain up to 500,000 characters. | 
| CrlContent | No | A PEM-encoded bundle of certificate revocation lists (CRLs). The value can contain up to 500,000 characters. Include no more than one CRL for each CA in the trust store. | 
| KmsKeyArn | No | The ARN of the customer managed AWS KMS key that encrypts the trust store content. If omitted, an AWS managed key is used. | 

If you use a customer managed AWS KMS key, its policy must allow SES to encrypt and decrypt the trust store for the ingress endpoint. See [KMS customer managed key (CMK) key policy for mTLS trust store](eb-policies.md#eb-policies-ingress-mtls-cmk).

**Warning**  
An expired CA certificate is removed from the active trust anchors. If an uploaded CRL expires, the CA certificate issued by the same subject is also removed from the active trust anchors. Clients whose certificates chain only to that CA cannot connect until you update the trust store.

## Issuing client certificates
<a name="eb-ingress-mtls-certificates"></a>

Use your organization's private CA or AWS Private CA to issue a separate client certificate to each independently managed sending system. Keep each private key on its client. Upload only CA certificates and CRLs to the ingress endpoint trust store.

If a client certificate contains an extended key usage extension, it must include `clientAuth`. A certificate without an extended key usage extension can be used for client authentication. Use `clientAuth` explicitly when issuing new certificates so the certificate purpose is clear.

### Generate a CA and client certificate for testing
<a name="eb-ingress-mtls-openssl-example"></a>

**Warning**  
The following OpenSSL example creates a new self-signed CA. Use it for testing in a controlled environment. For production, use an approved CA hierarchy, protect CA private keys with suitable key-management controls, and follow your organization's certificate policy.

Generate an encrypted CA private key and CA certificate.

```bash
PROMPT> openssl genpkey \
  -algorithm RSA \
  -aes-256-cbc \
  -pkeyopt rsa_keygen_bits:3072 \
  -out mail-manager-client-ca.key

PROMPT> openssl req \
  -x509 \
  -new \
  -sha256 \
  -days 3650 \
  -key mail-manager-client-ca.key \
  -subj '/CN=Example Mail Manager Client CA' \
  -out mail-manager-client-ca.pem
```

Generate an encrypted client private key and certificate-signing request.

```bash
PROMPT> openssl genpkey \
  -algorithm RSA \
  -aes-256-cbc \
  -pkeyopt rsa_keygen_bits:3072 \
  -out partner-relay.key

PROMPT> openssl req \
  -new \
  -sha256 \
  -key partner-relay.key \
  -subj '/CN=partner-relay.example.com' \
  -out partner-relay.csr
```

Save the following extension configuration as `partner-relay-extensions.cnf`.

```ini
basicConstraints = critical,CA:FALSE
keyUsage = critical,digitalSignature,keyEncipherment
extendedKeyUsage = clientAuth
subjectAltName = DNS:partner-relay.example.com
```

Issue the client certificate.

```bash
PROMPT> openssl x509 \
  -req \
  -sha256 \
  -days 365 \
  -in partner-relay.csr \
  -CA mail-manager-client-ca.pem \
  -CAkey mail-manager-client-ca.key \
  -CAcreateserial \
  -extfile partner-relay-extensions.cnf \
  -out partner-relay.pem
```

Configure the SMTP client with `partner-relay.pem`, its encrypted private key, and the complete intermediate certificate chain if one exists. Put `mail-manager-client-ca.pem` in the ingress endpoint `CAContent` bundle.

## Creating an mTLS ingress point with the AWS CLI
<a name="eb-ingress-mtls-cli"></a>

Save the following request as `create-mtls-ingress.yaml`. Replace the AWS Region-independent example IDs, name, and certificate body with your own values.

```yaml
IngressPointName: partner-mtls
Type: MTLS
RuleSetId: rs-0123456789abcdef01234567
TrafficPolicyId: tp-0123456789abcdef01234567
IngressPointConfiguration:
  TlsAuthConfiguration:
    TrustStore:
      CAContent: |-
        -----BEGIN CERTIFICATE-----
        MIIBexampleCertificateBody
        -----END CERTIFICATE-----
NetworkConfiguration:
  PublicNetworkConfiguration:
    IpType: IPV4
TlsPolicy: REQUIRED
```

Run the following command.

```bash
PROMPT> aws mailmanager create-ingress-point \
  --region {{us-east-1}} \
  --cli-input-yaml file://create-mtls-ingress.yaml
```

The response contains the `IngressPointId`. Wait for the ingress endpoint to become `ACTIVE` as described in [Ingress point provisioning status](eb-ingress.md#eb-ingress-status). Then configure the SMTP client to use STARTTLS and present its certificate and certificate chain.

## Rotating CA and client certificates
<a name="eb-ingress-mtls-rotation"></a>

Use an overlap period so clients can move to a new CA without an outage.

1. Create the new CA and issue new client certificates.

1. Update `CAContent` so the bundle contains both the current and new CA certificates. Keep the applicable CRL for each CA.

1. Deploy the new certificate and private key to each SMTP client.

1. Confirm that clients connect with certificates chained to the new CA.

1. Update the trust store again to remove the former CA and its CRL.

**Warning**  
Do not remove the former CA before every required client uses the new certificate chain. Removing the CA immediately causes those clients to fail the TLS handshake.

To update the trust store with the AWS CLI, save a complete replacement configuration as `update-mtls-trust-store.yaml`. Include every CA and CRL that must remain trusted.

```yaml
IngressPointId: inp-0123456789abcdef01234567
IngressPointConfiguration:
  TlsAuthConfiguration:
    TrustStore:
      CAContent: |-
        -----BEGIN CERTIFICATE-----
        MIIBcurrentCaCertificateBody
        -----END CERTIFICATE-----
        -----BEGIN CERTIFICATE-----
        MIIBnewCaCertificateBody
        -----END CERTIFICATE-----
      CrlContent: |-
        -----BEGIN X509 CRL-----
        MIIBcurrentCrlBody
        -----END X509 CRL-----
```

```bash
PROMPT> aws mailmanager update-ingress-point \
  --region {{us-east-1}} \
  --cli-input-yaml file://update-mtls-trust-store.yaml
```

Use the CA's supported revocation process to issue CRLs. Publish an updated CRL before its `nextUpdate` time. If you revoke a client certificate, update `CrlContent` with the CRL that contains its serial number.

## Using client certificate attributes in rule conditions
<a name="eb-ingress-mtls-rule-conditions"></a>

After a client completes mTLS authentication, rule conditions can evaluate its common name, serial number, and Subject Alternative Name values. Supported Subject Alternative Name types include email address, DNS name, directory name, URI, IP address, and registered ID.

Use these conditions to route or restrict an authenticated client after the traffic policy accepts the recipient. For operators and examples, see [Rule conditions](eb-rules-conditions.md).

## Monitoring certificates and rejected connections
<a name="eb-ingress-mtls-monitoring"></a>

For accepted messages, `APPLICATION_LOGS` includes client certificate details and trust-store monitoring. The following fragment shows the fields that report a CA or CRL that is invalid or expires within 90 days.

```json
{
  "ingress_point_type": "MTLS",
  "ingress_point_metadata": {
    "client_certificate_details": {
      "common_names": ["partner-relay.example.com"],
      "serial_number": "0A:DE:EB:89:42:FB:1C:67"
    },
    "trust_store_monitoring": {
      "ca_invalid_or_near_expiry": [],
      "crl_invalid_or_near_expiry": []
    }
  }
}
```

Create monitoring for nonempty `ca_invalid_or_near_expiry` and `crl_invalid_or_near_expiry` lists. Each list contains at most 10 entries.

A connection without a client certificate, with an untrusted certificate, or with a revoked certificate fails during TLS negotiation and does not create an application log. If the trust store has no active CA, the SMTP client can receive the following response.

```
550 5.7.0 No active trust anchors
```

For log delivery setup and the complete application-log schema, see [Ingress endpoint logs – `APPLICATION_LOGS`](eb-logging.md#ingress-endpoint-logs-app).

## Recommendations for mTLS ingress points
<a name="eb-ingress-mtls-recommendations"></a>
+ Use a separate client certificate for each independently managed sending system.
+ Protect client and CA private keys. Do not upload a private key to the ingress endpoint trust store.
+ Use short-lived client certificates and automate renewal where your CA and client software support it.
+ Include `clientAuth` when issuing a certificate with an extended key usage extension.
+ Rotate CAs with an overlap period and update CRLs before they expire.
+ Monitor the certificate and trust-store fields in `APPLICATION_LOGS`.
+ Use a restrictive traffic policy in addition to certificate authentication.