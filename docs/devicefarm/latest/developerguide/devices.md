# Device support in AWS Device Farm

The following sections provide information about device support in Device Farm.

###### Topics

- [Supported devices](#devices-supported "#devices-supported")
- [Device pools](#devices-pools "#devices-pools")
- [Private devices](#devices-private "#devices-private")
- [Device branding](#devices-branding "#devices-branding")
- [Device slots](#device-slots "#device-slots")
- [Preinstalled device apps](#devices-apps "#devices-apps")
- [Device capabilities](#devices-capabilities "#devices-capabilities")

## Supported devices

Device Farm provides support for hundreds of unique, popular Android and iOS
devices and operating system combinations. The list of available devices grows as new
devices enter the market. For the full list of devices, see [Device List](https://aws.amazon.com/device-farm/device-list/ "https://aws.amazon.com/device-farm/device-list/").

## Device pools

Device Farm organizes its devices into device pools that you can use for your testing. These
device pools contain related devices, such as devices that run only on Android or only
on iOS. Device Farm provides curated device pools, such as those for top devices. You can also
create device pools that mix public and private devices.

## Private devices

Private devices allow you to specify exact hardware and software configurations for your testing needs.
Certain configurations, such as rooted Android devices, can be supported as private devices. Each private
device is a physical device that Device Farm deploys on your behalf in an Amazon data center. Your private devices
are available exclusively to you for both automated and manual testing. After you choose to end your
subscription, the hardware is removed from our environment. For more information, see [Private Devices](https://aws.amazon.com/device-farm/pricing/#privateDevices "https://aws.amazon.com/device-farm/pricing/#privateDevices") and [Private devices in AWS Device Farm](working-with-private-devices.md "working-with-private-devices.md").

## Device branding

Device Farm runs tests on physical mobile and tablet devices from a variety of OEMs.

## Device slots

Device slots correspond to concurrency in which the number of device slots you have
purchased determines how many devices you can run in tests or remote access sessions.

There are two types of device slots:

- A _remote access device slot_ is one you can run in remote
  access sessions concurrently.

If you have one remote access device slot, you can only run one remote access
session at a time. If you purchase additional remote testing device slots, you
can run multiple sessions concurrently.

- An _automated testing device slot_ is one on which you can
  run tests concurrently.

If you have one automated testing device slot, you can only run tests on one
device at a time. If you purchase additional automated testing device slots, you
can run multiple tests concurrently, on multiple devices, to get test results
faster.

You can purchase device slots based on the device family (Android or iOS devices for
automated testing and Android or iOS devices for remote access).

For more information, see [Device Farm
Pricing](https://aws.amazon.com/device-farm/pricing/ "https://aws.amazon.com/device-farm/pricing/").

## Preinstalled device apps

Devices in Device Farm include a small number of apps that are already installed by
manufacturers and carriers.

## Device capabilities

All devices have a Wi-Fi connection to the internet. They do not have carrier
connections and cannot make phone calls or send SMS messages.

You can take photos with any device that supports a front- or rear-facing camera. Due
to the way the devices are mounted, photos might look dark and blurry.

Google Play Services is installed on devices that support it, but these devices do not
have an active Google account.
