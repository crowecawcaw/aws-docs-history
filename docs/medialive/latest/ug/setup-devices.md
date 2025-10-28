# Setting up AWS Elemental Link

If your organization uses AWS Elemental Link devices with AWS Elemental MediaLive or AWS Elemental MediaConnect, you must deploy
the device and configure the device.

AWS Elemental Link (Link ) is a _hardware device_ that
connects a live video source, such as a camera or video production equipment, to MediaLive. The
Link device connects to AWS over a secure connection that AWS manages.

Your organization might use Link in one or both of these ways:

- As the video source for the input that you attach to an AWS Elemental MediaLive channel. For more
  information about this input, see [Setting up an Elemental Link input](input-create-link-device.md "input-create-link-device.md").
- As the video source for an AWS Elemental MediaConnect flow. Only AWS Elemental Link UHD supports this usage. For
  more information about this input, see [Creating a transport stream flow
  that uses a standard source](../../../mediaconnect/latest/ug/flows-create-standard-source.md "../../../mediaconnect/latest/ug/flows-create-standard-source.md") in the AWS Elemental MediaConnect user guide.
  You must perform preliminary setup tasks so that you can use the Link device. Then to
  use the device, you must configure it to be used in a MediaLive or a MediaConnect workflow.

###### Topics

- [HD and UHD Link devices](elink-device-hd-uhd.md "elink-device-hd-uhd.md")
- [Deploying the Link hardware](elink-setup-device.md "elink-setup-device.md")
- [Using Link with a MediaLive input](device-use-input.md "device-use-input.md")
- [Using Link with a MediaConnect flow](device-use-flow.md "device-use-flow.md")
- [Managing Link devices](device-manage.md "device-manage.md")
