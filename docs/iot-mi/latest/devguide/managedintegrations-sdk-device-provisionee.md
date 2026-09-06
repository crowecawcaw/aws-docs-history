

# Provisionee
<a name="managedintegrations-sdk-device-provisionee"></a>

The provisionee is a component of Managed Integrations that enables fleet provisioning by claim. With the provisionee, you securely provision your devices. The SDK creates the necessary resources for device provisioning, which includes the device certificate and private keys that are obtained from the Managed Integrations cloud. When you want to provision your devices, or if there are any changes that can require you to re-provision your devices, you can use the provisionee.

**Topics**
+ [Provisionee workflow](#managedintegrations-sdk-device-provisionee-how)
+ [Set environment variables](#sdk-provisionee-envvars)
+ [Register a custom endpoint](#sdk-provisionee-endpoint-create)
+ [Create a provisioning profile](#sdk-provisionee-template-create)
+ [Create a managed thing](#sdk-provisionee-managed-thing-create)
+ [SDK user Wi-Fi provisioning](#sdk-provisionee-endpoint-wifi)
+ [Fleet provisioning by claim](#sdk-provisionee-endpoint-claim)
+ [Managed thing capabilities](#sdk-provisionee-endpoint-update)

## Provisionee workflow
<a name="managedintegrations-sdk-device-provisionee-how"></a>

The process requires setup on both cloud and device sides. Customers configure cloud requirements like custom endpoints, provisioning profiles, and managed things. At first device power-on, the provisionee:

1. Connects to the Managed Integrations endpoint using a claim certificate

1. Validates device parameters through fleet provisioning hooks

1. Obtains and stores a permanent certificate and private key on the device

1. The device uses the permanent certificate to reconnect

1. Discovers and uploads device capabilities to Managed Integrations

After successful provisioning, the device communicates directly with Managed Integrations. The provisionee activates only for re-provisioning tasks.

## Set environment variables
<a name="sdk-provisionee-envvars"></a>

Set the following AWS credentials in your cloud environment:

```
$ export AWS_ACCESS_KEY_ID=YOUR-ACCOUNT-ACCESS-KEY-ID
$ export AWS_SECRET_ACCESS_KEY=YOUR-ACCOUNT-SECRET-ACCESS-KEY
$ export AWS_DEFAULT_REGION=YOUR-DEFAULT-REGION
```

## Register a custom endpoint
<a name="sdk-provisionee-endpoint-create"></a>

Use the [RegisterCustomEndpoint](https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_RegisterCustomEndpoint.html) API command in your cloud environment to create a custom endpoint for device-to-cloud communication.

```
aws iot-managed-integrations register-custom-endpoint
```

**Example response**

```
{ "EndpointAddress":"{{[ACCOUNT-PREFIX]}}-ats.iot.{{AWS-REGION}}.amazonaws.com" }
```

**Note**  
 Store the endpoint address for configuring provisioning parameters. use the `GetCustomEndpoint` API, to return endpoint information. For more information, see [GetCustomEndpoint](https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_GetCustomEndpoint.html) API, and [RegisterCustomEndpoint](https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_RegisterCustomEndpoint.html) API in the *Managed Integrations API Reference Guide*. 

## Create a provisioning profile
<a name="sdk-provisionee-template-create"></a>

Create a provisioning profile that defines your fleet provisioning method. Run the [CreateProvisioningProfile](https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_CreateProvisioningProfile.html) API in your cloud environment to return a claim certificate and private key for device authentication:

```
aws iot-managed-integrations create-provisioning-profile \
--provisioning-type "FLEET_PROVISIONING" \
--name "PROVISIONING-PROFILE-NAME"
```

**Example response**

```
{ "Arn":"arn:aws:iot-managed-integrations:AWS-REGION:YOUR-ACCOUNT-ID:provisioning-profile/PROFILE_NAME",
    "ClaimCertificate":"string",
    "ClaimCertificatePrivateKey":"string",
    "Name":"ProfileName",
    "ProvisioningType":"FLEET_PROVISIONING"}
```

You can implement the corePKCS11 platform abstraction library (PAL) to make the corePKCS11 library work with your device. The corePKCS11 PAL ports must provide a location to store the claim certificate and private key. Using this feature, you can securely store the device's private key and certificate. You can store the private key and certificate on a hardware security module (HSM) or a trusted platform module (TPM).

## Create a managed thing
<a name="sdk-provisionee-managed-thing-create"></a>

Register your device with Managed Integrations cloud by using the [CreateManagedThing](https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_CreateManagedThing.html) API. Include the serial number (SN) and universal product code (UPC) of your device:

```
aws iot-managed-integrations create-managed-thing —role DEVICE \
  --authentication-material-type WIFI_SETUP_QR_BAR_CODE \
  --authentication-material "SN:DEVICE-SN;UPC:DEVICE-UPC;"
```

The following displays a sample API response.

```
{
   "Arn":"arn:aws:iot-managed-integrations:AWS-REGION:ACCOUNT-ID:managed-thing/59d3c90c55c4491192d841879192d33f",
   "CreatedAt":1.730960226491E9,
   "Id":"59d3c90c55c4491192d841879192d33f"
}
```

The API returns the **Managed thing ID** that can be used for provisioning validation. You will need to provide the device serial number (SN) and universal product code (UPC), which are matched with the approved managed thing during the provisioning transaction. The transaction returns a result similar to the following:

```
/**
 * @brief Device info structure.
 */
typedef struct iotmiDev_DeviceInfo 
{
    char serialNumber[ IOTMI_DEVICE_MAX_SERIAL_NUMBER_LENGTH + 1U ];
    char universalProductCode[ IOTMI_DEVICE_MAX_UPC_LENGTH + 1U ];
    char internationalArticleNumber[ IOTMI_DEVICE_MAX_EAN_LENGTH + 1U ];
} iotmiDev_DeviceInfo_t;
```

## SDK user Wi-Fi provisioning
<a name="sdk-provisionee-endpoint-wifi"></a>

Device manufacturers and solution providers have their own proprietary Wi-Fi provisioning service for receiving and configuring Wi-Fi credentials. The Wi-Fi provisioning service involves using dedicated mobile apps, Bluetooth Low Energy (BLE) connections, and other proprietary protocols to securely transfer Wi-Fi credentials for the initial setup process.

The consumer of the End device SDK must implement the Wi-Fi provisioning service and the device can connect to a Wi-Fi network.

Alternatively, the End device SDK can be built using the `IOTMI_USE_WSS_PROVISIONEE` build flag to enable WiFi Simple Setup (WSS) provisioning. WSS uses the Hub SDK's provisioner to automatically provision WiFi credentials, providing an alternative to proprietary WiFi provisioning methods. For more information, see [WiFi Simple Setup to onboard and operate devices](managedintegrations-sdk-v2-cookbook-wss.md).

## Fleet provisioning by claim
<a name="sdk-provisionee-endpoint-claim"></a>

Using the provisionee, the end user can provision a unique certificate and register it with Managed Integrations using provisioning by claim.

The client ID can be acquired either from the provisioning template response or the device certificate `<common name>“_”<serial number>`

## Managed thing capabilities
<a name="sdk-provisionee-endpoint-update"></a>

The provisionee discovers the managed thing capabilities, then uploads the capabilities to Managed Integrations. It makes the capabilities available to apps and other services to access. Devices, other web clients, and services can update the capabilities by using MQTT and the reserved MQTT topic, or HTTP using the REST API.