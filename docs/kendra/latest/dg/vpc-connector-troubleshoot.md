# Troubleshooting VPC connection

issues

If you encounter any issues with your virtual private cloud (VPC) connection,
check that your IAM permissions, security group settings, and the
subnet's route tables are configured correctly.

One potential cause of a failed data source connector sync is that the data source
might be unreachable from the subnet that you assigned to Amazon Kendra. To
troubleshoot this issue, we recommend that you create an Amazon EC2 instance
with the same Amazon VPC settings. Then, try to access the data source from
this Amazon EC2 instance using REST API calls or other methods (based on the
specific type of your data source).

If you successfully access the data source from the Amazon EC2 instance
that you create, it means your data source is reachable from this subnet. Therefore,
your sync issue isn't related to your data source being inaccessible by Amazon VPC.

If you can't access your Amazon EC2 instance from your VPC configuration
and validate it with the Amazon EC2 instance that you created, you need to
troubleshoot further. For example, if you have an Amazon S3 connector whose
sync failed with errors about connection issues, you can set up an Amazon EC2 instance with the same Amazon VPC configuration that you assigned to your
Amazon S3 connector. Then, use this Amazon EC2 instance to test if your
Amazon VPC has been set up correctly.

The following is an example of setting up an Amazon EC2 instance to
troubleshoot your Amazon VPC connection with an Amazon S3 data
source.

###### Topics

- [Step 1: Launch an Amazon EC2 instance](#vpc-connector-troubleshoot-1 "#vpc-connector-troubleshoot-1")
- [Step 2: Connect to Amazon EC2 instance](#vpc-connector-troubleshoot-2 "#vpc-connector-troubleshoot-2")
- [Step 3: Test Amazon S3
  access](#vpc-connector-troubleshoot-3 "#vpc-connector-troubleshoot-3")

## Step 1: Launch an Amazon EC2 instance

1.  Sign in to the AWS Management Console and open the Amazon EC2 console at
    [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2.  Select **Launch an instance**.
3.  Choose **Network settings**, and then choose
    **Edit**, and then do the following:
    1. Choose the same VPC and **Subnet** that you
       assigned to Amazon Kendra.
    2. For **Firewall (security groups)**, choose
       **Select existing security group**. Then,
       select the security group that you assigned to Amazon Kendra.

    ###### Note

    The security group should allow outbound traffic to
    Amazon S3. 3. Set **Auto-assign public IP** to
    **Disable**. 4. In **Advanced details**, do the following:

        * For **IAM instance profile**,
         select **Create new IAM profile** to
         create and attach an IAM instance profile
         to your instance. Make sure that the profile has
         permissions to access Amazon S3. For more
         information, see [How can I grant my Amazon EC2 instance
         access to an Amazon S3 bucket?](https://repost.aws/knowledge-center/ec2-instance-access-s3-bucket "https://repost.aws/knowledge-center/ec2-instance-access-s3-bucket") in
         AWS re:Post.
        * Leave all other settings as default.

    5. Review and launch the Amazon EC2 instance.

## Step 2: Connect to Amazon EC2 instance

After your Amazon EC2 instance is running, go to your instance detail
page and connect to your instance. To do so, use the steps in [Connect to your instances without requiring a public
IPv4 address using EC2 Instance Connect Endpoint](../../../AWSEC2/latest/UserGuide/connect-with-ec2-instance-connect-endpoint.md "../../../AWSEC2/latest/UserGuide/connect-with-ec2-instance-connect-endpoint.md") in the _Amazon EC2 User Guide for Linux
Instances_.

## Step 3: Test Amazon S3

access

After you have connected to your Amazon EC2 instance terminal, run an
AWS CLI command to test the connection from this private subnet to your Amazon S3 bucket.

To test Amazon S3 access, type the following AWS CLI command in the
AWS CLI: `aws s3 ls`

After the AWS CLI command runs, review the following:

- If you've set up the necessary IAM permissions
  correctly and your Amazon S3 setup is correct, you should see a
  list of your Amazon S3 buckets.
- If you see permission errors such as `Access Denied`, it's
  likely that yourVPC configuration is correct, but something is wrong
  with your IAM permissions or Amazon S3 bucket
  policy.

If the command is timing out, then it's likely that your connection is timing
out because your VPC setup is incorrect and the Amazon EC2 instance can't access Amazon S3
from your subnet. Reconfigure your VPC, and try again.
