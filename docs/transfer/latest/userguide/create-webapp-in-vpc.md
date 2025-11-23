# Create a Transfer Family web app in a VPC

This section describes the procedures for creating a Transfer Family web app in a VPC. You can host your web app's endpoint inside a virtual private cloud (VPC) to use for transferring data to and from an Amazon S3 bucket without going over the public internet. To assign users and groups that can use your web app, see [Assign or add users or groups to a Transfer Family
web app](webapp-add-users.md "webapp-add-users.md").

###### Note

To ensure a private end-to-end data flow when using a Transfer Family web app VPC endpoint, you must implement three additional components. First, set up a PrivateLink endpoint for Amazon S3 Control API operations, which is necessary for Amazon S3 Access Grants API calls. Second, configure an endpoint for Amazon S3 data access using either a PrivateLink Amazon S3 Gateway endpoint (for traffic from within your VPC) or an Amazon S3 Interface endpoint (for traffic from on-premises networks via VPN or Direct Connect). Third, lock down your Amazon S3 bucket access by updating the bucket policies to only permit traffic from these VPC endpoints. This combination ensures all data transfers remain within your private network infrastructure and never traverse the public internet.

## Create a Transfer Family web app

**Prerequisites**

- AWS IAM Identity Center set up with configured identity provider. See [Configure your identity provider for Transfer Family web
  apps](webapp-identity-center.md "webapp-identity-center.md").
- VPC and networking components set up. See [Create a VPC](../../../vpc/latest/userguide/create-vpc.md#create-vpc-and-other-resources "../../../vpc/latest/userguide/create-vpc.md#create-vpc-and-other-resources").
- API endpoint set up for Amazon S3 Control operations. See [Accessing Amazon S3 interface endpoints](../../../AmazonS3/latest/userguide/privatelink-interface-endpoints.md#s3-creating-vpc "../../../AmazonS3/latest/userguide/privatelink-interface-endpoints.md#s3-creating-vpc").
- VPC endpoints for Amazon S3 (Gateway or Interface) set up. See [Types of VPC endpoints for Amazon S3](../../../AmazonS3/latest/userguide/privatelink-interface-endpoints.md#types-of-vpc-endpoints-for-s3 "../../../AmazonS3/latest/userguide/privatelink-interface-endpoints.md#types-of-vpc-endpoints-for-s3"). If you’re using an interface
  endpoint, you must enable private DNS. For an example, see [Introducing private DNS support for Amazon S3 with
  AWS PrivateLink](https://aws.amazon.com/blogs/storage/introducing-private-dns-support-for-amazon-s3-with-aws-privatelink/ "https://aws.amazon.com/blogs/storage/introducing-private-dns-support-for-amazon-s3-with-aws-privatelink/").

###### Note

AWS IAM Identity Center does not support VPC endpoints; all authentication requests transit
the public internet. Additionally, Transfer Family web applications require internet
access to load static content (such as JavaScript, CSS, and HTML files). The
requirements for public internet access are separate from data access. Your VPC
endpoint ensures that connections are routed through your VPC
infrastructure.

###### To create a Transfer Family web app

1.  Sign in to the AWS Management Console and open the AWS Transfer Family console at [https://console.aws.amazon.com/transfer/](https://console.aws.amazon.com/transfer/ "https://console.aws.amazon.com/transfer/").
2.  In the left navigation pane, choose **Web apps**.
3.  Choose **Create web app**. For authentication access, the pane is populated as follows.
    - If you have already created either an organization or account instance in AWS IAM Identity Center, then you see this message: **Your AWS Transfer Family application connected to an account instance of IAM Identity Center**.
    - If you already have an account instance and are a member of an organization instance, you have the option to choose which instance to connect.
    - If you don't already have an account instance, or are a member in an organization instance, you're presented with the options to create an account instance.

4.  In the **Endpoint configuration** section, choose how your users will access your web app:
    - **Publicly accessible**: Your web app endpoint is accessible over the public via HTTPS. This option does not require any VPC configuration, making it straightforward to set up and suitable for applications intended for wide public use.
    - **VPC hosted**: Your web app endpoint is hosted within your Virtual Private Cloud (VPC), providing private network access through your VPC network, AWS Direct Connect, or VPN connections. This option offers enhanced security through network isolation and is recommended for internal applications.

    ###### Note

    You must have a dual-stack VPC configuration. For more
    information, see [Example dual-stack VPC configuration](../../../vpc/latest/userguide/vpc-migrate-ipv6-example.md "../../../vpc/latest/userguide/vpc-migrate-ipv6-example.md") in the
    _Amazon Virtual Private Cloud User Guide_.

    When configuring a VPC hosted endpoint, you'll need to specify:

        + **VPC**: Select an existing VPC or create a new one. A **Create a VPC** button is available.
        + **Availability zones**: Choose the availability zones where your endpoint will be deployed.
        + **Subnets**: Select subnets within each chosen availability zone.
        + **Security groups**: Select or create
         security groups to control access based on source IP
         addresses. If not specified, the VPC's default security
         group is used. Manage security groups through the VPC
         Console. Configure your VPC security groups to allow inbound
         traffic from your network over HTTPS on TCP port 443. This
         is required for IAM Identity Center authentication and web app static
         content loading.

    ###### Note

    The access endpoint cannot be customized for VPC endpoints. To add a custom URL, use the public endpoint.

## Post-creation steps

- Make sure to set up a Cross-origin resource sharing (CORS) policy for all of the buckets that are accessed from the web app endpoint. See [Cross-origin resource sharing (CORS) policy](#webapp-vpce-cors "#webapp-vpce-cors").
- Update your bucket policy to allow traffic only originating from your
  VPC through your VPC endpoint. See [Restricting access to a specific VPC endpoint](#webapp-vpce-bucket-policy "#webapp-vpce-bucket-policy").
- Assign or add users or groups to Transfer Family web app. See [Assign or add users or groups to a Transfer Family
  web app](webapp-add-users.md "webapp-add-users.md").

## Cross-origin resource sharing (CORS) policy

You must set up cross-origin resource sharing (CORS) for all buckets that are used by your web app. For more information about CORS, see [Set up Cross-origin resource sharing (CORS) for your
bucket](access-grant-cors.md "access-grant-cors.md").

###### Important

Before using the following example policy, replace the Allowed Origin with your access endpoint. Otherwise, your end users will receive an error when they attempt to access a location on your web app.

**Example policy:**

```
[
  {
    "AllowedHeaders": [
      "*"
    ],
    "AllowedMethods": [
      "GET",
      "PUT",
      "POST",
      "DELETE",
      "HEAD"
    ],
    "AllowedOrigins": [
      "https://vpce-1234567-example.vpce-mq.transfer-webapp.us-east-1.on.aws"
    ],
    "ExposeHeaders": [
      "last-modified",
      "content-length",
      "etag",
      "x-amz-version-id",
      "content-type",
      "x-amz-request-id",
      "x-amz-id-2",
      "date",
      "x-amz-cf-id",
      "x-amz-storage-class",
      "access-control-expose-headers"
    ],
    "MaxAgeSeconds": 3000
  }
]
```

## Restricting access to a specific VPC endpoint

The following is an example of an Amazon S3 bucket policy that restricts access to
a specific bucket, `amzn-s3-demo-bucket`, only from the VPC endpoint with
the ID `vpce-1a2b3c4d`. If the specified endpoint is not used, the policy
denies all access to the bucket. The `aws:SourceVpce` condition specifies
the endpoint. The `aws:SourceVpce` condition doesn't require an ARN for
the VPC endpoint resource, only the VPC endpoint ID. For more information about
updating your bucket policy to only allow traffic originating from your VPC, see
[Controlling access from VPC endpoints with bucket policies](../../../AmazonS3/latest/userguide/example-bucket-policies-vpc-endpoint.md "../../../AmazonS3/latest/userguide/example-bucket-policies-vpc-endpoint.md"). For more
information about using conditions in a policy, see [Bucket policy
examples using condition keys](../../../AmazonS3/latest/userguide/amazon-s3-policy-keys.md "../../../AmazonS3/latest/userguide/amazon-s3-policy-keys.md"). As a pre-requisite to applying this
policy, you should create an [Amazon S3 VPC endpoint](../../../AmazonS3/latest/userguide/privatelink-interface-endpoints.md "../../../AmazonS3/latest/userguide/privatelink-interface-endpoints.md").

###### Important

Before using the following example policy, replace the VPC endpoint ID with an appropriate value for your use case. Otherwise, you won't be able to access your bucket.

```
{
  "Version":"2012-10-17",
  "Id": "Policy1415115909152",
  "Statement": [
    {
      "Sid": "Access-to-specific-VPCE-only",
      "Principal": "*",
      "Action": "s3:*",
      "Effect": "Deny",
      "Resource": ["arn:aws:s3:::amzn-s3-demo-bucket",
                   "arn:aws:s3:::amzn-s3-demo-bucket/*"],
      "Condition": {
        "StringNotEquals": {
          "aws:SourceVpce": "vpce-1a2b3c4d"
        }
      }
    }
  ]
}
```
