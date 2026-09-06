

# Hub onboarding setup
<a name="managedintegrations-sdk-v2-cookbook-hubsetup"></a>

Complete these setup steps for each hub device before you begin the fleet provisioning onboarding process. This section describes how to create managed things, set up directory structures, and configure the required certificates.

**Topics**
+ [Step 1: Register a custom endpoint](#managedintegrations-sdk-v2-cookbook-acc)
+ [Step 2: Create a provisioning profile](#managedintegrations-sdk-v2-cookbook-fleet-provision)
+ [Step 3: Create a managed thing (fleet provisioning)](#managedintegrations-sdk-v2-cookbook-managedthing)
+ [Step 4: Create the directory structure](#managedintegrations-sdk-v2-cookbook-hubdir)
+ [Step 5: Add authentication materials to hub device](#managedintegrations-sdk-v2-cookbook-copycert)
+ [Step 6: Create the device configuration file](#managedintegrations-sdk-v2-cookbook-genconfig)
+ [Step 7: Copy the configuration file to your hub](#managedintegrations-sdk-v2-cookbook-copyconfig)

## Step 1: Register a custom endpoint
<a name="managedintegrations-sdk-v2-cookbook-acc"></a>

Create a dedicated communication endpoint that your devices use to exchange data with Managed Integrations. This endpoint establishes a secure connection point for all device-to-cloud messaging, including device commands, status updates, and notifications.

**To register an endpoint**
+ Use the [RegisterCustomEndpoint](https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_RegisterCustomEndpoint.html) API to create an endpoint for device-to-Managed Integrations communication.

  **RegisterCustomEndpoint Request example**

  ```
  aws iot-managed-integrations register-custom-endpoint  
  ```

  **Response:**

  ```
  {
    [{{ACCOUNT-PREFIX}}]-ats.iot.{{AWS-REGION}}.amazonaws.com
  }
  ```
**Note**  
Store the endpoint address. You'll need it for future device communication.

  To return the endpoint information, use the `GetCustomEndpoint` API.

  For more information, see the [RegisterCustomEndpoint](https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_RegisterCustomEndpoint.html) API and the [GetCustomEndpoint](https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_GetCustomEndpoint.html) API in the Managed Integrations *API Reference Guide*.

## Step 2: Create a provisioning profile
<a name="managedintegrations-sdk-v2-cookbook-fleet-provision"></a>

A provisioning profile contains the security credentials and configuration settings your devices need to connect to Managed Integrations. 

**To create a fleet provisioning profile**
+ <a name="managedintegrations-sdk-v2-cookbook-provisioning"></a>Call the [CreateProvisioningProfile](https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_CreateProvisioningProfile.html) API to generate the following:
  + A provisioning template that defines device connection settings
  + A claim certificate and private key for device authentication
**Important**  
Store the claim certificate, private key, and template ID securely. You'll need these credentials to onboard devices to Managed Integrations. If you lose these credentials, you must create a new provisioning profile.

**`CreateProvisioningProfile` example request**

```
aws iot-managed-integrations create-provisioning-profile \
    --provisioning-type FLEET_PROVISIONING \
    --name PROFILE_NAME
```

**Response:**

```
{
"Arn":"arn:aws:iotmanagedintegrations:{{AWS-REGION}}:{{ACCOUNT-ID}}:provisioning-profile/{{PROFILE-ID}}",
    "ClaimCertificate":
  "-----BEGIN CERTIFICATE-----
  MIICiTCCAfICCQD6m7.....w3rrszlaEXAMPLE=
  -----END CERTIFICATE-----",
    "ClaimCertificatePrivateKey":
  "-----BEGIN RSA PRIVATE KEY-----
  MIICiTCCAfICCQ...3rrszlaEXAMPLE=
 -----END RSA PRIVATE KEY-----",
    "Id": "{{PROFILE-ID}}",
    "{{PROFILE-NAME}}",
         "ProvisioningType": "FLEET_PROVISIONING"
}
```

## Step 3: Create a managed thing (fleet provisioning)
<a name="managedintegrations-sdk-v2-cookbook-managedthing"></a>

Use the `CreateManagedThing` API to create a managed thing for your hub device. Each hub requires its own managed thing with unique authentication materials. For more information, see the [CreateManagedThing](https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_CreateManagedThing.html) API in the Managed Integrations *API Reference*.

When you create a managed thing, specify these parameters:
+ `Role`: Set this value to `CONTROLLER` for hubs that do not support command and control, otherwise set to `DEVICE`.
+ `AuthenticationMaterialType`: Set this value to `WIFI_SETUP_QR_BAR_CODE`.
+ `AuthenticationMaterial`: Include the following fields. You can use either `UPC` or `EAN` but not both.
  + `SN`: The unique serial number for this device
  + `UPC`: The universal product code for this device
  + `EAN`: The international article number for this device

**Important**  
Each device must have a unique serial number (SN) in its authentication material.

**`CreateManagedThing` Request example**:

```
{ 
 "Role": "CONTROLLER",
 "AuthenticationMaterialType": "WIFI_SETUP_QR_BAR_CODE",
 "AuthenticationMaterial": "SN:123456789524;UPC:829576019524"
}
```

For more information, see [CreateManagedThing](https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_CreateManagedThing.html) in the Managed Integrations *API Reference*.

### (Optional) Get managed thing
<a name="managedintegrations-sdk-v2-cookbook-managedthing-get"></a>

The `ProvisioningStatus` of your managed thing must be `PRE_ASSOCIATED` before you can proceed. For more information on ProvisioningStatus, see [Device Provisioning](https://docs.aws.amazon.com/iot-mi/latest/devguide/device-provisioning.html). Use the `GetManagedThing` API to verify that your managed thing exists and is ready for provisioning. For more information, see [GetManagedThing](https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_GetManagedThing.html) in the Managed Integrations *API Reference*.

## Step 4: Create the directory structure
<a name="managedintegrations-sdk-v2-cookbook-hubdir"></a>

Create directories for your configuration files and certificates. By default, the hub onboarding process uses the `/data/aws/iotmi/config/iotmi_config.json`.

You can specify custom paths for certificates and private keys in the configuration file. This guide uses the default path `/data/aws/iotmi/certs`.

```
mkdir -p /data/aws/iotmi/config
mkdir -p /data/aws/iotmi/certs

/data/
    aws/
        iotmi/
            config/
            certs/
```

## Step 5: Add authentication materials to hub device
<a name="managedintegrations-sdk-v2-cookbook-copycert"></a>

Copy certificates and keys to your hub device, then create a device-specific configuration file. These files establish secure communication between your hub and Managed Integrations during the provisioning process.

**To copy claim certificate and key**
+ Copy these authentication files from your `CreateProvisioningProfile` API response to your hub device:
  + `claim_cert.pem`: The claim certificate (common to all devices)
  + `claim_pk.key`: The private key for the claim certificate

  Place both files in the `/data/aws/iotmi/certs` directory.
**Important**  
 When storing certificates and private keys in PEM format, ensure proper formatting by handling newline characters correctly. For PEM-encoded files, the newline characters `(\n)` must be replaced with actual line separators, as simply storing escaped newlines will not be correctly retrieved later. 
**Note**  
If you use secure storage, store these credentials in your secure storage location instead of the file system. For more information, see [Create a custom certificate handler for secure storage](managedintegrations-sdk-v2-cookbook-certhandler.md).

## Step 6: Create the device configuration file
<a name="managedintegrations-sdk-v2-cookbook-genconfig"></a>

Create a configuration file that contains unique device identifiers, certificate locations, and provisioning settings. The SDK uses this file during hub onboarding to authenticate your device, manage provisioning status, and store connection settings.

**Note**  
Each hub device requires its own configuration file with unique device-specific values.

Use the following procedure to create or modify your configuration file, and copy it to the hub.
+ <a name="managedintegrations-sdk-v2-cookbook-modifyconfig-fleet"></a>**Create or modify the configuration file (fleet provisioning)**. 

  Configure these required fields in the device configuration file:
  + Certificate paths

    1. `iot_claim_cert_path`: Location of your claim certificate (`claim_cert.pem`)

    1. `iot_claim_pk_path`: Location of your private key (`claim_pk.key`)

    1. Use `SECURE_STORAGE` for both fields when implementing the Secure Storage Cert Handler
  + Connection settings

    1. `fp_template_name`: The `ProvisioningProfile` name from earlier.

    1. `endpoint_url`: Your Managed Integrations endpoint URL from the `RegisterCustomEndpoint` API response (same for all devices in a Region).
  + Device identifiers

    1. `SN`: Device serial number that matches your `CreateManagedThing` API call (unique per device)

    1. `UPC`Universal product code from your `CreateManagedThing` API call (same for all devices of this product) 

  ```
  {
      "ro": {
          "iot_provisioning_method": "FLEET_PROVISIONING",
          "iot_claim_cert_path": "{{<SPECIFY_THIS_FIELD>}}",
          "iot_claim_pk_path": "{{<SPECIFY_THIS_FIELD>}}",
          "fp_template_name": "{{<SPECIFY_THIS_FIELD>}}",        
          "endpoint_url": "{{<SPECIFY_THIS_FIELD>}}",
          "SN": "{{<SPECIFY_THIS_FIELD>}}",
          "UPC": "{{<SPECIFY_THIS_FIELD>}}"        
      },
      "rw": {
          "iot_provisioning_state": "NOT_PROVISIONED"
      }
  }
  ```

### Contents of the configuration file
<a name="managedintegrations-sdk-v2-cookbook-config-contents"></a>

Review the contents of the `iotmi_config.json` file.


**Contents**  

| Key | Values | Added by customer? | Notes | 
| --- | --- | --- | --- | 
| iot\_provisioning\_method | FLEET\_PROVISIONING | Yes | Specify the provisioning method that you want to use. | 
| iot\_claim\_cert\_path | The file path that you specify or SECURE\_STORAGE. For example, /data/aws/iotmi/certs/claim\_cert.pem | Yes | Specify the file path that you want to use or SECURE\_STORAGE. | 
| iot\_claim\_pk\_path | The file path that you specify or SECURE\_STORAGE. For example, /data/aws/iotmi/certs/claim\_pk.pem | Yes | Specify the file path that you want to use or SECURE\_STORAGE. | 
| fp\_template\_name | The fleet provisioning template name should be equal to the name of the ProvisioningProfile that was used earlier. | Yes | Equal to the name of the ProvisioningProfile that was used earlier | 
| endpoint\_url | The endpoint URL for Managed Integrations. | Yes | Your devices use this URL to connect to the Managed Integrations cloud. To obtain this information, use the [RegisterCustomEndpoint](https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_RegisterCustomEndpoint.html) API. | 
| SN | The device serial number. For example, AIDACKCEVSQ6C2EXAMPLE. | Yes | You must provide this unique information for each device. | 
| UPC | Device universal product code. For example, 841667145075. | Yes | You must provide this information for the device. | 
| managed\_thing\_id | The ID of the managed thing. | No | This information is added later by the onboarding process after hub provisioning. | 
| iot\_provisioning\_state | The provisioning state. | Yes | The provisioning state must be set as NOT\_PROVISIONED. | 
| iot\_permanent\_cert\_path | The IoT certificate path. For example, /data/aws/iotmi/iot\_cert.pem. | No | This information is added later by the onboarding process after hub provisioning. | 
| iot\_permanent\_pk\_path | The IoT private key file path. For example, /data/aws/iotmi/iot\_pk.pem. | No | This information is added later by the onboarding process after hub provisioning. | 
| client\_id | The client ID that will be used for MQTT connections. | No | This information is added later by the onboarding process after hub provisioning, for other components to consume. | 
| mqtt\_keep\_alive\_interval | Range is 30-1200, and units are in seconds. The default value is 300. | Yes | Use this to set a keep-alive interval for MQTT connections. | 
| event\_manager\_upper\_bound | The default value is 500. | No | This information is added later by the onboarding process after hub provisioning, for other components to consume. | 

## Step 7: Copy the configuration file to your hub
<a name="managedintegrations-sdk-v2-cookbook-copyconfig"></a>

Copy your configuration file to `/data/aws/iotmi/config` or your custom directory path. You'll provide this path to the `HubOnboarding` binary during the onboarding process.

**For fleet provisioning**

```
/data/
    aws/
        iotmi/
            config/
                iotmi_config.json
            certs/
                claim_cert.pem
                claim_pk.key
```