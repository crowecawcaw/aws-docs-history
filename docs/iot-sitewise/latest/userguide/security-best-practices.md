# Security best practices for AWS IoT SiteWise

This topic contains security best practices for AWS IoT SiteWise.

## Use authentication credentials

on your OPC UA servers

Require authentication credentials to connect to your OPC UA servers. Consult the
documentation for your servers to do so. Then, to allow your SiteWise Edge gateway to connect to
your OPC UA servers, add server authentication secrets to your SiteWise Edge gateway. For more
information, see [Configure data source
authentication for SiteWise Edge](configure-source-authentication-ggv2.md "configure-source-authentication-ggv2.md").

## Use encrypted communication modes

for your OPC UA servers

Choose a non-deprecated, encrypted message security mode when you
configure your OPC UA sources for your SiteWise Edge gateway. This helps secure your industrial data
as it moves from your OPC UA servers to the SiteWise Edge gateway. For more information, see [Data in transit over the local network](local-encryption-in-transit.md "local-encryption-in-transit.md") and
[Set up an OPC UA source in
SiteWise Edge](configure-opcua-source.md "configure-opcua-source.md").

## Keep your components up to

date

If you use SiteWise Edge gateways to ingest data to the service, it's your responsibility to
conﬁgure and maintain your SiteWise Edge gateway's environment. This responsibility includes
upgrading to the latest versions of the gateway's system software, AWS IoT Greengrass software, and
connectors.

###### Note

The AWS IoT SiteWise Edge connector stores secrets on your file system. These secrets control who
can view the data cached within your SiteWise Edge gateway. It's strongly recommended that you
turn on disk or file-system encryption for the system running your SiteWise Edge gateway.

For information on how to upgrade components in the AWS IoT SiteWise console, see [Change the version of SiteWise Edge gateway
component packs](manage-gateways-ggv2.md#manage-gateway-update-packs "manage-gateways-ggv2.md#manage-gateway-update-packs").

## Encrypt your SiteWise Edge gateway's

file system

Encrypt and secure your SiteWise Edge gateway, so your industrial data is secure as it moves
through the SiteWise Edge gateway. If your SiteWise Edge gateway has a hardware security module, you can
configure AWS IoT Greengrass to secure your SiteWise Edge gateway. For more information, see [Hardware security integration](../../../greengrass/v1/developerguide/hardware-security.md "../../../greengrass/v1/developerguide/hardware-security.md") in the
_AWS IoT Greengrass Version 1 Developer Guide_. Otherwise, consult the documentation for your operating
system to learn how to encrypt and secure your file system.

## Secure access to your edge

configuration

Don't share your edge console application password or your SiteWise Monitor application password.
Don't put this password in places where anyone can see them. Implement a healthy password
rotation policy by configuring an appropriate expiration for your password.

## Securing data on Siemens

Industrial Edge Management

The device data you choose to share with AWS IoT SiteWise Edge is determined in your Siemens
IEM Databus configuration topics. By electing topics to share with SiteWise Edge, you are
sharing topic-level data with AWS IoT SiteWise. The Siemens Industrial Edge Marketplace
is an independent marketplace, separate from AWS. To protect your shared data, the SiteWise Edge
application will not run unless you utilize Siemens Secured Storage. For more
information, see [Secure Storage](https://docs.eu1.edge.siemens.cloud/build_a_device/device_building/development/development/secure-storage.html "https://docs.eu1.edge.siemens.cloud/build_a_device/device_building/development/development/secure-storage.html"), in Siemens documentation.

## Grant SiteWise Monitor users

minimum possible permissions

Follow the principle of least privilege by using the minimum set of access policy
permissions for your portal users.

- When you create a portal, define a role that allows the minimum set of assets needed
  for that portal. For more information, see [Use service roles for AWS IoT SiteWise Monitor](monitor-service-role.md "monitor-service-role.md").
- When you and your portal administrators create and share projects, use the minimum set
  of assets needed for that project.
- When an identity no longer needs access to a portal or project, remove them from that
  resource. If that identity is no longer applicable to your organization, delete that
  identity from your identity store.

The least principle best practice also applies to IAM roles. For more information, see
[Policy best
practices](security_iam_id-based-policy-examples.md#security_iam_service-with-iam-policy-best-practices "security_iam_id-based-policy-examples.md#security_iam_service-with-iam-policy-best-practices").

## Don't expose sensitive

information

You should prevent the logging of credentials and other sensitive information, such as
personally identifiable information (PII). We recommend that you implement the following
safeguards even though access to local logs on a SiteWise Edge gateway requires root privileges and
access to CloudWatch Logs requires IAM permissions.

- Don't use sensitive information in names, descriptions, or properties of your assets
  or models.
- Don't use sensitive information in SiteWise Edge gateway or source names.
- Don't use sensitive information in names or descriptions of your portals, projects, or
  dashboards.

## Follow AWS IoT Greengrass security best

practices

Follow AWS IoT Greengrass security best practices for your SiteWise Edge gateway. For more information, see
[Security best practices](../../../greengrass/v1/developerguide/security-best-practices.md "../../../greengrass/v1/developerguide/security-best-practices.md") in the
_AWS IoT Greengrass Version 1 Developer Guide_.

## See also

- [Security best practices](../../../iot/latest/developerguide/security-best-practices.md "../../../iot/latest/developerguide/security-best-practices.md")
  in the _AWS IoT Developer Guide_
- [Ten
  security golden rules for Industrial IoT solutions](https://aws.amazon.com/blogs/iot/ten-security-golden-rules-for-industrial-iot-solutions/ "https://aws.amazon.com/blogs/iot/ten-security-golden-rules-for-industrial-iot-solutions/")
