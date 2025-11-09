# Hub onboarding setup

Complete these setup steps for each hub device before you begin the fleet provisioning
onboarding process. This section describes how to create managed things, set up directory
structures, and configure the required certificates.

###### Setup steps

- [Step 1: Register a custom endpoint](#managedintegrations-sdk-v2-cookbook-acc "#managedintegrations-sdk-v2-cookbook-acc")
- [Step 2: Create a provisioning profile](#managedintegrations-sdk-v2-cookbook-fleet-provision "#managedintegrations-sdk-v2-cookbook-fleet-provision")
- [Step 3: Create a managed thing
  (fleet provisioning)](#managedintegrations-sdk-v2-cookbook-managedthing "#managedintegrations-sdk-v2-cookbook-managedthing")
- [Step 4: Create the directory
  structure](#managedintegrations-sdk-v2-cookbook-hubdir "#managedintegrations-sdk-v2-cookbook-hubdir")
- [Step 5: Add authentication materials to hub device](#managedintegrations-sdk-v2-cookbook-copycert "#managedintegrations-sdk-v2-cookbook-copycert")
- [Step 6: Create the device
  configuration file](#managedintegrations-sdk-v2-cookbook-genconfig "#managedintegrations-sdk-v2-cookbook-genconfig")
- [Step 7: Copy the configuration file to your hub](#managedintegrations-sdk-v2-cookbook-copyconfig "#managedintegrations-sdk-v2-cookbook-copyconfig")

## Step 1: Register a custom endpoint

Create a dedicated communication endpoint that your devices use to exchange data with
managed integrations. This endpoint establishes a secure connection point for all device-to-cloud
messaging, including device commands, status updates, and notifications.

###### To register an endpoint

- Use the [RegisterCustomEndpoint](../APIReference/API_RegisterCustomEndpoint.md "../APIReference/API_RegisterCustomEndpoint.md") API to create an endpoint for device-to-managed integrations
  communication.

**RegisterCustomEndpoint Request example**

```
aws iot-managed-integrations register-custom-endpoint

```

**Response:**

```
{
  [`ACCOUNT-PREFIX`]-ats.iot.`AWS-REGION`.amazonaws.com
}
```

###### Note

Store the endpoint address. You'll need it for future device communication.

To return the endpoint information, use the `GetCustomEndpoint` API.

For more information, see the [RegisterCustomEndpoint](../APIReference/API_RegisterCustomEndpoint.md "../APIReference/API_RegisterCustomEndpoint.md") API and the [GetCustomEndpoint](../APIReference/API_GetCustomEndpoint.md "../APIReference/API_GetCustomEndpoint.md") API in the managed integrations _API Reference Guide_.

## Step 2: Create a provisioning profile

A provisioning profile contains the security credentials and configuration settings your
devices need to connect to managed integrations.

###### To create a fleet provisioning profile

- Call the [CreateProvisioningProfile](../APIReference/API_CreateProvisioningProfile.md "../APIReference/API_CreateProvisioningProfile.md") API to generate the following:
  - A provisioning template that defines device connection settings
  - A claim certificate and private key for device authentication

###### Important

Store the claim certificate, private key, and template ID securely. You'll need
these credentials to onboard devices to managed integrations. If you lose these credentials, you
must create a new provisioning profile.

**`CreateProvisioningProfile` example
request**

```
aws iot-managed-integrations create-provisioning-profile \
    --provisioning-type FLEET_PROVISIONING \
    --name PROFILE_NAME

```

**Response:**

```
{
"Arn":"arn:aws:iotmanagedintegrations:`AWS-REGION`:`ACCOUNT-ID`:provisioning-profile/`PROFILE-ID`",
    "ClaimCertificate":
  "-----BEGIN CERTIFICATE-----
  MIICiTCCAfICCQD6m7.....w3rrszlaEXAMPLE=
  -----END CERTIFICATE-----",
    "ClaimCertificatePrivateKey":
  "-----BEGIN RSA PRIVATE KEY-----
  MIICiTCCAfICCQ...3rrszlaEXAMPLE=
 -----END RSA PRIVATE KEY-----",
    "Id": "`PROFILE-ID`",
    "`PROFILE-NAME`",
         "ProvisioningType": "FLEET_PROVISIONING"
}
```

## Step 3: Create a managed thing

(fleet provisioning)

Use the `CreateManagedThing` API to create a managed thing for your hub
device. Each hub requires its own managed thing with unique authentication materials. For
more information, see the [CreateManagedThing](../APIReference/API_CreateManagedThing.md "../APIReference/API_CreateManagedThing.md") API in the managed integrations _API Reference_.

When you create a managed thing, specify these parameters:

- `Role`: Set this value to `CONTROLLER` for hubs that do not support command and control, otherwise set to `DEVICE`.
- `AuthenticationMaterialType`: Set this value to `WIFI_SETUP_QR_BAR_CODE`.
- `AuthenticationMaterial`: Include the following fields. You can use either `UPC` or `EAN` but not both.
  - `SN`: The unique serial number for this device
  - `UPC`: The universal product code for this device
  - `EAN`: The international article number for this device

###### Important

Each device must have a unique serial number (SN) in its authentication
material.

**`CreateManagedThing` Request example**:

```
{
 "Role": "`CONTROLLER`",
 "AuthenticationMaterialType": "`WIFI_SETUP_QR_BAR_CODE`",
 "AuthenticationMaterial": "SN:`123456789524`;UPC:`829576019524`"
}
```

For more information, see [CreateManagedThing](../APIReference/API_CreateManagedThing.md "../APIReference/API_CreateManagedThing.md") in the managed integrations _API Reference_.

### (Optional) Get managed

thing

The `ProvisioningStatus` of your managed thing must be `PRE_ASSOCIATED` before you can proceed. For more information on ProvisioningStatus, see [Device Provisioning](device-provisioning.md "device-provisioning.md").
Use the `GetManagedThing` API to verify that your managed thing exists and is ready for provisioning.
For more information, see [GetManagedThing](../APIReference/API_GetManagedThing.md "../APIReference/API_GetManagedThing.md") in the managed integrations _API Reference_.

## Step 4: Create the directory

structure

Create directories for your configuration files and certificates. By default, the hub
onboarding process uses the `/data/aws/iotmi/config/iotmi_config.json`.

You can specify custom paths for certificates and private keys in the configuration
file. This guide uses the default path `/data/aws/iotmi/certs`.

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

Copy certificates and keys to your hub device, then create a device-specific
configuration file. These files establish secure communication between your hub and managed integrations
during the provisioning process.

###### To copy claim certificate and

key

- Copy these authentication files from your `CreateProvisioningProfile` API
  response to your hub device:

      + `claim_cert.pem`: The claim certificate (common to all
       devices)
      + `claim_pk.key`: The private key for the claim certificate

  Place both files in the `/data/aws/iotmi/certs` directory.

###### Important

When storing certificates and private keys in PEM format, ensure proper formatting by handling newline characters correctly.
For PEM-encoded files, the newline characters `(\n)` must be replaced with actual line separators,
as simply storing escaped newlines will not be correctly retrieved later.

###### Note

If you use secure storage, store these credentials in your secure storage location
instead of the file system. For more information, see [Create a custom certificate handler for secure storage](managedintegrations-sdk-v2-cookbook-certhandler.md "managedintegrations-sdk-v2-cookbook-certhandler.md").

## Step 6: Create the device

configuration file

Create a configuration file that contains unique device identifiers,
certificate locations, and provisioning settings. The SDK uses this file during hub
onboarding to authenticate your device, manage provisioning status, and store connection
settings.

###### Note

Each hub device requires its own configuration file with unique device-specific
values.

Use the following procedure to create or modify your configuration file, and copy it to the
hub.

- **Create or modify the configuration file (fleet
  provisioning)**.

Configure these required fields in the device configuration file:

    + Certificate paths




    	1. `iot_claim_cert_path`: Location of your claim certificate
    	 (`claim_cert.pem`)
    	2. `iot_claim_pk_path`: Location of your private key
    	 (`claim_pk.key`)
    	3. Use `SECURE_STORAGE` for both fields when implementing the Secure
    	 Storage Cert Handler
    + Connection settings




    	1. `fp_template_name`: The `ProvisioningProfile` name from earlier.
    	2. `endpoint_url`: Your managed integrations endpoint URL from the
    	 `RegisterCustomEndpoint` API response (same for all devices in a
    	 Region).
    + Device identifiers




    	1. `SN`: Device serial number that matches your
    	 `CreateManagedThing` API call (unique per device)
    	2. `UPC`Universal product code from your
    	 `CreateManagedThing` API call (same for all devices of this
    	 product)

```
{
    "ro": {
        "iot_provisioning_method": "FLEET_PROVISIONING",
        "iot_claim_cert_path": "`<SPECIFY_THIS_FIELD>`",
        "iot_claim_pk_path": "`<SPECIFY_THIS_FIELD>`",
        "fp_template_name": "`<SPECIFY_THIS_FIELD>`",
        "endpoint_url": "`<SPECIFY_THIS_FIELD>`",
        "SN": "`<SPECIFY_THIS_FIELD>`",
        "UPC": "`<SPECIFY_THIS_FIELD>`"
    },
    "rw": {
        "iot_provisioning_state": "NOT_PROVISIONED"
    }
}
```

### Contents of the configuration

file

Review the contents of the `iotmi_config.json`
file.

| Contents                    | Key                                                                                                                  | Values | Added by customer?                                                                                                                                                                                                                          | Notes |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| `iot_provisioning_method`   | `FLEET_PROVISIONING`                                                                                                 | Yes    | Specify the provisioning method that you want to use.                                                                                                                                                                                       |
| `iot_claim_cert_path`       | The file path that you specify or `SECURE_STORAGE`. For example,<br>`/data/aws/iotmi/certs/claim_cert.pem`           | Yes    | Specify the file path that you want to use or<br>`SECURE_STORAGE`.                                                                                                                                                                          |
| `iot_claim_pk_path`         | The file path that you specify or `SECURE_STORAGE`. For example,<br>`/data/aws/iotmi/certs/claim_pk.pem`             | Yes    | Specify the file path that you want to use or<br>`SECURE_STORAGE`.                                                                                                                                                                          |
| `fp_template_name`          | The fleet provisioning template name should be equal to the name of the `ProvisioningProfile` that was used earlier. | Yes    | Equal to the name of the `ProvisioningProfile` that was used earlier                                                                                                                                                                        |
| `endpoint_url`              | The endpoint URL for managed integrations.                                                                           | Yes    | Your devices use this URL to connect to the managed integrations cloud. To obtain this<br>information, use the [RegisterCustomEndpoint](../APIReference/API_RegisterCustomEndpoint.md "../APIReference/API_RegisterCustomEndpoint.md") API. |
| `SN`                        | The device serial number. For example, `AIDACKCEVSQ6C2EXAMPLE`.                                                      | Yes    | You must provide this unique information for each device.                                                                                                                                                                                   |
| `UPC`                       | Device universal product code. For example,<br>`841667145075`.                                                       | Yes    | You must provide this information for the device.                                                                                                                                                                                           |
| `managed_thing_id`          | The ID of the managed thing.                                                                                         | No     | This information is added later by the onboarding process after hub<br>provisioning.                                                                                                                                                        |
| `iot_provisioning_state`    | The provisioning state.                                                                                              | Yes    | The provisioning state must be set as `NOT_PROVISIONED`.                                                                                                                                                                                    |
| `iot_permanent_cert_path`   | The IoT certificate path. For example,<br>`/data/aws/iotmi/iot_cert.pem`.                                            | No     | This information is added later by the onboarding process after hub<br>provisioning.                                                                                                                                                        |
| `iot_permanent_pk_path`     | The IoT private key file path. For example,<br>`/data/aws/iotmi/iot_pk.pem`.                                         | No     | This information is added later by the onboarding process after hub<br>provisioning.                                                                                                                                                        |
| `client_id`                 | The client ID that will be used for MQTT connections.                                                                | No     | This information is added later by the onboarding process after hub<br>provisioning, for other components to consume.                                                                                                                       |
| `mqtt_keep_alive_interval`  | Range is 30-1200, and units are in seconds. The default value is 300.                                                | Yes    | Use this to set a keep-alive interval for MQTT connections.                                                                                                                                                                                 |
| `event_manager_upper_bound` | The default value is 500.                                                                                            | No     | This information is added later by the onboarding process after hub<br>provisioning, for other components to consume.                                                                                                                       |

## Step 7: Copy the configuration file to your hub

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
