# Using Amazon VPC with an Amazon S3

data source

This topic provides a step-by-step example that shows how to connect to an Amazon S3 bucket
by using an Amazon S3 connector through Amazon VPC. The example assumes that you're starting with
an existing S3 bucket. We recommend that you upload just a few documents to your S3
bucket to test the example.

You can connect Amazon Kendra to your Amazon S3 bucket through Amazon VPC. To do so, you must specify the Amazon VPC subnet and Amazon VPC security groups when creating your Amazon S3 data source
connector.

###### Important

So that an Amazon Kendra
Amazon S3 connector can access your Amazon S3 bucket, make sure that
you have assigned an Amazon S3 endpoint to your virtual private cloud
(VPC).

For Amazon Kendra to sync documents from your Amazon S3 bucket through
Amazon VPC, you must complete the following steps:

- Set up an Amazon S3 endpoint for Amazon VPC. For more
  information about how to set up an Amazon S3 endpoint, see [Gateway endpoints for Amazon S3](../../../vpc/latest/privatelink/vpc-endpoints-s3.md "../../../vpc/latest/privatelink/vpc-endpoints-s3.md") in the _AWS PrivateLink Guide_.
- (Optional) Checked your Amazon S3 bucket policies to make sure that
  the Amazon S3 bucket is accessible from the virtual private cloud (VPC)
  that you assigned to Amazon Kendra. For more information, see [Controlling access from VPC endpoints with bucket policies](../../../AmazonS3/latest/userguide/example-bucket-policies-vpc-endpoint.md "../../../AmazonS3/latest/userguide/example-bucket-policies-vpc-endpoint.md") in the
  _Amazon S3 User Guide_

###### Steps

- [Step 1: Configure an Amazon VPC](#s3-configure-vpc "#s3-configure-vpc")
- [(Optional) Step 2: Configure Amazon S3 bucket policy](#s3-configure-bucket-policy "#s3-configure-bucket-policy")
- [Step 3: Create a test Amazon S3 data source
  connector](#s3-connect-vpc "#s3-connect-vpc")

## Step 1: Configure an Amazon VPC

Create a VPC network including a private subnet with an Amazon S3 gateway
endpoint and a security group for Amazon Kendra to use later.

###### To configure a VPC with a private subnet, an S3 endpoint, and a security

group

1. Sign in to the AWS Management Console and open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. **Create a VPC with a private subnet and an S3
   endpoint for Amazon Kendra to use:**

From the navigation pane, choose **Your VPCs**, and then
choose **Create VPC**.

    1. For **Resources to create**, choose **VPC
     and more**.
    2. For **Name tag**, enable
     **Auto-generate**, then enter
     `kendra-s3-example`.
    3. For **IPv4 / IPv6 CIDR block**, keep the default
     values.
    4. For **Number of Availability Zones (AZs)**,
     choose **number 1**.
    5. Select **Customize AZs**, and then select an
     Availability Zone from the **First availability
     zone** list.


    Amazon Kendra only supports a specific set of Availability
     Zones.
    6. For **Number of public subnets**, choose
     **number 0**.
    7. For **Number of private subnets**, choose
     **number 1**.
    8. For **NAT gateways**, choose
     **None**.
    9. For **VPC endpoints**, choose **Amazon S3 gateway.**.
    10. Leave the rest of the values at their default settings.
    11. Select **Create VPC**.


    Wait until the **Create VPC** workflow finishes.
     Then, choose **View VPC** to check the
     **VPC** you just created.You have now created a VPC network with a private subnet, which does not

have access to the public internet. 3. **Copy your VPC endpoint ID of your Amazon S3
endpoint:**

    1. From the navigation pane, choose
     **Endpoints**.
    2. In the **Endpoints** list, find the Amazon S3 endpoint
     `kendra-s3-example-vpce-s3` that you just created
     together with your VPC.
    3. Make a note of the **VPC endpoint ID**.You have now created an Amazon S3 gateway endpoint to access your Amazon S3 bucket

through a subnet. 4. **Create a **Security Group** for
Amazon Kendra to use:**

    1. From the navigation pane, choose **Security
     Groups**, then select **Create security
     group**.
    2. For **Security group name**, enter
     `s3-data-source-security-group`.
    3. Choose your VPC from the **Amazon VPC**
     list.
    4. Leave **inbound rules** and **outbound
     rules** as the default.
    5. Choose **Create security group**.You have now created a VPC security group.

You assign the subnet and security group that you created to your Amazon Kendra Amazon S3 data source connector during the connector configuration process.

## (Optional) Step 2: Configure Amazon S3 bucket policy

In this optional step, learn how to configure an Amazon S3 bucket policy so that your
Amazon S3 bucket is only accessible from the VPC that you assign to Amazon Kendra.

Amazon Kendra uses IAM roles to access your Amazon S3 bucket and doesn't require
that you configure an Amazon S3 bucket policy. However, you might find it useful to
create a bucket policy if you want to configure an Amazon S3 connector using
an Amazon S3 bucket that has existing policies restricting access to it from the public
internet.

###### To configure your Amazon S3 bucket policy

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. From the navigation pane, choose **Buckets**.
3. Choose the name of the Amazon S3 bucket that you want to sync with Amazon Kendra.
4. Choose the **Permissions** tab, scroll down to
   **Bucket policy**, and then click on
   **Edit**.
5. Add or modify your bucket policy to allow access only from the VPC
   endpoint that you created.

The following is an example bucket policy. Replace
`bucket-name` and
`vpce-id` with your Amazon S3
bucket name and the Amazon S3 endpoint ID that you noted earlier. 6. Select **Save changes**.

Your S3 bucket is now accessible only from the specific VPC that you
created.

## Step 3: Create a test Amazon S3 data source

connector

To test your Amazon VPC configuration, create an Amazon S3
connector. Then, configure it with the VPC that you created by following the steps
outlined in [Amazon S3](data-source-s3.md "data-source-s3.md").

For Amazon VPC configuration values, choose the values that you created
during this example:

- **Amazon VPC(VPC)** –
  `kendra-s3-example-vpc`
- **Subnets** –
  `kendra-s3-example-subnet-private1-[availability
zone]`
- **Security groups** –
  `s3-data-source-security-group`

Wait for your connector to finish creating. After the Amazon S3 connector
has been created, choose **Sync now** to initiate a sync.

It might take several minutes to several hours to finish the sync, depending on
how many documents are in your Amazon S3 bucket. To test the example, we
recommend that you upload just a few documents to your S3 bucket. If your
configuration is correct, you should eventually see a **Sync
status** of **Completed**.

If you encounter any errors, see [Troubleshooting Amazon VPC connection](vpc-connector-troubleshoot.md "vpc-connector-troubleshoot.md").
