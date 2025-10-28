# Install the Hub SDK

with AWS IoT Greengrass

Deploy the managed integrations Hub SDK components for your devices using AWS IoT Greengrass (Java
Version).

###### Note

You must have already set up and have an understanding of AWS IoT Greengrass. For more information,
see [What is AWS IoT Greengrass](../../../greengrass/v2/developerguide/what-is-iot-greengrass.md "../../../greengrass/v2/developerguide/what-is-iot-greengrass.md") in the
_AWS IoT Greengrass developer guide documentation_.

The AWS IoT Greengrass user must have permission to modify the following directories:

- `/dev/aipc`
- `/data/aws/iotmi/config`
- `/data/ace/kvstorage`

###### Topics

- [Deploy components
  locally](#managedintegrations-sdk-v2-cookbook-deployment-local "#managedintegrations-sdk-v2-cookbook-deployment-local")
- [Cloud
  deployment](#managedintegrations-sdk-v2-cookbook-deployment-cloud "#managedintegrations-sdk-v2-cookbook-deployment-cloud")
- [Verify hub
  provisioning](#managedintegrations-sdk-v2-cookbook-validation-hub "#managedintegrations-sdk-v2-cookbook-validation-hub")
- [Verify CDMB
  operation](#managedintegrations-sdk-v2-cookbook-validation-cdmb "#managedintegrations-sdk-v2-cookbook-validation-cdmb")
- [Verify
  LPW-Provisioner operation](#managedintegrations-sdk-v2-cookbook-validation-provisioner "#managedintegrations-sdk-v2-cookbook-validation-provisioner")

## Deploy components

locally

Use the [CreateDeployment](../../../greengrass/v2/APIReference/API_CreateDeployment.md "../../../greengrass/v2/APIReference/API_CreateDeployment.md") AWS IoT Greengrass API on your device to deploy the Hub SDK components. The
version numbers are not static and can vary based on the version you use at the time. Use
the following format for `version`:
com.amazon.IoTManagedIntegrationsDevice.AceCommon=`0.2.0`.

```
/greengrass/v2/bin/greengrass-cli deployment create \
--recipeDir recipes \
--artifactDir artifacts \
-m "com.amazon.IoTManagedIntegrationsDevice.AceCommon=`version`" \
-m "com.amazon.IoTManagedIntegrationsDevice.HubOnboarding=`version`" \
-m "com.amazon.IoTManagedIntegrationsDevice.AceZigbee=`version`" \
-m "com.amazon.IoTManagedIntegrationsDevice.LPW-Provisioner=`version`" \
-m "com.amazon.IoTManagedIntegrationsDevice.Agent=`version`" \
-m "com.amazon.IoTManagedIntegrationsDevice.MQTTProxy=`version`" \
-m "com.amazon.IoTManagedIntegrationsDevice.CDMB=`version`" \
-m "com.amazon.IoTManagedIntegrationsDevice.AceZwave=`version`"
```

## Cloud

deployment

Follow the instructions in the [AWS IoT Greengrass developer
guide](../../../greengrass/v2/developerguide/upload-first-component.md "../../../greengrass/v2/developerguide/upload-first-component.md") to perform the following steps:

1. Upload artifacts to Amazon S3.
2. Update recipes to include the Amazon S3 artifact location.
3. Create a cloud deployment to the device for the new components.

## Verify hub

provisioning

Confirm successful provisioning by checking your configuration file. Open the
`/data/aws/iotmi/config/iotmi_config.json` file and verify the state is set
to `PROVISIONED`.

## Verify CDMB

operation

Check the logs file for CDMB startup messages and successful initialization. The
`logs file` location can vary depending on where AWS IoT Greengrass is
installed.

```
tail -f -n 100 `/greengrass/v2/logs/`com.amazon.IoTManagedIntegrationsDevice.CDMB.log
```

Example

```
[2024-09-06 02:31:54.413758906][IoTManagedIntegrationsDevice_CDMB][info] Successfully subscribed to topic: south/bF|gi_044F8821D0193608C8D5BF80858E20A56E3A8490/control
[2024-09-06 02:31:54.513956059][IoTManagedIntegrationsDevice_CDMB][info] Successfully subscribed to topic: south/bF|gi_044F8821D0193608C8D5BF80858E20A56E3A8490/setup
```

## Verify

LPW-Provisioner operation

Check the logs file for LPW-Provisioner startup messages and successful initialization.
The `logs file` location can vary depending on where AWS IoT Greengrass is
installed.

```
tail -f -n 100 `/greengrass/v2/logs/`com.amazon.IoTManagedIntegrationsDevice.LPW-Provisioner.log
```

Example

```
[2024-09-06 02:33:22.068898877][LPWProvisionerCore][info] Successfully subscribed to topic: south/bF|gi_044F8821D0193608C8D5BF80858E20A56E3A8490/setup
```
