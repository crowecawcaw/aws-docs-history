

# Data in transit between local components on SiteWise Edge
<a name="gateway-encryption-in-transit"></a>

SiteWise Edge gateways run on AWS IoT Greengrass, which doesn't encrypt data exchanged locally on the AWS IoT Greengrass core because the data doesn't leave the device. This includes communication between AWS IoT Greengrass components such as the AWS IoT SiteWise connector. For more information, see [Data on the core device](https://docs.aws.amazon.com/greengrass/v1/developerguide/encryption-in-transit.html#data-in-transit-locally) in the *AWS IoT Greengrass Version 1 Developer Guide*.