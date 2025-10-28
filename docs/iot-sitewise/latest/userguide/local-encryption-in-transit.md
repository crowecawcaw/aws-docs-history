# Data in transit over the local network

SiteWise Edge gateways follow OPC UA specifications for communication with local OPC UA sources.
It's your responsibility to configure your sources to use a message security mode that
encrypts data in transit.

If you choose a _sign_ message security mode, data in
transit between SiteWise Edge gateways and sources is signed but not encrypted. If you choose a
_sign and encrypt_ message security mode, the data in transit between
SiteWise Edge gateways and sources is signed and encrypted. For more information about configuring
sources, see [Add data sources to your AWS IoT SiteWise Edge gateway](add-data-sources.md "add-data-sources.md").

The communication between the edge console application and SiteWise Edge gateways is always
encrypted by TLS. The SiteWise Edge connector on the SiteWise Edge gateway generates and stores a
self-signed certificate to be able to establish a TLS connection with the edge console for
AWS IoT SiteWise application. You will need to copy this certificate from your SiteWise Edge gateway to the
edge console for AWS IoT SiteWise application before you connect the application to the SiteWise Edge gateway.
This ensures that the edge console for AWS IoT SiteWise application is able to verify that it has
connected to your trusted SiteWise Edge gateway.

In addition to TLS for secrecy and server authenticity, SiteWise Edge uses the SigV4 protocol
to establish the authenticity of the edge console application. The SiteWise Edge connector on the
SiteWise Edge gateway accepts and stores a password to be able to verify incoming connections from
the edge console application, SiteWise Monitor application running within browsers, and other clients
based on the AWS IoT SiteWise SDK.

For more information about generating the password and server
certificate, see [Manage SiteWise Edge gateways](manage-gateways-ggv2.md "manage-gateways-ggv2.md").
