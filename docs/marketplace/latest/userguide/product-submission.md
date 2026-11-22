

# Submitting your product for publication on AWS Marketplace

You use the product submission process to make your products available on AWS Marketplace. Products can be simple, such as a single Amazon Machine Image (AMI) with one price structure, or more complicated, with AWS CloudFormation templates, and complex pricing options and payment schedules. You create your product and submit it on the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central.

When you choose **Create product**, AWS Partner Central creates your product as a draft and opens its page. You then work through the steps under **Complete your listing**. When your listing is complete, choose **Publish** to submit it for review.

**Note**  
Data product providers create products in AWS Partner Central and prepare their data sets in the AWS Data Exchange console. For more information, see [Publishing a new product](https://docs.aws.amazon.com/data-exchange/latest/userguide/publishing-products.html) in the *AWS Data Exchange User Guide*.  
RTB Fabric module products are created in AWS Partner Central or with the AWS Marketplace Catalog API. For more information, see [Working with seller products](https://docs.aws.amazon.com/marketplace/latest/developerguide/work-with-seller-products.html) in the *AWS Marketplace Developer Guide*.

For the steps for your product type, see the following topics:
+ [Creating AMI-based products](ami-single-ami-products.md)
+ [EC2 Image Builder component-based products in AWS Marketplace](ec2-ib-component-products.md)
+ [Getting started with container products](container-product-getting-started.md)
+ [Listing your machine learning product in AWS Marketplace](ml-publishing-your-product-in-aws-marketplace.md)
+ [Creating a SaaS product in AWS Marketplace](saas-create-product.md)
+ [AI agent products](ai-agents-tools.md)
+ [Create a professional services product](proserv-getting-started.md#proserv-create)

To create or update several products in one request, use the AWS Marketplace Catalog API. One change set can include up to 20 changes for one or more products. For more information, see [Invoking multiple change types in one change set](https://docs.aws.amazon.com/marketplace/latest/APIReference/catalog-apis.html#multiple-change-types) in the *AWS Marketplace API Reference*.

If you have any problems making your submissions, contact the AWS Marketplace Seller Operations team on the [AWS Partner Central and Marketplace Support page](https://us-east-1.console.aws.amazon.com/partnercentral/support?region=us-east-1).

**Topics**
+ [Using the Products and services page](#using-the-products-tab)
+ [Company and product logo requirements](#seller-and-product-logos)
+ [Requirements for submitting paid repackaged software](#paid-repackaged-software)
+ [Requirements for products with a hardware component](#product-requirements-hardware)
+ [Submitting AMI products with CloudFormation templates](#aws-cloudformation-launched-product-free-or-paid-or-usage-based-paid-ami-product)
+ [Product changes and updates](#product-changes-and-updates)
+ [Timing and expectations](#timing-and-expectations)
+ [Submitting AMIs to AWS Marketplace](#submitting-amis-to-aws-marketplace)
+ [Final checklist](#final-checklist)

## Using the Products and services page
<a name="using-the-products-tab"></a>

The [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central lists your products and their visibility. To create a product, choose **Create product**. To work on an existing product, choose it.

A product's visibility controls who can view and buy it:
+ **Draft** – You're still setting up the product. Complete the product details and, for products with a delivery step, the delivery configuration to move it to **Limited**.
+ **Limited** – Your account and the accounts on your allowlist can view the product, so you can test it. To preview your listing, choose **View on AWS Marketplace** on the product's page.
+ **Public** – Any AWS Marketplace buyer can find and buy the product.
+ **Restricted** – New buyers can't see or buy the product. Existing subscribers keep access, but they can't renew their contracts.

When you choose **Publish** and submit your listing for review, AWS Marketplace reviews it against its policies. Automated checks can approve it within hours. If a check flags your listing, the review usually takes 3 to 5 business days. After AWS Marketplace approves your listing, any AWS Marketplace buyer can find and buy your product.

Each change to your product, such as new product details, Regions, or a version, is a change request. You track your product's change requests on its **Change history** tab. Each request has one of the following statuses:
+ **Preparing** – AWS Marketplace is reviewing your request.
+ **Applying** – AWS Marketplace is applying the change to your product.
+ **Succeeded** – The change is applied to your product.
+ **Failed** – The change wasn't applied. To see why, choose the request name.
+ **Cancelled** – You cancelled the request.

To cancel a request while its status is **Preparing**, choose the request name on the **Change history** tab, and then choose **Cancel request**. While a request is in progress, you can't submit another change to the same product until the request completes.

Changes to your public offer, such as new prices, appear on the offer's **Requests log** tab. For more information, see [Changing prices](pricing.md#changing-prices).

To add your product in an AWS GovCloud (US) Region, you must have an active AWS GovCloud (US) account that AWS Marketplace has verified, and comply with the AWS GovCloud (US) requirements, including export control requirements. If your account isn't verified, a request that adds an AWS GovCloud (US) Region fails. To request verification, choose **submit a support request** in the **AWS GovCloud (US) Region selection** alert on the **Add Regions** page. For more information, see [AWS GovCloud (US) Sign Up](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/getting-started-sign-up.html) in the *AWS GovCloud (US) User Guide*.

## Company and product logo requirements
<a name="seller-and-product-logos"></a>

Your company logo and the logo for your products must conform to the following AWS Marketplace guidelines so that the user experience is uniform when browsing AWS Marketplace: 

 **Product logo specifications** – Your product logo image should have a transparent or white background and be 120 to 640 pixels in size, with a 1:1 or 2:1 (wide) ratio. 

 **Company logo specifications** – Your company logo image should have a transparent background and be 220 x 220 pixels in size, allowing for 10 pixels of padding on each side within. 

## Requirements for submitting paid repackaged software
<a name="paid-repackaged-software"></a>

Before you can submit a listing for repackaged software, you must meet the following requirements. In this case, *Repackaged software* includes open-source AMIs or software created by another vendor, such as an AMI with Windows.

**Requirements**
+ The product must include tangible intellectual property beyond the original software. You cannot publish listings that only add support services, such as maintenance or troubleshooting, without additional software libraries, hardening, other technical modifications, or explicit permission from AWS Marketplace. To offer your support services, we recommend using [Professional services products in AWS Marketplace](proserv-products.md).
+ The product title must indicate the value added by your repackaging. Examples of product titles include: *Hardened <Product>*, *<Product> with added packages*, or *<Product1> on <Product2>*.
+ The product title must not contain any other language that is not otherwise supported with documentation. For example, the product title may not use the words *certified*, *original*, or *free* unless these are substantiated in the product details that you provide.
+ The product short description must include a clear statement summarizing the product charges. The short description must begin with the phrase *This is a repackaged open source software product wherein additional charges apply for...*. For example: *This is a repackaged open source software product wherein additional charges apply for a pre-hardened, CIS-benchmarked image*. Then, the long description must include a clear statement summarizing what you are charging for, as well as additional details describing those features.
+ The product logo must be same as the company logo that was used during your seller registration process. The product logo can differ from your company logo only if you use the official software logo, whereby you must receive explicit permission from the original software vendor. If you received explicit permission, provide the documentation to AWS Marketplace.
+ For AMI products, the AMI name must not be reused from the original product. The AMI name must begin with the seller name and follow this format: [Seller Name] [name-given-to-ami].

  If the AMI name does not adhere to the naming convention, you can copy the AMI from the AWS console and rename it. For more information, see [Copy an Amazon EC2 AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/CopyingAMIs.html), in the *Amazon EC2 User Guide*.

## Requirements for products with a hardware component
<a name="product-requirements-hardware"></a>

The sale of hardware products isn't permitted on AWS Marketplace. If you're submitting a software product that requires a hardware component (for example, a SIM card, smart device, IoT device, or sensor), you must meet the following requirements:
+ The hardware component can't be sold on AWS Marketplace.
+ The cost of the hardware component can't be included in the listing price of your product.
+ The **Product Overview** section of the listing must include the following statements: *Any hardware that may be required with this listing must be obtained separately. Review the product details for more information.*

## Submitting AMI products with CloudFormation templates
<a name="aws-cloudformation-launched-product-free-or-paid-or-usage-based-paid-ami-product"></a>

Buyers deploy an AMI with CloudFormation product from an CloudFormation template that launches your AMI and other AWS resources. You create it as an AMI-based product, and add versions that use the **AMI with CloudFormation** delivery method. A version can have one AMI delivery option and up to three CloudFormation template delivery options.

To submit an AMI with CloudFormation product, use the following sections:
+ [Choosing a pricing model](#define-pricing-model)
+ [Creating an AMI with CloudFormation product](#submitting-your-product)
+ [Providing your product information](#completing-plf)
+ [Submitting your product for review](#submit-plf)

### Choosing a pricing model
<a name="define-pricing-model"></a>

The pricing model controls which prices you enter for your product. You set it when you create the public offer for your product in **Step 3: Procurement configuration**. For AMI-based products, you can choose **Hourly**, **Usage pricing**, **Contract pricing**, **Free**, or **Bring your own license (BYOL)**. For details about each model, see [AMI product pricing for AWS Marketplace](pricing-ami-products.md).

### Creating an AMI with CloudFormation product
<a name="submitting-your-product"></a>

Create the product as described in [Create the listing](ami-single-ami-products.md#ami-create-product). For **Software type**, choose **AMI-based**.

On the **Configure version and delivery options** card, for **Delivery method**, select **AMI with CloudFormation**, and then enter the details for each template. For the fields, see [Add a new version](single-ami-versions.md#single-ami-adding-version). For template requirements, see [Add CloudFormation templates to your product](cloudformation.md).

### Adding CloudFormation templates to an existing product
<a name="download-existing-plf"></a>

To add CloudFormation templates to an existing AMI-based product, add a new version that uses the **AMI with CloudFormation** delivery method. You can't add a delivery option to a version after you submit it. For the procedure, see [Add a new version](single-ami-versions.md#single-ami-adding-version).

The form starts with values from your latest version. Enter the **Version title**, **Amazon Machine Image (AMI) ID**, **IAM access role ARN**, and each template's **AMI parameter name**.

### Providing your product information
<a name="completing-plf"></a>

You enter your product information in the steps under **Complete your listing** on the product's page:
+ In **Step 1: Product details**, you enter the product title, SKU, descriptions, highlights, logo, categories, keywords, and support details. For more information, see [Updating AMI-based product information on AWS Marketplace](single-ami-updating-product.md). For logo requirements, see [Company and product logo requirements](#seller-and-product-logos).
+ In **Step 2: Delivery configuration**, you complete the following cards:
  + On the **Add Regions** card, you choose the Regions where buyers can deploy your product. For more information, see [Add an AWS Region](single-ami-regions.md#single-ami-adding-regions). AWS GovCloud (US) Regions have extra requirements. For example, you must have an active AWS GovCloud (US) account that AWS Marketplace has verified. If your account isn't verified, a request that adds an AWS GovCloud (US) Region fails. To request verification, choose **submit a support request** in the **AWS GovCloud (US) Region selection** alert on the **Add Regions** page. For more information, see [Getting set up](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/getting-set-up.html) in the *AWS GovCloud (US) User Guide*.
  + On the **Add instance types** card, you choose the instance types that buyers can use. For more information, see [Adding an instance](single-ami-instance-types.md#single-ami-adding-instance-types).
  + On the **Configure version and delivery options** card, you enter the version, your AMI details, and each CloudFormation template with its title, descriptions, template link, architecture diagram, AMI parameter name, usage instructions, and recommended instance type. For the fields, see [Add a new version](single-ami-versions.md#single-ami-adding-version).

    To give AWS Marketplace access to your AMI, see [Giving AWS Marketplace access to your AMI](single-ami-marketplace-ami-access.md). Usage instructions must meet the requirements in [Creating AMI and container product usage instructions for AWS Marketplace](ami-container-product-usage-instructions.md). Architecture diagrams must meet the requirements in [Architectural diagram](cloudformation.md#topology-diagram).
+ In **Step 3: Procurement configuration**, you create your public offer, with its pricing, the countries where buyers can buy your product, the EULA, and the refund policy. For more information, see [AMI product pricing for AWS Marketplace](pricing-ami-products.md), [Update availability by country](single-ami-regions.md#single-ami-update-availability-by-country), [Updating end user license agreement (EULA) for your AMI-based AWS Marketplace product](single-ami-update-eula.md), and [Updating the refund policy for your AMI-based product on AWS Marketplace](single-ami-update-refund-policy.md). For the standard EULA, see [Using standardized contracts in AWS Marketplace](standardized-license-terms.md).

### Submitting your product for review
<a name="submit-plf"></a>

When your listing is complete, choose **Publish**, and then choose **Submit for review**. For the full procedure, see [Create the listing](ami-single-ami-products.md#ami-create-product).

AWS Marketplace reviews your listing against its policies before it goes live. Automated checks can approve it within hours. If a check flags your listing, the review usually takes 3 to 5 business days. After AWS Marketplace approves your listing, any AWS Marketplace buyer can find and buy your product.

### Updating your product
<a name="updating-your-product"></a>

You update an AMI with CloudFormation product the same way as other AMI-based products. Product updates appear on the product's **Change history** tab, and price changes appear on the offer's **Requests log** tab. For the procedures, see the following topics:
+ [Add a new version](single-ami-versions.md#single-ami-adding-version)
+ [Update version information](single-ami-versions.md#single-ami-updating-version)
+ [Restrict a version](single-ami-versions.md#single-ami-restricting-version)
+ [Changing prices](pricing.md#changing-prices)
+ [Adding and restricting AMI instances for AWS Marketplace](single-ami-instance-types.md)
+ [Managing AMI-based product availability by AWS Region and country](single-ami-regions.md)
+ [Updating AMI-based product information on AWS Marketplace](single-ami-updating-product.md)

In an existing version, you can update each template's title, descriptions, usage instructions, recommended instance type, and architecture diagram. To use a different CloudFormation template, add a new version.

## Product changes and updates
<a name="product-changes-and-updates"></a>

Sellers can submit changes to their product at any time, and they will be processed as described earlier. However, some changes can only be made every 90 or 120 days, or when pending changes are in place. Examples include price changes and AWS Region or instance type changes. Common changes include: 
+  **New version** – New versions of the software and roll outs of patches or updates. At your request, we can notify customers who have subscribed to your AWS Marketplace content about the availability of new versions or send upgrade instructions on your behalf. For more information, see [Add a new version](single-ami-versions.md#single-ami-adding-version).
+  **Product information change** – Changes to your product details, such as descriptions and URLs, and to each version's usage instructions. For more information, see [Updating AMI-based product information on AWS Marketplace](single-ami-updating-product.md) and [Update version information](single-ami-versions.md#single-ami-updating-version).
+  **Price change** – A change to the prices in your public offer. Price decreases take effect immediately. For a price increase, AWS Marketplace notifies existing buyers after the request is complete. The new price takes effect for them on the first day of the month after a 90-day notice period. For example, if you increase a price on March 16, the new price takes effect on July 1. New buyers pay the updated price immediately. For more information, see [Changing prices](pricing.md#changing-prices).
+  **Pricing model change** – You can't change the pricing model after you create the public offer for your product. To use a different pricing model, create a new product, and encourage current customers to migrate to it.
+  **Region or instance type change** – Adding or restricting instance types or Regions. For more information, see [Adding and restricting AMI instances for AWS Marketplace](single-ami-instance-types.md) and [Managing AMI-based product availability by AWS Region and country](single-ami-regions.md).
+  **Product removal** – Remove a product from AWS Marketplace to prevent new customers from subscribing. A notification to current customers is sent after the request is complete. For more information, see [Removing a product from AWS Marketplace](removing-products-from-aws-marketplace.md).

## Timing and expectations
<a name="timing-and-expectations"></a>

While we strive to process requests as quickly as possible, requests can require multiple iterations and review by the seller and the AWS Marketplace team. Use the following as guidance for the time needed to complete the process: 
+ Total request time normally takes 2–4 calendar weeks. More complex requests or products can take longer, due to multiple iterations and adjustments to product metadata and software.
+ We require a completed product request and AMI at least 45 days in advance of any planned events or releases, so we can prioritize the request accordingly.

If you have questions about your request, contact the AWS Marketplace support team on the AWS Partner Central and Marketplace Support page. 

## Submitting AMIs to AWS Marketplace
<a name="submitting-amis-to-aws-marketplace"></a>

All AMIs built and submitted to AWS Marketplace must adhere to all product policies. We suggest a few final checks of your AMI before submission: 
+ Remove all user credentials from the system; for example, all default passwords, authorization keys, key pairs, security keys or other credentials. 
+ Ensure that root login is disabled or locked. Only sudo access accounts are allowed. 
+ If you are submitting an AMI to be deployed into the AWS GovCloud (US) Region, you need an active [AWS GovCloud (US) account](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/getting-started-sign-up.html) that AWS Marketplace has verified, and you must agree to the [AWS GovCloud Requirements](https://aws.amazon.com/service-terms/) on the AWS website, including applicable export control requirements. To request verification, choose **submit a support request** in the **AWS GovCloud (US) Region selection** alert on the **Add Regions** page.

### AMI self-service scanning
<a name="ami-self-service-scanning"></a>

AWS Marketplace offers AMI scanning within AWS Partner Central. For new products, the system automatically runs a scan and provides results upon submission. For new versions of existing products, start a scan by selecting **Test this version** when you add the version. This process typically completes in less than an hour and delivers comprehensive feedback in a single, convenient location.

**To scan your AMI**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. On the **Delivery** tab, in the **Versions** section, choose **Add version**.

   For a new product, you can instead choose **Start** on the **Configure version and delivery options** card under **Step 2: Delivery configuration**. On a new product, **Add version** and this card are available after you complete the **Add Regions** and **Add instance types** cards.

1. On the **Configure version** step, enter the version information.

1. Under **Test version**, select **Test this version**.

1. Choose **Next**.

**To configure delivery options for an AMI scan**

1. On the **Configure delivery options** step, enter your AMI details and any CloudFormation templates.

   A test checks every field, so complete the step as you would for a new version. For the fields, see [Add a new version](single-ami-versions.md#single-ami-adding-version).

1. Choose **Next**.

1. On the **Review and test** step, choose **Run test**.

Your test appears on the product's **Change history** tab as **Test add version {{version-title}}**. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. If the status is **Succeeded**, your AMI passed scanning. To see why a request failed, choose the request name.

A test doesn't add a version, and your live listing doesn't change.

To publish a scanned AMI, add the version again without selecting **Test this version**. If you have any issues, contact the AWS Marketplace Seller Operations team on the AWS Partner Central and Marketplace Support page.

Your AMI must be in the `us-east-1` (N. Virginia) Region and owned by your AWS Marketplace seller account. If you need to grant other accounts access to AWS Partner Central, you must register those accounts as sellers. For more information, see [Registration process](registration-process.md). 

### AMI cloning and product code assignment
<a name="ami-cloning-and-product-code-assignment"></a>

After your AMI is submitted, AWS Marketplace creates cloned AMIs for each Region that you have indicated that software should be available in. During this cloning and publishing process, AWS Marketplace attaches a product code to the cloned AMIs. The product code is used to both control access and to meter usage. All submissions must go through this AMI cloning process. 

## Final checklist
<a name="final-checklist"></a>

To help avoid delays in publishing your product, use this checklist before you submit your product request. 

 **Product usage** 
+ Production-ready. 
+ Does not restrict product usage by time or other restrictions. 
+ Compatible with 1-click fulfillment experience. 
+ The software contains everything required to use the product, including client applications. 
+ Default user uses a randomized password and/or creation of initial user requires verification that the buyer is authorized to use the instance using a value unique to the instance such as instance ID. 

 **For free or paid products** 
+ No additional license is required to use the product. 
+ Paid repackaged software meets the AWS Marketplace [Requirements for submitting paid repackaged software](#paid-repackaged-software).
+ Buyer does not have to provide personally identifiable information (for example, an email address) to use the product. 

**AMI preparation**
+ Use hardware virtual machine (HVM) virtualization and 64-bit architecture. 
+ Does not contain any known vulnerabilities, malware, or viruses. 
+ Buyers have operating system-level administration access to the AMI. 
+ Scan your AMI with **Test this version** when you add a version. For more information, see [AMI self-service scanning](#ami-self-service-scanning).

 **For Windows AMIs** 
+ Use the most recent version of `Ec2ConfigService`, as described in [Configuring a Windows instance using the EC2Config service](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ec2config-service.html) in the *Amazon EC2 User Guide*. 
+ The `Ec2SetPassword`, `Ec2WindowsActivate`, and `Ec2HandleUserData` plugins are enabled, as described in [Configuring a Windows instance using the EC2Config service](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ec2config-service.html) in the *Amazon EC2 User Guide*.
+ No Guest Accounts or Remote Desktop Users are present. 

 **For Linux AMIs** 
+ Root login is locked and disabled. 
+ No authorized keys, default passwords, or other credentials are included. 
+ All required fields are completed. 
+ All values are within specified character limits. 
+ All URLs load without error. 
+ Product logo is 120 to 640 pixels wide and tall, with a 1:1 or 2:1 (wide) ratio. 
+ Pricing is specified for every instance type that you select (for the **Hourly** pricing model). 

If you have questions or comments about automated AMI building, contact the AWS Marketplace support team on the AWS Partner Central and Marketplace Support page. 