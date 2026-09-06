

# Troubleshooting access to Amazon S3
<a name="postgresql-s3-export-troubleshoot"></a>

If you encounter connection problems when attempting to export data to Amazon S3, first confirm that the outbound access rules for the VPC security group associated with your DB instance permit network connectivity. Specifically, the security group must have a rule that allows the DB instance to send TCP traffic to port 443 and to any IPv4 addresses (0.0.0.0/0). For more information, see [Provide access to the DB cluster in the VPC by creating a security group](CHAP_SettingUp_Aurora.md#CHAP_SettingUp_Aurora.SecurityGroup).

See also the following for recommendations:
+ [Troubleshooting Amazon Aurora identity and access](security_iam_troubleshoot.md)
+ [Troubleshooting Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/troubleshooting.html) in the *Amazon Simple Storage Service User Guide*
+ [Troubleshooting Amazon S3 and IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_iam-s3.html) in the *IAM User Guide*