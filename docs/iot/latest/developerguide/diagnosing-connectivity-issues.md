# Diagnosing connectivity issues

###### Help us improve this topic

[Let us know what would help make it better](../../../forms/aws-doc-feedback.md "../../../forms/aws-doc-feedback.md")

A successful connection to AWS IoT requires:

- A valid connection
- A valid and active certificate
- A policy that allows the desired connection and operation

## Connection

How do I find the correct endpoint?

- The `endpointAddress` returned by `aws iot describe-endpoint --endpoint-type iot:Data-ATS`

or

- The `domainName` returned by `aws iot describe-domain-configuration –-domain-configuration-name
"`domain_configuration_name`"`

How do I find the correct Server Name Indication (SNI) value?

The correct SNI value is the `endpointAddress` returned by the
**[describe-endpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-endpoint.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-endpoint.html")** or the `domainName` returned by
the **[describe-domain-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-domain-configuration.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-domain-configuration.html")** commands. It's the same address
as the endpoint in the previous step. When connecting devices to AWS IoT Core, clients
can send the [Server
Name Indication (SNI) extension](https://tools.ietf.org/html/rfc3546#section-3.1 "https://tools.ietf.org/html/rfc3546#section-3.1"), which is not required but highly
recommended. To use features such as [multi-account registration](x509-client-certs.md#multiple-account-cert "x509-client-certs.md#multiple-account-cert"), [custom domains](iot-custom-endpoints-configurable-custom.md "iot-custom-endpoints-configurable-custom.md"), and [VPC endpoints](IoTCore-VPC.md "IoTCore-VPC.md"), you must
use the SNI extension. For more information, see [Transport Security in AWS IoT](transport-security.md "transport-security.md").

How do I solve a connectivity issue that persists?

You can use AWS Device Advisor to help troubleshoot. Device Advisor's pre-built tests help
you validate your device software against best practices for usage of [TLS](protocols.md "protocols.md"), [MQTT](protocols.md "protocols.md"), [AWS IoT Device Shadow](iot-device-shadows.md "iot-device-shadows.md"), and [AWS IoT
Jobs](iot-jobs.md "iot-jobs.md").

Here is a link to the existing [Device Advisor](device-advisor.md "device-advisor.md") content.

## Authentication

Devices must be [authenticated](client-authentication.md "client-authentication.md") to connect
to AWS IoT endpoints. For devices that use [X.509 client certificates](x509-client-certs.md "x509-client-certs.md") for authentication, the certificates must be
registered with AWS IoT and be active.

How do my devices authenticate AWS IoT endpoints?

Add the AWS IoT CA certificate to your client's trust store. Refer to the
documentation on [Server
Authentication in AWS IoT Core](x509-client-certs.md#server-authentication "x509-client-certs.md#server-authentication") and then follow the links to download the
appropriate CA certificate.

What is checked when a device connects to AWS IoT?

When a device attempts to connect to AWS IoT:

1. AWS IoT checks for a valid certificate and Server Name Indication (SNI)
   value.
2. AWS IoT checks to see that the certificate used is registered with the AWS IoT
   Account and that it has been activated.
3. When a device attempts to perform any action in AWS IoT, such as to subscribe
   to or publish a message, the policy attached to the certificate it used to
   connect is checked to confirm that the device is authorized to perform that
   action.

How can I validate a correctly configured certificate?

Use the OpenSSL `s_client` command to test a connection to the AWS IoT
endpoint:

```
openssl s_client -connect `custom_endpoint`.iot.`aws-region`.amazonaws.com:8443 -CAfile `CA.pem` -cert `cert.pem` -key `privateKey.pem`
```

For more information about using `openssl s_client`, see [OpenSSL
s_client documentation](https://www.openssl.org/docs/man1.0.2/man1/openssl-s_client.html "https://www.openssl.org/docs/man1.0.2/man1/openssl-s_client.html").

How do I check the status of a certificate?

- ###### List the certificates

If you don't know the certificate ID, you can see the status of all your
certificates by using the `aws iot list-certificates` command.

- ###### Show a certificate's details

If you know the certificate's ID, this command shows you more detailed
information about the certificate.

```
aws iot describe-certificate --certificate-id "`certificateId`"
```

- ###### Review the certificate in the AWS IoT Console

In the [AWS IoT
console](https://console.aws.amazon.com/iot/home "https://console.aws.amazon.com/iot/home"), in the left menu, choose **Secure**,
and then choose **Certificates**.

Choose the certificate that you are using to connect from the list to open
its detail page.

In the certificate's detail page, you can see its current status.

The certificate's status can be changed by using the
**Actions** menu in the upper-right corner of the details
page.

## Authorization

AWS IoT resources use [AWS IoT Core policies](iot-policies.md "iot-policies.md") to
authorize those resources to perform [actions](iot-policy-actions.md "iot-policy-actions.md").
For an action to be authorized, the specified AWS IoT resources must have a policy document
attached to it that grants permission to perform that action.

I received a `PUBNACK` or `SUBNACK` response from the
broker. What do I do?

Make sure that there is a policy attached to the certificate you are using to
call AWS IoT. All publish/subscribe operations are denied by default.

Make sure the attached policy authorizes the [actions](iot-policy-actions.md "iot-policy-actions.md") you are trying to perform.

Make sure the attached policy authorizes the [resources](iot-action-resources.md "iot-action-resources.md") that are trying to perform the
authorized actions.

I have an _AUTHORIZATION_FAILURE_ entry in my logs.

Make sure that there is a policy attached to the certificate you are using to
call AWS IoT. All publish/subscribe operations are denied by default.

Make sure the attached policy authorizes the [actions](iot-policy-actions.md "iot-policy-actions.md") you are trying to perform.

Make sure the attached policy authorizes the [resources](iot-action-resources.md "iot-action-resources.md") that are trying to perform the
authorized actions.

How do I check what the policy authorizes?

In the [AWS IoT console](https://console.aws.amazon.com/iot/home "https://console.aws.amazon.com/iot/home"), in
the left menu, choose **Security**, and then choose
**Certificates**.

Choose the certificate that you are using to connect from the list to open its
detail page.

In the certificate's detail page, you can see its current status.

In the left menu of the certificate's detail page, choose
**Policies** to see the policies attached to the
certificate.

Choose the desired policy to see its details page.

In the policy's details page, review the policy's **Policy
document** to see what it authorizes.

Choose **Edit policy document** to make changes to the policy
document.

## Security and identity

When you provide the server certificates for AWS IoT custom domain configuration, the
certificates have a maximum of four domain names.

For more information, see [AWS IoT Core endpoints and quotas](../../../general/latest/gr/iot-core.md#security-limits "../../../general/latest/gr/iot-core.md#security-limits").
