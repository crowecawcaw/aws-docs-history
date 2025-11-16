# Managing versions for AMI-based products on

AWS Marketplace

When you create an Amazon Machine Image (AMI) based product on AWS Marketplace, you include a specific
version of your software. The lifecycle of an AMI-based product for AWS Marketplace doesn't end after
you publish the first version. You should keep your product up-to-date with new versions of
your software. The following sections show you how to manage your versions, which includes
updating version information (such as descriptions and dates), adding new versions, and
restricting access to previous versions.

###### Topics

- [Update version information](#single-ami-updating-version "#single-ami-updating-version")
- [Add a new version](#single-ami-adding-version "#single-ami-adding-version")
- [Restrict a version](#single-ami-restricting-version "#single-ami-restricting-version")

## Update version information

After a version is created, it can be helpful to provide updated information to your
buyers by modifying the information associated with the version. For example, if you
plan to restrict version 1.0 after version 1.1 is released, you can update the
description of version 1.0 to direct buyers to version 1.1, with the date that the
version will be restricted. You update the version information from the
AWS Marketplace Management Portal.

###### To update version information

1. Open the AWS Marketplace Management Portal at [https://aws.amazon.com/marketplace/management/tour/](https://aws.amazon.com/marketplace/management/tour/ "https://aws.amazon.com/marketplace/management/tour/"), and then sign
   in to your seller account.
2. Go to the [**Current server product**](https://aws.amazon.com/marketplace/management/products/server "https://aws.amazon.com/marketplace/management/products/server") page, on the
   **Server products** tab, then select the product that you
   want to modify.
3. From the **Request changes** dropdown, choose
   **Update version information**.
4. On the **Update version** page, select the version that you
   want to update.
5. Update any of the following information that you need to modify:
   - **Release notes**
   - **Usage instructions**
   - **64-bit (x86) Amazon Machine Image (AMI)** –
     Details on usage and security group

6. Select **Submit**.
7. Verify that the request appears on the **Requests** tab with
   the **Under review** status.

###### Note

You can't use this procedure to update the version title, or the AMI associated
with the version. Instead, [create a new
version](#single-ami-adding-version "#single-ami-adding-version") and [restrict the
previous version](#single-ami-restricting-version "#single-ami-restricting-version").

You can check the status of your request at any time from the
**Requests** tab of the [Server
Products](https://aws.amazon.com/marketplace/management/products/server "https://aws.amazon.com/marketplace/management/products/server") page. For more information, see [Get the status of a change
request](single-ami-create-change-request.md#single-ami-getting-change-request-status "single-ami-create-change-request.md#single-ami-getting-change-request-status").

## Add a new version

You can add a new version of your product when you make changes to the product, the
base image, or any other time you need to modify the AMI for the product. Add a new
version of your product from the AWS Marketplace Management Portal.

###### Note

For information about creating an AMI for AWS Marketplace, see [Best practices for building AMIs for use with AWS Marketplace](best-practices-for-building-your-amis.md "best-practices-for-building-your-amis.md").

###### To add a new version

1. Open the AWS Marketplace Management Portal at [https://aws.amazon.com/marketplace/management/tour/](https://aws.amazon.com/marketplace/management/tour/ "https://aws.amazon.com/marketplace/management/tour/"), and then sign
   in to your seller account.
2. Go to the [**Server products**](https://aws.amazon.com/marketplace/management/products/server "https://aws.amazon.com/marketplace/management/products/server") page, on the
   **Current server product** tab, then select the product
   that you want to modify.
3. From the **Request changes** dropdown, choose **Add
   new version**. The **Add a new version** form
   appears, populated with the information from your most recent
   version.

###### Note

You can also choose **Test 'Add version'** to scan your AMI and
AWS CloudFormation template(s) without adding a new version. For more information, refer
to
[Scanning your AMI for publishing requirements](best-practices-for-building-your-amis.md#self-service-scanning "best-practices-for-building-your-amis.md#self-service-scanning")
. 4. In the **Version information** section, provide the following
information:

    * **Version title** – Enter a valid string (for
     example `1.1` or `Version
     2.0`). It must be unique across the product.
    * **Release notes** – Enter text to describe
     details about this version.

5. In the **Delivery options** section, select how the buyer can
   deploy the solution, either AMI (standalone), AMI with CloudFormation, or both.
   You can choose up to three AMI with CloudFormation delivery options.

###### Note

New delivery options can't be added to an existing version. All delivery
options for a single version must be submitted in the same request. 6. In the **Amazon Machine Image (AMI)** section, provide the
following information:

    * **Amazon Machine Image ID** – Enter the AMI ID
     for the AMI that you want to use for this version. You can find the AMI
     ID from the  [list of AMIs in the console](https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#Images:sort=name "https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#Images:sort=name"). The AMI must exist in the
     US East (N. Virginia) Region, and in your AWS Marketplace Seller account. The
     snapshot associated with this AMI can't be encrypted.
    * **IAM access role ARN** – Enter the Amazon
     Resource Name (ARN) for an AWS Identity and Access Management (IAM) role that allows AWS Marketplace to
     gain access to your AMI. For instructions on how to create the IAM
     role, see [Giving AWS Marketplace access to your
     AMI](single-ami-marketplace-ami-access.md "single-ami-marketplace-ami-access.md"). Use the
     standard format for an IAM ARN, for example:
     `arn:aws:iam::123456789012:role/RoleName`.
     The ARN must exist in your AWS Marketplace Seller account.
    * **Operating system (OS)** – Enter the base
     operating system for your AMI.
    * **OS version** – Enter which version of the
     operating system that your AMI is using.
    * **OS user name** – For
     Linux-based AMIs, enter the name of a user that can be
     used to sign into the instance. We recommend using
     *ec2-user*.
    * **Scanning port** – Enter the port number that
     can be used to log into the operating system: the SSH port for a
     Linux AMI or the RDP port for a
     Windows AMI.

7. Provide the following configurations for the **AMI
   delivery option** section, if applicable:
   - **Recommended instance type**– Choose the
     instance type that buyers get by default.
   - **Usage instructions** – Enter instructions
     for using the AMI or a link to more information about using the AMI. For
     example: `To get started with the product, navigate to
https://example.com/usage.htm.`
   - **Endpoint URL** – Provide information about
     how the buyer can access the software after they create an instance.
     Enter the **Protocol** (_https_ or
     _http_), the **Relative URL**
     (for example, `/index.html`),
     and the **Port** (for example,
     `443`) that buyers can use to access your
     product. (The host name depends on the EC2 instance, so you only need to
     provide the relative path).
   - **Security group recommendations** – Enter the
     information for one or more recommendations, including the protocol
     (_TCP_ or _UDP_), range of
     ports to allow, and list of IPv4 CIDR IPs (in the form
     _xxx.xxx.xxx.xxx/nn_, for example,
     `192.0.2.0/24`).

8. Provide the following configuration settings for the **AMI with
   CloudFormation delivery option**, if applicable:
   - **Delivery option title** – This is a unique
     name to identify this Single AMI CloudFormation template delivery
     option.
   - **Short Description** – A brief description of
     the CloudFormation template.
   - **Long Description** – A detailed description
     of the CloudFormation template.
   - **Recommended Instance type** – The instance
     type, buyers get by default.
   - **Usage instructions** – Instructions for
     using the solution or a link to more information about using the
     solution.
   - **CloudFormation template link** – The URL to
     the location of your CloudFormation template in Amazon S3. For nested stacks
     or templates, provide the entry point, or parent, template. The Amazon S3
     bucket that your file resides must be publicly accessible. For more
     information, see [Add CloudFormation templates to your
     product](cloudformation.md "cloudformation.md").
   - **AMI parameter name** – Add the name of the
     parameter in the CloudFormation template that the EC2 instance resources
     in your template are referencing for their `ImageId` property
     value. AWS Marketplace replaces the specified parameter with an [AWS Systems Manager Parameter Store](../../../systems-manager/latest/userguide/systems-manager-parameter-store.md "../../../systems-manager/latest/userguide/systems-manager-parameter-store.md") parameter. When buyers deploy your template, that parameter
     resolves to the AWS Region-specific AMI ID of your published product.
     For more information, see [Requirements for AMI details](cloudformation.md#ami-requirements-sse "cloudformation.md#ami-requirements-sse").
   - **Architecture diagram link** – The URL to the
     location of your architectural diagram in Amazon S3. The max image file must
     be 1560x878 or 1560x3120 pixels in size with a 16:9 or 1:2 ratio. The Amazon S3
     bucket that your image file resides must be publicly accessible. For
     diagram requirements, see [Architectural diagram](cloudformation.md#topology-diagram "cloudformation.md#topology-diagram").

9. Select **Submit** to submit the request to add your new
   version.

###### Note

Adding a new version results in a scanning of the AMI. For more information, refer to
[Scanning your AMI for publishing requirements](best-practices-for-building-your-amis.md#self-service-scanning "best-practices-for-building-your-amis.md#self-service-scanning"). 10. Verify that the request appears on the **Requests** tab with
the **Under review** status. If there are errors to fix, the
page displays the errors in a table at the top of the page, and the specific
fields that need to be updated display in red.

You can check the status of your request at any time from the
**Requests** tab of the [**Server
products**](https://aws.amazon.com/marketplace/management/products/server "https://aws.amazon.com/marketplace/management/products/server") page. The new version will be reviewed and, if
successful, published as a new public version of your product. If there is an issue, the
status might be **Action required**. Select the request to see details,
including any issues.

If your request is successful, your existing users receive the following email
message. The message notifies them that the new version is available, links to the
version's release notes, and suggests that they upgrade to the latest version. As the
AWS account root user, you also receive a copy of the email message in the email
account that's associated with your AWS account.

```
Greetings from AWS Marketplace,

Thank you for subscribing to <product-title>

We are writing to inform you that <seller-name> has added a new version to <product-title> on AWS Marketplace.
As an existing customer, your subscription to the product, any running instances and access to previous versions
are unaffected. However, <seller-name> does recommend you to update to the latest version, <product-title>/<version-title>
by visiting <product-detail-page-of-new-listing>.

For additional questions or upgrade information, please contact <seller-name> directly. Click here <link of seller page on MP>
to visit the seller’s profile page on AWS Marketplace.

Release notes for <product-title>/<version-title>:

<release-notes>

Thank you,
The AWS Marketplace Team
https://aws.amazon.com/marketplace

AWS, Inc. is a subsidiary of Amazon.com, Inc. Amazon.com is a registered trademark of Amazon.com, Inc.
This message was produced and distributed by AWS Inc., 410 Terry Ave. North, Seattle, WA 98109-5210
```

## Restrict a version

If you want to prevent buyers from accessing a specific version of your public
product, you can restrict that version.

###### Note

All subscribers can use the current version regardless of the restriction status.
AWS Marketplace guidelines require that you continue to offer support to existing buyers for
90 days after restricting the version. Your AMI will be marked as deprecated after
the version is restricted. For more information, see [Deprecate an AMI](../../../AWSEC2/latest/WindowsGuide/ami-deprecate.md "../../../AWSEC2/latest/WindowsGuide/ami-deprecate.md") in the _Amazon Elastic Compute Cloud User Guide
for Windows Instances_.

###### To restrict a version

1. Open the AWS Marketplace Management Portal at [https://aws.amazon.com/marketplace/management/tour/](https://aws.amazon.com/marketplace/management/tour/ "https://aws.amazon.com/marketplace/management/tour/"), and then sign
   in to your seller account.
2. Go to the [**Server products**](https://aws.amazon.com/marketplace/management/products/server "https://aws.amazon.com/marketplace/management/products/server") page, on the
   **Current server product** tab, then select the product
   that you want to modify.
3. From the **Request changes** dropdown, choose
   **Restrict version**.
4. On the **Restrict version** page, select the version (or
   versions) that you want to restrict.
5. Select **Submit** to submit your request for review.
6. Verify that the **Requests** tab shows the **Request
   status** as **Under review**. When the request
   completes, the status is **Succeeded**.

###### Note

You can't restrict all versions of a product. If you try to restrict the last
remaining public version of a product, you will receive an error. To completely
remove a product, see [Removing a product from
AWS Marketplace](removing-products-from-aws-marketplace.md "removing-products-from-aws-marketplace.md").

You can check the status of your request at any time from the
**Requests** tab of the [**Server
products**](https://aws.amazon.com/marketplace/management/products/server "https://aws.amazon.com/marketplace/management/products/server") page. For more information, see [Get the status of a change
request](single-ami-create-change-request.md#single-ami-getting-change-request-status "single-ami-create-change-request.md#single-ami-getting-change-request-status").

###### Note

Restricting a version can take up to 3 days to complete.

If your request is successful, your existing users receive the following email message
that notifies them of the version restriction and suggests they use the most recent
version available. As the AWS account root user, you also receive a copy of the email
message in the email account that's associated with your AWS account.

```
Greetings from AWS Marketplace,

Thank you for subscribing to <product-title>.

We are writing to inform you that, as of <Version-Restriction-Date>, <Seller Name> will no longer offer version(s) "<version-title>" to new subscribers. Your use and subscription is unaffected for this version(s), however it is recommended that users upgrade to the latest version on AWS Marketplace.

For additional questions or upgrade information, please contact <seller-name> directly. Click here<link of seller page on MP> to visit the seller’s profile page on AWS Marketplace.

Thank you,
The AWS Marketplace Team
https://aws.amazon.com/marketplace

AWS, Inc. is a subsidiary of Amazon.com, Inc. Amazon.com is a registered trademark of Amazon.com, Inc. This message was produced and distributed by AWS Inc., 410 Terry Ave. North, Seattle, WA 98109-5210
```
