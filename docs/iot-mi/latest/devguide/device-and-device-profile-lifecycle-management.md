# Device and device profile

lifecycle

Managing the lifecycle of your devices and device profiles ensures your fleet of devices are
secure and running efficiently.

###### Topics

- [Device](#device "#device")
- [Device profile](#device-profile "#device-profile")

## Device

During initial onboarding, managed integrations creates a digital twin of your physical device called a _Managed Thing_. The Managed Thing has a `managedThingID` that provides a global
unique identifier to identify the device in managed integrations across all regions. The device pairs with
the local hub during provisioning for real-time communication with managed integrations or a third-party
cloud for third-party devices. A device is also associated with an owner as identified by the
`owner` parameter in the public APIs for a Managed Thing such as
`GetManagedThing`. The device is linked to the corresponding device profile based on
the type of device.

###### Note

A physical device may have multiple records if it is provisioned multiple times under
different customers.

The device lifecycle starts with the creation of the Managed Thing in managed integrations
using the `CreateManagedThing` API and ends when the customer deletes the
Managed Thing using the `DeleteManagedThing` API. The lifecycle of a
device is managed by the following public APIs:

- `CreateManagedThing`
- `ListManagedThings`
- `GetManagedThing`
- `UpdateManagedThing`
- `DeleteManagedThing`

## Device profile

A device profile represents a specific type of device such as a light bulb or doorbell. It
is associated with a manufacturer and contains the capabilities of the device. The device profile
stores the authentication materials needed for device connectivity setup requests with managed integrations.
The authentication materials used are the device bar code.

During the device manufacturing process, the manufacturer can register their device profiles
with managed integrations. This enables the manufacturer to obtain the necessary materials for the devices
from managed integrations during the onboarding and provisioning workflows. The metadata from the device
profile is stored on the physical device or printed on the device labeling. The lifecycle of the
device profile ends when the manufacturer deletes it in managed integrations.
