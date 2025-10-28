# Data in transit between local components on

SiteWise Edge

SiteWise Edge gateways run on AWS IoT Greengrass, which doesn't encrypt data exchanged locally on the AWS IoT Greengrass
core because the data doesn't leave the device. This includes communication between AWS IoT Greengrass
components such as the AWS IoT SiteWise connector. For more information, see [Data on the core
device](../../../greengrass/v1/developerguide/encryption-in-transit.md#data-in-transit-locally "../../../greengrass/v1/developerguide/encryption-in-transit.md#data-in-transit-locally") in the _AWS IoT Greengrass Version 1 Developer Guide_.
