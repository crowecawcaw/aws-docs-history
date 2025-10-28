# Remote Access

To reduce the need to send people on site in case of a
malfunctioning system, it is recommended to provide a remote
access capability on the device.  When IoT devices are
deployed in the field, remote access provides a way to
troubleshoot, change the configuration, access files such as
logs, and perform other operational tasks even if the device
is behind a firewall or private network. Users can update
devices through its command line interface or access the
device's package manager to add new software via Secure Shell
(SSH) or Remote Desktop Protocol (RDP)

Use
[AWS IoT Secure Tunneling](../../../iot/latest/developerguide/secure-tunneling.md "../../../iot/latest/developerguide/secure-tunneling.md") to establish bidirectional
communication to remote devices over a secure connection that
is managed by AWS IoT.  Secure tunneling does not require
updates to your existing inbound firewall rules, so you can
keep the same security level provided by firewall rules at a
remote site without adding operational overhead

[AWS Systems Manager](../../../systems-manager/latest/userguide/what-is-systems-manager.md "../../../systems-manager/latest/userguide/what-is-systems-manager.md") is another AWS service that you can use
to view and control your edge devices. Systems Manager enables
you to view operational data, automate operation tasks, and
maintain security and compliance through remote device access.

Choose a communication technology that is optimal for your use
case

The communications layer deals with connectivity to a network,
message routing among remote devices, and routing between
devices and the cloud. Communications, whether over a wired or
wireless network, can be a significant consumer of power and
compute for an IoT device. Care must be taken to minimize this
power draw when designing the hardware of a device as well as
the application.  Choose an optimal connectivity type from
options available at the device's operating location to
support data transfer with minimal power, optimal connected
time and minimal retries.
