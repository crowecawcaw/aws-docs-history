

# Data in transit over the internet
<a name="internet-encryption-in-transit"></a>

AWS IoT SiteWise uses Transport Layer Security (TLS) to encrypt all communication over the internet. All data sent to the AWS Cloud is sent over a TLS connection using MQTT or HTTPS protocols, so it's secure by default. SiteWise Edge gateways, which run on AWS IoT Greengrass, and property value notifications use the AWS IoT transport security model. For more information, see [Transport security](https://docs.aws.amazon.com/iot/latest/developerguide/transport-security.html) in the *AWS IoT Developer Guide*.