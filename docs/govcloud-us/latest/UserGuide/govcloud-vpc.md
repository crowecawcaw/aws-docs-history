# Amazon VPC in AWS GovCloud (US)

Amazon Virtual Private Cloud (Amazon VPC) enables you to launch Amazon Web Services (AWS) resources into a virtual network that you've defined. This virtual network closely resembles a traditional network that you'd operate in your own data center, with the benefits of using the scalable infrastructure of AWS.

###### Note

Not all Amazon VPC endpoints in AWS GovCloud (US) support Amazon VPC endpoint policies.

## How Amazon Virtual Private Cloud differs for AWS GovCloud (US)

- Use SSL (HTTPS) when you make calls to the service in the AWS GovCloud (US) Region. In other AWS Regions, you can use HTTP or HTTPS.
- Traffic mirror sessions are visible to the owner of a traffic mirror target only if created using the same account.
  If a traffic mirror target is shared with other accounts, those other accounts can still create sessions with that
  target, but those sessions are not visible to the target owner.
- Security group rule IDs are not available in the Amazon VPC console.
- The AWS-managed prefix list for Amazon CloudFront is not available.
- Reachability Analyzer is not supported.
- Network Access Analyzer is not supported.
- Amazon VPC Route Server is not supported.

## Documentation for Amazon Virtual Private Cloud

[Amazon VPC documentation](../../../vpc.md "../../../vpc.md")

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains
how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings.
The list can be used as a guide to help meet applicable customer compliance obligations.
Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Amazon VPC metadata is not permitted to contain export-controlled data. This metadata includes
  all of the configuration data that you enter when setting up and maintaining your VPCs. This
  applies to free-text entry fields for VPC resources, including but not limited to:
  - Names and descriptions of security groups and security group rules
  - Keys and values of DHCP option sets
  - Names of destination log groups for VPC Flow Logs
  - Tag keys and values
  - Service names of VPC endpoints
  - Client token values used for the idempotency of API requests
