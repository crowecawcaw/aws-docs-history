

# Amazon VPC in AWS GovCloud (US)
<a name="govcloud-vpc"></a>

Amazon Virtual Private Cloud (Amazon VPC) enables you to launch Amazon Web Services (AWS) resources into a virtual network that you’ve defined. This virtual network closely resembles a traditional network that you’d operate in your own data center, with the benefits of using the scalable infrastructure of AWS.

**Note**  
Not all Amazon VPC endpoints in AWS GovCloud (US) support Amazon VPC endpoint policies.

## Region availability
<a name="_region_availability"></a>

This service is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West) 
+  AWS GovCloud (US-East) 

## How Amazon Virtual Private Cloud differs
<a name="govcloud-vpc-diffs"></a>

The following differences apply to Amazon Virtual Private Cloud:
+ Use SSL (HTTPS) when you make calls to the service in the AWS GovCloud (US) Region. In other AWS Regions, you can use HTTP or HTTPS.
+ Traffic mirror sessions are visible to the owner of a traffic mirror target only if created using the same account. If a traffic mirror target is shared with other accounts, those other accounts can still create sessions with that target, but those sessions are not visible to the target owner.
+ Security group rule IDs are not available in the Amazon VPC console.
+ The AWS-managed prefix list for Amazon CloudFront is not available.
+ Amazon VPC Route Server is not available.

## Documentation
<a name="govcloud-vpc-docs"></a>
+  [Amazon VPC documentation](https://docs.aws.amazon.com/vpc/) 

## Export-controlled content
<a name="itar-boundary-4"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+  Amazon VPC metadata is not permitted to contain export-controlled data. This metadata includes all of the configuration data that you enter when setting up and maintaining your VPCs. This applies to free-text entry fields for VPC resources, including but not limited to:
  + Names and descriptions of security groups and security group rules
  + Keys and values of DHCP option sets
  + Names of destination log groups for VPC Flow Logs
  + Tag keys and values
  + Service names of VPC endpoints
  + Client token values used for the idempotency of API requests