# Step 2: License the Amazon DCV Server

After you have installed the Amazon DCV server software, you need to download and install
the license to use Amazon DCV. The Amazon DCV licensing requirements differ depending on where
you are installing and using the Amazon DCV server.

###### Important

The following licensing requirements only apply to Amazon DCV version 2017.0 and later.

## Amazon DCV licensing requirements

###### Topics

- [Amazon DCV on Amazon EC2](#setting-up-license-ec2 "#setting-up-license-ec2")
- [Other use cases for Amazon DCV](#setting-up-license-otherusecases "#setting-up-license-otherusecases")
- [Microsoft licensing requirements for remotely accessing Windows Server](#windows-lic-reqs "#windows-lic-reqs")

### Amazon DCV on Amazon EC2

You do not need a license server to install and use the Amazon DCV server on an EC2 instance,
including instances running on AWS Outposts and AWS Local Zones.
The Amazon DCV server automatically detects that it is running on an Amazon EC2 instance and
periodically connects to an S3 bucket to determine whether a valid license is available.

Make sure that your instance has the following properties:

- It can reach the Amazon S3 endpoint. If it has access to the internet, it connects
  using the Amazon S3 public endpoint. If your instance doesn't have access to the internet,
  configure a gateway endpoint for your VPC with an outbound security group rule or
  access control list (ACL) policy that allows you to reach Amazon S3 through HTTPS. For more
  information, see [Gateway VPC
  Endpoints](../../../vpc/latest/userguide/vpce-gateway.md "../../../vpc/latest/userguide/vpce-gateway.md") in the _Amazon VPC User Guide_. If you experience
  any issues connecting to the S3 bucket, see [Why can’t I connect to an
  S3 bucket using a gateway VPC endpoint?](https://aws.amazon.com/premiumsupport/knowledge-center/connect-s3-vpc-endpoint/ "https://aws.amazon.com/premiumsupport/knowledge-center/connect-s3-vpc-endpoint/") in the _AWS Knowledge
  Center_.
- It has permission to access the required Amazon S3 object. Add the following Amazon S3
  access policy to the instance's IAM role and replace the
  `region` placeholder with your AWS Region (for example,
  `us-east-1`). For more information, see [Create IAM Role](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "s3:GetObject",
 "Resource": "arn:aws:s3:::dcv-license.`region`/*"
 }
 ]
}`

```

- If you're using a Windows instance, ensure that the instance can access the
  _instance metadata service_. Access to this service is required
  to ensure that the Amazon DCV server can be properly licensed. For more information about the
  instance metadata service, see [Instance Metadata and
  User Data](../../../AWSEC2/latest/WindowsGuide/ec2-instance-metadata.md "../../../AWSEC2/latest/WindowsGuide/ec2-instance-metadata.md") in the _Amazon EC2 User Guide_.

If you're using a custom Windows AMI, you must install EC2Launch,
this ensures that your instance can access the instance metadata service. For more
information, see [Configuring a Windows Instance Using
EC2Launch](../../../AWSEC2/latest/WindowsGuide/ec2launch.md "../../../AWSEC2/latest/WindowsGuide/ec2launch.md") in the _Amazon EC2 User Guide_.

If you're installing and using the Amazon DCV server on an Amazon EC2 instance, you can skip the
rest of this chapter. The rest of this chapter only applies to all other use cases for the Amazon DCV server.

### Other use cases for Amazon DCV

For all other use cases, a license is required to install and use the Amazon DCV server. The following licensing
options are available:

- **Automatic evaluation license**— This type of license is
  automatically installed when you install the Amazon DCV server. This type of license is valid
  for a period of 30 days after it's installed. After the license expires, you can no
  longer create and host Amazon DCV sessions on the server. These licenses are suitable
  for short-term testing and evaluation. To test for a longer period, request an
  extended evaluation license.

###### Note

The Amazon DCV server defaults to the automatic evaluation license if no other license is
configured.

- **Extended evaluation license**— An extended evaluation
  license is an evaluation license that extends the initial 30-day evaluation period
  provided by the automatic evaluation license. The period is determined by AWS on a
  case-by-case basis. Extended evaluation licenses are invalid after they reach their
  expiration date, and you can no longer create and host Amazon DCV sessions on the server.
  Extended evaluation licenses must be requested from an Amazon DCV distributor or reseller
  listed on the [How to
  Buy](https://www.nice-software.com/index.html#buy "https://www.nice-software.com/index.html#buy") page of the Amazon DCV website. The licenses come as a license file that
  must be installed on the Amazon DCV server.

###### Note

When using Amazon DCV on Amazon EC2 Mac instance, Amazon DCV server the instance must have access to the Amazon DCV license S3 bucket. If the instance doesn't have access to the license S3 bucket, it will not be possible to start a Amazon DCV session.

- **Production license**—A production license is a full
  license that you purchase from Amazon DCV. Production licenses are _floating
  licenses_ that are managed by a license server. With floating licenses,
  you can run multiple Amazon DCV servers in your network. At the same time, you can also limit
  the number of concurrent Amazon DCV sessions you can create across all of the servers. You
  need one license for each concurrent Amazon DCV session. Production licenses are
  distributed as a license file that you must install on a Reprise License Manager (RLM)
  server. There are two types of production licenses:
  - **Perpetual Licenses**— Perpetual licenses
    don't have an expiration date and can be used for an indefinite period.
  - **Subscriptions**— Subscriptions are valid
    for a limited period of time, typically one year. The expiration date of the
    license is indicated in the license file. After the license expires, you can no
    longer create and host Amazon DCV sessions on your Amazon DCV servers.

For information about how to purchase a Amazon DCV perpetual license or a subscription, see
[How to Buy](https://www.nice-software.com/index.html#buy "https://www.nice-software.com/index.html#buy") on the
Amazon DCV website and find a Amazon DCV distributor or reseller in your region.

#### Licensing requirements

- Amazon DCV clients don't require a license.
- Amazon DCV server license files are backward compatible with previous versions of the Amazon DCV server. For
  example, you can use a Amazon DCV server version 2021 license with Amazon DCV server version 2019.
- Amazon DCV server versions require at least the same version of the Amazon DCV server license. For example, if
  you use a Amazon DCV server version 2021, you need a license version 2021 or later. If you upgrade
  to a later Amazon DCV server version, you must request compatible license files. For more
  information, contact your Amazon DCV distributor or reseller.

###### Note

For information about the Amazon DCV server compatibility, see [Compatibility considerations](setting-up-upgrading.md#compatibility-considerations "setting-up-upgrading.md#compatibility-considerations").

### Microsoft licensing requirements for remotely accessing Windows Server

Microsoft requires that, in addition to a Windows Server Client Access License (CAL),
you must have a Windows Server Remote Desktop Services (RDS) CAL for your version of
Windows Server for each user that remotely accesses the server’s graphical user interface
(GUI). This regardless of the remote display protocol that you use. This license is also
required if you use Amazon DCV to access the GUI of a remote Windows Server host.

If you run a Amazon DCV server on an Amazon EC2 instance and you use a [Windows Server
AMI](https://aws.amazon.com/windows/resources/amis/ "https://aws.amazon.com/windows/resources/amis/"), Amazon takes care of the licensing costs for the Windows Server CAL, and provides two Windows Server RDS CALs
that are intended solely for administrative purposes. This is for testing, maintenance, and administration only.

For more information, see the [Microsoft
Product Terms Site](https://www.microsoft.com/licensing/terms/ "https://www.microsoft.com/licensing/terms/"). If you have questions about your licensing or rights to Microsoft software,
consult your legal team, Microsoft, or your Microsoft reseller.
