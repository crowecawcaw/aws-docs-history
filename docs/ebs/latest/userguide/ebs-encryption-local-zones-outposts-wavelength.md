

# Amazon EBS encryption in Local Zones, Outposts, and Wavelength Zones
<a name="ebs-encryption-local-zones-outposts-wavelength"></a>

Amazon EBS encryption behavior varies depending on the type of location where you create your resources.

## Local Zones
<a name="ebs-encryption-local-zones"></a>

In the following Local Zones, all Amazon EBS resources are encrypted by default. You can't create unencrypted volumes or snapshots. If you don't specify a KMS key, Amazon EBS encrypts your resources with your account's default encryption key. By default, this is the AWS managed key (`aws/ebs`). To change the default encryption key for your account, see [Default encryption key](encryption-by-default.md#ebs-default-encryption-key).
+ North America: `us-east-1-atl-1a`, `us-east-1-bos-1a`, `us-east-1-chi-1a`, `us-east-1-dfw-1a`, `us-east-1-iah-1a`, `us-east-1-mci-1a`, `us-east-1-mia-1a`, `us-east-1-msp-1a`, `us-east-1-nyc-1a`, `us-east-1-phl-1a`, `us-east-1-qro-1a`, `us-east-2-mci-1a`, `us-east-2-mci-1b`, `us-west-2-den-1a`, `us-west-2-hnl-1a`, `us-west-2-las-1a`, `us-west-2-las-1b`, `us-west-2-pdx-1a`, `us-west-2-phx-1a`, `us-west-2-sea-1a`
+ Asia Pacific: `ap-northeast-1-tpe-1a`, `ap-south-1-ccu-1a`, `ap-south-1-ccu-2a`, `ap-south-1-del-1a`, `ap-south-1-del-2a`, `ap-southeast-1-bkk-1a`, `ap-southeast-1-han-1a`, `ap-southeast-1-mnl-1a`, `ap-southeast-2-akl-1a`, `ap-southeast-2-per-1a`
+ Europe: `eu-central-1-ath-1a`, `eu-central-1-ham-1a`, `eu-central-1-ist-1a`, `eu-central-1-waw-1a`, `eu-north-1-cph-1a`, `eu-north-1-hel-1a`
+ South America: `us-east-1-bue-1a`, `us-east-1-lim-1a`, `us-east-1-scl-1a`
+ Middle East: `me-south-1-mct-1a`
+ Africa: `af-south-1-los-1a`

In all other Local Zones, Amazon EBS encryption follows the same behavior as in the parent Region.

## Outposts and Wavelength Zones
<a name="ebs-encryption-outposts-wavelength"></a>

All Amazon EBS resources on AWS Outposts and in Wavelength Zones are encrypted by default. You can't create unencrypted volumes or snapshots. If you don't specify a KMS key, Amazon EBS encrypts your resources with your account's default encryption key. By default, this is the AWS managed key (`aws/ebs`). To change the default encryption key for your account, see [Default encryption key](encryption-by-default.md#ebs-default-encryption-key).

When you create a volume from a local snapshot in these zones, the volume is encrypted using the same KMS key as the source snapshot. However, you can change the encryption key when you copy a local snapshot.