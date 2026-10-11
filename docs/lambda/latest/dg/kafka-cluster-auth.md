

# Configuring cluster authentication methods in Lambda
<a name="kafka-cluster-auth"></a>

Lambda supports several methods to authenticate with your self-managed Apache Kafka cluster. Make sure that you configure the Kafka cluster to use one of these supported authentication methods. For more information about Kafka security, see the [Security](http://kafka.apache.org/documentation.html#security) section of the Kafka documentation.

## SASL/SCRAM authentication
<a name="smaa-auth-sasl"></a>

Lambda supports Simple Authentication and Security Layer/Salted Challenge Response Authentication Mechanism (SASL/SCRAM) authentication with Transport Layer Security (TLS) encryption (`SASL_SSL`). Lambda sends the encrypted credentials to authenticate with the cluster. Lambda doesn't support SASL/SCRAM with plaintext (`SASL_PLAINTEXT`). For more information about SASL/SCRAM authentication, see [RFC 5802](https://tools.ietf.org/html/rfc5802).

Lambda also supports SASL/PLAIN authentication. Because this mechanism uses clear text credentials, the connection to the server must use TLS encryption to ensure that the credentials are protected.

For SASL authentication, you store the sign-in credentials as a secret in AWS Secrets Manager. For more information about using Secrets Manager, see [Create an AWS Secrets Manager secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html) in the *AWS Secrets Manager User Guide*.

**Important**  
To use Secrets Manager for authentication, secrets must be stored in the same AWS region as your Lambda function.

## Mutual TLS authentication
<a name="smaa-auth-mtls"></a>

Mutual TLS (mTLS) provides two-way authentication between the client and server. The client sends a certificate to the server for the server to verify the client, and the server sends a certificate to the client for the client to verify the server. 

In self-managed Apache Kafka, Lambda acts as the client. You configure a client certificate (as a secret in Secrets Manager) to authenticate Lambda with your Kafka brokers. The client certificate must be signed by a CA in the server's trust store.

The Kafka cluster sends a server certificate to Lambda to authenticate the Kafka brokers with Lambda. The server certificate can be a public CA certificate or a private CA/self-signed certificate. The public CA certificate must be signed by a certificate authority (CA) that's in the Lambda trust store. For a private CA/self-signed certificate, you configure the server root CA certificate (as a secret in Secrets Manager). Lambda uses the root certificate to verify the Kafka brokers.

For more information about mTLS, see [ Introducing mutual TLS authentication for Amazon MSK as an event source](https://aws.amazon.com/blogs/compute/introducing-mutual-tls-authentication-for-amazon-msk-as-an-event-source).

## OAuth 2.0 authentication
<a name="smaa-auth-oauth"></a>

Lambda supports SASL/OAUTHBEARER authentication with TLS encryption (`SASL_SSL`). Lambda requests an access token from your OAuth 2.0 identity provider and presents that token to your Kafka brokers. Lambda refreshes the token before it expires. Configure your brokers to validate tokens from the same identity provider.

To use this method, choose `OAUTHBEARER_AUTH` as the `Type` of a [SourceAccessConfiguration](https://docs.aws.amazon.com/lambda/latest/api/API_SourceAccessConfiguration.html) and provide the Secrets Manager ARN of your OAuth secret in the `URI` field. For the contents of the secret, see [Configuring the OAuth secret](#smaa-auth-oauth-secret).

Lambda supports two grant types. The fields that you store in the secret determine which one Lambda uses.
+ **Client credentials** – Lambda sends a client ID and client secret to the token endpoint. Use this grant type when your identity provider issues a client secret.
+ **JWT bearer** – Lambda signs a JSON Web Token (JWT) assertion with a private key and sends the assertion to the token endpoint. Use this grant type when your identity provider expects a signed assertion instead of a client secret.

If your identity provider or your brokers require additional values, provide each one as its own source access configuration entry. Put the literal value in the `URI` field rather than a secret ARN.
+ `OAUTHBEARER_SCOPE` – The scope that Lambda requests when it asks for a token.
+ `OAUTHBEARER_AUDIENCE` – The audience that Lambda requests when it asks for a token.
+ `OAUTHBEARER_LOGICAL_CLUSTER` – The logical cluster ID that Lambda sends to your brokers as a SASL extension.
+ `OAUTHBEARER_IDENTITY_POOL` – The identity pool ID that Lambda sends to your brokers as a SASL extension.

**Note**  
These four types require an OAuth 2.0 authentication type. Provide them with `OAUTHBEARER_AUTH`, or provide only `OAUTHBEARER_AUDIENCE` with `IAM_OAUTHBEARER_AUTH`. If you provide any of them without one of these authentication types, Lambda returns a validation error.

If your brokers present a certificate signed by a private CA, also provide `SERVER_ROOT_CA_CERTIFICATE` so that Lambda can verify them. For more information, see [Configuring the server root CA certificate secret](#smaa-auth-ca-cert).

## IAM authentication
<a name="smaa-auth-iam"></a>

If your cluster is an Amazon MSK cluster that you reach through your own networking setup, you can register it as a self-managed Kafka event source and authenticate with IAM. Custom networking setups include a custom domain name in front of your brokers or a connection from another account. Lambda signs each connection with the credentials of your function's execution role, so you don't store any credentials in Secrets Manager.

To use this method, turn on IAM access control on your cluster. Then choose `IAM_AUTH` as the `Type` of a source access configuration and omit the `URI` field. Your function's execution role needs the cluster permissions described in [Configuring Lambda execution role permissions](with-kafka-permissions.md).

If your brokers present a certificate signed by a private CA, also provide `SERVER_ROOT_CA_CERTIFICATE` so that Lambda can verify them. A custom domain name in front of your brokers usually needs this.

## IAM authentication with SASL/OAUTHBEARER
<a name="smaa-auth-iam-oauth"></a>

If your brokers accept OAuth 2.0 tokens, you can use AWS as the identity provider. Lambda presents an AWS web identity token to your brokers over SASL/OAUTHBEARER. Lambda requests a short-lived token for your function's execution role with the `sts:GetWebIdentityToken` action, so you don't store any credentials in Secrets Manager. Lambda requests a new token before the current one expires.

To use this method, choose `IAM_OAUTHBEARER_AUTH` as the `Type` of a source access configuration and omit the `URI` field. You must also provide `OAUTHBEARER_AUDIENCE` with the audience that your brokers expect. Your function's execution role needs permission to call `sts:GetWebIdentityToken`.

Configure your brokers to trust AWS as an OpenID Connect (OIDC) identity provider before you create the event source mapping. If your brokers don't trust the AWS issuer, they reject the token and Lambda can't read from your topics.

**Note**  
`IAM_OAUTHBEARER_AUTH` supports only `OAUTHBEARER_AUDIENCE`. If you also provide `OAUTHBEARER_SCOPE`, `OAUTHBEARER_LOGICAL_CLUSTER`, or `OAUTHBEARER_IDENTITY_POOL`, Lambda returns a validation error.

## Configuring the client certificate secret
<a name="smaa-auth-secret"></a>

The CLIENT\_CERTIFICATE\_TLS\_AUTH secret requires a certificate field and a private key field. For an encrypted private key, the secret requires a private key password. Both the certificate and private key must be in PEM format.

**Note**  
Lambda supports the [PBES1](https://datatracker.ietf.org/doc/html/rfc2898/#section-6.1) (but not PBES2) private key encryption algorithms.

The certificate field must contain a list of certificates, beginning with the client certificate, followed by any intermediate certificates, and ending with the root certificate. Each certificate must start on a new line with the following structure:

```
-----BEGIN CERTIFICATE-----  
            <certificate contents>
-----END CERTIFICATE-----
```

Secrets Manager supports secrets up to 65,536 bytes, which is enough space for long certificate chains.

The private key must be in [PKCS \#8](https://datatracker.ietf.org/doc/html/rfc5208) format, with the following structure:

```
-----BEGIN PRIVATE KEY-----  
             <private key contents>
-----END PRIVATE KEY-----
```

For an encrypted private key, use the following structure:

```
-----BEGIN ENCRYPTED PRIVATE KEY-----  
              <private key contents>
-----END ENCRYPTED PRIVATE KEY-----
```

The following example shows the contents of a secret for mTLS authentication using an encrypted private key. For an encrypted private key, include the private key password in the secret.

```
{"privateKeyPassword":"testpassword",
"certificate":"-----BEGIN CERTIFICATE-----
MIIE5DCCAsygAwIBAgIRAPJdwaFaNRrytHBto0j5BA0wDQYJKoZIhvcNAQELBQAw
...
j0Lh4/+1HfgyE2KlmII36dg4IMzNjAFEBZiCRoPimO40s1cRqtFHXoal0QQbIlxk
cmUuiAii9R0=
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
MIIFgjCCA2qgAwIBAgIQdjNZd6uFf9hbNC5RdfmHrzANBgkqhkiG9w0BAQsFADBb
...
rQoiowbbk5wXCheYSANQIfTZ6weQTgiCHCCbuuMKNVS95FkXm0vqVD/YpXKwA/no
c8PH3PSoAaRwMMgOSA2ALJvbRz8mpg==
-----END CERTIFICATE-----",
"privateKey":"-----BEGIN ENCRYPTED PRIVATE KEY-----
MIIFKzBVBgkqhkiG9w0BBQ0wSDAnBgkqhkiG9w0BBQwwGgQUiAFcK5hT/X7Kjmgp
...
QrSekqF+kWzmB6nAfSzgO9IaoAaytLvNgGTckWeUkWn/V0Ck+LdGUXzAC4RxZnoQ
zp2mwJn2NYB7AZ7+imp0azDZb+8YG2aUCiyqb6PnnA==
-----END ENCRYPTED PRIVATE KEY-----"
}
```

## Configuring the server root CA certificate secret
<a name="smaa-auth-ca-cert"></a>

You create this secret if your Kafka brokers use TLS encryption with certificates signed by a private CA. You can use TLS encryption for VPC, SASL/SCRAM, SASL/PLAIN, or mTLS authentication.

The server root CA certificate secret requires a field that contains the Kafka broker's root CA certificate in PEM format. The following example shows the structure of the secret.

```
{"certificate":"-----BEGIN CERTIFICATE-----
MIID7zCCAtegAwIBAgIBADANBgkqhkiG9w0BAQsFADCBmDELMAkGA1UEBhMCVVMx
EDAOBgNVBAgTB0FyaXpvbmExEzARBgNVBAcTClNjb3R0c2RhbGUxJTAjBgNVBAoT
HFN0YXJmaWVsZCBUZWNobm9sb2dpZXMsIEluYy4xOzA5BgNVBAMTMlN0YXJmaWVs
ZCBTZXJ2aWNlcyBSb290IENlcnRpZmljYXRlIEF1dG...
-----END CERTIFICATE-----"
}
```

## Configuring the OAuth secret
<a name="smaa-auth-oauth-secret"></a>

You create this secret when you use `OAUTHBEARER_AUTH`. The secret is a JSON document. Every OAuth secret needs `oauthTokenEndpointUrl` and `oauthClientId`. Add the fields for only one grant type. If you provide fields from both grant types, Lambda returns a validation error.


| Field | Required | Description | 
| --- | --- | --- | 
| `oauthTokenEndpointUrl` | Y | The token endpoint of your identity provider. This must be an HTTPS URL. | 
| `oauthClientId` | Y | The client ID that your identity provider issued. | 
| `oauthClientSecret` | Client credentials only | The client secret that your identity provider issued. | 
| `oauthClientEmail` | JWT bearer only | The service account identity that Lambda puts in the JWT assertion. | 
| `oauthPrivateKey` | JWT bearer only | The private key that Lambda uses to sign the JWT assertion, in PEM format. | 
| `oauthTokenExpirationSeconds` | N | The lifetime of the JWT assertion that Lambda signs. Applies to the JWT bearer grant type only. | 
| `oauthIdpCaCertificate` | N | The root CA certificate of your identity provider, in PEM format. Provide this if your identity provider presents a certificate signed by a private CA. | 

The following example shows a secret for the client credentials grant type.

```
{"oauthTokenEndpointUrl":"https://idp.example.com/oauth2/token",
"oauthClientId":"my-client-id",
"oauthClientSecret":"my-client-secret"}
```

The following example shows a secret for the JWT bearer grant type.

```
{"oauthTokenEndpointUrl":"https://idp.example.com/oauth2/token",
"oauthClientId":"my-client-id",
"oauthClientEmail":"my-service-account@example.com",
"oauthPrivateKey":"-----BEGIN PRIVATE KEY-----
<private key contents>
-----END PRIVATE KEY-----"}
```

**Important**  
Store the secret in the same AWS Region as your Lambda function. Lambda reads the secret with your function's execution role, so that role needs `secretsmanager:GetSecretValue` permission on the secret.

You can rotate the credentials in the secret without recreating the event source mapping. Lambda picks up the new values and requests a new token.