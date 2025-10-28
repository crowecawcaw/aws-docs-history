# Working with AWS Elemental Link

Read this section if your organization uses AWS Elemental Link hardware devices as video sources for
inputs with AWS Elemental MediaLive channels. (Your organization might also use AWS Elemental Link hardware devices as
video sources for MediaConnect flows. For information about that usage, see [Using Link with a MediaConnect flow](device-use-flow.md "device-use-flow.md").)

AWS Elemental Link is a _hardware device_ that connects a live
video source, such as a camera or video production equipment, to MediaLive. The AWS Elemental Link hardware
device connects to AWS over a secure connection that AWS manages. For information about
purchasing AWS Elemental Link, see [Elemental Appliances and
Software](https://console.aws.amazon.com/elemental-appliances-software/home#/linkhome "https://console.aws.amazon.com/elemental-appliances-software/home#/linkhome").

There are two versions of the device:

- AWS Elemental Link HD, which can handle HD sources. This is the _HD
  device_.
- AWS Elemental Link UHD, which can handle HD and UHD sources. This is the _UHD
  device_.
  For more information about the versions of the devices, see [HD and UHD Link devices](elink-device-hd-uhd.md "elink-device-hd-uhd.md").

After the hardware device is connected, it automatically appears in MediaLive as a _Link input device_. The _Link input
device_ is an interface in MediaLive for the external hardware device. In other words,
you use the _Link input device_ in MediaLive to work with the
external hardware device.

After the Link input device exists, you create an _Elemental
Link input_ that uses that Link input device. You can then use the input as
you would use any input—you attach the input to a channel.

![Diagram showing AWS Elemental Link hardware device connecting to MediaLive's Link input device and Elemental Link input.](/images/medialive/latest/ug/images\link-parts.png)
To clarify the terminology:

- AWS Elemental Link (AWS Elemental Link) is a _physical hardware device_.
- Link input device is the _interface_ for AWS Elemental Link
  in MediaLive. It is the term that you see in the console.
- Elemental Link input is a _type of input_ in MediaLive.

###### Topics

- [Using AWS Elemental Link for a MediaLive input](elink-using.md "elink-using.md")
- [Using AWS Elemental Link in MediaConnect](elink-using-flow.md "elink-using-flow.md")
