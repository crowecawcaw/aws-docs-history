# Administrative tips for landing zone setup

Here are some tips for setting up and configuring your landing zone.

- The AWS Region where you do the most work should be your home Region.
- Set up your landing zone and deploy your Account Factory accounts from within your home
  Region.
- If you’re investing in several AWS Regions, be sure that your cloud resources are in the
  Region where you’ll do most of your cloud administrative work and run your workloads.
- By keeping your workloads and logs in the same AWS Region, you reduce the cost that would
  be associated with moving and retrieving log information across regions.
- The audit and other Amazon S3 buckets are created in the same AWS Region from which you
  launch AWS Control Tower. We recommend that you do not move these buckets.
- You can make your own log buckets in the Log Archive account, but it is not recommended.
  Be sure to leave the buckets created by AWS Control Tower.
- Your Amazon S3 access logs must be in
  the same AWS Region as the source buckets.
- When launching, AWS Security Token Service (STS) endpoints must be activated in the
  management account, for all Regions supported by AWS Control Tower. Otherwise, the launch may fail midway
  through the configuration process.
- _AWS Control Tower supports tagging for enabled controls only._ For more information, see [AWS Control Tower control tagging APIs](2023-all.md#control-tagging-apis "2023-all.md#control-tagging-apis").
- We recommend enabling multi-factor authentication (MFA) for every account that AWS Control Tower
  manages.
- Alternatively, you can use the AWS Root Access Management feature, which allows root actions to be performed on member accounts, and removes the need to enable MFA for every account. For more information, see [Centrally managing root access for customers using AWS Organizations](https://aws.amazon.com/blogs/aws/centrally-managing-root-access-for-customers-using-aws-organizations/ "https://aws.amazon.com/blogs/aws/centrally-managing-root-access-for-customers-using-aws-organizations/").

###### Considerations about VPCs

- The VPC created by AWS Control Tower is limited to the AWS Regions in which AWS Control Tower is
  available. Some customers whose workloads run in non-supported Regions may want to disable the
  VPC that is created with your Account Factory account. They may prefer to create a new VPC using the
  Service Catalog portfolio, or to create a custom VPC that runs only in the required Regions.
- The VPC created by AWS Control Tower is not the same as the default VPC that is created for all
  AWS accounts. In Regions where AWS Control Tower is supported, AWS Control Tower deletes the default VPC when
  it creates the AWS Control Tower VPC.
- If you delete your default VPC in your home AWS Region, it's best to delete it in all
  other AWS Regions.
