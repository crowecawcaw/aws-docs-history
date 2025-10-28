# Device provisioning

Device provisioning facilitates the device onboarding process, oversees the entire
device lifecycle, and establishes a centralized repository for device information that is
accessible to other aspects of managed integrations. Managed integrations provides a unified interface for managing
various device types, accommodating first-party customer devices directly connected through a
device software development kit (SDK) or commercial-off-the-shelf (COTS) devices indirectly
linked via a hub device.

Each device, regardless of the device type, in managed integrations has a globally unique identifier
called a `managedThingId`. This identifier is used in the onboarding and management of the
device for the entire device lifecycle. It is fully managed by managed integrations and unique to that
specific device across all of managed integrations in all AWS Regions. When a device is initially added to
managed integrations, this identifier is created and attached to the managed thing in managed integrations.
A managed thing is a digital representation of the physical device within managed integrations
to mirror all device metadata of the physical device. For third-party devices, they may have
their own, separate unique identifier specific to their third-party cloud in addition to the
`managedThingId` stored in managed integrations representing the physical device.

Devices being provisioned can have different statuses depending on what stage of the
onboarding flow they are in. The following list describes each provisioning status:

- ACTIVATED: The device has been found and command and control is available.
- DISCOVERED: The device has been found but command and control is not yet available.
- UNASSOCIATED: The managed thing has been created but requires further actions to be discovered. It is not reachable from the AWS Cloud or AWS IoT Managed integrations controllers (hubs)
- PRE_ASSOCIATED: The managed thing has been created and is ready for automatic discovery once powered on or connected. It is not reachable from the AWS Cloud or
  AWS IoT Managed integrations controllers (hubs).
- DELETE_IN_PROGRESS: Asynchronous deletion process started.
- DELETED: The device has been deleted from the AWS Cloud.
- ISOLATED: A previously discovered or activated managed thing that is no longer reachable. For example, a device for a third-party cloud whose connector associations have all been deleted.

The following onboarding flow is for provisioning your hub with
managed integrations:

[Onboard your hubs to managed integrations](managedintegrations-sdk-v2-cookbook-usinghub.md "managedintegrations-sdk-v2-cookbook-usinghub.md"): Setup core provisioner and protocol-specific plugins that work together to handle device authentication, communication, and setup.

The following onboarding flows are provided for provisioning your hub connected devices with
managed integrations:

- [Simple setup (SS)](managedintegrations-sdk-v2-device-onboarding.md#managedintegrations-sdk-v2-onboarding-ssflow "managedintegrations-sdk-v2-device-onboarding.md#managedintegrations-sdk-v2-onboarding-ssflow"): The end user powers on the IoT device and scans its QR code using the
  device manufacturer application. The device is then enrolled onto the managed integrations cloud and
  connects to the IoT hub.
- [Zero-touch setup (ZTS)](managedintegrations-sdk-v2-device-onboarding.md#managedintegrations-sdk-v2-onboarding-zerotouch-flow "managedintegrations-sdk-v2-device-onboarding.md#managedintegrations-sdk-v2-onboarding-zerotouch-flow"): The device is pre-associated upstream in the supply chain. For example,
  instead of end-users scanning the device QR code, this step is completed earlier to pre-link the device to the customer accounts.
- [User guided setup
  (UGS)](managedintegrations-sdk-v2-device-onboarding.md#managedintegrations-sdk-v2-onboarding-ugsflow "managedintegrations-sdk-v2-device-onboarding.md#managedintegrations-sdk-v2-onboarding-ugsflow"): The end user powers on the device and follows interactive steps
  to onboard it to managed integrations. This might include pressing a button on the IoT hub, using a device
  manufacturer app, or pressing buttons on both the hub and device. You can use this method if
  Simple setup fails.

###### Note

The device provisioning workflow in managed integrations is agnostic of the onboarding requirements
for a device. Managed integrations provides a streamlined user interface for onboarding and managing a
device, regardless of the device type or device protocol.
