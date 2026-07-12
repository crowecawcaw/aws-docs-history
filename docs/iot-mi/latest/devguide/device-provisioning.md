# Device provisioning

Device provisioning facilitates the device onboarding process, oversees the entire
device lifecycle, and establishes a centralized repository for device information that is
accessible to other aspects of Managed Integrations. Managed Integrations provides a unified interface for managing
various device types, accommodating first-party customer devices directly connected through a
device software development kit (SDK) or commercial-off-the-shelf (COTS) devices indirectly
linked via a hub device.

Each device, regardless of the device type, in Managed Integrations has a globally unique identifier
called a `managedThingId`. This identifier is used in the onboarding and management of the
device for the entire device lifecycle. It is fully managed by Managed Integrations and unique to that
specific device across all of Managed Integrations in all AWS Regions. When a device is initially added to
Managed Integrations, this identifier is created and attached to the managed thing in Managed Integrations.
A managed thing is a digital representation of the physical device within Managed Integrations
to mirror all device metadata of the physical device. For third-party devices, they may have
their own, separate unique identifier specific to their third-party cloud in addition to the
`managedThingId` stored in Managed Integrations representing the physical device.

Devices being provisioned can have different statuses depending on what stage of the
onboarding flow they are in. The following list describes each provisioning status:

- ACTIVATED: The device has been found and command and control is available.
- DISCOVERED: The device has been found but command and control is not yet available.
- UNASSOCIATED: The managed thing has been created but requires further actions to be discovered. It is not reachable from the AWS Cloud or AWS IoT Managed Integrations controllers (hubs)
- PRE\_ASSOCIATED: The managed thing has been created and is ready for automatic discovery once powered on or connected. It is not reachable from the AWS Cloud or
  AWS IoT Managed Integrations controllers (hubs).
- DELETE\_IN\_PROGRESS: Asynchronous deletion process started.
- DELETED: The device has been deleted from the AWS Cloud.
- ISOLATED: A previously discovered or activated managed thing that is no longer reachable. For example, a device for a third-party cloud whose connector associations have all been deleted.

The following onboarding flow is for provisioning your hub with
Managed Integrations:

[Onboard your hubs to Managed Integrations](managedintegrations-sdk-v2-cookbook-usinghub.md "managedintegrations-sdk-v2-cookbook-usinghub.md"): Setup core provisioner and protocol-specific plugins that work together to handle device authentication, communication, and setup.

The following onboarding flows are provided for provisioning your hub connected devices with
Managed Integrations:

- [Simple setup (SS)](managedintegrations-sdk-v2-device-onboarding.md#managedintegrations-sdk-v2-onboarding-ssflow "managedintegrations-sdk-v2-device-onboarding.md#managedintegrations-sdk-v2-onboarding-ssflow"): The end user powers on the IoT device and scans its QR code using the
  device manufacturer application. The device is then enrolled onto the Managed Integrations cloud and
  connects to the IoT hub.
- [Zero-touch setup (ZTS)](managedintegrations-sdk-v2-device-onboarding.md#managedintegrations-sdk-v2-onboarding-zerotouch-flow "managedintegrations-sdk-v2-device-onboarding.md#managedintegrations-sdk-v2-onboarding-zerotouch-flow"): The device is pre-associated upstream in the supply chain. For example,
  instead of end-users scanning the device QR code, this step is completed earlier to pre-link the device to the customer accounts.
- [User guided setup (UGS)](managedintegrations-sdk-v2-device-onboarding.md#managedintegrations-sdk-v2-onboarding-ugsflow "managedintegrations-sdk-v2-device-onboarding.md#managedintegrations-sdk-v2-onboarding-ugsflow"): The end user powers on the device and follows interactive steps
  to onboard it to Managed Integrations. This might include pressing a button on the IoT hub, using a device
  manufacturer app, or pressing buttons on both the hub and device. You can use this method if
  Simple setup fails.

###### Note

The device provisioning workflow in Managed Integrations is agnostic of the onboarding requirements
for a device. Managed Integrations provides a streamlined user interface for onboarding and managing a
device, regardless of the device type or device protocol.
