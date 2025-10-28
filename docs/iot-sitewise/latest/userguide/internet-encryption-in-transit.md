# Data in transit over the internet

AWS IoT SiteWise uses Transport Layer Security (TLS) to encrypt all communication over the internet.
All data sent to the AWS Cloud is sent over a TLS connection using MQTT or HTTPS protocols,
so it's secure by default. SiteWise Edge gateways, which run on AWS IoT Greengrass, and property value
notifications use the AWS IoT transport security model. For more information, see [Transport security](../../../iot/latest/developerguide/transport-security.md "../../../iot/latest/developerguide/transport-security.md") in the
_AWS IoT Developer Guide_.
