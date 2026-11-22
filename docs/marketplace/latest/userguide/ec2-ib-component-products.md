

# EC2 Image Builder component-based products in AWS Marketplace

As an AWS Marketplace seller, you can deliver your products to buyers with [Image Builder components](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html#image-builder). An Image Builder component is a fundamental building block used in the Image Builder service to create and maintain customized EC2 Image Builder components. Components are reusable, modular pieces of configuration that define a specific set of tasks to be performed during the image creation process.

A component defines the sequence of steps required to either customize an instance before image creation (a build component), or to test an instance that was launched from the created image (a test component). An Image builder component may consist of three items:
+ The component document, a declarative, YAML or JSON file that specifies the steps and actions to be run when the component is used to build an image.
+ Component attributes that provide the configuration options for a component. They help define the component's characteristics, behavior, and compatibility.
+ Software packages, the dependencies that must be installed for the component to function correctly.

You can publish Image Builder components on AWS Marketplace in AWS Partner Central or with the AWS Marketplace Catalog API. In AWS Partner Central, an Image Builder component product is an AMI-based product. You add each Image Builder component as an **EC2 Image Builder component** delivery option when you add a version. You can add up to 5 Image Builder components to a product. A version can also include **AMI (standalone)** and **AMI with CloudFormation** delivery options.

Before you publish, build and test your component, and create the IAM role that gives AWS Marketplace access to it. For instructions, see [Building and testing your Image Builder component](https://docs.aws.amazon.com/marketplace/latest/developerguide/work-with-ec2-image-builder-products.html#build-and-test-ib-component) and [Creating the AWS Marketplace IAM role](https://docs.aws.amazon.com/marketplace/latest/developerguide/work-with-ec2-image-builder-products.html#ib-create-iam-role) in the *AWS Marketplace Developer Guide*.

**To create an Image Builder component product**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose **Create product**.

1. Under **Product details**, for **Product name**, enter the name that buyers see on your listing and in AWS Marketplace search results.

   The name must be 2 to 72 characters and unique. **Catalog** shows the catalog that you create the product in.

1. For **Product type**, choose **Software**.

1. For **Software type**, choose **AMI-based**.

   This type covers standalone AMIs, AMIs with CloudFormation, and EC2 Image Builder components.

1. (Optional) Under **Tags**, add tags to your product.

1. Choose **Create product**.

   AWS Partner Central creates the product as a draft and opens its page, which shows **Complete your listing**.

**To complete product details and delivery configuration**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Complete **Step 1: Product details**.

1. Under **Step 2: Delivery configuration**, complete the **Add Regions**, **Add instance types**, and **Configure version and delivery options** cards, in that order.

   Each card is available after you complete the one before it. For the fields on each card, see [Add an AWS Region](single-ib-regions.md#single-ib-adding-regions), [Adding an instance](single-ib-instance-types.md#single-ib-adding-instance-types), and [Add a new version](single-ib-versions.md#single-ib-adding-version).

   The version that you add on the last card uses the **EC2 Image Builder component** delivery method. A version that has only Image Builder components still needs Regions and instance types.

1. Choose **Advance to procurement configuration**.

1. In the **Transition to Limited** dialog box, choose **Confirm and continue**.

   Your product is now in the **Limited** state, and you can test it with allowlisted accounts.

**To publish an Image Builder component product**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Complete **Step 3: Procurement configuration** and **Step 4: Testing and integrations**.

   You can publish without completing steps marked optional, such as **Step 5: Add-ons**.

1. Choose **Publish**.

1. In the confirmation dialog box, choose **Submit for review**.

AWS Marketplace reviews your listing against its policies before it goes live. Automated checks can approve it within hours. If a check flags your listing, the review usually takes 3 to 5 business days.

**Note**  
The **EC2 Image Builder component** delivery method isn't available in the AWS European Sovereign Cloud catalog.

To publish your component with the AWS Marketplace Catalog API, see [Work with EC2 Image Builder component products](https://docs.aws.amazon.com/marketplace/latest/developerguide/work-with-ec2-image-builder-products.html#publishing-ib-component-listing) in the *AWS Marketplace Developer Guide*.