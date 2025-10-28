# Networking in AWS Control Tower

AWS Control Tower provides basic support for networking through VPCs.

If the default configuration or capabilities of the AWS Control Tower VPC do not meet your needs,
you can use other AWS services to configure your VPC. For more information about how to
work with VPCs and AWS Control Tower, see [Building a Scalable and Secure Multi-VPC AWS Network Infrastructure](https://d1.awsstatic.com/whitepapers/building-a-scalable-and-secure-multi-vpc-aws-network-infrastructure.pdf "https://d1.awsstatic.com/whitepapers/building-a-scalable-and-secure-multi-vpc-aws-network-infrastructure.pdf").

AWS Control Tower supports IPv4 and IPv6 protocols, through dual-stack IP addresses. For more
information, see [AWS Control Catalog endpoints and quotas](../../../general/latest/gr/controlcatalog.md "../../../general/latest/gr/controlcatalog.md") and [AWS Control Tower endpoints and quotas](../../../general/latest/gr/controltower.md "../../../general/latest/gr/controltower.md").

###### Related topics

- For information about how AWS Control Tower works when you enroll accounts that have
  existing VPCs, see [Enroll existing accounts with
  VPCs](enroll-account.md#enroll-existing-accounts-with-vpcs "enroll-account.md#enroll-existing-accounts-with-vpcs").
- With Account Factory, you can provision accounts that include an AWS Control Tower VPC, or you
  can provision accounts without a VPC. For information about how to delete the
  AWS Control Tower VPC or configure AWS Control Tower accounts without a VPC, see [Walkthrough: Configure AWS Control Tower Without a
  VPC](configure-without-vpc.md "configure-without-vpc.md").
- For information about how to change account settings for VPCs, see the [Account Factory documentation](account-factory.md#configuring-account-factory-with-VPC-settings "account-factory.md#configuring-account-factory-with-VPC-settings") on updating an account.
- For more information about working with networking and VPCs in AWS Control Tower, see the
  section about [Networking](related-information.md#networking "related-information.md#networking") on the _Related
  information_ page of this _User
  Guide_.

## VPCs and AWS Regions in AWS Control Tower

As a standard part of account creation, AWS creates an AWS-default VPC in every
Region, even the Regions you are not governing with AWS Control Tower. This default VPC is not
the same as a VPC that AWS Control Tower creates for a provisioned account, but the AWS default
VPC in a non-governed Region may be accessible to IAM users.

Adminstrators can enable the Region deny control, so that your end-users do not have
permission to connect to a VPC in _a Region that's supported by
AWS Control Tower_ but outside your governed Regions. To configure the Region deny
control, go to the **Landing zone settings** page and select
**Modify settings**.

The Region deny control blocks API calls to most services in non-governed
AWS Regions. For more information, see [Deny access to
AWS based on the requested AWS Region.](primary-region-deny-policy.md "primary-region-deny-policy.md").

###### Note

The Region deny control may not prevent IAM users from connecting to an AWS
default VPC in a Region where AWS Control Tower is not supported.

Optionally, you can remove the AWS default VPCs in non-governed Regions. To list the
default VPC in a Region you can use a CLI command similar to this example:

```
aws ec2 --region us-west-1 describe-vpcs --filter Name=isDefault,Values=true
```
