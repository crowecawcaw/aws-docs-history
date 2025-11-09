# AWS Site-to-Site VPN in AWS GovCloud (US)

AWS Site-to-Site VPN enables you to securely connect your on-premises network or branch office site to your Amazon Virtual Private Cloud (Amazon VPC).

## How Site-to-Site VPN differs for AWS GovCloud (US)

- AWS Site-to-Site VPN integration with Global Accelerator (Accelerated VPN Connections) is not available in the AWS GovCloud (US) Region.
- The AWS Site-to-Site VPN endpoints in AWS GovCloud (US) operate using FIPS 140-3 validated cryptographic modules. Correspondingly, VPN connections created in GovCloud require a different set of algorithms to establish a tunnel. For more information about FIPS 140-3, see "Cryptographic Module Validation Program" on the NIST Computer Security Resource Center website.
- Use SSL (HTTPS) when you make calls to the service in the AWS GovCloud (US) Region. In other AWS Regions, you can use HTTP or HTTPS..

## Documentation for AWS Site-to-Site VPN

[AWS VPN documentation](../../../vpn.md "../../../vpn.md").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- AWS Site-to-Site VPN metadata is not permitted to contain export-controlled data. This metadata includes all of the configuration data that you enter when setting up and maintaining your Site-to-Site VPNs.

For example, do not enter export-controlled data into user input fields such as the following:

    + Display Name
    + Topic Policy
    + Topic Delivery Policy
    + Topic ARN
    + Endpoint
