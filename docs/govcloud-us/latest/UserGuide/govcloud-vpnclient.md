# AWS Client VPN in AWS GovCloud (US)

AWS Client VPN is a managed client-based AWS VPN service that enables you to securely access AWS resources and resources in your on-premises network. With AWS Client VPN, you can access your resources from any location using an OpenVPN-based VPN client.

## How Client VPN Differs for AWS GovCloud (US)

- AWS Client VPN endpoints in AWS GovCloud (US) operate using FIPS 140-3 validated cryptographic modules. AWS VPN connections created in AWS GovCloud (US) might require a different set of algorithms to establish a tunnel, depending on your client configuration. For more information about FIPS 140-3, see "Cryptographic Module Validation Program" on the NIST Computer Security Resource Center website.
- Use SSL (HTTPS) when you make calls to the service in the AWS GovCloud (US) Region. In other AWS Regions, you can use HTTP or HTTPS.

## Documentation for AWS Client VPN

[AWS Client VPN documentation](../../../vpn.md "../../../vpn.md").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- AWS Client VPN metadata is not permitted to contain export-controlled data. This metadata includes all of the configuration data that you enter when setting up and maintaining your Client VPN Endpoints.

For example, do not enter export-controlled data into user input fields such as the following:

    + Display Name
    + Topic Policy
    + Topic Delivery Policy
    + Topic ARN
    + Endpoint
