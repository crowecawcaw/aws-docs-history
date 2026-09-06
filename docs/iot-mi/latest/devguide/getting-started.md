

# Get started with managed integrations for AWS IoT Device Management
<a name="getting-started"></a>

The following sections outline the steps that you need to take to start using Managed Integrations.

**Topics**
+ [Device types](#managedintegrations-terminology-device-types)
+ [Configure encryption key](#3Pcloud-configure-encryption-key)
+ [Onboarding techniques](#different-types-of-oboarding)

## Device types
<a name="managedintegrations-terminology-device-types"></a>

Managed Integrations manages many types of devices. Each device is within one of the following three categories:
+ *Direct-connected devices*: This type of device directly connects to an Managed Integrations endpoint. Typically, these devices are built and managed by device manufacturers that include the Managed Integrations end device SDK for the direct connectivity.
+ *Hub-connected devices*: These devices connect to Managed Integrations through a hub running the managed integrations Hub SDK, which manages device discovery, onboarding, and control functions. End-users can onboard these devices using button press initiation or barcode scanning.

  The following two workflows are supported for onboarding a hub-connected device:
  + An end user initiated button press to start device discovery
  + Barcode-based scanning to perform the device association
+ *Cloud-to-cloud (C2C) devices*: These are devices that are designed and managed by vendors that maintain their own cloud infrastructure and branded mobile applications for device control. Managed integrations customers can access a catalog of pre-built C2C connectors or create their own, to develop IoT solutions that work with multiple third-party vendor clouds through a unified interface.

  When the end user powers on a C2C device for the first time, it must be provisioned with its respective third-party cloud provider for Managed Integrations to obtain its device capabilities and metadata. After completing that provisioning workflow, Managed Integrations can communicate with the cloud device and the third-party cloud provider on behalf of the end user.

**Note**  
A hub is not a specific device type as listed above. Its purpose is serving the role as a controller of smart home devices and facilitating a connection between Managed Integrations and third-party cloud providers. It can serve the role as both a device type as listed above and as a hub.

## Configure encryption key
<a name="3Pcloud-configure-encryption-key"></a>

Security is of paramount importance for data routed between the end user, Managed Integrations, and third-party clouds. One of the methods we support to protect your device data is end-to-end encryption leveraging a secure encryption key for routing your data.

As a customer of Managed Integrations, you have the following two options for using encryption keys:
+ Use the default Managed Integrations-managed encryption key.
+ Provide an AWS KMS key that you created.

For more information on the AWS KMS service, see [Key management service (KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html)

Calling the [PutDefaultEncryptionConfiguration](https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_PutDefaultEncryptionConfiguration.html) API in the *Managed Integrations API Reference Guide* grants you access to update which encryption key option you want to use. By default, managed integrations uses the default managed integrations managed encryption key. You can update your encryption key configuration at any time using the [PutDefaultEncryptionConfiguration](https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_PutDefaultEncryptionConfiguration.html) API.

Additionally, calling the [ GetDefaultEncryptionConfiguration](https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_GetDefaultEncryptionConfiguration.html) API command returns information about the encryption configuration for the AWS account in the default or specified region.

## Onboarding techniques
<a name="different-types-of-oboarding"></a>

 Listed below are the types of onboarding: 

### Direct-connected device onboarding
<a name="getting-started-known-sh-device-onboarding"></a>

See [Provisionee](managedintegrations-sdk-device-provisionee.md) for steps to onboard a direct connected device. 

### Hub onboarding
<a name="getting-started-hub-onboarding"></a>

See [Onboard your hubs to Managed Integrations](managedintegrations-sdk-v2-cookbook-usinghub.md) for steps to onboard the hub. 

### Hub-connected device onboarding
<a name="getting-started-hub-connected-device-onboarding"></a>

See [Onboard devices and operate them in hub](managedintegrations-sdk-v2-cookbook-onboard-to-hub.md) for steps to onboard a hub connected device. 

### Cloud-to-cloud device onboarding
<a name="getting-started-third-party-cloud-device-onboarding"></a>

See [Use a C2C (Cloud-to-Cloud) connector](use-c2c-create-cloud-connector.md) for steps to onboard a cloud device from a third-party cloud vendor to managed integrations. 