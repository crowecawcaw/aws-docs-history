# Static and dynamic configuration files for

an AWS Site-to-Site VPN customer gateway device

After you create the VPN connection, you additionally have the option to download an
AWS-provided sample configuration file from the Amazon VPC console, or by using the EC2
API. See [Step 6: Download the configuration file](SetUpVPNConnections.md#vpn-download-config "SetUpVPNConnections.md#vpn-download-config") for
more information. You can also download .zip files of sample configurations specifically for static vs. dynamic routing from those respective pages.

The AWS-provided sample configuration file contains information
specific to your VPN connection which you can use to configure your customer gateway
device. These device-specific configuration files are only available for devices that
AWS has tested. If your specific customer gateway device is not listed, you can download
a generic configuration file to begin with.

###### Important

The configuration file is an example only and might not match your intended Site-to-Site VPN
connection settings entirely. It specifies the minimum requirements for a Site-to-Site VPN
connection of AES128, SHA1, and Diffie-Hellman group 2 in most AWS Regions, and
AES128, SHA2, and Diffie-Hellman group 14 in the AWS GovCloud Regions. It also
specifies pre-shared keys for authentication. You must modify the example
configuration file to take advantage of additional security algorithms,
Diffie-Hellman groups, private certificates, and IPv6 traffic.

###### Note

These device-specific configuration files are provided by AWS on a best-effort
basis. While they have been tested by AWS, this testing is limited. If you are
experiencing an issue with the configuration files, you might need to contact the
specific vendor for additional support.

The following table contains a list of devices which have an example configuration
file available for download that has been updated to support IKEv2. We have introduced
IKEv2 support in the configuration files for many popular customer gateway devices
and will continue to add additional files over time. This list will be updated as more
example configuration files are added.

| Vendor                 | Platform             | Software             |
| ---------------------- | -------------------- | -------------------- |
| Checkpoint             | Gaia                 | R80.10+              |
| Cisco Meraki           | MX Series            | 15.12+ (WebUI)       |
| Cisco Systems, Inc.    | ASA 5500 Series      | ASA 9.7+ VTI         |
| Cisco Systems, Inc.    | CSRv AMI             | IOS 12.4+            |
| Fortinet               | Fortigate 40+ Series | FortiOS 6.4.4+ (GUI) |
| Juniper Networks, Inc. | J-Series Routers     | JunOS 9.5+           |
| Juniper Networks, Inc. | SRX Routers          | JunOS 11.0+          |
| Mikrotik               | RouterOS             | 6.44.3               |
| Palo Alto Networks     | PA Series            | PANOS 7.0+           |
| SonicWall              | NSA, TZ              | OS 6.5               |
| Sophos                 | Sophos Firewall      | v19+                 |
| Strongswan             | Ubuntu 16.04         | Strongswan 5.5.1+    |
| Yamaha                 | RTX Routers          | Rev.10.01.16+        |
