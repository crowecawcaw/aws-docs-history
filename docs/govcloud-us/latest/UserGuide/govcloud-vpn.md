

# AWS Site-to-Site VPN in AWS GovCloud (US)
<a name="govcloud-vpn"></a>

AWS Site-to-Site VPN enables you to securely connect your on-premises network or branch office site to your Amazon Virtual Private Cloud (Amazon VPC).

## Region availability
<a name="_region_availability"></a>

This service is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West) 
+  AWS GovCloud (US-East) 

## How Site-to-Site VPN differs
<a name="govcloud-vpn-diffs"></a>

The following differences apply to Site-to-Site VPN:
+  AWS Site-to-Site VPN integration with Global Accelerator (Accelerated VPN Connections) is not available in the AWS GovCloud (US) Region.
+ The AWS Site-to-Site VPN endpoints in AWS GovCloud (US) operate using FIPS 140-3 validated cryptographic modules. Correspondingly, VPN connections created in GovCloud require a different set of algorithms to establish a tunnel. For more information about FIPS 140-3, see "Cryptographic Module Validation Program" on the NIST Computer Security Resource Center website.
+ Use SSL (HTTPS) when you make calls to the service in the AWS GovCloud (US) Region. In other AWS Regions, you can use HTTP or HTTPS..

## Documentation
<a name="govcloud-vpn-docs"></a>
+  [Site-to-Site VPN documentation](https://docs.aws.amazon.com/vpn) 

## Export-controlled content
<a name="itar-boundary-2"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+  AWS Site-to-Site VPN metadata is not permitted to contain export-controlled data. This metadata includes all of the configuration data that you enter when setting up and maintaining your Site-to-Site VPNs.

  For example, do not enter export-controlled data into user input fields such as the following:
  + Display Name
  + Topic Policy
  + Topic Delivery Policy
  + Topic ARN
  + Endpoint