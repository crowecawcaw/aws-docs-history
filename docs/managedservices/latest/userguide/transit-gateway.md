# Use AMS SSP to provision AWS Transit Gateway in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access AWS Transit Gateway capabilities directly in your AMS managed account. AWS Transit Gateway is a service that enables you to connect your Amazon Virtual Private Cloud (VPCs) and your
on-premises networks to a single gateway.
As you grow the number of workloads running on AWS, you need to be able to scale your networks across multiple accounts and
Amazon VPCs to keep up with the growth.
Today, you can connect pairs of Amazon VPCs using peering. However, managing point-to-point connectivity across many Amazon
VPCs, without the ability to centrally
manage the connectivity policies, can be operationally costly and cumbersome. For on-premises connectivity, you need to
attach your AWS VPN to each individual Amazon VPC.
This solution can be time consuming to build and hard to manage when the number of VPCs grows into the hundreds.
To learn more, see [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/ "https://aws.amazon.com/transit-gateway/").

## AWS Transit Gateway in AWS Managed Services FAQ

Common questions and answers:

**Q: How do I request access to AWS Transit Gateway in my AMS account?**

Request access to AWS Transit Gateway by submitting an RFC with the Management | AWS service | Self-provisioned service | Add change type (ct-1w8z66n899dct).
This RFC provisions the following IAM role to your account: `customer_tgw_console_role`.
Once provisioned in your account, you must onboard the role in your federation solution.

**Q: What are the restrictions to using AWS Transit Gateway in my AMS account?**

Full functionality of AWS Transit Gateway is available in your AMS single-account landing zone account for the exception of
route table modifications for Transit Gateway routing. Request route table changes by submitting
a Management | Other | Other | Create change type (ct-1e1xtak34nx76).

###### Note

This service is only supported for single-account landing zone (SALZ), not multi-account landing zone (MALZ).

**Q: What are the prerequisites or dependencies to using AWS Transit Gateway in my AMS
account?**

There are no prerequisites or dependencies to use AWS Transit Gateway in your AMS account.
