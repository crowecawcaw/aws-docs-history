# Connect external applications

to the EMQX broker

This guide explains how to connect external applications to your AWS IoT SiteWise Edge
gateway through an EMQX broker on your deployed MQTT-enabled, V3 gateway. External applications
might include custom monitoring tools, third-party visualization software, or legacy
systems that need to interact with your industrial data at the edge.

We'll cover the configuration steps for both Linux and Microsoft
Windows environments, including EMQX deployment configuration, TLS setup
for secure connections, and authorization rules to control access to specific
topics.

###### Note

EMQX is not a vendor or supplier for AWS IoT SiteWise Edge.

###### Important

For securing connections to your gateway, we strongly recommend using
certificate-based authentication through the AWS IoT Greengrass client device authentication
feature. This method provides robust security through mutual TLS (mTLS)
authentication. For more information, see [Connect
client devices to core devices](../../../greengrass/v2/developerguide/connect-client-devices.md "../../../greengrass/v2/developerguide/connect-client-devices.md") in the
_AWS IoT Greengrass Version 2 Developer Guide_.

If you are not able to use certificate based authentication, follow this guide to
setup authentication using usernames and passwords.

## Prerequisites

- A SiteWise Edge MQTT-enabled, V3 gateway that has been deployed and is online
- Access to the gateway host
- Access to the AWS IoT SiteWise and AWS IoT Greengrass consoles

###### Topics

- [Message payload format for the
  EMQX broker on AWS IoT SiteWise Edge](connect-broker-payload-format.md "connect-broker-payload-format.md")
- [Configure the EMQX broker](configure-emqx-broker.md "configure-emqx-broker.md")
- [Connect an application to the EMQX
  broker on AWS IoT SiteWise Edge](connect-app-to-broker.md "connect-app-to-broker.md")
- [Set up authorization rules for
  AWS IoT SiteWise Edge in EMQX](authorization-rules-emqx-broker.md "authorization-rules-emqx-broker.md")
