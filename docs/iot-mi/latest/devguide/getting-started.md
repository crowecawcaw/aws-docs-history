# Get started with managed integrations for AWS IoT Device Management

The following sections outline the steps that you need to take to start using managed integrations.

###### Topics

- [Device types](#managedintegrations-terminology-device-types "#managedintegrations-terminology-device-types")
- [Configure encryption key](#3Pcloud-configure-encryption-key "#3Pcloud-configure-encryption-key")
- [Onboarding techniques](#different-types-of-oboarding "#different-types-of-oboarding")

## Device types

Managed integrations manages many types of devices. Each device is within one of the
following three categories:

- _Direct-connected devices_: This type of device directly connects to
  an managed integrations endpoint. Typically, these devices are built and managed by device manufacturers
  that include the managed integrations end device SDK for the direct connectivity.
- _Hub-connected devices_: These devices connect to managed integrations through a
  hub running the managed integrations Hub SDK, which manages device discovery, onboarding, and control functions.
  End-users can onboard these devices using button press initiation or barcode
  scanning.

The following two workflows are supported for onboarding a hub-connected
device:

    + An end user initiated button press to start device discovery
    + Barcode-based scanning to perform the device association

- _Cloud-to-cloud (C2C) devices_: These are devices that are designed and managed by vendors that maintain their own cloud infrastructure and branded
  mobile applications for device control. Managed integrations customers can access a catalog of pre-built C2C connectors or create their own, to develop IoT solutions
  that work with multiple third-party vendor clouds through a unified interface.

When the end user powers on a C2C device
for the first time, it must be provisioned with its respective third-party cloud provider for
managed integrations to obtain its device capabilities and metadata. After completing that provisioning
workflow, managed integrations can communicate with the cloud device and the third-party cloud provider
on behalf of the end user.

###### Note

A hub is not a specific device type as listed above. Its purpose is serving the role as a
controller of smart home devices and facilitating a connection between managed integrations and
third-party cloud providers. It can serve the role as both a device type as listed above and as
a hub.

## Configure encryption key

Security is of paramount importance for data routed between the end user, managed integrations, and
third-party clouds. One of the methods we support to protect your device data is end-to-end
encryption leveraging a secure encryption key for routing your data.

As a customer of managed integrations, you have the following two options for using encryption
keys:

- Use the default managed integrations-managed encryption key.
- Provide an AWS KMS key that you created.

For more information on the AWS KMS service, see [Key management
service (KMS)](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md")

Calling the
[PutDefaultEncryptionConfiguration](../APIReference/API_PutDefaultEncryptionConfiguration.md "../APIReference/API_PutDefaultEncryptionConfiguration.md") API
in the _Managed integrations API Reference Guide_ grants you access to update
which encryption key option you want to use. By default, managed integrations uses the default managed integrations
managed encryption key. You can update your encryption key configuration at any time using the
[PutDefaultEncryptionConfiguration](../APIReference/API_PutDefaultEncryptionConfiguration.md "../APIReference/API_PutDefaultEncryptionConfiguration.md") API.

Additionally, calling the [GetDefaultEncryptionConfiguration](../APIReference/API_GetDefaultEncryptionConfiguration.md "../APIReference/API_GetDefaultEncryptionConfiguration.md") API command
returns information about the encryption configuration for the AWS account in the default or
specified region.

## Onboarding techniques

Listed below are the types of onboarding:

### Direct-connected device

onboarding

See [Provisionee](managedintegrations-sdk-device-provisionee.md "managedintegrations-sdk-device-provisionee.md")
for steps to onboard a direct connected device.

### Hub onboarding

See [Onboard your hubs to managed integrations](managedintegrations-sdk-v2-cookbook-usinghub.md "managedintegrations-sdk-v2-cookbook-usinghub.md")
for steps to onboard the hub.

### Hub-connected device

onboarding

See [Onboard devices and operate them in hub](managedintegrations-sdk-v2-cookbook-onboard-to-hub.md "managedintegrations-sdk-v2-cookbook-onboard-to-hub.md")
for steps to onboard a hub connected device.

### Cloud-to-cloud device onboarding

See [Use a C2C (Cloud-to-Cloud) connector](use-c2c-create-cloud-connector.md "use-c2c-create-cloud-connector.md")
for steps to onboard a cloud device from a third-party cloud vendor to managed integrations.
