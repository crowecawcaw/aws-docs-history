

# What is a domain configuration?
<a name="iot-domain-configuration-what-is"></a>

In AWS IoT Core, a domain configuration refers to the setup and configuration of a domain (either AWS managed domain or customer managed domain) for your AWS IoT Core data endpoints. AWS IoT Core also provides a default endpoint for your AWS account (`iot:Data-ATS`) for devices to communicate with AWS IoT Core.

**Topics**
+ [Use cases](#iot-custom-endpoints-configurable-use-cases)
+ [Key concepts](#iot-domain-configuration-key-concepts)
+ [Important notes](#iot-custom-endpoints-configurable-notes)

## Use cases
<a name="iot-custom-endpoints-configurable-use-cases"></a>

You can use domain configurations to simplify tasks like the following.
+ Migrate devices to AWS IoT Core.
+ Support heterogeneous device fleets by maintaining separate domain configurations for separate device types.
+ Maintain brand identity (for example, through domain name) while migrating application infrastructure to AWS IoT Core.

## Key concepts
<a name="iot-domain-configuration-key-concepts"></a>

The following concepts provide details about domain configurations and related concepts.
+ **Domain configuration**

  The setup and configuration of a domain for your AWS IoT Core endpoints.
+ **Default endpoint domain**

  The domain that AWS IoT provides with the default endpoint such as `iot:Data-ATS`. To find the default endpoint, run the [describe-endpoint](https://docs.aws.amazon.com/cli/latest/reference/iot/describe-endpoint.html) or [describe-domain-configuration](https://docs.aws.amazon.com/cli/latest/reference/iot/describe-domain-configuration.html) CLI command. Alternatively, go to AWS IoT Core console, choose **Domain configurations** from **Connect** on the left navigation. The default endpoint is listed with the name `iot:Data-ATS`.
+ **AWS managed domain**

  The domain that AWS will manage. Choosing AWS managed domain means that your devices will connect using a data endpoint provided by AWS. AWS will manage the domain and the certificates.
+ **Customer managed domain**

  The domain that you will manage. Also known as custom domain. Choosing customer managed domain means that your devices will connect using a custom domain data endpoint. You will manage the domain and the certificates. Customer managed domain allows you to tailor the endpoint URLs to suit your needs. For example, you can use a custom domain name (`your-domain-name.com`) or apply specific access policies.
+ **Authentication type**

  The authentication type that you choose to authenticate your devices when connecting to AWS IoT Core. When creating a domain configuration, you must specify an authentication type. For more information, see [Choosing an authentication type for your device communication](protocols.md#connection-protocol-auth-mode).
+ **Application protocol**

  The application layer protocols which your devices use when connecting to AWS IoT Core. When creating a domain configuration, you must specify an application protocol. For more information, see [Choosing an application protocol for your device communication](protocols.md#protocol-selection).

## Important notes
<a name="iot-custom-endpoints-configurable-notes"></a>

AWS IoT Core uses the [server name indication (SNI) TLS extension](https://www.rfc-editor.org/rfc/rfc3546) to apply domain configurations. When connecting devices to AWS IoT Core, clients can send the [Server Name Indication (SNI) extension](https://tools.ietf.org/html/rfc3546#section-3.1), which is required for features such as [multi-account registration](https://docs.aws.amazon.com/iot/latest/developerguide/x509-client-certs.html#multiple-account-cert), [configurable endpoints](https://docs.aws.amazon.com/iot/latest/developerguide/iot-custom-endpoints-configurable.html), [custom domains](https://docs.aws.amazon.com/iot/latest/developerguide/iot-custom-endpoints-configurable-custom.html), and [VPC endpoints](https://docs.aws.amazon.com/iot/latest/developerguide/IoTCore-VPC.html). They also must pass a server name that is identical to the domain name that you specify in the domain configuration. To test this service, use the v2 version of the [AWS IoT Device SDKs](https://github.com/aws) in GitHub.

If you create multiple data endpoints in your AWS account, they will share AWS IoT Core resources such as MQTT topics, device shadows, and rules.

When you provide the server certificates for AWS IoT Core custom domain configuration, the certificates have a maximum of four domain names. For more information, see [AWS IoT Core endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/iot-core.html#security-limits).