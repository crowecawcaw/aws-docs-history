AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Updating your Amazon Linux 2 AMIs on Snowball Edge

As a best-practice for security, keep your Amazon Linux 2 AMIs up-to-date on Snowball Edge. Regularly check the [Amazon Linux 2 AMI (HVM), SSD Volume Type (64-bit x86)](https://aws.amazon.com/marketplace/pp/prodview-zc4x2k7vt6rpu "https://aws.amazon.com/marketplace/pp/prodview-zc4x2k7vt6rpu") in the AWS Marketplace for updates. When you identify the need to update your AMI, import the latest Amazon Linux 2 image to the Snow device. See [Importing an Image into Your Device as an Amazon EC2-compatible AMI](ec2-ami-import-cli.md "ec2-ami-import-cli.md").

You can also get the latest Amazon Linux 2 image ID using the `ssm get-parameters` command in the AWS CLI.

```

  aws ssm get-parameters --names /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2 --query 'Parameters[0].[Value]' --region `your-region`

```

The command returns the latest image ID of the AMI. For example:

```

   ami-0ccb473bada910e74

```
