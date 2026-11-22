

# Managing versions for EC2 Image Builder products on AWS Marketplace

You can manage the versions of your EC2 Image Builder component product in AWS Partner Central or with the AWS Marketplace Catalog API. In AWS Partner Central, an Image Builder component product is an AMI-based product, and each Image Builder component is a delivery option of a version.

To manage versions with the Catalog API, see the following sections in the *AWS Marketplace Developer Guide*:
+ [Add a new version](https://docs.aws.amazon.com/marketplace/latest/developerguide/work-with-ec2-image-builder-products.html#adding-new-ec2-ib-version-existing-product) 
+ [Update information about an existing version](https://docs.aws.amazon.com/marketplace/latest/developerguide/work-with-ec2-image-builder-products.html#updating-ec2-ib-product-version) 
+ [Restrict a version](https://docs.aws.amazon.com/marketplace/latest/developerguide/work-with-ec2-image-builder-products.html#restricting-ec2-ib-product-version) 

**Topics**
+ [Add a new version](#single-ib-adding-version)
+ [Update version information](#single-ib-updating-version)
+ [Restrict a version](#single-ib-restricting-version)

## Add a new version
<a name="single-ib-adding-version"></a>

Add a new version to deliver a new version of your Image Builder component. You can't change the component in an existing version.

**To add a new version**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose the **Delivery** tab.

1. In the **Versions** section, choose **Add version**.

   For a new product, you can instead choose **Start** on the **Configure version and delivery options** card under **Step 2: Delivery configuration**. On a new product, **Add version** and this card are available after you complete the **Add Regions** and **Add instance types** cards.

1. On the **Configure version** step, under **Version information**, enter the following:
   + **Version title** – A title that buyers use to tell your releases apart, for example {{1.1}}. The title can have up to 64 characters and must be unique in your product. You can't use `latest`, a space before ™, or characters other than printable ASCII characters and the symbols ©, ®, ™, ¢, £, ¤, and ¥. You can't change the title after you submit. To see your recent titles, expand **View previous version titles**.
   + **Release notes** – Details about this version, up to 30,000 characters.
   + (Optional) **Test version** – To check this version without adding it, select **Test this version**.

   The form starts with the values from your latest version, except **Component ARN** and **IAM access role ARN**. For a product that isn't in draft, **Version title** also starts blank.

1. (Optional) Under **Tags**, add tags to the change request.

1. Choose **Next**.

**To configure delivery options for a new version**

1. On the **Configure delivery options** step, under **Delivery option**, for **Delivery method**, select **EC2 Image Builder component**.

   You can also select **AMI (standalone)** or **AMI with CloudFormation** in the same version. For those fields, see [Add a new version](single-ami-versions.md#single-ami-adding-version).

   You can't add delivery options to a version after you submit it. Include every delivery option for this version in this request.
**Note**  
In the AWS European Sovereign Cloud catalog, the **EC2 Image Builder component** delivery method isn't available.

1. Under **EC2 Image Builder component delivery option**, enter the following for each component:
   + **Component ARN** – The Amazon Resource Name (ARN) of the EC2 Image Builder component that you want to publish, for example {{arn:aws:imagebuilder:us-east-1:123456789012:component/my-component/1.0.0/1}}. The component must exist in your AWS Marketplace seller account. You can't use a component ARN that another version of this product already uses.
   + **IAM access role ARN** – The ARN of an IAM role that gives AWS Marketplace access to your component. For instructions, see [Creating the AWS Marketplace IAM role](https://docs.aws.amazon.com/marketplace/latest/developerguide/work-with-ec2-image-builder-products.html#ib-create-iam-role) in the *AWS Marketplace Developer Guide*.
   + **Usage instructions** – How buyers use the component in their Image Builder pipelines, up to 4,000 characters.
   + (Optional) **Delivery option title** – A name for this delivery option, up to 72 characters. If you leave it blank, AWS Marketplace uses the component name.

   To add another component, choose **Add another Image Builder component**. A product can use up to five different Image Builder components across its public delivery options, and you can add each component only once, regardless of its version. If you reach the limit, remove a component, or restrict a version that uses one.

1. Choose **Next**.

1. On the **Review and submit** step, choose **Submit**.

   If you selected **Test this version**, the step is **Review and test**, and the button is **Run test**.

Your change request appears on the product's **Change history** tab. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name. While a request is in progress, the actions on the **Delivery** tab are unavailable.

## Update version information
<a name="single-ib-updating-version"></a>

You can update the release notes of a version, and the title and usage instructions of each Image Builder component in it.

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
   + For each **EC2 Image Builder component delivery option**: **Delivery option title** and **Usage instructions**.

   The same limits apply as when you add a version. You can't change the version title, component ARN, or IAM access role ARN. To change them, add a new version.

1. Choose **Save and submit**.

Your change request appears on the product's **Change history** tab. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name. While a request is in progress, the actions on the **Delivery** tab are unavailable.

## Restrict a version
<a name="single-ib-restricting-version"></a>

To prevent new buyers from subscribing to or deploying a version of your public product, restrict the version. Buyers with an active subscription keep access. Support them for 90 days after you restrict the version, as AWS Marketplace guidelines require.

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