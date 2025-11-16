AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Working with key pairs for EC2-compatible instances in AWS OpsHub

When you launch an Amazon EC2-compatible instance and intend to connect to it using SSH, you have to provide a key pair.
You can use Amazon EC2 to create a new key pair, or you can import an existing key pair or manage your key pairs.

###### To create, import, or manage key pairs

1. Open **Compute** on the AWS OpsHub dashboard.
2. In the navigation pane, choose the **Compute (EC2)** page, and then choose
   the **Key Pairs** tab. You are redirected to the Amazon EC2
   console where you can create, import, or manage your key pairs.
3. For instructions on how to create and import key pairs, see [Amazon EC2 key pairs and Linux instances](../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md#prepare-key-pair "../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md#prepare-key-pair") in the _Amazon EC2 User Guide_.
