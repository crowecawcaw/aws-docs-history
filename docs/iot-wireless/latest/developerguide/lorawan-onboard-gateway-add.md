# Add a gateway to AWS IoT Core for LoRaWAN

You can add your gateway to AWS IoT Core for LoRaWAN by using the console or the CLI.

Before adding your gateway, we recommend that you consider the factors mentioned
in the **Before onboarding your gateway** section of
[Onboard your gateways to
AWS IoT Core for LoRaWAN](lorawan-onboard-gateways.md "lorawan-onboard-gateways.md").

If you're adding your gateway for the first time, we recommend that you use the
console. If you want to add your gateway by using the CLI instead, you must have
already created the necessary IAM role so that the gateway can connect with
AWS IoT Core for LoRaWAN. For information about how to create the role, see [Add an IAM role to allow the
Configuration and Update Server (CUPS) to manage gateway credentials](lorawan-rfregion-permissions.md#lorawan-onboard-permissions "lorawan-rfregion-permissions.md#lorawan-onboard-permissions").

## Add a gateway using the

console

Navigate to the [AWS IoT Core for LoRaWAN](https://console.aws.amazon.com/iot/home#/wireless/landing "https://console.aws.amazon.com/iot/home#/wireless/landing")
**Intro** page of the AWS IoT console and choose **Get
started**, and then choose **Add gateway**. If
you've already added a gateway, choose **View gateway** to
view the gateway that you added. If you would like to add more gateways, choose
**Add gateway**.

1. ###### Provide gateway details and frequency band information

Use the **Gateway details** section to provide
information about the device configuration data such as the
Gateway's EUI and the frequency band configuration.

    * ###### Gateway's EUI


    The EUI (Extended Unique Identifier) of the individual
     gateway device. The EUI is a 16-digit alphanumeric code,
     such as `c0ee40ffff29df10`, that uniquely
     identifies a gateway in your LoRaWAN network. This
     information is specific to your gateway model and you can
     find it on your gateway device or in its user manual.


    ###### Note

    The Gateway's EUI is different from the Wi-Fi MAC address
     that you may see printed on your gateway device. The EUI
     follows a EUI-64 standard that uniquely identifies your
     gateway and therefore cannot be resued in other
     AWS accounts and regions.
    * ###### Frequency band (RFRegion)


    The gateway's frequency band. You can choose from
     `US915`, `EU868`,
     `AU915`, or `AS923-1`, depending
     on what your gateway supports and which country or region
     the gateway is physically connecting from. For more
     information about the bands, see [Consider selection of LoRa frequency
     bands for your gateways and device connection](lorawan-rfregion-permissions.md#lorawan-frequency-bands "lorawan-rfregion-permissions.md#lorawan-frequency-bands").

2. ###### Specify your wireless gateway configuration data
   (optional)

These fields are optional and you can use them to provide
additional information about the gateway and it's
configuration.

    * ###### Name, Description, and Tags for your gateway


    The information in these optional fields comes from how
     you organize and describe the elements in your wireless
     system. You can assign a **Name** to the
     gateway, use the **Description** field to
     provide information about the gateway, and use
     **Tags** to add key-value pairs of
     metadata about the gateway. For more information on naming
     and describing your resources, see [Describing your AWS IoT Wireless
     resources](getting-started.md#iotwireless-describe-resources "getting-started.md#iotwireless-describe-resources").
    * ###### LoRaWAN configuration using subbands and filters


    Optionally, you can also specify LoRaWAN configuration
     data such as the subbands that you want to use and filters
     that can control the flow of traffic. For this tutorial, you
     can skip these fields. For more information, see [Configure subbands and filtering
     capabilities of your LoRaWAN gateways](lorawan-subband-filter-configuration.md "lorawan-subband-filter-configuration.md").

3. ###### Associate an AWS IoT thing with the gateway

Specify whether to create an AWS IoT thing and associate it with the
gateway. Things in AWS IoT can make it easier to search and manage
your devices. Associating a thing with your gateway lets the gateway
access other AWS IoT Core features. 4. ###### Create and download the gateway certificate

To authenticate your gateway so that it can securely communicate
with AWS IoT, your LoRaWAN gateway must present a private key and
certificate to AWS IoT Core for LoRaWAN. Create a **Gateway
certificate** so that AWS IoT can verify your gateway's
identity by using the X.509 Standard.

Click the **Create certificate** button and
download the certificate files. You'll use them later to configure your
gateway. 5. ###### Copy the CUPS and LNS endpoints and download certificates

Your LoRaWAN gateway must connect to a CUPS or LNS endpoint when
establishing a connection to AWS IoT Core for LoRaWAN. We recommend that you
use the CUPS endpoint as it also provides configuration management.
To verify the authenticity of AWS IoT Core for LoRaWAN endpoints, your gateway
will use a trust certificate for each of the CUPS and LNS
endpoints,

Click the **Copy** button to copy the CUPS and LNS
endpoints. You'll need this information later to configure your gateway.
Then click the **Download server trust certificates**
button to download the trust certificates for the CUPS and LNS
endpoints. 6. ###### Create the IAM role for the gateway permissions

You need to add an IAM role that allows the Configuration and
Update Server (CUPS) to manage gateway credentials.

###### Note

In this step, you create the
**IoTWirelessGatewayCertManager** role. If you
have already created this role, you can skip this step. You must do
this before a LoRaWAN gateway tries to connect with AWS IoT Core for LoRaWAN;
however, you need to do it only once.

To create the **IoTWirelessGatewayCertManager** IAM
role for your account, click the **Create role**
button. If the role already exists, select it from the dropdown
list.

Click **Submit** to complete the gateway
creation.

## Add a gateway by using the

API

###### Note

If you're adding a gateway for the first time by using the API or CLI, you
must add the **IoTWirelessGatewayCertManager** IAM role
so that the gateway can connect with AWS IoT Core for LoRaWAN. For information about
how to create the role, see the following section [Add an IAM role to allow the
Configuration and Update Server (CUPS) to manage gateway credentials](lorawan-rfregion-permissions.md#lorawan-onboard-permissions "lorawan-rfregion-permissions.md#lorawan-onboard-permissions").

The following sections show how to add a gateway using the AWS IoT Wireless
API operations or the AWS CLI. You first add your gateway and then associate a
certificate with the gateway. You can also use the additional API operations,
such as to update an existing gateway.

###### Topics

- [How to add your gateway](#lorawan-gateway-api-add "#lorawan-gateway-api-add")
- [Associate a certificate with your
  gateway](#lorawan-gateway-cert "#lorawan-gateway-cert")
- [Additional API operations](#lorawan-gateway-api-list "#lorawan-gateway-api-list")

### How to add your gateway

You can use the AWS CLI to create a wireless gateway by using the [CreateWirelessGateway](../apireference/API_CreateWirelessGateway.md "../apireference/API_CreateWirelessGateway.md") API operation or the [create-wireless-gateway](../../../cli/latest/reference/iotwireless/create-wireless-gateway.md "../../../cli/latest/reference/iotwireless/create-wireless-gateway.md") CLI command to add your wireless
gateway.

###### Note

If your gateway is communicating with class B LoRaWAN devices, you can
also specify certain beaconing parameters when adding the gateway using
the `CreateWirelessGateway` API or the
`create-wireless-gateway` CLI command. For more
information, see [Configure beaconing for your
LoRaWAN gateways](lorawan-gateway-beaconing.md "lorawan-gateway-beaconing.md").

The following example creates a wireless LoRaWAN device gateway. You can
also provide an `input.json` file that will contain additional
details such as the gateway certificate and provisioning credentials.

###### Note

You can also perform this procedure with the API by using the methods
in the AWS API that correspond to the CLI commands shown here.

```
aws iotwireless create-wireless-gateway \
    --lorawan GatewayEui="a1b2c3d4567890ab",RfRegion="US915" \
    --name "myFirstLoRaWANGateway" \
    --description "Using my first LoRaWAN gateway"
    --cli-input-json `file://input.json`
```

### Associate a certificate with your

gateway

After you add your gateway to AWS IoT Wireless, it must be associated
with a certificate to connect to the CUPS endpoint. To connect to the
endpoint, your gateway running LoRa Basics Station requires the following
files:

- `cups.crt` - The gateway's CUPS certificate that it
  uses to connect to the CUPS endpoint.
- `cups.key` - Private key corresponding to the
  certificate.
- `cups.trust` - The trust certificate of the CUPS
  endpoint.
- `cups.uri` - The CUPS endpoint URI.

The following steps show you how to generate a certificate and associate
it with your gateway.

###### Topics

- [Step 1: Generating a
  gateway certificate](#lorawan-gateway-cert-generate "#lorawan-gateway-cert-generate")
- [Step 2: Obtaining server
  trust certificate and CUPS endpoint](#lorawan-gateway-cert-obtain "#lorawan-gateway-cert-obtain")
- [Step 3: Associate the
  certificate with your gateway](#lorawan-gateway-cert-associate "#lorawan-gateway-cert-associate")

#### Step 1: Generating a

gateway certificate

To generate a certificate for your gateway, use the AWS IoT API Reference
API action, [`CreateKeysAndCertificate`](../../../iot/latest/apireference/API_CreateKeysAndCertificate.md "../../../iot/latest/apireference/API_CreateKeysAndCertificate.md"), or the AWS CLI
command, [create-keys-and-certificate](../../../cli/latest/reference/iot/create-keys-and-certificate.md "../../../cli/latest/reference/iot/create-keys-and-certificate.md") CLI command.

The following command shows an example of generating the certificate,
`cups.crt`, and the private key,
`cups.key`.

```
aws iot create-keys-and-certificate \
    --set-as-active --certificate-pem-outfile "cups.crt" \
    --private-key-outfile "cups.key"
```

Running this command generates the certificate and private key, and a
certificate ID. The following example shows an output of running this
command.

```
{
    "certificateArn": "arn:aws:iot:`us-east-1`:`123456789012`:cert/`abc1234d55ef32101a34434bb123cba2a011b2cdefa6bb5cee1a221b4567ab12`",
    "certificateId": "`abc1234d55ef32101a34434bb123cba2a011b2cdefa6bb5cee1a221b4567ab12`",
    "certificatePem": "-----BEGIN CERTIFICATE-----\n..\n-----END CERTIFICATE-----\n,
          "KeyPair": {
              "PublicKey": "-----BEGIN PUBLIC KEY -----\n..\n----END PUBLIC KEY----\n",
              "PrivateKey": "----BEGIN RSA PRIVATE KEY----\n..\nEND RSA PRIVATE KEY----\n"
    }
}
```

Store the certificate ID temporarily, as it will be used in the
subsequent step to associate your certificate with the gateway.

###### Note

You must securely store the private key, `cups.key`. If
you misplace the private key, rerun the
`create-keys-and-certificate` command to generate
another certificate.

#### Step 2: Obtaining server

trust certificate and CUPS endpoint

Now that you've generated the certificate and private key, use the
[GetServiceEndpoint](../apireference/API_GetServiceEndpoint.md "../apireference/API_GetServiceEndpoint.md") API action or the [`get-service-endpoint`](../../../cli/latest/reference/iotwireless/get-service-endpoint.md "../../../cli/latest/reference/iotwireless/get-service-endpoint.md") CLI command to obtain
the server trust certificate, `cups.trust` and the endpoint
URI, `cups.uri`.

The following command shows an example of obtaining the server trust
certificate and the endpoint URI. When running the command, set the
`service-type` parameter to `CUPS`.

```
aws iotwireless get-service-endpoint --service-type CUPS
```

The following shows an output of running the command.

```
{
    "ServiceType": "CUPS",
    "ServiceEndpoint": "https://`ABCDEFGHIJKLMN`.cups.lorawan.`us-east-1`.amazonaws.com:443",
    "ServerTrust": "-----BEGIN CERTIFICATE-----\n..\n-----END CERTIFICATE-----\n"
}
```

The `ServiceEndpoint` obtained from the response
corresponds to the CUPS endpoint, `cups.uri`.

###### Note

Store the `ServerTrust` certificate in a
`.pem` file with the `\n` replaced by new
lines.

#### Step 3: Associate the

certificate with your gateway

You must associate the gateway's certificate that you generated with
the gateway that you added. AWS IoT Core for LoRaWAN will use this information to
identify the certificate that the gateway will use to connect to the
CUPS endpoint.

To associate the certificate with your gateway, use the [AssociateWirelessGatewaywithCertificate](../apireference/API_AssociateWirelessGatewaywithCertificate.md "../apireference/API_AssociateWirelessGatewaywithCertificate.md") API action or the
[`associate-wireless-gateway-with-certificate`](../../../cli/latest/reference/iotwireless/associate-wireless-gateway-with-certificate.md "../../../cli/latest/reference/iotwireless/associate-wireless-gateway-with-certificate.md")
CLI command.

The following command shows an example of associating a certificate
with your gateway.

```
aws iotwireless associate-wireless-gateway-with-certificate \
    --id `<WirelessGatewayId>` \
    --iot-certificate-id `<CertificateId>`
```

Running this command returns the `IotCertificateId`, which
is the ID of the certificate that you associated with the gateway. The
following shows an output of running the command, where the
`IotCertificateId` is the ID of the certificate, such as
`abc1234d55ef32101a34434bb123cba2a011b2cdefa6bb5cee1a221b4567ab12`.

```
{
    "IotCertificateId": "`<CertificateId>`"
}
```

### Additional API operations

You can use the following API actions to perform the tasks associated with
adding, updating, or deleting a LoRaWAN gateway.

###### AWS IoT Wireless API actions for AWS IoT Core for LoRaWAN gateways

- [GetWirelessGateway](../apireference/API_GetWirelessGateway.md "../apireference/API_GetWirelessGateway.md")
- [ListWirelessGateways](../apireference/API_ListWirelessGateways.md "../apireference/API_ListWirelessGateways.md")
- [UpdateWirelessGateway](../apireference/API_UpdateWirelessGateway.md "../apireference/API_UpdateWirelessGateway.md")
- [DeleteWirelessGateway](../apireference/API_DeleteWirelessGateway.md "../apireference/API_DeleteWirelessGateway.md")

For the complete list of the actions and data types available to create
and manage AWS IoT Core for LoRaWAN resources, see the [AWS IoT Wireless API
reference](../apireference/welcome.md "../apireference/welcome.md").

For information about the CLIs that you can use, see [AWS CLI reference](../../../cli/latest/reference/iotwireless/index.md "../../../cli/latest/reference/iotwireless/index.md").
