# Register a client certificate

when the client connects to AWS IoT just-in-time registration
(JITR)

You can configure a CA certificate to enable client certificates it has
signed to register with AWS IoT automatically the first time the client
connects to AWS IoT.

To register client certificates when a client connects to AWS IoT for the
first time, you must enable the CA certificate for automatic registration
and configure the first connection by the client to provide the required
certificates.

## Configure a CA

certificate to support automatic registration (console)

###### To configure a CA certificate to support automatic client

certificate registration using the AWS IoT console

1. Sign in to the AWS Management Console and open the [AWS IoT
   console](https://console.aws.amazon.com/iot/home "https://console.aws.amazon.com/iot/home").
2. In the left navigation pane, choose
   **Secure**, choose
   **CAs**.
3. In the list of certificate authorities, find the one for which
   you want to enable automatic registration, and open the option
   menu by using the ellipsis icon.
4. On the option menu, choose **Enable
   auto-registration**.

###### Note

The auto-registration status is not shown in the list of
certificate authorities. To see the auto-registration status of a
certificate authority, you must open the
**Details** page of the certificate
authority.

## Configure a CA

certificate to support automatic registration (CLI)

If you have already registered your CA certificate with AWS IoT, use the
[**update-ca-certificate**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-ca-certificate.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-ca-certificate.html") command to set
`autoRegistrationStatus` of the CA certificate to
`ENABLE`.

```
`aws iot update-ca-certificate \
--certificate-id `caCertificateId` \
--new-auto-registration-status ENABLE`
```

If you want to enable `autoRegistrationStatus` when you
register the CA certificate, use the [**register-ca-certificate**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/register-ca-certificate.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/register-ca-certificate.html")
command.

```
`aws iot register-ca-certificate \
--allow-auto-registration \
--ca-certificate file://`root_CA_cert_filename.pem` \
--verification-cert file://`verification_cert_filename.pem``
```

Use the [**describe-ca-certificate**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-ca-certificate.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-ca-certificate.html") command to
see the status of the CA certificate.

## Configure the first

connection by a client for automatic registration

When a client attempts to connect to AWS IoT for the first time, the
client certificate signed by your CA certificate must be present on the
client during the Transport Layer Security (TLS) handshake.

When the client connects to AWS IoT, use the client certificate you
created in [Create AWS IoT client certificates](device-certs-create.md "device-certs-create.md") or
[Create your own client certificates](device-certs-your-own.md "device-certs-your-own.md").
AWS IoT recognizes the CA certificate as a registered CA certificate,
registers the client certificate, and sets its status to
`PENDING_ACTIVATION`. This means that the client
certificate was automatically registered and is awaiting activation. The
client certificate's state must be `ACTIVE` before it can be
used to connect to AWS IoT. See [Activate or deactivate a
client certificate](activate-or-deactivate-device-cert.md "activate-or-deactivate-device-cert.md") for information on
activating a client certificate.

###### Note

You can provision devices using AWS IoT Core just-in-time
registration (JITR) feature without having to send the entire trust
chain on devices' first connection to AWS IoT Core. Presenting the CA
certificate is optional but the device is required to send the
[Server Name Indication (SNI)](https://datatracker.ietf.org/doc/html/rfc3546#section-3.1 "https://datatracker.ietf.org/doc/html/rfc3546#section-3.1") extension when they
connect.

When AWS IoT automatically registers a certificate or when a client
presents a certificate in the `PENDING_ACTIVATION` status,
AWS IoT publishes a message to the following MQTT topic:

`$aws/events/certificates/registered/`caCertificateId``

Where `caCertificateId` is the
ID of the CA certificate that issued the client certificate.

The message published to this topic has the following
structure:

```
{
        "certificateId": "`certificateId`",
        "caCertificateId": "`caCertificateId`",
        "timestamp": `timestamp`,
        "certificateStatus": "PENDING_ACTIVATION",
        "awsAccountId": "`awsAccountId`",
        "certificateRegistrationTimestamp": "`certificateRegistrationTimestamp`"
}
```

You can create a rule that listens on this topic and performs some
actions. We recommend that you create a Lambda rule that verifies the
client certificate is not on a certificate revocation list (CRL),
activates the certificate, and creates and attaches a policy to the
certificate. The policy determines which resources the client can
access. If the policy you are creating requires the client ID from the
connecting devices, you can use rule's clientid() function to retrieve
the client ID. An example rule definition can look like the
following:

```
SELECT *,
   clientid() as clientid
from $aws/events/certificates/registered/caCertificateId
```

In this example, the rule subscribes to the JITR topic
`$aws/events/certificates/registered/`caCertificateID``
and uses the clientid() function to retrieve the client ID. The rule
then appends the client ID to the JITR payload. For more information
about rule's clientid() function, see [clientid()](iot-sql-functions.md#iot-sql-function-clientid "iot-sql-functions.md#iot-sql-function-clientid").

For more information about how to create a Lambda rule that listens on
the
`$aws/events/certificates/registered/`caCertificateID``
topic and performs these actions, see [just-in-time registration of Client Certificates on
AWS IoT](https://aws.amazon.com/blogs/iot/just-in-time-registration-of-device-certificates-on-aws-iot/ "https://aws.amazon.com/blogs/iot/just-in-time-registration-of-device-certificates-on-aws-iot/").

If any error or exception occurs during the auto-registration of the
client certificates, AWS IoT sends events or messages to your logs in
CloudWatch Logs. For more information about setting up the logs for your account,
see the [Amazon CloudWatch documentation](../../../AmazonCloudWatch/latest/DeveloperGuide.md "../../../AmazonCloudWatch/latest/DeveloperGuide.md").
