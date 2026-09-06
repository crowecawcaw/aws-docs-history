

# Working with AWS Elemental Link
<a name="feature-elink"></a>

Read this section if your organization uses AWS Elemental Link hardware devices as video sources for inputs with AWS Elemental MediaLive channels. (Your organization might also use AWS Elemental Link hardware devices as video sources for MediaConnect flows. For information about that usage, see [Using Link with a MediaConnect flow](device-use-flow.md).)

AWS Elemental Link is a *hardware device* that connects a live video source, such as a camera or video production equipment, to MediaLive. The AWS Elemental Link hardware device connects to AWS over a secure connection that AWS manages. For information about purchasing AWS Elemental Link, see [Elemental Appliances and Software](https://console.aws.amazon.com/elemental-appliances-software/home#/linkhome).

There are two versions of the device:
+ AWS Elemental Link HD, which can handle HD sources. This is the *HD device*.
+ AWS Elemental Link UHD, which can handle HD and UHD sources. This is the *UHD device*.

For more information about the versions of the devices, see [HD and UHD Link devices](elink-device-hd-uhd.md).

After the hardware device is connected, it automatically appears in MediaLive as a *Link input device*. The *Link input device* is an interface in MediaLive for the external hardware device. In other words, you use the *Link input device* in MediaLive to work with the external hardware device.

After the Link input device exists, you create an *Elemental Link input* that uses that Link input device. You can then use the input as you would use any input—you attach the input to a channel. 

![Flow diagram showing AWS Elemental Link hardware device connecting to Link input device, then to Elemental Link input within MediaLive.](http://docs.aws.amazon.com/medialive/latest/ug/images/link-parts.png)


To clarify the terminology:
+ AWS Elemental Link (AWS Elemental Link) is a *physical hardware device*. 
+ Link input device is the *interface* for AWS Elemental Link in MediaLive. It is the term that you see in the console.
+ Elemental Link input is a *type of input* in MediaLive.

**Topics**
+ [Using AWS Elemental Link for a MediaLive input](elink-using.md)
+ [Using AWS Elemental Link in MediaConnect](elink-using-flow.md)