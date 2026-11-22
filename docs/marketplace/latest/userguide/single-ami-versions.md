

# Managing versions for AMI-based products on AWS Marketplace

When you create an Amazon Machine Image (AMI) based product on AWS Marketplace, you include a specific version of your software. The lifecycle of an AMI-based product for AWS Marketplace doesn't end after you publish the first version. You should keep your product up-to-date with new versions of your software. The following sections show you how to manage your versions, which includes updating version information (such as descriptions and dates), adding new versions, and restricting access to previous versions.

**Topics**
+ [View versions](#single-ami-viewing-versions)
+ [Update version information](#single-ami-updating-version)
+ [Add a new version](#single-ami-adding-version)
+ [Restrict a version](#single-ami-restricting-version)

## View versions
<a name="single-ami-viewing-versions"></a>

View your versions to check their scan results and to find your product ID, product code, and AMI aliases.

**To view versions**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose the **Delivery** tab.

   The **Versions** section lists your versions in the following columns:
   + **Version title** – The title that buyers see.
   + **Scan result** – The result of the latest security scan of the version: **Passed**, the number of issues found, **Assessment expired**, or **Missing permission**.
   + **Version visibility** – **Public** versions are discoverable and available to all buyers. **Limited** versions are available only to allowlisted AWS accounts. **Restricted** versions aren't offered to new subscribers. Existing subscribers can still launch them. AWS Marketplace marks a restricted version's AMI as deprecated, so it doesn't appear in AMI search results unless you search for its AMI ID.
   + **Due date** – The date by which you must resolve the security issues that a scan found.

1. Choose the title of the version.

   The **Version summary** section shows the **Product ID** and **Product code**. The section for an AMI delivery option shows the **AMI alias** of the version. For more information, see [Using AMI aliases in AWS Marketplace](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-ami-aliases.html) in the *AWS Marketplace Buyer Guide*.

If a scan finds security issues in a version, the version details page shows the **Security issues found** alert. To resolve the issues, add a new version and restrict the affected version by the due date. If you don't, AWS Marketplace restricts the affected versions or temporarily restricts the product. Active subscribers keep access, but new buyers can't find or subscribe to the product. To start a new version from the alert, choose **Add version**.

If your product uses custom metering or contract pricing, the version details page also shows the **Integrate new version with AWS Marketplace** alert. Each new version needs its own integration so that buyers are billed for their use.

## Update version information
<a name="single-ami-updating-version"></a>

After a version is created, it can be helpful to provide updated information to your buyers by modifying the information associated with the version. For example, if you plan to restrict version 1.0 after version 1.1 is released, you can update the description of version 1.0 to direct buyers to version 1.1, with the date that the version will be restricted. You update the version information from AWS Partner Central.

**To update version information**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose the **Delivery** tab.

1. In the **Versions** section, select the version that you want to update.

   You can update restricted versions too.

1. From the **Edit** menu, choose **Update version**.

   You can also choose **Edit** on the details page of the version.

1. Update any of the following fields:
   + **Release notes** – Up to 30,000 characters.
   + For the **AMI delivery option**: **Recommended instance type**, **Usage instructions**, **Security group recommendations**, and **Access endpoint URL**.
   + For each **AMI with CloudFormation delivery option**: **Delivery option title**, **Short description**, **Long description**, **Usage instructions**, **Recommended instance type**, and **Architecture diagram link**.
   + For each **EC2 Image Builder component delivery option**: **Delivery option title** and **Usage instructions**.

   The same limits apply as when you add a version. You can't change the version title, AMI ID, IAM access role ARN, operating system details, scanning port, or AFI IDs. To change them, add a new version.

1. Choose **Save and submit**.

Your change request appears on the product's **Change history** tab. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name. While a request is in progress, the actions on the **Delivery** tab are unavailable.

**Note**  
You can't use this procedure to update the version title, or the AMI associated with the version. Instead, [create a new version](#single-ami-adding-version) and [restrict the previous version](#single-ami-restricting-version).

## Add a new version
<a name="single-ami-adding-version"></a>

You can add a new version of your product when you make changes to the product, the base image, or any other time you need to modify the AMI for the product. Add a new version of your product from AWS Partner Central. 

**Note**  
For information about creating an AMI for AWS Marketplace, see [Best practices for building AMIs for use with AWS Marketplace](best-practices-for-building-your-amis.md).

**To add a new version**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose the **Delivery** tab.

1. In the **Versions** section, choose **Add version**.

   For a new product, you can instead choose **Start** on the **Configure version and delivery options** card under **Step 2: Delivery configuration**. On a new product, **Add version** and this card are available after you complete the **Add Regions** and **Add instance types** cards.

1. On the **Configure version** step, under **Version information**, enter the following:
   + **Version title** – A title that buyers use to tell your releases apart, for example {{1.1}}. The title can have up to 64 characters and must be unique in your product. You can't use `latest`, a space before ™, or characters other than printable ASCII characters and the symbols ©, ®, ™, ¢, £, ¤, and ¥. You can't change the title after you submit. To see your recent titles, expand **View previous version titles**.
   + **Release notes** – Details about this version, up to 30,000 characters.
   + (Optional) **Test version** – To check this version without adding it, select **Test this version**. For more information, see [Scanning your AMI for publishing requirements](best-practices-for-building-your-amis.md#self-service-scanning).

   The form starts with the values from your latest version, except **IAM access role ARN**, **Amazon FPGA Image (AFI) IDs**, **Component ARN**, and **AMI parameter name**. For a product that isn't in draft, **Version title** and **Amazon Machine Image (AMI) ID** also start blank.

1. (Optional) Under **Tags**, add tags to the change request.

1. Choose **Next**.

**To configure delivery options for a new version**

1. On the **Configure delivery options** step, under **Delivery option**, for **Delivery method**, select one or more of the following:
   + **AMI (standalone)** – Buyers deploy your AMI from AWS Marketplace or the Amazon EC2 console.
   + **AMI with CloudFormation** – Buyers deploy your AMI and other AWS resources with CloudFormation. You can add up to three CloudFormation templates.
   + **EC2 Image Builder component** – Buyers add your software to their own image pipelines. You can add up to five components. For more information, see [EC2 Image Builder component-based products in AWS Marketplace](ec2-ib-component-products.md).

   You can't add delivery options to a version after you submit it. Include every delivery option for this version in this request.
**Note**  
In the AWS European Sovereign Cloud catalog, only **AMI (standalone)** is available.

1. Enter the details for each delivery method that you selected:
   + If you selected **AMI (standalone)** or **AMI with CloudFormation**, enter the following under **Amazon Machine Image (AMI)**. These details apply to every AMI delivery option in the version.
     + **Amazon Machine Image (AMI) ID** – The ID of the AMI for this version, for example {{ami-086d874dcc2f96d24}}. The AMI must exist in the US East (N. Virginia) Region and in your AWS Marketplace seller account. The snapshot associated with this AMI can't be encrypted.
     + **IAM access role ARN** – The ARN of an IAM role that gives AWS Marketplace access to your AMI, for example {{arn:aws:iam::123456789012:role/RoleName}}. The role must exist in your AWS Marketplace seller account. For instructions, see [Giving AWS Marketplace access to your AMI](single-ami-marketplace-ami-access.md).
     + **Operating system (OS)** – Choose the base operating system of your AMI. It must be compatible with your product's instance types.
     + **OS version** – The version of the operating system.
     + **OS user name** – A user name that can sign in to the instance. Use letters, numbers, hyphens, and underscores. We recommend *ec2-user*.
     + (Optional) **Scanning port** – The SSH port for a Linux AMI or the RDP port for a Windows AMI.
     + (Optional) **Amazon FPGA Image (AFI) IDs** – Up to 15 AFI IDs to associate with your AMI. Choose **Add AFI ID** for each one. Each AFI must exist in the US East (N. Virginia) Region and in your AWS Marketplace seller account, and the IAM access role must have permission to share it with AWS Marketplace. For more information, see [Giving AWS Marketplace access to your FPGA images](https://docs.aws.amazon.com/marketplace/latest/userguide/single-ami-marketplace-ami-access.html#single-ami-marketplace-afi-access). AFIs load only on F2 instance types. Use AFI IDs only in a version whose sole delivery method is **AMI (standalone)**. A version with AFI IDs can't include **AMI with CloudFormation** or **EC2 Image Builder component** delivery options. Requests with AFI IDs take longer, because AWS Marketplace Seller Operations creates a copy of each AFI in every Region.
   + If you selected **AMI (standalone)**, enter the following under **AMI delivery option**:
     + **Recommended instance type** – Choose one of your product's instance types. Buyers see it labeled *Vendor recommended*, and it's selected by default when they launch.
     + **Usage instructions** – How buyers configure and run your software, or a link to those instructions, up to 4,000 characters.
     + **Security group recommendations** – At least one and up to 25 inbound rules. For each rule, choose the **Protocol** (*tcp* or *udp*), and enter the **Range start port** and **Range end port** (from 1 to 65,535). For **Comma-separated list of CIDR IPs**, enter from 1 to 5 IPv4 CIDR blocks, for example {{192.0.2.0/24}}. To add a rule, choose **Add another security group recommendation**.
     + (Optional) **Access endpoint URL** – How buyers reach your software after they launch an instance. Choose the **Protocol** (*http* or *https*), and enter the **Port** (for example, {{443}}) and the **Path** (for example, {{index.html}}). Don't begin the path with a slash. The host name depends on the instance, so you provide only the path. If you enter any of these values, the protocol and port are required.
   + If you selected **AMI with CloudFormation**, enter the following for each template under **AMI with CloudFormation delivery option**:
     + **Delivery option title** – A unique name for this delivery option, up to 72 characters.
     + **Short description** – Two or three sentences, up to 1,000 characters. Buyers must choose a *show more* link to read a description longer than 188 characters.
     + **Long description** – A detailed description, up to 3,000 characters.
     + **Usage instructions** – How buyers use the solution, or a link to those instructions, up to 4,000 characters.
     + **Recommended instance type** – The instance type that buyers get by default.
     + **CloudFormation template link** – The Amazon S3 URL of your template, for example {{https://bucket\_name.s3.amazonaws.com/template.yaml}}. For nested stacks, provide the entry point (parent) template. For more information, see [Add CloudFormation templates to your product](https://docs.aws.amazon.com/marketplace/latest/userguide/cloudformation.html).
     + **Architecture diagram link** – The Amazon S3 URL of your architecture diagram. The image must be 1560x878 or 1560x3120 pixels with a 16:9 or 1:2 ratio, and the bucket must be publicly accessible. For more information, see [Architectural diagram](https://docs.aws.amazon.com/marketplace/latest/userguide/cloudformation.html#topology-diagram).
     + **AMI parameter name** – The name of the template parameter that your EC2 instance resources use for their `ImageId` property, up to 100 letters and numbers. AWS Marketplace replaces it with an [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html) parameter that resolves to the Region-specific AMI ID of your product. For more information, see [Requirements for AMI details](https://docs.aws.amazon.com/marketplace/latest/userguide/cloudformation.html#ami-requirements-sse).

     To add another template, choose **Add another CloudFormation template**.
   + If you selected **EC2 Image Builder component**, enter the following for each component under **EC2 Image Builder component delivery option**:
     + **Component ARN** – The Amazon Resource Name (ARN) of the EC2 Image Builder component that you want to publish, for example {{arn:aws:imagebuilder:us-east-1:123456789012:component/my-component/1.0.0/1}}. The component must exist in your AWS Marketplace seller account. You can't use a component ARN that another version of this product already uses.
     + **IAM access role ARN** – The ARN of an IAM role that gives AWS Marketplace access to your component. For instructions, see [Creating the AWS Marketplace IAM role](https://docs.aws.amazon.com/marketplace/latest/developerguide/work-with-ec2-image-builder-products.html#ib-create-iam-role) in the *AWS Marketplace Developer Guide*.
     + **Usage instructions** – How buyers use the component in their Image Builder pipelines, up to 4,000 characters.
     + (Optional) **Delivery option title** – A name for this delivery option, up to 72 characters. If you leave it blank, AWS Marketplace uses the component name.

     To add another component, choose **Add another Image Builder component**. A product can use up to five different Image Builder components across its public delivery options, and you can add each component only once, regardless of its version. If you reach the limit, remove a component, or restrict a version that uses one.

1. Choose **Next**.

1. On the **Review and submit** step, choose **Submit**.

   If you selected **Test this version**, the step is **Review and test**, and the button is **Run test**.

Your change request appears on the product's **Change history** tab. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name. While a request is in progress, the actions on the **Delivery** tab are unavailable.

**Note**  
Adding a new version results in a scan of the AMI. For more information, see [Scanning your AMI for publishing requirements](best-practices-for-building-your-amis.md#self-service-scanning).

If your request is successful, your existing users receive the following email message. The message notifies them that the new version is available, links to the version's release notes, and suggests that they upgrade to the latest version. As the AWS account root user, you also receive a copy of the email message in the email account that's associated with your AWS account.

```
Greetings from AWS Marketplace,

Thank you for subscribing to <product-title>

We are writing to inform you that <seller-name> has added a new version to <product-title> on AWS Marketplace. 
As an existing customer, your subscription to the product, any running instances and access to previous versions 
are unaffected. However, <seller-name> does recommend you to update to the latest version, <product-title>/<version-title> 
by visiting <product-detail-page-of-new-listing>.

For additional questions or upgrade information, please contact <seller-name> directly. Visit <link of seller page on MP> 
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
<a name="single-ami-restricting-version"></a>

If you no longer want to offer a specific version of your public product to new subscribers, you can restrict that version.

**Note**  
All subscribers can use the current version regardless of the restriction status. AWS Marketplace guidelines require that you continue to offer support to existing buyers for 90 days after restricting the version. Your AMI will be marked as deprecated after the version is restricted. For more information, see [Deprecate an Amazon EC2 AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-deprecate.html) in the *Amazon EC2 User Guide*.

**To restrict a version**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose the **Delivery** tab.

1. In the **Versions** section, select the versions that you want to restrict.

   You can restrict only versions whose **Version visibility** is **Public**. At least one version must stay available.

1. From the **Edit** menu, choose **Restrict version**, or **Restrict versions** if you selected more than one.

   You can also choose **Restrict version** on the details page of the version.

1. In the confirmation dialog box, choose **Restrict version** or **Restrict versions**.

   You can't undo a restriction in AWS Partner Central.

Your change request appears on the product's **Change history** tab. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name. While a request is in progress, the actions on the **Delivery** tab are unavailable.

**Note**  
You can't restrict all versions of a product. If you select every public version, the restrict action is unavailable. To completely remove a product, see [Removing a product from AWS Marketplace](removing-products-from-aws-marketplace.md).

**Note**  
Restricting a version can take up to 3 days to complete.

If your request is successful, your existing users receive the following email message that notifies them of the version restriction and suggests they use the most recent version available. As the AWS account root user, you also receive a copy of the email message in the email account that's associated with your AWS account.

```
Greetings from AWS Marketplace,

Thank you for subscribing to <product-title>.

We are writing to inform you that, as of <Version-Restriction-Date>, <Seller Name> will no longer offer version(s) "<version-title>" to new subscribers. Your use and subscription is unaffected for this version(s), however it is recommended that users upgrade to the latest version on AWS Marketplace.

For additional questions or upgrade information, please contact <seller-name> directly. Visit <link of seller page on MP> to visit the seller's profile page on AWS Marketplace.

Thank you,
The AWS Marketplace Team
https://aws.amazon.com/marketplace

AWS, Inc. is a subsidiary of Amazon.com, Inc. Amazon.com is a registered trademark of Amazon.com, Inc. This message was produced and distributed by AWS Inc., 410 Terry Ave. North, Seattle, WA 98109-5210
```