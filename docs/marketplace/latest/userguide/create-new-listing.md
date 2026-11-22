

# Creating and publishing your listing

To list a machine learning product, you create the product, add its details and first version, and create a public offer. Then you test the product and submit it for review.

**Note**  
 Before creating your listing, ensure that you have the required resources specified in [Requirements and best practices for creating machine learning products](ml-listing-requirements-and-best-practices.md). 

**To create a machine learning product**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose **Create product**.

1. On the **Create product** page, for **Product name**, enter a unique name of 2 to 72 characters.

   Buyers see this name at the top of your product listing page and in search results.

1. For **Product type**, choose **Software**.

1. For **Software type**, choose **Machine learning**.

1. (Optional) Under **Tags**, add tags for the product. For more information, see [Tagging AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html).

1. Choose **Create product**.

AWS Partner Central creates your product with **Draft** visibility and opens its overview page. The **Complete your listing** progress bar shows the steps that remain.

**To complete product details and delivery configuration**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Complete **Step 1: Product details**.

1. Under **Step 2: Delivery configuration**, complete the **Add version** card. For the procedure, see [Adding the initial version](add-initial-version.md).

   The **Prepare your product in SageMaker AI** card is optional.

1. Choose **Advance to procurement configuration**.

1. In the **Transition to Limited** dialog box, choose **Confirm and continue**.

   Your product is now in the **Limited** state, and you can test it with allowlisted accounts.

**To create a public offer for a machine learning product**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Under **Step 3: Procurement configuration**, on the **Create public offer** card, choose **Start**.

   You can instead choose the **Procurement** tab, and then choose **Create public offer**. Both are available after your product has **Limited** visibility.

1. On the **Set pricing model** page, choose **Free**, **Usage - hourly**, or **Usage - per inference request**, and then choose **Next**.

   You can't change the pricing model later. For help choosing, see [Machine learning product pricing for AWS Marketplace](machine-learning-pricing.md).

1. On the **Configure pricing details and duration** page, enter your prices.

   With **Usage - hourly**, you set an hourly price for each instance type. With **Usage - per inference request**, you set a price per inference for real-time inference, and an hourly price for each instance type for batch transform and, for algorithms, training.

1. (Optional) To offer a free trial, select **Free trial**, and then choose a **Trial period** of 5 to 31 days.

   The free trial option appears only for a paid pricing model.

1. Choose **Next**.

**To complete the public offer**

1. On the **Specify refund policy** page, under **Refund policy**, enter the terms of your policy and the contact information that buyers use to request a refund, and then choose **Next**.

   The policy can have up to 500 characters.

1. On the **Configure legal terms and offer documents** page, for **Legal terms**, choose **Standard Contract for AWS Marketplace (SCMP)** or **Custom legal terms**, and then choose **Next**.

   With **Custom legal terms**, you upload your own end-user license agreement (EULA).

1. On the **Configure offer availability** page, for **Offer availability by country**, choose **All countries**, **All countries with exclusions**, or **Allowlisted countries only**, and then choose **Next**.

1. On the **Review and create** page, choose **Create public offer**.

   To change a page before you submit, choose **Edit** in its section.

AWS Partner Central returns you to the product's **Procurement** tab. While your request is in progress, the **Create public offer** card shows **Pending**. When the offer is created, the card shows **Complete**.

To finish your offer later, choose **Save and exit** on any page after **Set pricing model**. To continue, choose **Edit** on the **Create public offer** card.

**To publish a machine learning product**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Under **Step 4: Testing and integrations**, add the AWS accounts that test your product to the allowlist. For more information, see [Updating the allowlist](ml-update-allowlist.md).

   **Step 5: Add-ons** is optional. It holds add-ons that you can configure for your listing and buyer experience.

1. Test your product, and make sure that it meets the requirements in [Requirements and best practices for creating machine learning products](ml-listing-requirements-and-best-practices.md).

1. Choose **Publish**.

1. In the confirmation dialog box, choose **Submit for review**.