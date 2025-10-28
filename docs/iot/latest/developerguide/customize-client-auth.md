# Custom client certificate

validation

AWS IoT Core supports custom client certificate validation for X.509 client
certificates, which enhances client authentication management. This certificate
validation method is also known as pre-authentication certificate checks, in
which you evaluate client certificates based on your own criteria (defined in a
Lambda function) and revoke client certificates or the certificates' signing
certificate authority (CA) certificate to prevent clients to connect to
AWS IoT Core. For example, you can create your own certificate revocation checks
that validate the certificates' status against validation authorities that
support [Online Certificate Status Protocol (OCSP)](https://en.wikipedia.org/wiki/Online_Certificate_Status_Protocol "https://en.wikipedia.org/wiki/Online_Certificate_Status_Protocol") or [Certificate
Revocation Lists (CRL)](https://en.wikipedia.org/wiki/Certificate_revocation_list "https://en.wikipedia.org/wiki/Certificate_revocation_list") endpoints, and prevent connections for
clients with revoked certificates. The criteria used to evaluate client
certificates are defined in a Lambda function (also known as pre-authentication
Lambda). You must use the endpoints set in domain configurations and the [authentication type](protocols.md#connection-protocol-auth-mode "protocols.md#connection-protocol-auth-mode") must be
X.509 certificate. In addition, clients must provide the [Server Name
Indication (SNI)](https://www.rfc-editor.org/rfc/rfc3546#section-3.1 "https://www.rfc-editor.org/rfc/rfc3546#section-3.1") extension when connecting to AWS IoT Core.

###### Note

This feature is not supported in the AWS GovCloud (US) Regions.

###### The process of performing custom client certificate

validation involves the following steps.

- [Step 1: Register your X.509
  client certificates with AWS IoT Core](#client-auth-cert-verification "#client-auth-cert-verification")
- [Step 2: Create a Lambda function](#customize-client-auth-lambda "#customize-client-auth-lambda")
- [Step 3:
  Authorize AWS IoT to invoke your Lambda function](#customize-client-configuration-grant-permission "#customize-client-configuration-grant-permission")
- [Step 4: Set authentication
  configuration for a domain](#customize-client-configuration "#customize-client-configuration")

## Step 1: Register your X.509

client certificates with AWS IoT Core

If you haven't done this already, register and activate your [X.509 client
certificates](x509-client-certs.md "x509-client-certs.md") with AWS IoT Core. Otherwise, skip to the next
step.

To register and activate your client certificates with AWS IoT Core, follow
the steps:

1. If you [create
   client certificates directly with AWS IoT](device-certs-create.md "device-certs-create.md"). These client
   certificates will be automatically registered with AWS IoT Core.
2. If you [create your own client certificates](device-certs-your-own.md "device-certs-your-own.md"), follow [these
   instructions to register them with AWS IoT Core](register-device-cert.md "register-device-cert.md").
3. To activate your client certificates, follow [these
   instructions](activate-or-deactivate-device-cert.md "activate-or-deactivate-device-cert.md").

## Step 2: Create a Lambda function

You need to create a Lambda function that will perform certificate
verification and be called for every client connect attempt for the
configured endpoint. When creating this Lambda function, follow the general
guidance from [Create your first Lambda
function](../../../lambda/latest/dg/getting-started.md "../../../lambda/latest/dg/getting-started.md"). Additionally, ensure that the Lambda function adheres
to the expected request and response formats as follows:

**Lambda function event example**

```
{
	"connectionMetadata": {
		"id": "string"
	},
	"principalId": "string",
	"serverName": "string",
	"clientCertificateChain": [
		"string",
		"string"
	]
}
```

`connectionMetadata`

Metadata or additional information related to the client's
connection to AWS IoT Core.

`principalId`

The principal identifier associated with the client in the TLS
connection.

`serverName`

The [Server Name Indication (SNI)](https://www.rfc-editor.org/rfc/rfc3546#section-3.1 "https://www.rfc-editor.org/rfc/rfc3546#section-3.1") hostname string.
AWS IoT Core requires devices to send the [SNI
extension](https://www.rfc-editor.org/rfc/rfc3546#section-3.1 "https://www.rfc-editor.org/rfc/rfc3546#section-3.1") to the Transport Layer Security (TLS)
protocol and provide the complete endpoint address in the
`host_name` field.

`clientCertificateChain`

The array of strings that represents the client's X.509
certificate chain.

**Lambda function response example**

```
{
	"isAuthenticated": "boolean"
}
```

`isAuthenticated`

A Boolean value that indicates whether the request is
authenticated.

###### Note

In the Lambda response, `isAuthenticated` must be
`true` to proceed to further authentication and
authorization. Otherwise, the IoT client certificate can be disabled and
custom authentication with X.509 client certificates can be blocked for
further authentication and authorization.

## Step 3:

Authorize AWS IoT to invoke your Lambda function

After creating the Lambda function, you must grant permission for AWS IoT to
invoke it, by using the [add-permission](../../../cli/latest/reference/lambda/add-permission.md "../../../cli/latest/reference/lambda/add-permission.md") CLI command. Note that this Lambda function will
be invoked for every connect attempt to your configured endpoint. For more
information, see [Authorizing AWS IoT to
invoke your Lambda function](custom-auth-authorize.md "custom-auth-authorize.md").

## Step 4: Set authentication

configuration for a domain

The following section describes how to set authentication configuration
for a custom domain using the AWS CLI.

### Set client certificate

configuration for a domain (CLI)

If you don't have a domain configuration, use the [**create-domain-configuration**](../../../cli/latest/reference/iot/create-domain-configuration.md "../../../cli/latest/reference/iot/create-domain-configuration.md") CLI
command to create one. If you already have a domain configuration, use
the [**update-domain-configuration**](../../../cli/latest/reference/iot/update-domain-configuration.md "../../../cli/latest/reference/iot/update-domain-configuration.md") CLI
command to update the client certificate configuration for a domain. You
must add the ARN of the Lambda function that you've created in the
previous step.

```
`aws iot create-domain-configuration \
 --domain-configuration-name `domainConfigurationName` \
 --authentication-type AWS_X509|CUSTOM_AUTH_X509 \
 --application-protocol SECURE_MQTT|HTTPS \
 --client-certificate-config 'clientCertificateCallbackArn":"arn:aws:lambda:`us-east-2:123456789012`:function:`my-function:1`"}'`
```

```
`aws iot update-domain-configuration \
 --domain-configuration-name `domainConfigurationName` \
 --authentication-type AWS_X509|CUSTOM_AUTH_X509 \
 --application-protocol SECURE_MQTT|HTTPS \
 --client-certificate-config '{"clientCertificateCallbackArn":"arn:aws:lambda:`us-east-2:123456789012`:function:`my-function:1`"}'`
```

`domain-configuration-name`

The name of the domain configuration.

`authentication-type`

The authentication type of the domain configuration. For
more information, see [choosing an
authentication type](protocols.md#connection-protocol-auth-mode "protocols.md#connection-protocol-auth-mode").

`application-protocol`

The application protocol which devices use to communicate
with AWS IoT Core. For more information, see [choosing an application
protocol](protocols.md#protocol-selection "protocols.md#protocol-selection").

`client-certificate-config`

An object that
specifies the client authentication configuration for a
domain.

`clientCertificateCallbackArn`

The Amazon Resource
Name (ARN) of the Lambda function that AWS IoT invokes in TLS layer
when new connection is being established. To customize client
authentication to perform custom client certificate validation,
you must add the ARN of the Lambda function that you've created
in the previous step.

For more information, see [CreateDomainConfiguration](../apireference/API_CreateDomainConfiguration.md "../apireference/API_CreateDomainConfiguration.md") and [UpdateDomainConfiguration](../apireference/API_UpdateDomainConfiguration.md "../apireference/API_UpdateDomainConfiguration.md") from the _AWS IoT API Reference_. For more information about domain
configurations, see [Domain configurations](iot-custom-endpoints-configurable.md "iot-custom-endpoints-configurable.md").
