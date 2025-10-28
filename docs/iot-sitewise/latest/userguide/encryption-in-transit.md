# Data encryption in transit for AWS IoT SiteWise

AWS IoT SiteWise uses encryption in transit to secure the data transmitted between your devices,
gateways, and the AWS Cloud. Communication with AWS IoT SiteWise is encrypted using HTTPS and TLS
1.2, ensuring that your data remains confidential and protected from unauthorized access or
interception.

There are three modes of communication where data is in transit:

- [Over the internet](internet-encryption-in-transit.md "internet-encryption-in-transit.md") –
  Communication between local devices (including SiteWise Edge gateways) and AWS IoT SiteWise is
  encrypted.
- [Over the local network](local-encryption-in-transit.md "local-encryption-in-transit.md") –
  Communication between OpsHub for SiteWise application and SiteWise Edge gateways is always
  encrypted. Communication between the SiteWise monitor application running within your
  browser and SiteWise Edge gateways is always encrypted. Communication between SiteWise Edge gateways and
  OPC UA sources can be encrypted.
- [Between components on SiteWise Edge
  gateways](gateway-encryption-in-transit.md "gateway-encryption-in-transit.md") – Communication between AWS IoT Greengrass components on SiteWise Edge gateways isn't
  encrypted.

###### Topics

- [Data in transit over the internet](internet-encryption-in-transit.md "internet-encryption-in-transit.md")
- [Data in transit over the local network](local-encryption-in-transit.md "local-encryption-in-transit.md")
- [Data in transit between local components on
  SiteWise Edge](gateway-encryption-in-transit.md "gateway-encryption-in-transit.md")
