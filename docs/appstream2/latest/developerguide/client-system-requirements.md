# System Requirements and Considerations

The AppStream 2.0 client requires the following:

- Follow the principle of least privilege when launching the AppStream 2.0 client.
  The client should only run with the level of privilege required to complete
  a task.
- Client requirements
  - Windows client
    - Operating system — Windows 10 (32-bit or 64-bit),
      Windows 11 (64-bit)
    - Microsoft Visual C++ 2019 version 14.20.xx Redistributable
      or later. For more information, see the [Latest Microsoft Visual C++ Redistributable
      Version](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170 "https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170") in the Microsoft Support
      documentation.
    - RAM — 2 GB minimum
    - Hard drive space — 200 MB minimum

  - macOS client
    - Operating system — macOS 13 (Ventura), macOS 14
      (Sonoma), macOS 15 (Sequoia)
    - Hard drive space — 200 MB minimum

- Local administrator rights — Used if you want to install the AppStream 2.0
  USB driver for USB driver support.

###### Note

Local administrator rights are not supported for the macOS
client.

- An AppStream 2.0 image that uses the latest AppStream 2.0 agent or agent versions
  published on or after November 14, 2018. For information about AppStream 2.0 agent
  versions, see [AppStream 2.0 Agent Release Notes](agent-software-versions.md "agent-software-versions.md").
- The client supports UDP as well as the default TCP-based streaming over
  NICE DCV. For more information about NICE DCV and UDP, see [Enabling the QUIC UDP transport protocol](../../../dcv/latest/adminguide/enable-quic.md "../../../dcv/latest/adminguide/enable-quic.md"). If you want to enable
  UDP streaming for the client, make sure you meet the following requirements.
  If you don't meet the following requirements, the client will default back
  to TCP-based streaming.
  - Your Stack has been configured to prefer UDP in the
    **Streaming Setting Experience** section.
    For more information, see [Create an Amazon AppStream 2.0 Fleet and Stack](set-up-stacks-fleets.md "set-up-stacks-fleets.md").
  - Your network allows UDP traffic on port 8433 for the AWS IP
    Ranges. For more information, see [AWS IP address
    ranges](../../../general/latest/gr/aws-ip-ranges.md "../../../general/latest/gr/aws-ip-ranges.md").
  - You are using the latest base image when creating your fleet.
    For more information, see [AppStream 2.0 Base Image and Managed Image Update
    Release Notes](base-image-version-history.md "base-image-version-history.md").
  - Your end users are using the latest client. For more information,
    see [Supported
    clients](https://clients.amazonappstream.com/ "https://clients.amazonappstream.com/").

###### Note

We recommend an internet connection for AppStream 2.0 client installation. In some cases, the client
can't be installed on a computer that is not connected to the internet, or USB devices
might not work with applications streamed from AppStream 2.0. For more information, see
[Troubleshooting AppStream 2.0 User Issues](troubleshooting-user-issues.md "troubleshooting-user-issues.md").
